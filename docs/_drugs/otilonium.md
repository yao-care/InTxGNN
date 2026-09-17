---
layout: default
title: Otilonium
parent: Model Prediction Only (L5)
nav_order: 617
evidence_level: L5
indication_count: 10
---

# Otilonium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Otilonium：局部腸道解痙作用 到 Hypertrichosis（多毛症）預測

## 摘要

Otilonium（DrugBank DB13500）在證據包中原始適應症清單為空、作用機轉（MOA）為資料缺口，僅能由候選機轉線索文字得知其藥理分類為**腸道局部作用之抗蕈毒鹼／鈣通道阻斷劑**（國際文獻上多用於腸躁症相關適應症，全身吸收極低）。TxGNN 模型排名第一的預測適應症為 **Hypertrichosis（多毛症）**，預測分數 98.94%，但**零臨床試驗、零文獻**支持，且該分數與另外 8 個機轉上完全不相關的候選（Dandy-Walker 症候群、各部位息肉等）群聚在 0.985–0.989 區間，高度提示為模型雜訊而非真實訊號。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 台灣法規資料未記錄（`licenses` 為空、`total_licenses` = 0）；據候選機轉線索文字，國際上屬腸躁症相關腸道局部解痙劑，非本證據包核准來源 |
| 預測新適應症 | Hypertrichosis（多毛症） |
| TxGNN 預測分數 | 98.94% |
| 證據等級 | L5（僅模型預測，無臨床試驗、無文獻） |
| 台灣市場狀態 | Not marketed |
| 登記證數量 | 0 |
| 建議決策 | Hold |

---

## 為何這個預測不具說服力

目前尚無 Otilonium 詳細作用機轉（MOA）資料（DG002，High severity）。根據證據包內附的機轉線索，Otilonium 屬於腸道局部作用之抗蕈毒鹼／鈣通道阻斷劑，全身吸收極低，主要藥理標的在腸道平滑肌，與毛髮生長調控路徑（毛囊週期、雄性素受體訊號等）並無已知的生物學交集。

更關鍵的是，本候選（Hypertrichosis）與同批次排名第 2–10 的候選（Dandy-Walker 症候群、Ambras 型先天性全身多毛症、齒源性發育畸形症候群、毛幹結構異常、聲帶／中耳／子宮／外耳道／額竇息肉等）分數幾乎全數集中在 0.985–0.989 之間，且**除排名第 4 外全數零試驗、零文獻**。這種跨多個解剖部位、病因學互不相關卻分數高度集中的模式，是知識圖譜鄰接稀疏或 embedding 不穩定導致模型雜訊的典型特徵，而非藥物特異性訊號。

排名第 4（齒源性/牙周相關畸形症候群）雖檢索到 20 篇文獻，但經逐篇核對標題與摘要，內容全為牙周病一般病理生理、糖尿病共病、非手術治療等主題，**無任一篇提及 Otilonium 或其藥理成分**，屬關鍵字共現而非機轉證據，不能作為佐證。

---

## 臨床試驗證據

目前無相關臨床試驗註冊。

---

## 文獻證據

目前無相關文獻資料。

---

## 台灣市場資訊

Otilonium 目前於台灣**Not marketed**，無有效藥品許可證（`total_licenses` = 0），無登記資料可列示。

---

## 安全性考量

請參閱仿單所載安全性資訊。

（DDI 查詢無結果、警語與禁忌均為資料缺口 DG001，屬 Blocking 等級，尚無法進行 S1 安全性初評。）

---

## 結論與後續建議

**決策：Hold**

**理由：**
本候選證據等級為 L5，零臨床試驗、零文獻，且機轉上與已知藥理作用（腸道局部平滑肌調控）無合理連結；同批候選呈現的跨部位分數群聚模式進一步支持此為模型雜訊，而非具生物學意義的訊號，不建議推進至下一階段。

**若要推進，需補充：**
- TFDA／原廠仿單完整警語與禁忌資料（DG001，Blocking，阻擋 S1 安全性初評）
- DrugBank 或原廠 MOA 詳細資料（DG002，High）
- 若後續要重新評估，建議優先檢視與 Otilonium 已知腸道藥理作用機轉上更相關的適應症候選，而非本批多毛症／息肉類雜訊群集
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

