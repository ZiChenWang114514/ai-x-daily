# AIxDaily · 2026-09-03

今日精选：AI × Chem 14 项，AI × Bio 15 项，AI × Math 13 项，AI Voices 7 项，Engineering 4 项。今日更新以预印本和软件发布为主。化学与生物频道分别聚焦材料传感、腐蚀推理、计算病理和单细胞模型评估；数学频道关注空间推理与形式验证。所列研究均为预印本，未见同行评议论文；观点频道收录公开帖文，其中性能结论仍属发布方表述。工程侧则有 PyTorch 2.14.0 正式发布及两项热门开源工具。

## 今日重大进展

- [Google DeepMind 发布 Gemini 3.8 Flash 系列，瞄准智能体与代码安全](https://x.com/GoogleDeepMind/status/2095175498967949359) — Google DeepMind 官方公布 Gemini 3.8 Flash 与 3.8 Flash Cyber：前者面向软件工程、智能体任务和多步推理，后者用于漏洞检测及自动修补；发布方称前者较 3.7 Flash 有显著提升。
- [Lanyon 公布可形式化验证的理想磁流体动力学求解器](https://x.com/lanyon_ai/status/2094449821734060051) — Lanyon AI 公布，其系统约 7 分钟生成理想磁流体动力学求解器、约 3.2 万行 C 代码、5 万行 Lean 证明及约 150 项正确性定理，并完成磁散度校正和等离子流模拟验证。

## AI × Chem

采集 1654，候选 60，精选 14。来源状态：各来源已完成

- [Functional Biomaterials, Spatial Biosensing, and Artificial Intelligence](https://doi.org/10.26434/chemrxiv.15008031/v1) — 综述功能性生物材料、空间生物传感与 AI 的结合，讨论响应性水凝胶、nanozymes、MOFs、导电支架及器官芯片传感如何产生多模态细胞微环境数据，并用于材料优化、无标记光谱指纹和空间解卷积。
- [Generative artificial intelligence for reliable mechanistic reasoning for corrosion](https://arxiv.org/abs/2609.00099v1) — 构建面向镁合金腐蚀知识综合的领域 RAG 框架：以 840 篇同行评议论文中的 3,309 组专家核验问答微调 Llama-3.1-8B、Qwen-2.5-7B 和 Mistral-7B，并以 Reason Map 识别因果方向颠倒及缺乏证据支持的推断。
- [MolLedger: An Additive Graph Neural Network with Chemically Grounded ADME Attributions](https://arxiv.org/abs/2608.30636v1) — 提出 MolLedger 加性图神经网络，将 ADME 预测写为逐原子得分之和，并以辅助损失将原子贡献与化学性质关联，从模型结构中提供可解释的原子级归因。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2529，候选 60，精选 15。来源状态：各来源已完成

- [BanffNET, a Deep Learning System for Comprehensive Histological Lesion Quantification in Kidney Transplant Biopsies](https://www.medrxiv.org/content/10.64898/2026.08.28.26360029) — BanffNET在7,249张训练全切片图像上学习肾移植活检病变的连续量化，并在5个外部测试集、11,028张图像上评估；其评分与排斥反应分子谱的吻合度高于病理医师Banff评分。
- [A lipid-laden macrophage niche drives immunosuppression in primary central nervous system lymphoma](https://www.biorxiv.org/content/10.64898/2026.02.19.705289) — 研究以空间转录组、单细胞RNA测序、空间蛋白组和免疫完整小鼠模型，描述PCNSL中TREM2/GPNMB阳性脂质负荷巨噬细胞及其与Treg形成的免疫抑制微环境。
- [Accessible and reproducible deployment reveals the practical boundaries of single-cell foundation models](https://www.biorxiv.org/content/10.64898/2026.01.06.698060) — 统一的可重复部署框架比较13个单细胞基础模型与既有方法，覆盖近100个数据集，发现其优势主要出现在极低监督、罕见细胞标注和开放集细胞状态检测等任务。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 871，候选 60，精选 13。来源状态：各来源已完成

- [Autoregressive Mosaics: Probing 2D Spatial Reasoning in Text-Only Language Models](https://arxiv.org/abs/2608.30751v2) — AM-Bench 将“按完整几何描述生成代码”与“由不充分提示完成布局”分开评测，发现文本与代码模型在前一任务上较稳定，开放式二维布局能力却差异显著；以 SVG 代替过程式代码还能普遍提高布局分数。
- [LCoT-GV: Graph Attention Networks for Verifying Long Reasoning Chains in Large Language Models](https://arxiv.org/abs/2608.30679v1) — LCoT-GV 将长思维链表示为含推理步骤及语义、逻辑关系的图，再以图注意力网络预测思维链正确性，并构建了来自多个推理问答基准的图式验证数据集。
- [SOVER: Formal Certification of Optimization Reformulations via LLM-Assisted SMT Verification](https://arxiv.org/abs/2609.00728v1) — SOVER 用 LLM 提取变量映射，再分别以 Z3 和 dReal 对混合整数线性与连续非线性优化重构进行 SMT 认证；在 NLEquiv-150 的 150 对非线性重构上报告 149 对分类正确。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 122，候选 60，精选 7。来源状态：各来源已完成

- [@InSilicoMeds：🚀 5 new drug-discovery specialist LLMs. SOTA-level performance across 70+ benchmark tasks. Insilico Medicine has release](https://x.com/InSilicoMeds/status/2095139173644857621) — Insilico Medicine 的官方帖文宣布发布 5 个药物发现专用语言模型，称其由 MMAI Gym 训练，覆盖药物安全性、效力预测、化学合成与生物学，并在 70 多项基准任务中达到领先水平。
- [@GoogleDeepMind：Two new Gemini models are here to help scale your AI agents and secure code: 🔘 3.8 Flash: our most intelligent model yet](https://x.com/GoogleDeepMind/status/2095175498967949359) — Google DeepMind 官方帖文发布 Gemini 3.8 Flash 与 Gemini 3.8 Flash Cyber，并称前者在软件工程、智能体任务和多步推理上较 3.7 Flash 有明显提升，后者面向漏洞检测和自动修补。
- [@rohanpaul_ai：New HuggingFace paper argues that increasing agent autonomy can gradually make human oversight ineffective by causing ap](https://x.com/rohanpaul_ai/status/2094628310877913101) — Rohan Paul 转述一篇题为《AI Agents Push Humans Out of the Loop》的论文：随着智能体承担更多工作，批准疲劳、过度依赖、情境感知减弱和技能退化可能削弱人工监督的可靠性。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 67，候选 60，精选 4。来源状态：各来源已完成

- [PyTorch 2.14.0 Release](https://github.com/pytorch/pytorch/releases/tag/v2.14.0) — pytorch/pytorch 发布 PyTorch 2.14.0：Inductor 增加 NVGEMM、动态形状声明与实验性复数张量编译支持，分布式通信、Apple Silicon 线性代数及多硬件平台支持同步更新；多个旧 API 与既有梯度语义发生兼容性变化。
- [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) — debpalash/VoiceStudio 是本地优先的开源语音工作台，提供语音克隆、语音设计、视频配音、听写、转录和有声书制作；当天位列 GitHub Trending 第 4 名，新增 834 星标。
- [pacifio/atlas](https://github.com/pacifio/atlas) — pacifio/atlas 为多个编程智能体提供源码管理、改动追踪与统一查询能力；当天位列 GitHub Trending 第 9 名，新增 895 星标。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
