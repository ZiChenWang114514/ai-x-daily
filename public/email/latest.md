# AIxDaily · 2026-08-26

今日精选：AI × Chem 16 项，AI × Bio 15 项，AI × Math 10 项，AI Voices 8 项，Engineering 1 项。今日五个频道同为 2026-08-26。化学与生物重点均为预印本：前者涵盖本体引导分子生成、可编程 DNA 编码库与相互作用能预测，后者聚焦冠脉造影、多模态肿瘤表征和 EEG。数学频道三项也均为预印本；观点频道收录公开帖文及预发布教程，工程频道仅保留 llama.cpp v0.3.0 软件发布。相关研究结论仍有待同行评议或实际部署进一步检验。

## AI × Chem

采集 1512，候选 60，精选 16。来源状态：各来源已完成

- [Ontology-guided deep reinforcement learning for site-specific construction of lead compounds representing coal macromolecular active sites](https://doi.org/10.26434/chemrxiv.15007798/v1) — 该研究以实验表征约束六桥焦煤大分子模型，并将局部位点模型化合物的选择转化为本体知识驱动的强化学习生成任务；EF-GRL在四类官能团位点上获得了优于传统同系物的二维结构与三维静电势相似性。
- [DNA Directed Chemistry: Scalable Programmed DNA-Encoded Library Synthesis for More Chemically Diverse and Drug-Like Libraries](https://doi.org/10.26434/chemrxiv.15007812/v1) — 该研究提出Programmed DEL Synthesis（PDS），以DNA主动指导的sort-and-pool路线构建非组合式DNA编码化合物库，并用三步、三路径的Library i01及Carbonic Anhydrase（BCA-II）筛选验证编码和建库保真度。
- [σ-hat: A physics-informed model for accurate prediction of halogen, chalcogen, pnictogen and tetrel bond energies](https://doi.org/10.26434/chemrxiv.15007826/v1) — σ-hat以低成本几何和原子特征预测卤键、硫族键、氮族键和四价族键的高水平相互作用能；在SHEF1552和SH250×10上分别获得0.85 kcal mol−1 RMSE和0.80 kcal mol−1 MAE。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2378，候选 60，精选 15。来源状态：各来源已完成

- [A Vision-Language Model for Coronary Angiography Interpretation and Clinical Decision Support](https://www.medrxiv.org/content/10.64898/2026.08.11.26360095) — CAG-MIND 将多视角冠状动脉造影视频与手术报告语义配对预训练，并在内部及独立外部队列的 11 项下游任务中评估零样本迁移和监督微调表现。
- [A Multimodal Foundation Model for Longitudinal Patient Representation and Scalable Insight Generation in Oncology](https://arxiv.org/abs/2608.24688v1) — oFM 在 167 万例真实世界肿瘤患者的纵向临床、DNA、RNA 和 H&E 病理资料上训练，以患者状态嵌入支持预后和比较治疗分析。
- [Taming foundation model with invariance-oriented pre-training for broad-spectrum EEG analysis across signal-level, brain-state, and brain-health tasks](https://arxiv.org/abs/2608.24597v1) — INCEPT 以不变性导向的预训练方式，从超过 11,000 小时无标注临床 EEG 中学习可复用表征，并在覆盖信号、脑状态和脑健康的 10 个数据集上测试。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 861，候选 60，精选 10。来源状态：各来源已完成

- [Autonomous Mathematical Discovery in an Open-World Multi-Agent Environment](https://arxiv.org/abs/2608.23691v1) — Station 在无中心协调者的开放式多智能体环境中进行数学探索，并公开对话、证明和验证代码。作者报告它在 12 个 AlphaEvolve 构造问题及两个案例中得到若干相对既有文献的新结果。
- [Discovering Cross-Language Reasoning Invariance in LLMs with Geometry-Invariant Sparse Autoencoders](https://arxiv.org/abs/2608.23809v1) — 该研究以 MGSM 的六种语言推理轨迹考察跨语言数学推理表征，并用激活互换检验共享特征是否真正可替代。结果显示，几何相似度升高并不稳定地意味着功能可替代。
- [EMRB: A Multi-Level Benchmark for Evaluating LLM Reasoning over Raw Electromagnetic Signals](https://arxiv.org/abs/2608.24086v1) — EMRB 用仅含原始 I/Q 捕获的数据测试模型能否通过编写和运行代码完成电磁信号分析；其 200 道题目具有已验证的标准答案，并比较 14 个 LLM。ReconPilot 在 15 个骨干模型组合中的 13 个带来提升。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 62，候选 60，精选 8。来源状态：各来源已完成

- [@ben_burtenshaw：Been working on this a while, and super happy to share the first few pre-release chapter of this book on post-training. ](https://x.com/ben_burtenshaw/status/2092258193632297315) — Ben Burtenshaw 发布了《Post-Training AI》的前两章草稿，内容包括用原生 PyTorch 实现 SFT 和 GRPO。作者将其定位为帮助初学者建立后训练直觉的实践材料；编辑认为，代码规模和免费 GPU 的设定使其具备较强的可复现教学价值，但内容仍处于未编辑的预发布阶段。
- [@AndrewYNg：OpenWorker -- an open source agent that doesn't just chat but completes tasks on your laptop -- just released a new vers](https://x.com/AndrewYNg/status/2092315079576555806) — Andrew Ng 宣布 OpenWorker 新版本加入代码漏洞、依赖供应链注入和云配置攻击面的安全检查智能体，并称其编排软件完全开源、可在本地运行开放权重模型。上述功能与隐私收益均为作者声明；编辑认为，围绕智能体编排层可审计性的讨论具有实际工程意义。
- [@percyliang：The fact that Simile’s first technical blog post is about confidence is notable. Confidence is paramount to simulation. ](https://x.com/percyliang/status/2092302845987225809) — Percy Liang 评价 Simile 首篇技术博客聚焦置信度这一选题很重要，并区分了总体评测与逐查询的实时置信度估计。这是研究者对模拟系统可靠性的观点；编辑认为，它把“平均表现良好”与“此刻结果可否采用”的差别说得清楚。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 44，候选 42，精选 1。来源状态：各来源已完成

- [v0.3.0](https://github.com/ggml-org/llama.cpp/releases/tag/v0.3.0) — ggml-org/llama.cpp 发布 v0.3.0，新增 dots3-note 多模态模型与 DSA-ISWA KV cache，支持 GLM-4.5-Air 的 MTP、DeepSeek 4 的 `-sm tensor` 张量切分，并将 ggml 升级至 v0.22.0；同时改进多模态处理、服务器调试和聊天界面。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
