# AIxDaily · 2026-09-22

今日精选：AI × Chem 12 项，AI × Bio 15 项，AI × Math 0 项，AI Voices 10 项，Engineering 5 项。今日更新集中在可验证但仍需审慎解读的前沿进展：化学频道的两项生物催化与分子共折叠工作、生命科学频道的蛋白互作组与发育图谱研究均为预印本，不能等同于同行评议结论；AI Voices 主要是 X 上的公开观点及对论文的二手转述，工程频道则聚焦 GitHub 上的智能体开发框架与记忆、隔离环境工具。数学频道今日没有足够高质量更新。

## 今日重大进展

- [从头设计的金属蛋白酶实现高效肽键切割，并可作用于疾病相关底物](https://www.biorxiv.org/content/10.1101/2025.11.20.689622) — 研究者用 RoseTTAFold Diffusion 2 设计锌金属蛋白酶；135 个设计中 36% 具活性并能精准切割，最强设计使肽键水解加速超过 10^10 倍，还可切割 TDP-43 和 β-淀粉样蛋白。
- [X 转述 Google ScientistTwo：AI 将自己的研究发现作为基线继续改进](https://x.com/rohanpaul_ai/status/2101449041091657746) — 研究者在 X 上转述 Google 的 ScientistTwo：系统先改进人类方法，再把发现作为新基线继续迭代；帖文称其在 ICLR、ICML、NeurIPS 论文问题上成功率 80.4%，相对基线提升 25.2%。
- [FloatLib 在 Lean 中验证任意精度浮点运算，推进可证明科学计算](https://x.com/AnimaAnandkumar/status/2102048384802771185) — Anima Anandkumar 宣布 FloatLib：一个在 Lean 中验证的任意精度浮点库，覆盖 IEEE、posit、P3109 和小型 ML 格式；优化后的后端均附带证明，确保舍入、溢出和异常值结果符合规范。

## AI × Chem

采集 759，候选 60，精选 12。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable

- [Computational design of metalloproteases](https://www.biorxiv.org/content/10.1101/2025.11.20.689622) — 作者使用 RoseTTAFold Diffusion 2 for Molecular Interfaces，从最小催化基序出发进行锌金属蛋白酶从头设计。在实验测试的 135 个计算设计中，36% 具有活性并能在预定位置精准切割；进一步设计的金属蛋白酶可切割人 TDP-43、amyloid-{beta} peptide 和 serum amyloid A，并用于选择性解笼蔽细胞因子和受体拮抗剂。
- [Large scale prospective evaluation of co-folding across hundreds of Mac1-ligand complexes and three virtual screens](https://www.biorxiv.org/content/10.64898/2025.12.25.696505) — 研究对 551 个 SARS-CoV-2 NSP3 macrodomain（Mac1）配体复合物开展独立于训练数据的大规模前瞻性共折叠评估，并进一步测试三个虚拟筛选场景。AlphaFold3、Boltz-2 和 Chai-1 均能对超过一半的配体重现优于 2 [A] RMSD 的实验构象；Boltz-2 的亲和力预测与实测效力相关性最强。
- [SimSJSAlert: A Similarity-Augmented Multi-View Learning Framework with Scaffold Alerts for Drug-Induced Stevens-Johnson Syndrome Risk Assessment](https://doi.org/10.26434/chemrxiv.15008910/v2) — 作者构建 SimSJSAlert，通过融合 21 种分子表示、相似性信息和 scaffold alerts，对药物诱导的 Stevens-Johnson syndrome（SJS）风险进行 QSTR 预测。研究采用 scaffold-aware validation、外部 pharmacovigilance negative-signal 化合物评估及 SHAP 与 Bemis-Murcko scaffold 富集分析，并部署了可公开访问的网页服务器。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1443，候选 60，精选 15。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable

- [Integrating structural homology with deep learning to achieve highly accurate protein-protein interface prediction for the human interactome](https://www.biorxiv.org/content/10.1101/2025.06.09.658393) — PIONEER2 将结构同源性与几何深度学习结合，用于预测人类互作组中的蛋白质界面。
- [A lifespan single-cell atlas of the human developing hippocampus benchmarks familial Alzheimer's disease brain organoids.](https://www.biorxiv.org/content/10.64898/2026.09.18.752796) — HuDeHA 汇集从受孕后第3周到15.3岁的658,059个细胞，为家族性阿尔茨海默病脑类器官提供发育参照。
- [Bivalent bispecific CD28 antibodies reinforce T-cell responsiveness and revert anergy/quiescence in patients treated with bispecific CD3 antibodies](https://www.biorxiv.org/content/10.64898/2026.03.25.714198) — 双价双特异性 CD28 抗体在双特异性 CD3 抗体治疗背景下恢复T细胞反应性。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 0，候选 0，精选 0。来源状态：arXiv: RuntimeError: Unable to fetch https://export.arxiv.org/api/query?search_query=%28cat%3Acs.LG+OR+cat%3Acs.AI+OR+cat%3Acs.CL+OR+cat%3Acs.NE+OR+cat%3Astat.ML+OR+cat%3Acs.LO+OR+cat%3Acs.FL+OR+cat%3Acs.SC+OR+cat%3Amath.LO+OR+cat%3Acs.CE+OR+cat%3Aphysics.chem-ph+OR+cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.QM+OR+cat%3Aq-bio.NC%29&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending: HTTP Error 406: Not Acceptable

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 78，候选 60，精选 10。来源状态：各来源已完成

- [@rohanpaul_ai：New Google paper shows LLM agents handle long tasks better when their workflow lives in an editable procedure graph that](https://x.com/rohanpaul_ai/status/2101973711612190756) — 帖文转述一篇 Google 论文：让大语言模型智能体的工作流存在于可编辑、能从执行中学习的程序图中，而不是埋藏在聊天历史里，以改善长任务处理。
- [@AndrewYNg：The loudest voices stoking fears about AI dangers have made tremendous headway in the past two weeks. AI technology has ](https://x.com/AndrewYNg/status/2102140576498065758) — Andrew Ng 认为，近期 AI 风险讨论中的恐惧被炒作放大；他将智能体带来的主要新风险归为网络安全能力，并主张通过修复沙箱、监控和其他安全工程问题来降低风险，而不是暂停 AI 进展。
- [@DimitrisPapail：Test-time communication looks like a next axis for scaling capabilities New paper with the incredible @jon_ghoh and @vko](https://x.com/DimitrisPapail/status/2101901206746701880) — 论文作者 Dimitris Papailiopoulos 介绍一项关于测试时通信的研究：N 个相同智能体只通过共享日志协作，在三个研究型任务上超过独立工作的智能体。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 67，候选 60，精选 5。来源状态：各来源已完成

- [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) — BuilderIO/agent-native 是一个用于构建智能体应用的 TypeScript/React 框架，今日位列 GitHub Trending 第 1 名，新增 607 个星标（总计 5,861）。
- [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) — akitaonrails/ai-memory 为编程 Agent CLI 提供长期记忆，并支持不同 Agent 厂商之间的交接，今日位列 GitHub Trending 第 4 名，新增 217 个星标（总计 7,649）。
- [coder/coder](https://github.com/coder/coder) — coder/coder 为开发者及其智能体提供安全的开发环境，今日位列 GitHub Trending 第 5 名，新增 461 个星标（总计 16,399）。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
