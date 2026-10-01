# AIxDaily · 2026-10-02

今日精选：AI × Chem 16 项，AI × Bio 14 项，AI × Math 15 项，AI Voices 10 项，Engineering 6 项。共同日期为2026-10-02。AI×Chem前三项均为arXiv预印本，聚焦分子晶体生成、结构偏移下的性质预测与单步逆合成；AI×Bio前三项均为medRxiv/bioRxiv预印本，涉及临床仪表板、CASR变异分类和卒中单细胞信号。AI×Math关注形式化证明与推理基准；AI Voices为X公开观点或机构发布；Engineering前三为GitHub Trending项目而非版本发布。前三项未见足够高质量的同行评议论文。

## 今日重大进展

- [Cogentic 报告多智能体系统在五个开放问题上产出经专家核验的新结果](https://arxiv.org/abs/2609.40324v1) — 预印本提出 Cogentic：以 Gemini 为基础模型，用多智能体并行探索、对抗式验证和持久化“已验证账本”推进开放问题证明，并报告在线学习、拍卖理论和机制设计五个问题的新结果。
- [研究者公布 AI 发现单原子层材料抗失效，并展示自主构建科学仪器流程](https://x.com/ProfBuehlerMIT/status/2104857542350295433) — MIT 研究者 Markus J. Buehler 在 X 公布，AI 研究单原子层材料在原子结构开始破坏时仍保持承载，并自主编写力学引擎、结构生成、加载、分析和实验数据库，连续运行数日。
- [AI2 发布 Olmo-core 3：面向万亿参数 MoE 的开放训练基础设施](https://x.com/allen_ai/status/2105679258165068097) — AI2 官方发布 Olmo-core 3 开放训练基础设施，为大规模 MoE 提供可改造的分布式训练栈，目标支持下一代 Olmo 向万亿参数扩展，并开放 GitHub 代码供团队自建训练系统。

## AI × Chem

采集 2381，候选 60，精选 16。来源状态：各来源已完成

- [Riemannian Flow Models with Reinforcement Learning for Molecular Crystal Structure Prediction](https://arxiv.org/abs/2609.39773v1) — 提出CG-OMatG，一种等变Riemannian flow生成模型，以粗粒度层级表示和刚性分子体建模分子晶体堆积，并用策略梯度强化学习引导生成低能候选结构；在OMC25、CSD数据集和CSP盲测基准上进行了验证。
- [Molecular Property Prediction under Structural Shift with Tabular Foundation Models](https://arxiv.org/abs/2609.38744v1) — 提出MolPAIR，将分子级上下文与分子对比较结合到无需任务特定参数更新的表格基础模型中，用第二个冻结模型预测查询分子与参考分子之间的误差差异，以改进结构分布外的性质预测。
- [RetroGEF: Dynamic Graph Edit Flow for Single-Step Retrosynthesis](https://arxiv.org/abs/2609.38484v1) — 提出RetroGEF，一种动态图编辑流生成模型，从目标分子出发在同一生成过程中增添原子并改变化学键，直接学习产物—反应物对而无需预先规定编辑顺序，用于单步逆合成。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 3205，候选 60，精选 14。来源状态：各来源已完成

- [Effect of an Electronic Health Record-Integrated Clinical Dashboard for Radiologists on STAT Priority Chest Radiograph Reporting and Downstream Care: A Stepped-Wedge Cluster Randomized Trial](https://www.medrxiv.org/content/10.64898/2026.09.23.26363355) — 【preprint；随机试验】在 15 个服务区域、387 名放射科医师和 404,860 次急诊及住院 STAT 胸片检查中，评估接入 EHR 信息的临床仪表板。仪表板未改变报告特异性或处方，但与轻度提高的出院诊断一致性和减少随访胸部 CT 相关。
- [Single-cell profiling resolves gain- and loss-of-function mechanisms in CASR to advance mechanism-aware variant classification](https://www.biorxiv.org/content/10.64898/2026.09.26.754690) — 【preprint；临床验证】研究将单细胞 RNA-seq 与监督式机器学习结合，区分 CASR 变异的 gain-of-function（GOF）和 loss-of-function（LOF）机制；在 96 个专家标注变异上训练，并对 157 个意义未明变异分类，预测结果与超过 300,000 名患者的临床表型和血钙数据相互印证。
- [Multi-Model Machine Learning Consensus Identifies a Dual-Interferon Gene Signature in Ischemic Stroke: An Integrative Single-Cell Transcriptomic Analysis](https://www.biorxiv.org/content/10.64898/2026.09.25.754010) — 【preprint；动物单细胞数据】在小鼠 MCAO 模型的 54,599 个细胞上，比较 8 类机器学习模型并采用按个体划分的训练/测试集，得到 63 个共识基因和双干扰素信号模式；结果提出了卒中生物标志物候选，但尚需临床验证。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 1442，候选 60，精选 15。来源状态：各来源已完成

- [Fyan: A Human--AI Harness with Semantic Auditing for Document-Level Formalization](https://arxiv.org/abs/2609.39228v1) — FYAN 将数学文档形式化组织为规格说明、证明规划、逻辑审查、Lean 构造、知识整理和验证的一体化流程，并加入证据驱动的语义审计。
- [ArgGYM: A Procedural, Engine-Verified Benchmark for Structured Defeasible Reasoning](https://arxiv.org/abs/2609.38409v1) — ArgGYM 用符号论证引擎为可撤销推理建立程序化、引擎验证的基准和 RLVR 训练环境，覆盖 12 类任务与 1,440 个冻结实例。
- [Growing an Agent/Prover Interface: Evolutionary Tool Design for Cost-Efficient Theorem Proving in Rocq and Lean](https://arxiv.org/abs/2609.39544v1) — 该工作用进化式工具设计改造智能体与 Rocq/Lean 证明助手的交互接口，并发布可迁移的 MCP 服务器。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 110，候选 60，精选 10。来源状态：各来源已完成

- [@fchollet：The critical distinction between base LLMs (2024 and earlier) and modern LRMs is not symbolic tool use. It's the switch ](https://x.com/fchollet/status/2105729206273634696) — François Chollet 认为，现代长思维模型（LRM）与基础大语言模型的关键差异，在于从直接猜答案转向在测试时归纳生成程序或推理链；他以 ARC-1 表现对比说明这种范式变化。
- [@AnthropicAI：In physics, an “impedance mismatch” occurs when two systems each work well but are poorly matched. In this Science Blog ](https://x.com/AnthropicAI/status/2105733864152858919) — Anthropic 转发哈佛物理学家 Matthew Schwartz 的观点：当前人与 LLM 的协作方式与模型在科学计算中的优势存在“阻抗失配”，他据此开发了定量科学精确计算工具包。
- [@allen_ai：We’re releasing Olmo-core 3—open training infrastructure for large mixture-of-experts (MoE) models. It’s a core system b](https://x.com/allen_ai/status/2105679258165068097) — AI2 发布 Olmo-core 3，这是面向大规模混合专家模型的开放训练基础设施，目标是支持下一代 Olmo 扩展到万亿参数规模。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 91，候选 60，精选 6。来源状态：各来源已完成

- [cursor/plugins](https://github.com/cursor/plugins) — Cursor/plugins 提供 Cursor 插件规范与官方插件集合；当日位列 GitHub Trending 第 6 名，新增 157 星。
- [tile-ai/tilelang](https://github.com/tile-ai/tilelang) — TileLang 是面向 GPU、CPU 和其他加速器高性能内核开发的领域特定语言；当日位列 GitHub Trending 第 11 名，新增 157 星。
- [Friedrich-M/UniMate](https://github.com/Friedrich-M/UniMate) — UniMate 是用于让不同骨架共享同一动画生成模型的研究项目；当日位列 GitHub Trending 第 15 名，新增 225 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
