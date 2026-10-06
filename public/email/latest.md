# AIxDaily · 2026-10-07

今日精选：AI × Chem 16 项，AI × Bio 12 项，AI × Math 10 项，AI Voices 9 项，Engineering 9 项。今日五频道共同日期为 2026-10-07。化学与生物前三项均为预印本，重点在酶活性位点设计、mRNA密码子建模、非经典结晶，以及多模态临床证据、轴向干细胞和脓毒症肺损伤机制；数学同样以预印本为主，聚焦自动形式化、可验证辩论和 Lean 搜索。AI Voices 汇总 X 上的公开观点与厂商发布信息，工程频道则是 GitHub Trending 项目，不等同于同行评议或正式软件版本。今日前三项未见可明确归为同行评议论文的条目。

## 今日重大进展

- [预印本主张反驳 3SUM 与 APSP 假设，并提供 Lean 形式化](https://x.com/LechMazur/status/2107349990087458854) — 研究者在公开帖子中介绍一篇新预印本：其主张给出反驳 Randomized Integer Word-RAM 3SUM 猜想的算法，并声称同时处理 APSP 与 Exact Triangle 假设；帖子称该算法由 Anthropic 的 Claude 发现，论文附有 Lean 形式化。
- [OpenAI 发布内部前沿模型产出的722篇数学手稿，涵盖多项开放问题](https://x.com/cagrimbakirci/status/2107606048328593408) — 公开帖子转述 OpenAI 新仓库：内部未命名前沿模型从约4000个问题中筛选结果，发布722篇手稿、372项结果，涉及 Catalan 常数、黎曼 ζ 函数零点带、Hodge 猜想等，部分成果尚未 Lean 形式化。
- [Mistral 发布 Large 4：一万亿参数原生多模态模型，API 即日开放](https://x.com/MistralAI/status/2107457414387622310) — Mistral AI 官方公布 Large 4：总参数约一万亿、激活参数约490亿，原生处理多模态输入，在网络安全、制造、金融和视觉定位任务上宣称达到或超过闭源前沿模型；API 已可用，开放权重计划月底发布。

## AI × Chem

采集 1762，候选 60，精选 16。来源状态：各来源已完成

- [Complex enzyme active site scaffolding by iteratively detuned catalytic guidance](https://www.biorxiv.org/content/10.64898/2026.10.02.756307) — 提出 CaGE，通过逐轮减弱催化约束引导结构预测与序列设计，构建具有复杂活性位点的从头设计酶，并以非血红素铁酶和 PLP 依赖酶验证。
- [A generative language model decodes contextual constraints on codon choice for mRNA design](https://www.biorxiv.org/content/10.1101/2025.05.13.653614) — 提出 Trias 生成式编码器—解码器模型，从数百万条脊椎动物编码序列中学习密码子选择的局部与全局约束，并用于高表达 mRNA 设计。
- [Shaping single crystals through a controlled non-classical crystallization pathway](https://doi.org/10.26434/chemrxiv.15009961/v1) — 利用肽基 MOF 生长过程中的致密液体中间体和液—液相分离，在结晶前塑造单晶形状，并展示形状对机械性能的影响。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2505，候选 60，精选 12。来源状态：各来源已完成

- [Aligning Multimodal Patient Evidence with Biomedical Knowledge Graphs for Clinical LLMs](https://arxiv.org/abs/2610.06685v1) — 【preprint】MM-KG把患者的文本、影像、基因组和生物样本证据与生物医学知识图谱显式对齐，并在MIMIC-IV和ADNI上验证可追溯检索。
- [Capture of Post-Pluripotency Human Neuromesodermal and Neural Tube Axial Stem Cell States](https://www.biorxiv.org/content/10.1101/2024.03.26.586760) — 【preprint】研究捕获了两种人类轴向干细胞（AxSC）状态，并结合全基因组敲除筛选、多组学、DNA甲基化和小鼠嵌合体实验解析其调控特征。
- [Integrated single-cell transcriptomic analysis reveals KLF6-associated macrophage-alveolar epithelial crosstalk in sepsis-associated acute lung injury](https://europepmc.org/article/PPR/PPR1334065) — 【preprint】整合多套小鼠和人类单细胞数据，结合网络、转录因子和细胞通信分析，并用CLP小鼠免疫荧光验证KLF6/CD86共定位。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 1008，候选 60，精选 10。来源状态：各来源已完成

- [AIProver: Agentic Auto-Formalization of Mathematical Research via Certificate-Driven Evolving Harness](https://arxiv.org/abs/2610.05367v1) — AIProver 将 119B 开放权重模型、证书驱动验证和 HarnessEvolve 结合，用于研究级证明自动形式化与证明合成；LoCoBench 和语义正确性指标提供了较清晰的外部评测。
- [When Debate Helps: Proposal Supply and Verification-Aware Readout in Multi-Agent Reasoning](https://arxiv.org/abs/2610.04686v1) — 该工作把多智能体辩论拆成“提出正确候选”和“识别正确候选”两个环节，提出 recoverable headroom 与 Latent Verification Debate（LVD），并在匹配预算下进行控制实验。
- [Symbolic Search Is Not Exhausted: Persistent Proof-Space Exploration in Lean4](https://arxiv.org/abs/2610.04275v1) — ViaLean 在 Lean4 中维护持久化证明状态图，合并语义等价目标并保留已验证中间结构；模型无关配置在完整 miniF2F 测试集上达到 122/244 的 pass@1。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 72，候选 60，精选 9。来源状态：各来源已完成

- [@MistralAI：Meet Mistral Large 4, aka Le Chonk. • 1T parameters, natively multimodal. 49B active. It is the best open weights model ](https://x.com/MistralAI/status/2107457414387622310) — Mistral AI 宣布 Mistral Large 4：1 万亿参数、原生多模态、激活参数 490 亿，并称其在综合基准、网络防御、制造、金融和视觉定位方面达到或超过领先模型；API 已开放，开放权重计划于 10 月底发布。
- [@realchendahuang：GitHub 上出现了一个体量极大的 AI 工程全栈开源教程。 它一口气拆了 20 个阶段、523 个模块： 线性代数、反向传播、神经网络、语音处理、Transformer、模型微调、强化学习、多模态、MCP 协议、Agent 执行循环、多](https://x.com/realchendahuang/status/2107075664889413883) — 陈大黄介绍一个 GitHub AI 工程全栈教程，覆盖 20 个阶段、523 个模块，从基础数学和神经网络延伸到 Transformer、强化学习、多模态、MCP、智能体执行循环和生产部署；帖文称教程还被封装为可安装到 Claude Code 或 Codex 的 Agent 技能。
- [@OpenAI：We’re releasing a broad range of new mathematical results produced by an internal frontier model. We’ve been consulting ](https://x.com/OpenAI/status/2107596713791767021) — OpenAI 表示将发布一系列由内部前沿模型产生的数学结果，并称发布方式参考了高等研究院数学与人工智能独立咨询小组的建议。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 59，候选 57，精选 9。来源状态：各来源已完成

- [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) — earthtojake/text-to-cad 让编码智能体能够根据自然语言生成和处理 CAD 几何；当日 GitHub Trending 第 3 名，新增 620 星。
- [pbakaus/impeccable](https://github.com/pbakaus/impeccable) — pbakaus/impeccable 提供帮助 AI harness 改善设计产出的设计语言；当日 GitHub Trending 第 5 名，新增 609 星。
- [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) — ayghri/i-have-adhd 是用于约束编码智能体输出的技能，帮助其直接给出结论而不是把答案埋在冗长过程里；当日 GitHub Trending 第 7 名，新增 318 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
