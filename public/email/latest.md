# AIxDaily · 2026-09-11

今日精选：AI × Chem 14 项，AI × Bio 12 项，AI × Math 3 项，AI Voices 7 项，Engineering 8 项。9月11日的精选以预印本为主：化学侧聚焦聚合物文献结构化提取、反应机理评测与晶体生成；生物侧覆盖蛋白组尺度虚拟细胞和质谱基础模型；数学侧关注可验证推理。今日未见精选的同行评议论文。公开观点仅作为发布方陈述呈现；工程侧则有推理与训练工具的软件发布。

## 今日重大进展

- [OpenAI 称万智能体在 88 小时提出 Navier–Stokes 奇性证明](https://x.com/OpenAI/status/2097374643518640382) — OpenAI 在官方帖文中称，一款仍在训练的内部模型协调约 1 万个 AI 智能体，在 88 小时内提出受迫 Navier–Stokes 方程有限时间奇性的解析证明，并完成 Lean 形式化。
- [ProtiCelli 公布蛋白组尺度人类细胞虚拟显微图像资源](https://www.biorxiv.org/content/10.64898/2026.03.31.715748) — 研究团队在预印本中提出 ProtiCelli：仅以三种细胞地标染色为条件，从 Human Protein Atlas 图像生成 12,800 种人类蛋白的虚拟显微图像，并发布含 3,070 万张图像的 Proteome2Cell 资源。
- [DeepSeek 发布原生多模态 V4.1-Flash API](https://x.com/deepseek_ai/status/2097930620680941732) — DeepSeek 在官方帖文中发布 V4.1-Flash：该 API 支持原生多模态，并取代 V4-Flash 与 V4-Flash-Vision-Exp。发布方称，多方测试显示其在性能、成本、速度和总运行时间上优于 V4-Pro。

## AI × Chem

采集 832，候选 60，精选 14。来源状态：bioRxiv: RuntimeError: Unable to fetch https://api.biorxiv.org/details/biorxiv/2026-09-08/2026-09-11/270: The read operation timed out

- [PolyReader: an agentic LLM pipeline for extracting structured data from unstructured polymer scientific literature](https://doi.org/10.26434/chemrxiv.15008614/v1) — 提出 PolyReader：以论文及补充信息的层级结构为导航、带来源页码追溯的 LLM 代理，用于提取聚合物样本级数据；在42篇论文人工标注基准上显著优于单轮提示。
- [TSBench: A physics-grounded benchmark for evaluating LLM understanding of chemical reaction mechanisms](https://arxiv.org/abs/2609.08503v1) — TSBench 让 LLM 代理借助结构编辑工具构造过渡态猜测，并用自动量子化学流程按反应路径作物理判定，从而测量其对反应机理的理解。
- [uFlowCSP: Crystal Structure Prediction using Mean flow generative models](https://arxiv.org/abs/2609.09799v1) — uFlowCSP 以 MeanFlow 生成模型进行晶体结构预测，通过学习平均概率流速度，将一次生成所需的网络评估降至1–5次，并在 MP-20 与 CSPBench 上比较性能。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2321，候选 60，精选 12。来源状态：各来源已完成

- [Generative machine learning unlocks the first proteome-wide image of human cells](https://www.biorxiv.org/content/10.64898/2026.03.31.715748) — ProtiCelli 以三个细胞地标染色为条件，从 Human Protein Atlas 图像学习生成 12,800 种人类蛋白的虚拟显微图像，并发布 Proteome2Cell 虚拟细胞资源。
- [Learning from tandem mass spectra at scale with a self-supervised foundation model for proteomics](https://www.biorxiv.org/content/10.64898/2026.09.03.747733) — InstaNovo-FM 在 16.3 亿条 MS/MS 谱图和 1.846 亿条高置信度注释上预训练，为蛋白质组学谱图提供可迁移的自监督表征。
- [Perturbation-Aware Neural ODE (pNODE) Learns Microbiome Dynamics from Clinical Data and Predicts Gut-Borne Bloodstream Infections in Patients Receiving Cancer Treatment](https://www.biorxiv.org/content/10.1101/2025.11.26.690798) — pNODE 将微生物丰度与时间分辨的抗生素扰动纳入 Neural ODE，在超过 1,000 名 allo-HCT 患者的临床数据中预测肠源性血流感染风险相关轨迹。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 633，候选 60，精选 3。来源状态：各来源已完成

- [From Symbolic Perception to Logical Deduction: A Framework for Guiding Language Models in Geometric Reasoning](https://arxiv.org/abs/2609.10335v1) — 提出将几何图解析为符号表示、再由 Symbolic Solver 进行形式演绎的框架，并以 2025 年中国中考几何难题评测其表现。
- [StochBench: A Domain-Specific Benchmark for Stochastic Processes in Lean](https://arxiv.org/abs/2609.09264v1) — 发布 StochBench：覆盖随机过程的 450 题 Lean 4 形式化证明基准；基于 Opus 4.8 的智能体在每题 15 分钟限制下证明了 157 题。
- [Proof-Carrying Cognition: Closing the Verification Gap with Reality-Settled Reward](https://arxiv.org/abs/2609.09776v1) — 从理论与程序合成实验分析不可靠验证器在优化压力下的失效，并提出以现实结算标签约束奖励的 proof-carrying cognition 及 Soundness-under-Pressure 指标。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 75，候选 60，精选 7。来源状态：各来源已完成

- [@OpenAI：This model represents a step-function improvement on many benchmarks, and its training is ongoing. Our internal model gr](https://x.com/OpenAI/status/2097374643518640382) — OpenAI 在帖文中称，其仍在训练的模型在多项基准上有“阶跃式”提升；其内部团队以约 1 万个协同 AI 智能体在 88 小时内得到 Navier–Stokes 问题的解。这是发布方陈述，帖文本身未提供完整证明、基准细节或独立核验。
- [@Thom_Wolf：Two big updates. 1. I published an FT op-ed on the OpenAI/HF incident and follow-ups. 2. We're starting an Open Alignmen](https://x.com/Thom_Wolf/status/2098080470235762702) — Hugging Face 联合创始人 Thomas Wolf 表示，他已在《金融时报》发表关于 OpenAI/HF 事件及后续进展的评论，并称 Hugging Face 正在组建面向开源模型安全、对齐和网络安全的开放对齐团队。团队范围与后续产出尚未在帖文中展开。
- [@deepseek_ai：V4.1-Flash is now live on the DeepSeek API with native multimodal support. Set your model to deepseek-flash. V4-Flash an](https://x.com/deepseek_ai/status/2097930620680941732) — DeepSeek 在官方帖文中宣布 V4.1-Flash 已上线 API、支持原生多模态，并说明旧的 V4-Flash 与 V4-Flash-Vision-Exp 已退役；关于其优于 V4-Pro 的性能、成本、速度和总运行时间，则是帖文归纳的“多方测试”结论。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 70，候选 60，精选 8。来源状态：各来源已完成

- [v1.3.0rc26](https://github.com/NVIDIA/TensorRT-LLM/releases/tag/v1.3.0rc26) — NVIDIA/TensorRT-LLM 发布 v1.3.0rc26：增加 DeepSeek-V4、Qwen3.8 Flash Next、Kimi K3 等模型与硬件支持，补齐 Responses API，并带来 MoE、KV cache 和多节点推理优化；同时包含破坏性 API 调整与 RL 控制端点认证。
- [v1.13.0](https://github.com/huggingface/trl/releases/tag/v1.13.0) — Hugging Face TRL v1.13.0 新增长上下文训练指南与可运行示例：发布说明给出在单个 8×H100 节点上，以 Qwen3-8B 训练 1,048,576-token 序列的测量配置；同时继续扩展训练工具链。
- [alsk1992/CloddsBot](https://github.com/alsk1992/CloddsBot) — CloddsBot 位列当日 GitHub Trending 第 4 名，新增 299 星。它是一个可自托管的 AI 交易智能体，仓库称其可在预测市场、交易所、链上 DEX 与多条 EVM 链上扫描机会、执行交易和管理风险。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
