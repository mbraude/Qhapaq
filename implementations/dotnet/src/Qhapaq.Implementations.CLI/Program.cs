namespace Qhapaq.Implementations.CLI;

/// <summary>
/// Provides the qhapaq command-line process entry point.
/// </summary>
internal static class Program
{
    /// <summary>
    /// Reports that the CLI contract is not yet implemented.
    /// </summary>
    /// <returns>A nonzero exit code.</returns>
    private static int Main()
    {
        Console.Error.WriteLine(
            "The qhapaq CLI contract is not implemented in the initial architecture scaffold.");
        return 1;
    }
}
