# AIxDaily · 2026-09-08

今日精选呈现从可执行科研到智能体工程的连续链条：化学频道以两篇预印本关注合成感知分子设计和虚拟筛选接入自动化实验；生物频道的预印本将单细胞基因组毒性刻画与植物长序列模型并置。AI Voices 主要为机构或研究者公开观点，所述性能尚待独立核验；工程频道则反映视频渲染、文档规范化与技能封装工具的社区热度。AI×Math 今日没有足够高质量更新。

## 今日重大进展

- [研究者报告锌首次实现可逆氧化还原催化并用于芳基氟化物硼化](https://doi.org/10.26434/chemrxiv.15002479/v3) — 研究者在 ChemRxiv 预印本中报告首个清晰的 Zn(I)/Zn(II) 可逆氧化还原催化实例：在光照和二硼烷条件下实现芳基氟化物 C(sp2)–F 键硼化，并以实验和 DFT 支持催化循环。
- [OpenBMB 发布 MiniCPM5-2B，并开放数据、训练配方与 RL 栈](https://x.com/OpenBMB/status/2096970974247956501) — OpenBMB 发布并开源 20 亿参数的 MiniCPM5-2B，称其在 34 项基准平均得分 53.9、在两项小模型指数居前；同时开放模型、数据、训练配方与 RL 栈。
- [MetaGNN 作者撤回肿瘤代谢 GNN 的性能增益，公开基准失效审计](https://www.biorxiv.org/content/10.64898/2026.09.02.748315) — 作者在 bioRxiv 预印本中报告，原基准同时存在由输入阈值直接生成的标签泄漏、伪随机标签记忆和零特征输入；重建特征后模型低于原始表达基线，并撤回此前的 AUROC 增益。

## AI × Chem

采集 371，候选 50，精选 12。来源状态：各来源已完成

- [OmniSyn unifies target-aware molecular generation and optimization within a synthesis-native LLM framework across the human proteome](https://www.biorxiv.org/content/10.64898/2026.09.02.748775) — OmniSyn 将蛋白序列条件分子生成、合成轨迹生成、可合成性投影与 hit-to-lead 优化整合到 MoE 语言模型中，并在 MolGenBench 未见靶点和全人类蛋白组尺度进行评估。
- [A retrieval-augmented agent bridges virtual screening and automated synthesis](https://doi.org/10.26434/chemrxiv.15008409/v1) — Syn-RRAG 是检索增强的 LLM 合成智能体：以初始逆合成、反应先例检索和分层细化生成包含完整实验参数的方案，并在自动化平台合成验证了 3 个虚拟筛选候选物。
- [Machine Learning for High-Throughput Reaction Yield Prediction in DNA-Encoded Library Synthesis](https://doi.org/10.26434/chemrxiv.15008275/v2) — 该研究为 DNA-encoded library (DEL) 单循环反应收率预测提出以暴露官能团、局部环境、building block (BB) 和反应类型为输入的局部表征；GAT 在真实高通量数据上优于指纹基线。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 437，候选 60，精选 14。来源状态：各来源已完成

- [Chromosomal mutational signatures of DNA damaging agents at single cell resolution](https://www.biorxiv.org/content/10.64898/2026.08.30.748106) — 该研究以单细胞全基因组测序、系统发育重建和突变特征分解，解析DNA损伤药物诱导的染色体拷贝数改变；在遗传背景、剂量、停药时间及患者来源异种移植模型间检验了特征。
- [BOTANIC-1: a series of long-context plant genomic foundation models in the agentic era](https://www.biorxiv.org/content/10.64898/2026.09.04.749355) — BOTANIC-1发布面向植物研究的长上下文基因组语言模型系列，可处理数百bp至128 kbp序列，并报告在大规模植物基因组学任务上优于通用及植物专用基线。
- [A dual proteomics analysis of paired cerebrospinal fluid and plasma from patients with neurodegenerative diseases](https://www.medrxiv.org/content/10.64898/2026.09.02.26361977) — 该配对脑脊液—血浆蛋白质组研究在67名个体中比较SomaScan 11K与NULISAseq CNS，并报告NEFL、NPTX2、TREM2和CHIT1的跨平台一致性及与疾病严重度的区室特异关联。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 0，候选 0，精选 0。来源状态：各来源已完成

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 45，候选 42，精选 8。来源状态：各来源已完成

- [@OpenBMB：🚀 Meet MiniCPM5-2B, a 2B-parameter language model bringing high intelligence density to the edge, now open source! It ra](https://x.com/OpenBMB/status/2096970974247956501) — OpenBMB 宣布开源 MiniCPM5-2B，并称同时开放训练数据、训练配方与 RL 栈；帖文还报告其在34项基准上的平均分及两个指数成绩，均属发布方自述。
- [@polynoamial：One of the most interesting blog posts we've released: details on internal research acceleration at @OpenAI. I expect th](https://x.com/polynoamial/status/2096638670703055312) — Noam Brown 转介 OpenAI 关于内部研究加速的博客，并称文中说明了为优先保障监测、对齐和安全而如何安排模型开发节奏。
- [@ycombinator：Harnesses often get dismissed as just scaffolding, just prompt engineering, and not real research. But that couldn't be ](https://x.com/ycombinator/status/2096970626036855197) — Y Combinator 主张不应把 harness 视为仅是提示工程或外围脚手架，并以“相同权重在更好 harness 下 ARC-AGI 从30%到95%”说明其重要性；该具体数字为帖文陈述。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 46，候选 44，精选 4。来源状态：各来源已完成

- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) — 面向智能体的 HTML 到视频渲染框架，可将可编排网页内容产出为视频；当日 GitHub Trending 第 1 名，新增 734 星。
- [microsoft/markitdown](https://github.com/microsoft/markitdown) — 将文件和 Office 文档转换为 Markdown 的 Python 工具，服务于下游文本处理；当日 GitHub Trending 第 2 名，新增 771 星。
- [openai/skills](https://github.com/openai/skills) — Codex 的技能目录，为可复用的编码智能体能力提供组织入口；当日 GitHub Trending 第 11 名，新增 372 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
