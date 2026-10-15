# AIxDaily · 2026-10-16

今日精选：AI × Chem 16 项，AI × Bio 13 项，AI × Math 12 项，AI Voices 10 项，Engineering 9 项。2026年10月16日，五频道前三项精选显示：化学、生物以预印本为主，涉及材料性质预测、聚合物膜、细胞表型、神经退行性疾病与肠道衰老；数学聚焦可执行形式化、定义复用和证据优先验证。AI Voices 汇集 X 公开观点，讨论文本生成、混合推理与个人智能体评测；Engineering 则带来 llama.cpp、Transformers、TRL 软件更新。前三项中未见同行评议论文，预印本和帖文结论仍需核对原文。

## 今日重大进展

- [Blanc 将已部署以太坊字节码纳入 Lean 形式化验证，连精确 Gas 与重入性质也可证明](https://arxiv.org/abs/2610.19764v1) — 研究者提出 Blanc/Jaune 栈，直接读取已部署 EVM 运行时字节码，以 Lean 4 内核检查证书验证真实合约；覆盖精确 gas、存储、重入和主网交易，并给出 EIP-7002、Uniswap V2、Curve 等实例。
- [Transformers v5.20.0 接入 Muse Spark Open，816B 多模态模型进入开源推理栈](https://github.com/huggingface/transformers/releases/tag/v5.20.0) — Hugging Face 发布 Transformers v5.20.0，新增对 Meta Muse Spark Open 的统一支持：816B 总参数、42B 激活参数、最长约104.8万 token，文本、图像、音频和视频共享上下文，并面向代理式编程。
- [Autonomous Science Bench 把 AI 科学代理带入真实测量闭环，公开实验活动与排行榜](https://arxiv.org/abs/2610.18449v1) — 研究者发布 Autonomous Science Bench 0.1，提供六个来自生物、化学和材料实验的预算受限 design-build-test-learn 活动；代理需选择设计、接收实验室测量并迭代，试点144次中最佳配置成功率67%。

## AI × Chem

采集 2044，候选 60，精选 16。来源状态：各来源已完成

- [Predicting Glass Transition Temperature of Polyimide Homopolymers and Copolymers Using Interpretable QSPR-Based Machine Learning: The MFKit Framework](https://doi.org/10.26434/chemrxiv.15010512/v1) — 提出可解释的QSPR机器学习框架MFKit，用物理依据充分的单体描述符和Gaussian Process Regression预测聚酰亚胺均聚物与共聚物的玻璃化转变温度，并以因果推断、SHAP和DSC实验验证结构–性能关系。
- [ReproBAIT: Can coding agents build their own biological AI tools?](https://arxiv.org/abs/2610.19810v1) — 提出ReproBAIT评测编码代理在受限信息、时间和算力条件下重建并训练已发表生物AI工具的能力，覆盖ProteinMPNN、RFdiffusion3和闭源分子设计工具，并专门检测记忆化。
- [Gas-Conditioned Message Passing Graph Neural Network for Permeability Prediction in Polymeric Membranes](https://doi.org/10.26434/chemrxiv.15010381/v2) — 提出气体条件化消息传递图神经网络GC-MPNN，将气体描述符与聚合物单体图联合建模，在leave-one-gas-out设定下预测聚合物膜对未见气体的渗透率，并用主动学习少量补标提升性能。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2008，候选 60，精选 13。来源状态：各来源已完成

- [From Closed-Set Annotation to In-Context Discovery: Biologically Grounded LLMs for Cellular Profiling](https://www.biorxiv.org/content/10.64898/2026.10.07.757352) — 预印本；CellScribe将单细胞基础模型嵌入、细胞本体和元程序整合进同一生成式框架，并用强化学习和上下文学习识别训练词表外的细胞类型。
- [Cerebrospinal fluid dopa-decarboxylase is a biomarker of dopaminergic dysfunction](https://www.medrxiv.org/content/10.64898/2026.10.13.26364985) — 临床相关预印本；在PPMI和独立单中心队列中，脑脊液 DDC 与 DaT-SPECT 指标及运动进展相关，并具有中等至较好的鉴别性能。
- [Progerin disrupts intestinal epithelial homeostasis by impairing mitochondrial metabolism and absorptive enterocyte maturation](https://www.biorxiv.org/content/10.64898/2026.10.09.758066) — 预印本；在两种 LmnaG609G 小鼠模型、肠道类器官和单细胞转录组中，研究显示 progerin 伴随线粒体代谢受损、肠屏障通透性升高及吸收性肠细胞成熟停滞。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 1098，候选 60，精选 12。来源状态：各来源已完成

- [Verifying deployed bytecode against executable EVM semantics, with exact gas and no added axioms](https://arxiv.org/abs/2610.19764v1) — Blanc 将已部署的 EVM 字节码直接接入 Lean 4 证明栈，并以可执行的 Jaune 语义验证真实合约性质，覆盖精确 gas、存储模型、重入和主网交易行为。
- [Definition Grounding in Theory-Level Auto-formalization](https://arxiv.org/abs/2610.19223v1) — Definition grounding 通过持续判断和修订定义，评估理论级自动形式化是否产生可复用、能支撑后续定理的 Lean 定义；ReuseBench 显示定义兼容性仍是主要瓶颈。
- [Evidence-First Agentic Verification](https://arxiv.org/abs/2610.17724v1) — Sauron 是一种证据优先的 agent 验证器，会独立核对环境状态、执行轨迹和声明，并为每个判定生成可审计证据回执；在人类标注和故障注入测试中均优于基线。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 91，候选 60，精选 10。来源状态：各来源已完成

- [@ishanskhare：Excited to announce Next-Concept Modeling (NCM): our new paradigm for fast and parallel, coarse-to-fine text generation.](https://x.com/ishanskhare/status/2110447249901965495) — Ishan Khare 宣布 Next-Concept Modeling（NCM），一种快速、并行、由粗到细的文本生成范式；帖文称其相较参数规模相近的扩散语言模型，在摘要和翻译上快31倍，在无条件生成上快10–21倍，并减少3–5倍训练 token。
- [@omarsar0：Banger paper from Stanford, Together AI, and colleagues. This paper proposes Hybrid Reasoning Agents, which reason inter](https://x.com/omarsar0/status/2110488828062675096) — 帖文介绍斯坦福、Together AI 等团队提出的 Hybrid Reasoning Agents：智能体主要在潜在空间中推理，仅在调用工具或作答时切换到文本；帖文称其在11项基准上平均超过前沿 LLM 智能体10.4%，少用35.5%–54.7% token，速度快1.8–2.6倍。
- [@XiaominLi98：We just launched PersonalAgentEval (https://personalagenteval.com) The first benchmark built to evaluate personal agents](https://x.com/XiaominLi98/status/2110531123424182518) — Xiaomin Li 宣布 PersonalAgentEval，这是一个评估个人智能体的基准，覆盖不同用户、偏好和领域；团队用预先载入13个月真实历史记录的账户，测试了7个流行个人智能体的日常工作流。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 66，候选 60，精选 9。来源状态：各来源已完成

- [v0.7.0](https://github.com/ggml-org/llama.cpp/releases/tag/v0.7.0) — ggml-org/llama.cpp 发布 v0.7.0：加入 LiliCorr 与 GLM5-Next MTP 投机解码、主机内存 MoE 专家 GPU 缓存（官方说明离载场景最高约 2.2 倍解码加速），并扩展多种新模型、嵌入模型和决策模型支持。
- [Release v5.20.0](https://github.com/huggingface/transformers/releases/tag/v5.20.0) — Hugging Face Transformers 发布 v5.20.0，新增 Meta Muse Spark Open 多模态 MoE 模型支持，并原生接入 Ling 3.0 Flash 等模型。
- [v1.16.0](https://github.com/huggingface/trl/releases/tag/v1.16.0) — Hugging Face TRL 发布 v1.16.0，补齐 AWS Trainium/Neuron 训练支持，并改进 AsyncGRPO 的 tree attention 与无 Triton 设备上的融合内核。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
