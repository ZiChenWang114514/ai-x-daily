# AIxDaily · 2026-10-14

今日精选：AI × Chem 14 项，AI × Bio 16 项，AI × Math 0 项，AI Voices 10 项，Engineering 6 项。今日五频道呈现“科研预印本+工程项目+公开观点”的组合：AI×化学聚焦带校准不确定性的分子性质预测、对映选择性人工金属酶及计算药物发现综述；AI×生物覆盖低样本临床预测、帕金森生物标志物和百日咳监测。化学与生物精选均为预印本，今日没有同行评议论文入选。AI Voices 汇集 X 上的基准、模型架构和教材线索，属于公开帖文；Engineering 则是 GitHub Trending 软件项目。AI×数学今日没有足够高质量更新。

## 今日重大进展

- [Anthropic公布自研源代码管理系统，五个月把单体仓库迁离 Git](https://x.com/AnthropicAI/status/2110047081414987957) — Anthropic工程博客公布自研源代码管理系统：随着代码合并量从5月日均约2500次增至9月逾3万次，公司称面向人类的开发基础设施成为瓶颈，并在五个月内完成单体仓库迁移。
- [Gemini 4 Argon据称仅凭视频教会人形机器人连续投中7次](https://x.com/GoogleDeepMind/status/2110078384617464201) — Google DeepMind称，Gemini 4 Argon仅观察一段视频，便完成物理映射、编写仿真，并指导Apptronik Apollo人形机器人连续7次投中玉米洞。
- [Pushmeet Kohli称 Argon 找到 Grad 猜想更多反例](https://x.com/pushmeet/status/2110049810342609120) — Google DeepMind负责人 Pushmeet Kohli在公开帖文中称，Argon发现核聚变等离子体中Grad猜想的更多反例，并得到恒星器三维磁场的新解析解，用于改进设计代码验证。

## AI × Chem

采集 841，候选 60，精选 14。来源状态：各来源已完成

- [Molecular Property Prediction with Well-Calibrated Uncertainties via Graph Neural Networks and Conformal Quantile Regression](https://doi.org/10.26434/chemrxiv.15010324/v1) — 将保序分位数回归（CQR）与图神经网络结合，用于分子性质预测和校准预测不确定性；在量子力学、物理化学和药代动力学数据集上与多种不确定性方法比较，并在抗生素回顾性虚拟筛选中取得超过 90% 的命中率。
- [De Novo Design of Enantioselective Artificial Metalloenzyme Photocatalysts Containing Metal Polypyridine Cofactors](https://doi.org/10.26434/chemrxiv.15002852/v3) — 利用生成式蛋白质设计从头构建人工金属酶支架，使金属多吡啶光催化辅因子实现对映选择性光催化；瞬态吸收表征将催化提升归因于辅因子量子产率和激发态寿命增加以及活性位点近端底物结合。
- [Computationally Guided Discovery of Cannabinoid Derivatives for Antiviral and Anticancer Applications: From Chemical Space to Experimental Validation](https://doi.org/10.26434/chemrxiv.15008399/v2) — 综述以大麻素衍生物为对象的计算药物发现流程，整合化学空间生成、靶点识别、虚拟筛选、分子对接、分子动力学、自由能、量子化学、QSAR、AI/ML 和 ADMET，并强调生化、细胞及动物验证的闭环。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1123，候选 60，精选 16。来源状态：各来源已完成

- [Can GPT Be Used as an Alternative Prediction Model to Traditional Machine Learning and Neural Networks on Low-Volume Clinical Data?](https://www.medrxiv.org/content/10.64898/2026.08.19.26360765) — 预印本；提出将结构化临床记录转写为医生风格文本，并用 GPT4 生成医学释义后微调 GPT2，在四个低样本、类别不平衡的疾病数据集上进行疾病预测。
- [Application of Bayesian-Derived Gene Interaction Network and Subnetwork for Classification of Idiopathic Parkinson Disease with Biomarkers](https://www.biorxiv.org/content/10.64898/2026.10.05.756343) — 预印本；在 PPMI 队列血液转录组上用 Bayesian gene interaction network 进行信号扩散，并结合临床特征和 random forest 筛选 13 个 Parkinson Disease 生物标志物基因。
- [Enhancing molecular and genomic approaches for Bordetella pertussis investigation and public health surveillance in Victoria, Australia](https://www.medrxiv.org/content/10.64898/2026.10.11.26364704) — 预印本；在 Victoria, Australia 的 2024–2025 百日咳疫情期间评估 culture-independent PCR、amplicon sequencing、耐药筛查和 shotgun metagenomics 的公共卫生监测可行性。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 0，候选 0，精选 0。来源状态：各来源已完成

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 71，候选 60，精选 10。来源状态：各来源已完成

- [@induction_labs：Human researchers decide everything from compute and data spend to what experiments to run. To replace them, models need](https://x.com/induction_labs/status/2110059300651679969) — Induction Labs宣布推出 FrontierML 基准，评估智能体如何分配计算与数据预算，并在21项端到端机器学习任务上提升模型性能。事实来自帖文；其对“替代人类研究者所需判断力”的表述属于作者设定。编辑判断：该基准直接测量智能体的科研资源配置能力。
- [@neal_k_patel：You already gave the LLM the answer. So why is it writing it out from scratch? Introducing a new AI model architecture: ](https://x.com/neal_k_patel/status/2109978626124898587) — Neal Patel介绍受约束解码模型（CDM）：针对单一任务读取一次输入并直接输出答案，跳过逐词生成循环。帖子强调其速度、一致性和成本优势；具体性能数据尚未提供。
- [@Gorden_Sun：谁把教材上传Arxiv了？ 《Agentic Large Language Models》（智能体大语言模型）：来自荷兰莱顿大学的AI教材，内容涵盖大模型工作原理、Agent原理等相关AI内容，共472页。 地址：https://arxiv](https://x.com/Gorden_Sun/status/2109937184900063249) — Gorden Sun分享荷兰莱顿大学的《Agentic Large Language Models》教材，称其涵盖大模型和智能体原理，共472页。事实限于帖文所述书目信息。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 56，候选 55，精选 6。来源状态：各来源已完成

- [morluto/rea](https://github.com/morluto/rea) — GitHub Trending 当日第 1 名，新增 54,706 颗星。rea 用智能体辅助从应用行为一直逆向到原生二进制，整合反编译、静态分析、MCP 与命令行工作流。
- [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) — GitHub Trending 当日第 2 名，新增 1,961 颗星。项目在浏览器中以真实数据驱动的 3D 地球呈现航班、卫星和空间情报信息。
- [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) — GitHub Trending 当日第 3 名，新增 2,277 颗星。VoiceStudio 是完全本地运行的语音工作台，覆盖声音克隆、语音设计、视频配音、听写、转录和有声书制作，支持 646 种语言。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
