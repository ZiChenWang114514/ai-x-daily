# AIxDaily · 2026-10-20

今日精选：AI × Chem 3 项，AI × Bio 14 项，AI × Math 0 项，AI Voices 8 项，Engineering 3 项。10月20日，AIXChem 与 AIXBio 各精选三项预印本：涉及蛋白结合位点网络、蛋白生成引导、化学蛋白质组学覆盖，以及跨物种基因组模型、蛋白质组学和抗体药物偶联物组合；当前未见同行评议论文入选。AIXMath 今日没有足够高质量更新。AI Voices 汇集三条公开帖文，Engineering 则关注两个 GitHub 热门项目与 JAX v0.12.0 软件发布。

## 今日重大进展

- [研究者发布 Mercury 3，声称扩散式语言模型达到千 token/秒级](https://x.com/StefanoErmon/status/2112222911218291051) — Stefano Ermon 宣布发布 Mercury 3，称其在质量评测上超过 GPT-6 Luna 与 Haiku 5.5，同时吞吐超过每秒 1000 个 token；当前候选仅给出发布者单方面对比。
- [OpenAI 公开 722 篇数学稿件，覆盖 372 个未解问题](https://x.com/lctrnotes/status/2111920313474941227) — 帖文转述 OpenAI 于 10 月 6 日将 722 篇内部模型产出的数学稿件放入公开仓库，涉及 372 个此前未解结果，其中 235 项附有机器检查的 Lean 证明；这是一项研究规模与开放方式的声明。
- [Google Quantum AI 展示 Willow 芯片魔态培育，帖文称误差降低约 40 倍](https://x.com/professorclawai/status/2111851464977011002) — 帖文转述 Google Quantum AI 在《Science》发表 Willow 处理器的首次硬件魔态培育演示，称误差降低约 40 倍并达到创纪录 T 态；候选未提供论文细节。

## AI × Chem

采集 356，候选 41，精选 3。来源状态：各来源已完成

- [Network organization of protein binding-site landscapes across scales](https://www.biorxiv.org/content/10.64898/2026.10.17.759831) — 将 121,673 个经实验鉴定、去冗余的蛋白质配体结合位点编码为 ProtT5 表征，构建互近邻网络，分析结合位点在全局、介观和局部尺度上的组织规律；在激酶中进一步区分蛋白内不同结合区域及重复出现的残基定义微环境，并发现低序列同一性、不同 InterPro 注释蛋白之间的相似识别环境。
- [Generative steering to adapt proteins beyond native biological contexts](https://www.biorxiv.org/content/10.1101/2025.07.11.664238) — 提出 ProVADA 测试时蛋白生成引导框架，通过 Mixture-Adaptation Directed Annealing 采样器在保留功能约束的同时引导预训练蛋白生成器满足外部指定性质；实验上将分泌型 human renin 改造成具有活性且可被药物抑制的胞质蛋白酶，并对两个小鼠单链抗体片段去免疫化。
- [Determinants of cysteine coverage by chemoproteomics](https://www.biorxiv.org/content/10.64898/2026.10.12.758458) — 结合半胱氨酸特征化、可解释机器学习和稳健统计过滤，研究 IA-DTB 化学蛋白质组学中半胱氨酸可检测性的决定因素；模型显示蛋白质丰度和肽段自身性质是 LC-MS 行为的主要决定因素，并提出距离型统计过滤器以提高重复性。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1339，候选 60，精选 14。来源状态：各来源已完成

- [DeepD enables efficient genome modeling and controllable long-context sequence generation across domains of life](https://www.biorxiv.org/content/10.64898/2026.10.13.758170) — Preprint：DeepD 是在所有生命域全基因组序列上训练的、具备单核苷酸分辨率和 1-million-token 上下文的稀疏 mixture-of-experts 基因组基础模型，同时支持序列到功能预测和可控的基因组级生成。
- [Scalable proteomics with multiDIA resolves proteoforms in neurodegenerative disease](https://www.biorxiv.org/content/10.64898/2026.10.16.756994) — Preprint：multiDIA 通过多蛋白酶独立消化与 data-independent acquisition 提升有限样本的蛋白质组覆盖，在 Parkinson's disease 脑样本中解析出单蛋白酶流程无法检测的 proteoform 变化。
- [Antibody-drug conjugate combination therapy targeting LGR5 and MET with different payloads enhances efficacy in preclinical colorectal cancer models](https://www.biorxiv.org/content/10.64898/2026.07.18.739355) — Preprint：研究设计了靶向 LGR5 和 MET、使用不同 payloads 的抗体药物偶联物组合，并在结直肠癌细胞、模型和 patient-derived xenografts 中评估其抑制复发的效果。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 0，候选 0，精选 0。来源状态：各来源已完成

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 61，候选 58，精选 8。来源状态：各来源已完成

- [@StefanoErmon：1/4 Today, we’re releasing Mercury 3. Mercury 3 is by far our most powerful model and the most intelligent diffusion LLM](https://x.com/StefanoErmon/status/2112222911218291051) — Stefano Ermon 宣布发布 Mercury 3，并声称该扩散式语言模型在质量上超过 GPT-6 Luna 和 Haiku 5.5，运行速度超过每秒 1000 个 token。
- [@migtissera：I'm releasing Tess-4.5-27B today. Tess-4.5 surpasses its Qwen3.8-27B base model on our engineering evaluations while usi](https://x.com/migtissera/status/2112184384518488085) — Migel Tissera 发布 Tess-4.5-27B，称其在工程评测中超过基础模型 Qwen3.8-27B，同时减少 30% 的推理 token；模型使用真实工程会话生成的推理轨迹微调。
- [@NVIDIAAI：Already running a model endpoint? What does it take to scale it on Kubernetes? In five minutes, we walk through how NVID](https://x.com/NVIDIAAI/status/2111864348717224259) — NVIDIA AI 介绍 NVIDIA Dynamo 在 Kubernetes 上部署和扩展模型端点的演示，重点是可扩展 worker 与兼容 OpenAI 的端点。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 57，候选 55，精选 3。来源状态：各来源已完成

- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) — headroomlabs-ai/headroom 在工具输出、日志、文件和 RAG 片段进入大模型前进行上下文压缩，提供库、代理和 MCP Server；项目称可让编码智能体减少约20%的令牌，并让 JSON 输出减少60%–95%。2026-10-20 位列 GitHub Trending 第7名，新增317颗星。
- [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) — shiyu-coder/Kronos 是面向金融市场语言的基础模型项目，目标是为金融时间序列建模和预测提供可复用的预训练模型。2026-10-20 位列 GitHub Trending 第12名，新增355颗星。
- [JAX v0.12.0](https://github.com/jax-ml/jax/releases/tag/jax-v0.12.0) — JAX 发布 v0.12.0：新增 erfcinv、polynomial、可定制 rematerialization、MXFP4 缩放矩阵乘、IFRT Proxy 后端、Profiler 会话 API，以及 oneAPI/ROCm 支持扩展；同时移除 custom_remat，并将 x86-64 最低要求提高到 Haswell（AVX2/FMA），要求 NumPy 2.2 或更高版本。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
