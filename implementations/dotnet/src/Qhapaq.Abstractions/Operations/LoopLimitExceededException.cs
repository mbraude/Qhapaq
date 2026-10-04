namespace Qhapaq.Abstractions.Operations;

/// <summary>
/// Reports that a bounded loop remained active after its configured limit.
/// </summary>
public sealed class LoopLimitExceededException : Exception
{
    /// <summary>
    /// Initializes a new instance of the <see cref="LoopLimitExceededException"/> class.
    /// </summary>
    /// <param name="maxIterations">The configured maximum number of body executions.</param>
    public LoopLimitExceededException(int maxIterations)
        : base($"The loop condition remained true after {maxIterations} iterations.")
    {
        ArgumentOutOfRangeException.ThrowIfNegativeOrZero(maxIterations);
        this.MaxIterations = maxIterations;
    }

    /// <summary>
    /// Gets the configured maximum number of body executions.
    /// </summary>
    public int MaxIterations { get; }
}
