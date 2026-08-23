# AIxDaily · 2026-08-24

今日精选呈现两条主线：化学、生物与数学频道均以预印本为主，研究设计和结果仍需同行评议及独立验证；AI Voices 收录的是机构发布与研究者公开观点，所述性能多为发布方主张；工程频道则集中于官方软件正式发布，涉及生成工作流、LLM 服务和开发协作工具。

## AI × Chem

采集 1227，候选 60，精选 16。来源状态：各来源已完成

- [Systematic Benchmarking of AI-Based Molecular Generation Models for Structure-Based Drug Design](https://www.biorxiv.org/content/10.64898/2026.08.14.744939) — 该研究在176个经过整理、覆盖多类治疗靶点的蛋白—配体体系上，比较了12种分子生成与优化方法，并以已获实验验证的配体界定参考化学空间。评测显示，不同架构各有优势：受体条件化方法利用结合口袋几何，流模型采样效率较高，参考条件化方法适合类似物生成，合成感知设计则改善化学可行性；没有单一方法能够同时优化全部指标。作者还构建了整合分子动力学受体构象集合、集合对接和蛋白—配体相互作用图的SAFC，用于给生成分子提供动态感知的功能活性排序。
- [Resolution-standardized evaluation of ligand atomic coordinates in crystallographic structures using machine learning](https://www.biorxiv.org/content/10.64898/2026.08.17.745351) — 研究提出原子Box Correlation Coefficient（aBCC），在分辨率标准化框架中逐原子衡量配体坐标与电子密度的一致性；并以3D-CNN模型QAEmap从电子密度图预测aBCC。模型使用PDB高分辨率结构构建的傅里叶截断电子密度图和相应配体坐标训练，在截断图与实验PDB结构上评估，预测在约3.5 Å以内仍可靠。
- [PandaDock: An Open-Source Molecular Docking Platform with Flexible-Ligand Search and Equivariant Neural Scoring](https://www.biorxiv.org/content/10.64898/2026.08.19.745667) — PandaDock是开源分子对接平台，结合柔性配体构象搜索、预计算亲和力网格、诱导契合/金属配位/锚定对接模块和SE(3)等变GNN评分。作者在814个复合物和多个独立数据集上报告姿势恢复、亲和力预测与运行效率；其经验评分函数在30个GABAA受体化合物系列中位列25种方法第8。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2132，候选 60，精选 11。来源状态：各来源已完成

- [The urinary-metabolite-based lung cancer index (uLCI): an interpretable machine-learning risk model for early-stage disease](https://www.medrxiv.org/content/10.64898/2026.06.26.26356700) — uLCI 将4种尿液代谢物与年龄、种族和吸烟情况整合为可解释的肺癌检测风险指数，并在独立队列中完成无重新拟合验证。
- [Explainable Transformer Models for Clinical Prediction Tasks on Structured Electronic Health Records](https://arxiv.org/abs/2608.20315v1) — BERT-LER 在7,500万名患者的去标识化 EHR 上预训练，以百分位分箱表示检验值，并给出事件级归因。
- [CorSeg-CineSAX: An Open-Source Deep Learning Framework for Fully Automatic Segmentation of Short-Axis Cine Cardiac MRI Across Multiple Cardiac Diseases](https://www.medrxiv.org/content/10.64898/2026.04.01.26349955) — CorSeg-CineSAX 开源发布心脏短轴电影 MRI 自动分割模型，并在内部与三个独立公开外部数据集上评估。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 228，候选 60，精选 2。来源状态：OpenReview: RuntimeError: 未配置 OpenReview 账号

- [FormalTCS: Benchmarking End-to-End Frontier Formal Theoretical Computer Science Research of Large Language Models](https://arxiv.org/abs/2608.20153v1) — FormalTCS以2025—2026年STOC、FOCS、SODA和COLT论文为来源，构建175项端到端理论计算机科学研究任务，并保留经专家核验的Lean形式化与证明。
- [Rule-Compliant Visual Spatial Planning for Multimodal Large Language Models](https://arxiv.org/abs/2608.20237v1) — RuleMaze以带自然语言规则的迷宫任务评测MLLM的视觉感知、规则解释与受约束行动规划，并用可执行验证器检查规则遵循。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 77，候选 60，精选 9。来源状态：各来源已完成

- [@deepseek_ai：DeepSeek-V4-Flash-Vision-Exp is now live on the DeepSeek API Platform! 🚀 🔹 This experimental multimodal model matches De](https://x.com/deepseek_ai/status/2090730032574631962) — DeepSeek 宣布实验性多模态模型 DeepSeek-V4-Flash-Vision-Exp 上线，并称其文本能力与 V4-Flash 相当，多模态智能体基准表现接近 Opus-4.8；同时发布了支持该模型的 Harness 0.1.1。
- [@chelseabfinn：One of the most important aspects of scientific discovery is deciding where to draw insights from. While LLMs are promis](https://x.com/chelseabfinn/status/2091320499498553656) — Chelsea Finn 指出，科学发现的一项关键工作是判断应从何处提取洞见；她认为 LLM 用于科学虽有潜力，但这一环节仍缺少数据集和评测，并邀请公众参与相应数据集建设。
- [@EinsiaAI：1/ Recursive self-improvement (RSI) depends on agents improving how AI systems are trained —not just tuning hyperparamet](https://x.com/EinsiaAI/status/2090854778301771909) — Einsia 发布 AI4AI-Bench 的结果，称该基准涵盖 10 个真实研究仓库和 10 类算法；帖文报告平均得分 0.166、最高模型 Opus 5 得分 0.288，并给出探索成本数据。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 60，候选 60，精选 7。来源状态：各来源已完成

- [Diffusers 0.40.0: New pipelines, tensor-parallel support, improved CLI, and more](https://github.com/huggingface/diffusers/releases/tag/v0.40.0) — huggingface/diffusers 发布 v0.40.0，新增 MiniMax-H3、MiniMax Music 3、Stable Audio 3、LTX-2.5、Wan-Animate-2 等管线；Modular Diffusers 转为稳定支持，并加入 CUDA 与 AWS Neuron 的 tensor-parallel 推理、量化后端及路径遍历修复。
- [Ray-2.58.0](https://github.com/ray-project/ray/releases/tag/ray-2.58.0) — ray-project/ray 发布 ray-2.58.0，完成 Ray Serve LLM 的 KV cache/token 感知路由，推出 Ray Sandbox、TPU 调度与 Ray Data shuffle v2，并修复 Ray Data 任意代码执行风险和 Serve token 认证绕过。
- [0.149.0](https://github.com/openai/codex/releases/tag/rust-v0.149.0) — openai/codex 发布 rust-v0.149.0，加入 `codex agents` 任务面板、工作目录命令、`codex queue`、更完整的 Vim 编辑与扩展的 `codex doctor` 诊断；同时修正会话权限、子 Agent 通知和实时连接恢复等问题。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
