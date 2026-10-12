# AIxDaily · 2026-10-13

今日精选：AI × Chem 13 项，AI × Bio 14 项，AI × Math 0 项，AI Voices 7 项，Engineering 2 项。今日五频道有两条主线：AI×Chem 与 AI×Bio 各选三项，均为 ChemRxiv、bioRxiv 或 Europe PMC 标注的预印本，覆盖环肽设计、PFAS 质谱库、膜蛋白界面和空间转录组；AI Voices 汇总 X 公开帖文，涉及研究世界模型、ReplaySSM 和结构化决策，不等同同行评议结论；Engineering 为 GitHub Trending 仓库动态。AI×Math 今日没有足够高质量更新。

## 今日重大进展

- [研究者公布 Lean 形式化的 Vaught 猜想反例](https://x.com/cameronfreer/status/2109268549130674453) — 研究者 Cameron Freer 公布一项形式化结果，称其在 Lean、mathlib 与自建 infinitary-logic 库中构造了无穷逻辑版本 Vaught 猜想的反例，并公开证明策略与可复用代码。
- [ReplaySSM 从论文机制进入 GLM 与主流推理栈生产部署](https://x.com/zwljohnny/status/2109679465609470216) — 研究者 Ze‑Wei Liou 称 ReplaySSM 已在 GLM‑5.3‑Flash、Kimi‑K3 生产运行，并进入多套主流推理框架；标准解码最高提速1.47倍，推测解码最高2.1倍。
- [CP‑GFM‑SGX 以实验反馈把 KRAS 环肽亲和力优化至约 1 μM](https://doi.org/10.26434/chemrxiv.15010253/v1) — ChemRxiv 预印本提出 CP‑GFM‑SGX，将拓扑感知全原子生成、受体条件结构评估和证据状态机合并，并以 SPR/BLI 反馈把 KRAS G12D 环肽报告亲和力从约 60 μM 优化到约 1 μM。

## AI × Chem

采集 585，候选 60，精选 13。来源状态：各来源已完成

- [CP-GFM-SGX: Topology-Aware Cyclic Peptide Generation and Design with Receptor-Conditioned Structural Evaluation and Experimental KRAS Affinity Optimization](https://doi.org/10.26434/chemrxiv.15010253/v1) — 提出面向受体的拓扑感知环肽生成系统CP-GFM-SGX，将全原子生成模型与Unified Evidence State Machine（UESM）结合，并通过结构基准、故障注入测试及KRAS G12D实验反馈验证设计流程。
- [FMS2Lib: A Machine Learning-Ready Tandem Mass Spectral Library for Nontargeted Analysis of Non-conventional PFAS](https://doi.org/10.26434/chemrxiv.15010212/v1) — 建立包含34,686种含氟类药物化合物串联质谱的FMS2Lib库，并将其用于非靶向PFAS的机器学习分子式预测和结构注释。
- [CHORUS: A proteome-scale atlas of membrane interaction interfaces constructed using cross-protein language model embeddings from sequences alone](https://www.biorxiv.org/content/10.64898/2026.10.04.756538) — 提出仅依赖序列的膜蛋白相互作用界面预测框架CHORUS，整合不同蛋白语言模型和层深表示，构建覆盖80,619种跨膜蛋白的残基分辨率交互图谱。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1328，候选 60，精选 14。来源状态：各来源已完成

- [Development of a Multimodal Large Language Model for Early Warning and Diagnosis of Dry Eye Disease](https://europepmc.org/article/PPR/PPR1338533) — 基于 Qwen2-VL 的多模态大语言模型 DED-MLLM，整合问卷、眼科影像和临床检查数据，在 874 名参与者及三个中心的外部队列上完成干眼病早期预警和诊断验证。
- [Coordinated Enhancement of Molecular and Spatial Fidelity for Biological Inference in Spatial Transcriptomics](https://www.biorxiv.org/content/10.64898/2025.12.23.696267) — FOCUS 是融合空间转录组、组织学、细胞掩膜、scRNA-seq 参考和空间共表达先验的多模态生成基础模型，用于协同提升空间转录组的分子定量和空间定位保真度。
- [Representing biological concepts as directions in foundation model embeddings](https://www.biorxiv.org/content/10.64898/2026.10.10.758204) — 概念激活向量（CAV）把蛋白质和单细胞基础模型嵌入中的生物学属性表示为可解释、可复用的方向，并恢复 GO、EC、Pfam、DNA 结合和癌症表达转变等特征。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 0，候选 0，精选 0。来源状态：各来源已完成

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 48，候选 45，精选 7。来源状态：各来源已完成

- [@rohanpaul_ai：New Amazon paper shows that an LLM can act as a research world model, predicting whether a training change will help bef](https://x.com/rohanpaul_ai/status/2109243398628708619) — 事实：Rohan Paul 转述亚马逊研究，研究者用大型语言模型预测训练改动在实际运行前可能带来的收益。作者称，该方法在2653条、9个设置的真实实验记录上测试，并在5个设置中将平均排名相关性从0.506提高到0.774。
- [@zwljohnny：ReplaySSM now runs in production in GLM-5.3-Flash and Kimi-K3, and ships in TensorRT-LLM, vLLM, FlashInfer, and SGLang! ](https://x.com/zwljohnny/status/2109679465609470216) — 事实：Ze-Wei（Johnny）Liou 表示 ReplaySSM 已在 GLM-5.3-Flash 和 Kimi-K3 中投入生产，并进入 TensorRT-LLM、vLLM、FlashInfer 与 SGLang。作者报告标准解码最高提速1.47倍、推测解码最高提速2.1倍。
- [@mrm8488：🧭 New model: Typed Decision, built on EmbeddingGemma 2 Give it a state + any schema of questions → typed, calibrated ans](https://x.com/mrm8488/status/2109406679045423394) — 事实：Manu Romero 介绍 Typed Decision 模型，称其基于 EmbeddingGemma 2，可直接输出类型化、校准后的决策结果。在 typed-decisions 评测上得分76.4%，比27B语言模型低约6个百分点，但参数量约少100倍。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 9，候选 9，精选 2。来源状态：GitHub Releases: TimeoutError: The read operation timed out

- [microsoft/BitNet](https://github.com/microsoft/BitNet) — 微软 BitNet 是面向 1-bit 大语言模型的官方推理框架，今日 GitHub Trending 第 8 名，新增 134 星，总星标 40,879。
- [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) — Alishahryar1/free-claude-code 将 Claude Code、Codex、VSCode、Pi、OpenCode 等多种 coding harness 汇聚到终端、应用、IDE、手机和浏览器，今日 GitHub Trending 第 9 名，新增 705 星，总星标 58,992。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
