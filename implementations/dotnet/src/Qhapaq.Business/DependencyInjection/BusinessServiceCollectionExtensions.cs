using Microsoft.Extensions.DependencyInjection;
using Qhapaq.DAL.DependencyInjection;

namespace Qhapaq.Business.DependencyInjection;

/// <summary>
/// Provides dependency-injection registration for the Business layer.
/// </summary>
internal static class BusinessServiceCollectionExtensions
{
    /// <summary>
    /// Registers Business services and delegates DAL registration.
    /// </summary>
    /// <param name="services">The service collection to update.</param>
    /// <returns>The supplied service collection.</returns>
    internal static IServiceCollection AddQhapaqBusiness(this IServiceCollection services)
    {
        ArgumentNullException.ThrowIfNull(services);
        services.AddQhapaqDal();
        return services;
    }
}
