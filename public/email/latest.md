# AIxDaily · 2026-10-31

今日精选：AI × Chem 12 项，AI × Bio 14 项，AI × Math 14 项，AI Voices 10 项，Engineering 5 项。今日更新以预印本、公开帖文和开源项目为主：化学聚焦自改进分子发现、抗菌药物再利用与反应网络生成；生物覆盖医疗结局预测、肺部影像和儿科脑瘤诊断；数学推进分层奖励、证明评测与 Lean 验证。AI Voices 讨论上下文检索、3D 代码模型和药物开发基金；Engineering 聚焦设计审查、可审计 AI coworker 与 Agent Skills。前三项未见同行评议论文或新软件 Release。

## 今日重大进展

- [Lean 4 内核检验解决 Kullmann 的 w(2;3,21)=416 猜想，209 个情形由 cake_lpr 逐一排除](https://x.com/EitanNahmias/status/2116005645841477818) — 研究者 Eitan Nahmias 宣布，Kullmann 的 w(2;3,21)=416 猜想已由 Lean 4 定理解决；209 个候选情形经内核检查均被 cake_lpr 排除，证明记录已公开。
- [ReactNexus 生成并验证完整反应网络：从反应物图搜索无预设产物的机理路径](https://arxiv.org/abs/2610.38236v1) — 预印本提出 ReactNexus，从反应物图生成过渡态、完整反应轨迹和反应网络，再用机器学习原子间势及 DFT/IRC 验证；作者报告 1 万个候选中 80.8% 通过连接验证，并以碳正离子级联和质谱案例展示用途。
- [Mainplane 以完整会话检索替代有损压缩，开源代理恢复上下文的成本与等待显著下降](https://x.com/Alezander9/status/2115842962521509968) — 研究者 Alexander Yue 发布 MIT 开源 Mainplane：保留完整代理会话，新会话按需检索原文；约 40 万 token 会话中，恢复耗时 38 秒、成本 1.99，降至 15 秒和 0.10。

## AI × Chem

采集 1642，候选 60，精选 12。来源状态：各来源已完成

- [MoLRSI: A Recursive Self-Improving AI agent for Molecular Discovery](https://arxiv.org/abs/2610.39714v1) — MoLRSI通过持久化跨任务记忆和递归优化，自动改进分子发现工作流与搜索策略；在抗生素筛选和肽-MHC结合剂设计中取得了实验验证的命中。
- [Interpreting Graph Neural Networks for Antibacterial Drug Repurposing against Acinetobacter baumannii](https://www.biorxiv.org/content/10.64898/2026.10.26.761825) — 研究用图神经网络解释Acinetobacter baumannii抗菌活性预测，并据此筛选Drug Repurposing Hub，最终测试CE3F4。
- [Generative discovery of chemical reaction networks](https://arxiv.org/abs/2610.38236v1) — ReactNexus从反应物图出发生成过渡态和完整反应轨迹，用机器学习原子间势与DFT/IRC验证反应网络，探索无预设产物或模板的反应机制。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2326，候选 60，精选 14。来源状态：各来源已完成

- [Performance of a foundation model to generate thousands of predicted outcomes across multiple use cases](https://www.medrxiv.org/content/10.64898/2026.10.28.26366723) — PhenOM 在超过 4 亿份纵向患者记录上训练，覆盖 1770 多个结局和数千项预测任务，系统评估未来风险、筛查、照护机会和治疗效果。
- [PulmoDiagAI: An Intelligent Medical Diagnosis System for Automated Pulmonary Pathology Classification using Deep Learning](https://europepmc.org/article/PPR/PPR1351893) — PulmoDiagAI 比较 VGG19、ResNet50、MobileNetV3、EfficientNet-B3 和 DenseNet121，在公开胸部影像数据集上进行肺癌和 COVID‑19 分类。
- [PedDx: An End-to-End Deep Learning Framework for Pediatric Posterior Fossa Tumor Diagnosis with Agentic AI-Enabled Independent External Evaluation](https://www.medrxiv.org/content/10.64898/2026.10.27.26366616) — PedDx 使用 T2 加权 MRI、预训练 3DINO 表征、校准预测和置信度弃答，并在复现、外部验证、分布外和独立机构工作流中评估儿科后颅窝肿瘤诊断。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 689，候选 60，精选 14。来源状态：各来源已完成

- [H^2R: Hierarchical Hint-Based Reward for Mathematical Reasoning via Reinforcement Learning](https://arxiv.org/abs/2610.39934v1) — 提出 H^2R 分层提示奖励框架，把数学题的子问题结构作为 RLVR 的中间监督，并发布 HiMath 基准。Qwen2.5-Math-7B 在 HiMath 上的准确率由 30.4% 提升至 39.1%，使用 Oracle 分层提示时达 45.6%。
- [Ramanujan Challenge Results: AI-Assisted Evaluation Pipeline for Multi-Format Proofs](https://arxiv.org/abs/2610.40551v1) — 分析 Ramanujan Challenge 的研究级数论题提交结果，并提出覆盖自然语言证明、CAS 代码和 Lean 形式化的 AI 辅助评测流程。该流程将自然语言证明误报率从 23% 降至 6%，支持代码判断准确率从 46% 提升至 58%。
- [Scaling Lean Theorem Proving for Real-World Code Verification](https://arxiv.org/abs/2610.38174v1) — 提出 EasyProver，通过递归代理、异步搜索和并行 tactic 探索扩展 Lean 定理证明，并构建 Aegis 实现级验证任务。系统在 PutnamBench、IMO 2026 形式化、NTP4VC 和 VERINA 上接近饱和，在 2,000 个更难语句上 30 分钟内证明了 52.7%。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 77，候选 60，精选 10。来源状态：各来源已完成

- [@Alezander9：Compaction is a mistake. When an agent's context fills up, tools like Codex and Claude Code compact it: 1. The model pre](https://x.com/Alezander9/status/2115842962521509968) — 作者分享 Mainplane 的上下文检索方案：保留完整会话记录，在新会话中按需检索原文，并给出约40万 token 会话的耗时与成本对比。
- [@dextune：Qwen3.5-4B-3D-Coder w/ Three.js A 4B parameter model can generate interactive 3D scenes using Three.js. Qwen3.5-4B-3D-Co](https://x.com/dextune/status/2116164031488868393) — 帖文介绍 Qwen3.5-4B-3D-Coder：4B 参数模型可用 Three.js 生成交互式3D场景；10月29日更新公开了 FP16 权重、训练数据集和技术报告。
- [@BenjamineYLiu：Today we’re announcing the 600M Formation Bio Drug Development Accelerator Fund. @lintaho and I started @FormationBio be](https://x.com/BenjamineYLiu/status/2115446436020027812) — Formation Bio 联合创始人宣布设立6亿美元药物开发加速基金，计划把资本、药物开发经验和 AI 能力结合起来，推动候选药物进入临床。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 68，候选 59，精选 5。来源状态：各来源已完成

- [pbakaus/impeccable](https://github.com/pbakaus/impeccable) — pbakaus/impeccable 是面向编码代理的设计技能与评审词汇，用于改进界面、进行设计审查，并在发布前发现 AI slop；10 月 31 日 GitHub Trending 第 3 名，当日新增 2299 颗星。
- [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) — CopilotKit/OpenBot 提供开源 AI coworker：每个智能体拥有独立浏览器、文件和工具环境，并在执行前决定动作、执行后记录结果；10 月 31 日排名第 4，当日新增 707 颗星。
- [anthropics/skills](https://github.com/anthropics/skills) — anthropics/skills 是 Anthropic 发布的 Agent Skills 公共仓库，为代理提供可复用的技能规范与实现参考；10 月 31 日排名第 11，当日新增 287 颗星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
