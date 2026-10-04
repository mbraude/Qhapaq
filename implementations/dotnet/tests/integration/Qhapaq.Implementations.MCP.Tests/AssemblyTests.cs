using System.Reflection;

namespace Qhapaq.Implementations.MCP.Tests;

public sealed class AssemblyTests
{
    [Fact]
    public void McpAssembly_UsesExpectedName()
    {
        Assembly assembly = Assembly.Load("Qhapaq.Implementations.MCP");

        Assert.Equal("Qhapaq.Implementations.MCP", assembly.GetName().Name);
        Assert.Empty(assembly.GetExportedTypes());
    }
}
