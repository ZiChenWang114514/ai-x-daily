# AIxDaily · 2026-09-24

今日精选：AI × Chem 16 项，AI × Bio 14 项，AI × Math 0 项，AI Voices 9 项，Engineering 10 项。9月24日的更新横跨反应计算、生物机制与智能体工程。化学和生物栏目以预印本为主，分别关注数据高效反应势、肌肉再生细胞亚群及疾病模型；工程端出现智能体编排和办公对象运行时的开源动向。公开观点栏目披露强化学习资源与心理健康评测基准，但相关性能、安全性主张仍应以原始报告和独立复评为准；数学频道未有足够高质量更新。

## 今日重大进展

- [Anthropic 公布 Claude 发现疑似新型噬菌体 DNA 酶系统](https://x.com/AnthropicAI/status/2102824959827742916) — Anthropic 公布，Claude 在噬菌体 DNA 中发现一个此前未知的酶系统；酶基因旁存在类似 CRISPR 的重复 DNA 阵列。该机构称尚不清楚其功能，正继续判断它是否具备可编程 DNA 操作潜力。
- [Courtade–Kumar 猜想据报获完整证明](https://x.com/yesnoerror/status/2102685032200478934) — 一则研究者帖文称，一篇 85 页论文首次完整证明 Courtade–Kumar 猜想：对任意带噪 n 比特向量，提取信息最优的布尔函数仍是只跟踪单一比特的“独裁者函数”，更复杂函数不能更优。
- [OpenAI 将插件与 GPT-6 接入 ChatGPT Voice](https://x.com/OpenAI/status/2102808325742322002) — OpenAI 宣布，ChatGPT Voice 已可调用邮件、日历和 Slack 等插件，并由 GPT-6 Astra、Sol、Luna 驱动；该能力在 ChatGPT Work 的网页和移动端全球推送，可语音完成文档、演示、网站、表格与浏览器任务。

## AI × Chem

采集 633，候选 60，精选 16。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable

- [Data-Efficient Machine Learning Potentials for Organic Reactions through Active-Learning-Guided Fine-Tuning](https://doi.org/10.26434/chemrxiv.15009333/v1) — 提出 MACEPre-DeePEST-OS：以预训练化学知识为基础、由主动学习选择量子化学标注构象的反应机器学习势。该方法仅标注约 1,900 万候选构象中的约 2%，便在多类有机反应中实现过渡态优化与能垒预测，并报告了跨数据集和超出微调分子规模的测试。
- [Integrative Physics and Machine Learning-Based Optimal Binding Pose Generator for Protein-Ligand Complexes](https://doi.org/10.26434/chemrxiv.15009330/v1) — 构建结合物理与机器学习的蛋白—配体最优结合姿势生成方法，针对 TNKS2 和 3CLPro 各使用 10,000 个分子的数据集训练，并在约 3,000 个分子的外部验证集上评估。作者称该方法可筛除松弛后不太可能具有有利结合亲和力的姿势，从而减少后续计算。
- [Uni-Macro-FRPN: Full-Resolution and Cross-Scale Learning for Polymers](https://doi.org/10.26434/chemrxiv.15009049/v2) — Uni-Macro-FRPN 在统一框架中保留原子级、单体级及显式聚合物拓扑信息，以两个 Transformer 学习 BigSMILES 表征。在 BCDB 层状/非层状分类上达到 86.4% 准确率和 90.6% ROC–AUC，并新建包含 1,640 个点的全原子 MD 拓扑丰富基准。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1123，候选 60，精选 14。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable；medRxiv: JSONDecodeError: Expecting value: line 1 column 1 (char 0)

- [Multiomics Characterization Identifies S1P-secreting USSHigh Skeletal Muscle Stem Cells as Essential Drivers of Niche Remodeling and Muscle Regeneration](https://www.biorxiv.org/content/10.64898/2026.09.18.752516) — 多组学揭示分泌 S1P 的 USSHigh 骨骼肌干细胞驱动损伤后微环境重塑与再生。
- [Genomic Engineering of Gene Dosage: A Generalizable Framework for Modeling Haploinsufficiency-Mediated Human Disorders through Splicing Modulation](https://www.biorxiv.org/content/10.64898/2026.09.20.753023) — 利用可调控可变剪接盒构建更接近人类单倍剂量不足疾病的动物模型。
- [Proinflammatory cytokines promote tau aggregation by inducing cleavage in human Alzheimer’s disease](https://europepmc.org/article/PPR/PPR1323735) — 炎性细胞因子经免疫蛋白酶体相关 tau 切割促进阿尔茨海默病 tau 聚集。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 0，候选 0，精选 0。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable；OpenReview: RuntimeError: colmweb.org/COLM/2026/Conference: HTTP 503

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 89，候选 60，精选 9。来源状态：各来源已完成

- [@_LuoFuli：MiMo-V2.6: The Hard Road to Scaling Up RL MiMo-V2.6 is very likely one of the largest single RL runs, by compute, that a](https://x.com/_LuoFuli/status/2102162926802968749) — Fuli Luo 宣布 MiMo-V2.6，并称团队投入数十人长期扩展强化学习；帖文同时称已发布由 MiMo RL 轨迹蒸馏的 Qwen 模型、7,000 个环境及完整 RL 训练框架。
- [@OpenAI：We're demonstrating how frontier models have continued to improve in realistic mental health conversations with MentalHe](https://x.com/OpenAI/status/2102837574092161102) — OpenAI 宣布开放 MentalHealthBench：该基准用于评估前沿模型在现实心理健康对话中的表现，构建时获得80余名心理健康临床医生的意见。
- [@XiaomiTech_：A classic mathematical theorem. 6,000+ lines of Lean code. Verified by the kernel. Xiaomi MiMo 2.6 Pro assisted research](https://x.com/XiaomiTech_/status/2102291812870176810) — 小米称，MiMo 2.6 Pro 协助研究者在 Lean 4 中完整形式化 Li–Yorke 论文的主定理；项目逾6,000行 Lean 代码，并由内核验证且无未完成证明占位符。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 94，候选 60，精选 10。来源状态：各来源已完成

- [google/ax](https://github.com/google/ax) — Google 的开源智能体编排运行时，今日 GitHub Trending 第 2 名，新增 1,542 星。
- [dream-num/univer](https://github.com/dream-num/univer) — Univer 是面向 AI 智能体的办公软件运行时，覆盖表格、文档、幻灯片、画布、关系表和 PDF；今日 GitHub Trending 第 6 名，新增 1,140 星。
- [superdesigndev/treg](https://github.com/superdesigndev/treg) — Treg 将自身定位为“面向智能体工具的 OpenRouter”，提供工具注册与接入层；今日 GitHub Trending 第 11 名，新增 502 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
