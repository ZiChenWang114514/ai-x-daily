# AIxDaily · 2026-09-12

今日精选以预印本和工程更新为主：化学方向出现把语言表征接入反应优化闭环的前瞻性实验报告；生物方向集中于阿尔茨海默病遗传与多组学关联；数学方向评估拓扑推理与 Lean 验证。声音频道兼有公开观点和厂商技术更新，工程频道则聚焦开源研究智能体与规格驱动开发工具。上述预印本及厂商表述尚待独立复核。

## 今日重大进展

- [OpenAI/Navier–Stokes 研究引发数学界集中讨论](https://x.com/zjasper/status/2097547276755619988) — 数学研究者 Jasper 在 X 上称，OpenAI 围绕 Navier–Stokes 千禧年难题的工作“具有历史性”；帖文称相关研究路线已积累多年，并讨论大规模智能体沿既有方向并行探索的可能。
- [Magenta 把数学推理接入 Lean 机器验证闭环](https://arxiv.org/abs/2609.11319v1) — 预印本提出 Magenta：将自然语言解题转为 Lean 4 陈述和机器检查证明，并用陈述核验与错误归因反馈修正失败尝试；作者报告其在多项奥赛基准达到 100% 准确率，并解出 IMO 2026 全部六题。
- [OpenAI 发布面向长时运行的 Agents API](https://openai.com/index/introducing-the-agents-api) — OpenAI 发布 Agents API，提供由 Codex harness 驱动的托管云端智能体服务，覆盖编排、长时运行会话和工具使用，面向构建并上线持续运行的智能体应用。

## AI × Chem

采集 1453，候选 60，精选 15。来源状态：各来源已完成

- [Dynamic language model representations for multi-objective reaction optimisation](https://arxiv.org/abs/2609.11790v1) — 该研究将反应条件的文本描述经微调语言模型编码，并与高斯过程代理模型联合训练，用于多目标贝叶斯反应优化。在镍、钯交叉偶联及前瞻性钯催化氰化和不对称氢化中，模型以更少实验收敛；两轮高通量实验后，条件可直接放大至克级，并分别得到 94% 和 84% 收率，后者 ee 为 99.6%。
- [Reframing enzyme function prediction as conditional generation](https://www.biorxiv.org/content/10.64898/2026.09.09.750355) — Fluxion 将酶功能预测重构为条件生成任务：结合蛋白语言模型表征、合成化学和生化数据，生成催化残基间的多步电子流轨迹。模型在 P450 区域选择性、两个实验特异性数据集及非天然定向进化筛选产物上进行了评估。
- [IntelliPore: A Foundation Model for Gas Adsorption in Porous Materials](https://doi.org/10.26434/chemrxiv.15008693/v1) — IntelliPore 是面向多孔材料气体吸附的基础模型，在 1,250 万条公开 MOF 和 COF 吸附数据上预训练，并报告可迁移到沸石和多孔聚合物网络等未见材料类别。作者称其以 0.86 million 参数实现较强的小样本性能和吸附性质预测表现。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2307，候选 60，精选 12。来源状态：各来源已完成

- [Sex-aware Cross-tissue Regulatory Transformer Identified Sexually Dimorphic Alzheimer's Disease Risk Loci and Causal Cellular Circuit](https://europepmc.org/article/PPR/PPR1316932) — 阿尔茨海默病（AD）遗传效应和调控背景中的性别差异仍未完全阐明。我们采用按性别分层及基因型×性别模型分析了 449,335 名欧洲祖源参与者，并开发了 STAGE-AD——一个整合分子 QTL、表观基因组及单细胞注释的 Transformer。按性别分层的分析识别出 8 个女性和 3 个男性全基因组显著信号，暂定为新信号。主测试集的精确率-召回率曲线下面积为 0.895（95% 置信区间，0.877–0.912）；在位点留出和 APOE 区域留出条件下，分别降至 0.751 和 0.681。独立的 HUNT 和 MVP 队列中的统计遗传学整合支持 106 个位点的 236 个基因。预先设定的终生风险假设得到女性和男性的责任度量表 SNP 遗传力分别为 11.42% 和 9.23%。消融分析表明，女性偏向预测依赖于胶质细胞注释，男性偏向预测依赖于内皮细胞和少突胶质细胞注释。利用来自 579 名 NPAD 脑供体的多组学和神经病理学数据，评估了 11 条候选的变异—基因—组织—细胞—病理链条。这些发现强调，在包括阿尔茨海默病在内的健康状况研究中应考虑性别特异性遗传结构，并为更具针对性的治疗策略铺路。
- [Genetic risk implicating endolysosomal network genes correlates with endolysosomal dysfunction across neural cell types in Alzheimer's disease](https://www.biorxiv.org/content/10.1101/2025.03.16.643481) — 迟发性阿尔茨海默病（LOAD）具有复杂的基因组结构。LOAD 风险变异提示，包括内溶酶体网络（ELN）在内的多条通路参与阿尔茨海默病（AD）的病理生物学。特定通路中的遗传风险是否与相应的生物学功能障碍相关，仍基本未知。我们使用 14 个涉及 ELN 基因、已充分确立的 AD 风险等位基因，开发了内溶酶体通路特异性多基因风险评分（ePRS）。我们研究 ePRS 与 AD 神经病理之间的关联，随后在按 ePRS 负担分层的死后背外侧前额叶皮层供体样本中，考察细胞特异性的内溶酶体形态和转录组特征。我们发现，尽管 ePRS 代表的位点少得多，但其与 AD 诊断和神经病理学指标显著相关，表现可与非通路特异性 PRS 相当。高 ePRS 与神经元内体体积、数量和核周聚集增加相关，且独立于 AD 病理。单核 RNA 测序显示，与 ePRS 状态相关的细胞类型特异性转录组变化影响谷氨酸能信号、蛋白质稳态、DNA 损伤反应和免疫功能。神经元、星形胶质细胞、少突胶质细胞和小胶质细胞均显示与 ePRS 负担相关的不同基因表达模式。总体而言，这些结果提供证据表明，含有 ELN 基因的 AD 遗传风险变异与人脑组织中的内溶酶体功能障碍相关。这些发现提示，通路特异性遗传风险有助于 AD 中相应的细胞病理，并提出 ELN AD 变异参与发病机制的候选机制。
- [LiverDCP: A Disease-Cell-Protein Framework for Multi-scale Modeling of Disease Biology](https://www.biorxiv.org/content/10.64898/2026.08.07.743628) — 理解分子相互作用如何在细胞环境中产生疾病表型，是生物医学研究的核心挑战。本文提出疾病—细胞—蛋白质（DCP）范式，用于多尺度疾病生物学建模；该范式在统一图架构中共同表示疾病状态、细胞组成和蛋白质相互作用网络。我们在肝脏中以 LiverDCP 实现该范式：整合肝病的协调化单细胞图谱 LiverHomo 与蛋白质组范围预测的蛋白质—蛋白质相互作用，构建了跨多种肝病和细胞条件的 280 多个环境特异性互作组。LiverDCP 采用多环境表征学习策略，可跨数百个疾病—细胞环境联合训练，在保留环境特异性变化的同时捕捉共享相互作用原理。LiverDCP 通过几何感知的两阶段训练方案整合预训练的蛋白质序列衍生特征，该方案在提升预测性能的同时保留嵌入结构。所得 DCP 蛋白质嵌入揭示了跨疾病的蛋白质功能状态广泛重连，并为下游生物医学应用提供可迁移表征。在表征学习过程中不使用 GWAS 监督的条件下，LiverDCP 可进行疾病风险基因分类，并识别遗传风险可能发挥作用的细胞类型。对于治疗靶点发现，LiverDCP 回收了已确立的 II 期及以上 MASH 靶点，并从未注释蛋白质组中优先筛选出此前未被识别的候选者；前 50 个预测中有 26 个显示与 MASH 生物学相关的独立 PubMed 证据。环境特异性相互作用分析还为表征较少的候选者提供机制假设。总体而言，DCP 构建了一个可泛化框架，用于跨复杂疾病连接分子相互作用、细胞环境、遗传风险和治疗机会。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 618，候选 60，精选 7。来源状态：各来源已完成

- [MindTopo: Can Foundation Models Reason in Topological Space?](https://arxiv.org/abs/2609.11900v1) — MindTopo以拓扑不变量为核心，评估多模态模型在拓扑关系识别、变化推断及闭环规划中的表现。
- [Magenta: Closing the Loop Between Mathematical Reasoning and Lean Verification](https://arxiv.org/abs/2609.11319v1) — Magenta将自然语言解题、Lean 4 陈述生成和机器检查证明串联，并以陈述核验和错误归因反馈处理失败尝试。
- [Can LLMs Follow Medical Expert Logic? A Benchmark for Hierarchical Logical Consistency in Risk-of-Bias Assessment](https://arxiv.org/abs/2609.11185v1) — LogiMed-RoB以 Cochrane RoB 2.0 专家逻辑为基础，分层测量模型在偏倚风险评估中的逻辑一致性与证据忠实性。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 66，候选 60，精选 5。来源状态：各来源已完成

- [@omarsar0：Another banger paper from Google. If you build memory for long-horizon agents, this one is worth your time. Agents usual](https://x.com/omarsar0/status/2097755424007373270) — 原帖介绍一篇关于长时程智能体记忆的 Google 论文：其将程序性知识表示为“程序—关系—程序”三元组，以区别于存储事实的知识图谱。帖文未附论文链接，具体方法与实验仍无法由候选文本核查。
- [CUDA Toolkit 13.4 Adds Windows on Arm Support and Greater Control over Shared GPUs](https://developer.nvidia.com/blog/cuda-toolkit-13-4-adds-windows-on-arm-support-and-greater-control-over-shared-gpus/) — NVIDIA 官方技术博客发布 CUDA Toolkit 13.4，标题明确列出新增 Windows on Arm 支持及更强的共享 GPU 控制。
- [How Full-Stack NIM Optimizations Deliver 2.5x More Users on Nemotron 3 Ultra](https://developer.nvidia.com/blog/how-full-stack-nim-optimizations-deliver-2-5x-more-users-on-nemotron-3-ultra/) — NVIDIA 官方技术博客介绍面向 Nemotron 3 Ultra 的全栈 NIM 优化；标题称这些优化可承载 2.5 倍更多用户。该倍数是发布方在其工程配置下的陈述。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 77，候选 60，精选 7。来源状态：各来源已完成

- [alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch) — alphaXiv/OpenResearch 位列当日 GitHub Trending 第 14 名，新增 156 星；它让用户使用任意模型并行运行研究智能体。
- [github/spec-kit](https://github.com/github/spec-kit) — github/spec-kit 位列当日 GitHub Trending 第 15 名，新增 985 星；它提供规格驱动开发的起步工具包，面向结合 AI/Copilot 的需求与工程流程。
- [melgarafael/DeskcommCRM](https://github.com/melgarafael/DeskcommCRM) — melgarafael/DeskcommCRM 位列当日 GitHub Trending 第 4 名，新增 126 星；这是带原生 AI 智能体和 WhatsApp 接入的自托管 CRM，并支持 MCP、多租户与 RAG。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
