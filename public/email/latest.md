# AIxDaily · 2026-08-22

今日精选：AI × Chem 16 项，AI × Bio 15 项，AI × Math 9 项，AI Voices 10 项，Engineering 8 项。今日五频道共同日期为8月22日。所选研究条目均为预印本，未列同行评议论文：化学聚焦药物设计与结构质控，生物覆盖扰动组学与蛋白语言模型，数学着眼形式化研究评测。AI Voices 收录机构的公开研究发布和研究者的公开观点，其中基准成绩仍需按完整评测定义核查；工程频道则为 Diffusers 与 Codex 等软件发布，涉及功能、安全及会话管理更新。

## AI × Chem

采集 1821，候选 60，精选 16。来源状态：各来源已完成

- [Systematic Benchmarking of AI-Based Molecular Generation Models for Structure-Based Drug Design](https://www.biorxiv.org/content/10.64898/2026.08.14.744939) — 在176个蛋白—配体体系上系统比较12类生成与优化方法，并以整合受体构象集合、集合对接和蛋白—配体相互作用图的SAFC补充传统打分。
- [Resolution-standardized evaluation of ligand atomic coordinates in crystallographic structures using machine learning](https://www.biorxiv.org/content/10.64898/2026.08.17.745351) — 提出原子级aBCC指标及3D-CNN模型QAEmap，用分辨率标准化的方式评估晶体结构中配体坐标与电子密度的一致性。
- [Monroe: A Molecular Foundation Model for In-Context Probabilistic Inference](https://arxiv.org/abs/2608.18982v1) — Monroe以超过8100万PM6分子预训练，并结合立体化学图表示、构象去噪和TabPFN下游预测，用于数据有限条件下的生物测定活性预测。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2791，候选 60，精选 15。来源状态：各来源已完成

- [Signature Recontextualization: Mapping perturbational signatures across biological contexts](https://www.biorxiv.org/content/10.64898/2026.08.14.744937) — 提出跨生物学背景扰动转录组预测的标准化基准 sigRecon，在四类 CRISPR、药物和大鼠体内扰动数据上比较 projectCor、netProp、scGPT、STACK 与统计基线，并公开数据、方法和评估工具。
- [Single-cell foundation models benefit from cross-modal training: adding proteomics data beats parameter scaling](https://www.biorxiv.org/content/10.64898/2026.08.14.744845) — 以 440 项质谱研究的 48,843 个蛋白质组样本继续预训练 Tahoe-x1；70M 参数模型在多数原有基准上达到或超过 1B 和 3B 参数 RNA-only 模型，并改善保留的蛋白质扰动基准迁移。
- [A contextualised protein language model reveals the functional syntax of bacterial evolution](https://www.biorxiv.org/content/10.1101/2025.07.20.665723) — Bacformer 将逾 130 万个细菌基因组表示为有序蛋白质序列进行预训练，报告了蛋白质互作、操纵子、表型和合成蛋白质组设计任务的结果，并对操纵子结构进行了实验验证。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 513，候选 60，精选 9。来源状态：OpenReview: RuntimeError: 未配置 OpenReview 账号

- [FormalTCS: Benchmarking End-to-End Frontier Formal Theoretical Computer Science Research of Large Language Models](https://arxiv.org/abs/2608.20153v1) — FormalTCS 以近期顶会论文中的定义、假设和 Lean 证明为基础，评测模型完成端到端理论计算机科学研究的能力，并报告自动形式化仍是主要短板。
- [Grading the Graders: Verification Autonomy Levels (L0-L5) for LLM Reasoning](https://arxiv.org/abs/2608.19009v2) — 该工作提出 Verification Autonomy Levels（VAL），按验证规范的来源及判定可保证的内容，区分 LLM 自述、客观真值和可判定形式系统中的验证能力。
- [Preference Reasoning under Indeterminacy in Large Language Models](https://arxiv.org/abs/2608.18631v1) — 该研究将偏好推理中的不定性区分为认识论不定性和结构性不定性，并测试语言模型能否识别问题是否存在确定解。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 83，候选 60，精选 10。来源状态：各来源已完成

- [@NVIDIAAI：We benchmarked 300+ NVIDIA verified skills to see how much they actually help agents on real tasks. Same task, same mode](https://x.com/NVIDIAAI/status/2090113635683340622) — NVIDIA 表示，其在相同任务、模型和设置下比较了 300 余项已验证技能，并报告技能带来三项明显增益。帖文未给出任务构成、指标定义和统计不确定性；编辑认为，其开源评测器及对技能效用的量化主张值得工程团队进一步核查。
- [@NVIDIAAI：Our general-purpose coding agent just scored 100% on the ARC-AGI-3 interactive reasoning benchmark. NVIDIA AVO completed](https://x.com/NVIDIAAI/status/2090786258981466231) — NVIDIA 宣称其通用编程智能体 AVO 在 25 个公开环境中完成 183 个关卡，并据此称在 ARC-AGI-3 交互式推理基准取得 100%。候选集中同时存在对“公开演示集”与完整基准不能混同的专业质疑；编辑认为该结果重要，但应以独立评测和完整基准定义为准。
- [@fchollet：This is very nice work from NVIDIA. Like all high-performing approaches on ARC-AGI-3, it uses deep learning-guided on-th](https://x.com/fchollet/status/2090838046937645398) — François Chollet 认为 NVIDIA 的工作“非常好”，并将其归入以深度学习引导、即时合成符号世界模型的高表现 ARC-AGI-3 方法。其核心观点是：公开演示集的满分不能表述为完整 ARC-AGI-3 基准的满分；编辑认为这是对近期基准传播中评测范围的必要澄清。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 62，候选 60，精选 8。来源状态：各来源已完成

- [Diffusers 0.40.0: New pipelines, tensor-parallel support, improved CLI, and more](https://github.com/huggingface/diffusers/releases/tag/v0.40.0) — huggingface/diffusers v0.40.0 新增多套视频、音乐、音频与图像编辑管线，将 Modular Diffusers 转为稳定支持；加入 CUDA 与 AWS Neuron 的张量并行推理，并修复分片检查点索引可能导致的路径遍历与越界文件读取问题。
- [0.149.0](https://github.com/openai/codex/releases/tag/rust-v0.149.0) — openai/codex rust-v0.149.0 为 TUI 增加交互式 codex agents 任务面板、工作目录命令与 codex queue，并扩展 SDK 精确配置覆盖和 max、ultra 推理强度。
- [0.148.0](https://github.com/openai/codex/releases/tag/rust-v0.148.0) — openai/codex rust-v0.148.0 增加 TUI 对话导出、会话 fork 与归档恢复、Amazon Bedrock Runtime 提供方和异步 Hooks/MCP 调用，同时强化会话恢复、连接恢复与 Windows、Linux 沙箱限制。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
