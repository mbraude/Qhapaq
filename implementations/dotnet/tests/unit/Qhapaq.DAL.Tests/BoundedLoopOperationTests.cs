using Qhapaq.Abstractions.Operations;
using Qhapaq.DAL.Operations;

namespace Qhapaq.DAL.Tests;

public sealed class BoundedLoopOperationTests
{
    [Fact]
    public async Task ExecuteAsync_StopsWhenConditionBecomesFalse()
    {
        var condition = new DelegateOperation<int, bool>(
            static (state, _) => Task.FromResult(state < 3));
        var body = new DelegateOperation<int, int>(static (state, _) => Task.FromResult(state + 1));
        var operation = new BoundedLoopOperation<int>(condition, body, maxIterations: 5);

        int result = await operation.ExecuteAsync(0, TestContext.Current.CancellationToken);

        Assert.Equal(3, result);
    }

    [Fact]
    public async Task ExecuteAsync_WhenConditionRemainsTrue_ThrowsLoopLimitException()
    {
        var condition = new DelegateOperation<int, bool>(static (_, _) => Task.FromResult(true));
        var body = new DelegateOperation<int, int>(static (state, _) => Task.FromResult(state + 1));
        var operation = new BoundedLoopOperation<int>(condition, body, maxIterations: 2);

        LoopLimitExceededException exception =
            await Assert.ThrowsAsync<LoopLimitExceededException>(
                () => operation.ExecuteAsync(0, TestContext.Current.CancellationToken));

        Assert.Equal(2, exception.MaxIterations);
    }

    [Fact]
    public void Constructor_WhenMaximumIsNotPositive_ThrowsArgumentOutOfRangeException()
    {
        var condition = new DelegateOperation<int, bool>(static (_, _) => Task.FromResult(false));
        var body = new DelegateOperation<int, int>(static (state, _) => Task.FromResult(state));

        Assert.Throws<ArgumentOutOfRangeException>(
            () => new BoundedLoopOperation<int>(condition, body, maxIterations: 0));
    }
}
