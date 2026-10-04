using System.Reflection;

namespace Qhapaq.Business.Tests;

public sealed class AssemblyTests
{
    [Fact]
    public void BusinessAssembly_UsesExpectedName()
    {
        Assembly assembly = Assembly.Load("Qhapaq.Business");

        Assert.Equal("Qhapaq.Business", assembly.GetName().Name);
        Assert.Empty(assembly.GetExportedTypes());
    }
}
