# AIxDaily · 2026-10-12

今日精选：AI × Chem 7 项，AI × Bio 15 项，AI × Math 5 项，AI Voices 6 项，Engineering 2 项。今日五频道共同日期为 2026-10-12。学术精选以预印本为主，覆盖蛋白设计、生命科学数据与医疗评测、智能体推理和图学习，所列结果尚未等同于同行评议结论。公开观点侧重 LLM 能力认知和基础设施安全，工程侧则出现逆向工程智能体工具与 Python SDK 发布；两者应分别视作观点、项目动向和软件版本信息。

## 今日重大进展

- [研究者称 Google DeepMind 的证明智能体解出 9 个 Erdős 开放题](https://x.com/bravo_abad/status/2108880988461818255) — 研究者 Jorge Bravo Abad 在 X 介绍，Google DeepMind 团队以能生成 Lean 证明的智能体，解出包括悬置 56 年问题在内的 9 个 Erdős 开放题，并证明了 44 条整数数列猜想。
- [预印本报告：自主 Claude Code 在 19 亿蛋白簇中发现新型逆转录酶](https://www.biorxiv.org/content/10.64898/2026.10.05.755809) — 研究团队在 bioRxiv 报告，多实例 Claude Code 勘查 19 亿个蛋白簇的逆转录酶位点，识别出与约 200 nt 重复阵列及伴侣基因相连的巨型噬菌体新家族 ART；感染实验中其阵列高表达。

## AI × Chem

采集 1597，候选 60，精选 7。来源状态：各来源已完成

- [Filling the Missing Puzzle: Integrating Interaction and Evolutionary Information to Enhance Protein Fitness Prediction in Inverse Folding](https://www.biorxiv.org/content/10.64898/2026.10.05.756918) — zPolaron 将蛋白—配体相互作用、结构和进化信息整合到异质图神经网络中，用于功能导向的逆折叠与蛋白适应度预测；除多项基准外，作者还以 CalA6-D205A-S160G 和 CalB-I121M 的湿实验验证了活性提升。
- [Autonomous AI agents discover reverse transcriptases with tandem repeat arrays](https://www.biorxiv.org/content/10.64898/2026.10.05.755809) — 研究以自主运行的 Claude Code 检索 19 亿个蛋白簇中的逆转录酶位点，发现与约 200 nt 重复单元阵列及伙伴基因耦联的 jumbo 噬菌体新型 array-associated RTs（ART）；感染中的表达和离散阵列信号支持其为 RNA 指导系统。
- [The Batten disease gene product CLN6 is a glycerophosphoglycerol epimerase that establishes S,S-BMP stereochemistry](https://www.biorxiv.org/content/10.64898/2026.10.07.757477) — 研究鉴定出 Batten 病蛋白 CLN6 是一种 Ca2+-依赖的 glycerophosphoglycerol epimerase，可将 R,S-GPG 转化为 S,S-GPG，从而在 BMP 生物合成中建立关键立体化学；纯化蛋白、细胞、鼠组织和患者样本均支持该结论。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2290，候选 60，精选 15。来源状态：各来源已完成

- [DBCLS BioHackathon 2026 report: An interactive, harmonised BioSample metadata resource for biological sample discovery](https://europepmc.org/article/PPR/PPR1338353) — 本地部署LLM将420万条人和小鼠BioSample记录标准化为820万条可追溯的本体注释值。
- [MedBenchAgent: Towards Systematic Automation of Medical VLM Benchmark Construction](https://arxiv.org/abs/2610.11312v1) — MedBenchAgent以受约束编译和中间表示自动构建可审计的医疗VLM基准规范与测试条目。
- [A unified framework for quantitative splicing and transcript prediction](https://www.biorxiv.org/content/10.64898/2026.10.08.757673) — SpliceAI2从基因组序列重建完整转录本，并定量预测变异对剪接的影响。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 508，候选 60，精选 5。来源状态：各来源已完成

- [When Should Agents Think? Adaptive Reasoning via Cross-Turn Estimation](https://arxiv.org/abs/2610.12061v1) — RACE 用移除额外推理后参考动作的似然下降估计跨轮动作支撑，并据此训练智能体在推理与直接行动之间自适应选择。论文报告其在四类智能体基准上降低推理成本，同时维持或提升任务表现。
- [Batch Before You Lift: Scalable Topological Deep Learning on Large Graphs](https://arxiv.org/abs/2610.12247v1) — Cluster-TNN 在每个小批次中局部进行图提升，以避免拓扑深度学习的全图高阶结构物化。论文在 21 组与全图执行相匹配的比较中报告所有配置的峰值 GPU 内存均下降，平均降幅为 83.2%，且预测性能保持有竞争力。
- [From a Prompt to Repertoires: Evolving Functional REpertoires Enable LLM Continual Learning](https://arxiv.org/abs/2610.11373v1) — EFRE 将单一优化提示替换为会随新任务到来而演化的功能集合：兼容更新改进已有函数，冲突更新产生新函数。摘要报告，在三任务持续学习流中其最终平均表现比 GRPO 高 7.50 个百分点，且适应 Bio 任务后 FinQA 的表现降幅为 1.56 个百分点。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 81，候选 60，精选 6。来源状态：各来源已完成

- [@karpathy：Dusting off this tweet from April because this gap in shared understanding of LLM capability is *widening*. It's now les](https://x.com/karpathy/status/2109361546505966046) — Karpathy 以粗略估算描述了 LLM 使用者从几乎未接触者到内部前沿系统使用者的分层漏斗；文中的人数与比例属于作者估算，并非统计报告。
- [@fangfu0830：Let's cooking in the AgentGarten! Welcome to our Blog: Code Worlds for Evolving Agents. Paper: https://arxiv.org/abs/261](https://x.com/fangfu0830/status/2108439468147663206) — Fangfu Liu 发布 AgentGarten 的博客，并同时给出论文、代码库和项目页链接，提供了研究与复现入口。
- [@AnthropicAI：To help secure systems like power grids and water systems, we're launching a new Critical Infrastructure Defense Program](https://x.com/AnthropicAI/status/2108302541385499103) — Anthropic 宣布启动关键基础设施防御计划，称将把前沿 Claude 模型、驻场工程师和最新研究带给电网、水系统等运营方及其安全、制造和技术服务提供商。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 62，候选 58，精选 2。来源状态：各来源已完成

- [morluto/rea](https://github.com/morluto/rea) — morluto/rea 是用智能体辅助逆向工程的开发者工具，可从应用行为分析延伸到原生二进制分析。当天位列 GitHub Trending 第 1 名，新增 25,585 星。
- [v3.28.0](https://github.com/openai/openai-python/releases/tag/v3.28.0) — openai/openai-python 发布 v3.28.0：新增智能体环境暂停与过期能力的 API 支持，并更新 PyJWT 安全版本约束。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
