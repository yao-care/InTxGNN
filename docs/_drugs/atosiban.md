---
layout: default
title: Atosiban
parent: 僅模型預測 (L5)
nav_order: 81
evidence_level: L5
indication_count: 10
---

# Atosiban
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

# Atosiban: From Preterm Labor to Primary Hereditary Glaucoma

## One-Sentence Summary

Atosiban (Tractocile®/Antocin®) is a synthetic peptide tocolytic agent approved by the EMA for the management of threatening preterm birth between 24 and 33 weeks of gestation, working by competitively blocking oxytocin and vasopressin receptors to suppress uterine contractions.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, however this indication is currently supported by **no clinical trials** and **no publications** — the prediction is based entirely on knowledge graph inference.
Given the absence of translational evidence and the weak mechanistic rationale connecting OT/V1A receptor antagonism to the genetic trabecular meshwork pathology of this disease, this candidate warrants a Hold until foundational preclinical data can be established.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Preterm labor — EMA-approved tocolytic for threatening preterm delivery at 24–33 weeks gestation |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Atosiban is a competitive antagonist at four human G-protein coupled receptors: the oxytocin receptor (OXTR), and vasopressin receptors V1A (AVPR1A), V1B (AVPR1B), and V2 (AVPR2). In obstetrics, blocking the oxytocin receptor on uterine myometrium reduces calcium-dependent smooth muscle contractions, thereby delaying preterm birth. The drug is approved by the EMA but has not received US FDA approval.

The theoretical bridge to primary hereditary glaucoma rests on the observation that the anterior segment of the eye — particularly the ciliary body and trabecular meshwork — expresses both oxytocin and V1-type vasopressin receptors. Some basic research suggests that V1A receptor activation may influence aqueous humor secretion, meaning that a V1A antagonist like Atosiban could theoretically modulate intraocular pressure. This is the pathway the TxGNN knowledge graph likely exploited when generating this prediction.

However, primary hereditary glaucoma — which is caused by dominant mutations in genes such as *MYOC* (myocilin) and *OPTN* (optineurin) — is driven by misfolded protein aggregation and structural dysfunction of the trabecular meshwork, not by dynamic receptor-mediated regulation of aqueous humor. The OT/vasopressin signaling axis has no established role in this genetic disease mechanism, and the mechanistic connection is extremely tenuous. The high prediction score reflects graph-level pharmacological proximity rather than a validated therapeutic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Primary Hereditary Glaucoma.

---

## Literature Evidence

Currently no related literature available for Primary Hereditary Glaucoma.

---

## India Market Information

Atosiban is not currently registered or marketed in India. No product authorizations are on record.

---

## Safety Considerations

**Receptor Pharmacology (Known Targets):**

The safety profile of Atosiban in any new indication must account for its multi-receptor binding activity. The following human receptors are known to be antagonized by Atosiban:

| Receptor | Gene | Key Physiological Role |
|----------|------|------------------------|
| Oxytocin receptor (OXTR) | OXTR (Ensembl: ENSG00000180914) | Uterine contraction, social bonding, lactation |
| Vasopressin V1A receptor | AVPR1A (Ensembl: ENSG00000166148) | Vascular smooth muscle tone, platelet aggregation |
| Vasopressin V1B receptor | AVPR1B (Ensembl: ENSG00000198049) | Pituitary ACTH release, stress axis regulation |
| Vasopressin V2 receptor | AVPR2 (Ensembl: ENSG00000126895) | Renal water reabsorption, antidiuretic effect |

V1A and V2 receptor antagonism in non-pregnant populations could affect vascular tone and renal water handling — effects not typically relevant in the original tocolytic indication but that would require assessment in any new patient population (e.g., glaucoma patients who may be elderly or have cardiovascular comorbidities).

For full warnings and contraindications, please refer to the EMA-approved Summary of Product Characteristics (SmPC). Package insert data was not available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-predicted indications for Atosiban in this Evidence Pack are rated Evidence Level L5 (model prediction only), and for the top-ranked indication — primary hereditary glaucoma — the mechanistic link between Atosiban's receptor pharmacology and the genetic trabecular meshwork pathology underlying this disease is not supported by any preclinical, clinical, or observational data. Proceeding without a biological proof-of-concept would be premature.

**To proceed, the following is needed:**
- **Basic science validation**: Confirm functional oxytocin/V1A receptor expression in trabecular meshwork cells derived from MYOC/OPTN mutation carriers, and measure whether receptor antagonism produces a measurable reduction in aqueous humor outflow resistance or intraocular pressure in relevant cell or animal models
- **Mechanistic plausibility study**: Distinguish whether TxGNN's prediction reflects genuine pharmacological relevance or incidental knowledge graph connectivity (e.g., shared "eye receptor" node linkage)
- **Safety profiling in target population**: Primary hereditary glaucoma patients are often young adults on long-term therapy; V1A/V2 receptor antagonism effects on blood pressure and renal function in this demographic are not characterized
- **Regulatory pathway**: Atosiban is not registered in India; any clinical development would require a full registration submission (New Drug Application) before patient access is possible
- **Package insert review**: Obtain the EMA SmPC to document all contraindications, special population warnings, and drug-drug interactions before advancing to any translational study

> ⚠️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

