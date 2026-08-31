param(
    [string]$StartDate = "2026-08-01",
    [string]$EndDate = "2026-08-30"
)

$ErrorActionPreference = "Stop"
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$WorkRoot = Join-Path $RepoRoot "work\engineering-trending-backfill"
$ArchiveRepo = Join-Path $RepoRoot "work\vendor\trending-collection"
$Schema = Join-Path $RepoRoot "ops\codex\channel_curation.schema.json"
$Curations = Join-Path $WorkRoot "curations"
New-Item -ItemType Directory -Force -Path $Curations | Out-Null

$CodexCommand = (Get-Command codex.cmd -ErrorAction Stop).Source
$CodexRoot = Split-Path $CodexCommand -Parent
$CodexJavaScript = Join-Path $CodexRoot "node_modules\@openai\codex\bin\codex.js"
$Node = (Get-Command node.exe -ErrorAction Stop).Source

Push-Location $RepoRoot
try {
    python backend/backfill_engineering_trending.py prepare --archive-repo $ArchiveRepo --work-root $WorkRoot --start $StartDate --end $EndDate
    if ($LASTEXITCODE -ne 0) { throw "Historical Trending preparation failed" }

    $Current = [datetime]::ParseExact($StartDate, "yyyy-MM-dd", $null)
    $End = [datetime]::ParseExact($EndDate, "yyyy-MM-dd", $null)
    while ($Current -le $End) {
        $Day = $Current.ToString("yyyy-MM-dd")
        $Prompt = Join-Path $WorkRoot "prompts\$Day.md"
        $Output = Join-Path $Curations "$Day.json"
        $Stdout = Join-Path $WorkRoot "logs\$Day-output.txt"
        $Stderr = Join-Path $WorkRoot "logs\$Day-error.txt"
        New-Item -ItemType Directory -Force -Path (Split-Path $Stdout -Parent) | Out-Null
        $Ready = $false
        if (Test-Path -LiteralPath $Output) {
            try {
                $Existing = Get-Content -LiteralPath $Output -Raw -Encoding UTF8 | ConvertFrom-Json
                $Ready = $Existing.date -eq $Day -and $Existing.channel -eq "engineering"
            } catch { $Ready = $false }
        }
        if (-not $Ready) {
            Write-Host "Reviewing Engineering Trending $Day with gpt-5.6-terra / high"
            $Args = @(
                $CodexJavaScript, "exec", "--ephemeral", "--sandbox", "read-only", "--color", "never",
                "--model", "gpt-5.6-terra", "-c", 'model_reasoning_effort="high"',
                "-C", $RepoRoot, "--output-schema", $Schema,
                "--output-last-message", $Output, "-"
            )
            $Process = Start-Process -FilePath $Node -ArgumentList $Args -WorkingDirectory $RepoRoot -RedirectStandardInput $Prompt -RedirectStandardOutput $Stdout -RedirectStandardError $Stderr -WindowStyle Hidden -Wait -PassThru
            if ($Process.ExitCode -ne 0) { throw "Engineering Trending review failed for $Day with exit code $($Process.ExitCode)" }
        } else {
            Write-Host "Using completed review for $Day"
        }
        $Current = $Current.AddDays(1)
    }

    python backend/backfill_engineering_trending.py publish --work-root $WorkRoot --site-root public --start $StartDate --end $EndDate
    if ($LASTEXITCODE -ne 0) { throw "Historical Trending publication failed" }
    python backend/hub_publish.py --site-root public
    if ($LASTEXITCODE -ne 0) { throw "Hub rebuild failed" }
}
finally {
    Pop-Location
}
