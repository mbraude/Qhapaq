namespace Qhapaq.Abstractions.Operations;

/// <summary>
/// Maps an input value to an output value asynchronously.
/// </summary>
/// <typeparam name="TInput">The operation input type.</typeparam>
/// <typeparam name="TOutput">The operation output type.</typeparam>
public interface IOperation<TInput, TOutput>
{
    /// <summary>
    /// Executes the operation.
    /// </summary>
    /// <param name="input">The input value.</param>
    /// <param name="cancellationToken">A signal that the operation should cancel.</param>
    /// <returns>A task that completes with the operation output.</returns>
    Task<TOutput> ExecuteAsync(TInput input, CancellationToken cancellationToken = default);
}
