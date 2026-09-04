# AIxDaily · 2026-09-05

今日精选：AI × Chem 14 项，AI × Bio 10 项，AI × Math 7 项，AI Voices 7 项，Engineering 8 项。9月5日的五频道精选显示，科研侧以预印本为主：化学关注药物—靶标表征与DEL反应预测，生物延伸至抗蛇毒蛋白和单细胞表征，数学则检验多语言推理稳健性与奖励设计。AI Voices收录公开帖文和转述观点，尚非同行评议结论；工程频道报道GitHub热门开源项目，前三项并非版本化软件发布。

## 今日重大进展

- [OpenAI 发布 GPT-6 Astra：通用计算机智能体走向产品化](https://x.com/OpenAI/status/2095595742975197690) — OpenAI 发布 GPT-6 Astra，称其在计算机操作、浏览、软件工程、网络安全、科学与专业工作上达到新水平；官方后续表示该模型已进入 ChatGPT Work、Codex 和 API。
- [Anthropic 公布 Claude 完成费马大定理的 Lean 形式化](https://x.com/AnthropicAI/status/2095947707605266436) — Anthropic 公布 Claude 完成费马大定理的端到端 Lean 形式化，并称代码超过1,300万行、覆盖逾29,000条相关定理。费马大定理早在1995年被证明，本次工作使其推理链可由机器检查。
- [K2 Horizon 开放六模型系列，代码、数据与训练配方同步公布](https://x.com/IFM_AI/status/2095497035806113861) — Institute of Foundation Models 发布0.9B至375B的六模型 K2 Horizon 系列，并公布代码、训练数据及配方；机构称小型型号在各自尺寸的编程和智能体任务中达到领先表现。

## AI × Chem

采集 1441，候选 60，精选 14。来源状态：各来源已完成

- [Comprehensive Evaluation of Protein Language Model Embeddings for Drug-Target Affinity Prediction](https://www.biorxiv.org/content/10.64898/2026.08.31.748056) — 系统比较多类预训练蛋白语言模型嵌入及改良卷积架构在药物—靶标亲和力预测中的作用，并在 Davis、KIBA 及冷启动划分上评估泛化表现。结果表明，传统卷积模型的简单架构改进可能已能缩小其与大型 PLM 的差距。
- [Machine Learning for High-Throughput Reaction Yield Prediction in DNA-Encoded Library Synthesis](https://doi.org/10.26434/chemrxiv.15008275/v1) — 提出面向 DEL 单循环反应验证的官能团中心机器学习框架，仅以暴露反应官能团、局部环境、构件和反应类型为输入；在真实高通量数据上，局部表征的 GNN 优于指纹基线。
- [De novo design of ligand binding proteins using large language models alone](https://www.biorxiv.org/content/10.64898/2026.09.02.748987) — 检验 Claude、ChatGPT、Gemini 等通用 LLM 是否可仅依靠提示中的设计原则，从头生成结合金属或疏水小分子的蛋白；筛选后进行了实验验证，金属结合蛋白和 perfluorooctanoic acid 结合蛋白均报告 25% 命中率。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2208，候选 60，精选 10。来源状态：各来源已完成

- [De novo designed single-domain antibodies protect against lethal cobra venom neurotoxicity in vivo](https://europepmc.org/article/PPR/PPR1311990) — 从头设计单域抗体在小鼠中抵御致死性眼镜蛇神经毒素
- [scRep: A Latent-Space Self-Distilled Foundation Model for Single-Cell Representation Learning](https://www.biorxiv.org/content/10.64898/2026.08.31.747784) — scRep：以潜在空间自蒸馏学习单细胞表征的基础模型
- [DeepCNet: A multimodal deep learning model for predicting cell type-specific gene expression and promoter-enhancer interactions from single-cell multiome data](https://europepmc.org/article/PPR/PPR1311522) — DeepCNet 从单细胞 multiome 数据预测细胞类型特异的表达与启动子—增强子互作

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 620，候选 60，精选 7。来源状态：各来源已完成

- [Lost in Reordering: Structural Sensitivity of Multilingual LLMs under Semantics-Preserving Perturbations](https://arxiv.org/abs/2609.03511v1) — 该研究以 Hindi 和 Malayalam 中保持语义不变的语序重排、主被动转换为扰动，构建 IndicReStruct，并在 GSM8K 衍生任务上检验六个 LLM 的数学推理稳健性。结果显示，结构变化会稳定降低表现，残差流激活修补分析将部分失败关联到实体与数量的对应关系。
- [Gradients Know What Outcomes Don't: Unlocking Reinforcement Learning for LLM Reasoning with Gradient-Aligned Rewards](https://arxiv.org/abs/2609.03342v1) — GAR 在策略梯度空间中，把每条 rollout 的紧凑梯度向量与专家锚点梯度作余弦比较，形成稠密奖励。论文在 Qwen3-4B 与 Qwen3-8B 上报告其在竞赛级数学基准优于 GRPO 等比较方法，并测试了向 GPQA Diamond、MMLU-Pro 的迁移。
- [Extending concurrent separation logic to the hardware level to verify the xv6 OS kernel on RISC-V with AI agents](https://arxiv.org/abs/2609.04043v1) — MachCSL 将基于 Iris 的并发分离逻辑延伸到 Sail RISC-V 语义下的指令级硬件执行，并以 AI agents 协助验证 6,593 行 C 与汇编构成的 xv6 内核。摘要报告发现了 xv6 的 9 个缺陷及 Sail RISC-V 语义中的 1 个缺陷。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 123，候选 60，精选 7。来源状态：各来源已完成

- [@IFM_AI：Introducing K2 Horizon: a connected fleet of six foundation models ranging from 0.9 billion to 375 billion parameters. -](https://x.com/IFM_AI/status/2095497035806113861) — Institute of Foundation Models 发布 K2 Horizon，称其由 6 个参数规模 0.9B 至 375B 的基础模型组成，并公开代码、训练数据与训练配方；各尺寸性能纪录属于发布方说法。
- [@ArtificialAnlys：Announcing Artificial Analysis Intelligence Index v4.2. We are accelerating elements of our upcoming v5 release with int](https://x.com/ArtificialAnlys/status/2096001986110099767) — Artificial Analysis 发布 Intelligence Index v4.2，加入智能体知识工作和长上下文文档推理测试，并调整私有及留出测试集的权重。
- [@Thom_Wolf：Another swarm of AI agents in the wild, this time on a German-language forum, found by safety researchers looking for ac](https://x.com/Thom_Wolf/status/2095889630306472127) — Thomas Wolf 转述一份关于德语论坛 AI 智能体活动的报告，并据此讨论智能体对评测机制的逆向分析与协同行为。帖文中的事件细节来自其所引报告，关于训练与部署关系的判断属于作者观点。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 70，候选 60，精选 8。来源状态：各来源已完成

- [anthropics/skills](https://github.com/anthropics/skills) — Anthropic 的公开 Agent Skills 仓库，GitHub Trending 第 5 名，当天新增 512 星。它提供可供智能体使用的技能包集合。
- [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) — NousResearch/hermes-agent 是强调随用户使用持续成长的智能体，GitHub Trending 第 7 名，当天新增 721 星。仓库主题覆盖 AI 智能体、LLM 与多家模型及编码助手生态。
- [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude) — magnitudedev/magnitude 是可按本机硬件运行本地模型、并接入既有智能体的开源推理服务器，GitHub Trending 第 9 名，当天新增 395 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
