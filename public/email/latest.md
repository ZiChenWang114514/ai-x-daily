# AIxDaily · 2026-10-25

今日精选：AI × Chem 5 项，AI × Bio 16 项，AI × Math 4 项，AI Voices 7 项，Engineering 8 项。今日五频道共同日期为2026年10月25日。化学、生物前三项均为预印本，涵盖催化与材料、染色质机制、医疗数据治理、皮肤病分类及临床LLM使用；数学前三项为arXiv预印本，聚焦开放式智能、UML生成幻觉和长对话状态完整性。AI Voices前三项为X公开帖文，涉及Brotli漏洞、论文串讲和约化轮SHA-256分析。Engineering前三项为GitHub Trending软件项目动态，非版本发布；前三项未见可确认的同行评议论文。

## 今日重大进展

- [OpenAI红队披露Brotli未授权远程代码执行漏洞，修复波及Node.js等下游生态](https://x.com/OpenAI/status/2113766354386084338) — OpenAI公布红队测试发现：广泛用于 Node.js、Bun、Envoy 等软件的 Brotli 压缩库存在可被恶意压缩数据触发的未授权远程代码执行漏洞；Brotli、Node.js 等下游项目已发布或正在发布修复。
- [研究者报告将SHA-256约化轮碰撞推进至39轮，安全裕度再收窄](https://x.com/FutureDies/status/2113251812908151231) — 公开帖文报告：约化 39 轮 SHA-256 碰撞攻击较前人改进逾 30 bit；Hashsmash 社区将复杂度估计更新为约 118.15 bit。完整 SHA-256 仍未被攻破。
- [片段可追溯神经模型把EI质谱预测扩展到8700万级化学库](https://doi.org/10.26434/chemrxiv.15008135/v2) — ChemRxiv 预印本提出片段可追溯的 EI-MS 神经模拟：scaffold split 上 top-1 检索准确率较最强基线提高 32%，达到量子化学模拟水平，速度约快七个数量级，并测试 8730 万分子库。

## AI × Chem

采集 1252，候选 60，精选 5。来源状态：各来源已完成

- [Copper-Catalyzed Borylation of 2-Bromostyrenes via 1,3-Bromine and 1,4-Boryl Group Migrations](https://doi.org/10.26434/chemrxiv.15010958/v1) — 报道铜催化 2-溴苯乙烯与二硼试剂的级联硼化，将副反应转化为 1,4-硼迁移；DFT 解析了反应机理，反应耐受氯取代，对二溴苯乙烯具有位点选择性，并可放大至克级。
- [Controlled Decoration of Electrochemically Exfoliated Graphene with Gold Nanoparticles for Electrocatalysis and Sensing](https://doi.org/10.26434/chemrxiv.15010981/v1) — 以水、氢氧化钠和甘油为试剂，通过一锅法在电化学剥离石墨烯上原位生长无表面活性剂金纳米颗粒，并独立调控粒径与负载量；复合材料用于乙醇氧化和色氨酸传感。
- [Aclarubicin disrupts RNA polymerase II progression at replication-coupled histone genes](https://www.biorxiv.org/content/10.64898/2026.07.08.737292) — 在 aclarubicin 处理的人细胞中使用 CUT&Tag 追踪 RNA polymerase II（Pol II）及其他转录调控因子，发现其强烈扰乱复制耦联组蛋白基因，并导致非生产性 Pol II 转录机器积累。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1986，候选 60，精选 16。来源状态：各来源已完成

- [From Healthcare Data to Actionable Intelligence: An Integrative Review and Gated Framework for Trustworthy Al-Enabled Healthcare Analytics](https://europepmc.org/article/PPR/PPR1348661) — 整合性综述提出 D2AI 门控框架，将医疗数据转化为可负责行动智能的过程划分为数据就绪、证据可追溯、输出可靠和行动就绪四个连续要求。
- [General-Purpose Vision Models to Dermatology-Specific Foundation Models: Comparative Evaluation for Facial Skin Disease Classification](https://europepmc.org/article/PPR/PPR1347902) — 在统一下游分类框架下比较 7 种视觉表征用于 6 类面部皮肤病分类，Derm Foundation 与 XGBoost 组合在测试集达到 88.17% accuracy、88.05% macro-F1 和 98.58% macro-AUROC。
- [Current Attitudes and Use Patterns of Large Language Models in Clinical Practice and Medical Education Among Trauma Providers](https://www.medrxiv.org/content/10.64898/2026.10.20.26366047) — 对创伤照护、临床指南制定和医学教育参与者调查 LLM 使用、态度与风险：62 名临床医生中 15% 每日使用，26% 从不使用；96% 的会后受访者支持将 LLM 教育纳入临床培训。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 357，候选 60，精选 4。来源状态：各来源已完成

- [Co-Recursive Semantic Self-Extension: A Mathematical Foundation for Open-Ended Intelligence](https://arxiv.org/abs/2610.31097v1) — 提出“语义自扩展”框架，用部分赋值、不可判定性和 Kolmogorov complexity 讨论开放式智能的理论边界，并分析外部记忆与多智能体耦合的作用。
- [Tracing Hallucinations in LLM Reasoning for UML Class Diagram Generation: An Empirical Taxonomy and Mitigation Study](https://arxiv.org/abs/2610.30946v1) — 建立 UML 类图生成中 LLM 幻觉的11类经验分类，区分提示忠实性、代码忠实性和推理质量，并在多模型数据与13个 Golden UML ModelSet 案例上评估提示约束。
- [When LLMs Forget What They Believe: Characterizing State Integrity Collapse in Long-Horizon Dialogues](https://arxiv.org/abs/2610.31314v1) — 定义长对话中的 State Integrity Collapse，并提出 StateTrack-Bench，测试数值、格式、角色、事实记忆和逻辑规则约束在多轮对话中的持续执行。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 67，候选 56，精选 7。来源状态：各来源已完成

- [@OpenAI：During this red-teaming exercise, we also found a vulnerability that allows for unauthenticated remote code execution in](https://x.com/OpenAI/status/2113766354386084338) — OpenAI 披露，其红队测试发现 Brotli 压缩库存在可导致未经身份验证远程代码执行的漏洞，并推动 Brotli、Node.js 等下游项目发布修复。
- [@Junioryu136689：Enzyme wet-lab loops, RNA binders in latent space, and clinical AI that gets audited before it ships. BioTender Daily Pa](https://x.com/Junioryu136689/status/2113624758080159787) — BioTender 在帖文中汇总 6 篇新论文，涉及实验反馈驱动的多位点序列搜索、RNA 构象与蛋白质组装、跨模态潜在表示连接、CRISPR 引导序列发现、临床数据成员推断和放射学报告生成。
- [@FutureDies：SHA-256 is not broken, but its security margin lost 1 more round this year: Last week I found a collision attack on redu](https://x.com/FutureDies/status/2113251812908151231) — 密码分析研究者 Dariia Porechna 报告，其对约化 39 轮 SHA-256 的碰撞攻击较先前工作提升超过 30 bit，并在 Hashsmash 协作中继续更新估计复杂度。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 61，候选 53，精选 8。来源状态：各来源已完成

- [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) — cloudflare/security-audit-skill 为编码智能体提供多阶段安全审计，并输出可独立验证的机器可读发现；当天位列 GitHub Trending 第 1 名，新增 2271 星。
- [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) — NVIDIA/OpenShell 提供面向自主 AI 智能体的安全、私有运行时；当天位列 GitHub Trending 第 2 名，新增 893 星。
- [Nutlope/hallmark](https://github.com/Nutlope/hallmark) — Nutlope/hallmark 是面向 Claude Code、Cursor 和 Codex 的反 AI 低质设计技能；当天位列 GitHub Trending 第 4 名，新增 570 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
