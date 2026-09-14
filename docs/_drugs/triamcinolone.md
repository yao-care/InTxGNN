---
layout: default
title: Triamcinolone
parent: 僅模型預測 (L5)
nav_order: 854
evidence_level: L5
indication_count: 10
---

# Triamcinolone
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

# Triamcinolone：從皮質類固醇抗發炎治療到 Idiopathic Steroid-Sensitive Nephrotic Syndrome

## 一句話摘要

Triamcinolone 是合成型糖皮質類固醇（corticosteroid），已知作用機轉資料目前缺失，但依藥理分類廣泛用於發炎、過敏及自體免疫相關疾病；該藥於印度**尚未上市**，無在地藥證。TxGNN 本次針對此藥共預測 10 個候選適應症，其中以 **Idiopathic Steroid-Sensitive Nephrotic Syndrome（類固醇敏感型腎病症候群）** 之機轉合理性與證據品質最高（預測分數 **99.76%**），目前有 **3 篇文獻**支持，但尚無 triamcinolone 專屬之臨床試驗。其餘 9 項候選多屬毛囊/落髮相關罕見疾病，證據品質偏低（多為 L5，Hold）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 資料缺失（印度未上市，無核准適應症文字；依藥理分類已知用於發炎/過敏/自體免疫疾病） |
| 預測新適應症 | Idiopathic Steroid-Sensitive Nephrotic Syndrome |
| TxGNN 預測分數 | 99.76%（原始分數 0.99758，rank 4783） |
| 證據等級 | L3（觀察性研究／系統性回顧） |
| 印度市場狀態 | ✗ 未上市 |
| 藥證登記數 | 0 |
| 建議決策 | Proceed with Guardrails（附加條件下推進） |

---

## 為何此預測合理？

目前尚無 triamcinolone 詳細作用機轉（MOA）資料。依已知資訊，triamcinolone 屬於糖皮質類固醇（corticosteroid）類藥物，具抗發炎與免疫抑制作用，此為該藥物類別已被廣泛驗證的核心藥理特性。

Idiopathic steroid-sensitive nephrotic syndrome 此一疾病的**定義本身即為「對糖皮質類固醇治療有反應」**的腎病症候群——換言之，皮質類固醇（如 prednisolone 類）本來就是此病的標準第一線治療。Triamcinolone 作為同類糖皮質激素，在機轉上與此適應症具有高度合理性與一致性，這也是本候選在 10 項預測中證據等級最高（L3）、且獲得「Proceed with Guardrails」建議的主要原因。

