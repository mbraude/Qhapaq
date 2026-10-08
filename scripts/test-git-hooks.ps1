$ErrorActionPreference = 'Stop'
$hookDirectory = Join-Path (Split-Path $PSScriptRoot -Parent) '.githooks'
$temporaryDirectory = Join-Path ([IO.Path]::GetTempPath()) ("qhapaq-hook-tests-" + [guid]::NewGuid())
$cases = @(
    foreach ($kind in 'requirement', 'amendment', 'extension', 'bug', 'editorial', 'refactor', 'maintenance') {
        @{ Name = "valid $kind"; Message = "test: example`n`nChange-Kind: $kind`n"; Expected = 0 }
    }
    @{ Name = 'other trailers'; Message = "test: example`n`nChange-Kind: bug`nSpec: R-0001-012@abcdef`nCo-authored-by: Example <example@example.invalid>`n"; Expected = 0 }
    @{ Name = 'CRLF'; Message = "test: example`r`n`r`nChange-Kind: maintenance`r`n"; Expected = 0 }
    @{ Name = 'missing'; Message = "test: example`n"; Expected = 1 }
    @{ Name = 'unknown kind'; Message = "test: example`n`nChange-Kind: feature`n"; Expected = 1 }
    @{ Name = 'duplicate'; Message = "test: example`n`nChange-Kind: bug`nChange-Kind: bug`n"; Expected = 1 }
    @{ Name = 'conflicting kinds'; Message = "test: example`n`nChange-Kind: bug`nChange-Kind: extension`n"; Expected = 1 }
    @{ Name = 'wrong key case'; Message = "test: example`n`nchange-kind: bug`n"; Expected = 1 }
    @{ Name = 'wrong value case'; Message = "test: example`n`nChange-Kind: Bug`n"; Expected = 1 }
    @{ Name = 'empty value'; Message = "test: example`n`nChange-Kind:`n"; Expected = 1 }
    @{ Name = 'subject only'; Message = "Change-Kind: maintenance`n"; Expected = 1 }
    @{ Name = 'body only'; Message = "test: example`n`nChange-Kind: bug`n`nNot a trailer block.`n"; Expected = 1 }
)

try {
    [void][IO.Directory]::CreateDirectory($temporaryDirectory)
    & git -C $temporaryDirectory init --quiet
    if ($LASTEXITCODE -ne 0) { throw 'Could not initialize the isolated hook-test repository.' }
    $messagePath = Join-Path $temporaryDirectory 'message.txt'
    foreach ($case in $cases) {
        [IO.File]::WriteAllText($messagePath, $case.Message, [Text.UTF8Encoding]::new($false))
        $output = & git -C $temporaryDirectory -c "core.hooksPath=$hookDirectory" hook run commit-msg -- $messagePath 2>&1
        $exitCode = $LASTEXITCODE
        if ($exitCode -ne $case.Expected) {
            throw "Hook case '$($case.Name)' expected exit $($case.Expected), got ${exitCode}: $($output -join "`n")"
        }
        if ($case.Expected -ne 0 -and ($output -join "`n") -notmatch 'require exactly one Change-Kind:') {
            throw "Hook case '$($case.Name)' failed without the required diagnostic: $($output -join "`n")"
        }
        Write-Output "PASS: $($case.Name)"
    }
    Write-Output "Passed $($cases.Count) hook cases."
}
finally {
    if (Test-Path -LiteralPath $temporaryDirectory) {
        Remove-Item -LiteralPath $temporaryDirectory -Recurse -Force
    }
}
