# AIxDaily

X 只走 Grok 检索，不走官方 X API。自动访问固定使用 `grok-4.6` 与 `low` 推理强度。

## Codex

Codex 不执行 `ops/grok/daily_visit_prompt.md`，也不直接检索 X。Codex 只运行 `ops/run_local_pipeline.ps1`；该脚本负责写访问票、启动 Grok、读取完成缓存并继续五频道审阅与发布。

## Grok

仅当当前执行者是 Grok，且仓库里有 `work/grok-x/<date>.request.json`、对应缓存尚未就绪时，才执行 `ops/grok/daily_visit_prompt.md`。Grok 完成 X 采集后结束，不审阅频道、不修改 `public/`、不 commit 或 push。

完整合同见 `ops/grok/x_harvest_protocol.md`。五频道学术审阅仍由 Codex `gpt-5.6-terra` / `high` 完成。

## 历史重复检查

运行日报、补做指定日期或修复发布流程时使用 `$aixdaily-operator`，并阅读其中的 `references/dedup-policy.md`。候选生成、频道审阅写入和综合日报发布都必须检查目标日期之前的 `public/data/daily/archive/*.json`。同一事件没有可核实变化时不再报道；明确的新版本、新修订、新软件发布或新帖文仍可入选。发布前必须运行 `backend/audit_cross_day_dedup.py --target-date <YYYY-MM-DD>`，检测到残余重复时停止提交与推送。
