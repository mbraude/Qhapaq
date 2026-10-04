using Qhapaq.DAL.Operations;

namespace Qhapaq.DAL.Tests;

public sealed class ConditionalOperationTests
{
    [Theory]
    [InlineData(true, "true")]
    [InlineData(false, "false")]
    public async Task ExecuteAsync_ExecutesOnlySelectedBranch(bool predicateResult, string expected)
    {
        var trueExecutions = 0;
        var falseExecutions = 0;
        var predicate = new DelegateOperation<int, bool>(
            (_, _) => Task.FromResult(predicateResult));
        var whenTrue = new DelegateOperation<int, string>(
            (_, _) =>
            {
                trueExecutions++;
                return Task.FromResult("true");
            });
        var whenFalse = new DelegateOperation<int, string>(
            (_, _) =>
            {
                falseExecutions++;
                return Task.FromResult("false");
            });
        var operation = new ConditionalOperation<int, string>(predicate, whenTrue, whenFalse);

        string actual = await operation.ExecuteAsync(42, TestContext.Current.CancellationToken);

        Assert.Equal(expected, actual);
        Assert.Equal(predicateResult ? 1 : 0, trueExecutions);
        Assert.Equal(predicateResult ? 0 : 1, falseExecutions);
    }
}
