namespace Qhapaq.Abstractions.Operations;

/// <summary>
/// Contains the stable outputs of a binary parallel operation.
/// </summary>
/// <typeparam name="TLeft">The left output type.</typeparam>
/// <typeparam name="TRight">The right output type.</typeparam>
/// <param name="Left">The left branch output.</param>
/// <param name="Right">The right branch output.</param>
public sealed record ParallelResult<TLeft, TRight>(TLeft Left, TRight Right);
