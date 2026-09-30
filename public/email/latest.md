# AIxDaily · 2026-10-01

今日精选：AI × Chem 16 项，AI × Bio 15 项，AI × Math 16 项，AI Voices 10 项，Engineering 4 项。今日五频道前三项显示：AI×化学、AI×生物和 AI×数学均以 arXiv/bioRxiv 预印本为主，分别聚焦多模态分子表征、工具增强化学推理、形式化证明与推理不确定性；当前未见同行评议论文入选。AI Voices 汇集 X 上的公开观点与研究发布，涉及自动化基准、蛋白质水印和代理工具链；Engineering 则是 GitHub Trending 项目，涵盖短视频生成、代码知识图谱与技能清单，属于软件项目热度而非新版本发布。

## 今日重大进展

- [ValsAI称用Lean形式化证明七电子Thomson问题，五角双锥成为唯一全局极小构型](https://x.com/ValsAI/status/2104757093039546519) — ValsAI公开称，十个Claude Sonnet 5.5智能体把七电子Thomson问题写成Lean证明：在单位球面上，五角双锥是总库仑能量的唯一全局极小构型（按旋转、反射和重标记同一），证明文件通过Lean内核检查。
- [Google DeepMind发布Gemini 4 Argon，面向复杂编码与网络安全工作流开放测试](https://x.com/GoogleDeepMind/status/2105388084154056939) — Google DeepMind在公开帖文中宣布Gemini 4 Argon，定位为处理编码、企业知识工作和网络安全防御的前沿模型，并通过Fairwind计划向受信任测试者推出。
- [Google DeepMind研究者称SynthID Bio已为AI设计蛋白质加入水印且保留功能](https://x.com/pushmeet/status/2105343729619927236) — Google DeepMind研究者Pushmeet Kohli公开称，团队已成功合成带有SynthID Bio水印且保持功能的AI设计蛋白质，并将其定位为生成生物学溯源与生物安全的概念验证。

## AI × Chem

采集 2670，候选 60，精选 16。来源状态：各来源已完成

- [MoTIF-X: A Multimodal Tokenized Framework for Interpretable and Extensible Molecular Representation Learning](https://arxiv.org/abs/2609.37384v1) — MoTIF-X以图结构化学基元为共同锚点，联合分子图、SMILES和3D构象进行多模态分子表征学习，并用于分子性质预测和药物-靶点相互作用预测。
- [TMCS: Tool-Grounded Multi-Agent Reasoning for Compositional Chemical Problem Solving](https://arxiv.org/abs/2609.35336v1) — TMCS将组合化学问题形式化为由专门化代理、外部工具、少样本轨迹记忆和结构化反思组成的闭环工作流，连接分子生成、理解、编辑、描述和优化。
- [Mirror-Score: Calibrated, Inference-only Scoring Exposes the Limits of Sequence-compatibility Ranking in D-peptide Design](https://arxiv.org/abs/2609.36057v1) — Mirror-Score为异手性D-肽/L-蛋白复合物提出校准的仅推理评分，并用31个晶体复合物和文献亲和力检验ProteinMPNN及Boltz-2评分在D-肽设计中的排序能力。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 3411，候选 60，精选 15。来源状态：各来源已完成

- [Biological rationales from language models enable leakage-resistant forecasts of target-indication success](https://www.biorxiv.org/content/10.64898/2026.09.24.754137) — PRIORITI 以 LLM 整合不依赖具体药物的人类遗传学证据，并在时间外 target-indication 预测中保持校准性能。
- [Combining interstrand crosslinking agents with histone deacetylase inhibitors against high grade IDH mutant gliomas](https://www.biorxiv.org/content/10.64898/2026.09.28.755068) — KL-50 与 belinostat 在患者来源 IDHmut 胶质瘤模型中显示协同细胞毒性，并在原位异种移植模型中延长生存。
- [Prion Protein Deficiency Results in Synaptic, Neural Network and Behavioral Alterations](https://www.biorxiv.org/content/10.64898/2026.04.07.716931) — 多个 Prnp-/- 小鼠模型显示 PrPC 缺失伴随突触蛋白、神经网络动力学和恐惧反应改变。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 1635，候选 60，精选 16。来源状态：各来源已完成

- [Learning to Prove, Not Just to Answer: Reinforcement Learning from Formal Verification for Natural-Language Logical Reasoning](https://arxiv.org/abs/2609.37203v1) — Proof-R1 将自然语言逻辑推理训练改造成带形式验证的证明构造任务：只有通过基于 UNSAT 的机器可检验义务检查的结论，才能进入已验证证明状态，并追踪支撑最终答案的依赖闭包。
- [Probability is Not Enough: Exploring and Counting Divergent Tokens for Reasoning Uncertainty Quantification in LLMs](https://arxiv.org/abs/2609.38070v1) — Divergent Token Confidence（DTC）通过统计两个模型在同一推理轨迹上下一词分布显著分歧的 token 数量，估计 LLM 推理的不确定性；在六个数学基准上报告了优于概率式和口头置信度基线的校准结果。
- [Inducing Process Supervision from Outcome-Only Reinforcement Learning](https://arxiv.org/abs/2609.36641v1) — TIPS 仅使用最终答案是否正确的强化学习信号，训练生成式过程奖励模型同时输出思维链、逐步标签和结果标签；在 ProcessBench 上以 3.2K 条结果标注轨迹取得 85.2 F1。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 81，候选 60，精选 10。来源状态：各来源已完成

- [@jaseweston：Introducing *AutoBenchmark* - Creating benchmarks automatically - Benchmarking benchmark creation - Studying the role & ](https://x.com/jaseweston/status/2105305463784935791) — Jason Weston介绍AutoBenchmark，主张用人—代理协作自动创建和评测AI研究基准，并形成递归改进循环。帖文中的协作优势与方法可行性是作者报告的结果。
- [@pushmeet：Very happy to announce that our team @GoogleDeepmind has pushed the boundaries of generative biology, achieving the succ](https://x.com/pushmeet/status/2105343729619927236) — Google DeepMind研究者Pushmeet Kohli称，团队已成功合成具备功能且带有水印的AI设计蛋白质，并介绍SynthID Bio这一蛋白质水印方法。
- [@LongTermMemoryE：Raven 0.2.0 — The Harness of Harnesses, built for RSI. 🐦‍⬛ One harness can't be best at everything. Raven combines its o](https://x.com/LongTermMemoryE/status/2104745468119146913) — Yafeng Deng发布Raven 0.2.0，这是一个将研究、编码、设计和运维等专用工具链与Claude Code、Codex等代理组合起来的开源“工具链的工具链”，采用Apache-2.0许可。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 17，候选 17，精选 4。来源状态：GitHub Releases: IncompleteRead: IncompleteRead(59567 bytes read, 43279 more expected)

- [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) — harry0703/MoneyPrinterTurbo 使用大模型和自动化工作流，根据主题或关键词一键生成高清短视频；今日位列 GitHub Trending 第6名，新增464星。
- [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) — colbymchenry/codegraph 将代码预索引为本地知识图谱，并在代码变更时自动同步，为 Claude Code、Codex、Gemini、Cursor 等编程代理减少上下文 token 和工具调用；今日位列第14名，新增159星。
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) — ComposioHQ/awesome-claude-skills 汇总用于定制 Claude AI 工作流的 Skills、资源和工具；今日位列 GitHub Trending 第8名，新增118星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
