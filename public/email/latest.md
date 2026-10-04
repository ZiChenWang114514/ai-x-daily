# AIxDaily · 2026-10-05

今日精选：AI × Chem 16 项，AI × Bio 15 项，AI × Math 16 项，AI Voices 10 项，Engineering 8 项。今日五频道共同呈现一条主线：AI 正从模型与基准走向可审计、可复现的科研和工程流程。AI×Chem 聚焦耐药抑制剂、高阶分子表示与强关联模拟；AI×Bio 关注生物医学自动化、深度生存分析和生物输入审计；AI×Math 探索 Lean 证明审计、技能演化与可执行验证强化学习，三学术频道前三项均为预印本。AI Voices 是公开帖文，Engineering 是 GitHub Trending 项目，均不等同于同行评议论文或正式软件发布。

## 今日重大进展

- [Google DeepMind 发布 SynthID Bio：把不可见水印直接嵌入蛋白质序列](https://x.com/GoogleDeepMind/status/2105624656170643854) — Google DeepMind 公布 SynthID Bio 水印方法，可在不改变生物学功能的前提下，把不可察觉的签名直接嵌入 AI 生成的蛋白质序列。
- [Ray 2.59.0 将 Ray Data LLM 与 Ray Serve LLM 推至 GA，重做分布式 AI 生产栈](https://github.com/ray-project/ray/releases/tag/ray-2.59.0) — Ray 2.59.0 宣布 Ray Data LLM 与 Ray Serve LLM 达到稳定版，升级 vLLM 0.27.0，并加入磁盘外置 shuffle、压缩、Tracing、KV 路由和集群安全默认值。
- [FORALL-LEAN-AGENT 提出可审计证明流程，作者报告 PutnamBench 672 题全部通过](https://arxiv.org/abs/2610.00885v1) — 预印本提出 FORALL-LEAN-AGENT，把隔离工作区、Lean 工具、命题对照、假设审计和独立复核绑定到同一证明产物；作者报告在 672 道 PutnamBench 题上全部通过。

## AI × Chem

采集 1042，候选 60，精选 16。来源状态：各来源已完成

- [A Dynamics-Informed Machine Learning Framework for Inhibitor Optimization Against Quickly Evolving Targets to Avoid Resistance](https://www.biorxiv.org/content/10.64898/2026.09.25.754496) — ROBUST 将实验抑制常数、分子动力学模拟和可解释统计模型结合，用于分析 HIV-1 protease 耐药突变与抑制剂改造如何共同影响结合能，并优先筛选具有耐药谱优势的 darunavir 类似物。
- [Higher-Order Molecular Grammars for Generative and Foundation Models in Chemistry](https://arxiv.org/abs/2610.02186v1) — HGR 将分子提升为组合复形，并用高阶上下文无关文法解析为规则序列，以显式表示环系和重复基元；作者同时构建 RingDiv 数据集和 RDI 指标。
- [Automated Many-Body Simulations of Strongly Correlated Systems Using a Correlation-Aware Agentic Framework](https://arxiv.org/abs/2610.00943v1) — CAFES 用相关性诊断、自适应方法选择和 LLM 辅助，自动编排强关联体系的多体电子结构计算，并在 lutein、扩展 honeycomb Hubbard 模型和 CCSD 数据集上展示工作流。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1731，候选 60，精选 15。来源状态：各来源已完成

- [Prompt-as-a-Protocol with Agentic Research Automation: A Validated Methodology for AI-Native Biomedical Data Science Producing Peer-Reviewed Findings Across Genomics and Biosensor Domains](https://europepmc.org/article/PPR/PPR1332696) — 提出 Prompt-as-a-Protocol（PaaP）与 Generative Research Automation（GRA）方法，把自然语言研究问题转为可执行分析协议，并在单细胞转录组和生物传感器两个前瞻性案例中验证。
- [Deep Survival Analysis: A Comprehensive Review of Methods, Applications, and Open Challenges in Biomedicine](https://europepmc.org/article/PPR/PPR1331894) — 系统综述2018—2026年深度生存分析方法、应用、数据集与评估实践，覆盖 Cox 扩展、离散时间、分布式、多模态、Transformer 和基础模型范式。
- [When Do Biological Reasoning Models Use Their Biological Inputs?](https://arxiv.org/abs/2610.00898v1) — 对六种生物推理模型在 DNA、蛋白质和单细胞任务中的输入依赖进行扰动、证据冲突、线性探针和推理轨迹审计，发现部分模型的生物基础模型输入对性能贡献很小。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 509，候选 60，精选 16。来源状态：各来源已完成

- [FORALL-LEAN-AGENT for Auditable Reasoning in Formal Mathematics and Software Verification](https://arxiv.org/abs/2610.00885v1) — FORALL-LEAN-AGENT 将 Lean 工具、隔离工作区、陈述对照、公理审计和独立复核绑定到同一候选证明工件，提供可追溯的形式化数学与软件验证审计流程。
- [SkillEvoLean: Mutation-enhanced skill evolution for Lean provers](https://arxiv.org/abs/2610.01799v1) — SkillEvoLean 在 Lean 定理证明中联合演化求解策略与数学参考知识；当轨迹全部失败时，以概念引导的变异生成新技能，并由 Lean 验证器筛选。
- [Function-Structured Reinforcement Learning with Executable Verifiers for Mathematical Reasoning](https://arxiv.org/abs/2610.01729v1) — FSG-RL 将子问题函数图、Python 实现和多重可执行验证器结合，用答案门控奖励与片段级信用分配训练算法化数学推理。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 89，候选 60，精选 10。来源状态：各来源已完成

- [@shobhitbanga：Introducing Sales Agent Eval by Voice Arena: a live benchmark that ranks voice sales agents by revenue from real sales a](https://x.com/shobhitbanga/status/2106734834832081050) — 事实：Voice Arena 发布 Sales Agent Eval，将语音销售代理置于真实销售收入和人工基线下进行实时排名。
- [@ylecun：Training frontier models is expensive; distilling is cheap; this market force tells us frontier foundation models will b](https://x.com/ylecun/status/2106783662117151003) — 作者观点：Yann LeCun 认为前沿模型训练成本高、蒸馏成本低，这种市场力量将推动前沿基础模型走向免费和开放。
- [@ritakozlov：today we open sourced clef and clef-flash, our first homegrown models, now available on Cloudflare Workers AI. https://b](https://x.com/ritakozlov/status/2105683951595725177) — 事实：Cloudflare 开源 clef 和 clef-flash，称其为首批自研模型，并在 Cloudflare Workers AI 上提供。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 78，候选 60，精选 8。来源状态：各来源已完成

- [tester-army/e2e](https://github.com/tester-army/e2e) — tester-army/e2e 是面向 Web 和移动应用的端到端测试框架；当日 GitHub Trending 第 1 名，新增 344 星。
- [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) — Panniantong/Agent-Reach 为 AI 智能体提供跨站点读取与搜索能力，可接入 Twitter、Reddit、YouTube、GitHub、Bilibili 和小红书；当日 GitHub Trending 第 6 名，新增 979 星。
- [getsentry/sentry](https://github.com/getsentry/sentry) — getsentry/sentry 是面向开发者的错误跟踪与性能监控平台；当日 GitHub Trending 第 7 名，新增 152 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
