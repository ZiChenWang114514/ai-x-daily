# AIxDaily · 2026-09-16

今日精选：AI × Chem 16 项，AI × Bio 12 项，AI × Math 13 项，AI Voices 10 项，Engineering 10 项。9月16日的精选以预印本和公开发布为主：化学、生命科学与数学频道均聚焦尚未同行评议的研究，分别讨论亲和力评测、临床预测数据与形式化验证；AI Voices 收录发布方公告和研究者风险声明，应视为公开观点或发布说法。工程频道则反映 GitHub 趋势项目，非正式软件发布。前列条目中未见可据此确认的同行评议论文，相关性能和应用结论仍需原始研究、独立复现或实测支持。

## 今日重大进展

- [Google DeepMind 发布 Gemini 3.8 Live，主打实时对话与后台任务](https://x.com/GoogleDeepMind/status/2099907440422830269) — Google DeepMind 在 X 发布 Gemini 3.8 Live 与 Extended Thinking，称其为最新对话式 AI；其定位是让模型在用户保持对话时同步思考，并在后台持续处理任务。
- [Diogo Almeida 公布 Jev，称以 RLCD 重排前沿模型的速度与成本](https://x.com/CompleteSkeptic/status/2099925682726002904) — Diogo Almeida 在 X 公布前沿模型 Jev，并称其基于新的 RLCD 训练方式，面向决策型“可组合智能”；发布方给出的指标为速度提升20至200倍、成本降低40至400倍，且输出 token 免费。
- [Omega Institute 公布 AI 智能体形式化证明：解出 Ralf Stephan 2003 猜想](https://x.com/OmegaDesci/status/2099849280433664475) — Omega Institute 称其开源 trureturing 中的 AI 智能体已完成 Lean 形式化证明：对 OEIS A005590 的递推序列，r(3n)=0 当且仅当 n 的二进制展开不含相邻的1。

## AI × Chem

采集 1437，候选 60，精选 16。来源状态：bioRxiv: RuntimeError: Unable to fetch https://api.biorxiv.org/details/biorxiv/2026-09-13/2026-09-16/30: The read operation timed out

- [MIRAGE: Measuring Interpolation and Redundancy in Affinity GEneralization](https://arxiv.org/abs/2609.14491v1) — MIRAGE 提出以蛋白家族历史数据支持度为显式变量的亲和力与构象预测评测框架，显示部分共折叠模型在新蛋白家族上的优势可被家族冗余显著夸大，并发布了相应基准与数据集。
- [Multimodal deep learning from spectra for small-molecule structure identification: enhancing robustness with mixed-condition training](https://arxiv.org/abs/2609.14360v1) — 该研究以混合条件训练和 mixture-of-experts 融合提升 MS、IR、1H NMR 与13C NMR 多模态谱图驱动的小分子候选结构重排序，在缺失、低质量或不一致谱图下保持较强鲁棒性。
- [Can Autonomous LLM Agents Execute Multireference Quantum Chemistry Calculations?](https://arxiv.org/abs/2609.13357v1) — 研究评估自主 LLM 智能体能否完成多参考量子化学工作流，并以结构化决策阶梯改善活性空间选择、收敛恢复与态识别，在 QUESTDB 垂直跃迁能上提高覆盖率并降低误差。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2489，候选 60，精选 12。来源状态：bioRxiv: RuntimeError: Unable to fetch https://api.biorxiv.org/details/biorxiv/2026-09-13/2026-09-16/120: The read operation timed out

- [Potential of Artificial Intelligence Algorithms for Identification of Relevant Diagnostic and Prognostic Biomarkers of Early-Stage Liver Cancer](https://arxiv.org/abs/2609.15638v1) — 研究以三个来源数据集经半监督学习构建的 HCC 转录组标志物数据集训练深度学习模型；15 基因 SelectKBest 模型准确率为 90.74%，并以 SHAP 和功能实验将 DNAJB14 列为重点候选。
- [Countering Neural Activity Drift: Sustained Long-term Seizure Prediction Using an Evolutionary Machine-Learning Framework on Continuous Intracranial EEG](https://www.medrxiv.org/content/10.64898/2026.09.14.26359203) — 该研究公开连续长期立体脑电图数据集，覆盖 16 名患者、664.9 小时数据和 121 次发作，并以伪前瞻在线评估量化神经活动漂移对癫痫预测的影响。
- [Agentic-AI-ready genome-wide poxvirus-host interaction screen refined by a protein language model](https://europepmc.org/article/PPR/PPR1318417) — ICARus 将蛋白质语言模型导出的蛋白—蛋白相互作用信息整合到全基因组 vaccinia virus 宿主因子 RNA 干扰筛选，并提供原始及经修正的筛选读出。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 1371，候选 60，精选 13。来源状态：各来源已完成

- [Beyond Solver Verdicts: Generative Reward Models for Autoformalization](https://arxiv.org/abs/2609.11085v2) — 提出 Generative Verification（GenV），用于检验自动形式化结果是否与指定参考形式化严格等价，而非仅依赖求解器给出的可满足性或判定结果。
- [Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science](https://arxiv.org/abs/2609.15983v1) — Stellar Colosseum 是用于数学与理论计算机科学长程研究的多智能体编排框架，结合策略探索、证明计划分解、反驳和验证反馈回路。
- [Func-R1: Incentivizing Mathematical Function Reasoning in Multimodal Large Language Models](https://arxiv.org/abs/2609.14779v1) — Func-R1 面向图像中函数题的多模态数学推理，通过解耦架构、分层后训练和 PATO 同时处理视觉证据与理论推理。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 107，候选 60，精选 10。来源状态：各来源已完成

- [@MultiverseCompu：⚛️🇪🇺 Introducing Quasar 1.1 438B, the first AI model using quantum-generated data. Quasar 438B, the best European AI mod](https://x.com/MultiverseCompu/status/2099885003492470993) — 事实：Multiverse Computing 在 X 宣布 Quasar 1.1 438B，称其部分“healing set”由运行于 IBM Quantum System Two 的混合量子语言模型生成，并首次进入 CompactifAI 流程。帖文同时提出性能、欧洲部署与合规主张；这些均为发布方说法。
- [@DKokotajlo：Dan Selsam is a current OpenAI capabilities researcher. (since 2022) He was my boss for a while. He doesn't have a twitt](https://x.com/DKokotajlo/status/2099600298855829616) — 事实：Daniel Kokotajlo 转发了一份署名 Dan Selsam 的 AI 风险个人声明。声明作者认为，单靠放缓前沿研发不足以限制长期风险，并把模型在自认未受监控情境下的可评估性视为被忽略的问题。
- [@PhAILabs：Scientific discovery often requires changing the question itself. Today, PhAI Labs releases the technical report for Dis](https://x.com/PhAILabs/status/2099898541342675291) — 事实：PhAI Labs 宣布发布 Discovery Foundation Models（DFM）技术报告，将其描述为能识别未知问题、提出问题、形成假设、设计实验并随证据修正理解的 AI 研究方向。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 57，候选 56，精选 10。来源状态：各来源已完成

- [alibaba/open-code-review](https://github.com/alibaba/open-code-review) — alibaba/open-code-review 是将确定性检查流水线与 LLM 智能体结合的代码审查工具，可给出精确到行的评论，并内置空指针、线程安全、XSS、SQL 注入等多语言规则。它今日位列 GitHub Trending 第 1 名，新增 2,751 星。
- [JustVugg/colibri](https://github.com/JustVugg/colibri) — JustVugg/colibri 是纯 C、零依赖的 MoE 模型推理引擎，通过从磁盘流式加载专家，尝试让既有硬件运行前沿 MoE 模型。它今日位列 GitHub Trending 第 2 名，新增 2,035 星。
- [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) — debpalash/VoiceStudio 是完全本地运行的开源语音工作台，覆盖声音克隆、声音设计、视频配音、听写、转录和有声书制作。它今日位列 GitHub Trending 第 4 名，新增 2,081 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
