using Microsoft.Extensions.DependencyInjection;

namespace Qhapaq.DAL.DependencyInjection;

/// <summary>
/// Provides dependency-injection registration for the DAL layer.
/// </summary>
internal static class DalServiceCollectionExtensions
{
    /// <summary>
    /// Registers DAL services with the supplied service collection.
    /// </summary>
    /// <param name="services">The service collection to update.</param>
    /// <returns>The supplied service collection.</returns>
    internal static IServiceCollection AddQhapaqDal(this IServiceCollection services)
    {
        ArgumentNullException.ThrowIfNull(services);
        return services;
    }
}
