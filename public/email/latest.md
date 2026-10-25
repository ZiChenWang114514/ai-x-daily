# AIxDaily · 2026-10-26

今日精选：AI × Chem 4 项，AI × Bio 13 项，AI × Math 2 项，AI Voices 9 项，Engineering 2 项。今日五频道共呈现两类主线：研究侧精选均为预印本，涵盖脑类器官中的西尼罗病毒代谢靶点、有机磷化合物代谢、跨生物情境扰动签名、RNA 相分离序列特征及跨模型表示几何；应用评测关注饮食图像和医学考试中的多模态可靠性。AI Voices 是 X 公开观点，Engineering 是 GitHub Trending 软件项目动态；未见同行评议论文或明确的新版本发布。

## 今日重大进展

- [Omega Desci 公布 Lean 4 机检解决55个开放问题，量子信息猜想获形式化定理](https://x.com/OmegaDesci/status/2113301987873919473) — Omega Desci 在公开帖文中报告，团队于10月22日解决文献中的55个开放问题，覆盖量子信息、图论、特殊函数和整数序列；其中包括 Chitambar 等人2021年猜想，并全部用 Lean 4 机器检查。
- [Claude 为逾百个开源库生成 RISC-V 汇编级安全证明，LLM 形式化验证迈向规模化](https://x.com/__alpoge__/status/2113410635673550975) — 合作方在 X 上报告，与 Theorem 合作后，Claude 已为100多个真实开源软件库生成 RISC-V 汇编级安全属性的形式化证明，目标是把可证明安全保证纳入日常软件开发流程。
- [ARC Institute 用单细胞基因组潜在空间寻找功能性 RNA，AI 开始扫描生命“暗空间”](https://x.com/patrickc/status/2113432794571641156) — Patrick Collison 转发 ARC Institute 的研究动态：团队利用单细胞生命基因组的潜在空间表示，结合深度学习与可解释性寻找新的功能性 RNA 候选，并探索智能体加速组合搜索。

## AI × Chem

采集 1320，候选 60，精选 4。来源状态：各来源已完成

- [Single-cell analysis of West Nile virus infection in brain organoids identified a serine synthesis enzyme as a determinant of viral neural tropism and a druggable antiviral target](https://www.biorxiv.org/content/10.64898/2026.10.23.761475) — 研究建立人脑类器官中的西尼罗病毒（WNV）感染模型，并用病毒纳入式单细胞 RNA 测序解析细胞嗜性与宿主反应；结果锁定 PHGDH 介导的丝氨酸合成依赖，并通过 RNA 干扰、药理抑制和 FDA 批准药物 disulfiram 验证其抗病毒潜力。
- [Human CYP1A2 metabolism of organophosphorus pesticides and nerve agent surrogates](https://www.biorxiv.org/content/10.64898/2026.10.20.760143) — 用 LC-MS/MS 测定 CYP1A2 对有机磷化合物的降解能力，并结合 pFluor50 抑制实验和基于 CYP1A2 晶体结构 PDB ID: 2HI4 的分子对接，比较 thion 与 oxon 代谢及抑制关系。
- [Sequence architecture of RNA reveals key molecular signatures driving RNA phase separation](https://www.biorxiv.org/content/10.64898/2026.10.23.761066) — 提出可解释的混合机器学习框架，用 167 个人工设计序列描述符与 RNA-FM 的 640 维上下文嵌入，通过交叉验证 stacking 识别与液-液相分离（LLPS）相关的 RNA，并用特征消融、SHAP 和 MALAT1、TMPO-AS1 案例分析提出机制线索。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1890，候选 60，精选 13。来源状态：各来源已完成

- [Signature Recontextualization: Mapping perturbational signatures across biological contexts](https://www.biorxiv.org/content/10.64898/2026.08.14.744937) — 提出跨生物学情境预测扰动转录签名的统一基准，在细胞系和大鼠组织数据上比较 projectCor、netProp、scGPT、STACK 及统计基线。
- [Image-Based Dietary Assessment Using Multimodal Large Language Models: Performance, Limitations, and Clinical Applicability in Diabetes](https://europepmc.org/article/PPR/PPR1349416) — SeeFood 基准在真实饮食照片上评估8个多模态大模型，并扩展到1680张照片和275个参与者日。
- [Re-evaluating the benefit of training scale in cell foundation models](https://www.biorxiv.org/content/10.64898/2026.06.04.730272) — 比较不同预训练语料规模下的一、二代单细胞基础模型，指出冻结表示评估比常规微调更能显现规模效应。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 358，候选 60，精选 2。来源状态：各来源已完成

- [The Geometry of Meaning in Neural Manifolds](https://arxiv.org/abs/2610.30938v1) — 以语义对应为核心，研究如何在不同架构、随机初始化和优化轨迹造成的非兼容参数坐标下，对齐独立训练模型的表示；论文汇总了覆盖视觉、语言、强化学习和神经科学等领域的 14 项对应驱动方法。
- [Would an LLM Match into a Residency? Uncertainty, Reasoning and Image Use of Open Language Models on the Spanish MIR Examination](https://arxiv.org/abs/2610.31586v1) — 在西班牙 MIR 住院医师考试的 1,552 道题上评估 4 个 8B 至 27B 参数开放模型，除准确率外还检验置信度校准、临床推理可靠性和图像使用情况。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 64，候选 49，精选 9。来源状态：各来源已完成

- [@adxtyahq：Today, I'm launching https://llmdojo.dev - The hands-on way to learn AI engineering: LLMs, RAG, agents, evals and infere](https://x.com/adxtyahq/status/2114000416245703087) — Aditya 宣布上线 LLMDojo，用交互式实验教授 LLM、RAG、智能体、评测和推理，并支持在浏览器中调整分词器、注意力、嵌入与 KV 缓存、训练神经网络。
- [@patrickc：New from @arcinstitute: using the latent space representation of genomes from single-cell life to find new candidate fun](https://x.com/patrickc/status/2113432794571641156) — Patrick Collison 转发 ARC Institute 的工作：利用单细胞生命基因组的潜在空间表示寻找新的功能性 RNA 候选。
- [@chelseabfinn：Generative value classifiers are a new parametrization of Q-functions that don't require action conditioning. We think t](https://x.com/chelseabfinn/status/2114117117813706782) — Chelsea Finn 介绍 Generative Value Classifiers：一种不需要动作条件输入的 Q 函数新参数化，并给出论文链接。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 62，候选 53，精选 2。来源状态：各来源已完成

- [JetBrains/thinkrail](https://github.com/JetBrains/thinkrail) — JetBrains/thinkrail 在当日 GitHub Trending 排名第 8，新增 52 星。它把 pi agent 接入轻量级 IDE，并按个人工作方式定制智能体工作流，面向希望将规范驱动开发与 AI 编程结合起来的开发者。
- [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) — AgriciDaniel/claude-seo 在当日 GitHub Trending 排名第 11，新增 179 星。它为 Claude Code 提供通用 SEO 技能，拆分为 26 个子技能和 19 个子智能体，覆盖技术 SEO、结构化数据、GEO/AEO、Agent readiness、链接、跨地区站点和报告生成。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
