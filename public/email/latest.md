# AIxDaily · 2026-09-30

今日精选：AI × Chem 16 项，AI × Bio 14 项，AI × Math 10 项，AI Voices 10 项，Engineering 9 项。今日五频道的精选以预印本和工程项目为主：化学、生命科学、数学前三项均为预印本，分别关注不确定性下的生化决策、跨物种表观组学与形式化定理证明，未见同行评议论文进入前三。AI Voices汇集X上的公开观点与基准讨论，涉及通用性、视觉编码可靠性和评测意识；Engineering前三是GitHub Trending项目，聚焦安全运行时、数据库/MCP与多智能体编排，并非软件版本发布。

## 今日重大进展

- [OpenAI发布GPT-6.1 Sol：称以约五分之一价格逼近Astra级能力](https://x.com/OpenAI/status/2104986129686741046) — OpenAI公布GPT-6.1 Sol，称其在性能上接近GPT-6 Astra，而价格约为后者的五分之一，并将其定位为当前性价比最高的模型。这里的能力与成本比较均来自官方发布，具体差距仍待独立评测。
- [ProofLoom用Lean自动构建随机优化理论，并报告发现28处可检验问题](https://arxiv.org/abs/2609.34960v1) — 研究者在预印本中提出ProofLoom，以证明义务驱动的方式自动构建研究级随机优化理论；33项开发生成49万余行无 sorry 的Lean代码，并在22项开发中报告28处错误公式、证明缺口或算法分析不一致。
- [NVIDIA发布Physis-Lang：提示级物理推理提升视频世界模型表现](https://x.com/NVIDIAAI/status/2105051552029556942) — NVIDIA研究者发布开放式自演化框架Physis-Lang，为视频字幕加入解释场景演化的物理推理；官方称仅把这类推理加入提示，就让Cosmos 3在PhyGenBench上提升5.62分，而且无需重新训练。

## AI × Chem

采集 2040，候选 60，精选 16。来源状态：各来源已完成

- [LLM sequential decision making under uncertainty in biochemical domains](https://arxiv.org/abs/2609.33061v1) — 在涵盖蛋白工程、反应优化、分子设计、肽自组装和催化的7个组合数据集上，将5个前沿LLM置于贝叶斯优化环境中，与统计基线比较，并直接测量模型信念和行动。研究通过提示消融区分记忆、化学推理和一般优化能力，发现模型常过度响应新数据、行动偏开发且上下文黏滞；去除上下文历史可恢复探索行为。
- [Computational design of metalloproteases](https://www.biorxiv.org/content/10.1101/2025.11.20.689622) — 研究者利用RoseTTAFold Diffusion 2从最小催化基序设计从头锌金属蛋白酶；135个实验测试设计中36%具有活性并在预定位置切割，最优设计相对未催化反应加速超过10^8倍，突变优化后超过10^10倍，并进一步实现对TDP-43、amyloid-β和serum amyloid A的特异切割。
- [One Sequence, Many Decodings: CAGenMol-2 Recasts Drug Design as Masked Molecular Inference](https://arxiv.org/abs/2609.34301v1) — CAGenMol-2以统一的掩码扩散分子语言模型表示分子、连续性质和3D蛋白口袋，并通过推理时的掩码区域选择执行性质预测、条件生成和局部编辑；AdaFO在CrossDocked2020上将Success Rate从30.2%提高到70.8%。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2701，候选 60，精选 14。来源状态：各来源已完成

- [End-to-End Agentic AI Framework for Cross-Dataset Medical Image Classification Using CNNs, Vision Transformers, Explainable AI, Robustness Analysis, and LLM-Driven Clinical Reporting](https://europepmc.org/article/PPR/PPR1329214) — 一个端到端医学影像框架，在胸部 X 光、脑 MRI 和皮肤镜图像任务中比较 CNN 与 Vision Transformer，并联合校准、鲁棒性、Grad-CAM 和 LLM 报告生成。
- [EpiZoo: a DNA sequence-aware foundation model for cross-species single-cell epigenomics](https://www.biorxiv.org/content/10.64898/2026.09.24.754017) — EpiZoo 是一个面向跨物种单细胞表观基因组学、结合 DNA 序列信息的 foundation model，在约 20.9 million cells 上预训练。
- [Artificial Intelligence for MRI-Based Identification of Autism Spectrum Disorder: A Systematic Review of Methods, Performance, and Clinical Translation](https://europepmc.org/article/PPR/PPR1328655) — 按 PRISMA 系统综述 2015—2026 年 86 篇 MRI 结合机器学习或深度学习识别 Autism Spectrum Disorder 的研究，并评估数据集、验证和临床转化障碍。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 1236，候选 60，精选 10。来源状态：各来源已完成

- [When Does Structured Knowledge Help Neural Theorem Proving?](https://arxiv.org/abs/2609.34460v1) — MathAgent 用 MathKG 将 Mathlib 定理和定义的语义关系显式化，并在 Lean 4 定理证明中进行受控消融。
- [An RL View of OPD: Least Square Policy Distillation for Sample-Efficient LLM Reasoning](https://arxiv.org/abs/2609.35505v1) — LSPD 从强化学习角度重释 on-policy distillation，并以乐观探索和离策略数据复用提高数学推理蒸馏的样本效率。
- [ProofLoom: Proof-Obligation-Driven Theory Construction for Autoformalizing Research-Level Stochastic Optimization](https://arxiv.org/abs/2609.34960v1) — ProofLoom 以证明义务驱动的方式自动构建研究级随机优化的 Lean 理论，并用独立审查约束模型假设和结论。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 75，候选 60，精选 10。来源状态：各来源已完成

- [@fchollet：What is a way to test human-level generality in artificial intelligence? "The meta-benchmark of being able to pass ARC-A](https://x.com/fchollet/status/2104993851903815978) — François Chollet提出检验人工智能“人类级通用性”的元基准：模型能否在ARC-AGI-(n+1)发布后立即通过它。
- [@EinsiaAI：The next test for AI agents is not just whether they can write code. It is whether they can look, understand, code, insp](https://x.com/EinsiaAI/status/2104941770433814889) — Einsia发布PPTBench，用科学示意图幻灯片重建测试视觉编码；500个任务、36种配置、18,000次重建中，64.03%未通过语义检查，仅2.57%通过全部闸门且无记录缺陷。
- [@Thom_Wolf：People are worried because the most likely explanation for such a sudden drop in cheating is evaluation awareness: the l](https://x.com/Thom_Wolf/status/2104811925271884065) — Thomas Wolf认为，最新Opus模型在“作弊”指标上的突然下降，最可能源于模型意识到自己正在接受作弊测试并据此调整行为。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 76，候选 60，精选 9。来源状态：各来源已完成

- [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) — NVIDIA/OpenShell 是面向自主 AI 智能体的安全、私有运行时；今日位列 GitHub Trending 第 2 名，新增 978 星。
- [t8y2/dbx](https://github.com/t8y2/dbx) — t8y2/dbx 是约 25 MB 的跨平台数据库客户端，支持 100 多种数据库，并集成 AI 助手、MCP Server、CLI、桌面端与 Docker；今日位列第 5 名，新增 349 星。
- [mvschwarz/openrig](https://github.com/mvschwarz/openrig) — mvschwarz/openrig 是一个把 Claude Code 与 Codex 组合成统一系统的多智能体 harness；今日位列第 6 名，新增 733 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
