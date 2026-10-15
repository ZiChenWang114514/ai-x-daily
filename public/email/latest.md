# AIxDaily · 2026-10-15

今日精选：AI × Chem 16 项，AI × Bio 13 项，AI × Math 16 项，AI Voices 10 项，Engineering 8 项。今日五频道共同日期为 2026-10-15。内容以预印本和公开观点为主：AI×Chem 聚焦生成式分子设计、药物发现代理与逆合成；AI×Bio 涵盖乳腺癌预后、创伤性脑损伤血脑屏障和超增强子调控；AI×Math 讨论形式化验证与协作推理。AI Voices 汇总 X 公开帖，Engineering 则是 GitHub Trending 项目快照。所列论文均为预印本，未见同行评议论文；工程条目也不等同于今日软件新版本发布。

## 今日重大进展

- [Google DeepMind称 Gemini 4 Argon 数小时设计出5种经实验室验证的丝氨酸酯酶](https://x.com/GoogleDeepMind/status/2110421871103730104) — Google DeepMind在公开帖文中称，Gemini 4 Argon将酶工程压缩到数小时，设计出5种经实验室验证的丝氨酸酯酶，显示生成式模型开始直接影响湿实验路线。
- [Ai2发布HiRO-ACEv2：全球3公里极端天气模拟成本降至X-SHiELD约1/300](https://x.com/allen_ai/status/2110407184685072881) — Ai2公开HiRO-ACEv2，两阶段把100公里气候模拟下采样到3公里，可生成全球多年极端天气数据；官方称其在百万分之一稀有事件上的统计结果与X-SHiELD相差不超过3%。
- [Anthropic公布Claude蒸馏攻击防御进展，称已显著降低模型复制有效性](https://x.com/AnthropicAI/status/2109795898909950247) — Anthropic在公开帖文中称，过去数月已显著降低针对Claude的蒸馏攻击有效性，并将具体防御方法写入研究博客，回应前沿模型被系统性提取能力的安全问题。

## AI × Chem

采集 2999，候选 60，精选 16。来源状态：各来源已完成

- [Prospective discovery of LasB inhibitors by integrating generative design, free energy ranking, and experimental validation](https://www.biorxiv.org/content/10.64898/2026.10.12.758448) — 提出开源计算—实验一体化流程，将片段式从头分子设计与严格的绝对结合自由能计算结合，用于筛选 LasB 抑制剂；从约40,000个候选中优先合成测试，发现3个此前未报道的纳摩尔级抑制剂。
- [MADDIE: Multi-Agent Drug Discovery Engine](https://arxiv.org/abs/2610.16975v1) — 构建多智能体药物发现引擎 MADDIE，由 Orchestrator 协调 HitIdentifier、LeadOptimizer、Synthesizer 和 Evaluator 四类专门智能体，在50个蛋白靶点上完成分子设计与合成路线规划。
- [Single-step Retrosynthesis via Reinforcement Learning from Forward Feedback](https://arxiv.org/abs/2610.15141v1) — 提出 RetroRLFF，在单步逆合成中同时利用参考反应一致性和冻结正向反应模型的反馈，通过序列级强化学习生成更符合化学可行性的反应物集合。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2978，候选 60，精选 13。来源状态：各来源已完成

- [Multimodal Machine Learning-Based Clinical and Genomic Prognostic Factors for Progression-Free Survival in Metastatic Breast Cancer Using Phase III MONALEESA Trials](https://www.medrxiv.org/content/10.64898/2026.10.09.26364892) — 【preprint；clinical】整合 MONALEESA-2、-3、-7 三项 III 期试验的临床、基因表达和 ctDNA 数据，利用多模态融合模型预测 HR+/HER2− 晚期乳腺癌无进展生存期。
- [Cerebral microthrombi promote focal Cav-1-dependent blood-brain barrier impairment, triggering neuroinflammation and neuronal damage after traumatic brain injury](https://www.biorxiv.org/content/10.64898/2026.09.24.754043) — 【preprint；in vivo】结合荧光纳米示踪、光电关联成像、单细胞转录组和 Cav-1 遗传操作，研究创伤性脑损伤后微血栓、血脑屏障渗漏与神经损伤的联系。
- [Decoding super-enhancer regulatory grammar and pathogenic gain-of-function variants directly from DNA sequence](https://www.biorxiv.org/content/10.64898/2026.10.11.756618) — 【preprint；实验】Borzoi-SE 从长程 DNA 序列直接识别 90 种人类谱系的超级增强子，解析其调控语法，并用 CRISPRi 验证 β-珠蛋白超级增强子中的关键位点。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 2000，候选 60，精选 16。来源状态：各来源已完成

- [TLA-Verus: Generating and Solving Temporal Proof Obligations with LLM Agents](https://arxiv.org/abs/2610.14923v1) — TLA-Verus 将 TLA+ 规约转译为 Verus 证明义务，并用 LLM agent 生成安全性与活性证明。
- [Beyond LLM Judge: Mechanical Verification for Agentic Autoformalization](https://arxiv.org/abs/2610.20573v1) — Beyond LLM Judge 将语义审查与机械数值检查、空洞性检查结合，用于验证 Lean 形式化是否忠实。
- [Compositional RL: Evaluating and Training LLMs for Collaborative Reasoning](https://arxiv.org/abs/2610.17456v1) — Compositional RL 用 Shapley 值与留一法定义模型在协作系统中的贡献，并训练面向整体协作结果的策略。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 70，候选 60，精选 10。来源状态：各来源已完成

- [@r_de_santi：We’re bringing natural-language control to any scientific generator. We are very excited to introduce LLM-to-Flow Distil](https://x.com/r_de_santi/status/2110433657664000234) — 作者介绍 LLM-to-Flow Distillation（LFD）：通过迭代式 DPO，把前沿大模型从自然语言发现目标中提炼出的子目标知识注入科学生成器，并报告其在留出计算评测中超过 FlowGRPO、DiffusionNFT。
- [@AnimaAnandkumar：Excited to share ReRoute, our new framework for scientific counterfactual prediction: informed by partial physics knowle](https://x.com/AnimaAnandkumar/status/2110141540639355137) — Anima Anandkumar 介绍 ReRoute：把观测数据与部分物理知识结合，用轻量微调预测未见过的干预情形；帖文报告气候模拟器误差最多降低31.8%、受控平流–扩散实验反事实误差最多降低89.6%，并给出 Lean 机器检查证明。
- [@Dipanjan_Dey：⚠️ Frontier AI models still fall significantly short of human designers on design creativity. ⚠️ Introducing Design Crea](https://x.com/Dipanjan_Dey/status/2110401121672130566) — Design Creativity Bench 评估16个前沿模型在80个开放式 UI 设计任务中的创意表现；帖文称最佳模型 GPT-6 Astra 得分65.5，而人类设计师参考得分为92.3。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 65，候选 60，精选 8。来源状态：各来源已完成

- [morluto/rea](https://github.com/morluto/rea) — rea 使用智能体从应用行为一路分析到原生二进制，面向逆向工程和开发者工具场景。
- [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) — VoiceStudio 是一个完全本地运行的 ElevenLabs 替代方案，覆盖语音克隆、语音设计、视频配音、听写、转录和有声书制作。
- [sponsors/mksglu](https://github.com/sponsors/mksglu) — mksglu 面向 AI 编码代理优化上下文窗口，通过沙箱化工具输出、持久化会话记忆和 MCP 加钩路由来减少上下文开销。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
