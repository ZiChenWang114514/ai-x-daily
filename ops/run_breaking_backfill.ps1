param(
    [Parameter(Mandatory = $true)][string]$StartDate,
    [Parameter(Mandatory = $true)][string]$EndDate,
    [int]$ChunkSize = 7
)

$ErrorActionPreference = "Stop"
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$WorkRoot = Join-Path $RepoRoot "work\local-pipeline\breaking-backfill"
$Python = (Get-Command python -ErrorAction Stop).Source
$CodexCommand = (Get-Command codex.cmd -ErrorAction Stop).Source
$CodexRoot = Split-Path $CodexCommand -Parent
$CodexJavaScript = Join-Path $CodexRoot "node_modules\@openai\codex\bin\codex.js"
$Node = (Get-Command node.exe -ErrorAction Stop).Source
$SchemaPath = Join-Path $RepoRoot "ops\codex\breaking_backfill.schema.json"
$PromptTemplate = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot "ops\codex\breaking_backfill_prompt.md") -Encoding UTF8

$Start = [DateTime]::ParseExact($StartDate, "yyyy-MM-dd", [Globalization.CultureInfo]::InvariantCulture)
$End = [DateTime]::ParseExact($EndDate, "yyyy-MM-dd", [Globalization.CultureInfo]::InvariantCulture)
if ($End -lt $Start) { throw "EndDate precedes StartDate" }
if ($ChunkSize -lt 1) { throw "ChunkSize must be positive" }

New-Item -ItemType Directory -Force -Path $WorkRoot | Out-Null
$Cursor = $Start
$ChunkNumber = 0
while ($Cursor -le $End) {
    $ChunkNumber += 1
    $ChunkEnd = $Cursor.AddDays($ChunkSize - 1)
    if ($ChunkEnd -gt $End) { $ChunkEnd = $End }
    $ChunkDir = Join-Path $WorkRoot ("chunk-{0:d2}" -f $ChunkNumber)
    New-Item -ItemType Directory -Force -Path $ChunkDir | Out-Null
    $CandidatePath = Join-Path $ChunkDir "current-candidates.json"
    $CurationPath = Join-Path $ChunkDir "curation.json"
    $PromptPath = Join-Path $ChunkDir "prompt.md"
    $StdoutPath = Join-Path $ChunkDir "codex-output.txt"
    $StderrPath = Join-Path $ChunkDir "codex-error.txt"

    & $Python "backend/backfill_breaking_news.py" prepare --root $RepoRoot --site-root "public" --start-date $Cursor.ToString("yyyy-MM-dd") --end-date $ChunkEnd.ToString("yyyy-MM-dd") --output $CandidatePath
    if ($LASTEXITCODE -ne 0) { throw "Candidate preparation failed" }

    $RelativeCandidate = [IO.Path]::GetRelativePath($RepoRoot, $CandidatePath).Replace("\", "/")
    $Prompt = $PromptTemplate.Replace("work/local-pipeline/breaking-backfill/current-candidates.json", $RelativeCandidate)
    [IO.File]::WriteAllText($PromptPath, $Prompt, (New-Object Text.UTF8Encoding($false)))

    $CodexArgs = @(
        $CodexJavaScript, "exec", "--ephemeral", "--sandbox", "read-only", "--color", "never",
        "--model", "gpt-5.6-terra", "-c", "model_reasoning_effort=`"high`"",
        "-C", $RepoRoot, "--output-schema", $SchemaPath,
        "--output-last-message", $CurationPath, "-"
    )
    $Process = Start-Process -FilePath $Node -ArgumentList $CodexArgs -WorkingDirectory $RepoRoot -RedirectStandardInput $PromptPath -RedirectStandardOutput $StdoutPath -RedirectStandardError $StderrPath -WindowStyle Hidden -Wait -PassThru
    if ($Process.ExitCode -ne 0) {
        if (Test-Path $StderrPath) { Get-Content $StderrPath -Encoding UTF8 | Write-Host }
        throw "Codex historical review failed for $($Cursor.ToString('yyyy-MM-dd')) to $($ChunkEnd.ToString('yyyy-MM-dd'))"
    }

    & $Python "backend/backfill_breaking_news.py" apply $CurationPath --site-root "public" --candidates-root (Join-Path $ChunkDir "candidates")
    if ($LASTEXITCODE -ne 0) { throw "Applying historical review failed" }
    Write-Host "Completed major developments: $($Cursor.ToString('yyyy-MM-dd')) to $($ChunkEnd.ToString('yyyy-MM-dd'))"
    $Cursor = $ChunkEnd.AddDays(1)
}
