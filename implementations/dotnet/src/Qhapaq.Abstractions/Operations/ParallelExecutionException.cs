using System.Collections.ObjectModel;

namespace Qhapaq.Abstractions.Operations;

/// <summary>
/// Reports one or more failures observed while executing parallel branches.
/// </summary>
public sealed class ParallelExecutionException : Exception
{
    /// <summary>
    /// Initializes a new instance of the <see cref="ParallelExecutionException"/> class.
    /// </summary>
    /// <param name="branchExceptions">The failures observed from parallel branches.</param>
    /// <exception cref="ArgumentException">
    /// <paramref name="branchExceptions"/> is empty.
    /// </exception>
    public ParallelExecutionException(IEnumerable<Exception> branchExceptions)
        : this(CreateExceptionList(branchExceptions))
    {
    }

    /// <summary>
    /// Initializes a new instance of the <see cref="ParallelExecutionException"/> class from a
    /// validated exception collection.
    /// </summary>
    /// <param name="branchExceptions">
    /// The validated failures observed from parallel branches.
    /// </param>
    private ParallelExecutionException(IReadOnlyList<Exception> branchExceptions)
        : base("One or more parallel operation branches failed.", branchExceptions[0])
    {
        this.BranchExceptions = branchExceptions;
    }

    /// <summary>
    /// Gets the branch failures in stable left-to-right order.
    /// </summary>
    public IReadOnlyList<Exception> BranchExceptions { get; }

    /// <summary>
    /// Validates and copies the supplied branch exceptions.
    /// </summary>
    /// <param name="branchExceptions">The branch exceptions to validate and copy.</param>
    /// <returns>A read-only copy of the supplied exceptions.</returns>
    private static IReadOnlyList<Exception> CreateExceptionList(
        IEnumerable<Exception> branchExceptions)
    {
        ArgumentNullException.ThrowIfNull(branchExceptions);

        Exception[] exceptions = branchExceptions.ToArray();
        if (exceptions.Length == 0)
        {
            throw new ArgumentException(
                "At least one branch exception is required.",
                nameof(branchExceptions));
        }

        if (exceptions.Any(static exception => exception is null))
        {
            throw new ArgumentException(
                "Branch exceptions cannot contain null values.",
                nameof(branchExceptions));
        }

        return new ReadOnlyCollection<Exception>(exceptions);
    }
}
