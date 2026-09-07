# AIxDaily · 2026-09-07

今日精选呈现“科研预印本与工具动态并行”的格局：化学侧聚焦新抗原排序和抗菌肽预测，生物侧涵盖肿瘤表观治疗、显性遗传病编辑及阿尔茨海默病单核图谱，均为预印本，尚待同行评议与独立验证。AI Voices 同时收录第三方预发布评测、研究者公开观点和模型方官方发布；工程频道则是 GitHub Trending 的开源项目快照，不能等同于软件正式发布。数学频道今日没有足够高质量更新。

## 今日重大进展

- [OpenAI 发布 GPT-6 Astra，并上线 GPT-6 Pro](https://openai.com/index/gpt-6-astra) — OpenAI 发布 GPT-6 Astra，称其为新一代智能模型，重点覆盖计算机操作、编程、网络安全与科学任务；该模型已通过 GPT-6 Pro 向 Pro、Business 和 Enterprise 用户提供。
- [Anthropic 报告 Claude 用 11 天自主形式化费马大定理证明](https://x.com/Vashishtrv/status/2096017675713679438) — Anthropic 报告称，Claude 在约 11 天内大体自主地将费马大定理的既有证明写成 Lean 形式化证明。该工作没有提出费马大定理的新解法，而是推进了对其完整机器可检验证明的构建。
- [Allen AI 公布大气—海洋耦合气候模拟器 SamudrACE-E3SMv3](https://x.com/allen_ai/status/2095948629160665410) — Allen AI 与 E3SM 团队公布 SamudrACE-E3SMv3：将大气与海洋机器学习模拟器耦合，使二者在运行中相互反馈。其报告称，单张 H100 每天可模拟约 1,100 年气候，而 E3SM 约需 105 个节点模拟 28 年。

## AI × Chem

采集 1172，候选 60，精选 2。来源状态：各来源已完成

- [DeepPROTECTNeo: A Context-aware Personalized and Reverse Vaccinology-guided Deep Learning Framework for Immunogenicity Prediction](https://www.biorxiv.org/content/10.1101/2025.01.04.631301) — DeepPROTECTNeo 将变异检测、HLA 分型、pMHC 亲和力预测、TCR 谱挖掘和 TCR–表位结合预测串为端到端个体化新抗原优选流程；在严格 TCR 划分下报告 AUROC 0.7856、AUPRC 0.7932，并在患者队列中找回34个已验证高亲和力新表位中的18个。
- [Coarse composition suffices: tabular in-context learning for multi-activity antimicrobial peptide profiling](https://www.biorxiv.org/content/10.64898/2026.08.27.747591) — 该研究以330个可解释的序列描述符和 TabPFN 构建无需梯度训练的多标签抗菌肽活性预测流程。在 ESCAPE 的82,359条肽、5个标签上，模型达到 mAP-5=77.8%，并通过消融显示少量全局理化特征已可恢复大部分性能，尤其改善远缘同源肽的预测。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixchem/)

## AI × Bio

采集 1877，候选 60，精选 12。来源状态：各来源已完成

- [Cell cycle control of chromatin creates a therapeutic window for epigenetic therapy in tumors](https://www.biorxiv.org/content/10.64898/2026.09.03.748889) — 研究以 AML 为模型，提出延长 G1 期可重塑染色质状态，并通过药物与 CRISPR-Cas9 筛选确定 LSD1 抑制是该状态下的脆弱性；联合低剂量 palbociclib 与 LSD1 抑制剂在异种移植模型中延长生存。
- [Common variant-based genome editing to address the heterogeneity of pathogenic variants in dominant disorders](https://europepmc.org/article/PPR/PPR1312157) — COVER 利用与致病变异顺式连锁的杂合常见变异，选择性失活显性遗传病的突变等位基因；作者估计其覆盖 902 个致病基因，并在 APP 与 GFAP 患者来源 iPSC 模型中验证。
- [An Integrated Single-Nucleus Atlas Resolves Cell-Type-Specific Programs and Molecular Subtypes in Alzheimer's Disease](https://www.biorxiv.org/content/10.64898/2026.09.03.747935) — panAD 整合 13 项研究中 791 名个体的超过 300 万个细胞核，并以 MONET 从协变量校正的多细胞类型表达谱中解析 AD 的四种分子亚型。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixbio/)

## AI × Math

采集 290，候选 60，精选 0。来源状态：各来源已完成

- 今日无足够高质量更新。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aixmath/)

## AI Voices

采集 74，候选 60，精选 5。来源状态：各来源已完成

- [@EpochAIResearch：GPT-6 Astra has set a new ECI record, with a score of 169. This is a substantial jump from the prior best (163), but is ](https://x.com/EpochAIResearch/status/2095602754282783108) — Epoch AI 报告称，GPT-6 Astra 在其 ECI、数学、持续学习和游戏谜题基准上创下纪录；其同时明确表示，ECI 提升仍处于推理时代趋势的不确定性范围内，且该机构获得了 OpenAI 的预发布测试访问。
- [@merettm：I wrote about the state of AI, why I’m concerned about the next few years, and the choices we need to make to keep the f](https://x.com/merettm/status/2096630018495377464) — OpenAI 首席科学家 Jakub Pachocki 表示，他撰文讨论了 AI 的现状、自己对未来数年的担忧，以及让未来仍掌握在人类手中所需作出的选择，并链接至 OpenAI 的《An Alien Mind》。
- [GPT-6 Astra: A new generation of intelligence](https://openai.com/index/gpt-6-astra) — OpenAI 的官方研究博客发布 GPT-6 Astra，并将其定位为覆盖计算机使用、编程、网络安全和科学任务的新一代模型。文中“最智能、最对齐”和“最先进”等表述为 OpenAI 自身主张。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/aivoices/)

## Engineering

采集 64，候选 59，精选 4。来源状态：各来源已完成

- [blader/humanizer](https://github.com/blader/humanizer) — blader/humanizer 是用于削弱文本中 AI 生成痕迹的智能体技能；当日 GitHub Trending 第 7 名，新增 748 星。
- [aipoch/open-science](https://github.com/aipoch/open-science) — aipoch/open-science 是开源、本地优先且模型无关的 AI 科研工作台，整合科学智能体、Python/R 笔记本、数据连接器与可复现溯源；当日 GitHub Trending 第 14 名，新增 145 星。
- [OpenWhispr/openwhispr](https://github.com/OpenWhispr/openwhispr) — OpenWhispr/openwhispr 是跨平台语音转写应用，可在本地运行 NVIDIA Parakeet 或 Whisper，也可通过自带密钥接入云端模型；当日 GitHub Trending 第 15 名，新增 225 星。

[查看频道专页](https://zichenwang114514.github.io/ai-x-daily/channels/engineering/)

[查看完整网站与历史归档](https://zichenwang114514.github.io/ai-x-daily/)
