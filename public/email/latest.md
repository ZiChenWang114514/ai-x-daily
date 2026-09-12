# AIxDaily · 2026-09-13

今日精选：AI × Chem 5 项，AI × Bio 13 项，AI × Math 0 项，AI Voices 6 项，Engineering 4 项。今日五频道共同日期为 2026-09-13。化学与生物焦点均来自尚未经同行评议的预印本，分别涵盖肽设计表征、肿瘤免疫与神经母细胞瘤等；AI Voices 收录公开帖文，其中基准定位和性能数字仅代表发布方表述。工程侧入选 GitHub Trending 开源项目快照，并非软件正式发布；AI×Math 因候选不足暂不推荐。

## 今日重大进展

- [帖文转述 DeepMind 与 Janelia 开源可在物理引擎运行的数字果蝇](https://x.com/Zyvex_0x/status/2098350851764945230) — 一则高互动 X 帖文称，Google DeepMind 与 HHMI Janelia 将由显微数据逐关节重建的 flybody 以 Apache 2.0 开源；该数字果蝇可在本地物理引擎中行走、抓握、飞行和着陆。
- [帖文报告生成式 AI 发现药物 rentosertib 进入 III 期临床](https://x.com/sciqst/status/2098271475006329240) — X 帖文报告，rentosertib 已进入 III 期临床，并称其为首个进入该阶段的生成式 AI 发现药物；原帖同时列出其 IIa 期高剂量组与安慰剂组的肺功能变化数据。
- [研究者公布对 Erdős 第364题相关猜想的部分推进，并以 Lean 形式化检验](https://x.com/LovedayChey/status/2097969310484304125) — 数学研究者 Chey Loveday 公布一篇预印本，称其处理了 Erdős 第364题中“平方中项”扇区，触及 Erdős–Mollin–Walsh 关于不存在三个连续强数的猜想；完整问题仍未解决。

## AI × Chem

采集 712，候选 60，精选 5。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 429: Unknown Error

- [Chemical Descriptors and Deep Learning Embeddings for Scoring de novo Peptide Designs](https://www.biorxiv.org/content/10.64898/2026.09.10.750670) — 该研究在9个公开数据集上比较序列化学描述符与蛋白语言/折叠模型深度表示，用于预测从头设计肽的5类可开发性性状和4类结合亲和力终点。结果表明，简单可解释的化学描述符模型常可达到或接近复杂深度模型的表现；Boltz-2 pair 表示的信息量最高，但其亲和力预测受肽分子量显著混杂。
- [The small molecule inhibitor SU056-mediated targeting of YB1 inhibits the Rb pathway in triple-negative breast cancer tumors](https://www.biorxiv.org/content/10.64898/2026.09.05.749600) — 研究报道小分子 SU056 通过促使 YB1 降解，抑制三阴性乳腺癌（TNBC）的增殖、克隆形成、肿瘤球形成、干性和迁移；其与 CDK4/6 抑制剂 Palbociclib 联用在细胞及异种移植和患者来源异种移植（PDX）模型中增强抑瘤效果。机制上，遗传和药理学靶向 YB1 均调节 Cyclin D/CDK4/6/Rb 轴并诱导 G1 阻滞。
- [Predicting Capsid Protein Binding Sites in Single-Stranded RNA Viruses Using Machine Learning from Local Geometric Features](https://www.biorxiv.org/content/10.64898/2026.09.10.750674) — 该工作将 RNA 三级结构建模、局部几何特征和神经网络结合，用于预测单链 RNA 病毒衣壳蛋白结合位点。在 Qbeta; 噬菌体的实验注释 RNA 片段基准上，5折交叉验证 AUC 为0.88；使用 AlphaFold 预测 RNA 结构时仍获 AUC = 0.75。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1601，候选 60，精选 13。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 429: Unknown Error

- [Pan-cancer prediction of tumor immune activation and response to immune checkpoint blockade from tumor transcriptomics and histopathology](https://www.biorxiv.org/content/10.1101/2025.06.27.661875) — TIME_ACT 以泛癌转录组和病理切片预测肿瘤免疫活化及免疫检查点阻断应答。
- [Preclinical trial supports dual inhibition of BCL2 and Aurora kinase A for MYCN -amplified high-risk neuroblastoma](https://europepmc.org/article/PPR/PPR1317864) — 在 MYCN 扩增高危神经母细胞瘤 PDX 中，venetoclax-alisertib 联合抑制显示出强于对照联合化疗的前临床活性。
- [The Parkinson 's Disease Associated BAP1/ASXL3 Complex Regulates the Internalization of α-Synuclein Fibrils by Reprogramming the Cell Surface Glycoproteome](https://www.medrxiv.org/content/10.64898/2026.09.09.26362627) — 全基因组 CRISPRa 筛选和人中脑类器官研究将 BAP1/ASXL3 与 -Syn 纤维内吞调控联系起来。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 0，候选 0，精选 0。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 429: Unknown Error

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 66，候选 60，精选 6。来源状态：各来源已完成

- [@arcprize：ARC-AGI-4 will be a benchmark for autonomous open-ended innovation. It will continue our commitment to open-source, givi](https://x.com/arcprize/status/2098849962754978152) — ARC Prize 官方账号宣布，ARC-AGI-4 将定位为“自主开放式创新”的基准，并强调开源与共享评测目标。人类仍明显强于 AI 的表述是该机构在帖文中的判断。
- [@Zyvex_0x：Someone open sourced an entire animal. Not a model of an animal. The animal. A fruit fly, rebuilt joint by joint from mi](https://x.com/Zyvex_0x/status/2098350851764945230) — 帖文称 Google DeepMind 与 HHMI Janelia 制作了名为 flybody 的数字果蝇：它由显微数据逐关节重建，可在本地物理引擎中完成多种动作，并已发表于 Nature、以 Apache 2.0 许可证置于 GitHub。候选文本未附论文或代码链接。
- [@cohere：On the WMT benchmark (averaged across all languages), North Small Translate achieves an 83.6 score, outperforming models](https://x.com/cohere/status/2098081717529551246) — Cohere 官方账号称，其 North Small Translate 在跨语言平均的 WMT 基准上得分 83.6，高于 DeepL、Google Translate、GLM 5.2 和 Mistral Large 3 等模型。该比较是发布方在未于候选文本说明的评测设置下作出的陈述。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 65，候选 60，精选 4。来源状态：各来源已完成

- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) — Shubhamsaboo/awesome-llm-apps 汇集 100 余个开源 AI 智能体、Agent Skills 与 RAG 应用示例；今日 GitHub Trending 第 10 名，新增 237 星。
- [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE) — multimodal-art-projection/YuE 提供 YuE2 音乐生成模型，覆盖符号规划、零样本翻唱与智能体式音乐编辑；今日 GitHub Trending 第 14 名，新增 193 星。
- [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) — max-sixty/worktrunk 是面向并行 AI 智能体工作流的 Git worktree 管理 CLI；今日 GitHub Trending 第 15 名，新增 137 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
