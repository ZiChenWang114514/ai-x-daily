# AIxDaily · 2026-08-30

今日精选：AI × Chem 10 项，AI × Bio 14 项，AI × Math 6 项，AI Voices 9 项，Engineering 1 项。今日五个频道共同更新至8月30日，科研三频道以预印本为主：化学关注细胞功能预测与虚拟筛选，生物聚焦医学多模态与蛋白质组基础模型，数学侧重科研代理实验忠实度审计。AI Voices 汇集公开帖文和研究发布，涉及语音智能体、递归自我改进评测与自动化对齐；工程频道仅精选一项软件发布。各项性能与结论均应按其原始发布类型理解。

## 今日重大进展

- [Levent Alpöge 公布 S⁶ 复结构候选构造，Claude 参与生成](https://x.com/__alpoge__/status/2091639630504604060) — Levent Alpöge 公布逾百页的 S⁶ 复结构候选构造，主张通过模形式相关的复二维环面族与特殊纤维紧化，在光滑六维球面上构造复结构；Claude 参与了构造生成。
- [Anthropic 发布科研与先进制造设备控制标准 MHS 研究预览](https://x.com/AnthropicAI/status/2093038426140651791) — Anthropic 发布 Model Hardware Standard 研究预览，试图为 AI 智能体安全操作科研和先进制造设备建立通用标准。官方称，早期测试已用于药物发现、成像实验和量子计算激光稳定。
- [Pipecat 发布开放语音智能体模型 PhoneLLM Alpha 1](https://x.com/kwindla/status/2093014818647339026) — Pipecat 团队发布面向语音智能体的开放权重模型 PhoneLLM Alpha 1，提供基准、权重与部署材料。发布方主张，它在典型语音任务上达到 GPT 5.6 Terra 水平，同时延迟约为三分之一、成本约为十八分之一。

## AI × Chem

采集 918，候选 60，精选 10。来源状态：各来源已完成

- [A pretrained unified model enables cellular functional profile prediction and multi-objective virtual drug screening](https://www.biorxiv.org/content/10.64898/2026.08.25.746866) — InsilicoCell 以监督式 Transformer 预训练整合七类细胞功能任务、逾 8,800 万条测量，并用于多目标虚拟筛选；摘要报告了 c-Myc 活性抑制剂、抗纤维化剂和促干性化合物的实验验证。
- [Can SMILES be fragmented into a concatenable ordered sequence of retrosynthetically interesting string block ?](https://www.biorxiv.org/content/10.64898/2026.08.25.747180) — 研究通过穷举 SMILES 表示来构造与逆合成断键对应的可拼接字符串块，在 MOSES 的 190 万个分子中为 85%实现全部逆合成键的字符串覆盖，并测试其对 MolGPT 与 MCTS 从头设计的影响。
- [Coarse composition suffices: tabular in-context learning for multi-activity antimicrobial peptide profiling](https://www.biorxiv.org/content/10.64898/2026.08.27.747591) — 该研究以 330 个可解释序列描述符结合表格基础模型 TabPFN，在 ESCAPE 的 82,359 条抗菌肽、五标签任务上完成免训练的多活性预测，并报告 mAP-5 达 77.8%。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 972，候选 60，精选 14。来源状态：各来源已完成

- [From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation](https://arxiv.org/abs/2608.26856v1) — MedREAL：用于医学 VQA 与分割的推理驱动像素级定位框架。
- [OmicsFM brings proteomics into the foundation model era](https://www.biorxiv.org/content/10.64898/2026.08.25.747021) — OmicsFM：以大规模再处理蛋白质组数据训练的模态无关 Transformer。
- [Decoding Radiation-Induced Transcriptomic Signatures of Human Leukocytes using Long-Read RNA-Seq: Clinical and Biodosimetric Implications](https://www.biorxiv.org/content/10.64898/2026.02.04.703787) — 采用长读长 RNA-Seq 解析人白细胞辐射诱导的转录组和异构体变化。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 284，候选 60，精选 6。来源状态：各来源已完成

- [Beyond Execution: Auditing Experimental Fidelity in LLM-Driven Scientific Research](https://arxiv.org/abs/2608.26753v1) — ABE-Ralph 将论文主张、协议、必需组件、基线与指标编码为实验约束，用于审计 LLM 科研代理是否忠实复现实验。在 30 次长程复现实验中，作者报告其稳健执行率为 93%，并在 23 个 NatureBench 发现任务中的 5 项达到或超过既有最佳结果。
- [GRAIN: Bridging Name and Narrative Shifts in Real-World Graph Reasoning through Invariance-Rewarded Agentic RL](https://arxiv.org/abs/2608.27142v1) — GRAIN 以结构不变性奖励训练单代理完成文本到图结构的解析与工具执行，并以 GRIT 基准检验节点命名和叙述方式改变时的鲁棒性。作者报告：相对多代理基线，准确率提高 16.45%，延迟约降低 24%，且将 SFT 模型的 OOD 差距从 15.77% 降至 7.80%。
- [SymbolLKG: Towards Verifiable Logical Reasoning via Logical Knowledge Graph and Symbolic Solvers](https://arxiv.org/abs/2608.26836v1) — SymbolLKG 将逻辑规则和约束显式编码进 Logical Knowledge Graph，并用 Logic Router 将任务分派给符号求解器，以生成可核验的逻辑推理路径。作者称其在逻辑推理基准上优于提示和 RAG 基线。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 50，候选 43，精选 9。来源状态：各来源已完成

- [@kwindla：Introducing PhoneLLM, an open model for voice agents. GPT 5.6 Terra performance on typical voice agent tasks at 1/3 the ](https://x.com/kwindla/status/2093014818647339026) — Pipecat 团队发布了面向语音智能体的开放权重模型 PhoneLLM Alpha 1，并提供权重、基准和部署说明。作者声称，该模型在典型语音任务上可达到 GPT 5.6 Terra 的性能，同时延迟约为三分之一、成本约为十八分之一。
- [@HuaxiuYaoML：Can frontier AI agents achieve Recursive Self-Improvement by turning a weak method into one that performs better on hidd](https://x.com/HuaxiuYaoML/status/2092779580004474985) — Huaxiu Yao 宣布 RSI-Exam：该基准包含6个领域的88项可执行研究任务，并开放社区贡献任务。帖文报告，Opus 5 在88项任务的隐藏集合上以0.464的平均分居首。
- [@AnthropicAI：Claude can reliably fix measurable misalignment. But subtle or rare failures may have no benchmark at all—so everything ](https://x.com/AnthropicAI/status/2093386535618113627) — Anthropic 发布自动化对齐研究报告及研究设置。官方报告称，其自动化研究者可在可测量的对齐失效上改进安全指标；帖文同时强调，细微或罕见的失效可能缺少可用基准。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 63，候选 48，精选 1。来源状态：GitHub Trending: HTTP 404 Not Found

- [0.151.0](https://github.com/openai/codex/releases/tag/rust-v0.151.0) — openai/codex 发布 rust-v0.151.0，加入可选 MCP 服务器工具发现的可配置等待时间、扩展处理 MCP 工具结果的能力和按仓库合并的插件目录配置；并修复权限状态、模型切换、远程沙箱和 MCP 错误传递问题。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
