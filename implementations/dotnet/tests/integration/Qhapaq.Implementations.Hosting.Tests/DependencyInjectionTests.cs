using Microsoft.Extensions.DependencyInjection;
using Qhapaq.Implementations.Hosting.DependencyInjection;

namespace Qhapaq.Implementations.Hosting.Tests;

public sealed class DependencyInjectionTests
{
    [Fact]
    public void AddQhapaq_BuildsWithScopeValidation()
    {
        var services = new ServiceCollection();

        services.AddQhapaq();

        using ServiceProvider provider = services.BuildServiceProvider(
            new ServiceProviderOptions
            {
                ValidateOnBuild = true,
                ValidateScopes = true,
            });
    }
}
