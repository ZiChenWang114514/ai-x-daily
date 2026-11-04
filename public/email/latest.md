# AIxDaily · 2026-11-05

今日精选：AI × Chem 14 项，AI × Bio 16 项，AI × Math 16 项，AI Voices 10 项，Engineering 8 项。今日五频道围绕 AI 科研与工程进展展开，但证据类型不同：AI×Chem 与 AI×Bio 的前三项均为 arXiv/bioRxiv 预印本，覆盖亲和力预测、反应图抽取、代谢物结构推断、微生物基因组和三维调控等方向；AI×Math 关注可执行逻辑程序、零阶强化学习与 Lean 证明搜索。AI Voices 前三项是公开 X 帖文，工程频道前三项是 GitHub Trending 项目，不能等同同行评议论文或正式软件版本。

## 今日重大进展

- [研究者公布 Kaplansky 猜想（双曲群情形）的 Lean 4 形式化](https://x.com/Nidhal_Mg/status/2117855877562585487) — 研究者 Nidhal Mghirbi 发布 Lean 4 代码，称其形式化了 Kaplansky 猜想在双曲群情形的主定理，并在项目页给出证明、贡献与来源说明。
- [研究者提出 Weight‑Space Programming：GPT‑6 Astra 直接编辑模型权重](https://x.com/rikiyatakehi/status/2117313742891327994) — Rikiya Takehi 称，GPT‑6 Astra 在无需梯度或训练的情况下仅改写 Qwen3.5‑0.8B 的 0.016% 权重，修复推理循环，数学表现最高提升 6 倍、指令遵循提升 3 倍。
- [Anthropic 公布 Claude 协助解析细菌来源 vault 颗粒首个三维结构](https://x.com/AnthropicAI/status/2118073665296228863) — Anthropic 表示，其生物学团队与 Claude 合作解析了细菌来源 vault 颗粒的首个三维结构，并发现细菌及其感染病毒的类似蛋白也能组装出 vault。

## AI × Chem

采集 2198，候选 60，精选 14。来源状态：各来源已完成

- [Molecular Prior Networks](https://arxiv.org/abs/2611.05103v1) — 提出 Molecular Prior Networks：用在数千个既有亲和力数据集上训练的 Transformer，从带标签的支持分子一次前向预测查询分子的蛋白质—配体亲和力，无需针对新任务重新训练。
- [RxnMiner: A Multimodal Agent for Structured Reaction Data Extraction from Chemistry Figures](https://arxiv.org/abs/2611.02826v1) — 提出 RxnMiner 多模态智能体和 ChemRxn-Bench，用于从包含模板、取代基表和产物网格的化学反应图中恢复结构化、可追溯的反应记录。
- [DEEPNET-LLM: Highly accurate structure prediction of unknown metabolites from mass spectra via their molecular neighborhoods](https://www.biorxiv.org/content/10.64898/2026.10.28.762558) — 提出 DEEPNET-LLM，通过 Molecular Community Networking 将质谱查询限制在全局代谢组的局部邻域，再用 AI 推理传播邻域结构信息，实现未知代谢物结构预测。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2780，候选 60，精选 16。来源状态：各来源已完成

- [MicrobeRT: A Framework and Suite of Fine-tuned Language Models for Genomic Sequences](https://www.biorxiv.org/content/10.64898/2026.11.03.763945) — MicrobeRT 将多个基因组语言模型微调为可执行物种分类、抗生素耐药基因检测和致病性评估的宏基因组分析套件。
- [Decoding Cell-type Specific Gene Regulation with CellReg3D by Integrating DNA Large Language Models and 3D Genome Structure](https://www.biorxiv.org/content/10.64898/2026.11.01.763421) — CellReg3D 将 DNA 语言模型编码的局部序列模式与 Hi-C 推断的三维染色质相互作用结合，用于细胞类型特异性基因调控建模。
- [A Biologically Inspired Attention Model for Neural Signal Analysis](https://www.biorxiv.org/content/10.1101/2024.08.13.607787) — SPARKS 将自注意力、Hebbian 学习和预测编码式训练结合，用于在神经信号解码中同时获得高性能和可解释的功能连接。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 889，候选 60，精选 16。来源状态：各来源已完成

- [ALBI: LLM-Guided Inductive Logic Programming via Iterative Generate-Test-Constrain Refineme](https://arxiv.org/abs/2611.05039v1) — ALBI 用大语言模型提出归纳逻辑程序候选，再由 SWI-Prolog 形式验证器测试并根据诊断反馈迭代修正；在30个标准 ILP 基准上，三种模型均达到100%成功率，并通过语义匿名化测试。
- [The Cost of Mismatch: Noise Amplification in Zeroth-Order Reinforcement Learning](https://arxiv.org/abs/2611.03260v2) — 论文建立零阶优化梯度估计的方差理论，说明匹配数据可消除噪声放大，并提出 ZO-BOLT；显式收敛保证和端到端实验支持了理论预测。
- [Reap: Uncovering Monte Carlo proof search with a lightweight model](https://arxiv.org/abs/2611.02678v1) — Reap 在 Lean4 中实现策略—价值引导的蒙特卡洛树搜索，并共享证明状态转移、AND-OR 搜索与回放验证；1.7B 参数的 Reaper-1 在 miniF2F-test 上达到 pass@32 79.9%。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 84，候选 60，精选 10。来源状态：各来源已完成

- [@MIT_CSAIL：What if an optimizer could think and react while a neural network trains? MIT researchers developed OPAL: a deep learnin](https://x.com/MIT_CSAIL/status/2117300744168608012) — 事实：MIT CSAIL 表示，OPAL 是一种能观察训练动态并在训练过程中重写自身代码的 AI 智能体优化器，已在视觉和语言任务上提升模型性能。
- [@rikiyatakehi：We asked GPT-6 Astra to edit Qwen3.5-0.8B weights to improve math. It directly changed only 0.016% of weights, fixing 0.](https://x.com/rikiyatakehi/status/2117313742891327994) — 事实：Rikiya Takehi 称，GPT-6 Astra 对 Qwen3.5-0.8B 的权重直接修改了 0.016%，在无需梯度或训练的情况下修复推理循环，并使数学表现最高提升 6 倍、指令遵循提升 3 倍。作者将其称为 Weight-Space Programming。
- [@0xDing：分享下我们在做真正的 Agent OS 过程中的一些架构思考与工程实践：真实企业是一个多主体、权限互斥且状态持续演进的分布式组织；给单机 Harness 套网页聊天壳子，或往群聊里塞外挂 MCP 的共享机器人，从架构第一天起就注定走不通。](https://x.com/0xDing/status/2117883383489675593) — 原文为中文。作者分享其构建 Agent OS 时的架构思考与工程实践，强调企业环境是多主体、权限互斥、状态持续演进的分布式组织。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 75，候选 60，精选 8。来源状态：各来源已完成

- [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) — NVIDIA 的 Auto Ontology 位列当日 GitHub Trending 第 1 名，新增 2,053 颗星。它用 Python 构建面向数据的语义图推理层，为 LLM 和智能体生成更确定的查询与检索上下文。
- [The-PR-Agent/pr-agent](https://github.com/The-PR-Agent/pr-agent) — The-PR-Agent/pr-agent 位列当日 Trending 第 8 名，新增 279 颗星。它是面向 Pull Request 的开源 AI 审查器，可接入 OpenAI、Anthropic、Ollama 等模型来辅助代码审查。
- [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) — FareedKhan-dev/kimi-k3-in-c 位列当日 Trending 第 11 名，新增 351 颗星。项目用便携式 C99、无 BLAS、无框架、无 GPU 的方式实现 Kimi K3 推理，描述声称可在单 CPU、8.24 GB 内存上运行 2.78 万亿参数模型。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
