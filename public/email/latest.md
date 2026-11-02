# AIxDaily · 2026-11-03

今日精选：AI × Chem 13 项，AI × Bio 15 项，AI × Math 0 项，AI Voices 10 项，Engineering 6 项。今日（2026-11-03）五频道呈现出“方法创新多、证据层级不一”的格局：AI×Chem 前三项均为预印本，聚焦蛋白构象、水合预测与溶剂排序；AI×Bio 同时有一篇同行评议综述和两篇预印本，覆盖精准给药、衰老标志与细胞重编程。AI×Math 今日没有足够高质量更新。AI Voices 收录的是公开帖文与课程、观点信息，不等同于同行评议结论；Engineering 前三项是 GitHub Trending 开源软件动向，暂非正式版本发布公告。

## 今日重大进展

- [Hydrogen-1.0公布：面向科学发现的开放权重模型宣称超越GPT-6-Astra](https://x.com/chenru_duan/status/2117249292469665838) — Chenru Duan公布 Hydrogen-1.0，称其基于 GLM-5.3、在内部科学数据与实验室记录上后训练，报告 FrontierScience-Research 38.3%、GPQA-Diamonds 93.0%，并以开放权重服务科学发现。
- [vLLM v0.33.0发布：推理栈接入大批新模型与推测解码能力](https://github.com/vllm-project/vllm/releases/tag/v0.33.0rc3) — vllm-project/vllm发布v0.33.0rc3，汇集927次提交，新增多种模型、推测解码、KV传输和OpenAI兼容接口，并默认提供CUDA 13与ROCm 10镜像，同时移除部分旧执行器与CUDA 12.9构建。
- [QA-Bench发布：把AI代码代理的找Bug能力拉到真实应用场景](https://x.com/wuweiweiwu/status/2117306624452792446) — 作者公布QA-Bench，面向真实应用中的可复现缺陷发现，并称其智能体Mo找到的bug数量分别达到Codex的2.7倍、Claude Code的6.3倍；方法和数据已公开。

## AI × Chem

采集 509，候选 60，精选 13。来源状态：各来源已完成

- [Differentiable Spin-Center Diffusion Model Enables DEER-Guided Generative Pipeline of Weighted Protein Ensembles](https://www.biorxiv.org/content/10.64898/2026.10.29.762916) — 提出可微分的自旋中心扩散模型，并将其与冻结的 Boltz-2 结构生成器结合，使 DEER 实验距离分布 P(r) 能在推理阶段直接引导加权蛋白构象集合生成；在合成数据和 PfMATE、LmrP、MhsT、P-glycoprotein 转运蛋白上恢复构象比例并估计条件依赖的自由能差。
- [3DRISM Solvation for Accurate and Large-Scale Protein Hydration Prediction and Mechanistic Interpretation](https://doi.org/10.26434/chemrxiv.15011467/v1) — 系统评估 3DRISM 在大规模蛋白水合位点预测中的表现，并与 SuperWater 及显式溶剂 MD 对比；在3,139个域外蛋白、20个随机蛋白和 SiaP 配体结合口袋案例中检验精度、效率及突变诱导的局部脱水解释能力。
- [SolviScope: An Interaction-Aware Graph Neural Network for Solvent Ranking of Small Organic Molecules in Pure and Multicomponent Solvent Systems](https://doi.org/10.26434/chemrxiv.15011474/v1) — 开发 SolviScope 图神经网络，用于纯溶剂和二元混合溶剂中的溶解度预测与溶剂排序；模型在结构留出集、外部基准和工业溶质混合物上评估，并对两个未见 API 进行回顾性溶剂/反溶剂优先级排序。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1376，候选 60，精选 15。来源状态：各来源已完成

- [Machine Learning-Augmented Precision Dosing: Integrating Pharmacokinetic Modeling With Clinical Decision Support.](https://europepmc.org/article/MED/42902867) — 综述机器学习如何与群体药代动力学、PBPK、贝叶斯预测和治疗药物监测结合，用于暴露量预测、有限采样 AUC 估计、风险分层和序贯给药。
- [Atherosclerosis and Diabetic Foot Share a Common Molecular Signature of Cellular Senescence: A Multi-Omics and Machine Learning Study](https://europepmc.org/article/PPR/PPR1354635) — 整合 DFU 与 AS 转录组、单细胞和组织验证，筛出 CALCOCO1、CCND2、FUCA1 三个共同衰老特征基因，并观察到 metformin 可在体外部分逆转成纤维细胞衰老表型。
- [FateDriver: Weakly supervised dual-view graph learning for transition-specific prioritization of candidate regulators in cellular reprogramming](https://europepmc.org/article/PPR/PPR1354904) — FateDriver 将单细胞转录组中的细胞与基因建模为双视图图网络，把已递送诱导因子作为稀疏标签，在 OSKM、GMT 和体内部分重编程数据中进行转变特异的调控因子排序。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 0，候选 0，精选 0。来源状态：各来源已完成

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 43，候选 38，精选 10。来源状态：各来源已完成

- [@fchollet：The most grating aspect of LLM writing is that it tries to turn every single sentence into a punchline, a witty slogan, ](https://x.com/fchollet/status/2117315680119013865) — 事实：François Chollet 批评大语言模型写作把每句话都处理成“妙语”或口号。作者观点：这种平均用力的表达削弱了重点层次。编辑判断：这是对生成式写作风格的直接质量批评。
- [@shao__meng：斯坦福大学课程 CS329A Self-Improving AI Agents @achowdhery @Azaliamirh 两位老师主讲，以 "一线经验 + 论文精读" 为骨架，以 "造一个能自我改进的智能体" 为课程目标，Youtub](https://x.com/shao__meng/status/2116901124716347815) — 事实：帖文介绍斯坦福 CS329A“Self-Improving AI Agents”课程，由两位教师授课，YouTube 已收录全部9节。编辑判断：课程将一线经验与论文精读结合，具有较明确的学习入口。
- [@Saboo_Shubham_：AI Agent framework vs harness. A framework is a library you import to build an agent. ADK, LangGraph, and CrewAI give yo](https://x.com/Saboo_Shubham_/status/2116402491827143098) — 事实：作者区分 framework 与 harness：前者提供构建组件，后者把循环、工具、上下文、记忆和子智能体整合成可运行的智能体。编辑判断：这是一种面向工程实践的架构分类。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 50，候选 49，精选 6。来源状态：各来源已完成

- [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) — vercel-labs/agent-desktop 是面向 AI 智能体的计算机使用 CLI，位列当日 GitHub Trending 第1名，新增2243颗星。
- [JustVugg/colibri](https://github.com/JustVugg/colibri) — JustVugg/colibri 用纯 C、零依赖和磁盘流式加载，在现有硬件上运行前沿 MoE 模型，位列当日 GitHub Trending 第10名，新增655颗星。
- [paperclipai/paperclip](https://github.com/paperclipai/paperclip) — paperclipai/paperclip 是用于管理工作型智能体的开源应用，位列当日 GitHub Trending 第13名，新增451颗星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
