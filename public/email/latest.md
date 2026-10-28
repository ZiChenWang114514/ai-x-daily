# AIxDaily · 2026-10-29

今日精选：AI × Chem 13 项，AI × Bio 14 项，AI × Math 11 项，AI Voices 8 项，Engineering 10 项。今日五频道更新可分三类：AI×Chem、AI×Bio 与 AI×Math 的精选均为预印本，覆盖非经典氨基酸肽结构、激酶—底物互作、医学影像与临床智能体，以及数学证明评测和 Lean 算法设计；AI Voices 汇总 X 上关于基准演进、扑克 AI 教学和代理记忆成本的公开观点；Engineering 发布 PyTorch 2.15、TensorRT-LLM 1.4.0rc2 与 llama.cpp 0.8.0。精选未见同行评议论文。

## 今日重大进展

- [Google DeepMind 宣布 Gemini 4 Carbon，称其在网络安全与长时程任务达业界最先进](https://x.com/GoogleDeepMind/status/2115489356437651654) — Google DeepMind 发布 Gemini 4 Carbon，称其在网络安全和长时程任务上达到业界最先进水平；这是机构对下一代前沿模型的公开发布，具体基准与分数尚未在候选帖中给出。
- [PyTorch 2.15 将重写 NCCL 设为默认，分布式训练与多硬件推理进入新基线](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — PyTorch 2.15 发布，重写 NCCL 成为默认，强化 FSDP2/流水线通信控制，并支持 NVFP4、Apple Silicon FP8 及 CUDA、ROCm、Python 3.15。
- [llama.cpp v0.8.0 为本地模型加入实时音频与 OpenAI Realtime 兼容接口](https://github.com/ggml-org/llama.cpp/releases/tag/v0.8.0) — ggml-org 发布 llama.cpp v0.8.0，新增实验性流式音频、/v1/realtime 与 /tts 接口，并加入文本、视觉、音频和全模态模型架构及多后端优化，让本地推理从文本生成扩展到实时多模态交互。

## AI × Chem

采集 1831，候选 60，精选 13。来源状态：各来源已完成

- [Neopep: Reinforcement Learning From Machine-Learned Force Field Energy for Non-Canonical Peptide Structure Prediction](https://www.biorxiv.org/content/10.64898/2026.10.22.760799) — 提出 Neopep：先在PDB结构上预训练序列条件扩散模型，再利用机器学习力场（MLFF）能量进行强化学习微调，用于含非经典氨基酸（ncAA）肽的结构预测。模型在189种ncAA上训练，并在真实结构评估中取得更低平均RMSD。
- [High-throughput mapping of kinase-substrate interactions with protein language models and phospho-PCA](https://www.biorxiv.org/content/10.64898/2026.10.26.762004) — 构建实验室闭环框架，将蛋白质语言模型 KINBERT 与磷酸化蛋白互补分析（phospho-PCA）结合，用于高通量预测和实测激酶–底物相互作用。研究识别了21种激酶中的23个构建体对应的新型高置信底物，并在标准及分布外基准上验证模型性能。
- [PLANTMETBENCH: A MULTIMODAL KNOWLEDGE GRAPH BENCHMARK FOR BIOSYNTHESIS PREDICTION](https://doi.org/10.26434/chemrxiv.15011165/v1) — 发布 PlantMetBench，多模态植物代谢知识图谱基准，覆盖424种生物、13,682种蛋白质、2,741个基因、4,577种代谢物和11,980个实验整理的酶–反应对。该基准以生物种间不重叠的链路预测任务评估多种异质图神经网络。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2611，候选 60，精选 14。来源状态：各来源已完成

- [Systematic Morphometric Brain Autoencoding for Representation Learning in Neurodegenerative Diseases](https://arxiv.org/abs/2610.37074v1) — SYMBA 是面向结构脑 MRI 的自监督预训练框架，通过解剖约束掩码、多尺度结构相似性重建和渐进式课程学习，利用 6,953 例来自 9 个异质队列的 T1 加权 MRI，在独立数据集上评估神经退行性疾病任务。
- [DocTalk: Enhancing Medical Knowledge Retrieval via Fine-tuned Large Language Models with Chain-of-Thought Reasoning for Robust Clinical Decision Support](https://arxiv.org/abs/2610.34871v1) — DocTalk 从去标识化出院小结生成 500 对临床问答，并比较 6 个开源 LLM 在 LoRA 指令微调前后的医学问答性能，同时在 PubMedQA 上测试外部泛化。
- [ClinVerse: A Realistic Multi-Agent Diagnostic Environment for Training and Evaluating Medical Agents](https://arxiv.org/abs/2610.34878v1) — ClinVerse 基于由真实世界 EHR 派生的 150k 个诊断病例，构建包含 6 个临床角色的多智能体动态诊断环境，并用轨迹级评分训练和评估医学智能体。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 894，候选 60，精选 11。来源状态：各来源已完成

- [Can LLMs Reliably Grade Olympiad Proofs? A Study of Mathematical Verification with LLMs](https://arxiv.org/abs/2610.36767v1) — 研究 LLM 对奥林匹克数学证明进行评分与验证的可靠性，构建含 USAMO 2025 候选解及专家评分的数据集，并比较 20 个模型。MABGrader 在 Quadratic Weighted Kappa 上较 ProofGrader 提高 26.4%，评分误差降低 14%。
- [Agentic Algorithm Design: LLMs that Propose, Formalise, and Prove Runtime Bounds for Evolutionary Algorithms in Lean](https://arxiv.org/abs/2610.35595v2) — 提出一个分阶段流程，让 LLM 在 Lean 中同时完成进化算法设计、形式化和运行时间证明。15 次运行中有 12 次在 8 类问题上得到机器检查的期望运行时间界，并通过消融显示分阶段设计优于零样本设计。
- [Agent-Conditioned Routing: Diverse Reasoning Paths Within One Frozen Model](https://arxiv.org/abs/2610.37375v1) — 研究冻结稀疏 MoE 模型能否通过不同专家可用性掩码产生多样数学与物理解法。ACR 在 126 题基准上提高了产生至少两种主要方法的题目比例，但盲审显示正确率较低。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 80，候选 60，精选 8。来源状态：各来源已完成

- [@polynoamial：Only 2.5 years ago, AI labs would highlight their frontier LLM performance on grade school math benchmarks (GSM8K). I ca](https://x.com/polynoamial/status/2114886357739000015) — Noam Brown指出，仅两年半前，AI实验室还常用GSM8K小学数学基准展示前沿模型能力，并期待未来两年半继续出现跨越式进展。
- [@polynoamial：Every winter, @MIT has run a 1-month class (6.9630) in which students make poker AIs and compete against each other for ](https://x.com/polynoamial/status/2115125429619343609) — Noam Brown介绍MIT每年冬季举办的一个月扑克AI课程，并称编码代理已将扑克机器人原型制作时间压缩到约一小时。
- [@sermakarevich：A review of 30 memory products for AI agents: what each one saves, how it gets memory back into the prompt, what happens](https://x.com/sermakarevich/status/2115087554877776113) — Sergii Makarevych称其评测覆盖30款AI代理记忆产品，比较记忆写入、回填提示词、事实变更处理及被价格页忽略的提取token成本。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 68，候选 60，精选 10。来源状态：各来源已完成

- [PyTorch 2.15.0 Release](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — PyTorch 2.15.0 发布：重写 NCCL 后端成为默认，FSDP2 与流水线获得更细的通信和显存控制，新增 NVFP4 解码、Apple Silicon FP8、CUDA 13.2/13.4、ROCm 10.0 与 Python 3.15 支持。
- [v1.4.0rc2](https://github.com/NVIDIA/TensorRT-LLM/releases/tag/v1.4.0rc2) — NVIDIA/TensorRT-LLM v1.4.0rc2 发布；Python wheel 使用 1.4.0rc2.post1，修复阻碍 PyPI 发布的 Git 依赖并更新 Boost 镜像，同时扩展 Rubin、NVFP4、Cosmos3、MiniMax、Qwen 等模型和服务能力。
- [v0.8.0](https://github.com/ggml-org/llama.cpp/releases/tag/v0.8.0) — ggml-org/llama.cpp v0.8.0 发布：加入 LiquidAI LFM3 文本、视觉、音频和全模态模型，新增实时音频及 /v1/realtime、/tts 服务端点，并扩展多种模型架构、工具调用和后端优化。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
