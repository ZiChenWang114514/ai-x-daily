# AIxDaily · 2026-08-30

今日精选：AI × Chem 8 项，AI × Bio 14 项，AI × Math 6 项，AI Voices 8 项，Engineering 1 项。今日关注聚焦可验证的科研智能与工具实践：化学和生物频道均以预印本为主，分别讨论合成可及性表示、医学多模态与蛋白质组基础模型；数学频道提出实验保真审计和可验证推理；AI Voices 汇集公开发布与观点，性能主张仍待独立复现；工程频道则记录 Codex 的正式软件发布。

## AI × Chem

采集 918，候选 60，精选 8。来源状态：各来源已完成

- [Can SMILES be fragmented into a concatenable ordered sequence of retrosynthetically interesting string block ?](https://www.biorxiv.org/content/10.64898/2026.08.25.747180) — 该研究通过枚举同一分子的 SMILES 表示，将与自动逆合成分析得到的潜在合成子相对应的字符串片段组织为可拼接、有序的区块，并在 MolGPT 与 Monte Carlo Tree Search（MCTS）生成中测试其作用。
- [Bridging Food Chemistry and Computational Approaches with Agentic AI: Plant Protein Solubility and Bioactive-Enzyme Interactions](https://doi.org/10.26434/chemrxiv.15007938/v1) — 该工作提出可见、逐步的人机协作 Agentic AI 工作流，将食品化学假设转为可规划、实施、测试和复用的计算流程，并以植物蛋白溶解性和膳食多酚—胰脂肪酶相互作用为例验证。
- [Four numbers, one axis: deep learning models reveal what leaf spectrum constrains about Farquhar-von Caemmerer-Berry photosynthesis](https://www.biorxiv.org/content/10.64898/2026.08.27.747677) — 研究以数据集阻断、物种阻断和留一数据集验证重新评估叶片反射光谱预测 FvCB 光合参数的能力，并利用带固定可微 FvCB 解码器的卷积编码器考察参数可辨识性。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 972，候选 60，精选 14。来源状态：各来源已完成

- [From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation](https://arxiv.org/abs/2608.26856v1) — MedREAL 将医学多模态语言模型的诊断推理与像素级分割连接起来，并在四种影像模态的 13,824 个专家验证样本上评估。
- [Trends in Machine Learning and Feature Selection Stability for Human Gut Microbiome (Shotgun Metagenomics) and Metabolomics Matched Datasets](https://www.biorxiv.org/content/10.1101/2025.06.21.660858) — 该研究系统比较人类肠道宏基因组—代谢组匹配数据中的多组学整合策略、机器学习算法及特征选择稳定性。
- [OmicsFM brings proteomics into the foundation model era](https://www.biorxiv.org/content/10.64898/2026.08.25.747021) — OmicsFM 在 1,397 个重处理 PRIDE 项目的 48,837 份蛋白质组学谱上预训练，以测试蛋白质组基础模型的表征能力。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 284，候选 60，精选 6。来源状态：各来源已完成

- [Beyond Execution: Auditing Experimental Fidelity in LLM-Driven Scientific Research](https://arxiv.org/abs/2608.26753v1) — ABE-Ralph 以原始参考方法为依据审计 LLM 驱动的科学实验复现，将主张、方案、必要组件、基线和指标表示为结构化实验约束，并进行定量、定性与代码级核查。
- [GRAIN: Bridging Name and Narrative Shifts in Real-World Graph Reasoning through Invariance-Rewarded Agentic RL](https://arxiv.org/abs/2608.27142v1) — GRAIN 用结构不变性奖励训练单智能体，将文本中的图任务解析为结构并调用工具执行；其 GRIT 基准专门测量节点名称与任务表述变化带来的推理脆弱性。
- [SymbolLKG: Towards Verifiable Logical Reasoning via Logical Knowledge Graph and Symbolic Solvers](https://arxiv.org/abs/2608.26836v1) — SymbolLKG 将 Logical Knowledge Graph、拓扑感知检索和动态符号求解器路由结合，以显式表示逻辑规则与约束，并生成可核查的逻辑推理路径。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 50，候选 43，精选 8。来源状态：各来源已完成

- [@kwindla：Introducing PhoneLLM, an open model for voice agents. GPT 5.6 Terra performance on typical voice agent tasks at 1/3 the ](https://x.com/kwindla/status/2093014818647339026) — Pipecat 团队成员发布 PhoneLLM，帖文称其为面向语音智能体的开放模型，并称其在典型任务上以更低延迟和成本达到 GPT 5.6 Terra 的性能。
- [@random_walker：My best rough estimate of the fraction of the scientific literature that’s wrong — flat-out wrong, you’d-be-nuts-to-rely](https://x.com/random_walker/status/2093359668806512793) — Arvind Narayanan 估计，大量科学文献存在严重错误；他认为科学自我修正依赖后续复现、计算检查和假设挑战，并主张文献智能体应主动检索后续质疑研究。
- [@HuaxiuYaoML：Can frontier AI agents achieve Recursive Self-Improvement by turning a weak method into one that performs better on hidd](https://x.com/HuaxiuYaoML/status/2092779580004474985) — Huaxiu Yao 宣布 RSI-Exam：覆盖 6 个领域、含 88 个可执行研究任务的递归自我改进评测，并开放征集任务贡献；帖文给出 Opus 5 的隐藏集平均分。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 63，候选 48，精选 1。来源状态：各来源已完成

- [0.151.0](https://github.com/openai/codex/releases/tag/rust-v0.151.0) — openai/codex 发布 rust-v0.151.0：新增可选 MCP 服务器工具发现的可配置宽限期、扩展对 MCP 工具结果的检查或替换能力，以及按仓库合并的插件目录配置；同时修复权限配置、模型切换、远程沙箱和 MCP 错误传递等问题。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
