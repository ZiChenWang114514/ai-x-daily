# AIxDaily · 2026-11-02

今日精选：AI × Chem 3 项，AI × Bio 10 项，AI × Math 2 项，AI Voices 3 项，Engineering 7 项。11月2日，五个频道的精选以公开预印本和工程项目为主，暂无明确的同行评议论文入选。AI×Chem聚焦多智能体harness、声学agent与物理信息机器学习；AI×Bio覆盖环境健康问答、细胞重编程和膝关节力学模拟。AI×Math关注三维推理基准与球体表示的符号推理。AI Voices收录官方技术博客与研究简报，Engineering呈现浏览器、金融基础模型和多智能体工作流等GitHub项目。

## 今日重大进展

- [单次 MRI 驱动的膝关节力学模拟扩展到 756 膝，揭示软骨负荷与骨关节炎进展关联](https://www.medrxiv.org/content/10.64898/2026.10.29.26366866) — 预印本提出从单次膝 MRI 自动构建生物力学模型的管线，结合深度学习分割、神经形状模型和接触力学，在 756 个膝关节、7,560 次标准步态模拟中实现 99.6% 收敛，并关联组织压力与六年软骨变薄。
- [Lightpanda 开源 AI 无头浏览器冲上 GitHub Trending 前二，瞄准代理自动化运行时](https://github.com/lightpanda-io/browser) — Lightpanda 开源轻量无头浏览器，面向 AI 代理与自动化，兼容 CDP、Playwright 和 Puppeteer；项目在 GitHub Trending 排名第 2，当日新增 827 星、累计约 4 万星。

## AI × Chem

采集 1297，候选 60，精选 3。来源状态：各来源已完成

- [Harness engineering enables a multi-agent LLM system to generate cross-domain hypotheses beyond single-investigator reach](https://www.biorxiv.org/content/10.64898/2026.10.25.761203) — 研究一个连接五个 Model Context Protocol 服务器、调用 66 个外部工具的生物学多智能体 LLM 系统，比较 Claude Sonnet 4.6 与 Opus 4.8，并提出 ABCD-Stack harness。结果显示，在提示词、模式、假设数量和查询完全匹配时，模型层级差异消失，harness 设计比模型升级更能决定假设质量。
- [Practical Assessment of Agentic Systems in Acoustics](https://arxiv.org/abs/2610.39685v1) — 评估 agent 及其 harness 组件在两类声学工程任务中的作用：车辆内音频故障检测与超材料单元设计。系统在故障定位上接近完美，并能找到满足指定频段插入损耗的超材料单元；基准分析显示，弱模型会限制 harness 的收益。
- [Spectroscopy-Based Machine Learning to Predict Stem-End Rot in Avocados with the Temporal Effects](https://www.biorxiv.org/content/10.64898/2026.10.29.762723) — 使用鳄梨高光谱 Vis-NIR 数据预测茎端腐烂，比较仅光谱、加入储藏时长和加入一阶动力学约束的 PINN 三种模型。模型在早期储藏数据上训练、在第12天测试，PINN 在未见时间条件下泛化最好，而简单加入时间会过拟合。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1921，候选 60，精选 10。来源状态：各来源已完成

- [FateDriver: Weakly supervised dual-view graph learning for transition-specific prioritization of candidate regulators in cellular reprogramming](https://www.biorxiv.org/content/10.64898/2026.10.27.762150) — 【preprint】FateDriver 是一种弱监督双视图图神经网络，将单细胞转录组中的细胞和基因联合建模，并利用已递送诱导因子为稀疏标签，针对特定细胞重编程转变优先排序候选调控因子。
- [Neural shape models enable cohort-scale simulation of knee cartilage mechanics](https://www.medrxiv.org/content/10.64898/2026.10.29.26366866) — 【preprint】利用深度学习分割、神经形状模型和弹性基础接触模型，从单次 MRI 自动构建膝关节生物力学模型，并在 Osteoarthritis Initiative 的 756 个膝关节和 10 种标准步态下完成队列规模模拟。
- [Autonomous Hypothesis Testing Against Public Biomedical Data with Literature-Grounded Calibration](https://europepmc.org/article/PPR/PPR1353529) — 【preprint】提出一个四阶段、盲法且以文献校准的自主计算假设检验流程，在五项生物医学任务中评估数据发现、分析执行和结果验证能力。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 406，候选 60，精选 2。来源状态：各来源已完成

- [Where Do Vision Language Models Fail at 3D Reasoning?](https://arxiv.org/abs/2610.39639v1) — 提出 BedBench，用 13 个程序生成任务评估视觉语言模型在三维推理中的单项判断、组合答案、一致使用属性和图像依赖。12 个开放权重模型与 4 个前沿模型的结果显示，模型在逐颜色计数及其一致运用上明显落后于人类；微调和提供文本计数可改善部分表现，但不能稳定解决精确组合回答。
- [Non-Zero Radius: The Missing Component of Neural Networks](https://arxiv.org/abs/2610.39559v1) — 提出 Sphere Neural Networks（SphNNs），将概念表示为具有非零半径的球体，并以 transition map 进行无训练的亚里士多德三段论推理。论文把该表示视为对传统零半径向量表示的理论扩展，但候选摘要未提供与现有符号推理系统的系统性基准。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 20，候选 18，精选 3。来源状态：X: RuntimeError: 未找到 Grok X 检索缓存。请先按 ops/grok/x_harvest_protocol.md 采集

- [Run AI Models for Edge Application Development with Just a Few Commands](https://developer.nvidia.com/blog/run-ai-models-for-edge-application-development-with-just-a-few-commands/) — 事实：NVIDIA 技术博客介绍了用少量命令运行边缘 AI 模型的方式，并以驾驶员注意力和座舱状况监测等场景为例。作者观点：AI 应用正在从数据中心扩展到边缘。编辑判断：内容面向实际部署，能为边缘智能体开发提供工程入口。
- [Build Specialized Agents on a Stack You Control with NVIDIA NemoClaw](https://developer.nvidia.com/blog/build-specialized-agents-on-a-stack-you-control-with-nvidia-nemoclaw/) — 事实：NVIDIA 技术博客将自主智能体拆分为模型、工具链和领域专用工具，并介绍用于更安全部署的 NemoClaw 运行时。作者观点：安全部署需要由运行时强制执行约束。编辑判断：文章提供了面向可控智能体栈的具体工程框架。
- [Microsoft Research Focus – Edition #97](https://www.microsoft.com/en-us/research/podcast/microsoft-research-focus-edition-97/) — 事实：Microsoft Research 的第 97 期节目汇总了编码智能体挑战、职场中的 AI 使用方式和扩展期天气预报等研究动态。作者观点：这些议题代表微软近期值得关注的研究方向。编辑判断：虽然是研究综述而非单篇论文，但覆盖面和官方来源使其具有信息筛选价值。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 64，候选 57，精选 7。来源状态：各来源已完成

- [lightpanda-io/browser](https://github.com/lightpanda-io/browser) — Lightpanda 是面向 AI 与自动化的轻量级无头浏览器，兼容 CDP、Playwright 和 Puppeteer；2026-11-02 GitHub Trending 第 2 名，当日新增 827 颗星。
- [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) — Kronos 是面向金融市场语言的基础模型，用于建模和理解市场数据；2026-11-02 GitHub Trending 第 3 名，当日新增 611 颗星。
- [sponsors/Donchitos](https://github.com/sponsors/Donchitos) — Donchitos 将 Claude Code 组织成完整的游戏开发工作室，提供 49 个 AI 智能体、72 个工作流技能和模拟真实工作室层级的协作系统；2026-11-02 GitHub Trending 第 8 名，当日新增 970 颗星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
