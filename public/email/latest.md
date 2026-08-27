# AIxDaily · 2026-08-27

今日精选：AI × Chem 12 项，AI × Bio 14 项，AI × Math 8 项，AI Voices 8 项，Engineering 6 项。今日五个频道均有精选。研究侧以预印本为主：化学关注对接后筛选，生物涉及心衰风险预测与多轮诊断评测，数学聚焦可机检的优化建模验证。AI Voices 收录机构公开帖文，相关性能和事故信息仍待原始报告佐证；工程频道则是可用的软件发布，升级前应阅读兼容性说明。

## AI × Chem

采集 1250，候选 60，精选 12。来源状态：bioRxiv: RuntimeError: Unable to fetch https://api.biorxiv.org/details/biorxiv/2026-08-24/2026-08-27/0:

- [Hit-Triage Pretrained Transformer (Hit-TPT), an Interaction-Agnostic Graph-Transformer for Post-docking Enrichment](https://doi.org/10.26434/chemrxiv.15007932/v1) — Hit-TPT 以蛋白–配体相互作用图为输入，结合物理信息原子特征与 3D 位置编码，用于对接后筛选的真结合物优先级排序；在 DUD-E 的 77/25 靶标严格划分中报告 EF1%=42，并通过跨靶标分析检验其是否学习到真实相互作用。
- [A Hierarchical Synergistic Deep Learning Framework Integrating Composition, Structure, and Ionic Transport for Solid-State Electrolyte Discovery](https://arxiv.org/abs/2608.25592v1) — 该研究构建由组成、结构和离子输运模块协同的深度学习筛选流程，在 30,364,908 个 Alex/ICSD 候选中识别 97 种高性能固态电解质，并以独立实验数据核对卤化物候选的高电导结构区域。
- [Explain and Go Beyond with Surfacia: A Surface-Descriptor based Workflow for Interpretable Molecular Machine Learning](https://doi.org/10.26434/chemrxiv.15007949/v1) — Surfacia 将波函数导出的分子表面描述符、紧凑模型、SHAP 解释和候选可视化整合为自动流程，并在 CO2RR 改性剂、有机催化剂系列及 ESOL 上考察可解释预测和有限实验预算下的候选优先级选择。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2061，候选 60，精选 14。来源状态：bioRxiv: RuntimeError: Unable to fetch https://api.biorxiv.org/details/biorxiv/2026-08-24/2026-08-27/0:；medRxiv: URLError: 

- [Personalized Knowledge-based Graph Neural Networks and Regression Analysis for Computational Diagnosis of High-Risk Cardiovascular Disease Patients](https://europepmc.org/article/PPR/PPR1305997) — 以个体化知识图谱 GNN 预测心肌梗死后心力衰竭风险，并分析 empagliflozin 治疗反应。
- [MTDiag: A Multi-Turn Diagnostic Dataset Towards Clinically Meaningful LLM Evaluation](https://arxiv.org/abs/2608.25085v1) — MTDiag 提供由医生验证的多轮诊断对话数据集及临床知识导向评估指标。
- [CytoGate-Bench: an LLM benchmark for cross-panel cell gating in cytometry](https://europepmc.org/article/PPR/PPR1305902) — CytoGate-Bench 将跨抗体面板的细胞术人工门控转化为零样本 LLM 基准。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 1061，候选 60，精选 8。来源状态：各来源已完成

- [FLARE: Verifying MILP Reformulations with LLM-Based Theorem Proving](https://arxiv.org/abs/2608.25220v1) — FLARE 将 MILP 重表述的等价性验证形式化到 Lean 中，并用 LLM agent 与 Lean proof assistant 对照参考表述生成机器可检验证书。
- [MathAdv: What Theorem Provers Know, Reason, Formalize, and Generalize](https://arxiv.org/abs/2608.25449v1) — MathAdv 以 Lean 4 定理证明为主任务，并用知识、非形式推理和等价改写任务诊断模型在不同数学领域的能力与稳健性。
- [PhysElite: How Far Are LLMs from Solving Olympiad-Level Physics Problems?](https://arxiv.org/abs/2608.25097v1) — PhysElite 提供 11,586 道中英双语、多模态的奥赛级物理题，并以最终答案和步骤级过程评估考察 MLLM 推理。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 65，候选 60，精选 8。来源状态：各来源已完成

- [@Alibaba_Qwen：Meet Qwen3.8-Flash, a multimodal MoE and an early preview of the Qwen4 architecture, now open-weight! The production ver](https://x.com/Alibaba_Qwen/status/2092591393424515114) — Qwen 官方发布了开放权重的 Qwen3.8-Flash，并将其描述为 Qwen4 架构的早期预览；帖文列出模型规模、上下文长度、训练成本比较和多项基准分数，这些性能与成本结论均为发布方主张。编辑认为，开放权重、较低激活参数规模与架构信息使其成为值得持续核验的重要模型发布。
- [@OpenAI：We have conducted a thorough investigation into the Hugging Face incident. We are releasing a technical report and accom](https://x.com/OpenAI/status/2092691861773160673) — OpenAI 表示已完成对 Hugging Face 事件的调查，并将发布技术报告和配套博客，内容包括重建智能体活动、分析既有安全措施失效原因及防范措施。事件细节与整改成效尚待报告正文提供证据；编辑认为，公开事故复盘对智能体安全实践具有较高参考价值。
- [@AnthropicAI：Three research groups—Stanford’s Social and Language Technologies lab, Oxford’s Human Information Processing Lab, and ME](https://x.com/AnthropicAI/status/2092661574523867302) — Anthropic 称，斯坦福 SALT Lab、牛津 Human Information Processing Lab 与 METR 三个研究组设计了独立研究，分析 2026 年 4 至 5 月间 25 万段 claude.ai 或 Claude Code 对话的聚合输出。该数据范围来自机构帖文；编辑认为，向外部团队开放隐私保护后的实际使用数据，有助于把 AI 社会影响研究延伸到实验室之外。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 58，候选 57，精选 6。来源状态：各来源已完成

- [Release: v5.16.0](https://github.com/huggingface/transformers/releases/tag/v5.16.0) — huggingface/transformers v5.16.0 新增 Qwen4-Exp、GraniteSpeech5、Step3p7、CohereCompass、ESMC 和 ESMFold2 模型支持；同时以 DTensor 原生后端替换旧 tensor-parallel 实现，并改进量化、缓存和并行推理。
- [v0.28.0](https://github.com/vllm-project/vllm/releases/tag/v0.28.0) — vllm-project/vllm v0.28.0 集中优化 Kimi-K3 与 DeepSeek V4 服务，加入更多推测解码、KV cache 分级卸载、Model Runner V2 与多硬件支持，并修复音频解码时长校验可被绕过的 DoS 问题。
- [v1.11.0](https://github.com/huggingface/trl/releases/tag/v1.11.0) — huggingface/trl v1.11.0 改用 vLLM 原生 server，新增实验性 `AsyncDistillationTrainer` 与多教师 MOPD，并加入多个模型支持和 VLM 强化学习训练修复。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
