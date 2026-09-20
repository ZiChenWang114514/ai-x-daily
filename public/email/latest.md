# AIxDaily · 2026-09-21

今日精选：AI × Chem 12 项，AI × Bio 16 项，AI × Math 0 项，AI Voices 5 项，Engineering 4 项。今日五频道以研究预印本、公开观点与工程项目为主。化学聚焦AI辅助材料筛选及虚拟筛选控制；生物呈现空间多组学和疫苗配方优化等预印本。数学频道没有足够高质量更新。AI Voices收录公开帖文中的论文转述、数据集公告和实践看法，需回查原始材料；工程频道则关注GitHub Trending项目，非同行评议研究或正式软件发布。

## 今日重大进展

- [SIFT 研究报告以 LLM 预筛降低自我改进编程智能体的评测成本](https://x.com/dair_ai/status/2101410759511322725) — 一则讨论 MIT 与 Sakana AI 工作的公开帖文称，SIFT 先由 LLM 裁判筛选智能体自我修改候选，再进行完整评测；其在 Polyglot 上以少于 50 CPU 小时达到 35.1%。
- [研究者公布覆盖 61.2 亿次请求的 LLM 推理元数据轨迹](https://x.com/1a1a11a/status/2101469990188732897) — 研究者 Juncheng Yang 在 X 公布覆盖一年的 LLM 推理元数据轨迹，称其包含 61.2 亿次请求，面向真实服务负载建模、系统设计和基础设施优化研究。

## AI × Chem

采集 123，候选 15，精选 12。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable；bioRxiv: RuntimeError: Unable to fetch https://api.biorxiv.org/details/biorxiv/2026-09-17/2026-09-21/0: The read operation timed out

- [Artificial Intelligence-Assisted Dopant Discovery toward Air-Stable Sulfide Solid-State Electrolytes](https://doi.org/10.26434/chemrxiv.15009059/v1) — 工作构建了由检索增强系统、LLM 预筛和组成机器学习模型组成的掺杂剂发现平台，以水解反应的最小 Gibbs 自由能变化量表征硫化物固态电解质 LPSC 的空气稳定性。平台筛出 BiF3、CoF3、InF3 和 SnF4 等候选；其中 LPSC-BiF3 在 10% RH 空气暴露 6 h 后仍保留 91% 的离子电导率，并在 Li-In||NCM811 全电池中显示出良好循环稳定性。
- [Per-Stage Controls and Failure Modes in a Co-Folding Virtual Screening Cascade for the Keap1–Nrf2 Interaction](https://doi.org/10.26434/chemrxiv.15008984/v1) — 工作以 Keap1–Nrf2 蛋白–蛋白相互作用和 130,793 个可按需合成化合物为测试床，逐阶段审计共折叠、学习型亲和力、构象和溶剂化评分组成的虚拟筛选流程。结果显示亲和力模型难以量化效价差、存在分子量耦合且不能区分对映体；构象置信度对几何正确性的信息量有限。作者提出并发布了含匹配诱饵门控等测试的可复用控制套件。
- [Dynamic Parameter Screening for Accelerated Mechanistic Analysis](https://doi.org/10.26434/chemrxiv.15008823/v2) — 作者提出动态参数筛选（DPS）：在单次批式反应连续监测过程中，依次加入试剂和催化剂，同时探测多种物种的动力学影响。以 PdCl2(dppf)·CH2Cl2、PEPPSI-iPr 和 XPhos Pd G2 催化的 Kumada–Tamao–Corriu 偶联为例，DPS 通常与逐一变量法给出一致的定性和定量结论，并据此提出低催化剂负载下的慢加料提速策略。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1141，候选 60，精选 16。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable；bioRxiv: RuntimeError: Unable to fetch https://api.biorxiv.org/details/biorxiv/2026-09-17/2026-09-21/180: The read operation timed out

- [Spatially resolved multimodal hallmarks of response to neoadjuvant immunotherapies in the melanoma ecosystem in 2D and 3D](https://europepmc.org/article/PPR/PPR1322928) — 最大规模的新辅助免疫检查点阻断空间多组学队列，以超过 1.12 亿个单细胞解析黑色素瘤治疗响应相关的三级淋巴结构、免疫—基质生态位及其三维组织。
- [Accelerated discovery of thermostable vaccines using data-efficient AI](https://europepmc.org/article/PPR/PPR1322905) — AGENT 将高通量实验与贝叶斯优化结合，用稀疏配方数据在六轮迭代中发现可在 37 °C 保存超过两个月且保持活性的固态 mRNA-LNP 疫苗配方，并在啮齿动物和非人灵长类中验证。
- [Systematic Engineering of Loss-of-Function Alleles in the Zebrafish Mitochondrial Proteome](https://europepmc.org/article/PPR/PPR1322723) — Z-Terminator 利用线粒体 TALE 碱基编辑器，在斑马鱼中系统构建全部 mtDNA 编码 OXPHOS 亚基的功能缺失等位基因，并解析异质性、组织分布及毛细胞功能表型。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 0，候选 0，精选 0。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 67，候选 60，精选 5。来源状态：各来源已完成

- [@dair_ai：Banger paper from MIT and Sakana AI. They show that self-improving coding agents work. The best part is that their appro](https://x.com/dair_ai/status/2101410759511322725) — DAIR.AI转述MIT与Sakana AI的SIFT研究：帖文称，该方法以LLM裁判预筛候选自我修改，将完整基准评估集中在更有希望的候选上，并报告了相对DGM更低的计算开销和Polyglot结果。
- [@1a1a11a：Announcing one year of LLM inference metadata traces, with 6.12 billion requests. We hope this dataset can support resea](https://x.com/1a1a11a/status/2101469990188732897) — Juncheng Yang宣布发布覆盖一年的LLM推理元数据轨迹，称其包含61.2亿次请求，并希望数据集支持真实服务负载理解、系统设计与基础设施优化研究。
- [@omarsar0：One of the craziest use cases I’ve found for Jev: verifiers. I am so excited about this that I at least wanted to share ](https://x.com/omarsar0/status/2101443311454036477) — Omar Sar0分享其工程经验：他称自己用Jev为智能体框架的/goal功能构建了逐轮完成度验证器，以较低成本更频繁地检查目标是否真正完成。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 80，候选 60，精选 4。来源状态：各来源已完成

- [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) — BuilderIO 的 agent-native 是用于构建智能体应用的框架；当日 GitHub Trending 第 2 名，新增 89 星。
- [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) — paperless-ngx 是面向扫描、索引与归档的社区维护文档管理系统；当日 GitHub Trending 第 6 名，新增 32 星。
- [vercel-labs/json-render](https://github.com/vercel-labs/json-render) — Vercel Labs 的 json-render 是生成式 UI 框架；当日 GitHub Trending 第 12 名，新增 332 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
