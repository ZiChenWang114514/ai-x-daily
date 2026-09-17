# AIxDaily · 2026-09-18

今日精选：AI × Chem 11 项，AI × Bio 16 项，AI × Math 0 项，AI Voices 10 项，Engineering 10 项。9月18日，化学与生物频道的前列内容均为预印本：前者聚焦反应解析及催化、聚合物建模，后者结合扰动组学与遗传信息研究靶点和疾病机制。AI Voices 收录机构或研究者的公开发布与观点，工程频道呈现 GitHub 当日趋势项目；AI × Math 今日未见足够高质量更新。

## 今日重大进展

- [Stellar Colosseum：多智能体框架报告长证明与竞赛推理新纪录](https://x.com/mirrokni/status/2100660772393320476) — 研究者 Vahab Mirrokni 公布 Stellar Colosseum 技术报告：该多智能体框架将策略探索、证明分解、子问题求解和全局验证分工协作。其帖文称，系统已产出经作者或 Lean 核验的长证明，在 Codeforces 达到 4263 分，并在 TCS-Bench 取得 71.0%。
- [Anthropic 开源生物模型推理优化：覆盖 30 余模型、平均提速 4 倍](https://x.com/AnthropicAI/status/2100701581109072332) — Anthropic 发布称，Claude 为 30 多个开源生物学模型优化了推理，其中包括分子系统结构建模、类药分子设计和突变效应预测所用模型；部分优化通过定制 GPU 软件实现，官方报告平均推理速度提升 4 倍，并承诺开源全部代码。
- [AI 据报数日找到两条迄今最复杂的高秩椭圆曲线](https://x.com/sciam/status/2100178162474742097) — 《科学美国人》报道，AI 在数日内发现两条迄今最复杂的高秩椭圆曲线；此前同类纪录推进曾耗时 18 年。该结果触及有理数域上椭圆曲线秩能否任意增大的长期问题，但并未解决这一开放问题。

## AI × Chem

采集 875，候选 60，精选 11。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable

- [Chemistry-Informed Multimodal Model for Structure Elucidation in Automated Reaction Discovery](https://doi.org/10.26434/chemrxiv.15008991/v1) — DynaMAIK 是用于自动化反应发现的多模态 Transformer：将 GC-MS 电子电离质谱与以 SMILES 编码的反应物、试剂上下文结合，预测产物结构及分子式。在逾300万反应—谱图对训练后，模型在留出的实验测试集上达到87% top-1、94% top-10 结构准确率，并在高通量硫醇化反应中直接完成实验筛选产物指认。
- [Data-Driven Exploration of Literature-Derived Catalyst and Reaction Spaces for the Vapor-Phase Aldol Condensation of Acetate with Formaldehyde](https://doi.org/10.26434/chemrxiv.15008977/v1) — 研究汇编71篇文献中的375条醋酸酯与甲醛气相热催化羟醛缩合数据，并以发表物分组交叉验证、正则化树模型和 SHAP 分析处理稀疏异质数据。结果识别三类催化剂，指出液时空速和反应物摩尔比是丙烯酸酯生产率的主导变量，同时将失活与产率相关联。
- [Polymer Informatics Atlas: Property-Specific Representations, Chemistry-Aware Generalization, and Reliability-Aware Machine Learning Across Five Polymer Properties](https://doi.org/10.26434/chemrxiv.15008969/v1) — 该聚合物信息学研究在 NeurIPS Open Polymer Prediction 2025 的7,973个 RDKit-valid 重复单元上，比较描述符、Morgan 指纹及混合表征对 Tg、FFV、Tc、密度和 Rg 的预测。它进一步以化学分割、掩码多任务学习、集成与 split-conformal 校准检验模型外推性和不确定性。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1672，候选 60，精选 16。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable

- [Genome-scale perturbation signatures from primary human CD4 + T cells improve genetics-based prioritization of immune drug targets](https://europepmc.org/article/PPR/PPR1320752) — IGNITE 将2200万原代人CD4 + T细胞的 genome-scale perturb-seq 与人类遗传学先验整合，用于免疫药物靶点排序，并提供公开分数。
- [Integration of cell-specific gene expression and chromatin accessibility facilitates localization of neurodegenerative risk in microglia](https://www.biorxiv.org/content/10.64898/2026.09.15.751821) — 研究在135个 iPSC 供体来源的神经元和小胶质细胞中整合 scRNA-seq、scATAC-seq、QTL 与 Perturb-seq，定位神经退行性疾病风险相关的细胞类型与调控元件。
- [Genomic foundation model-derived disruption profiling links somatic mutations to cancer biology and clinical outcomes](https://www.medrxiv.org/content/10.64898/2026.09.15.26363174) — 研究以 AlphaGenome 和 AlphaMissense 对 TCGA 8,800名患者、33种癌症的体细胞突变进行序列到功能预测，并构建患者-基因扰动图谱。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 0，候选 0，精选 0。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 63，候选 60，精选 10。来源状态：各来源已完成

- [@IFM_AI：Today’s LLMs still write like typewriters: one token at a time. This sequential process creates a hard inference bottlen](https://x.com/IFM_AI/status/2100618934915592640) — Institute of Foundation Models 介绍 Uno，并称其以扩散式生成实现对自回归语言模型的无损加速；帖文报告 K2-Horizon-7B 在质量和吞吐量上优于既有扩散方法，最高提速2.2倍。
- [@_sophia_tang_：Can we train a one-step discrete generator without a teacher model? Introducing Discrete Beckmann Transport Models 🛸 — a](https://x.com/_sophia_tang_/status/2100205583332688172) — Sophia Tang 发布与 Shiyi Wang 合作的 Discrete Beckmann Transport Models：作者称该离散生成模型可在一步内把潜在空间中的任一点送至单纯形顶点，并报告语言建模和少步推理的结果。
- [@Letian_Wang_6：Earlier, quite a few people who attended CVPR told me they came away pretty disappointed — including some extremely seni](https://x.com/Letian_Wang_6/status/2100230477009318055) — Letian Wang 基于自己在 ECCV 的经历及与会者反馈，描述了传统计算机视觉研究在大模型发展背景下的焦虑，并提出其可能被基础模型吸收的问题。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 81，候选 60，精选 10。来源状态：各来源已完成

- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — addyosmani/agent-skills 为 AI 编程智能体提供可复用的生产级工程技能包；本日 GitHub Trending 第 3 名，新增 680 星。
- [Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill) — Tencent/BrowserSkill 通过 CLI 与浏览器扩展，让可调用 Shell 的 AI 智能体操作用户真实、已登录的浏览器；本日 GitHub Trending 第 4 名，新增 1,350 星。
- [anthropics/claude-code](https://github.com/anthropics/claude-code) — anthropics/claude-code 是终端中的编程智能体，可理解代码库、执行常规任务、解释复杂代码并处理 Git 工作流；本日 GitHub Trending 第 6 名，新增 538 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
