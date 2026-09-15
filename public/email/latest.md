# AIxDaily · 2026-09-15

今日精选：AI × Chem 6 项，AI × Bio 8 项，AI × Math 0 项，AI Voices 7 项，Engineering 9 项。9月15日的精选以预印本与公开工程动向为主：化学聚焦三维相互作用条件下的分子生成，生物涵盖超声触发的非病毒基因递送；数学频道因数据源获取失败没有可审阅内容。观点频道收录公开帖文，反思智能体评测与真实部署；工程频道呈现当日热门开源项目，不将其热度等同于经验证的软件能力。

## 今日重大进展

- [2004 年强 Papadimitriou–Ratajczak 猜想被宣布解决](https://x.com/LechMazur/status/2098915169799733339) — Lech Mazur 公布，强 Papadimitriou–Ratajczak 猜想已获证明：每个 3-连通平面图都存在凸贪心绘制。其称证明由 ProofAtlas 与 GPT-6 Pro 找到，并已用 Lean 形式化为约 5.2 万行。
- [Reward AI 公布可跨机器人零样本泛化的 OM-1](https://x.com/RewardAI_/status/2099553899804053992) — Reward AI 在公开帖中发布首个机器人基础模型 OM-1，称其直接从人类操作数据学习，无需遥操作或机器人数据，即可零样本适配桌面机械臂、工业臂与人形机器人，并支持多机器人协作。
- [社媒称 Atria Dawn Preview 以 MIT 许可开放 744B MoE 智能体模型](https://x.com/Smlay_ero/status/2099699408900342255) — 公开帖称，上海 AI 实验室于 9 月 14 日开源 Atria Dawn Preview：它基于 744B 参数 GLM-5.2 MoE，提供权重与代码、256K 上下文，并面向长程智能体任务；帖文同时列出多项基准成绩。

## AI × Chem

采集 317，候选 39，精选 6。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 429: Unknown Error

- [Interaction Profiles as a Universal Language for Generative Molecular Design with ShEPhERD-2](https://www.biorxiv.org/content/10.64898/2026.09.10.750648) — ShEPhERD-2 以形状、静电和定向药效团构成的三维相互作用谱为条件，生成低应变、类药小分子；同一模型可用于生物电子等排体片段合并、双靶点设计、选择性工程和模态转换，无需任务特异性再训练。
- [Machine Learning-Guided Classification of Druggable Pockets and Phylogenetic Druggability Transfer Across the Human Kinome](https://www.biorxiv.org/content/10.64898/2026.09.06.749698) — 研究汇集 11,945 个激酶抑制剂复合物，以 Extra Trees 分类器根据口袋残基—配体相互作用标注七类经典结合模式及变构亚类，并将结果与 Manning 激酶组系统发育整合，以推断未充分研究激酶的变构可成药性。
- [Heterogeneous graph neural networks with biological prior knowledge for interpretable drug repurposing in triple-negative breast cancer](https://www.biorxiv.org/content/10.64898/2026.09.08.750045) — PRECISION 将转录因子调控网络、蛋白—蛋白相互作用和药物—靶点边整合为异质 GNN，用于三阴性乳腺癌药物再定位；作者以细胞系留出、多队列生存关联及 39 例配对样本评估，提出 7 个候选药物并指向 EGFR 信号轴。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1027，候选 60，精选 8。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 429: Unknown Error；medRxiv: JSONDecodeError: Expecting value: line 1 column 1 (char 0)

- [Nonviral, ultrasound-triggered gene delivery platform via gas-core cationic nanobubbles](https://www.biorxiv.org/content/10.64898/2026.09.11.749060) — 气核阳离子纳米气泡在体外高效内化并负载质粒 DNA；在小鼠肝脏中，超声触发后出现局部 GFP 表达及可同步监测的造影变化。
- [TransBind2: Improving Transcription Factor-DNA Binding Prediction with Multimodal Data and Bidirectional Cross Attention](https://www.biorxiv.org/content/10.64898/2026.09.07.749913) — TransBind2 以 DNA 序列、DNase-seq 可及性、基因组可比对性和 ProstT5 的 TF 序列—结构表示为输入，在 690 个 ChIP-seq 实验、161 个 TF 和 91 种细胞类型上报告宏平均 AUROC 0.9648。
- [Diagnostic Performance of Agentic AI for Rare Disease Diagnosis: A Systematic Review, Meta-analysis, Workflow Development, and Benchmark-based Validation](https://europepmc.org/article/PPR/PPR1318941) — 该系统综述与单臂随机效应 Meta 分析纳入 7 项研究、19 个效应量和 33,738 个病例；其 50 例 RareBench 验证中，工作流辅助 GPT 的 Top-1 正确数为 11/50，独立 GPT 为 5/50。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 0，候选 0，精选 0。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 429: Unknown Error

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 91，候选 60，精选 7。来源状态：各来源已完成

- [@dair_ai：Great paper from Amazon. In discusses when not to trust LLM judges for agent evaluation. (bookmark it) A common way to c](https://x.com/dair_ai/status/2099518541930332182) — DAIR.AI 转述一项 Amazon 研究：在 25 个、来自六家提供商的智能体上，LLM 裁判的满意度判断与任务成功可能脱钩，且能力接近的智能体比较更易误判。
- [@chelseabfinn：A video from a Pi robot deployed at Dandelion Chocolate, fully autonomous w/ no interventions. 🤖 Deploying robots has ta](https://x.com/chelseabfinn/status/2099669259735728252) — Chelsea Finn 报告了一台部署于 Dandelion Chocolate 的 Pi 机器人；她以持续真实部署为例，说明“做出一个箱子”和连续数小时可靠地完成工作之间存在明显差距。
- [@fchollet：> One could even define intelligence as the efficiency with which one converts experience into competence; by this defin](https://x.com/fchollet/status/2099633702888439865) — François Chollet 提出，应以“将经验转化为能力的效率”界定智能；据此，他认为当前 AI 在样本、测试时计算和能耗效率上仍远低于人类。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 59，候选 58，精选 9。来源状态：各来源已完成

- [JustVugg/colibri](https://github.com/JustVugg/colibri) — JustVugg/colibri 是纯 C、零依赖的 MoE 模型推理引擎，通过从磁盘流式载入专家，尝试让现有硬件运行前沿 MoE 模型；当日 GitHub Trending 第 1 名，新增 2,173 星。
- [alibaba/open-code-review](https://github.com/alibaba/open-code-review) — alibaba/open-code-review 将确定性流水线与 LLM 智能体结合，生成精确到代码行的审查意见，并内置多语言的空指针、线程安全、XSS 和 SQL 注入规则；当日 GitHub Trending 第 2 名，新增 1,571 星。
- [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE) — multimodal-art-projection/YuE 发布 YuE2 音乐生成模型，支持符号化规划、零样本翻唱与智能体式音乐编辑；当日 GitHub Trending 第 3 名，新增 559 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
