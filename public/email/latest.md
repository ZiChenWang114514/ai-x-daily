# AIxDaily · 2026-10-17

今日精选：AI × Chem 15 项，AI × Bio 12 项，AI × Math 11 项，AI Voices 10 项，Engineering 7 项。2026年10月17日，化学、生物和数学前三项均为预印本：前两者聚焦肽毒性数据、蛋白去免疫化、功能RNA、神经影像模型与临床试验预测，数学侧重Lean证明、探究式推理和神经符号代理。AI Voices为X公开帖文，Engineering为GitHub Trending项目快照。所列条目未见同行评议论文，趋势快照也不等同于软件正式发布。

## 今日重大进展

- [IneqAgent 把不等式证明推进到 Lean：报告 94.09% 解题率并强化多项猜想](https://arxiv.org/abs/2610.20681v1) — arXiv 预印本提出 IneqAgent，将大模型推理和符号计算接入 Lean4；报告基准解出 175/186 题，并给出 Dittert 猜想强化及 Holens–Djokovic (4,4) 不等式的形式化证书。
- [MESSI 用生成式扩散模型设计低免疫原性蛋白，兼顾结构、活性与表位清除](https://www.biorxiv.org/content/10.64898/2026.10.09.758136) — bioRxiv 预印本报告 MESSI：以蛋白结构为输入，通过离散扩散生成避开指定 MHC-II 结合肽的序列。作者在荧光素酶、PD-1 mini-binder 和尿酸酶上实验验证，获得预测无表位且活性更高的变体。
- [Meta AI 发布 816B 开放权重 Muse Spark Open，支持百万上下文与原生多模态](https://x.com/AIatMeta/status/2110779754274292212) — Meta AI 在公开帖中宣布 Muse Spark Open，称其面向编程、智能体和多步推理：总参数 8160 亿、每 token 激活 420 亿，支持百万 token 上下文，并原生处理文本、图像、视频和音频。

## AI × Chem

采集 940，候选 60，精选 15。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=400&max_results=100&sortBy=submittedDate&sortOrder=descending: The read operation timed out

- [NoiTox: A Machine Learning Strategy for Peptide Toxicity Prediction Reveals Label Noise in Benchmark Datasets](https://www.biorxiv.org/content/10.64898/2026.10.08.757741) — 提出 NoiTox 多模型肽毒性预测策略，结合 Boruta 理化/组成/原子描述符、ESM-2 嵌入和图神经网络，并系统评估基准数据中的标签噪声。
- [Protein Deimmunization with a Generative Diffusion Model](https://www.biorxiv.org/content/10.64898/2026.10.09.758136) — 开发生成式离散扩散模型 MESSI，以蛋白质结构为输入设计保留结构、降低 MHC-II 预测表位的蛋白序列，并在 luciferase、PD-1 mini-binder 和 uricase 上进行验证。
- [Programmable design of functional RNAs through multimodal generative learning](https://www.biorxiv.org/content/10.64898/2026.10.14.759035) — 提出 RNAverse 多模态生成模型，从 RNA 序列、实验结构探测谱和功能注释学习可条件化设计语法，并在多类 RNA、5' UTR、基因治疗和疫苗相关场景中进行生成与实验测试。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1707，候选 60，精选 12。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=400&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 429: Unknown Error

- [Neuro-JEPA: Building and Evaluating Health-System Scale Neuroimaging Foundation Models with Mixture of Experts](https://europepmc.org/article/PPR/PPR1340166) — Neuro-JEPA 是一个结合潜在预测学习与稀疏混合专家架构的多模态脑 MRI 基础模型，在 1.55 million 次扫描（428,647 项临床影像研究）上预训练，并在 3 个独立医疗系统、12 个公开数据集的 47 项下游任务中评估。模型在多种单对比度、多模态和跨域任务中整体表现最佳，在数据稀缺的胶质增生和多发性硬化病理任务上较既有基础模型最高提升 15%。
- [inClinico Agent for clinical trial endpoint prediction and prospective evaluation](https://www.medrxiv.org/content/10.64898/2026.10.13.26365373) — inClinico Agent 用注册时可获得的靶点、作用机制、药物形式、试验设计和文献嵌入等特征，分别预测 I–IV 期试验的疗效或安全性终点成功概率。在 2021 年后启动试验的测试集上，疗效模型 AUROC 为 0.828（n=2,347），安全性模型 AUROC 为 0.809（n=1,485），并建立了包含 2,040 项进行中试验的前瞻性 ClinBench。
- [Resolving neurodegenerative and therapeutic crosstalk in biofluid proteomes for Parkinson's disease surveillance](https://www.medrxiv.org/content/10.64898/2026.10.14.26364535) — 研究对 Parkinson's Precision Medicine Initiative 的 832 名参与者开展纵向高通量蛋白质组分析，覆盖 850 份血浆和 1,200 份 CSF 样本，识别出 68 个血浆和 3 个 CSF 疾病负荷生物标志物，以及 4 个血浆疾病活动标志物，并解析了 12 种抗帕金森病药物剂量与蛋白质变化的关系。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 1079，候选 60，精选 11。来源状态：各来源已完成

- [IneqAgent: Agentic Inequality Proving in Lean with Symbolic Computation](https://arxiv.org/abs/2610.20681v1) — IneqAgent 将大语言模型推理、引理级蒙特卡洛树搜索与符号计算后端结合，在 Lean4 中自动生成并核验不等式证明。
- [Evaluating Inquiry Learning in LLM-Based Agents: Hypothesizing, Reasoning, and Exploration](https://arxiv.org/abs/2610.21604v1) — 该工作在可交互的数学 Countdown 环境中评估大语言模型的探索、假设生成和迭代推理能力，并测试教育式脚手架引导。
- [OntoAct: Hypothesis-Based Neuro-Symbolic Agents through Ontological Abstraction](https://arxiv.org/abs/2610.21983v1) — OntoAct 用本体抽象把经验转成可复用公理，由 LLM 提出假设和行动，再由符号验证器检查条件并依据新证据更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 88，候选 60，精选 10。来源状态：各来源已完成

- [@samschapiro：Are large language models more creative than humans at combining ideas? Here, we introduce Kombine, a new benchmark of c](https://x.com/samschapiro/status/2110370039861768457) — Samuel Schapiro介绍Kombine组合创造力基准：测试显示，大语言模型在组合式创造力上超过平均人类，但概念融合仍是最难任务，前沿模型也表现吃力。
- [@onloglogn：Introducing RSI-Inference Bench from Apple ML Research https://github.com/apple-aiml-research/ml-rsi-inference-bench Can](https://x.com/onloglogn/status/2111170954944823685) — Ruixiang Zhang介绍Apple ML Research的RSI-Inference Bench，用真实vLLM和SGLang任务评估智能体能否改进运行AI的系统；项目消耗10万API token和5万GPU小时，当前最佳智能体pass@1为26.7%，且测试仍未饱和。
- [@hardmaru：The AI Scientist v3 is out: The Agentic Scientist. GitHub: https://github.com/SakanaAI/AI-Scientist-v3 Blog: https://pub](https://x.com/hardmaru/status/2110739454948520260) — Sakana AI发布AI Scientist v3“Agentic Scientist”。系统从“一个智能体写一篇论文”转向由并行智能体组成的脚手架，协调整个科研循环；帖文同时提供GitHub、博客和arXiv入口。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 65，候选 58，精选 7。来源状态：各来源已完成

- [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) — Anthropic 官方维护的 Claude Code 插件目录，集中提供 MCP 与 Skills 扩展；10 月 17 日 GitHub Trending 第 1 名，当日新增 1,552 星。
- [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) — 面向科研智能体的技能库，提供 177 个经过验证的技能和 100 多个科学数据库，覆盖生物、化学、医学与药物发现；当日 Trending 第 2 名，新增 1,158 星。
- [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) — CLI-Anything 旨在把各类软件包装成可被智能体调用的命令行接口；当日 Trending 第 4 名，新增 323 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
