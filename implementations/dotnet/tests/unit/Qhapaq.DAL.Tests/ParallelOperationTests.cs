using Qhapaq.Abstractions.Operations;
using Qhapaq.DAL.Operations;

namespace Qhapaq.DAL.Tests;

public sealed class ParallelOperationTests
{
    [Fact]
    public async Task ExecuteAsync_ReturnsStableLeftAndRightOutputs()
    {
        var left = new DelegateOperation<int, string>(
            static (input, _) => Task.FromResult($"left-{input}"));
        var right = new DelegateOperation<int, string>(
            static (input, _) => Task.FromResult($"right-{input}"));
        var operation = new ParallelOperation<int, string, string>(left, right);

        ParallelResult<string, string> result =
            await operation.ExecuteAsync(7, TestContext.Current.CancellationToken);

        Assert.Equal("left-7", result.Left);
        Assert.Equal("right-7", result.Right);
    }

    [Fact]
    public async Task ExecuteAsync_WhenBothBranchesFail_ReportsBothFailuresInBranchOrder()
    {
        var enteredBranches = 0;
        var bothBranchesEntered = new TaskCompletionSource(
            TaskCreationOptions.RunContinuationsAsynchronously);
        var leftFailure = new InvalidOperationException("left");
        var rightFailure = new NotSupportedException("right");

        Task WaitForBothBranchesAsync()
        {
            if (Interlocked.Increment(ref enteredBranches) == 2)
            {
                bothBranchesEntered.SetResult();
            }

            return bothBranchesEntered.Task;
        }

        var left = new DelegateOperation<int, string>(
            async (_, _) =>
            {
                await WaitForBothBranchesAsync();
                throw leftFailure;
            });
        var right = new DelegateOperation<int, string>(
            async (_, _) =>
            {
                await WaitForBothBranchesAsync();
                throw rightFailure;
            });
        var operation = new ParallelOperation<int, string, string>(left, right);

        ParallelExecutionException exception =
            await Assert.ThrowsAsync<ParallelExecutionException>(
                () => operation.ExecuteAsync(0, TestContext.Current.CancellationToken));

        Assert.Equal([leftFailure, rightFailure], exception.BranchExceptions);
    }

    [Fact]
    public async Task ExecuteAsync_WhenOneBranchFails_CancelsTheOtherBranch()
    {
        var branchStarted = new TaskCompletionSource(
            TaskCreationOptions.RunContinuationsAsynchronously);
        var cancellationObserved = new TaskCompletionSource(
            TaskCreationOptions.RunContinuationsAsynchronously);
        var failure = new InvalidOperationException("left");

        var left = new DelegateOperation<int, string>(
            async (_, _) =>
            {
                await branchStarted.Task;
                throw failure;
            });
        var right = new DelegateOperation<int, string>(
            async (_, cancellationToken) =>
            {
                branchStarted.SetResult();

                try
                {
                    await Task.Delay(Timeout.InfiniteTimeSpan, cancellationToken);
                    return "unreachable";
                }
                catch (OperationCanceledException)
                {
                    cancellationObserved.SetResult();
                    throw;
                }
            });
        var operation = new ParallelOperation<int, string, string>(left, right);

        ParallelExecutionException exception =
            await Assert.ThrowsAsync<ParallelExecutionException>(
                () => operation.ExecuteAsync(0, TestContext.Current.CancellationToken));

        await cancellationObserved.Task.WaitAsync(
            TimeSpan.FromSeconds(1),
            TestContext.Current.CancellationToken);
        Assert.Equal([failure], exception.BranchExceptions);
    }

    [Fact]
    public async Task ExecuteAsync_WhenBranchFaultsWithCancellationException_ReportsFailure()
    {
        var failure = new OperationCanceledException("operation-specific cancellation");
        var left = new DelegateOperation<int, string>(
            (_, _) => Task.FromException<string>(failure));
        var right = new DelegateOperation<int, string>(static (_, _) => Task.FromResult("right"));
        var operation = new ParallelOperation<int, string, string>(left, right);

        ParallelExecutionException exception =
            await Assert.ThrowsAsync<ParallelExecutionException>(
                () => operation.ExecuteAsync(0, TestContext.Current.CancellationToken));

        Assert.Equal([failure], exception.BranchExceptions);
    }
}
