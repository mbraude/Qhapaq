using System.Reflection;

namespace Qhapaq.Service.V1.Tests;

public sealed class AssemblyTests
{
    [Fact]
    public void ServiceAssembly_UsesExpectedName()
    {
        Assembly assembly = Assembly.Load("Qhapaq.Service.V1");

        Assert.Equal("Qhapaq.Service.V1", assembly.GetName().Name);
    }
}
