using Qhapaq.Abstractions.Operations;

namespace Qhapaq.DAL.Operations;

/// <summary>
/// Executes two operations concurrently with shared input and coordinated cancellation.
/// </summary>
/// <typeparam name="TInput">The shared branch input type.</typeparam>
/// <typeparam name="TLeft">The left branch output type.</typeparam>
/// <typeparam name="TRight">The right branch output type.</typeparam>
internal sealed class ParallelOperation<TInput, TLeft, TRight>
    : IOperation<TInput, ParallelResult<TLeft, TRight>>
{
    /// <summary>
    /// The operation that produces the left result.
    /// </summary>
    private readonly IOperation<TInput, TLeft> left;

    /// <summary>
    /// The operation that produces the right result.
    /// </summary>
    private readonly IOperation<TInput, TRight> right;

    /// <summary>
    /// Initializes a new instance of the
    /// <see cref="ParallelOperation{TInput, TLeft, TRight}"/> class.
    /// </summary>
    /// <param name="left">The operation that produces the left result.</param>
    /// <param name="right">The operation that produces the right result.</param>
    public ParallelOperation(IOperation<TInput, TLeft> left, IOperation<TInput, TRight> right)
    {
        ArgumentNullException.ThrowIfNull(left);
        ArgumentNullException.ThrowIfNull(right);

        this.left = left;
        this.right = right;
    }

    /// <inheritdoc />
    public async Task<ParallelResult<TLeft, TRight>> ExecuteAsync(
        TInput input,
        CancellationToken cancellationToken = default)
    {
        cancellationToken.ThrowIfCancellationRequested();

        using var branchCancellation = CancellationTokenSource.CreateLinkedTokenSource(
            cancellationToken);

        Exception? leftFailure = null;
        Exception? rightFailure = null;
        Task<TLeft> leftTask = ExecuteBranchAsync(
            this.left,
            input,
            branchCancellation,
            exception => leftFailure = exception);
        Task<TRight> rightTask = ExecuteBranchAsync(
            this.right,
            input,
            branchCancellation,
            exception => rightFailure = exception);

        try
        {
            await Task.WhenAll(leftTask, rightTask).ConfigureAwait(false);
        }
        catch
        {
            IReadOnlyList<Exception> failures = GetFailures(leftFailure, rightFailure);
            if (failures.Count > 0)
            {
                throw new ParallelExecutionException(failures);
            }

            cancellationToken.ThrowIfCancellationRequested();
            throw;
        }

        TLeft left = await leftTask.ConfigureAwait(false);
        TRight right = await rightTask.ConfigureAwait(false);
        return new ParallelResult<TLeft, TRight>(left, right);
    }

    /// <summary>
    /// Executes one parallel branch and records failures before task cancellation
    /// semantics can hide them.
    /// </summary>
    /// <typeparam name="TOutput">The branch output type.</typeparam>
    /// <param name="operation">The branch operation.</param>
    /// <param name="input">The shared operation input.</param>
    /// <param name="branchCancellation">The linked cancellation source for both branches.</param>
    /// <param name="recordFailure">The callback that records a branch failure.</param>
    /// <returns>A task that completes with the branch output.</returns>
    private static async Task<TOutput> ExecuteBranchAsync<TOutput>(
        IOperation<TInput, TOutput> operation,
        TInput input,
        CancellationTokenSource branchCancellation,
        Action<Exception> recordFailure)
    {
        try
        {
            return await operation
                .ExecuteAsync(input, branchCancellation.Token)
                .ConfigureAwait(false);
        }
        catch (OperationCanceledException exception)
            when (branchCancellation.IsCancellationRequested &&
                  exception.CancellationToken == branchCancellation.Token)
        {
            throw;
        }
        catch (Exception exception)
        {
            recordFailure(exception);
            await branchCancellation.CancelAsync().ConfigureAwait(false);
            throw;
        }
    }

    /// <summary>
    /// Creates a stable left-to-right collection of recorded branch failures.
    /// </summary>
    /// <param name="leftFailure">The left branch failure, if any.</param>
    /// <param name="rightFailure">The right branch failure, if any.</param>
    /// <returns>The recorded failures in branch order.</returns>
    private static IReadOnlyList<Exception> GetFailures(
        Exception? leftFailure,
        Exception? rightFailure)
    {
        var failures = new List<Exception>(capacity: 2);
        if (leftFailure is not null)
        {
            failures.Add(leftFailure);
        }

        if (rightFailure is not null)
        {
            failures.Add(rightFailure);
        }

        return failures;
    }
}
