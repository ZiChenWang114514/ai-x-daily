# AIxDaily · 2026-09-06

今日精选：AI × Chem 4 项，AI × Bio 16 项，AI × Math 4 项，AI Voices 5 项，Engineering 0 项。2026年9月6日所参考的精选以预印本为主，未见同行评议论文：化学覆盖光驱动聚合物后修饰、毒性预测与蛋白无序区模型；生物聚焦单细胞和空间组学整合；数学关注三维推理、漏洞修复与知识冲突评测。AI Voices 为模型发布和技术博客等公开更新，能力主张尚待独立检验；工程频道没有精选，未见可确认的软件发布。

## 今日重大进展

- [OpenAI 发布 GPT-6 Astra，瞄准计算机使用、编程与科学工作流](https://openai.com/index/gpt-6-astra) — OpenAI 官方新闻稿发布 GPT-6 Astra，称其为新一代智能模型，并主张它在计算机使用、编程、网络安全和科学任务上具备最先进能力。

## AI × Chem

采集 1142，候选 60，精选 4。来源状态：各来源已完成

- [Catalyst-Free, Visible-Light-Driven Hydrogenation and Giese Addition of N-Hydroxyphthalimide Ester–Containing Polymers Using Hantzsch Esters](https://doi.org/10.26434/chemrxiv.15008271/v1) — 提出以NHPI ester–containing polymers与Hantzsch esters形成EDA complexes为基础的无催化剂、可见光驱动后官能化方法，通过侧链脱羧实现氢化，并扩展至Giese addition。该方法适用于acrylates、polyacrylonitrile和polystyrene等体系，可在自然日光下进行克级反应；调节光强可抑制acrylonitrile copolymer中的交联，Giese addition的官能化程度最高达79%。
- [Analysis of Prompt Engineering for Drug Toxicity Prediction](https://arxiv.org/abs/2609.03635v1) — 系统考察LLMs在药物毒性预测中对角色设定、提示结构与规则解读等提示措辞的敏感性。作者先让LLMs识别毒性相关化学性质，再据此生成数据集并输入机器学习算法；实验显示LLM的自然随机变异大于提示微调带来的影响，而用cheminformatic code提取特征可显著提升模型性能。
- [PredIDR3: A new output-encoding scheme and abundant negative source provide more information for deep learning-based protein intrinsic disorder prediction](https://www.biorxiv.org/content/10.64898/2026.09.01.748564) — PredIDR3是用于从蛋白质序列预测内在无序区（IDRs）的深度卷积模型系列。其采用可容纳size=91滑动窗口的新输出编码，并从PDB和DisProt的非IDRs补充负样本；在CAID3的Disorder-PDB上，AUC_ROC由PredIDR2的0.936提高至0.953，且在CAID3各项指标上与领先方法相当，并提供CAID Prediction Portal与Singularity container访问。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1844，候选 60，精选 16。来源状态：各来源已完成

- [Generative atlasing in universal gene expression space defines cell types and microenvironment spectra during disease progression](https://europepmc.org/article/PPR/PPR1312099) — UniGeneX 将多队列转录组重建到可量化的 Universal Gene Expression (UGE) 空间，并用于肺纤维化和胶质瘤的单细胞—空间图谱分析。
- [FADVI: disentangled representation learning for robust integration of single-cell and spatial omics data](https://www.biorxiv.org/content/10.1101/2025.11.03.683998) — FADVI 以变分自编码器分离批次、标签相关和残余子空间，在 scRNA-seq、scATAC-seq 与高分辨率空间转录组基准中评估整合表现。
- [Global tree encoding of atlas-scale single-cell genomics](https://www.biorxiv.org/content/10.64898/2026.08.31.747971) — MILK 将高维单细胞群体组织为统一树表示，面向图谱尺度的代表性抽样、生成模型训练、基础模型基准和跨物种比较。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 289，候选 60，精选 4。来源状态：各来源已完成

- [GraFT: A Training-Free Framework for Spatial Reasoning in Multimodal Large Language Models via 3D Scene Graphs](https://arxiv.org/abs/2609.03892v1) — GraFT 以紧凑的 3D 场景图、符号几何工具、鸟瞰图和任务相关的自我中心视角，为冻结的多模态大语言模型补充三维空间推理所需的结构信息。
- [PatchBench: Evaluating AI Agents for Vulnerability Patching](https://arxiv.org/abs/2609.04075v1) — PatchBench 面向 C/C++ 漏洞修复代理，针对仅以 PoC 不再触发崩溃作为成功标准所造成的记忆化补丁和表面修复偏差，提出更严格的安全性与语义正确性验证。
- [KC-Bench: A Dynamic Interactive Benchmark for Evaluating Knowledge Conflicts in LLM Agents](https://arxiv.org/abs/2609.03588v1) — KC-Bench 以受控多轮交互任务考察 LLM 代理如何协调用户指令、参数知识与动态环境观测之间的事实、身份和时间冲突。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 14，候选 14，精选 5。来源状态：X: RuntimeError: 未找到 Grok X 检索缓存。请先按 ops/grok/x_harvest_protocol.md 采集

- [GPT-6 Astra: A new generation of intelligence](https://openai.com/index/gpt-6-astra) — 事实：OpenAI 官方新闻稿介绍 GPT-6 Astra，并将其描述为其迄今最智能、最对齐的模型。作者主张：该模型在计算机使用、编程、网络安全和科学方面具备最先进能力。
- [Building a Memory-Driven Agent with NVIDIA NemoClaw](https://developer.nvidia.com/blog/building-a-memory-driven-agent-with-nvidia-nemoclaw/) — 事实：NVIDIA 技术博客发布了使用 NemoClaw 构建记忆驱动智能体的文章。正文可见摘录指出，企业工作涉及随时间变化的消息、决策、项目和责任；缺少这些上下文的智能体需要重建它们。
- [Frontier Reasoning Reaches the Edge: How to Deploy and Optimize Models on NVIDIA Jetson](https://developer.nvidia.com/blog/frontier-reasoning-reaches-the-edge-how-to-deploy-and-optimize-models-on-nvidia-jetson/) — 事实：NVIDIA 技术博客讨论在 Jetson 上部署和优化前沿推理模型。作者观点：在边缘侧运行推理型和智能体式 AI 一直比应有的更困难，直到最近能够多步推理的模型仍过于庞大。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 46，候选 41，精选 0。来源状态：GitHub Trending: TimeoutError: The read operation timed out

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
