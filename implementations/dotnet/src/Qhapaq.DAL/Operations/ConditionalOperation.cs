using Qhapaq.Abstractions.Operations;

namespace Qhapaq.DAL.Operations;

/// <summary>
/// Executes one of two operations based on the result of a predicate operation.
/// </summary>
/// <typeparam name="TInput">The shared predicate and branch input type.</typeparam>
/// <typeparam name="TOutput">The shared branch output type.</typeparam>
internal sealed class ConditionalOperation<TInput, TOutput>
    : IOperation<TInput, TOutput>
{
    /// <summary>
    /// The operation that selects which branch to execute.
    /// </summary>
    private readonly IOperation<TInput, bool> predicate;

    /// <summary>
    /// The operation selected when the predicate returns <see langword="true"/>.
    /// </summary>
    private readonly IOperation<TInput, TOutput> whenTrue;

    /// <summary>
    /// The operation selected when the predicate returns <see langword="false"/>.
    /// </summary>
    private readonly IOperation<TInput, TOutput> whenFalse;

    /// <summary>
    /// Initializes a new instance of the <see cref="ConditionalOperation{TInput, TOutput}"/> class.
    /// </summary>
    /// <param name="predicate">The operation that selects a branch.</param>
    /// <param name="whenTrue">The branch selected for a <see langword="true"/> result.</param>
    /// <param name="whenFalse">The branch selected for a <see langword="false"/> result.</param>
    public ConditionalOperation(
        IOperation<TInput, bool> predicate,
        IOperation<TInput, TOutput> whenTrue,
        IOperation<TInput, TOutput> whenFalse)
    {
        ArgumentNullException.ThrowIfNull(predicate);
        ArgumentNullException.ThrowIfNull(whenTrue);
        ArgumentNullException.ThrowIfNull(whenFalse);

        this.predicate = predicate;
        this.whenTrue = whenTrue;
        this.whenFalse = whenFalse;
    }

    /// <inheritdoc />
    public async Task<TOutput> ExecuteAsync(
        TInput input,
        CancellationToken cancellationToken = default)
    {
        cancellationToken.ThrowIfCancellationRequested();

        bool condition = await this.predicate
            .ExecuteAsync(input, cancellationToken)
            .ConfigureAwait(false);

        IOperation<TInput, TOutput> selected = condition ? this.whenTrue : this.whenFalse;
        return await selected.ExecuteAsync(input, cancellationToken).ConfigureAwait(false);
    }
}
