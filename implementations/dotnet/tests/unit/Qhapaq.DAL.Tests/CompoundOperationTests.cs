using Qhapaq.DAL.Operations;

namespace Qhapaq.DAL.Tests;

public sealed class CompoundOperationTests
{
    [Fact]
    public async Task ExecuteAsync_PassesFirstOutputToSecondOperation()
    {
        var first = new DelegateOperation<int, string>(
            static (input, _) => Task.FromResult(input.ToString()));
        var second = new DelegateOperation<string, int>(
            static (input, _) => Task.FromResult(input.Length));
        var operation = new CompoundOperation<int, string, int>(first, second);

        int result = await operation.ExecuteAsync(123, TestContext.Current.CancellationToken);

        Assert.Equal(3, result);
    }

    [Fact]
    public async Task ExecuteAsync_WhenFirstFails_DoesNotExecuteSecondOperation()
    {
        var expected = new InvalidOperationException("first failed");
        var first = new DelegateOperation<int, string>(
            (_, _) => Task.FromException<string>(expected));
        var secondExecuted = false;
        var second = new DelegateOperation<string, int>(
            (_, _) =>
            {
                secondExecuted = true;
                return Task.FromResult(0);
            });
        var operation = new CompoundOperation<int, string, int>(first, second);

        InvalidOperationException actual = await Assert.ThrowsAsync<InvalidOperationException>(
            () => operation.ExecuteAsync(123, TestContext.Current.CancellationToken));

        Assert.Same(expected, actual);
        Assert.False(secondExecuted);
    }
}
