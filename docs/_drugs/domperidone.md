---
layout: default
title: Domperidone
parent: 僅模型預測 (L5)
nav_order: 257
evidence_level: L5
indication_count: 1
---

# Domperidone
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

# Domperidone: From Dyspepsia/Nausea to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Domperidone (Motilium®) is a peripheral dopamine D2/D3 receptor antagonist widely used to manage dyspepsia, heartburn, epigastric pain, nausea, and vomiting.
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
however, **no clinical trials and no publications** currently support this direction — the prediction is based solely on knowledge-graph network topology.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Dyspepsia, heartburn, epigastric pain, nausea, and vomiting |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known pharmacological information, Domperidone is a peripheral dopamine D2/D3 receptor antagonist. It does not cross the blood-brain barrier to a clinically significant degree, and its established efficacy in gastrointestinal symptoms (nausea, dyspepsia) stems from blockade of D2/D3 receptors in the chemoreceptor trigger zone and gut.

The mechanistic bridge to NSIAD is extremely tenuous. NSIAD is caused by gain-of-function mutations in the AVPR2 gene (encoding the V2 vasopressin receptor), leading to constitutive activation of the receptor independent of ADH levels, resulting in persistent water retention and hyponatraemia. Domperidone has no known direct action on the V2 receptor or its downstream signaling cascade (Gs/cAMP/AQP2 pathway).

The only conceivable indirect links are: (1) renal dopamine D1-like receptors promote natriuresis and diuresis — D2 antagonism by domperidone could theoretically perturb this balance; and (2) peripheral dopamine tone may modestly influence pituitary ADH release. Neither mechanism is relevant to NSIAD, where the defect lies constitutively downstream of ADH. The TxGNN high score (99.08%) is almost certainly attributable to network proximity between dopaminergic, renal, and water-electrolyte nodes in the knowledge graph, rather than direct mechanistic evidence. Validation would need to begin at the level of basic laboratory experiments.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Domperidone is not currently registered or marketed in India under the data available in this Evidence Pack (0 authorizations on record).

> **Note:** Domperidone is available as an over-the-counter or prescription medicine in numerous countries (including several European markets and parts of Asia) under brand names such as Motilium® and Nauzelin®. However, neither the US FDA nor the EMA has granted central marketing authorization; individual national approvals apply. India-specific regulatory status should be verified directly against CDSCO records.

---

## Safety Considerations

No key warnings or contraindication data were available in this Evidence Pack.

**Pharmacological Target Interactions (from receptor binding data):**

| Target | Gene | Interaction Type | Clinical Relevance |
|--------|------|-----------------|-------------------|
| D₂ receptor | DRD2 (ENSG00000149295) | Antagonist (primary mechanism) | Basis of antiemetic and prokinetic action; QTc prolongation risk at high doses is a known class concern |
| D₃ receptor | DRD3 (ENSG00000151577) | Antagonist | Contributes to peripheral dopaminergic blockade |

> Please refer to the package insert (applicable jurisdiction) for full safety information, including QT-interval prolongation warnings, cardiac arrhythmia risk, and drug interactions with CYP3A4 inhibitors.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.08%), but the mechanistic hypothesis is extremely weak — NSIAD is driven by constitutive AVPR2 activation entirely independent of dopaminergic pathways, and there is zero clinical or preclinical evidence supporting domperidone use in this ultra-rare disease. This is an L5 prediction with no supporting literature, no registered trials, and no approved use in India.

**To proceed, the following would be needed:**

- **MOA clarification:** Obtain full DrugBank mechanistic profile and identify any secondary targets that might relate to renal water handling or V2R signaling
- **Basic science validation:** In vitro or animal model studies examining domperidone effects on renal AVPR2 pathway or aquaporin-2 expression
- **NSIAD literature review:** Confirm there is truly no published case report or hypothesis paper linking dopamine antagonism to NSIAD management
- **Regulatory safety file:** Download and parse the package insert from at least one approved jurisdiction (e.g., EMA) to complete the blocking DG001 data gap on warnings and contraindications
- **CDSCO verification:** Confirm India regulatory status directly via the CDSCO online database, as the current 0-registration status may reflect data pipeline limitations rather than true non-availability
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

