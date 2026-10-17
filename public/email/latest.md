# AIxDaily · 2026-10-18

今日精选：AI × Chem 7 项，AI × Bio 13 项，AI × Math 9 项，AI Voices 10 项，Engineering 1 项。今日五频道均为 2026-10-18。AI×Chem 关注亲和力预测、测定感知建模和药物再利用；AI×Bio 聚焦免疫治疗耐药、卵巢癌糖组学与单细胞模型；AI×Math 探索持续学习、评测不确定性和多智能体聚合。前三个频道所列均为预印本，未见同行评议论文。AI Voices 汇集 X 公开观点或厂商公告，Engineering 仅有一项 GitHub Trending 软件项目，未指向具体 Release。

## 今日重大进展

- [CRADLE-1 报告将多模态蛋白质先导优化接入实验闭环](https://www.biorxiv.org/content/10.64898/2026.03.06.710001) — 预印本提出 CRADLE-1 自动化蛋白质工程框架，结合蛋白质语言模型、进化微调和实验室闭环，在抗体、肽、酶、CRISPR 与疫苗等模态上优化多个属性；作者报告体外验证所需湿实验轮次较理性设计减少 4–7 倍。
- [少量数据投毒即可重定向蛋白质设计模型生成](https://arxiv.org/abs/2610.21200v1) — 预印本测试两类数据投毒：向 ProtGPT2、ProGen2 预训练语料注入触发序列，或向检索库插入恶意记录；递增暴露下最早约 200 条污染样本即可触发，检索攻击还可在 97% 自由文本请求中占据 top-16。

## AI × Chem

采集 1214，候选 60，精选 7。来源状态：各来源已完成

- [Exploring the Upper Boundaries of Distance-Based Protein-Ligand Binding Affinity Prediction: Accuracy Improvements via Linear Regression and Artificial Neural Networks](https://www.biorxiv.org/content/10.1101/2025.10.07.680851) — 提出允许距离变量幂指数自由优化的蛋白质–配体结合亲和力与结合能预测策略，将优化后的距离描述符与线性回归、人工神经网络结合，在 PDBbind version 2024 高质量数据集上训练和验证；混合模型的 Pearson 相关系数 R 达到 0.800–0.900，并超过既有线性和机器学习评分函数。
- [Benchmarking Large Language Models for Assay-Aware Drug-Target Binding Affinity Prediction](https://www.biorxiv.org/content/10.64898/2026.10.11.758217) — 研究自然语言测定描述是否能在分子和蛋白质表征之外提供药物–靶点结合亲和力预测信息，并提出 ACL-DTI 与 MAMMAL-AsAP 两种测定感知模型；在五个 triplet-disjoint 随机划分上，MAMMAL-AsAP 的最高 R^2 为 0.7198 +/- 0.0085，掩码实验还显示 ACL-DTI 对不完整测定描述具有较强稳健性。
- [RePurpose: An LLM-Assisted, Source-Traceable Drug Repurposing Tool with Retrospective Validation on Clemastine in Multiple Sclerosis](https://www.biorxiv.org/content/10.64898/2026.10.14.759218) — 推出 RePurpose 网页工具，将 Open Targets、ClinicalTrials.gov、UniProt 和 PubMed 等来源与大语言模型结合，根据自然语言目标筛选并排序候选药物；以多发性硬化症中的 clemastine 为例进行回顾性验证，工具能在机制措辞查询中稳定找回 clemastine，但未能通过疾病措辞查询发现它。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1891，候选 60，精选 13。来源状态：各来源已完成

- [Multimodal profiling for prediction of primary resistance to anti-PD-(L)1 therapy in advanced non-small-cell lung cancer: the prospective PIONeeR biomarkers study](https://www.medrxiv.org/content/10.64898/2026.01.09.26343779) — PIONeeR 前瞻性多中心研究整合六个生物学层面的基线数据，评估晚期 NSCLC 对 anti-PD-(L)1 治疗原发耐药的预测。
- [Glycomics Profiling Reveals a Stromal Chondroitin-4-sulfate State that Shapes Platinum Response in Ovarian Cancer](https://www.biorxiv.org/content/10.1101/2025.10.06.675352) — 糖组学、单细胞转录组和 PDX 实验证实，基质软骨素-4-硫酸（C4S）状态与卵巢癌铂类反应相关。
- [Panoramic modelling of single-cell transcriptomes at scale with CellNet](https://arxiv.org/abs/2610.21943v1) — CellNet 将 DNA 来源的基因身份与 RNA 表达编码到共享图像表示中，并在 40 个物种的 2.31 亿细胞谱系上预训练。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 468，候选 60，精选 9。来源状态：各来源已完成

- [Functional Subnetwork Localization for Efficient Continual Learning in Large Language Models](https://arxiv.org/abs/2610.21537v1) — 提出 Function-isolated Memory-Efficient Optimization（CiMEO），先用梯度归因定位功能子网络，再将每个训练样本路由到相应子网络，仅更新选定区域的参数和优化器状态。在 140 万条顺序指令及五个生成式基准上报告了较高平均性能，并分析了子空间重叠与主角度。
- [Rubric Judgments Lack Uncertainty: Conformal Weighting for LLM Evaluation](https://arxiv.org/abs/2610.21214v1) — 提出 Uncertainty-aware Rubric Weighting（URW），用 conformal calibration 估计评分规约各标准的判断不确定性，再通过 split-conformal p-values 生成带覆盖保证的标准权重。实验显示其能提升成对偏好准确率和后续 RL 对齐效果。
- [Bias Control and Injection for Multi-Agent Aggregation](https://arxiv.org/abs/2610.21290v1) — 研究多智能体聚合中的非语义偏差，提出测试时聚合框架：对不同答案展示风格归一化的推理轨迹，并将初始选择置于少数位置以注入偏差、观察决策不稳定性。该方法在三个数学推理基准和四种异构 LLM 组合上报告了更高准确率与更高 token 效率。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 83，候选 60，精选 10。来源状态：各来源已完成

- [@haofeiyu44：How to build sample-efficient RL algorithms for long-horizon language agents? Our answer: Just ONE additional loss on to](https://x.com/haofeiyu44/status/2111158324984991902) — Haofei Yu 报告称：在 GRPO 之上增加一个多步动作预测损失后，5 个长程智能体基准的样本效率最高可提高 2 倍。
- [@NVIDIAAI：Building safer AI agents takes more than model safeguards. @perplexity_ai open sourced SPACE, the agent sandbox platform](https://x.com/NVIDIAAI/status/2111488462264410553) — NVIDIA AI 宣布，Perplexity 已开源 SPACE，这是支撑 Computer 的智能体沙箱平台，可控制智能体运行代码的位置及其可访问资源。
- [@NVIDIAAI：And @AIatMeta went live with Muse Spark Open! The 816B model was trained on NVIDIA GB300 NVL72. Its 1M-token context win](https://x.com/NVIDIAAI/status/2110799083749495190) — NVIDIA AI 介绍 Muse Spark Open：816B 参数模型在 GB300 NVL72 上训练，支持 100 万 token 上下文；Meta 还提供面向 Blackwell Ultra 的 NVFP4 检查点，宣称单 GPU 吞吐超过每秒 5 万 token。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 62，候选 55，精选 1。来源状态：各来源已完成

- [stablyai/orca](https://github.com/stablyai/orca) — Orca 用于管理一组编码智能体，可在桌面端、移动端和远程运行时中运行 Grok Bot、Claude Code 等代理，并支持终端、工作树和多代理编排。当日 GitHub Trending 排名第 8，新增 829 星，累计 95,318 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
