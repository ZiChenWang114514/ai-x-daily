# AIxDaily · 2026-10-09

今日精选：AI × Chem 15 项，AI × Bio 14 项，AI × Math 8 项，AI Voices 10 项，Engineering 8 项。今日五频道以预印本和公开发布为主，前三项中未见入选的同行评议论文：化学、生命科学与数学均聚焦尚待同行评议的预印本，涉及合成闭环、临床模型外部验证与形式化验证或推理训练；AI Voices 收录机构和研究者的公开帖文，提示模型供应链和科研协作的新案例；工程频道则是 GitHub 热门开源项目，并非正式软件发布。整体证据强度从实验与基准报告到机构自述不等，应用结论仍需独立复核。

## 今日重大进展

- [纳维—斯托克斯证明主张遭形式化对应关系质疑](https://x.com/ValerioCapraro/status/2108153427742032300) — Valerio Capraro 公开指出，OpenAI 对纳维—斯托克斯方程的自然语言论证与 Lean 对应证明至少有两处不一致，认为形式验证未必覆盖原始命题及推理的语义。
- [Hyper Screening X 报告在万亿级可合成空间闭环发现先导物](https://www.biorxiv.org/content/10.64898/2026.10.01.755933) — 预印本提出 Hyper Screening X，把结构导向生成设计、确定性反应逻辑与自动化合成硬件结合；在 11 万亿可合成分子空间中评估 1000 万候选，并报告获得两种首创先导物。
- [Anthropic 发布面向开源项目的 AI 漏洞扫描服务](https://x.com/AnthropicAI/status/2108302543977906649) — Anthropic 发布 OSS Scanner，称将免费、定期用前沿模型扫描自愿加入的开源项目，并交付含概念验证、问题说明和修复建议的漏洞报告。

## AI × Chem

采集 2048，候选 60，精选 15。来源状态：各来源已完成

- [Synthesis-aware generative design in trillion-scale chemical spaces for automated drug discovery](https://www.biorxiv.org/content/10.64898/2026.10.01.755933) — Hyper Screening X将结构导向生成设计、确定性反应逻辑和自动化合成硬件整合，在11万亿可合成化合物空间中仅评估1000万候选物；面向具有隐蔽界面的SLC1A5变体开展前瞻验证，获得96%的合成成功率、50%的功能命中率及两种首创先导物。
- [CircuitATLAS: Agentic reasoning over a systems neuroscience knowledge graph for target discovery in circuitopathies](https://arxiv.org/abs/2610.09643v1) — CircuitATLAS构建了含383万节点、766万边的可溯源神经科学知识图谱，并以智能体从疾病表型推理至回路、细胞和分子干预。在体内4-aminopyridine挑战中，ATP1A3的中间神经元限制性表达消除了β和γ频段反应，随后进入结构导向小分子开发。
- [Evaluating Autonomous LLM Agents Across Molecular Prediction and Optimization Benchmarks](https://www.biorxiv.org/content/10.64898/2026.10.01.755314) — 研究在TDC ADMET、OpenADMET ExpansionRx、PXR Induction和PMO四类基准上评估自主LLM智能体开发分子方法的能力；多智能体Codex在若干标准设置下达到或超过已发表参照方法。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2933，候选 60，精选 14。来源状态：各来源已完成

- [HealthFound: a health world model for quantitative reasoning on longitudinal health profiles](https://www.medrxiv.org/content/10.64898/2026.10.03.26364142) — HealthFound 在 50 余万人的 15 年纵向记录上构建 1,240 万训练样本，并在 UK Biobank、MIMIC-IV 和 NHANES 中评估医学定量推理与外部泛化。
- [External Evaluation and Calibration Drift of Explainable Machine Learning Models for Acute and Chronic GVHD Prediction After Allogeneic HSCT](https://www.medrxiv.org/content/10.64898/2026.06.14.26355639) — 该研究以 2,509 例训练、14,788 例六队列外部评估，显示 GVHD 预测模型在外部队列中区分度有限且校准可显著漂移。
- [RFM: A Lightweight Retinal Foundation Model for Generalised Oculomics](https://www.medrxiv.org/content/10.64898/2026.10.02.26362554) — RFM 以 430 万张眼底彩照进行自监督领域适配，在六个外部数据集上测试眼科分级、生物标志物回归和事件预测。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 1029，候选 60，精选 8。来源状态：各来源已完成

- [Cost-Efficient Theorem Proving via Agent Orchestration in Program Verification](https://arxiv.org/abs/2610.09681v1) — CoCo-Prover 将 Lean 4 程序验证中的证明搜索建模为兼顾成本的元层决策：在声明内使用 AND/OR 证明超图、在声明间使用引理依赖图，并以路由器协调按次计费的专业代理。在五个函数级与仓库级基准上，论文报告其求解率均最高，并将相对最强基线的成本最多降低 30.9%。
- [Multi-Aspect Runtime Verification for Simulation-Based V&V of LLM-Enabled Autonomous Agents](https://arxiv.org/abs/2610.08928v1) — 该工作将自然语言政策拆为同一事件流上的空间、时间和语义三类监测规范，并以带溯源的四值代数融合判定。在三个模拟领域中，组合式监测器报告将攻击成功率降至零、未观察到假阳性，且具有微秒级单事件开销。
- [BoT-GRPO: Efficient Process-Reward RL for Reasoning via Bag-of-Token Aggregation](https://arxiv.org/abs/2610.09804v1) — BoT-GRPO 以按序列长度加权的 token 奖励聚合替代 GRPO 对整段轨迹共享优势值的做法，无需价值网络。在 React 代码生成和 AIME 数学推理中，论文报告其收敛更快；AIME 的 Pass@k 相对 GRPO 最多提高 8.1 个百分点，且训练步数减半。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 97，候选 60，精选 10。来源状态：各来源已完成

- [@lmoroney：How much would it cost someone to hide a backdoor in an open model you download? ProjectDiscovery just tried it, and the](https://x.com/lmoroney/status/2108071329790370027) — Laurence Moroney 转述 ProjectDiscovery 的演示：攻击者可用低成本 LoRA 微调，为开源工具调用模型植入由特定短语触发的恶意行为；该演示称常规基准测试未能暴露问题。
- [@AnthropicAI：An astrophysicist worked with Claude Science to create the first complete ultraviolet map of the sky. Astronomers have a](https://x.com/AnthropicAI/status/2108290395599667700) — Anthropic 称，天体物理学家 Brice Ménard 借助 Claude Science 汇集既有数据并以统计推断填补空白，制作了完整的全天紫外线地图。
- [@OpenAI：GPT‑6 with Intelligent UI rolls out globally to Plus, Pro, Business, and Enterprise users today and will expand to Free ](https://x.com/OpenAI/status/2107895006350791071) — OpenAI 宣布 GPT-6 及 Intelligent UI 向多个 ChatGPT 订阅层级全球推出，并说明此次变更仅涉及 Chat 标签页，Work 和 Codex 的模型不变。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 73，候选 60，精选 8。来源状态：各来源已完成

- [morluto/rea](https://github.com/morluto/rea) — REA 是用智能体辅助逆向工程的开发者工具，可从应用行为一路分析到原生二进制；今日 GitHub Trending 第 3 名，新增 7,744 星。
- [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) — Anthropic 开源面向知识工作者的 Claude Cowork 插件集合；今日 GitHub Trending 第 7 名，新增 309 星。
- [storytold/artcraft](https://github.com/storytold/artcraft) — ArtCraft 是面向艺术家、设计师和电影制作者的创作引擎；今日 GitHub Trending 第 8 名，新增 2,510 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
