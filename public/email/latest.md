# AIxDaily · 2026-09-14

今日精选：AI × Chem 2 项，AI × Bio 15 项，AI × Math 0 项，AI Voices 0 项，Engineering 1 项。2026年9月14日的精选以预印本为主：化学频道聚焦聚焦超声递送与三维分子生成；生物频道关注可追溯的靶点发现及筛选数据分析。工程频道仅保留一个 GitHub Trending 仓库快照，并非软件发布。数学和公开观点频道均无足够高质量更新；今日没有同行评议论文入选。

## 今日重大进展

- [研究者报告：生物医学 AI 模型比较广泛受交叉验证统计偏差影响](https://www.biorxiv.org/content/10.64898/2026.05.17.724301) — 研究者报告，对 30 个领域 184 项高影响生物医学 AI 研究的审查发现，常用交叉验证比较忽略折间相关性；作者提出 SHARP 以控制假阳性并兼顾统计功效。
- [AutoScreen 公布功能基因组靶点发现多智能体系统](https://europepmc.org/article/PPR/PPR1316885) — 研究者公布 AutoScreen：一个服务功能基因组学靶点发现的多智能体系统，覆盖 CRISPR 筛选设计、命中重排和证据溯源；论文在 320 个筛选上评测，并报告原代 NK 细胞与前瞻性 T 细胞筛选验证。
- [Miniscope Zero 提出全无线单细胞神经成像平台](https://europepmc.org/article/PPR/PPR1317750) — 研究者提出 Miniscope Zero，以无线供电和高速光学数据链路实现自由行为动物的单细胞分辨率神经荧光成像；论文展示迷宫、三维行为及多动物同步记录。

## AI × Chem

采集 844，候选 60，精选 2。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 429: Unknown Error

- [Noninvasive Focal Gene Delivery of Functional Neural Actuators to the Primate Spinal Cord using Focused Ultrasound](https://www.biorxiv.org/content/10.64898/2026.09.05.749619) — 研究以聚焦超声（FUS）在绒猴颈段和胸段脊髓局灶、非侵入性地打开血-脊髓屏障，并递送经全身给药的病毒载体和化学遗传学载荷。作者系统优化声学参数，借助 PET、行为学和组织病理学显示靶区转基因表达、神经功能与组织完整性均得到支持，并提供脊髓 MRI/CT 模板和定位装置设计文件。
- [Interaction Profiles as a Universal Language for Generative Molecular Design with ShEPhERD-2](https://www.biorxiv.org/content/10.64898/2026.09.10.750648) — ShEPhERD-2 将形状、静电和具有方向性的药效团组成的三维相互作用图谱作为条件，生成低应变、类药分子。该模型可在无需任务专属再训练的情况下执行生物电子等排片段合并、双靶点设计、选择性工程和模态转换，并支持药效团优先级、子结构约束及多个相互作用图谱组合。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1691，候选 60，精选 15。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=100&max_results=100&sortBy=submittedDate&sortOrder=descending: The read operation timed out

- [AutoScreen: AI Co-Scientist System for Target Discovery in Functional Genomics](https://europepmc.org/article/PPR/PPR1316885) — AutoScreen 是用于功能基因组学靶点发现的多智能体 AI 系统，覆盖筛选设计、命中重排序、证据整合与溯源；在 320 个基因组尺度 CRISPR 筛选中评测，并报告了 NK 细胞杀伤实验和前瞻性 T 细胞筛选验证。
- [Agentic-AI-ready genome-wide poxvirus-host interaction screen refined by a protein language model](https://www.biorxiv.org/content/10.64898/2026.09.10.750412) — ICARus 将蛋白语言模型导出的蛋白互作信息用于正例-未标记读出校正，以改进痘病毒宿主因子的全基因组 RNA 干扰筛选命中优先级，并提供原始与校正后的读出资源。
- [Evaluating Safety-Critical Communication Behavior of Large Language Models Using Workflow-Embedded Multi-Agent Clinical Simulation](https://europepmc.org/article/PPR/PPR1317399) — 该研究以角色锁定的多智能体病房升级沟通模拟评估 LLM；在 200 对模拟中，ISBAR 交接降低幻觉频率并缩短对话，但未降低关键安全遗漏。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 3，候选 1，精选 0。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=100&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 429: Unknown Error

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 17，候选 14，精选 0。来源状态：X: RuntimeError: 未找到 Grok X 检索缓存。请先按 ops/grok/x_harvest_protocol.md 采集

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 68，候选 60，精选 1。来源状态：各来源已完成

- [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills) — tech-leads-club/agent-skills 是面向专业 AI 编程智能体的技能注册表，可为 Antigravity、Claude Code、Cursor、Copilot 等工具接入扩展；今日 GitHub Trending 第 4 名，新增 215 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
