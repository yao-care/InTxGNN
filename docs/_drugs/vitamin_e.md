---
layout: default
title: Vitamin E
parent: 僅模型預測 (L5)
nav_order: 886
evidence_level: L5
indication_count: 10
---

# Vitamin E
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Vitamin E：從維生素補充適應症到先天性膽紅素代謝障礙（Inborn Disorder of Bilirubin Metabolism）

## 一句話摘要

Vitamin E（維生素E）為脂溶性抗氧化營養素，目前台灣未查得核准藥證與明確核准適應症。TxGNN 模型預測其可能對**先天性膽紅素代謝障礙**具潛在效益，但目前僅有 **3 筆臨床試驗**（皆非直接測試 Vitamin E 於此疾病）與 **2 篇文獻**（均為 Tier 3 回顧/個案性質）支持，證據強度薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 查無資料（台灣未上市，無核准適應症文字） |
| 預測新適應症 | Inborn Disorder of Bilirubin Metabolism（先天性膽紅素代謝障礙） |
| TxGNN 預測分數 | 99.99%（rank 522） |
| 證據等級 | L4（機轉/臨床前層級） |
| 台灣市場狀態 | 未上市 |
| 藥證登記數 | 0 |
| 建議決策 | **Hold（暫緩）** |

---

## 為什麼這個預測合理？

目前**沒有 Vitamin E 詳細作用機轉（MOA）資料**（DG002，High 嚴重度缺口）。根據既有公開資訊，Vitamin E 屬脂溶性抗氧化維生素，其在「維生素E缺乏症」的療效已獲確立；機轉上，作為自由基清除劑，理論上可能減少脂質過氧化、降低氧化壓力，因此被模型連結至肝膽代謝相關疾病。

然而，就先天性膽紅素代謝障礙（如 Crigler-Najjar 症候群、進行性家族性肝內膽汁淤積等）而言，此類疾病的核心病理是**膽紅素合成酵素或轉運蛋白的原發性基因缺陷**，並非氧化壓力主導。文獻與試驗證據顯示，這類病人常見脂溶性維生素（含 Vitamin E）吸收不良，因此臨床上補充 Vitamin E 多屬「糾正繼發性缺乏」，而非「治療原發代謝缺陷」。現有列出的 3 筆臨床試驗也均非直接以 Vitamin E 介入本疾病為目的，關聯性偏間接、機轉推論尚待驗證。

---

## 臨床試驗證據

| 試驗編號 | 期別 | 狀態 | 收案人數 | 重點發現 |
|---------|------|------|------|---------|
| [NCT06465810](https://clinicaltrials.gov/study/NCT06465810) | N/A | 招募中 | 1,850 | 跨國 ATTR 類澱粉沉積症真實世界登錄研究，涵蓋膽紅素代謝疾病族群，但未特定測試 Vitamin E 介入（相關性等級 B） |
| [NCT01556906](https://clinicaltrials.gov/study/NCT01556906) | Phase 2 | 已完成 | 6 | MTP 抑制劑 lomitapide 於純合子家族性高膽固醇血症之劑量遞增試驗，介入藥物非 Vitamin E，僅間接相關（相關性等級 C） |
| [NCT03115086](https://clinicaltrials.gov/study/NCT03115086) | N/A | 進行中未招募 | 55 | Cholbam（cholic acid）上市後觀察性病患登錄，收集疾病自然史資料，非藥物介入試驗（相關性等級 B） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 重點發現 |
|------|-----|------|------|---------|
| [7915305](https://pubmed.ncbi.nlm.nih.gov/7915305/) | 1994 | Case report/Review | The Journal of Pediatrics | 描述 3β-hydroxy-C27-steroid dehydrogenase/isomerase 缺乏導致之進行性肝內膽汁淤積新病因，屬疾病機轉描述性文獻，非 Vitamin E 介入研究 |
| [803225](https://pubmed.ncbi.nlm.nih.gov/803225/) | 1975 | Review | The New England Journal of Medicine | 新生兒非溶血性黃疸之回顧文獻，無摘要內容，與 Vitamin E 治療無直接關聯 |

---

## 台灣市場資訊

目前查無台灣核准藥證資料（市場狀態：未上市，登記數：0，無可列示之許可證/適應症文字）。

---

## 安全性考量

**藥物交互作用**（來源：DDInter，共查得 173 筆交互作用紀錄，以下為節錄）：

- **Moderate 等級**（需留意，多與抗凝血/抗血小板及礦物質吸收相關）：Acetylsalicylic acid、Iron、Iron sucrose、Sevelamer、Abciximab、Antithrombin III human、Apixaban、Dipyridamole、Betrixaban、Bivalirudin、Cangrelor、Caplacizumab — 高劑量 Vitamin E 理論上可能增強抗凝血/抗血小板藥物之出血風險，並可能與鐵劑/磷結合劑產生吸收層面交互作用。
- **Minor 等級**：Hydrocortisone、Triamcinolone、Dexamethasone、Betamethasone、Budesonide、Orlistat、Prednisone、Prednisolone。

⚠️ 因**仿單警語與禁忌症資料缺失**（DG001，Blocking 嚴重度），無法完成完整安全性初評，此為進入下一階段的阻斷性缺口。

---

## 結論與下一步

**決策：Hold（暫緩）**

**理由：**
- 排名第一之預測適應症（先天性膽紅素代謝障礙）僅達 L4（機轉/臨床前）證據等級，現有 3 筆試驗皆非直接測試 Vitamin E 於此疾病，2 篇文獻亦僅屬回顧/個案描述性質，尚不足以支持進入下一階段安全性評估。
- 仿單警語/禁忌症資料缺失屬 Blocking 等級缺口，依規範無法完成 S1 安全性初評。

**若要推進，需補齊：**
- TFDA 仿單警語與禁忌症資料（下載並解析官方仿單 PDF）
- Vitamin E 完整作用機轉（MOA）資料（查詢 DrugBank API）
- 針對先天性膽紅素代謝障礙之直接介入性人體試驗證據

**附註：** 同一 Evidence Pack 中排名第二的「bilirubin metabolism disease（廣義膽紅素代謝疾病，含 NAFLD/NASH 相關肝功能異常）」證據等級達 **L2**，已有一項完成之 Phase 4 頭對頭 RCT（Vitamin E vs UDCA vs pentoxifylline，n=102）及多項觀察性佇列支持，建議另案評估該適應症之推進可行性。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

