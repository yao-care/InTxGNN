---
layout: default
title: Arginine
parent: 僅模型預測 (L5)
nav_order: 68
evidence_level: L5
indication_count: 1
---

# Arginine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Arginine: From Nutritional Supplement to Gastroparesis

## One-Sentence Summary

L-Arginine（精胺酸）是人體的半必需胺基酸，臨床上廣泛用於營養補充、代謝支持及成長激素激發試驗。TxGNN 模型預測其對**胃輕癱（Gastroparesis）**可能具有治療潛力，預測分數高達 **99.42%**；目前支持此方向的直接臨床試驗數量極少（0 件直接相關），但有 **10 篇基礎/動物研究文獻**提供機轉層面的間接支持，整體證據尚處於早期研究階段。

---

## Quick Overview

| 項目 | 內容 |
|------|------|
| Original Indication | 營養補充 / 胺基酸療法（臨床無正式核准適應症記錄） |
| Predicted New Indication | Gastroparesis（胃輕癱） |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L4（臨床前研究 / 機轉研究） |
| India Market Status | ✗ 未上市 |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

L-精胺酸（L-Arginine）是一氧化氮合酶（NOS）的唯一生理底物，透過酵素催化生成一氧化氮（Nitric Oxide, NO）。NO 是腸神經系統中最重要的抑制性神經傳導物質，負責調控胃底的**容受性舒張（receptive relaxation）**及幽門括約肌的鬆弛，使胃能正常儲存食物並有序排空。

胃輕癱的核心病理之一正是 nitrergic 神經元（nNOS⁺ 細胞）的進行性喪失，導致 NO 合成不足，進而引發幽門持續收縮與胃排空障礙。在此背景下，補充精胺酸可增加 NO 合成底物的可用性，理論上有機會恢復 nitrergic 訊號傳遞、改善胃動力。

最直接的實驗支持來自 PMID 25057793（Reichardt et al., 2014）：該研究在小鼠中證實，類固醇（地塞米松）可耗竭體內 L-精胺酸，並直接誘發胃輕癱；補充 L-精胺酸可逆轉此效應。這項證據確立了「精胺酸缺乏 → NO 不足 → 胃輕癱」的直接因果鏈，為 TxGNN 的預測提供了具體的機轉依據。然而，目前所有支持證據均來自動物模型，尚無人體臨床試驗直接評估精胺酸對胃輕癱患者的療效與安全性。

---

## Clinical Trial Evidence

