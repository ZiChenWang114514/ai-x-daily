# AIxDaily · 2026-11-01

今日精选：AI × Chem 8 项，AI × Bio 9 项，AI × Math 7 项，AI Voices 9 项，Engineering 3 项。今日五频道前三项显示，研究侧以预印本为主：AI×Chem 聚焦 NMR 结构解析、ADMET 公平评测和蛋白结合体设计；AI×Bio 强调单细胞 GRN 加速、环境健康检索与胶质瘤影像组学；AI×Math 关注代理验证、动态环境审计和 Transformer 形式语义。AI Voices 是公开帖文与观点，Engineering 是 GitHub Trending 软件项目快照；前三项未见同行评议论文或明确的新版本发布。

## 今日重大进展

- [Axiom 与 Yifeng Huang 公开宣布证明 Huang–Jiang–Oblomkov 猜想](https://x.com/axiommathai/status/2115850590278565916) — Axiom 与 Yifeng Huang 在公开帖文中宣布已证明 Huang–Jiang–Oblomkov 猜想；帖文将结果表述为针对每个环面结的一族无穷对象的统一结论。
- [Rock Matrix 开源 EdgeRock-4B，以固定容量记忆挑战长程推理的显存瓶颈](https://x.com/testingcatalog/status/2116500778814697819) — TestingCatalog 报道 Rock Matrix 开源 EdgeRock-4B：模型完整保留最近 1024 个 token，并将更早的重要信息写入独立记忆库；项目方报告其在 AIME 2024–2026 平均 pass@1 达 82.9%。
- [Anthropic 让数千个 Claude 代理自动寻找训练数据监控器的盲点](https://x.com/AnthropicAI/status/2116349211549843666) — Anthropic 公布自动化微妙涌现失配研究：让数千个 Claude 代理尝试规避训练数据监控器，生成表面无害却会传授失配行为的文本样本，用于改进后续监控器。

## AI × Chem

采集 1208，候选 60，精选 8。来源状态：各来源已完成

- [Small molecule structure elucidation from NMR spectra with generative and reasoning models](https://www.biorxiv.org/content/10.64898/2026.10.29.762711) — 提出 ChefNMR2 原子级 flow-matching 模型及 ChefNMR2-Agent，依据分子式和一维 1H、13C NMR 光谱自动生成并推理小分子结构；在多项基准上优于现有工具，并解析了四种新型天然产物。
- [Task-Dependent Performance of GNNs and Pretrained Models in ADMET Prediction](https://www.biorxiv.org/content/10.64898/2026.10.26.761652) — 在六个 Therapeutics Data Commons ADMET 终点上，以 scaffold-split 和匹配调参预算比较 GNN、ChemBERTa、MolCLR 及分子指纹，发现没有模型家族普遍占优，性能高度依赖具体终点和评估协议。
- [LPT: Orchestrating bounded agentic loops for automated protein binder design](https://www.biorxiv.org/content/10.64898/2026.10.29.762730) — 提出 LPT（little protein tiger），用固定编排的有界 LLM 循环、工具调用和约 14000 篇论文的整理数据库，仅凭自然语言提示完成蛋白质结合体设计，并针对 CALCRL/RAMP1、PD-1/PD-L1 和 PVR-TIGIT 生成候选。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1796，候选 60，精选 9。来源状态：medRxiv: TimeoutError: The read operation timed out

- [flashscenic: Accelerated GRN Analysis with RegDiffusion for Large-Scale Single-Cell Data](https://www.biorxiv.org/content/10.64898/2026.10.26.761795) — preprint；flashscenic 将 SCENIC 基因调控网络分析重构为 GPU 张量计算，并在大规模 AML 单细胞图谱上进行整合基准测试。
- [An Agentic AI Pipeline for an Evidence-Grounded Environmental Health Public Information System: Development and Evaluation](https://europepmc.org/article/PPR/PPR1353251) — preprint；构建证据约束的 agentic AI 环境健康信息系统，将实时环境数据与健康指南整合为社区尺度回答。
- [GlioMIL: A Frozen-Backbone Multiple-Instance Learning Framework for Calibrated and Explainable Glioma Radiogenomics](https://europepmc.org/article/PPR/PPR1353920) — preprint；GlioMIL 用冻结的 ImageNet 预训练骨干和注意力 MIL 从多对比 MRI 预测胶质瘤分子状态，并通过消融与校准分析揭示结构化特征的作用。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 406，候选 60，精选 7。来源状态：各来源已完成

- [VeriCUA: Verification as Agentic Exploration for Computer-Using Agents](https://arxiv.org/abs/2610.40578v1) — VeriCUA 将任务完成验证建模为跨平台的主动证据搜集：先构造任务量规，再选择 GUI 或代码检查，并按显式证据规则合并结果。摘要称其在多种在线、离线环境和观测模态下提升了与参考标签的一致性，尤其改善困难离线案例并减少在线的虚假完成判定。
- [EnvOS: Auditing Computer-Use Agents When the World Moves On : Phenomenon-Based Task Construction, Certification, and Evidence-Based Evaluation](https://arxiv.org/abs/2610.40246v1) — EnvOS 用经认证的动态环境评测计算机使用代理：运行前验证环境变化、可解性和评分器，运行后用归档证据复核结果。摘要报告了临床预约和保险理赔中的对照实验，以及对损坏轨迹的盲测，显示环境变化呈现方式会显著影响代理表现，且审计流水线能发现评分问题。
- [From the Transformer to a Formal Semantics of Coordinated Transformations](https://arxiv.org/abs/2610.39735v1) — 论文从 Transformer 出发，抽象出一类参数化变换的协调系统，定义向量的外延/内涵解释、参数结构的二阶解释以及“变换概念”，并分析注意力头和残差连接的共同代数—语义核心。结果是形式语义框架，而非对模型数学推理能力的直接基准测试。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 55，候选 49，精选 9。来源状态：各来源已完成

- [@AnthropicAI：New Anthropic research: Automating subtle emergent misalignment research. Red-teaming is a vital part of model safety te](https://x.com/AnthropicAI/status/2116349211549843666) — Anthropic介绍一项自动化微妙涌现失配研究：让数千个 Claude 代理尝试规避训练数据监控器，并生成表面无害、实际会传授失配行为的文本。
- [@jaseweston：Claim: Humans & AI are better together if we want to recursively (co-)improve to a brighter future for *humanity* Instea](https://x.com/jaseweston/status/2115992445930311714) — Jason Weston发布新论文，围绕人类如何引导研究代理、代理奖励劫持、人与代理交互及沟通提出 Autobenchmark、HackBench、AutoInteract 和 unslopping AI 四项工作。
- [@AnimaAnandkumar：Inspired by the spinor nature of spin–orbit-coupled electronic states, we introduce eSpinor, an SU(2)-equivariant graph ](https://x.com/AnimaAnandkumar/status/2116393184641315017) — Anima Anandkumar介绍 eSpinor：一个施加 SU(2) 等变归纳偏置的图神经网络，用于预测自旋轨道耦合相关磁性，并报告了对未见配体、单分子磁体和溶剂迁移预测的改进。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 14，候选 14，精选 3。来源状态：GitHub Releases: IncompleteRead: IncompleteRead(1627067 bytes read, 15137 more expected)

- [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) — HKUDS/DeepTutor 是面向终身个性化辅导的 AI 智能体系统，结合深度研究、RAG、多智能体协作和 CLI 工具；11 月 1 日 GitHub Trending 第 10 名，当日新增 1035 颗星。
- [Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas) — Orkas-AI/Orkas 是本地优先的桌面 AI 团队：由 Commander 将目标拆成待办，协调 16 个内置专业智能体，并接入 Claude Code、Codex、OpenCode、OpenClaw 和 Hermes，支持项目、定时自动化与连接器；11 月 1 日排名第 11，当日新增 1118 颗星。
- [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — THU-MAIC/OpenMAIC 提供一键启动的开放式多智能体互动课堂，将多个智能体组织成沉浸式学习体验；11 月 1 日 GitHub Trending 第 12 名，当日新增 115 颗星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
