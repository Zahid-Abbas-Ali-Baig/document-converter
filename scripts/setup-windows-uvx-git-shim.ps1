# One-time fix for Microsoft Store Claude Desktop: uv needs "git" on PATH when
# spawning MCP servers, but Claude often passes a minimal PATH that omits Git.
# This places a tiny git.cmd next to uvx.exe so "uvx --from git+..." works.
$ErrorActionPreference = "Stop"

$uvBin = Join-Path $env:USERPROFILE ".local\bin"
$gitExe = "C:\Program Files\Git\cmd\git.exe"
$shim = Join-Path $uvBin "git.cmd"

if (-not (Test-Path $gitExe)) {
    Write-Error "Git not found at $gitExe. Install Git for Windows: https://git-scm.com/download/win"
}

New-Item -ItemType Directory -Force -Path $uvBin | Out-Null
Set-Content -Path $shim -Encoding ASCII -Value "@`"$gitExe`" %*"
Write-Host "Created $shim"
Write-Host "You can now use uvx --from git+... in Claude Desktop (restart Claude after updating config)."
