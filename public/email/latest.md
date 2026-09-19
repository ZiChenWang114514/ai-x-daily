# AIxDaily · 2026-09-20

今日精选：AI × Chem 6 项，AI × Bio 13 项，AI × Math 0 项，AI Voices 7 项，Engineering 2 项。9月20日的精选以预印本与工程动态为主：AI×Chem 聚焦用于 cryo-EM 建模和 ncRNA 生成的两篇预印本；AI×Bio 收录 RNA 设计、空间转录组和癌症风险分层等预印本，临床转化仍待进一步验证。AI×Math 暂无入选。AI Voices 同时呈现未经一手材料核实的公开观点与 NVIDIA 技术博客的测评实践；Engineering 为 GitHub Trending 项目快照，并非软件正式发布。

## 今日重大进展

- [GPT-6 Astra 据称协助解出 2017 年以来的投票理论开放问题](https://x.com/EpochAIResearch/status/2100986494873989227) — Epoch AI 公布，研究者在与 GPT-6 Astra 的交互中获得关键思路和证明，解出了 FrontierMath 收录的一道“重大进展”级题目；该题触及一个自 2017 年悬而未决的投票理论问题。
- [《Science》刊出 Virtual Biotech 多智能体药物研发组织框架](https://x.com/james_y_zou/status/2100648966866231592) — 研究者公布，其“Virtual Biotech”以虚拟首席科学家协调大量 AI 科研智能体，并由科学审稿角色质疑结论、识别缺失证据，覆盖从靶点发现到临床试验设计的药物研发流程。

## AI × Chem

采集 809，候选 60，精选 6。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable

- [EM3DFold: accurate de novo protein and nucleic acid model building for cryo-EM maps using language model-powered deep learning](https://www.biorxiv.org/content/10.64898/2026.09.16.752067) — EM3DFold以密度感知的大语言模型三轨注意力网络，联合序列、cryo-EM密度图和结构信息，实现蛋白质、核酸及其复合物的从头全原子建模；在298张独立实验cryo-EM图谱上的评测显示其优于多种现有自动建模工具。
- [Conditional Generation And Inpainting Of Non-coding RNA Sequences With Masked Discrete Diffusion](https://www.biorxiv.org/content/10.64898/2026.09.17.752279) — RNA-MDLM将Masked Discrete Language Models扩展至ncRNA的条件生成和序列补全，以预训练RNA语言模型的RNA类型表征及改进的classifier-free guidance控制生成；作者还提出REPAINT GAMES基准，并在460万条ncRNA序列上进行训练与消融评估。
- [Pep-PU-GAN: Positive-Unlabeled Adversarial Learning for Peptide Function Prediction](https://www.biorxiv.org/content/10.64898/2026.09.13.751209) — Pep-PU-GAN结合正例-未标注学习、GAN和GNN，将肽表示为残基图，并通过合成嵌入和双功能判别器处理稀缺负例问题。在4,049条正例神经肽与8,558条未标注肽的任务中，模型在独立留出基准上报告F1为0.93、AUROC为0.98。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1428，候选 60，精选 13。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable

- [Unlocking Programmable and Creative RNA Sequence Design with RDiffusion](https://europepmc.org/article/PPR/PPR1322331) — RDiffusion 以离散扩散生成 Transformer 按功能、家族、结构或结合蛋白条件设计 RNA，并在骨关节炎临床样本中报告了 miRNA 候选物的验证结果。
- [spaGFM is a scalable graph foundation model for spatial transcriptomics analyses](https://europepmc.org/article/PPR/PPR1322216) — spaGFM 用随机游走序列化细胞邻域，在 132 个空间转录组数据集的 4,390 万细胞上预训练图基础模型。
- [Identifying cohorts at elevated risk of cancers using generative modeling of patient health states](https://www.medrxiv.org/content/10.64898/2026.09.09.26362676) — GenEHR 在数百万患者的 EHR 上训练自回归生成模型，并在五个大型 EHR 队列中以监督适配改善五年内首次癌症诊断风险分层。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 0，候选 0，精选 0。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 72，候选 60，精选 7。来源状态：各来源已完成

- [@thesupermannx：LLMs can now talk to each other without words. Chinese researchers open-sourced a new paradigm that lets LLMs communicat](https://x.com/thesupermannx/status/2100636553576124595) — 一则公开帖文介绍了 Cache-to-Cache（C2C）多智能体通信方案：将源模型的 KV cache 经神经网络投射并融合到目标模型，而非先生成自然语言文本。帖文声称该方法配有逐层门控，并在其引用的基准中带来准确率和速度提升。
- [@omarsar0：Banger paper from NVIDIA on shared memory for research agents. Agora records every result, hypothesis and verification a](https://x.com/omarsar0/status/2100624082752667809) — 一则公开帖文介绍 NVIDIA 的 Agora 研究：系统把结果、假设和验证记录为不可变 Git 提交，并据称让 13 个 LLM 工作者在无预分配任务、无中心规划器的条件下运行近 12 天。帖文还给出了压缩指标和独立复现实验次数。
- [Benchmarking LLM Inference at Scale with AIPerf](https://developer.nvidia.com/blog/benchmarking-llm-inference-at-scale-with-aiperf/) — NVIDIA 技术博客发布 AIPerf 的推理压测说明，聚焦在可重复、接近真实流量模式下测量首 token 时间（TTFT）、token 间延迟（ITL）、端到端延迟与吞吐量。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 78，候选 60，精选 2。来源状态：各来源已完成

- [higgsfield-ai/higgsfield](https://github.com/higgsfield-ai/higgsfield) — Higgsfield 提供面向超大规模模型训练的容错 GPU 编排与机器学习框架；今日 GitHub Trending 第 7 名，新增 314 星。
- [yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X) — Codex-X 是用于管理 OpenAI Codex 桌面端与 CLI 的跨平台可视化工具，覆盖 Provider/API 切换、会话同步、提示词注入、Skills/MCP 管理和 TOML 配置；今日 GitHub Trending 第 15 名，新增 59 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
