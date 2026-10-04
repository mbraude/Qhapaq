using Qhapaq.Abstractions.Operations;

namespace Qhapaq.DAL.Operations;

/// <summary>
/// Executes a stateful loop with a required maximum number of body executions.
/// </summary>
/// <typeparam name="TState">The loop state type.</typeparam>
internal sealed class BoundedLoopOperation<TState> : IOperation<TState, TState>
{
    /// <summary>
    /// The operation that determines whether another iteration should run.
    /// </summary>
    private readonly IOperation<TState, bool> condition;

    /// <summary>
    /// The operation that produces the state for the next iteration.
    /// </summary>
    private readonly IOperation<TState, TState> body;

    /// <summary>
    /// The maximum number of body executions.
    /// </summary>
    private readonly int maxIterations;

    /// <summary>
    /// Initializes a new instance of the <see cref="BoundedLoopOperation{TState}"/> class.
    /// </summary>
    /// <param name="condition">The operation that determines whether the body should run.</param>
    /// <param name="body">The operation that updates the loop state.</param>
    /// <param name="maxIterations">The maximum number of body executions.</param>
    public BoundedLoopOperation(
        IOperation<TState, bool> condition,
        IOperation<TState, TState> body,
        int maxIterations)
    {
        ArgumentNullException.ThrowIfNull(condition);
        ArgumentNullException.ThrowIfNull(body);
        ArgumentOutOfRangeException.ThrowIfNegativeOrZero(maxIterations);

        this.condition = condition;
        this.body = body;
        this.maxIterations = maxIterations;
    }

    /// <inheritdoc />
    public async Task<TState> ExecuteAsync(
        TState input,
        CancellationToken cancellationToken = default)
    {
        TState state = input;

        for (int iteration = 0; iteration < this.maxIterations; iteration++)
        {
            cancellationToken.ThrowIfCancellationRequested();

            if (!await this.condition.ExecuteAsync(state, cancellationToken).ConfigureAwait(false))
            {
                return state;
            }

            state = await this.body.ExecuteAsync(state, cancellationToken).ConfigureAwait(false);
        }

        cancellationToken.ThrowIfCancellationRequested();
        if (await this.condition.ExecuteAsync(state, cancellationToken).ConfigureAwait(false))
        {
            throw new LoopLimitExceededException(this.maxIterations);
        }

        return state;
    }
}
