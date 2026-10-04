using Qhapaq.Abstractions.Operations;

namespace Qhapaq.DAL.Operations;

/// <summary>
/// Executes two operations sequentially by passing the first output to the second operation.
/// </summary>
/// <typeparam name="TInput">The first operation input type.</typeparam>
/// <typeparam name="TIntermediate">The value passed between the operations.</typeparam>
/// <typeparam name="TOutput">The second operation output type.</typeparam>
internal sealed class CompoundOperation<TInput, TIntermediate, TOutput>
    : IOperation<TInput, TOutput>
{
    /// <summary>
    /// The operation that produces the intermediate value.
    /// </summary>
    private readonly IOperation<TInput, TIntermediate> first;

    /// <summary>
    /// The operation that transforms the intermediate value into the output.
    /// </summary>
    private readonly IOperation<TIntermediate, TOutput> second;

    /// <summary>
    /// Initializes a new instance of the
    /// <see cref="CompoundOperation{TInput, TIntermediate, TOutput}"/> class.
    /// </summary>
    /// <param name="first">The operation that runs first.</param>
    /// <param name="second">The operation that receives the intermediate value.</param>
    public CompoundOperation(
        IOperation<TInput, TIntermediate> first,
        IOperation<TIntermediate, TOutput> second)
    {
        ArgumentNullException.ThrowIfNull(first);
        ArgumentNullException.ThrowIfNull(second);

        this.first = first;
        this.second = second;
    }

    /// <inheritdoc />
    public async Task<TOutput> ExecuteAsync(
        TInput input,
        CancellationToken cancellationToken = default)
    {
        cancellationToken.ThrowIfCancellationRequested();

        TIntermediate intermediate = await this.first
            .ExecuteAsync(input, cancellationToken)
            .ConfigureAwait(false);

        return await this.second
            .ExecuteAsync(intermediate, cancellationToken)
            .ConfigureAwait(false);
    }
}
