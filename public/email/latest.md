# AIxDaily · 2026-10-28

今日精选：AI × Chem 12 项，AI × Bio 14 项，AI × Math 15 项，AI Voices 10 项，Engineering 4 项。聚焦预印本和软件发布：AI×Chem报道生成模型设计MMP12肽抑制剂及肽、蛋白互作预测；AI×Bio聚焦罕见病诊断数据泄漏、空间转录组靶点、抗体设计；AI×Math展示LLM与Lean算法证明、鲁棒性攻击和知识图谱推理。AI Voices为公开帖文，涉及Genie 4、GPT-6.1 Terra及Claude辅助数学；Engineering带来DeepTutor、Codex和Diffusers更新。学术条目均为预印本，未宣称同行评议。

## 今日重大进展

- [Axiom 宣布完成有限单群分类定理的 Lean 自动形式化](https://x.com/axiommathai/status/2115089794867040584) — Axiom 在公开帖中宣布，已将约1.5万页、跨越数代数学家工作的有限单群分类定理完整自动形式化为 Lean 代码，并称整个证明已通过计算机验证。
- [LLM 首次在 Lean 中自主提出算法并证明运行时间界](https://arxiv.org/abs/2610.35595v1) — arXiv 预印本提出分阶段流程，让前沿 LLM 自主提出黑箱优化算法、在 Lean 中形式化并证明运行时间界；15 次运行中 12 次完成机器检查的保证。
- [Pythia-1 在22个靶点上设计出具活性的全长抗体](https://www.biorxiv.org/content/10.64898/2026.10.21.760573) — bioRxiv 预印本报告 Pythia-1 全原子生成模型在 22 个治疗靶点上设计全长 IgG；每个靶点最多筛选 48 个候选，获得单纳摩尔级结合或功能活性。

## AI × Chem

采集 1429，候选 60，精选 12。来源状态：各来源已完成

- [Accelerated discovery and optimization of a potent andselective MMP12 inhibitor with the machine learningplatform CAMOLE-1](https://www.biorxiv.org/content/10.64898/2026.10.21.755545) — 介绍 Calico All-Atom Molecule Engine（CAMOLE-1），用全原子扩散模型、物理计算筛选和生化测试，迭代设计并优化 MMP12 肽抑制剂。研究历时约一年合成 270 条肽，并以肽结合晶体结构验证预测结构。
- [AntiOxiPred: Predicting Antioxidant Peptides using Machine Learning Techniques and BLAST](https://www.biorxiv.org/content/10.64898/2026.10.21.760867) — 提出 AntiOxiPred，用 one-hot、序列组成特征、蛋白语言模型嵌入及特征融合预测抗氧化肽；CatBoost 与 BLAST 集成模型在独立测试集和两个外部验证集上取得较高性能，并提供网页、独立程序和 pip 工具。
- [Predicting Protein-Protein Interactions Using Vectorized Sequence Descriptors and Machine Learning Classifiers](https://www.biorxiv.org/content/10.64898/2026.10.21.760860) — 将 120 个 Auto-Covariance、686 个 Conjoint Triad 和 1,820 个 Local Descriptors 序列特征与 SVM、Random Forest 和 XGBoost 结合，用于蛋白质-蛋白质相互作用预测，并在独立 Human-PPI 测试集上评估泛化。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2189，候选 60，精选 14。来源状态：各来源已完成

- [Auditing evaluation artifacts and data leakage in large language model systems for rare disease diagnosis](https://arxiv.org/abs/2610.33592v1) — 预印本：对罕见病诊断中的评估伪影和数据泄漏进行大规模实证审计。
- [An evidence-governed agent harness for spatial transcriptomics prioritizes ICAM-1 as a target in lung fibrosis](https://www.biorxiv.org/content/10.64898/2026.10.22.760550) — 预印本：DeepMAST将空间转录组分析、证据检索和多智能体编排结合，用于靶点优先级排序。
- [Design of full-length agonist and antagonist antibodies for hard targets](https://www.biorxiv.org/content/10.64898/2026.10.21.760573) — 预印本：Pythia-1全原子生成模型在22个治疗靶点上设计全长激动剂和拮抗剂抗体。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 777，候选 60，精选 15。来源状态：各来源已完成

- [Agentic Algorithm Design: LLMs that Propose, Formalise, and Prove Runtime Bounds for Evolutionary Algorithms in Lean](https://arxiv.org/abs/2610.35595v1) — 提出分阶段的 LLM—Lean 流水线，让模型提出黑箱优化算法并形式化证明其期望运行时间界。
- [Attack logics, not outputs: Concept-based Property Attacks for Shortcut Elimination in Neural Networks](https://arxiv.org/abs/2610.34923v1) — 将对抗攻击从最终类别翻转扩展到可解释概念之间的逻辑性质违例，并形式化分析搜索空间。
- [Evolve on Graph: Self-Evolving Knowledge Graph Reasoning without Question Annotations](https://arxiv.org/abs/2610.35598v1) — 提出 Evolve on Graph，通过图自博弈和可符号验证的拓扑合成，让 LLM 在没有问答标注时自我提升知识图谱推理。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 65，候选 58，精选 10。来源状态：各来源已完成

- [@GoogleDeepMind：Here is what is new with Genie 4: photorealism built on Gemini Omni; advanced physics; real-time controls; native audio;](https://x.com/GoogleDeepMind/status/2115114030503166385) — 事实：Google DeepMind介绍Genie 4新增照片级真实感、高级物理、实时控制、原生音频和多步骤事件推理。作者认为这些能力可用于构建安全虚拟环境，以观察智能体和机器人如何导航。
- [@OpenAI：GPT-6.1 Terra substantially outperforms GPT-5.6 Terra on Agents Last Exam, a test of how well agents use software at wor](https://x.com/OpenAI/status/2114780717188272382) — 事实：OpenAI称GPT-6.1 Terra在Agents Last Exam上显著超过GPT-5.6 Terra，达到GPT-6 Astra水平，同时每token价格约为其十分之一，平均任务完成速度超过两者三倍。
- [@__alpoge__：The core algorithm was found on October 16 by an internal Claude research model with 14M output tokens and no human inpu](https://x.com/__alpoge__/status/2114930095009968506) — 事实：帖文称，一个内部Claude研究模型于10月16日发现核心算法，使用约1400万输出token且没有人工输入；Anthropic研究人员随后与Claude合作改进论文呈现，并公开了相关代码仓库。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 56，候选 54，精选 4。来源状态：各来源已完成

- [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) — HKUDS/DeepTutor 登上 GitHub Trending 第 9 名，当日新增 1,587 星。它将多智能体、深度研究、RAG 和 CLI 组合成可持续个性化辅导系统。
- [0.165.0](https://github.com/openai/codex/releases/tag/rust-v0.165.0) — openai/codex 发布 0.165.0：新增内置 Google Cloud Vertex AI 提供商和 GPT-6.1 Terra 模型目录，改进会话选择器与 Agent Command Center，并默认启用部分模型的推理强度动态调整和新用户 memory v2。
- [v0.42.1 — fix component resolution in `from_pretrained` to prevent `trust_remote_code` bypass](https://github.com/huggingface/diffusers/releases/tag/v0.42.1) — huggingface/diffusers 发布 v0.42.1 安全版本，修复 from_pretrained 加载组件时库名解析不当导致的 trust_remote_code 绕过风险。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
