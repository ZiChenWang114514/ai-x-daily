# AIxDaily · 2026-09-19

今日精选：AI × Chem 16 项，AI × Bio 12 项，AI × Math 0 项，AI Voices 8 项，Engineering 7 项。9月19日的精选聚焦科研智能体、临床文本评估与模型部署。化学和生物频道以预印本为主：前者梳理生成式小分子设计并展示计算工作流，后者报道虚拟细胞建模和症状抽取评估；这些结果尚待同行评议或进一步验证。AI Voices 收录模型发布和研究者公开观点，不能等同于独立实证。工程频道则反映规格驱动开发、插件与本地记忆基础设施的开源动向。

## 今日重大进展

- [Qwen 发布首个面向智能体的原生全模态模型 Qwen3.8-Omni-Flash](https://x.com/Alibaba_Qwen/status/2100785962414702599) — Qwen 在官方帖文发布 Qwen3.8-Omni-Flash，称其将原生音视频理解、推理和工具使用整合为一体，支持百万 token 长上下文；发布方报告其在两项多模态智能体基准平均提升 19.5 分。
- [PrismML 发布 5.9 GB 的三值量化 Bonsai 2 27B](https://x.com/PrismML/status/2100692248480596348) — PrismML 在官方帖文发布基于 Qwen3.8 27B 的 Ternary Bonsai 2 27B，以 Apache 2.0 开源。团队称其为 5.9 GB、约全精度版本九分之一，保留 98.2% 综合基准性能。
- [百万级筛选推动从头设计游离碳水化合物结合蛋白](https://www.biorxiv.org/content/10.64898/2026.09.12.751118) — 研究者在预印本中提出潜在生成搜索，以推理时奖励引导的序列—结构协同生成设计结合蛋白；逾百万个设计经噬菌体展示筛选，并报告首次获得可结合游离碳水化合物、可区分血型抗原的从头设计蛋白。

## AI × Chem

采集 978，候选 60，精选 16。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable

- [From Computational Chemistry to Generative Models: A Survey of AI-Driven Small-Molecule Drug Discovery](https://doi.org/10.26434/chemrxiv.15008163/v3) — 综述2017—2025年、更新至2026年1月31日的AI小分子药物发现工作，比较自回归、VAE、GAN、流模型、扩散模型及强化学习，并讨论分子表示、数据集、基准和图神经网络。
- [LLMsFold: Integrating Large Language Models and Biophysical Simulations for De Novo Drug Design](https://www.biorxiv.org/content/10.64898/2026.03.02.709055) — LLMsFold以70 billion参数的LlaMA家族模型生成受类药性约束的SMILES，再以Boltz-2评估蛋白-配体共折叠结构和结合亲和力，并通过强化学习优化ACVR1与CD19候选分子。
- [TRACEDD: A Tool-grounded Reasoning and Agentic Coordination for Explainable Drug Design](https://www.biorxiv.org/content/10.64898/2026.09.12.751167) — TRACEDD提出以工具优先的多智能体药物设计架构，将靶点验证、可成药性、分子生成、ADMET和逆合成等模块置于Reason-Act-Observe流程中，并以JAK2案例演示。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1694，候选 60，精选 12。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable

- [AI Scientists for Building Virtual-Cell Models](https://europepmc.org/article/PPR/PPR1321498) — CellForge 以多智能体协作完成单细胞扰动模型的假设、训练与验证流程。
- [Extracting Symptoms of Psychotic Disorders from Clinical Notes using Natural Language Processing.](https://www.medrxiv.org/content/10.64898/2026.09.16.26363090) — 在 N = 704 的重性精神疾病队列中，14 个通用 LLM 对精神分裂症症状抽取的表现为较差至中等。
- [3D Spatial Interactomics Maps the Dynamics of NF-κB Multiprotein Signalosomes in Single Cells](https://www.biorxiv.org/content/10.64898/2026.09.14.751198) — 3D iseqPLA 在单细胞中追踪 NF{kappa}B 多蛋白信号复合体的空间与时间动态。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 0，候选 0，精选 0。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 81，候选 60，精选 8。来源状态：各来源已完成

- [@PrismML：Today, we’re announcing Ternary Bonsai 2 27B. Based on Qwen3.8 27B, Bonsai 2 27B is 9x smaller than its full-precision c](https://x.com/PrismML/status/2100692248480596348) — PrismML 在官方帖文中发布 Ternary Bonsai 2 27B，并称其基于 Qwen3.8 27B、体积约为全精度版本的九分之一。发布方声称该模型保留 98.2% 的综合基准性能。编辑判断：这是有明确版本、许可证与可量化主张的模型发布，但性能仍应以独立复现为准。
- [@Alibaba_Qwen：🚀 Meet Qwen3.8-Omni-Flash, Qwen's first omni-modal model built around agentic capabilities! Native audio-video understan](https://x.com/Alibaba_Qwen/status/2100785962414702599) — Qwen 官方帖文发布 Qwen3.8-Omni-Flash，称其将原生音视频理解、推理和工具使用整合于同一模型。发布方报告其在两个智能体基准上的平均分提高 19.5 点，并称长视频场景比静态理解少用 51.8% token。编辑判断：该帖文给出了任务与指标名称，但比较结论仍是发布方报告。
- [@polynoamial：A few thoughts on this: 1) If you’ve only seen clips of this interview, I’d encourage you to watch the full podcast. I p](https://x.com/polynoamial/status/2100998240586137701) — Noam Brown 澄清访谈片段中的隔离案例旨在说明绝对隔离保证的困难，而非讨论通过温度传感器窃取模型权重。他认为智能体即使完全隔离也可用极少信息协调，并主张安全设计应高估风险、采用多层防护和空气隔离。编辑判断：这是研究者对具体安全设计取舍的公开解释，不是新的实验结果。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 84，候选 60，精选 7。来源状态：各来源已完成

- [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) — Fission-AI/OpenSpec 为 AI 编程助手提供规格驱动开发工作流；今日 GitHub Trending 第 8 名，新增 298 星。
- [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) — anthropics/knowledge-work-plugins 是面向 Claude Cowork 知识工作场景的开源插件库；今日 GitHub Trending 第 10 名，新增 300 星。
- [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) — supermemoryai/supermemory 提供可完全本地运行的智能体记忆与上下文引擎及应用；今日 GitHub Trending 第 11 名，新增 140 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