需注意的是，所附文獻均為治療策略回顧或病例系列，反映的是「糖皮質類固醇這一藥物類別」在此病的既定地位，尚未有直接鎖定 triamcinolone 特定劑型/劑量的對照試驗，此為後續需要補強之處。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 重點發現 |
|------|-----|------|------|---------|
| [20156172](https://pubmed.ncbi.nlm.nih.gov/20156172/) | 2010 | Review | Current Medicinal Chemistry | 兒童特發性腎病症候群治療策略回顧，多數病例對類固醇治療有反應，類固醇依賴型則需鈣調磷酸酶抑制劑等輔助治療 |
| [22495188](https://pubmed.ncbi.nlm.nih.gov/22495188/) | 2012 | Review | Minerva Pediatrica | 特發性腎病症候群新治療策略回顧，多數病人對類固醇有反應，強調類固醇於此病的核心地位 |
| [4834775](https://pubmed.ncbi.nlm.nih.gov/4834775/) | 1974 | Retrospective Cohort | American Journal of Diseases of Children | 148例兒童特發性腎病症候群之臨床再評估病例系列 |

---

## 其他候選適應症（優先度較低，供參考）

除上述主要候選外，本次 TxGNN 共預測 10 個適應症，多數為毛囊/落髮相關罕見疾病，證據等級偏低，暫不建議優先投入：

| 排序 | 適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|--------|-----------|---------|---------|------|
| 1 | Alopecia mucinosa | 99.99% | pending | pending | 待評估（4篇文獻，均為病例報告層級） |
| 2 | Telogen effluvium | 99.99% | L5 | S0 | Hold（非發炎主導病理，機轉關聯薄弱） |
| 3 | Quinquaud's folliculitis decalvans | 99.99% | L4 | S1 | Research Question（機轉合理但文獻未直接對應 triamcinolone） |
| 4 | Alopecia antibody deficiency | 99.99% | L5 | S0 | Hold（無文獻／試驗支持） |
| 5 | Hereditary hypotrichosis with recurrent skin vesicles | 99.99% | L5 | S0 | Hold（單基因疾病，機轉不相關） |
| 6 | Alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome | 99.99% | L5 | S0 | Hold（罕見症候群，無證據） |
| 7 | Atrichia with papular lesions | 99.96% | L5 | S0 | Hold（角質分化異常，非發炎驅動） |
| 9 | Alopecia universalis onychodystrophy vitiligo | 99.75% | L5 | S0 | Hold（無文獻／試驗支持） |
| 10 | Sporadic idiopathic steroid-**resistant** nephrotic syndrome | 99.74% | L5 | S0 | Hold（**機轉矛盾**：定義即為對類固醇無反應，與 triamcinolone 作用機轉相悖） |

---

## 印度市場資訊

Triamcinolone 目前於印度**未上市**，無任何有效藥證登記，故無藥品名稱、劑型或核准適應症資料可供列示。

---

## 安全性考量

**藥物交互作用**（來源：DDI 查詢，總計 696 筆交互作用紀錄，以下為重點摘錄）：

| 交互藥物 | 嚴重度 | 來源 |
|---------|-------|------|
| Adalimumab | Major | ddinter |
| Alefacept | Moderate | ddinter |
| Alemtuzumab | Moderate | ddinter |
| Aldesleukin | Moderate | ddinter |
| Zidovudine | Moderate | ddinter |
| Acetazolamide | Moderate | ddinter |
| Ibuprofen | Moderate | ddinter |
| Ketorolac | Moderate | ddinter |
| Isotretinoin | Moderate | ddinter |
| Salbutamol / Formoterol | Minor | ddinter |

其中與 Adalimumab 之交互作用列為 **Major** 等級，兩者合併使用需特別留意免疫抑制疊加風險；與其他免疫調節劑（Alefacept、Alemtuzumab、Aldesleukin）及 NSAIDs（Ibuprofen、Ketorolac）之交互作用亦建議臨床監測。

> 仿單警語與禁忌資料目前缺失（見下方 Next Steps，此為 Blocking 等級資料缺口），無法完成 S1 安全性初評，請以官方仿單為準。

---

## 結論與下一步

**決策：Proceed with Guardrails（附加條件下推進）**

**理由：**
Idiopathic steroid-sensitive nephrotic syndrome 之候選適應症具高度機轉合理性（疾病定義本身即為類固醇反應性），並有 L3 等級的觀察性研究／回顧文獻支持，但目前缺乏 triamcinolone 專屬之對照試驗，且本藥於印度尚未上市、仿單安全性資料缺失，故不宜直接判定 Go，需附加條件推進。

**若要繼續推進，需補齊：**
- 取得完整仿單警語與禁忌資料（DG001，Blocking 等級，S1 安全性初評之必要前提）
- 取得 triamcinolone 完整作用機轉（MOA）資料（DG002）
- 評估印度上市／引進路徑（目前市場狀態為未上市，藥證數為 0）
- 搜尋或規劃 triamcinolone 專屬於 idiopathic steroid-sensitive nephrotic syndrome 之前瞻性療效資料，以補強 L3 等級證據
- 其餘 9 項候選適應症（多為 L5／S0／Hold）暫不建議投入資源，除非未來出現新增文獻或試驗證據；特別留意 rank 10（steroid-resistant nephrotic syndrome）屬機轉矛盾案例，不應與 rank 8 混淆處理
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

