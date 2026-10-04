using Microsoft.Extensions.DependencyInjection;
using Qhapaq.Business.DependencyInjection;

namespace Qhapaq.Service.V1.DependencyInjection;

/// <summary>
/// Registers the version 1 Qhapaq service layer and its lower-layer dependencies.
/// </summary>
public static class ServiceCollectionExtensions
{
    /// <summary>
    /// Adds the version 1 Qhapaq service layer to a service collection.
    /// </summary>
    /// <param name="services">The service collection to update.</param>
    /// <returns>The supplied service collection.</returns>
    public static IServiceCollection AddQhapaqServiceV1(this IServiceCollection services)
    {
        ArgumentNullException.ThrowIfNull(services);
        services.AddQhapaqBusiness();
        return services;
    }
}
