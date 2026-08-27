---
layout: default
title: Magnesium Citrate
parent: 僅模型預測 (L5)
nav_order: 405
evidence_level: L5
indication_count: 2
---

# Magnesium Citrate
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

# Magnesium Citrate: From Osmotic Laxative/Mineral Supplement to Calcium-Alkali Syndrome

## One-Sentence Summary

Magnesium citrate is a magnesium salt commonly used as an osmotic laxative and mineral supplement to correct magnesium deficiency.
The TxGNN model predicts it may be effective for **Calcium-Alkali Syndrome**,
however **0 clinical trials** and **0 publications** currently support this direction — this remains a model-prediction-only finding at the present stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication data available in regulatory records |
| Predicted New Indication | Calcium-Alkali Syndrome |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known pharmacology, Magnesium citrate delivers two biologically active components: magnesium ions (Mg²⁺) and citrate. Magnesium ions can competitively inhibit calcium reabsorption at both the intestinal epithelium and renal tubular level — sharing transport channels (TRPM6/TRPM7) with calcium — which theoretically could reduce serum calcium levels in hypercalcaemic states.

However, a critical mechanistic paradox undermines this rationale. The citrate moiety carries a pronounced alkalizing effect: it is metabolised to bicarbonate (HCO₃⁻), which could directly worsen the metabolic alkalosis that sits at the very core of calcium-alkali syndrome pathology. The two components of this drug work in opposing directions: Mg²⁺ may help lower calcium while citrate may aggravate alkalosis. The net clinical outcome is therefore ambiguous, and this contradictory mechanism sharply limits confidence in the prediction.

Furthermore, the 235 documented drug interactions raise serious co-administration concerns, particularly with agents frequently encountered alongside calcium-alkali syndrome (e.g., calcium supplements, diuretics, proton pump inhibitors). Although the TxGNN score is exceptionally high (99.51%), the complete absence of clinical or preclinical evidence — combined with the mechanistic contradiction — means this prediction must be treated with significant caution until further data emerge.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Magnesium citrate (DrugBank ID: DB11110) currently has **no registered products** in the Indian market. No authorization records exist in the available regulatory dataset.

---

## Safety Considerations

**Drug Interactions** (235 total interactions identified; top interactions listed below):

| Interacting Drug | Severity | Source |
|------------------|----------|--------|
| Dolutegravir | **Major** | DDInter |
| Abiraterone | Moderate | DDInter |
| Tramadol | Moderate | DDInter |
| Acetazolamide | Moderate | DDInter |
| Doxycycline | Moderate | DDInter |
| Hydrocortisone | Moderate | DDInter |
| Amiodarone | Moderate | DDInter |
| Arsenic trioxide | Moderate | DDInter |
| Hydrochlorothiazide | Moderate | DDInter |
| Alendronic acid | Moderate | DDInter |

> A total of **235 drug interactions** have been identified. This is a notably high interaction burden. Consult the full interaction database before any co-administration decision.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.51%), the mechanistic case for Magnesium citrate in calcium-alkali syndrome is inherently contradictory — the magnesium component may reduce hypercalcaemia while the citrate component risks worsening the metabolic alkalosis that defines the syndrome. With zero supporting clinical trials or literature, no market authorisation in India, and a substantial DDI burden (235 interactions), the evidence basis is entirely insufficient to proceed.

**To proceed, the following is needed:**
- Retrieve full MOA data from DrugBank to confirm or refine the mechanistic hypothesis
- Commission or identify preclinical studies (cell/animal models) that specifically examine the net effect of magnesium citrate on calcium-alkali balance
- Conduct a targeted literature search for any case reports or observational data linking magnesium supplementation to outcomes in calcium-alkali or hypercalcaemic-alkalosis conditions
- Perform a comprehensive DDI risk assessment focusing on agents commonly used in calcium-alkali syndrome management (calcium supplements, thiazide diuretics, PPIs, antacids)
- Obtain TFDA package insert to identify official warnings and contraindications (currently a blocking data gap)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

