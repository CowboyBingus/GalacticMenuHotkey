$ErrorActionPreference = 'Stop'
python -B (Join-Path $PSScriptRoot 'scripts/build.py')
if ($LASTEXITCODE -ne 0) { throw "Addon packaging failed with exit code $LASTEXITCODE." }
