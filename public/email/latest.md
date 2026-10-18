# AIxDaily · 2026-10-19

今日精选：AI × Chem 8 项，AI × Bio 13 项，AI × Math 6 项，AI Voices 10 项，Engineering 4 项。今日五频道前三项显示，研究侧以预印本为主：化学聚焦 RNA‑配体位点、可扩展酶检索与复杂活性位点设计；生物关注可追溯药物再利用、分子编码和边缘细胞分割；数学侧评测程序性幻觉、代理鲁棒性与科研判断。AI Voices收录X上的公开观点，涉及嵌入模型基准、O‑kRystal及Harness²；工程侧则有vLLM v0.32.0软件发布和两个GitHub趋势项目。当前前三项未包含同行评议论文。

## 今日重大进展

- [X 帖文称 Google 开源 Harness²，智能体可按任务自我改写 harness](https://x.com/akshay_pachaar/status/2111753928031531232) — X 帖文介绍 Google 开源 Harness²：代理在不改模型权重的情况下，按任务改写提示、工具、记忆、技能和子代理组合；帖文称其在 Gemini 3.5 Flash、GLM-5 的多类工作基准上一轮即超过原始配置。
- [O-kRystal 以低成本 PBE 信息校正近 6000 种材料的超越 DFT 能带](https://x.com/AnimaAnandkumar/status/2111579335161520630) — 研究者公布 O-kRystal：E(3) 等变图神经网络用低成本 PBE 轨道信息校正电子态、预测 HSE06 能带；帖文称其覆盖近 6000 种三维材料，在强关联材料基准将 PBE 能带能量 MAE 降低 68.7%。
- [EzHit 将酶–反应检索扩展到 3000 万条宏基因组序列并完成实验验证](https://www.biorxiv.org/content/10.64898/2026.10.15.759509) — bioRxiv 预印本提出 EzHit 双向酶–反应检索框架，以几何置信度筛选候选；作者在近万亿规模 OMG_Prot50–RHEA 检索中保留 3027 万条序列的 82 亿个反应关联，并对优先候选完成活性实验验证。

## AI × Chem

采集 1289，候选 60，精选 8。来源状态：各来源已完成

- [LigRNA: High-accuracy prediction of RNA-ligand binding sites via dynamic chemical complementarity and language model encoding](https://www.biorxiv.org/content/10.64898/2026.10.15.759315) — LigRNA 通过结构引导的语言模型嵌入、RNA 物理化学特征、配体分子图和跨注意力联合预测 RNA-配体结合位点，在 TE9 和 TE18 数据集上优于 GATRsite。
- [Scalable Enzyme Reaction Retrieval Enables Metagenomic Biocatalyst Discovery](https://www.biorxiv.org/content/10.64898/2026.10.15.759509) — EzHit 是一个轻量级的双向酶-反应检索框架，用于酶注释、孤儿反应检索和家族特异性微调，并以 Mahalanobis 距离几何置信度筛选大规模宏基因组候选酶；作者还对优先候选进行了活性实验验证。
- [Complex enzyme active site scaffolding by iteratively detuned catalytic guidance](https://www.biorxiv.org/content/10.64898/2026.10.02.756307) — CaGE 交替进行约束引导的结构预测和序列设计，并逐轮减弱约束；它通过 RF3、classifier-free guidance 和无需训练的 motif guidance 设计复杂酶活性位点，并以独立 AF3 预测、活性位点替换和 2.7[A] 晶体结构支持设计机制。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1968，候选 60，精选 13。来源状态：各来源已完成

- [RePurpose: An LLM-Assisted, Source-Traceable Drug Repurposing Tool with Retrospective Validation on Clemastine in Multiple Sclerosis](https://europepmc.org/article/PPR/PPR1343903) — RePurpose是一个可追溯来源的LLM辅助药物再利用工具，并以多发性硬化中的clemastine进行回顾性验证。
- [A systematic investigation of molecular encoding methods for drug property predictions across neural network and Transformer encoder-based model](https://europepmc.org/article/PPR/PPR1343052) — 系统比较多种分子编码在神经网络和Transformer模型药物性质预测中的作用，并分析内在注意力可解释性。
- [Entropy-driven adaptive neural architecture search for cell segmentation on edge devices](https://europepmc.org/article/PPR/PPR1343720) — 提出熵驱动、硬件感知的神经架构搜索，用于资源受限边缘设备上的细胞图像分割。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 468，候选 60，精选 6。来源状态：各来源已完成

- [DialFork: Going Beyond Factuality to Evaluate Procedural Hallucination in Conversational Agents](https://arxiv.org/abs/2610.21561v1) — 提出 DialFork 基准，通过受控分叉对话构造程序性幻觉，并用 FlowKL、FlowScore 评估对话流程偏离。数据覆盖 24 个任务、12 个领域和 36,278 段对话，FlowScore 在 7 个编码器上优于基线。
- [AgentPerturb: Evaluating LLM Agent Robustness under Controlled Interaction Perturbations](https://arxiv.org/abs/2610.21624v1) — 提出 AgentPerturb，用二维扰动框架系统评估 LLM 代理在 APEX-Agents 和 Toolathlon 中的鲁棒性，并分析扰动导致的失败机制与计算成本。
- [SciΠvot: Benchmarking Principal-Investigator Judgment at Pivotal Moments of Scientific AutoResearch Agents](https://arxiv.org/abs/2610.21082v1) — 构建 SciΠvot 科学判断基准，从 26 个项目、6 个科学领域和 6 个月的代理研究记录中提取 248 个由资深研究者纠正的决策案例，并比较模型与研究人员的判断。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 79，候选 60，精选 10。来源状态：各来源已完成

- [@cohere：Some strong embeddings models have been released recently. Ours is still better. We benchmarked Embed 5 Fast against Goo](https://x.com/cohere/status/2111544722535645187) — Cohere 声称 Embed 5 Fast 在 163 个数据集的 RCP-nDCG@10 评测中，于超过 95% 的数据集领先 EmbeddingGemma 2；这是发布方自报的基准结果。
- [@AnimaAnandkumar：Can we predict electronic bands beyond DFT across different systems? We introduce O-krystal, a periodic E(3)-equivariant](https://x.com/AnimaAnandkumar/status/2111579335161520630) — Anima Anandkumar 介绍 O-kRystal：利用低成本 PBE 计算的轨道信息，训练周期性 E(3) 等变图神经网络来校正电子态，并在约 6000 种材料上预测 HSE06 能带。
- [@akshay_pachaar：Google just open-sourced Harness². (turn any harness into a self-improving system) a harness is everything wrapped aroun](https://x.com/akshay_pachaar/status/2111753928031531232) — 帖文介绍 Google 开源 Harness²：让代理在模型权重不变的情况下，按任务自行修改系统提示、工具、记忆、技能和子代理等 harness 组件，并称其在多类工作基准上一轮修改就超过原始配置。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 66，候选 60，精选 4。来源状态：各来源已完成

- [v0.32.0](https://github.com/vllm-project/vllm/releases/tag/v0.32.0) — vllm v0.32.0 发布：新增结构化决策与通用解析器、低精度 KV 缓存、Model Runner V2 和多项启动及调度优化，并扩展模型与多模态支持；同时修复三项安全问题。
- [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) — akitaonrails/ai-memory 当日位列 GitHub Trending 第6名，新增513星；项目为编码 CLI 智能体提供长期记忆，并支持不同智能体厂商之间交接。
- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) — Comfy-Org/ComfyUI 当日位列 GitHub Trending 第13名，新增155星；项目以图/节点界面组织扩散模型工作流，并同时提供 GUI、API 和本地后端。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
