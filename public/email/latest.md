# AIxDaily · 2026-08-25

今日精选：AI × Chem 9 项，AI × Bio 14 项，AI × Math 8 项，AI Voices 3 项，Engineering 0 项。今日研究线索以预印本为主：化学聚焦药物模型验证、聚合模拟与 RNA 基础模型；生物涉及乳腺癌转录组、单细胞药物扰动和阿尔茨海默病图谱；数学关注本地模型评测与长程推理。AI Voices 收录公开研究发布和个人观点，其中性能说法仍待论文或技术材料核验；工程频道未形成软件发布精选。

## AI × Chem

采集 1068，候选 60，精选 9。来源状态：各来源已完成

- [Model Validation Protocols for Machine Learning in Small Molecule Drug Discovery](https://www.biorxiv.org/content/10.64898/2026.08.19.745868) — 提出小分子药物发现中机器学习模型的五项验证建议，并在 ADME 数据集与两类模型上展示现行评估方案可能高估性能、遗漏关键失效模式。
- [First-Principles Atomistic Structure and Dynamics of Polyethylene During High-Pressure Radical Polymerization via Machine Learning Force Fields](https://arxiv.org/abs/2608.21741v1) — 将深度势机器学习力场与含 vdW 校正的杂化 DFT 结合，模拟高压自由基聚合条件下聚乙烯低聚物和长链的原子级结构与动力学。
- [RIBOSPAN: A Long-Context RNA Foundation Model for Versatile RNA Modeling](https://arxiv.org/abs/2608.22849v1) — 发布 16.1 亿参数、原生支持 10,240 nt 上下文的双向 RNA 基础模型 RIBOSPAN，并以其骨干开展全长 mRNA 生成、重设计和保留蛋白质的 CDS 优化。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1740，候选 60，精选 14。来源状态：各来源已完成

- [Population-scale integration of tumor transcriptomics into breast cancer care: a decade of the SCAN-B initiative](https://www.medrxiv.org/content/10.64898/2026.08.20.26360879) — SCAN-B 十年期前瞻性项目将人群尺度乳腺癌 RNA 测序、长期临床资料与常规分子诊断相结合。
- [A mechanism-annotated benchmark reveals limited fidelity to drug-response signatures in single-cell perturbation models](https://www.biorxiv.org/content/10.64898/2026.08.19.745729) — scDrugPerturb-Bench 以机制注释的单细胞扰动数据评估药物反应预测模型，并发现表达重建指标与机制保真度并不稳定一致。
- [Mapping Alzheimer's neuropathology signatures to the whole brain transcriptome using machine learning data fusion](https://www.biorxiv.org/content/10.64898/2026.08.19.745861) — 研究用机器学习融合逾 200 万个皮层细胞与全脑图谱，构建阿尔茨海默病相关转录组信号的全脑预测图。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 596，候选 60，精选 8。来源状态：各来源已完成

- [More Accurate or More Efficient? Evaluating Locally Deployed Compact Open-Weight Language Models for Mathematical Reasoning](https://arxiv.org/abs/2608.22048v1) — 对三款 50 亿参数以下本地开源权重模型进行数学推理的受控评测，同时比较正确率、能耗、运行时间与错误类型。
- [Lexical Perturbations Disrupt LLM Reasoning: An Empirical Study of Attention Diversion](https://arxiv.org/abs/2608.22140v1) — 研究在四个推理基准上测试词汇扰动，发现字符级噪声会显著削弱多步推理，并用注意力干预分析其机制。
- [SRPO: Self-Reflective Policy Optimization for Long-Horizon Reasoning](https://arxiv.org/abs/2608.23493v1) — SRPO 通过反思已完成轨迹生成修补信息，并把稀疏终局监督转为 token 级训练信号；摘要报告其在 AIME'24 和多项长程任务上的结果。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 51，候选 51，精选 3。来源状态：各来源已完成

- [@AnimaAnandkumar：Tackling a 60-year-old challenge in quantum chemistry: making density functional theory scale nearly linearly with syste](https://x.com/AnimaAnandkumar/status/2092031815448248594) — Anima Anandkumar 在帖文中介绍其团队的统一 AI 模型，并称该模型可在准线性时间内进行分子与材料的量子力学模拟；帖文还称，约 8 万电子的镁位错自洽计算可在单张 GPU 上完成。编辑判断：若论文中的方法、验证范围与算力比较得到充分核验，这会是 AI 加速第一性原理计算的重要进展。
- [@MSFTResearch：Skala 1.1, the updated deep-learning exchange-correlation functional from Microsoft Research, provides greater accuracy,](https://x.com/MSFTResearch/status/2091918455301628355) — Microsoft Research 发布 Skala 1.1，并称这一深度学习交换-相关泛函提高了准确性、扩大了在计算化学工具生态中的可用性，同时提供持续更新的计算性能基准。编辑判断：这类面向软件生态与基准维护的研究更新，比单一模型宣传更便于专业读者追踪实际可用性。
- [@AndrewYNg：In the fight to defend openness in AI, the Marin project is a precious demonstration of openness in model training, with](https://x.com/AndrewYNg/status/2091688153048645650) — Andrew Ng 将 Marin 项目称为模型训练开放性的示范，并提到其公开了代码、数据、训练配方和实验结果；这也是他对开放研究实践的明确肯定。编辑判断：该观点把讨论从开放权重延伸到训练过程与实验记录的可检验性，具有专业讨论价值。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 0，候选 0，精选 0。来源状态：GitHub Releases: URLError: 

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