目前資料庫中查詢到的唯一相關試驗（NCT01702051）與精胺酸治療胃輕癱**不具直接相關性**，列於下方供參考：

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01702051](https://clinicaltrials.gov/study/NCT01702051) | N/A | Unknown | 150 | 評估胰腺切除術後自體胰島細胞移植改善血糖控制之觀察性研究；雖胰全切後常見胃輕癱，且精胺酸激發試驗可用於評估胰島功能，但本試驗並非以精胺酸介入治療胃輕癱。**相關性評級：C（間接背景關聯）** |

> ⚠️ 目前尚無以精胺酸為干預措施、以胃輕癱為主要終點的直接臨床試驗。

---

## Literature Evidence

以下文獻均為動物研究，提供精胺酸與胃輕癱之間的機轉與病理生理學關聯：

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25057793](https://pubmed.ncbi.nlm.nih.gov/25057793/) | 2014 | Animal Study (Mouse) | Endocrinology | **最關鍵文獻**：地塞米松耗竭小鼠體內 L-精胺酸，直接誘發胃輕癱；補充 L-精胺酸可逆轉此效應，確立精胺酸缺乏與胃輕癱的直接因果關係 |
| [23639814](https://pubmed.ncbi.nlm.nih.gov/23639814/) | 2013 | Animal Study (Mouse) | Am J Physiol Gastrointest Liver Physiol | 四氫生物蝶呤（BH4，NOS 輔因子）缺乏的新生小鼠出現胃輕癱，顯示 NO 合成通路缺損與胃排空障礙的關聯 |
| [35380456](https://pubmed.ncbi.nlm.nih.gov/35380456/) | 2022 | Animal Study (Rat) | Am J Physiol Gastrointest Liver Physiol | 帕金森病 6-OHDA 大鼠模型中，幽門括約肌的 nitrergic 鬆弛功能受損，支持 NO 缺乏在胃輕癱中的核心角色 |
| [18312542](https://pubmed.ncbi.nlm.nih.gov/18312542/) | 2008 | Animal Study (Rat) | Neurogastroenterol Motility | 糖尿病 BB 大鼠空腸 nNOS 表現降低，揭示糖尿病性胃輕癱中 nitrergic 神經元功能喪失的機轉 |
| [33867519](https://pubmed.ncbi.nlm.nih.gov/33867519/) | 2021 | Case Report | Am J Case Reports | MELAS 粒線體疾病患者（m.3243A>G），生活方式介入後乳酸值恢復正常；患者有胃輕癱，精胺酸為 MELAS 常用補充劑，提供間接臨床背景 |
| [18322959](https://pubmed.ncbi.nlm.nih.gov/18322959/) | 2008 | Animal Study (Mouse) | World J Gastroenterol | 評估 ghrelin 與 GHRP-6 在糖尿病小鼠胃輕癱中的促胃動力作用，提供藥理比較背景 |
| [19023028](https://pubmed.ncbi.nlm.nih.gov/19023028/) | 2009 | Animal Study (Dog) | Am J Physiol Gastrointest Liver Physiol | 同步胃電刺激（SGES）透過 nitrergic 通路改善迷走神經切除後的胃容受性障礙，間接支持 NO 訊號在胃動力調控中的重要性 |
| [31984783](https://pubmed.ncbi.nlm.nih.gov/31984783/) | 2020 | Animal Study (Rat) | Am J Physiol Gastrointest Liver Physiol | 薦神經刺激（SNS）透過脊髓傳入與迷走傳出通路改善胃容受功能，提供神經調控背景 |
| [21193530](https://pubmed.ncbi.nlm.nih.gov/21193530/) | 2011 | Animal Study (Rat) | Am J Physiol Gastrointest Liver Physiol | 高血糖透過結狀神經節 KATP 通道抑制胃動力，揭示糖尿病性胃輕癱的神經機轉 |
| [8194696](https://pubmed.ncbi.nlm.nih.gov/8194696/) | 1994 | Animal Study (Rat) | Gastroenterology | 食物蛋白質誘發過敏反應導致大鼠胃排空延遲，探討胃輕癱的免疫病理機轉 |

---

## India Market Information

根據現有資料，**L-Arginine 目前在印度無已登記之藥品許可證（License）**，市場狀態為「未上市」。

> 注意：精胺酸以膳食補充劑形式在市場上廣泛流通，但作為處方藥物適應症的正式核准資料尚未收錄於本資料庫。建議另查 CDSCO 官方資料庫確認補充劑及原料藥的登記現況。

---

## Safety Considerations

> 目前安全性資料（包括警語、禁忌症及藥物交互作用）尚未完整收集。請參閱產品仿單之警語與注意事項。
>
> 特別提醒：精胺酸在特定情況下（如嚴重肝功能不全、敗血症患者）的安全性需個別評估；大劑量靜脈注射精胺酸鹽酸鹽可能引發高氯性酸中毒，使用前應確認完整安全性資料。

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
現有證據僅達 L4（臨床前動物研究），雖然機轉假說具邏輯一致性（NO 底物補充 → nitrergic 訊號恢復 → 改善胃動力），但缺乏人體試驗數據，且藥品在印度市場完全無上市紀錄，安全性資料庫亦存在關鍵缺口，不具備推進臨床應用的條件。

**To proceed, the following is needed:**

- **安全性資料補全**：查詢 CDSCO 仿單、DrugBank 完整藥物資訊，確認警語、禁忌症與藥物交互作用（目前均為 Data Gap，屬 Blocking 層級）
- **MOA 文件化**：取得 DrugBank 正式機轉資料，完成機轉關聯性分析
- **概念驗證研究設計**：規劃以胃輕癱患者為對象的 Phase 1/2 探索性試驗，評估 L-精胺酸補充（口服或靜脈注射）對胃排空速率（胃排空閃爍攝影）的影響
- **適合族群界定**：優先考慮精胺酸缺乏相關族群，如 MELAS 患者（m.3243A>G）、長期類固醇使用者，或可測量 nNOS 活性的糖尿病性胃輕癱患者
- **生物標記策略**：探討血漿 L-精胺酸濃度、NO 代謝物（硝酸鹽/亞硝酸鹽）作為療效替代指標的可行性
- **印度市場法規評估**：確認精胺酸在印度作為處方藥的法規路徑及現行市場狀態

---

> ⚠️ **免責聲明**：本報告為 TxGNN 模型預測結果之研究摘要，僅供學術研究參考，**不構成醫療建議**。老藥新用候選適應症需經過嚴格臨床驗證方可應用於患者。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

