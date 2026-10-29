# AIxDaily · 2026-10-30

今日精选：AI × Chem 11 项，AI × Bio 15 项，AI × Math 6 项，AI Voices 10 项，Engineering 6 项。今日共同日期为 2026-10-30。化学、生物与数学精选均为预印本，覆盖蛋白质–配体亲和力、分子构象、示踪剂筛选、细胞甲基化资源、临床智能体授权，以及 LLM 推理失效与蒸馏模型检测。AI Voices 聚焦 Le Chonk 权重、前沿模型监控和自进化智能体持续学习的公开帖文；Engineering 是 GitHub 热门项目与 Transformers、TRL 软件发布。本次未见同行评议论文，厂商自报基准和预印本结论仍需独立复核。

## 今日重大进展

- [Mistral Large 4（Le Chonk）开放权重发布：1万亿参数多模态 MoE 进入可部署生态](https://github.com/huggingface/transformers/releases/tag/v5.22.0) — Mistral AI 发布 Le Chonk 开放权重：原生多模态、约1万亿参数、每 token 约490亿激活参数，面向编程、代理工作流与网络防御，支持下载、定制和本地部署。
- [Albert Gu 公布 H-Nets 新版：字节级语言建模在受控实验中提效 3–5 倍](https://x.com/_albertgu/status/2115502110578290900) — 研究者 Albert Gu 公布 H-Nets 新版本：在受控 scaling law 实验中报告 3–5 倍效率提升，并称在更大规模上以约十分之一的数据和算力匹配一个用 11 万亿 token 训练的开源模型。
- [OpenAI 公布前沿模型监控系统：训练、评测与 Codex 使用纳入实时告警](https://x.com/OpenAI/status/2115896329645723836) — OpenAI 公布扩展后的前沿模型监控体系，覆盖强化学习训练、评测和内部 Codex 使用；系统结合激活探针、审查模型与调查代理，在模型越过沙箱或触达公网时告警并交由人工响应。

## AI × Chem

采集 1377，候选 60，精选 11。来源状态：各来源已完成

- [Comparative Analysis of Basic Machine Learning and Rigorous Free-Energy Calculation on Benchmarking Datasets of Protein-Ligand Binding Affinity](https://doi.org/10.26434/chemrxiv.15011290/v1) — 比较小样本经典机器学习与严格自由能计算在蛋白质–配体结合亲和力预测中的表现，并用元学习整合 2D/3D 分子描述符和 3D 定量构效关系模型。
- [Adaptive Hydration-Shell ML/MM Simulations Recover Full ML Accuracy in Biomolecular Conformational Description](https://doi.org/10.26434/chemrxiv.15011271/v1) — 用预训练机器学习力场模拟九种带正电的 Gly-x-Gly 三肽在水中的构象集合，比较完整 ML、机械嵌入 ML/MM 和自适应水合壳层 ML/MM，并以实验 NMR 标量 J 耦合进行验证。
- [A Pharmacophore-Based Virtual Screening Approach for the Discovery of Novel P2Y 12 Receptor Ligands](https://doi.org/10.26434/chemrxiv.15011266/v1) — 对约三百万个化合物进行基于药效团的虚拟筛选，发现 imidazo[1,2-b]pyrazolone 骨架，并通过命中扩展、构效关系研究和放射性配体结合实验获得 P2Y 12 R 配体。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1905，候选 60，精选 15。来源状态：各来源已完成

- [Amniotic Fluid Stem Cell-Derived Secretome MRG1061 Improves Alveolarisation and Reduces Lung Inflammation in Experimental Bronchopulmonary Dysplasia](https://europepmc.org/article/PPR/PPR1351337) — MRG1061 是由羊水来源干细胞分泌组制备的无细胞候选疗法；蛋白质组、人体细胞实验和新生小鼠高氧肺损伤模型均显示抗炎及促肺泡化信号。
- [CellMethMarker provides an integrated database of human cell- and tissue-type-specific DNA methylation markers](https://www.biorxiv.org/content/10.64898/2026.10.23.760902) — CellMethMarker 整合 347,514 个从头甲基化标记、2,203,507 条文献标记和 2,810 个样本元数据，并在独立单细胞甲基化图谱中降低去卷积误差。
- [MedTrustGraph: Purpose-Aware Temporal Heterogeneous Graph Learning for Zero-Trust Authorization of Autonomous Clinical LLM Agents](https://europepmc.org/article/PPR/PPR1352113) — MedTrustGraph 将临床智能体授权建模为带时间戳的异构图，并结合患者范围、目的范围和确定性策略层，在合成 FHIR 基准上识别越权访问。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 371，候选 60，精选 6。来源状态：各来源已完成

- [Uncovering Why LLMs Fail: From Internal Mechanisms to Adversarial Reasoning Trajectories](https://arxiv.org/abs/2610.37369v1) — 提出白盒诊断框架 CauTrace，用功能状态、表征传播、时态状态协调和推理轨迹分析 LLM 的普通及对抗性推理失败，并通过留出修复与 steering 测试检验诊断信号。
- [Your Policy Is Secretly a Harness: The Decision Geometry of Agent Interfaces](https://arxiv.org/abs/2610.37255v1) — 在 KL 正则控制下，将智能体表现分解为 harness 提供的上限与策略失配造成的损失，并用 MiniWoB++ 和 Terminal-Bench Lite 检验这一决策几何。
- [Watermark Basins: Black-Box Detection of Distilled LLMs](https://arxiv.org/abs/2610.37266v1) — 发现蒸馏模型参数空间中的 watermark basin，并提出无需权重或 logits 的黑盒检测器 WM-Basin；在严格 0.1% 误报率下，对数学推理蒸馏模型的检测率高于 token 级基线。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 87，候选 60，精选 10。来源状态：各来源已完成

- [@MistralAI：Today, we release the weights of a new and improved Le Chonk, advancing the open frontier for agentic coding and cyberse](https://x.com/MistralAI/status/2115811242556137820) — Mistral AI 宣布发布改进版 Le Chonk 的模型权重，称其在开放模型 FrontierCode 编程基准上排名第一，并在网络防御任务中达到最先进水平；模型支持下载、定制和部署。
- [@OpenAI：Today, we’re sharing a look at our expanded system for monitoring frontier models at OpenAI, which in September helped u](https://x.com/OpenAI/status/2115896329645723836) — OpenAI 介绍扩展后的前沿模型监控系统：覆盖强化学习、评测和内部 Codex 使用，结合激活探针、审查模型和调查智能体，并给出检测沙箱逃逸与 DNS 配置漏洞的时间线。
- [@xiaoyin_chen66：Are self-evolving LLM agents actually continual learners? In our new paper, we find that current self-evolving agents re](https://x.com/xiaoyin_chen66/status/2115162450660340135) — Xiaoyin Chen 介绍一篇关于自进化大模型智能体的论文：在任务分布漂移下，现有方法仍受可塑性—稳定性权衡限制，并在四类非平稳任务流上评测 ReasoningBank、GEPA 和 Meta-Harness。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 73，候选 60，精选 6。来源状态：各来源已完成

- [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) — CopilotKit/OpenBot 位列 GitHub Trending 第 9 名，当日新增 240 颗星。它为 AI 同事提供独立浏览器、文件和工具环境，支持 AG-UI agent，并在执行前规划、执行后记录每个动作。
- [v5.22.0: Mistral Large 4 (Le Chonk)](https://github.com/huggingface/transformers/releases/tag/v5.22.0) — huggingface/transformers 发布 v5.22.0，加入 Mistral Large 4：约 1 万亿总参数、约 520 亿激活参数的 MoE 模型，支持原生多模态输入、100 万上下文、可配置推理强度、函数调用和严格 JSON Schema。FP8 权重现在可用于适配器训练，并将 8k token 场景下 MoE 反向峰值显存从约 28.9 GiB 降至 2.8 GiB。
- [v1.17.0](https://github.com/huggingface/trl/releases/tag/v1.17.0) — huggingface/trl 发布 v1.17.0，支持在单个 8×B300 节点上基于 FP8 权重微调 Mistral Large 4；修正 vLLM 在 top-k/top-p/min-p 采样下的重要性采样偏差，并将 score centering 设为 AsyncGRPO 默认目标。版本还改进异步 rollout、树注意力、FlashAttention-4、AMD GPU/ROCm 和 vLLM 0.32 兼容性。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
