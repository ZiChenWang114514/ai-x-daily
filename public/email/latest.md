# AIxDaily · 2026-10-06

今日精选：AI × Chem 14 项，AI × Bio 15 项，AI × Math 0 项，AI Voices 4 项，Engineering 3 项。今日更新集中在生物化学研究与工程软件，数学频道暂无精选。AI×Chem 三项均为预印本，涉及酶发现、黏液溶解肽和序列可控聚合物设计；AI×Bio 含两篇预印本及一篇同行评议综述，覆盖知识图谱查询、结直肠癌空间组学与超声成像。AI Voices 收录 DeepMind 酶设计预印本公告及 OpenAI 对文本水印的公开说明；Engineering 则更新 Cloudflare OS 趋势项目和 vLLM、llama.cpp 软件版本。

## 今日重大进展

- [公开帖文称：70年数学难题 Pierce–Birkhoff 猜想获解](https://x.com/katedeyneka/status/2107161752475759011) — Kate Deyneka 在 X 发帖称，团队已解决拥有约70年历史的 Pierce–Birkhoff 猜想；该猜想位于实代数几何核心，涉及正多项式在半代数集合上的表示问题。帖子未附证明细节。
- [Google DeepMind 发布 AlphaProtein Novo：从头设计可催化定制反应的新酶](https://x.com/pushmeet/status/2107128950975529455) — Google DeepMind 团队公布 AlphaProtein Novo 预印本与代码，报告系统能生成自然界未见的新酶，在两个基准反应上达到当时最佳活性，并设计出合成哌啶药用结构、降解 DEHP 的酶。
- [vLLM v0.31.0 发布：DeepSeek V4.1-Flash 加速、推测解码与快速重启进入服务栈](https://github.com/vllm-project/vllm/releases/tag/v0.31.0) — vLLM 发布 v0.31.0，默认启用面向 DeepSeek V4.1-Flash 的 FlashMLA/NVFP4 路径，加入 Model Runner V2 推测解码、权重缓存快速重启、MoE 扩展与多模态请求安全门控。

## AI × Chem

采集 330，候选 49，精选 14。来源状态：各来源已完成

- [Iterative computational bioprospecting of hydroxymethylfurfural oxidases combining molecular simulation and machine learning](https://www.biorxiv.org/content/10.64898/2026.09.29.755274) — 研究以分子模拟、机器学习和实验反馈构成迭代式计算生物勘探流程，筛选天然 HMFO，并发现多个对 FFCA 氧化活性显著提高的候选酶。
- [Mining the cysteine-motif repertoire of airway mucins reveals redox-active mucolytic peptides](https://doi.org/10.26434/chemrxiv.15009830/v1) — 系统挖掘气道黏蛋白 MUC5B 和 MUC5AC 的邻近半胱氨酸基序，筛得具有硫醇–二硫键交换活性的黏液溶解肽，并在囊性纤维化和哮喘黏液中验证其作用。
- [Machine Learning-Accelerated Inverse Design of Sequence-Controlled Terpolymers](https://doi.org/10.26434/chemrxiv.15009833/v1) — 用受物理约束的随机模拟算法生成序列可控三元共聚物数据，再以 XGBoost 数字孪生和确定性求根优化器反推单体进料与反应性比，实现闭环逆向设计。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 712，候选 60，精选 15。来源状态：各来源已完成

- [MOSAIC: Learning Graph Node Embeddings from Spectrally Isolated Dominant Subspaces of Accumulated Diffusion Operators](https://europepmc.org/article/PPR/PPR1333536) — 提出可版本化的 ddkg.skill，帮助大语言模型可靠查询整合 NIH DDKG 生物医学知识图谱。
- [Cohort-scale Spatial Host-Microbiome Predicts Post-Resection Recurrence in Colorectal Cancer](https://www.medrxiv.org/content/10.64898/2026.09.29.26363734) — AlphaFISH 将亚细胞空间宿主—微生物组学与深度学习结合，用于结直肠癌病理特征和术后复发预测。
- [Advancing Ultrasound Beamforming With Deep Learning: A Comprehensive Review of Methods, Datasets, Benchmarks, and Computational Challenges.](https://europepmc.org/article/MED/42829544) — 综述深度学习超声波束形成的模型、数据集、基准、硬件加速和临床转化挑战。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 0，候选 0，精选 0。来源状态：各来源已完成

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 59，候选 58，精选 4。来源状态：各来源已完成

- [@pushmeet：Today, our team is sharing a preprint on our new system for generative de-novo enzyme design, AlphaProtein Novo. At @Goo](https://x.com/pushmeet/status/2107128950975529455) — Pushmeet Kohli 分享 AlphaProtein Novo 预印本：该系统用于从头设计新酶，在两个基准反应上取得当前最先进的活性，并设计出可合成哌啶药用结构、降解环境增塑剂 DEHP 的酶。
- [@OpenAI：We're expanding our approach to content provenance to include text in response to EU regulatory requirements, while reco](https://x.com/OpenAI/status/2107164650249101695) — OpenAI 表示将把内容来源追踪扩展到文本：未来几周在欧盟为符合条件的 ChatGPT 和 Codex 文本启用水印，API 用户目前可在全球范围为部分模型开启文本水印。
- [@OpenAI：Watermarks have limits. They’re often undetectable, especially in short passages. Rewriting or translating text can comp](https://x.com/OpenAI/status/2107164653147340988) — OpenAI 说明文本水印的已知局限：短文本中可能难以检测，改写或翻译可完全去除水印，因此检测器暂时只向获批研究者开放，并将持续评估改进。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 55，候选 54，精选 3。来源状态：各来源已完成

- [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) — Cloudflare OS 是构建在 Cloudflare Workers 上的智能体工作空间，用于创建文档、构建应用，并让智能体接入企业上下文与系统；2026-10-06 位列 GitHub Trending 第10名，当日新增102星。
- [v0.31.0](https://github.com/vllm-project/vllm/releases/tag/v0.31.0) — vLLM 发布 v0.31.0，加入 DeepSeek V4.1-Flash 等模型的硬件加速路径、Model Runner V2 推测解码、快速重启、KV 缓存与大规模 MoE 服务优化，并增加请求级多模态参数保护等安全限制。
- [v0.6.0](https://github.com/ggml-org/llama.cpp/releases/tag/v0.6.0) — llama.cpp 发布 v0.6.0，新增扩展批处理 API、GLM-5.3-Flash 与 Clef 决策模型支持、Qwen4Exp 的 MTP 推测解码，并提供 /v1/systemone 决策模型接口；同时更新 Hugging Face 模型下载链路和 Metal/Vulkan 稀疏注意力内核。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
