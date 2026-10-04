using Qhapaq.Abstractions.Operations;

namespace Qhapaq.DAL.Tests;

internal sealed class DelegateOperation<TInput, TOutput>(
    Func<TInput, CancellationToken, Task<TOutput>> execute)
    : IOperation<TInput, TOutput>
{
    public Task<TOutput> ExecuteAsync(TInput input, CancellationToken cancellationToken = default)
    {
        return execute(input, cancellationToken);
    }
}
