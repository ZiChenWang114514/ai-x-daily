# AIxDaily · 2026-10-21

今日精选：AI × Chem 14 项，AI × Bio 12 项，AI × Math 13 项，AI Voices 6 项，Engineering 1 项。今日五频道的更新以预印本为主：化学聚焦蛋白质组反向靶点捕获、反馈式逆合成与 AI—物理—实验药物发现；生物医学强调临床模型校准、医学影像工作流和跨物种基因调控；数学频道集中于 Lean 协调证明与形式化验证。AI Voices 的帖子是公开帖文，涉及 Flora、SKY-001 及 Anthropic 数据开放，性能说法仍属作者自报；Engineering 仅有 DeepSpeed v0.19.8 软件发布，参考项中未见同行评议论文。

## 今日重大进展

- [Maestro 让 Lean 证明器全局协同回溯，Claude Opus 5 解出 PutnamBench 669/672 题](https://arxiv.org/abs/2610.25920v1) — Maestro 论文提出 Lean 证明框架，让证明器报告失败原因并全局回溯重规划；Claude Opus 5 在 arXivLean 48 个定理中找到 34 个证明，PutnamBench 解出 669/672 题。
- [GenFish 将反向靶点捕获改写为生成式检索，覆盖全人类蛋白质组](https://arxiv.org/abs/2610.24458v1) — 论文提出 GenFish，将反向靶点捕获改写为生成式检索，并发布 ProTargetBench；在覆盖 20,431 个人类蛋白的评测中，GenFish 在 198 个留出分子上超过四类神经和三类非神经基线。
- [研究者发布 SKY-001：自称首个工程世界模型，CAD/BIM 速度最高快 125 倍](https://x.com/spisallyouneed/status/2112242023805964327) — 研究者 Sam Pasupalak 在 X 发布 SKY-001，称其为首个工程世界模型；据帖文，CAD/BIM 任务相较测试前沿模型快 51–125 倍、成本低 150–210 倍且 IoU 更高。

## AI × Chem

采集 1438，候选 60，精选 14。来源状态：各来源已完成

- [Generative Retrieval for Reverse Target Fishing with a Proteome-Scale Benchmark](https://arxiv.org/abs/2610.24458v1) — 提出 GenFish，将反向靶点捕获重构为生成式检索，并用 ProTargetBench 评估其在全蛋白质组中恢复实验阳性靶点的能力。
- [ReTRACE: Feedback-Guided LLM Agent in a Chemistry Harness for Retrosynthesis Planning](https://arxiv.org/abs/2610.24744v1) — 提出 ReTRACE 化学智能体，将 LLM、分子工具、单步逆合成引擎、可购买原料库、路线记忆和多标准评估器组合，用评估反馈迭代修正逆合成路线。
- [IMPECCABLE: A Digital Twin Drug Discovery Workflow Comprising AI, Physics and Experiment & the Creation of Nanomolar-Potent Inhibitors](https://doi.org/10.26434/chemrxiv.15002535/v3) — 构建融合物理计算、AI、主动学习和实验药物化学的 IMPECCABLE 数字孪生流程，并在 WDR91 上以前瞻性实验验证获得4个纳摩尔级抑制剂。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2257，候选 60，精选 12。来源状态：各来源已完成

- [Auto-MD-bench: Evaluating Autoresearch Agents for Real-World Medical Tasks](https://arxiv.org/abs/2610.25069v1) — Auto-MD-bench 以 15 个真实医疗任务、10 个临床数据集和跨队列/医院/时间外部验证评估四类自动建模智能体，发现高主指标并不保证校准和跨人群稳健性。
- [MedMCP: An Open Agentic Ecosystem for Medical Imaging Workflows](https://www.biorxiv.org/content/10.64898/2026.10.12.758708) — MedMCP 将本地语言模型的工作流编排与领域工具执行分离，提供带权限门、完整溯源和可重复运行的医学影像分析环境。
- [Predicting cell-state-specific gene regulation from DNA across species](https://www.biorxiv.org/content/10.64898/2026.10.19.760026) — Bolero 用 1,070 万个细胞、33 个数据集和 6 种哺乳动物训练，结合细胞状态嵌入预测 DNA 驱动的状态特异性染色质可及性和转录本丰度。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 853，候选 60，精选 13。来源状态：各来源已完成

- [Maestro: Agentic Formal Proof Development by Coordination](https://arxiv.org/abs/2610.25920v1) — Maestro 是一个面向 Lean 形式化证明的协调式证明框架：它让不同证明器报告失败原因，由全局协调器决定引导、修正错误引理、撤回错误子树并重新规划。四个前沿模型在数学与软件验证基准上测试，Claude Opus 5 在 arXivLean 48 个定理中独立发现 34 个证明。
- [Formally Verified Autoresearch for Analyzing the Expressivity of Multi-Head Attention](https://arxiv.org/abs/2610.25341v1) — 论文研究带加性位置嵌入的单层、仅注意力 Transformer，定义布尔函数的 head complexity，并给出精确正规形、阈值次数下界及一个十比特反例；相关定理由模型提出并在 Lean 中形式化和机器验证。
- [Conformal Prediction-Enabled Sequence-level Policy Optimization for Reasoning Language Models](https://arxiv.org/abs/2610.25092v1) — CSPO 将共形预测用于序列级策略优化，依据近期训练统计量自适应校准裁剪区间，并给出含误覆盖率、CDF 差异和策略漂移项的概率界；Qwen3-1.7B 系列在数学推理基准上相对 GSPO 有改进。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 48，候选 45，精选 6。来源状态：各来源已完成

- [@DrJimFan：We built a robotics data engine with Astra-level performance at 125x lower cost. And we are open-sourcing the weights to](https://x.com/DrJimFan/status/2112597587987689912) — 事实：Jim Fan 宣布开源 Flora 模型套件，用于把原始视频转化为机器人学习训练信号，并称其内部数据引擎每天在500张 GPU 上标注20万小时视频。作者观点：Flora 可将机器人数据引擎成本降至 Astra 级方案的 1/125。编辑判断：这是具有明确数据管线和训练用途的开放模型发布，但性能与成本对比仍需查看完整技术材料。
- [@spisallyouneed：Introducing SKY-001, the first Engineering World Model. On CAD and BIM tasks, it beats GPT-6 Astra and every frontier mo](https://x.com/spisallyouneed/status/2112242023805964327) — 事实：Sam Pasupalak 发布 SKY-001，并称其在 CAD 与 BIM 任务上相较测试的前沿模型速度快51–125倍、成本低150–210倍且 IoU 更高。作者观点：该模型被定位为“Engineering World Model”，服务于自主制造。编辑判断：帖文给出可量化工程指标，但未附基准协议或外部复核，结论应视为自报结果。
- [@AnthropicAI：We’re releasing all 211 of the tested designs and the lab data as a resource for scientists: https://huggingface.co/data](https://x.com/AnthropicAI/status/2112579263039725659) — 事实：Anthropic 宣布公开全部211个经过测试的设计及实验室数据，并提供技术报告。作者观点：这些材料被定位为供科学家复用的资源。编辑判断：相较单纯宣传研究结果，开放设计与实验数据更有利于独立复核和后续方法比较。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 55，候选 52，精选 1。来源状态：各来源已完成

- [v0.19.8 Patch Release](https://github.com/deepspeedai/DeepSpeed/releases/tag/v0.19.8) — microsoft/DeepSpeed 发布 v0.19.8，新增和改进 AutoEP、AutoTP、ZeRO、MoE、连续 rollout、NPU/XPU 后端及 CUDA Graph 等训练与推理能力，同时修复多项内存、梯度、检查点和兼容性问题。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
