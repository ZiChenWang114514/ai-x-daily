# AIxDaily · 2026-09-29

今日精选：AI × Chem 16 项，AI × Bio 14 项，AI × Math 16 项，AI Voices 9 项，Engineering 3 项。今日五频道共同日期为 2026-09-29。前三项显示，化学与生物聚焦虚拟筛选、低数据药物设计、RNA 生成模型及临床蛋白组/眼科验证；数学频道集中于由求解器复核的硬件形式化验证。AI Voices 是公开 X 观点，讨论代理沙箱与文本质量；Engineering 则是 Codex、OpenAI Python SDK 和 LangChain 的软件发布。上述论文均标为预印本，未见同行评议论文；帖文观点与软件版本不等同于论文结论。

## 今日重大进展

- [NVIDIA Open Agent Safety Platform 发布：把代理安全移到模型之外](https://x.com/Thom_Wolf/status/2104570048459190762) — Thomas Wolf 介绍 NVIDIA OpenShell 与 Sentry：沙箱隔离代理、外部监管器托管凭据，Z3 检查权限，BlueField-4 DPU 独立监控。
- [AnewDDE 把结构预测、分子设计与实验决策串成闭环药物发现引擎](https://europepmc.org/article/PPR/PPR1328052) — 预印本提出 AnewDDE，将结构预测、亲和力估计、分子设计、LLM 推理和实验决策连成闭环；在纳米抗体发现示范中，报告 10.7% 的单个位数纳摩尔结合体命中率，并用 SPR 实验验证。

## AI × Chem

采集 2498，候选 60，精选 16。来源状态：各来源已完成

- [TopU-LBVS: A Realistic Multi Target Benchmark for Ligand Based Virtual Screening](https://arxiv.org/abs/2609.29740v1) — 提出 TopU-LBVS 多靶点配体虚拟筛选基准，基于 ChEMBL~35 构建覆盖93个蛋白靶点、7类蛋白的属性匹配和结构相似硬负样本库，并提供三种固定评测协议和十类基线。
- [Target-Specific De Novo Drug Design via Fine-Tuned Language Models and Molecular Docking, Molecular Dynamics Simulation Validation](https://doi.org/10.26434/chemrxiv.15009523/v1) — 将 Qwen 2.5 0.5B 微调为从蛋白质氨基酸序列生成分子 SELFIES，并结合束搜索、随机采样、分子对接、分子动力学和 MM/PBSA 对代表性化合物进行验证。
- [RNASeek: A Cross-Phyla Generative Foundation Model for Multipurpose RNA Modeling and Reinforcement Learning-Based Design](https://www.biorxiv.org/content/10.64898/2026.09.24.754173) — 提出1.6-billion-parameter 的 RNASeek 生成式基础模型，在跨物种转录组上预训练，并通过功能预测器和 GRPO 强化学习设计具有目标核酶自切活性和 mRNA 稳定性的 RNA 序列。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 3442，候选 60，精选 14。来源状态：各来源已完成

- [AnewDDE: An Agentic Drug Discovery Engine for Biomolecular Interaction Modelling and Closed-Loop Design](https://europepmc.org/article/PPR/PPR1328052) — AnewDDE 将结构预测、亲和力估计、分子设计、LLM 推理和实验决策整合为闭环药物发现引擎，并在纳米抗体发现中报告 SPR 验证的结合体。
- [Differentiating benign from malignant adnexal masses by biomarker-agnostic plasma proteomics using adaptive machine learning](https://europepmc.org/article/PPR/PPR1328467) — ADAPT-MS 直接从 discovery-mode 质谱血浆蛋白组区分良恶性附件包块，在多中心前瞻性研究中完成内部、外部和与 O-RADS/CA-125 的比较验证。
- [Detecting Glaucoma Across Multi-ethnic Myopic and Non-Myopic Populations Using an Uncertainty-Aware Vision Transformer: A Multicentre Model Development and Validation Study](https://arxiv.org/abs/2609.29433v2) — 不确定性感知的 ViT-B/16 在 56,483 张眼底照片上开发，并在三大洲 16 个独立数据集和高近视亚组中进行多中心验证。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 2000，候选 60，精选 16。来源状态：各来源已完成

- [Agentic-IC3: Enabling Semantic Proof Search in IC3 Model Checking](https://arxiv.org/abs/2609.27162v1) — Agentic-IC3 将语言模型代理接入 Pono 的字级 IC3 模型检查器，用 RTL 语义指导不变式与引理搜索，并由后端验证所有提议。
- [SLED-IFV: Solver-Validated LLM-Guided Decomposition for Scalable Hardware Information-Flow Verification](https://arxiv.org/abs/2609.25637v1) — SLED-IFV 让语言模型提出硬件信息流验证的语义分解，再由控制器和形式化后端检查并接受这些证明工件。
- [EquivSVA: A Formally Verified Dataset of Behavioral Assertions Across Equivalent RTL Implementations](https://arxiv.org/abs/2609.26751v1) — EquivSVA 按行为族组织形式化验证的数据集：每个行为由四种结构不同但外部等价的 RTL 实现、金标准属性、突变体及验证证据组成。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 58，候选 56，精选 9。来源状态：各来源已完成

- [@Thom_Wolf：In July, AI agents running a security test escaped their sandbox and ended up inside @huggingface's servers. So today we](https://x.com/Thom_Wolf/status/2104570048459190762) — Thomas Wolf 介绍 NVIDIA Open Agent Safety Platform、OpenShell 与 Sentry 的代理安全架构。
- [@AndrewYNg：The OpenAI-Hugging Face hack was enabled by weak sandboxing. It is great that Nvidia is releasing open source tools for ](https://x.com/AndrewYNg/status/2104660347730969087) — Andrew Ng 说明 OpenWorker 将基于 NVIDIA OpenShell，为网络安全代理提供确定性沙箱与审计。
- [@jaseweston：Claim: we've solved the AI slop problem (!) 💩🧹✨ Blog post: https://facebookresearch.github.io/RAM/blogs/unslop/ 🧵1/5 Key](https://x.com/jaseweston/status/2104564368792854860) — Jason Weston 介绍 RL-XAR：从专家写作中学习评分标准，以提升模型生成的科学、文学和百科文本质量。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 65，候选 60，精选 3。来源状态：各来源已完成

- [0.158.0](https://github.com/openai/codex/releases/tag/rust-v0.158.0) — openai/codex 发布 rust-v0.158.0，新增 MCP 预注册 OAuth 客户端密钥、exec-server WebSocket bearer token、透明背景图像编辑，并修复 Windows/Linux 沙箱与权限审查问题。
- [v3.20.0](https://github.com/openai/openai-python/releases/tag/v3.20.0) — openai/openai-python 发布 v3.20.0，加入 Agents credential/session 选项和 Responses WebSocket 增量快照，并修复 TLS 重试、实时转录时序与 WebSocket 队列处理问题。
- [langchain==1.4.3](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.4.3) — langchain-ai/langchain 发布 langchain==1.4.3，支持 Bedrock Mantle 聊天模型，识别无 profile 的 GPT-6 结构化输出，并修复 fallback 缓存设置和 create_agent 无效工具调用。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
