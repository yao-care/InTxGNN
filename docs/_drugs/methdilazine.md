---
layout: default
title: Methdilazine
parent: 僅模型預測 (L5)
nav_order: 425
evidence_level: L5
indication_count: 1
---

# Methdilazine
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

# Methdilazine: From Pruritus to Nasal Cavity Disease

## One-Sentence Summary

Methdilazine (DB00902) is a first-generation phenothiazine-class H1 receptor antagonist (antihistamine), historically used for pruritus and allergic skin conditions.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, with a high prediction score of **99.06%**.
However, **no clinical trials and no published literature** currently support this specific repurposing direction — the prediction is based on model inference only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pruritus / Allergic conditions (phenothiazine antihistamine class) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological class information, Methdilazine is a first-generation phenothiazine-type H1 receptor antagonist. As an antihistamine, it theoretically blocks histamine-mediated effects on nasal mucosa — including congestion, pruritus, and hypersecretion — which are hallmark features of allergic rhinitis and other nasal cavity diseases.

This mechanistic link is a **class-level extrapolation**: while the H1 antagonism mechanism is well-established for this drug class (e.g., chlorphenamine, promethazine), there is no direct clinical evidence that Methdilazine itself has been evaluated for nasal cavity disease. The TxGNN knowledge graph model likely inferred this connection based on the pharmacological relationship between antihistamines and upper airway diseases.

It should be noted that the original approved indications data for Methdilazine is absent in the regulatory database, and no India-registered products exist. The mechanistic link strength is therefore classified as **indirect / inferential**, pending retrieval of the full DrugBank MOA profile.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Methdilazine is currently **not marketed in India**. No product registrations or approved licenses were identified in the regulatory database. This drug has no locally registered dosage forms or approved indications on record.

---

## Safety Considerations

**Drug Interactions (401 total interactions identified):**

| Interacting Drug | Severity | Notes |
|-----------------|----------|-------|
| Bupropion | **Major** | Co-administration should be avoided |
| Potassium Citrate | **Major** | Co-administration should be avoided |
| Epinephrine | Moderate | Use with caution |
| Morphine | Moderate | Additive CNS/respiratory depression risk |
| Atropine | Moderate | Additive anticholinergic effects |
| Hyoscyamine | Moderate | Additive anticholinergic effects |
| Glycopyrronium | Moderate | Additive anticholinergic effects |
| Metformin | Moderate | Monitor blood glucose |
| Pioglitazone | Moderate | Monitor blood glucose |
| Acarbose | Moderate | Monitor blood glucose |
| Alogliptin | Moderate | Monitor blood glucose |
| Canagliflozin | Moderate | Monitor blood glucose |
| Dapagliflozin | Moderate | Monitor blood glucose |
| Saxagliptin | Moderate | Monitor blood glucose |
| Albiglutide | Moderate | Monitor blood glucose |
| Chlorpropamide | Moderate | Monitor blood glucose |
| Loperamide | Moderate | Use with caution |
| Lorcaserin | Moderate | Use with caution |
| Picosulfuric Acid | Moderate | Use with caution |
| Polyethylene Glycol (3350 with electrolytes) | Moderate | Use with caution |

> **Note:** The total DDI burden is substantial (401 interactions). The notable pattern of **multiple moderate interactions with antidiabetic agents** (e.g., Metformin, SGLT-2 inhibitors, DPP-4 inhibitors) suggests potential antagonism of hypoglycaemic effects, consistent with known anticholinergic/phenothiazine class effects on glucose metabolism. Please refer to the full package insert for complete safety information, as TFDA-sourced warnings and contraindications were not retrievable for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.06%) for Methdilazine in nasal cavity disease, and the mechanistic rationale (H1 antagonism → nasal mucosal effect) is pharmacologically plausible. However, **zero clinical trials and zero published literature** were identified to support this specific application, placing the evidence at the lowest level (L5 — model prediction only). Without any empirical validation, this candidate cannot advance beyond the exploratory stage.

**To proceed, the following is needed:**

- **MOA data retrieval:** Query DrugBank API for full mechanism of action, pharmacodynamics, and pharmacokinetics of Methdilazine (DG002 — High severity)
- **TFDA package insert:** Download and parse the official prescribing information PDF to populate key warnings and contraindications (DG001 — Blocking severity)
- **Scoping literature review:** Conduct a broader PubMed/Embase search for Methdilazine in any nasal or upper respiratory condition (including allergic rhinitis, sinusitis) to identify whether indirect evidence exists
- **Regulatory feasibility assessment:** Evaluate whether India market entry is viable, given zero current registrations and unknown original indication status
- **Comparator analysis:** Benchmark against approved antihistamines already indicated for nasal diseases (e.g., cetirizine, loratadine, fexofenadine) to assess differentiation potential and whether a new clinical program is justified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

