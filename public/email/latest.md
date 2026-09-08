# AIxDaily · 2026-09-09

今日精选：AI × Chem 12 项，AI × Bio 10 项，AI × Math 0 项，AI Voices 9 项，Engineering 4 项。今日更新横跨化学、生物医学与智能体工程：ChemRxiv 预印本从高通量药化到可迭代合成代理，并提示材料训练数据审计的重要性；生物频道的三项均为预印本，涉及分诊评测、数据库代理与兽医 EHR 分类。AI Voices 聚焦机构和作者的公开观点，数学正确性与研究来源仍待独立审查；工程频道则为 GitHub Trending 项目，适用性需本地验证。AI×Math 今日没有足够高质量更新。

## 今日重大进展

- [OpenAI 公布智能体解答 Navier–Stokes 千禧年难题](https://x.com/OpenAI/status/2097374640582668336) — OpenAI 公布称，一组由下一代模型驱动的智能体已给出 Navier–Stokes 千禧年难题的一份解答。该问题追问三维光滑流体运动会否在有限时间出现破裂，悬而未决约90年。
- [Google DeepMind 发布 AlphaGenome Atlas，覆盖90亿种单碱基变异预测](https://x.com/GoogleDeepMind/status/2097325048109384166) — Google DeepMind 发布 AlphaGenome Atlas：一个可检索数据库，映射人类基因组全部约90亿种可能单碱基 DNA 变异的预测影响，面向研究者探索变异与生物学机制。

## AI × Chem

采集 588，候选 60，精选 12。来源状态：各来源已完成

- [High-Throughput Experimentation Enables the C6-Functionalisation of 1H-Indazol-3-Amines as Antitubercular Agents](https://doi.org/10.26434/chemrxiv.15008508/v1) — 以 984 个平行反应构成的高通量实验系统绘制 Suzuki–Miyaura 与 Buchwald–Hartwig 偶联的条件空间，并将 1H-indazol-3-amine 骨架用于分枝杆菌 TrxR 抑制剂开发；工作同时给出了生化活性和 5 个共晶结构验证。
- [CampChem: Rubric-Grounded Adaptive Campaigns for Multi-Round Organic Synthesis with Residual Spectral Observation](https://doi.org/10.26434/chemrxiv.15008453/v1) — CampChem 将化学指令 LLM 扩展为可根据失败条件和 NMR 残余峰进行多轮修订的合成活动代理，并以规则驱动的强化学习约束化学计量、危险相容性、槽位完整性和光谱一致性。
- [A single reference-energy outlier nearly eliminates Co–O chemistry from a generative model's training distribution](https://doi.org/10.26434/chemrxiv.15008501/v1) — 对 MatterGen 生成的 44,688 个氧化物进行元素分辨审计后，作者定位到 Alex-MP-20 中一个异常参考能量条目；该条目扭曲 Co–O 凸包并使稳定性筛选几乎清除含钴训练样本。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1083，候选 60，精选 10。来源状态：各来源已完成

- [Reasoning Before Disposition: A Model-Agnostic Cannot-Miss Discipline for Quiet Emergencies and the Case for Deterministic Enforcement](https://www.medrxiv.org/content/10.64898/2026.09.02.26362074) — 在跨 8 个模型的构建性分诊评测中，不能漏诊规则降低了非典型急症的低分诊率；作者明确指出尚不能据此主张临床安全性。
- [Democratizing Agentic Access to Bioinformatics and Biopharmaceutical Databases and Analyses with BioMCP-TS](https://www.biorxiv.org/content/10.64898/2026.09.03.749120) — BioMCP-TS 将 50+ 生物信息、药物和专利数据库检索，与浏览器内 WebAssembly 分析整合到开源 MCP 服务器。
- [Hybrid Rule-Based and Machine Learning Classification of Military Working Dog Medical Problems Using SNOMED CT and the Veterinary Extension](https://europepmc.org/article/PPR/PPR1313756) — 混合规则、SapBERT 链接和监督分类流程为 73,856 条军犬兽医 EHR 问题记录分配了临床类别，并由 9 位专家盲法评审验证。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 0，候选 0，精选 0。来源状态：各来源已完成

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 64，候选 60，精选 9。来源状态：各来源已完成

- [@OpenAI：We’re sharing a solution to the Navier-Stokes Millennium Prize Problem, one of the deepest problems at the frontier of m](https://x.com/OpenAI/status/2097374640582668336) — 事实：OpenAI 公开称，其下一代模型驱动的一组智能体给出了 Navier–Stokes 千禧年难题的解，并说明该问题涉及光滑三维流动是否会发生破裂。
- [@AnimaAnandkumar：We have found stable singularity on 3D Euler! http://anima-ai.org/2026/09/07/stable-singularity-of-the-euler-equations-o](https://x.com/AnimaAnandkumar/status/2097216195342864528) — 事实：Anima Anandkumar 发布了关于三维 Euler 方程稳定奇点的研究链接，并描述以 PINN 寻找近似解、再分析其稳定性的路线。作者观点：物理信息与物理中心的 AI 对物理系统研究很关键，而 LLM 缺少这种物理扎根。
- [@OpenAI：We congratulate Levent Alpöge and Tristan Buckmaster on their remarkable mathematical work. We (the researchers and the ](https://x.com/OpenAI/status/2097375276384567642) — 事实：OpenAI 就 Navier–Stokes 公告回应称，在对方公开前未通过任何方式接触其工作，也未为解题访问特定用户数据；同时称不能排除去标识化衍生数据曾帮助改进模型。该机构还称双方在 Euler 问题中证明的精确结果不同。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 51，候选 50，精选 4。来源状态：各来源已完成

- [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) — 面向编码智能体的输出约束技能，避免把结论埋进冗长过程，提供更适合注意力管理的简洁回答格式；当日 GitHub Trending 第1名，新增422星。
- [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) — 以单个 CLAUDE.md 文件汇集大语言模型编码常见失误的规避建议，用于改善 Claude Code 行为；当日 GitHub Trending 第8名，新增533星。
- [browser-use/browser-use](https://github.com/browser-use/browser-use) — 为 AI 智能体提供网站访问与浏览器任务自动化能力，基于 Python 和 Playwright 等工具连接网页操作；当日 GitHub Trending 第12名，新增320星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
