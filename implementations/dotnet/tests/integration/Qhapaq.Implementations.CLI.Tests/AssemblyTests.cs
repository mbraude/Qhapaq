using System.Reflection;

namespace Qhapaq.Implementations.CLI.Tests;

public sealed class AssemblyTests
{
    [Fact]
    public void CliAssembly_UsesExpectedName()
    {
        Assembly assembly = Assembly.Load("Qhapaq.Implementations.CLI");

        Assert.Equal("Qhapaq.Implementations.CLI", assembly.GetName().Name);
        Assert.Empty(assembly.GetExportedTypes());
    }
}
