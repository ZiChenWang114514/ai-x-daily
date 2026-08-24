param(
    [int]$ReviewProcessId
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $ProjectRoot
$CandidateRoot = Join-Path $ProjectRoot "work\openreview-math-backfill\candidates"
$CurationRoot = Join-Path $ProjectRoot "work\openreview-math-backfill\curations"

Wait-Process -Id $ReviewProcessId -ErrorAction SilentlyContinue
Get-ChildItem -LiteralPath $CandidateRoot -Filter "*.candidates.json" | ForEach-Object {
    $candidate = Get-Content -Raw -LiteralPath $_.FullName | ConvertFrom-Json
    if ([int]$candidate.count -gt 0 -and [int]$candidate.selection_capacity -gt 0) {
        $dateText = $_.BaseName -replace '\.candidates$', ''
        if (-not (Test-Path -LiteralPath (Join-Path $CurationRoot "$dateText.json"))) {
            throw "Missing completed curation for $dateText"
        }
    }
}

python backend\backfill_openreview_math.py apply --start 2026-08-01 --end 2026-08-24 --root . --site-root public
python -m unittest
foreach ($dateText in @("2026-08-16","2026-08-17","2026-08-18","2026-08-19","2026-08-20","2026-08-21","2026-08-22","2026-08-23","2026-08-24")) {
    python backend\audit_cross_day_dedup.py --site-root public --target-date $dateText
}

git add -- backend\aix_pipeline.py backend\backfill_openreview_math.py ops\review_openreview_math_backfill.ps1 ops\finalize_openreview_math_backfill.ps1 public\data\channels\aixmath public\data\daily
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git commit -m "data: backfill August OpenReview math"
    git push
}
