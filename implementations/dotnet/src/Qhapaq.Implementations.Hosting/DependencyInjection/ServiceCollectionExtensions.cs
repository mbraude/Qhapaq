using Microsoft.Extensions.DependencyInjection;
using Qhapaq.Service.V1.DependencyInjection;

namespace Qhapaq.Implementations.Hosting.DependencyInjection;

/// <summary>
/// Provides the supported composition entry point for Qhapaq hosts.
/// </summary>
public static class ServiceCollectionExtensions
{
    /// <summary>
    /// Adds Qhapaq application services to a service collection.
    /// </summary>
    /// <param name="services">The service collection to update.</param>
    /// <returns>The supplied service collection.</returns>
    public static IServiceCollection AddQhapaq(this IServiceCollection services)
    {
        ArgumentNullException.ThrowIfNull(services);
        services.AddQhapaqServiceV1();
        return services;
    }
}
