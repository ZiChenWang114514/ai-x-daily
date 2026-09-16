# AIxDaily · 2026-09-17

今日精选以预印本、机构公开帖文和开源软件项目为主，未见以同行评议论文身份入选的条目。化学与生物频道聚焦 AI 驱动的药物设计、扰动组学和临床前后相关证据；AI Voices 提供科学智能体与模型安全的公开观点；工程频道则呈现可审计安全审计、语音与视觉工具的社区热度。AI×Math 今日没有足够高质量更新。

## 今日重大进展

- [Periodic Labs 报告 Neon 将困难 X 射线衍射分析成功率提升约二十倍](https://x.com/LiamFedus/status/2099896059409367356) — Periodic Labs 团队在公开帖文中报告，Neon 经实验室数据、中期训练与强化学习后，在 134 个困难 X 射线衍射样品上的分析成功率由 2.7% 升至 55.3%；结果由与人类专家校准的模型评审。
- [OpenAI 发布模型失配披露框架并公开六份案例报告](https://x.com/OpenAI/status/2100344867507327087) — OpenAI 发布跟踪、调查和公开模型失配实例的框架，规定披露条件与时间线，即使行为尚未完全解释或缓解也可公开；同时发布近六个月训练和评估中观察到的六份失配案例报告。
- [预印本报告 AI 设计的 MsbA 抗生素候选物在小鼠感染模型中降低菌负荷](https://www.biorxiv.org/content/10.64898/2026.09.12.751098) — 一篇 bioRxiv 预印本报告，以 Link-INVENT 和 AutoMolDesigner 设计出靶向 MsbA 的小分子 Y-11；其在耐碳青霉烯鲍曼不动杆菌模型中显示活性，并在小鼠感染实验中降低菌负荷。

## AI × Chem

采集 863，候选 60，精选 16。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable

- [Deep reinforcement learning-driven discovery of a MsbA-targeted small-molecule antibiotic for the treatment of Acinetobacter baumannii infection](https://www.biorxiv.org/content/10.64898/2026.09.12.751098) — 以 cerastecin Cpd 4 为起点，研究结合 Link-INVENT 与 AutoMolDesigner 进行分子设计、化学衍生化和抗菌评估，获得靶向 MsbA 的小分子 Y-11；摘要报告其在耐碳青霉烯鲍曼不动杆菌、细胞毒性/溶血、耐药频率、小鼠感染模型及多种机制实验中的结果。
- [ABCP_finder: A Transformer Embedding-Based Prediction of Anti-Breast Cancer Peptides](https://www.biorxiv.org/content/10.64898/2026.09.06.749767) — ABCP_finder 将 ProtBERT 或 ESM2 的蛋白语言模型嵌入与 MLP 分类器结合，通过 CD-HIT 的同源性识别划分预测抗乳腺癌肽；摘要报告 ProtBERT 模型在不平衡数据上的性能、校准阈值及 xDeep-AcPEP 外部验证。
- [Comprehensive Chemical Space Exploration in De Novo Drug Design: An Algorithmically Constrained, Parallel Dual-Paradigm Framework Validated on BACE1](https://doi.org/10.26434/chemrxiv-2025-bj970/v3) — 研究提出并行的配体基础与结构基础从头设计框架，以 Zoned Applicability Domain 作为实时强化学习奖励梯度、以 SILE 作为代际适应度函数，并在 BACE1 上结合药代过滤、穷尽对接和分子动力学进行评估。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1701，候选 60，精选 15。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable

- [Genome-scale perturbation signatures from primary human CD4+ T cells improve genetics-based prioritization of immune drug targets](https://www.biorxiv.org/content/10.64898/2026.09.12.748195) — IGNITE 整合 2,200 万原代人 CD4+ T 细胞的 Perturb-seq 特征与人类遗传学先验，用于免疫药物靶点排序，并在时间冻结验证中优于仅遗传学模型。
- [Safety, Immunogenicity, Antibody Persistence, and Booster Responses of an Animal-Component-Free Vero Cell Rabies Vaccine: A Randomized, Active-Controlled Phase III Trial.](https://europepmc.org/article/PPR/PPR1319856) — 一项 1,200 人随机、活性对照 Phase III 预印本显示，无动物源成分 Vero Cell 人用狂犬病疫苗的免疫原性不劣于对照，并报告一年抗体持续性和加强免疫反应。
- [Transcriptome-wide mapping reveals a non-canonical RNA-dependent mechanism of platinum cancer drugs](https://www.biorxiv.org/content/10.64898/2025.12.20.694502) — PlatRNA-seq 将顺铂的 RNA 结合定位到转录组范围，结果支持 RNA 结合可能部分介导其细胞毒性，并指向 rG4 与 R-loop 相关机制。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 0，候选 0，精选 0。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 61，候选 58，精选 6。来源状态：各来源已完成

- [@PhAILabs：Today, PhAI Labs launches ScienceBuddy, an interactive research workspace for scientific agents that improve through res](https://x.com/PhAILabs/status/2100260928776515909) — PhAI Labs 宣布推出 ScienceBuddy，并介绍其以运行框架改进和量规引导强化学习构成的双循环机制；发布方报告，在 180 个保留科学问题上，Qwen3.5-4B 的 pass@4 覆盖率由 48.3% 升至 67.8%。编辑认为，该帖同时给出系统设计与固定尝试预算下的量化结果，信息密度较高。
- [@OpenAI：We're sharing our new framework for tracking, investigating, and disclosing instances of model misalignment at OpenAI. T](https://x.com/OpenAI/status/2100344867507327087) — OpenAI 表示已建立模型失配事件的追踪、调查和披露框架，并同步发布过去六个月训练或评估中观察到的六份相关报告。该框架承认部分行为在尚未完全解释或缓解时也可能披露；编辑认为，这为比较机构如何报告安全事件提供了具体材料。
- [@NVIDIAAI：Images rarely show an object’s full 3D geometry. At #ECCV2026, our research team introduced Axolotl3D, a multimodal and ](https://x.com/NVIDIAAI/status/2100282884624097690) — NVIDIA AI 称其在 ECCV 2026 发布了 Axolotl3D：一个具多模态和遮挡感知能力的三维生成模型，可结合图像、相机数据及部分几何信息重建缺失区域。帖文所称单视角和多视角结果为最佳表现，属于发布方主张；编辑认为其问题设定与方法要点明确。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 76，候选 60，精选 5。来源状态：各来源已完成

- [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) — Cloudflare 的 coding-agent skill 将安全审计拆为多个阶段，并输出可独立核验、机器可读的发现；当天 GitHub Trending 第2名，新增1,249星。
- [jamiepine/voicebox](https://github.com/jamiepine/voicebox) — Voicebox 是开源 AI 语音工作室，提供声音克隆、语音听写与生成；当天 GitHub Trending 第5名，新增409星。
- [roboflow/supervision](https://github.com/roboflow/supervision) — Roboflow Supervision 提供可复用的计算机视觉工具，覆盖检测、分割、分类、跟踪和视频处理；当天 GitHub Trending 第12名，新增292星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
