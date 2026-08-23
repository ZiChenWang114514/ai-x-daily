# AIxDaily · 2026-08-23

今日精选：AI × Chem 16 项，AI × Bio 15 项，AI × Math 7 项，AI Voices 8 项，Engineering 8 项。今日五线齐发：化学与生命频道主要是预印本，前者覆盖分子生成评测和药物发现验证，后者聚焦跨情境扰动、跨模态单细胞与泛癌预测；数学亦均为预印本，讨论形式化研究和推理验证。AI Voices 收录公开帖文，提供基准与性能主张的观察，尚非同行评议证据。工程频道则为官方软件发布，涉及 Diffusers 与 Codex 的功能、兼容性和安全更新。

## AI × Chem

采集 1807，候选 60，精选 16。来源状态：各来源已完成

- [Systematic Benchmarking of AI-Based Molecular Generation Models for Structure-Based Drug Design](https://www.biorxiv.org/content/10.64898/2026.08.14.744939) — 在176个蛋白—配体体系上系统比较12类结构导向的分子生成与优化方法，并提出结合受体构象集合、集合对接和蛋白—配体相互作用图的SAFC功能分类器。结果显示各类模型各有适用场景，尚无单一方法能同时优化所有成药与计算指标。
- [A multi-agent molecular optimization framework leads to a rapid-recovery intravenous anesthetic candidate with an improved safety margin](https://www.biorxiv.org/content/10.64898/2026.08.17.745149) — MASCOT以三个职责不同的智能体协同图编辑式分子优化，并在六项基准设置中优于比较方法。该框架从remimazolam出发筛得RM-7；动物研究显示其麻醉效力、功能恢复速度和治疗指数均优于母体，同时保留flumazenil可逆性。
- [Learning from Nature: De novo Generative Design of Natural-Product-Inspired Opioid Agonists](https://doi.org/10.26434/chemrxiv.15007728/v1) — 研究以mitragynine pseudoindoxyl的μ-阿片受体特征引导深度生成设计，获得结构不同的新型激动剂。合成化合物中约三分之一具有强受体激活作用，先导物显示良好药代性质、较少脱靶活性和无β-arrestin募集，并由冷冻电镜验证正构位点结合。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2776，候选 60，精选 15。来源状态：各来源已完成

- [Signature Recontextualization: Mapping perturbational signatures across biological contexts](https://www.biorxiv.org/content/10.64898/2026.08.14.744937) — 提出 signature recontextualization 基准，系统比较跨生物学情境预测扰动转录组特征的方法，并发布 sigRecon 开源 R 包。
- [Single-cell foundation models benefit from cross-modal training: adding proteomics data beats parameter scaling](https://www.biorxiv.org/content/10.64898/2026.08.14.744845) — 以 440 项质谱研究的 48,843 个蛋白质组样本对 Tahoe-x1 继续预训练，交叉模态训练在多项评测中达到或超过更大的 RNA-only 模型。
- [PanoraOnc: A pan-cancer clinico-genomic AI model for transferable outcome predictions](https://www.medrxiv.org/content/10.64898/2026.08.17.26354679) — PanoraOnc 在 66 种癌症、84,131 名患者的真实世界临床、基因组与影像资料上预训练，用于跨癌种治疗结局预测与可解释特征发现。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 513，候选 60，精选 7。来源状态：OpenReview: RuntimeError: 未配置 OpenReview 账号

- [FormalTCS: Benchmarking End-to-End Frontier Formal Theoretical Computer Science Research of Large Language Models](https://arxiv.org/abs/2608.20153v1) — FormalTCS 以近期顶会理论计算机科学论文为来源，评测模型从理解定义到 Lean 证明的端到端研究能力。
- [Grading the Graders: Verification Autonomy Levels (L0-L5) for LLM Reasoning](https://arxiv.org/abs/2608.19009v2) — 该文提出 Verification Autonomy Levels (VAL)，按验证规范来源和结论保证程度描述 LLM 推理验证系统。
- [Preference Reasoning under Indeterminacy in Large Language Models](https://arxiv.org/abs/2608.18631v1) — 该研究把偏好推理中的不确定性区分为认识论不确定性和结构不确定性，并考察模型能否识别无确定解的实例。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 71，候选 60，精选 8。来源状态：各来源已完成

- [@rohanpaul_ai：New Alibaba ByteDance paper shows that AI agents can no longer be served like ordinary LLM requests. Because most of the](https://x.com/rohanpaul_ai/status/2090884141101482407) — 帖文转述一篇阿里巴巴与字节跳动论文：研究以 10 个智能体应用构成 AgentSysBench，认为智能体服务的性能瓶颈常跨越工具、记忆、环境和模型，且不一定主要来自模型推理。
- [@fchollet：This is very nice work from NVIDIA. Like all high-performing approaches on ARC-AGI-3, it uses deep learning-guided on-th](https://x.com/fchollet/status/2090838046937645398) — François Chollet 评价 NVIDIA 的 ARC-AGI-3 方案，并指出其采用深度学习引导的即时符号世界模型合成。作者特别认为，公开演示集的满分不能等同于完整 ARC-AGI-3 基准的满分。
- [@EinsiaAI：1/ Recursive self-improvement (RSI) depends on agents improving how AI systems are trained —not just tuning hyperparamet](https://x.com/EinsiaAI/status/2090854778301771909) — Einsia 发布 AI4AI-Bench，称其覆盖 10 个算法家族的 10 个真实研究代码库，用于直接测试智能体改进训练算法的能力；帖文报告当前模型得分仍较低。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 67，候选 60，精选 8。来源状态：各来源已完成

- [Diffusers 0.40.0: New pipelines, tensor-parallel support, improved CLI, and more](https://github.com/huggingface/diffusers/releases/tag/v0.40.0) — huggingface/diffusers v0.40.0 新增多条生成模型 pipeline，并让 Modular Diffusers 进入稳定支持阶段；同时带来 tensor-parallel 推理、量化后端与重要兼容性和安全更新。
- [0.149.0](https://github.com/openai/codex/releases/tag/rust-v0.149.0) — openai/codex 0.149.0 为 TUI 增加 `codex agents` 交互式任务面板、工作目录命令和消息队列，并强化诊断、会话恢复与安全处理。
- [0.148.0](https://github.com/openai/codex/releases/tag/rust-v0.148.0) — openai/codex 0.148.0 支持对话导出、会话 fork 与归档恢复、Amazon Bedrock Runtime 和异步 Hook/MCP 调用，同时修复恢复会话、连接和沙箱限制相关问题。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
