# AIxDaily · 2026-10-23

今日精选：AI × Chem 15 项，AI × Bio 13 项，AI × Math 16 项，AI Voices 10 项，Engineering 10 项。本期共同日期为 2026-10-23。化学、生物和数学频道的前三项均为预印本：化学聚焦强化学习酶工程、自动化级联反应与手性膦酸酯合成；生物聚焦单细胞资源、药物反应基准和跨物种基因组注释；数学聚焦可验证证书与形式化程序验证。AI Voices 收录三条 X 公开观点，涉及长上下文检索、软件安全证明和地球观测嵌入。Engineering 为 GitHub Trending 项目，前三项不是版本发布。上述前三项未见同行评议论文。

## 今日重大进展

- [Anthropic称Claude已在百余个真实开源库上完成大规模形式化安全验证](https://x.com/AnthropicAI/status/2113390212911083894) — Anthropic在Frontier Red Team官方帖文中称，与Theorem合作使用Claude，在数周内为100多个真实世界开源软件库证明安全属性，显示形式化验证开始从小型代码库走向大规模软件。
- [Carbon-X：14B开放DNA模型据作者报告逼近前沿模型，成本低约千倍](https://x.com/Thom_Wolf/status/2113345703485309335) — Thomas Wolf公布Carbon-X：与TIGEM等机构合作训练的开放14B DNA模型，在其团队基准上得分67%，接近GPT-6.1 Sol，宣称约低1000倍成本；权重开放，可在学术界可获得的笔记本硬件上运行。
- [CascadeMAP让酶级联优化进入七天无人值守的闭环实验](https://www.biorxiv.org/content/10.64898/2026.06.04.730034) — bioRxiv预印本报告CascadeMAP将微流控、高通量检测、贝叶斯优化和多智能体分析接成闭环；平台连续无人运行7天，处理约29.5万次反应、7400种条件，并以少三倍实验条件达到相近最优值。

## AI × Chem

采集 2646，候选 60，精选 15。来源状态：各来源已完成

- [Reinforcement learning with evolutionary priors unlocks multi-site enzyme optimization from sparse experimental feedback](https://www.biorxiv.org/content/10.64898/2026.10.19.760152) — 提出 AlphaVariant，将生成式进化先验、低样本适应性模型和强化学习结合，用稀疏实验反馈搜索多位点蛋白序列空间，并在 savinase 活性、多目标性质和应用测试中验证。
- [CascadeMAP: Autonomous Closed-loop Optimization of Enzyme Cascades via Microfluidics, Machine Learning and Agentic AI](https://www.biorxiv.org/content/10.64898/2026.06.04.730034) — 构建 CascadeMAP 自动化微流控闭环平台，将 Bayesian optimization、多智能体分析和正交检测用于两类三酶级联反应优化，连续无人运行 7 天。
- [Outpacing H-Phosphonate Oxidation: Enantioconvergent Deborylative Synthesis of α-Stereogenic Alkyl Phosphonates](https://doi.org/10.26434/chemrxiv.15010820/v1) — 报道首个不对称 deborylative C(sp3)–P 偶联，以手性配体调控铜的氧化还原性质，实现 α-手性烷基膦酸酯的对映收敛合成，并结合循环伏安、Hammett 分析、化学计量实验和 DFT 解析机理。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 3388，候选 60，精选 13。来源状态：各来源已完成

- [GENOAR: Global Engine for Navigating the Omnicell space via Agent-based Research](https://www.biorxiv.org/content/10.64898/2026.10.15.759380) — GENOAR以AI代理和并行计算构建覆盖约5400万个人类与小鼠细胞的可检索单细胞转录组资源，并验证了视网膜母细胞瘤祖细胞相关信号。
- [Predicting Pre-treatment Resistance or Post-treatment Effect? A Systematic Benchmarking of Single-Cell Drug Response Models](https://www.biorxiv.org/content/10.64898/2026.04.10.717709) — 对26个数据集、超过760,000个细胞、12种癌症和21种治疗药物的单细胞药物反应模型进行系统基准评测，并纳入有实验验证的谱系追踪数据。
- [Carbon-A: Unified Genome Annotation across Eukaryotic Diversity](https://www.biorxiv.org/content/10.64898/2026.10.20.760448) — Carbon-A用单一1.2-billion-parameter模型跨真核生物预测蛋白编码基因，并在42个基因组和GenBank大规模数据库上评测。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 1316，候选 60，精选 16。来源状态：各来源已完成

- [LLM2Cert: LLM Synthesis of Certificates with SMT/Lean Verification](https://arxiv.org/abs/2610.30524v1) — 提出 LLM2Cert 与 DynaCertBench：让 LLM 生成 Lyapunov 函数和 barrier certificates，再由 SMT 或 Lean Proof-Repair 检查证明义务；在 105 个实例上验证通过 81 个（77.1%），比无反馈的一次性提议高 17.1 个百分点。
- [VERDICT: Multi-Agent Parallel Modular Verification](https://arxiv.org/abs/2610.29147v1) — 提出 VERDICT 多智能体框架，用假设式并行规范综合和双向跨过程冲突协调并行化大型程序的演绎验证；在真实 C 程序上提高规范质量并缩短验证时间，并扩展到完整的 20,000 行 X.509 解析器。
- [TrustedCode: Evaluating Large Language Models for Developing Trusted Code through Automated Program Verification](https://arxiv.org/abs/2610.30432v1) — 提出 TrustedCode，用 LLM 将 AI 生成的 Python 代码类型检查、翻译为 WhyML，并通过 Why3 后端自动定理证明器验证形式化规范；在 10 个不同复杂度的程序上分析错误来源。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 73，候选 60，精选 10。来源状态：各来源已完成

- [@chelseabfinn：How do we scale up the context of LLMs? Agentic search scales to arbitrarily large amounts of info, but can easily miss ](https://x.com/chelseabfinn/status/2113036636586131475) — 作者报告一种通过优化信息组织来提升智能体搜索下游效用的方法，在分布外领域带来 30% 以上的增益，并公开论文和代码。
- [@__alpoge__：(Quite topical, of course note caveats!) Most software is riddled with bugs, which AI can now easily find and exploit. F](https://x.com/__alpoge__/status/2113410635673550975) — 作者介绍与 Theorem 的合作：使用 Claude 在 100 多个真实世界开源软件库的 RISC-V 汇编代码层面证明安全属性。
- [@allen_ai：OlmoEarth v1.3 is out. State-of-the-art embeddings from the same foundation model family, precomputed for every 10 m pix](https://x.com/allen_ai/status/2113298265928020126) — Ai2 发布 OlmoEarth v1.3，提供覆盖全球每个 10 米像素的预计算嵌入，并新增浏览器工具用于探索和定制地图。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 60，候选 56，精选 10。来源状态：各来源已完成

- [Nutlope/hallmark](https://github.com/Nutlope/hallmark) — Nutlope/hallmark 是面向 Claude Code、Cursor 和 Codex 的反 AI 低质设计技能；当天位列 GitHub Trending 第 4 名，新增 567 星。
- [makecindy/cindy](https://github.com/makecindy/cindy) — makecindy/cindy 是开箱即用的开源 AI 智能体，覆盖桌面与移动端；当天位列 GitHub Trending 第 10 名，新增 471 星。
- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) — google-gemini/gemini-cli 将 Gemini 能力带入终端，提供开源 AI 智能体和 MCP 客户端/服务端能力；当天位列 GitHub Trending 第 8 名，新增 38 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
