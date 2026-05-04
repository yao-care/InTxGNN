---
layout: default
title: Amylmetacresol
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
---

# Amylmetacresol
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

# Amylmetacresol: From Antiseptic/Throat Infections to Cauda Equina Syndrome

## One-Sentence Summary

Amylmetacresol is a phenolic antiseptic compound commonly used in over-the-counter throat lozenge formulations to relieve minor throat infections and mouth discomfort.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, achieving a prediction score of **99.99%**.
However, there are currently **0 clinical trials** and **0 publications** supporting this direction, and all predictions in this batch are classified as **L5** (model prediction only), with a recommendation to **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Topical antiseptic; throat/mouth infection relief (OTC lozenge formulations) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (MOA Data Gap). Based on known information, Amylmetacresol is a phenolic antiseptic compound widely used in combination OTC throat lozenges (e.g., Strepsils, in combination with dichlorobenzyl alcohol). Its broad-spectrum antimicrobial and mild local anesthetic properties have been validated for oral/pharyngeal mucosal applications.

Cauda Equina Syndrome is a neurological emergency caused by compression of the lumbar nerve roots at the base of the spinal cord, primarily requiring surgical decompression. The pathophysiology is anatomical and mechanical in nature — there is no recognized pharmacological pathway connecting a topical antiseptic/disinfectant mechanism to nerve root decompression or neurological recovery.

The extremely high TxGNN score (99.99%) for this indication — alongside a similarly high ranking for multiple anatomically unrelated conditions (neurogenic bladder, uveitis, IBS, and several ciliary body diseases) — strongly suggests a **false positive driven by training data sparsity** rather than a genuine biological signal. The absence of any supporting clinical trials or literature across all 10 predicted indications further reinforces this interpretation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Amylmetacresol currently has **no registered products** in India. No authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Note:** Both key warnings and contraindications data are unavailable for this drug in the current evidence pack. No drug-drug interaction records were identified. Full safety assessment should be completed before any further evaluation stage.

---

## Full Prediction Overview (All 10 Ranked Indications)

All 10 predicted indications are at Evidence Level **L5** with a **Hold** recommendation. The pattern of predictions is notable:

| Rank | Disease | TxGNN Score | Key Concern |
|------|---------|-------------|-------------|
| 1 | Cauda Equina Syndrome | 99.99% | No mechanistic link to antiseptic MOA; surgical condition |
| 2 | Neurogenic Bladder (obsolete term) | 99.96% | Obsolete OMOP/MONDO terminology; no MOA link |
| 3 | Irritable Bowel Syndrome | 99.89% | Non-selective gut microbiome disruption risk |
| 4 | Ciliary Body Disease | 99.70% | Ocular safety unknown; broad disease category |
| 5 | Panuveitis | 99.68% | Ocular penetration/safety data absent |
| 6 | Iris Disease | 99.63% | Likely KG ontology cluster artifact |
| 7 | Infectious Anterior Uveitis | 99.57% | Conceptually closest match but no ocular delivery data |
| 8 | Uveitis | 99.53% | Overlaps with rank 5–7; ontology clustering suspected |
| 9 | Ciliary Body Cancer | 99.46% | No antineoplastic mechanism; high false-positive risk |
| 10 | Benign Neoplasm of Ciliary Body | 99.45% | Minimal pharmacological treatment need |

**Pattern observation:** Ranks 4–10 are dominated by ocular anterior segment diseases (ciliary body, iris, uvea), strongly suggesting a **knowledge graph ontology clustering artifact** rather than distinct independent predictions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications lack any supporting clinical or preclinical evidence (L5), the drug's mechanism of action is undocumented in the current evidence pack, and the prediction pattern shows clear signs of knowledge graph false positives (ontology clustering in ocular diseases, training data sparsity in neurological indications). There is currently no scientific basis to advance any of these candidates to the next evaluation stage.

**To proceed, the following is needed:**

- **MOA characterization**: Obtain full mechanism of action data from DrugBank or primary literature to determine whether Amylmetacresol has any systemic or non-antiseptic biological activities
- **False positive investigation**: Audit TxGNN training data density for the 10 predicted disease nodes to confirm the clustering artifact hypothesis
- **Ontology deduplication**: Consolidate the 7 ocular indications (ranks 4–10) into a single representative candidate (suggested: Infectious Anterior Uveitis, rank 7) before further evaluation
- **Safety baseline**: Retrieve the full CDSCO/TFDA package insert or equivalent regulatory label to complete the S1 safety pre-screening
- **India registration review**: Determine whether any Amylmetacresol-containing products (combination lozenges) are registered in India under combination drug categories, which may have been missed by single-ingredient search
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

