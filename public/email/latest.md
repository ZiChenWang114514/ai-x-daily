# AIxDaily · 2026-10-08

今日精选：AI × Chem 16 项，AI × Bio 14 项，AI × Math 15 项，AI Voices 10 项，Engineering 3 项。今日五频道以预印本和公开观点为主，未见可确认的同行评议论文。化学聚焦蛋白语言模型、结构基础模型与 Atom-JEPA；生物覆盖知识图谱查询、药物相互作用和跨物种 miRNA 基准。数学讨论零知识审计、Lean 证明及数值证据。AI Voices 汇集模型能力、生成式药物设计和生物数据合作观点；工程频道呈现 GitHub Trending 软件项目，因 Releases 源超时，未确认新版本发布。

## 今日重大进展

- [OpenAI 将 GPT-6 与 Intelligent UI 推向 ChatGPT 全体用户](https://x.com/OpenAI/status/2107894997538525580) — OpenAI 宣布 GPT‑6 与 Intelligent UI 开始在 ChatGPT 面向所有用户推送；系统可按问题组合文字、图形、图表、按钮、表单等交互元素，让复杂解释和任务操作直接嵌入对话。
- [Anthropic 发布 Claude Haiku 5.5：小模型成本较 4.5 降约75%](https://x.com/claudeai/status/2107894039626277339) — Anthropic 发布 Claude Haiku 5.5，称其是迄今最快、最强且最便宜的 Haiku；官方帖文给出的平均运行成本比 Haiku 4.5 低约75%，并新增可调 effort，在成本与智能之间按任务取舍。
- [flow-1 公开发布：作者称其以 23 倍低成本监测每次智能体运行](https://x.com/skull8888888888/status/2107138967644541129) — 研究者 Robert 在 X 介绍 flow-1：该模型用强化学习发现智能体轨迹错误，作者称其轨迹智能匹配 GPT‑6 Sol，成本低 23 倍，且比 GPT‑6 Luna 低 25%，可免抽样监测每次运行。

## AI × Chem

采集 2051，候选 60，精选 16。来源状态：各来源已完成

- [Protein Language Model-Conditioned Graph Neural Networks for Multitask GPCR Ligand Activity Prediction](https://www.biorxiv.org/content/10.64898/2026.09.27.754816) — 提出融合配体分子图与GPCR蛋白语言模型表示的多模态图神经网络，同时预测定量pActivity和二元活性，并在多种化学与靶点划分下评估其泛化能力。
- [Beyond the Ligand Applicability Domain: Generalization and Local Resolution in Structure-Aware Foundation Models for Affinity Prediction](https://doi.org/10.26434/chemrxiv.15010040/v1) — 系统评估Boltz-2在12个激酶靶点上的亲和力排序、结合口袋敏感性、选择性和化学系列内排序，界定结构感知基础模型从全局优先级到局部类似物决策的能力边界。
- [Atom-JEPA: Joint-Embedding Predictive Architecture for 3D Atomistic Systems](https://arxiv.org/abs/2610.08400v1) — 提出Atom-JEPA，自监督学习框架在无标注三维分子和晶体结构上进行原子级与子结构级联合嵌入预测预训练，并迁移到ADMET、量子化学和晶体物性任务。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2589，候选 60，精选 14。来源状态：medRxiv: HTTP 500

- [ddkg.skill: A Compositional Agent Skill for Translating Biomedical and Bioinformatics Questions into Cypher for the Data Distillery Knowledge Graph](https://www.biorxiv.org/content/10.64898/2026.09.26.754400) — preprint；提出可加载到兼容 LLM 会话中的 ddkg.skill，用于把生物医学与生物信息学问题转化为可验证的 DDKG Cypher 查询。
- [Multimodal Deep Learning for Drug–Drug Interaction Prediction using Structural Biological and Semantic Information](https://europepmc.org/article/PPR/PPR1334611) — preprint；HySEAtt-DDI 融合化学结构、生物相互作用和语义信息预测药物—药物相互作用。
- [pre-miRBench: a multispecies benchmark and reference model for animal precursor microRNA prediction](https://www.biorxiv.org/content/10.64898/2026.09.30.755660) — preprint；pre-miRBench 统一了 71 个动物物种的前体 miRNA 预测基准，并提供可复现参考模型。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 1051，候选 60，精选 15。来源状态：各来源已完成

- [Data, Numbers, and Geometry: Three Tutorials on Numerical Methods, Machine Learning, and Evaluation](https://arxiv.org/abs/2610.07220v1) — 三份面向数学研究的教程，区分数值一致性、预测准确率、结构保证和严格界，并用区间算术检验神经网络残差。
- [zkLLMPoT: Efficient Zero Knowledge Proof of Training for Large Language Models](https://arxiv.org/abs/2610.08258v1) — zkLLMPoT 用零知识证明审计训练后模型在挑战序列上的目标值，在不泄露权重和私有数据的情况下给出可验证结果。
- [LeanPlan: Optimal Planning with LLM-Generated Heuristics and Admissibility Proofs](https://arxiv.org/abs/2610.08246v1) — LeanPlan 让 LLM 生成的启发式函数同时带有 Lean 4 机器检查的可采纳性证明，用于寻找最优规划。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 99，候选 60，精选 10。来源状态：各来源已完成

- [@polynoamial：LLMs have crossed an important threshold: surpassing top human experts on some research problems. Capabilities have been](https://x.com/polynoamial/status/2107947189184164056) — Noam Brown 认为，大语言模型已在部分研究问题上超过顶尖人类专家；他同时强调模型能力仍不均衡，数学领域的突破可能预示其他科学领域的进展。
- [@IsomorphicLabs：Previously, 85% of proteins associated with human disease were deemed intractable – their shapes and function made them ](https://x.com/IsomorphicLabs/status/2107495373455429850) — Isomorphic Labs 表示，过去约 85% 的疾病相关蛋白被视为难以开展传统化学筛选；其帖文称，AI 生成式分子设计正在扩大这些靶点的可开发空间。
- [@pushmeet：Building predictive biology models is one of the most important scientific challenges of our time, but solving this requ](https://x.com/pushmeet/status/2107873568822276533) — Pushmeet Kohli 宣布 Google DeepMind 与 Chan Zuckerberg Initiative 的 Virtual Biology Initiative 合作，建设用于预测生物学的多模态实验数据集。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 13，候选 13，精选 3。来源状态：GitHub Releases: TimeoutError: The read operation timed out

- [morluto/rea](https://github.com/morluto/rea) — rea 使用智能体逆向分析应用行为直至原生二进制；当日 GitHub Trending 第 1 名，新增 4666 星。
- [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) — cmux 是基于 Ghostty 的开源 macOS 终端，为 AI 编程智能体提供垂直标签、通知和可编程的多任务工作区；当日 GitHub Trending 第 9 名，新增 96 星。
- [tester-army/e2e](https://github.com/tester-army/e2e) — tester-army/e2e 提供面向 Web 与移动应用的新一代端到端测试框架，兼容 Playwright 工作流；当日 GitHub Trending 第 12 名，新增 1391 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
