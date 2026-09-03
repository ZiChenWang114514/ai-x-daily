# AIxDaily · 2026-09-04

今日精选：AI × Chem 11 项，AI × Bio 11 项，AI × Math 12 项，AI Voices 9 项，Engineering 4 项。2026年9月4日的五频道内容以预印本、公开帖文和软件动态为主。化学聚焦聚合物生成设计与零样本建模评估，生命科学呈现抗体从头设计和单细胞参考资源；数学频道关注交互式证据核验与模型逻辑评测。AI Voices 汇集发布者和研究者的公开观点，需与技术报告及独立评测结合阅读；工程频道则记录智能体工具的趋势项目和正式软件发布。本批前三项中未见可确认的同行评议论文。

## 今日重大进展

- [OpenAI 发布 GPT-6 Astra，主打可连续执行的计算机操作](https://x.com/markchen90/status/2095597534412673109) — OpenAI 研究负责人 Mark Chen 宣布 GPT-6 Astra，称其可构建和测试软件、跨电脑应用执行任务并辅助开放科学问题探索，同时配备更强的智能体监督与对齐设计。
- [GPT-6 Astra 推进相邻素数最大间隔的经典下界](https://x.com/mehtaab_sawhney/status/2095597484773134805) — OpenAI 研究者 Mehtaab Sawhney 公布，GPT-6 Astra 对相邻素数最大间隔给出约 log log n 因子的改进；帖文称这是自20世纪30年代以来首见的同量级提升。
- [Google 公布成年雄性果蝇完整脑与中枢神经系统图谱](https://x.com/NewsFromGoogle/status/2095553014715093022) — Google 在公开帖文中称，其与 HHMI Janelia 等合作，借助 AI 将数百万张二维图像重建为三维神经结构，绘出逾16.6万个成年雄性果蝇神经元。

## AI × Chem

采集 1527，候选 60，精选 11。来源状态：各来源已完成

- [HiPoly: a hierarchical polymer-native AI framework for property prediction and generative design](https://arxiv.org/abs/2609.02746v1) — HiPoly 提出面向聚合物的三级图模型，以统一表示单体连接、组成和分子量，并将实验配方数据、性质预测、生成设计和分子模拟验证整合为同一工作流。作者在多组分聚合物热物性预测上报告领先精度，并以消融实验检验各设计环节；该方法还筛得并独立验证了具有目标表面能的无 PFAS 候选材料。
- [X-ray crystallographic fragment screening reveals novel and conformationally dynamic ligand-binding sites in Mycobacterium tuberculosis FtsZ](https://www.biorxiv.org/content/10.64898/2026.09.01.748605) — 研究对结核分枝杆菌 FtsZ 开展 X 射线晶体学片段筛选：1,070 个晶体经片段浸泡，714 份数据集进入 PanDDA 分析，149 份显示可支持片段结合建模的事件图密度。作者报告 15 个新结合位点，并观察到 FtsZ 的 ON/OFF 构象及片段对不同链的不对称结合。
- [Systematic evaluation of LLM-based zero-shot model construction in chemistry and materials science: predictive performance and response reliability](https://doi.org/10.26434/chemrxiv.15008241/v1) — 该研究将 LLM 给出的两两比较与偏好学习结合，在不使用目标体系实测目标性质的情况下构建实验条件排序模型。作者在 9 个化学与材料数据集、两家提供商的 6 个 LLM 上评估预测表现、位置偏差、一致性和弃答行为，发现数据集本身比模型选择更影响结果，偏好学习通常优于 LLM 直接预测性质。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2354，候选 60，精选 11。来源状态：各来源已完成

- [De novo designed single-domain antibodies protect against lethal cobra venom neurotoxicity in vivo](https://www.biorxiv.org/content/10.64898/2026.09.01.748349) — 比较 Germinal、RFantibody 与 BoltzGen 的 VHH 从头设计能力，并在小鼠中验证针对眼镜蛇 α-cobratoxin 的保护作用。
- [scMaize: A Single-Cell Foundation Model and Integrated Atlas for Maize](https://www.biorxiv.org/content/10.64898/2026.08.01.742180) — scMaize 整合 385,675 个玉米单细胞并训练带 GO 功能先验的 Transformer 基础模型。
- [immgenT: A Comprehensive Reference of Convergent T-cell States in the Mouse](https://www.biorxiv.org/content/10.64898/2026.01.30.702892) — immgenT 构建覆盖近乎全部小鼠器官和疾病状态的 T 细胞参考图谱，并以深度生成模型定义 8 个谱系和 107 个稳健簇。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 714，候选 60，精选 12。来源状态：各来源已完成

- [InSight: A Benchmark for Agentic Claim Verification in Interactive Visualizations](https://arxiv.org/abs/2609.01383v1) — InSight 构建了交互式可视化中的智能体主张核验基准，要求模型通过操作网页环境判断主张是否得到证据支持、被证据反驳或无法核验。
- [When Decodability Is Not Enough: Logical Validity Representations, Behavioral Dissociation, and Causal Tests in Language Models](https://arxiv.org/abs/2609.02438v1) — 该研究以五个开放权重 Transformer 为对象，区分逻辑有效性信息在隐藏状态中可被解码、能在行为上表达以及能产生因果作用这三件不同的事。
- [Benchmarking Language Models for Statistical Problem Formulation](https://arxiv.org/abs/2609.01982v1) — StatFormBench 将统计问题表述形式化为统计问题分类、变量识别与角色分配两个子任务，并在 1,013 个样本上评测 14 个开放和闭源 LLM。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 109，候选 60，精选 9。来源状态：各来源已完成

- [@markchen90：GPT-6 Astra is here! This is a big moment for our research team - years of work on pretraining, reinforcement learning, ](https://x.com/markchen90/status/2095597534412673109) — Mark Chen 在发布帖文中宣布 GPT-6 Astra，并称该模型可构建和测试软件、跨计算机应用工作及协助探索开放科学问题；他将其可用性与更强的智能体监督和对齐工作联系起来。
- [@fchollet：Many of you will ask, "if it saturates ARC 3, is it AGI?" We're not making this claim. All we know about the system so f](https://x.com/fchollet/status/2095599835932135919) — François Chollet 表示，ARC-AGI-3 的饱和分数不构成 AGI 证明；他认为该基准考察探索、不确定性下适应和有限数据中的因果世界建模，但任务规模远小于现实世界任务。
- [@kenbwork：We introduce an Antibody Discovery Benchmark, a benchmark for testing whether AI agents can make scientific decisions ac](https://x.com/kenbwork/status/2095236267873284278) — Kenny Workman 介绍 Antibody Discovery Benchmark：100 项评测覆盖治疗性抗体发现的十个环节；在 20 种模型—运行框架组合中，最强系统也仅通过约半数尝试，帖文称 Opus 5 配合 Claude Code 以 53% 领先。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 72，候选 60，精选 4。来源状态：各来源已完成

- [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) — NousResearch/hermes-agent 是可随用户工作方式持续扩展的 AI 智能体项目；当天位列 GitHub Trending 第 3 名，新增 778 星标。
- [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) — magnitudedev/magnitude 是面向本地模型的开源推理服务器，可接入既有智能体工具；当天位列 GitHub Trending 第 14 名，新增 130 星标。
- [0.153.0](https://github.com/openai/codex/releases/tag/rust-v0.153.0) — openai/codex 发布 rust-v0.153.0：加入远程插件市场管理、Vim 撤销与重做、完整终端历史显示和实验性上下文管理；同时改善应用服务器重连、MCP 审批隔离及会话压缩后的恢复体验。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
