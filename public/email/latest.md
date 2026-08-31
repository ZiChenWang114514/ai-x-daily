# AIxDaily · 2026-08-31

今日精选：AI × Chem 14 项，AI × Bio 11 项，AI × Math 6 项，AI Voices 10 项，Engineering 10 项。今日研究面以预印本为主：化学频道关注细胞化学蛋白质组学建模，生物频道聚焦空间组学与病理图像推断，数学频道检验几何形式化和工具辅助推理。AI Voices 收录公司说明与个人经验等公开观点，其中基准表现仍待独立核验。工程频道则呈现多智能体课堂、架构可视化和小模型训练等 GitHub 热门开源项目，均属软件动态，并非同行评议研究结论。

## 今日重大进展

- [AI 生成的交换代数证明完成 Lean 4 形式化检查](https://x.com/BehroozParhami/status/2092867122930274783) — 一则公开帖文称，研究者将交换代数中的开放问题交给 AI，AI 生成非正式证明；团队随后把证明转写为 Lean 4 项目，并由机器检查器确认其形式化正确性。
- [Pinal 公布从自然语言描述直接设计功能蛋白的结果](https://www.biorxiv.org/content/10.1101/2024.08.01.606258) — 研究团队在预印本中公布 Pinal：这一 160 亿参数模型可由功能自然语言描述生成蛋白。在荧光蛋白、PET 水解酶、醇脱氢酶和 H-protein 四类设计中，全部产物均显示功能，两种酶实现催化周转。
- [Simular 报告 Sai 在 OSWorld 2.0 计算机使用基准取得 73%](https://x.com/SimularAI/status/2093009990663434361) — Simular 在公开帖文中报告，其计算机使用智能体 Sai 在 OSWorld 2.0 的 CUA 基准取得 73%，称其超过 Opus 5 与 GPT-5.6 Sol，并将单项任务成本降至后两者约三分之二。

## AI × Chem

采集 1404，候选 60，精选 14。来源状态：各来源已完成

- [Chemi-Proteome Language Attention Network Empowers Fragment-Based Ligand Interactome and Binding Sites Discovery with Evidence](https://www.biorxiv.org/content/10.64898/2026.08.26.747036) — C-PLANK 直接学习活细胞 FFF 化学蛋白质组学中的片段—蛋白相互作用，并以双线性注意力结合全局细胞状态与局部残基—原子信息。在 8 项研究汇集的 431 个配体互作组上，它在随机和 cold-protein 评测中优于所比较模型，且预测指纹得到结构口袋、共晶结构和细胞结合位点的旁证；一个新配体随后被验证为细胞中发挥作用的 SIRT3 激动剂化学探针。
- [Toward De Novo Protein Design from Natural Language](https://www.biorxiv.org/content/10.1101/2024.08.01.606258) — Pinal 是一个把自然语言功能描述直接生成为多样且有活性的蛋白质的 160 亿参数模型，训练使用 17 亿个蛋白质—文本对。作者从四类功能中设计蛋白；荧光蛋白、PET 水解酶、醇脱氢酶和代谢 H-protein 均有功能，其中两种酶实现催化周转，所设计 H-protein 的性能为天然对应物的 1.7 倍。
- [OmniScore: Universal Scoring of Diverse Biomolecular Complexes via Equivariant Geometry-Aware Discrete Representation Learning](https://www.biorxiv.org/content/10.64898/2026.08.28.747942) — OmniScore 以图和序列双视角编码复合物三维几何，并通过预训练的共享表示和轻量任务头服务多个结构评分任务。其在报告的抗体—抗原及纳米抗体—抗原质量评估指标上优于比较基线；冻结的残基嵌入在标准基准的功能位点准确率为 71.8%，蛋白—配体打分和排序则与专用方法相当。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 2002，候选 60，精选 11。来源状态：medRxiv: RemoteDisconnected: Remote end closed connection without response

- [RECON infers regions of interest from H&E images and reconstructs whole-slide molecular profiles at single-cell resolution](https://europepmc.org/article/PPR/PPR1308114) — RECON 从 H&E 图像选择代表性 ROI，并在单细胞尺度重建全切片转录组或蛋白质组图谱。
- [Benchmarking cell type annotation in spatial transcriptomics: resolving cellular hierarchies, biological fidelity, and dynamic cell states](https://europepmc.org/article/PPR/PPR1307536) — 一项覆盖20种方法、4种空间转录组技术和6种场景的细胞类型注释系统基准研究。
- [A Translational Platform for Brain-Computer Interfaces and Adaptive Neuromodulation: Technical Characterization, Long-Term Validation, and Implementation of the CorTec Brain Interchange--BCI2000 Ecosystem](https://www.biorxiv.org/content/10.64898/2026.08.27.747359) — CorTec Brain Interchange—BCI2000 开源生态系统完成台架、长期动物和人体概念验证。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 606，候选 60，精选 6。来源状态：各来源已完成

- [NL2AGBench: Benchmarking LLM Auto-Formalization for AlphaGeometry](https://arxiv.org/abs/2608.28481v1) — NL2AGBench 评估 LLM 将英文几何题转写为 AlphaGeometry 可执行形式化表示的能力，并以 AlphaGeometry 执行结果检验译文质量。
- [Learning to Use Tools: Reinforcement Learning for Tool-Integrated Mathematical Reasoning](https://arxiv.org/abs/2608.28447v1) — 该工作在 Countdown 数学任务中训练模型调用计算器，并以自动可验证的最终答案奖励比较多种强化学习方法。
- [Program Learning with Verifiable Rewards: Symbolic Backpropagation for Post-Training LLMs](https://arxiv.org/abs/2608.28421v1) — PLVR 将具有可验证中间步骤的推理表示为由确定性与神经原语组成的显式程序，并用类型推导实现符号反向传播。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 102，候选 60，精选 10。来源状态：各来源已完成

- [@SimularAI：Our computer-use agent @sai_borg just beat Opus 5 and GPT-5.6 Sol on OSWorld 2.0. Sai scored 73% on the CUA benchmark wh](https://x.com/SimularAI/status/2093009990663434361) — Simular 在公开帖文中称，其计算机使用智能体 Sai 在 OSWorld 2.0 的 CUA 基准获得 73%，并在该比较中超过 Opus 5 与 GPT-5.6 Sol。
- [@NVIDIAAI：Already running an inference engine? So where does NVIDIA Dynamo fit in? In five minutes, we break down how Dynamo sits ](https://x.com/NVIDIAAI/status/2093444391797158049) — NVIDIA 说明 Dynamo 如何围绕 SGLang、vLLM 和 TensorRT-LLM 等推理引擎工作，以扩展跨 GPU 与跨节点推理。
- [@guansi：我一直建议，想真正学大模型的人，最好自己本地部署一次。 这是给大模型祛魅最快的方法。 平时我们在网页里用 ChatGPT、Claude，很容易产生一种错觉：后面好像藏着一个会思考、会记忆、会使用工具的“智慧大脑”。 但你真把一个模型下载下来](https://x.com/guansi/status/2093350155043135915) — 管四以个人部署经验建议学习者亲自本地运行模型，并指出 API、上下文、并发、显存、量化与工具调用等环节能帮助理解模型系统。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 83，候选 60，精选 10。来源状态：各来源已完成

- [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) — THU-MAIC/OpenMAIC 是一键部署的多智能体互动课堂系统，当天位列 GitHub Trending 第 1 名，新增 1,370 星。
- [tt-a1i/archify](https://github.com/tt-a1i/archify) — tt-a1i/archify 为编码智能体生成可验证的软件架构、工作流、时序和数据流图，并输出可独立打开的动态 HTML；当天位列 GitHub Trending 第 2 名，新增 3,722 星。
- [jingyaogong/minimind](https://github.com/jingyaogong/minimind) — jingyaogong/minimind 提供从零训练小型语言模型的教学型实现，目标是在约 2 小时内训练 6,400 万参数模型；当天位列 GitHub Trending 第 6 名，新增 472 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
