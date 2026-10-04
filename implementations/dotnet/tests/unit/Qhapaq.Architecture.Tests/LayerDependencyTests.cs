using System.Reflection;
using System.Xml.Linq;
using Microsoft.Extensions.DependencyInjection;

namespace Qhapaq.Architecture.Tests;

public sealed class LayerDependencyTests
{
    /// <summary>
    /// The permitted direct project references for each production assembly.
    /// </summary>
    private static readonly IReadOnlyDictionary<string, string[]> AllowedProjectReferences =
        new Dictionary<string, string[]>(StringComparer.Ordinal)
        {
            ["Qhapaq.Abstractions"] = [],
            ["Qhapaq.DAL"] = ["Qhapaq.Abstractions"],
            ["Qhapaq.Business"] = ["Qhapaq.Abstractions", "Qhapaq.DAL"],
            ["Qhapaq.Service.V1"] = ["Qhapaq.Abstractions", "Qhapaq.Business"],
            ["Qhapaq.Implementations.Hosting"] = ["Qhapaq.Service.V1"],
            ["Qhapaq.Implementations.MCP"] =
                ["Qhapaq.Abstractions", "Qhapaq.Implementations.Hosting"],
            ["Qhapaq.Implementations.CLI"] =
                ["Qhapaq.Abstractions", "Qhapaq.Implementations.Hosting"],
        };

    [Fact]
    public void ProductionProjects_ReferenceOnlyPermittedProjects()
    {
        string sourceDirectory = Path.Combine(FindSolutionDirectory(), "src");

        foreach ((string projectName, string[] expectedReferences) in AllowedProjectReferences)
        {
            string projectPath = Path.Combine(
                sourceDirectory,
                projectName,
                $"{projectName}.csproj");
            var project = XDocument.Load(projectPath);

            string[] actualReferences = project
                .Descendants("ProjectReference")
                .Select(reference => reference.Attribute("Include")?.Value)
                .Where(static include => include is not null)
                .Select(static include => Path.GetFileNameWithoutExtension(include))
                .Order(StringComparer.Ordinal)
                .ToArray()!;

            Assert.Equal(expectedReferences.Order(StringComparer.Ordinal), actualReferences);
        }
    }

    [Fact]
    public void ProductionAssemblies_HaveExpectedNames()
    {
        foreach (string projectName in AllowedProjectReferences.Keys)
        {
            Assembly assembly = Assembly.Load(new AssemblyName(projectName));

            Assert.Equal(projectName, assembly.GetName().Name);
            Assert.All(
                assembly.GetTypes().Where(static type => type.Namespace is not null),
                type => Assert.StartsWith(projectName, type.Namespace, StringComparison.Ordinal));
        }
    }

    [Fact]
    public void ProductionAssemblies_ReferenceOnlyPermittedQhapaqAssemblies()
    {
        foreach ((string assemblyName, string[] expectedReferences) in AllowedProjectReferences)
        {
            Assembly assembly = Assembly.Load(new AssemblyName(assemblyName));
            string[] actualReferences = assembly
                .GetReferencedAssemblies()
                .Select(static reference => reference.Name)
                .Where(static name =>
                    name is not null &&
                    name.StartsWith("Qhapaq.", StringComparison.Ordinal))
                .Order(StringComparer.Ordinal)
                .ToArray()!;

            Assert.Subset(
                expectedReferences.ToHashSet(StringComparer.Ordinal),
                actualReferences.ToHashSet(StringComparer.Ordinal));
        }
    }

    [Fact]
    public void InternalLayers_DoNotExposePublicTypes()
    {
        string[] internalAssemblies =
        [
            "Qhapaq.Business",
            "Qhapaq.DAL",
            "Qhapaq.Implementations.CLI",
            "Qhapaq.Implementations.MCP",
        ];

        foreach (string assemblyName in internalAssemblies)
        {
            Assembly assembly = Assembly.Load(new AssemblyName(assemblyName));
            Assert.Empty(assembly.GetExportedTypes());
        }
    }

    [Fact]
    public void CompositionAssemblies_ExposeOnlyRegistrationEntryPoints()
    {
        IReadOnlyDictionary<string, string> expectedTypes =
            new Dictionary<string, string>(StringComparer.Ordinal)
            {
                ["Qhapaq.Service.V1"] =
                    "Qhapaq.Service.V1.DependencyInjection.ServiceCollectionExtensions",
                ["Qhapaq.Implementations.Hosting"] =
                    "Qhapaq.Implementations.Hosting.DependencyInjection.ServiceCollectionExtensions",
            };

        foreach ((string assemblyName, string expectedType) in expectedTypes)
        {
            Assembly assembly = Assembly.Load(new AssemblyName(assemblyName));
            Type publicType = Assert.Single(assembly.GetExportedTypes());

            Assert.Equal(expectedType, publicType.FullName);
        }
    }

    [Fact]
    public void BehavioralTypes_DoNotDependOnDependencyInjectionContainers()
    {
        Type[] prohibitedTypes =
        [
            typeof(IServiceCollection),
            typeof(IServiceProvider),
            typeof(IServiceScopeFactory),
        ];

        foreach (string assemblyName in AllowedProjectReferences.Keys)
        {
            Assembly assembly = Assembly.Load(new AssemblyName(assemblyName));
            IEnumerable<Type> behavioralTypes = assembly
                .GetTypes()
                .Where(static type =>
                    type.Namespace is not null &&
                    !type.Namespace.EndsWith(".DependencyInjection", StringComparison.Ordinal));

            foreach (Type type in behavioralTypes)
            {
                IEnumerable<Type> dependencies = GetDeclaredDependencyTypes(type);
                Assert.DoesNotContain(
                    dependencies,
                    dependency => prohibitedTypes.Contains(dependency));
            }
        }
    }

    private static IEnumerable<Type> GetDeclaredDependencyTypes(Type type)
    {
        const BindingFlags flags =
            BindingFlags.Public |
            BindingFlags.NonPublic |
            BindingFlags.Instance |
            BindingFlags.Static |
            BindingFlags.DeclaredOnly;

        IEnumerable<Type> constructorDependencies = type
            .GetConstructors(flags)
            .SelectMany(static constructor => constructor.GetParameters())
            .Select(static parameter => parameter.ParameterType);

        IEnumerable<Type> methodDependencies = type
            .GetMethods(flags)
            .SelectMany(static method =>
                method.GetParameters()
                    .Select(static parameter => parameter.ParameterType)
                    .Append(method.ReturnType));

        IEnumerable<Type> fieldDependencies = type
            .GetFields(flags)
            .Select(static field => field.FieldType);

        return constructorDependencies
            .Concat(methodDependencies)
            .Concat(fieldDependencies)
            .SelectMany(ExpandType);
    }

    private static IEnumerable<Type> ExpandType(Type type)
    {
        yield return type;

        foreach (Type genericArgument in type.GetGenericArguments())
        {
            foreach (Type expandedType in ExpandType(genericArgument))
            {
                yield return expandedType;
            }
        }
    }

    private static string FindSolutionDirectory()
    {
        DirectoryInfo? directory = new(AppContext.BaseDirectory);

        while (directory is not null)
        {
            if (File.Exists(Path.Combine(directory.FullName, "Qhapaq.slnx")))
            {
                return directory.FullName;
            }

            directory = directory.Parent;
        }

        throw new DirectoryNotFoundException(
            "Could not locate Qhapaq.slnx from the test output directory.");
    }
}
