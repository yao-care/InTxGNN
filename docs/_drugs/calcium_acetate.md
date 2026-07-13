---
layout: default
title: Calcium Acetate
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 2
---

# Calcium Acetate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Calcium Acetate: From Phosphate Binding to Calcium-Alkali Syndrome

## One-Sentence Summary

Calcium acetate is a calcium salt used primarily as a phosphate binder to control hyperphosphatemia in chronic kidney disease (CKD) patients on dialysis.
The TxGNN model assigns it a high score (99.90%) for **Calcium-Alkali Syndrome**, but this prediction demands critical interpretation: mechanistically, calcium acetate is a known **precipitant** of this syndrome — not a treatment for it — suggesting a false-positive signal driven by graph proximity in the knowledge graph.
Currently, **no clinical trials or publications** directly support a therapeutic role in this indication, placing evidence at **L5 (model prediction only)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in India (known use: phosphate binding in CKD/hyperphosphatemia) |
| Predicted New Indication | Calcium-Alkali Syndrome |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

> ⚠️ **Reverse Signal Warning**: The TxGNN high score here most likely reflects a pharmacological proximity in the knowledge graph, not a therapeutic relationship. Calcium-alkali syndrome (formerly milk-alkali syndrome) is a clinical triad of hypercalcemia, metabolic alkalosis, and progressive renal impairment caused by excessive ingestion of calcium combined with absorbable alkali. Since calcium acetate is itself a calcium salt that releases bioavailable calcium ions upon ingestion, administering it could plausibly **trigger or aggravate** this syndrome — not resolve it. The predicted direction is mechanistically inverted.

Currently, detailed mechanism of action data is not available for this Evidence Pack. Based on established pharmacology, calcium acetate dissociates in the gastrointestinal tract to release calcium ions and acetate. Its primary clinical role is as an oral phosphate binder: free calcium ions bind dietary phosphate in the gut lumen, preventing its absorption and reducing serum phosphate in dialysis-dependent patients.

The TxGNN knowledge graph links calcium acetate to calcium-alkali syndrome because both involve calcium homeostasis — but this graph edge encodes a pathophysiological cause-effect relationship, not a therapeutic one. A score of 0.9990 reflects how close calcium salts and calcium metabolism disorders sit in the graph topology. This is a textbook example of a **knowledge-graph false positive**: high prediction score does not imply repurposing plausibility when the mechanistic direction is reversed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03591471](https://clinicaltrials.gov/study/NCT03591471) | Phase 1/2 | Unknown | 500 | ⚠️ **Pipeline mismatch** — This trial investigates Traditional Chinese Medicine (Tripterygium Wilfordii glycosides) for Henoch-Schönlein Purpura Nephritis in children. It has no connection to calcium acetate or calcium-alkali syndrome. Retrieved due to shared renal keywords; does not constitute supporting evidence. |

No valid clinical trials for calcium acetate in calcium-alkali syndrome are currently registered.

---

## India Market Information

Calcium acetate currently has **no registered pharmaceutical products** in India. There are no market authorizations, licensed brands, or approved indications on record.

---

## Safety Considerations

**Drug Interactions** (83 total interactions on file; clinically significant selections listed below):

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Dolutegravir | **Major** | Calcium chelates integrase inhibitors — substantially reduces antiviral plasma exposure |
| Bictegravir | **Major** | Same chelation mechanism; HIV treatment failure risk |
| Doxycycline | Moderate | Calcium forms insoluble chelates with tetracyclines, reducing antibiotic absorption |
| Tetracycline | Moderate | Same chelation class as doxycycline |
| Alendronic acid | Moderate | Calcium reduces oral bisphosphonate absorption |
| Risedronic acid | Moderate | Same bisphosphonate absorption interaction |
| Ibandronate | Moderate | Same bisphosphonate absorption interaction |
| Hydrochlorothiazide | Moderate | Thiazide diuretics increase renal calcium reabsorption — co-administration raises hypercalcemia risk |
| Calcipotriol (topical) | Moderate | Vitamin D analogue; additive hypercalcemia risk with systemic calcium loading |
| Calcitriol (topical) | Moderate | Vitamin D analogue; additive hypercalcemia risk |

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rank-1 TxGNN prediction (calcium-alkali syndrome) represents a pharmacological paradox — calcium acetate is a documented causative agent of this syndrome, not a therapeutic option. The 99.90% prediction score reflects graph topology bias rather than repurposing plausibility. No clinical trial or literature evidence exists to support further development in this direction.

**To proceed with evaluation of this drug candidate, the following is needed:**

- **Nephrologist consultation** to formally confirm the reverse-signal interpretation and rule out any niche scenario where calcium acetate might be beneficial (e.g., chelating excess oxalate in a subset of patients)
- **Investigation of rank-2 prediction** (primary bone dysplasia with defective bone mineralization, score 99.88%) — this carries a biologically plausible mechanistic rationale (calcium ions support hydroxyapatite formation) and may represent a more legitimate repurposing signal, though it also lacks clinical trial or literature support at this time
- **MOA data from DrugBank API** (DG002) to complete the mechanistic plausibility assessment
- **CDSCO/package insert review** (DG001) to retrieve warnings, contraindications, and labelled dosing before any clinical discussion proceeds
- If the rank-2 indication is pursued: preclinical literature search for calcium supplementation in rare bone mineralization disorders (e.g., hypophosphatasia subtypes not treated with asfotase alfa)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

