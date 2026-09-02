# AIxDaily · 2026-09-02

今日精选：AI × Chem 16 项，AI × Bio 14 项，AI × Math 13 项，AI Voices 10 项，Engineering 9 项。今日五个频道共同日期为9月2日。AI×化学、生物和数学的前三项均为预印本，涉及结构—亲和力数据、临床与转录组应用及推理评测，前三项中未见同行评议论文。AI Voices 收录官方公开帖文和研究博客；工程频道前三项均为 GitHub 热门项目，覆盖编程、科研工作流与多智能体互动应用。

## 今日重大进展

- [OpenAI 预览 Astra：首个达到“关键”网络安全能力阈值的模型](https://openai.com/index/path-to-astra) — OpenAI 发布 Astra 预览，并称这是首个达到其 Preparedness Framework“关键”网络安全能力阈值的模型；公司同时公开了评估方法，以及随能力升级的发布安全措施。
- [李飞飞公布 Atlas：从零预训练的多模态世界模型](https://x.com/drfeifei/status/2094840371675283673) — World Labs 联合创始人李飞飞公布 Atlas，称其为从零预训练的多模态世界模型，可由单张图重建大场景、输出原生三维空间，并以像素级精度控制相机视角。
- [Google Research 发布 TimesFM-3：一次前向计算完成多变量预测](https://x.com/GoogleResearch/status/2094483372718580066) — Google Research 宣布 TimesFM-3，称该时间序列基础模型可在一次前向计算中进行零样本多变量预测，并在主要基准上显著优于其他预测模型。

## AI × Chem

采集 1355，候选 60，精选 16。来源状态：各来源已完成

- [The first OpenBind release: An open experimental structure-affinity dataset and benchmark for structure-based AI](https://www.biorxiv.org/content/10.64898/2026.08.27.747600) — OpenBind 首次公开了以肠道病毒2A protease为对象的蛋白—配体结构—亲和力数据集，并用其评估对接、共折叠、亲和力预测和虚拟筛选；在片段筛选结构上微调 OpenFold3-p2 可提升后续化合物的构象预测与虚拟筛选表现。
- [When Do Models Win? A Learning Curve Benchmark for Molecular Property Prediction in Low-Data Regimes](https://doi.org/10.26434/chemrxiv.15001253/v6) — 该工作在 QM9、ESOL、Lipophilicity 和 BACE 的 scaffold split 上，以50至3,000个样本比较传统机器学习、GNN、分子语言模型和3D网络，量化数据规模与任务类型如何共同决定模型选择。
- [An Agentic Retrobiosynthesis Framework with Learned Frontier Selection](https://arxiv.org/abs/2608.30702v1) — 该研究将 Qwen2.5-7B 用作规则驱动逆生物合成中的前沿分子选择策略，在保持生化反应生成器完全一致的条件下，评估提示和 LoRA 微调对有限搜索预算的贡献。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2120，候选 60，精选 14。来源状态：各来源已完成

- [Context-aware LLM extraction and controlled-vocabulary normalization of GEO transcriptomic sample metadata](https://europepmc.org/article/PPR/PPR1308540) — 该研究以本地可部署LLM将GEO转录组样本的自由文本元数据转为标准化的组织、状态和处理标签，并在804,427个人类样本上评估。
- [Clinical evaluation of artificial intelligence for diagnostics of antibiotic-resistant bacteria](https://www.medrxiv.org/content/10.64898/2026.08.27.26361401) — 研究在99株临床尿液E. coli分离株上评估AI药敏预测，并量化保形预测在降低错误与增加拒答之间的权衡。
- [INTERVenE: Temporal-Abstraction-Interval Based Transformers for Short-Horizon Medical Event Prediction](https://arxiv.org/abs/2608.29901v1) — INTERVenE将知识驱动的时间抽象区间编码为具名临床概念token，在57,078例MIMIC-IV住院记录上进行短期风险与事件时间预测。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 731，候选 60，精选 13。来源状态：各来源已完成

- [DERELAB: Probing Defeasible Reasoning and Confirmation Bias in LLMs with a Generative Benchmark](https://arxiv.org/abs/2608.30413v1) — DeReLab 从参数化图生成多轮信念更新对话，并在每一步提供经形式化验证的标准答案，用于测量模型面对支持或反驳证据时是否更新结论。
- [HSRM: Hidden-State Reward Models for Test-Time Verification](https://arxiv.org/abs/2608.30841v1) — HSRM 直接读取生成器隐藏状态，对数学解答候选排序，以较小验证器替代重新阅读完整文本的验证流程。
- [Autoregressive Mosaics: Probing 2D Spatial Reasoning in Text-Only Language Models](https://arxiv.org/abs/2608.30751v1) — AM-Bench 将文字描述到绘图代码的转换，与根据不充分提示组织二维布局的任务区分开来，考察文本模型的二维空间推理。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 59，候选 56，精选 10。来源状态：各来源已完成

- [@GoogleResearch：Introducing TimesFM-3, a state-of-the-art time series foundation model that enables accurate multivariate time series fo](https://x.com/GoogleResearch/status/2094483372718580066) — Google Research 宣布 TimesFM-3，用单次前向传播完成多变量时间序列预测，并称其在主要基准上显著优于其他预测模型。
- [@vllm_project：🎉 Congrats to @deepseek_ai on DeepSeek-V4-Flash-Vision-Exp, the first multimodal model in the V4 family! vLLM serves it ](https://x.com/vllm_project/status/2094711861472350343) — vLLM 宣布已支持 DeepSeek-V4-Flash-Vision-Exp，并说明该模型在 V4-Flash MoE 主干上加入视觉编码器和对齐器。
- [Path to Astra: critical capabilities and frontier safeguards](https://openai.com/index/path-to-astra) — OpenAI 官方博客称，Astra 是首个达到其 Preparedness Framework“关键”网络安全能力阈值的模型，并配有更强的发布安全措施。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 58，候选 57，精选 9。来源状态：各来源已完成

- [Gitlawb/openclaude](https://github.com/Gitlawb/openclaude) — 面向 AI 编程智能体的命令行工具，GitHub Trending 第 1 名，日增 80 星标。
- [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) — 为 Claude Code 提供科研工作流技能集，覆盖检索、写作、审阅、修改与定稿，GitHub Trending 第 2 名，日增 193 星标。
- [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — 开放式多智能体交互课堂项目，提供一键式沉浸学习体验，GitHub Trending 第 3 名，日增 3128 星标。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
