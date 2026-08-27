---
layout: default
title: Iopromide
parent: 僅模型預測 (L5)
nav_order: 342
evidence_level: L5
indication_count: 10
---

# Iopromide
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

# Iopromide: From Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Iopromide is a non-ionic iodinated contrast agent used exclusively for diagnostic medical imaging (such as CT and angiography) — it has no established therapeutic indication.
The TxGNN model predicts it may be relevant for **Osteoarthritis Susceptibility** (rank #1 with a score of **99.57%**), yet all 10 predicted indications carry an **L5 evidence level** with **0 clinical trials** and only sparse imaging-related literature — none of which supports therapeutic use.
The high prediction scores are most likely artifacts of imaging co-occurrence bias within the knowledge graph, not genuine drug-disease relationships.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Diagnostic contrast agent for medical imaging (CT, angiography) |
| Predicted New Indication | Osteoarthritis Susceptibility |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Iopromide (DrugBank DB09156) is a water-soluble, non-ionic, low-osmolality iodinated contrast agent. It functions by attenuating X-rays due to its iodine content, thereby enhancing the visibility of vascular structures and soft tissues in radiographic imaging. It has no receptor binding, no enzyme inhibition, and no known intracellular signalling activity — it is pharmacologically inert beyond its physical radiodensity property.

Detailed mechanism of action (MOA) data is not available in the current Evidence Pack. Based on its known pharmacology, Iopromide is administered intravenously or intra-arterially to improve contrast in CT scans and angiographic procedures. There is no plausible biochemical pathway by which this compound would modulate cartilage degradation, joint inflammation, chondrocyte survival, or any other process relevant to osteoarthritis pathogenesis.

The TxGNN model's high prediction score for musculoskeletal conditions (osteoarthritis, rheumatoid arthritis, brachyolmia, pseudoachondroplasia, etc.) almost certainly reflects **diagnostic imaging co-occurrence bias**: contrast agents are frequently administered during imaging studies of patients who have these conditions, creating spurious drug-disease associations in the knowledge graph. The `repurposing_rationale` embedded in the Evidence Pack for every top-10 prediction explicitly identifies this as a likely false positive. This pattern — a pure diagnostic reagent scoring highly for a broad range of unrelated diseases — is a well-recognised failure mode of graph-based drug repurposing models.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **Note on adjacent evidence:** Literature retrieved for lower-ranked indications (osteoarthritis rank #2, rheumatoid arthritis rank #3, hemoglobinopathy rank #9) uniformly confirms that Iopromide appears in these contexts exclusively as a **diagnostic contrast agent**, not as a therapeutic intervention. PMID [16628721](https://pubmed.ncbi.nlm.nih.gov/16628721/) is particularly notable: it documents a **cerebrovascular adverse event** in a sickle cell patient who received a low-osmolar contrast agent, representing a safety warning rather than therapeutic evidence.

---

## India Market Information

Iopromide currently has no drug registrations in India. No authorisation records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Known class-level consideration (contrast agents):** Iodinated contrast agents as a class carry risks of contrast-induced nephropathy (CIN), hypersensitivity/anaphylactoid reactions, and thyroid dysfunction due to iodine load. In patients with sickle cell disease, low-osmolar contrast agents have been associated with cerebral vaso-occlusive events (see PMID [16628721](https://pubmed.ncbi.nlm.nih.gov/16628721/)). These are safety signals — not therapeutic indications — and should be considered if Iopromide is used for any future imaging-based application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Iopromide receive an L5 evidence level (model prediction only, no supporting studies), and the mechanistic rationale embedded in the Evidence Pack itself identifies these predictions as highly likely false positives driven by diagnostic imaging co-occurrence in the training data. Iopromide is a pharmacologically inert contrast medium with no established or plausible therapeutic mechanism for any of the predicted conditions.

**To proceed, the following is needed:**

- **Do not pursue repurposing without mechanistic basis:** Confirm via DrugBank API whether any off-target pharmacological activity has been identified for Iopromide (e.g., effects on signalling pathways beyond contrast enhancement).
- **Knowledge graph debiasing:** Investigate whether the TxGNN training graph contains imaging procedure nodes that are co-linked to both contrast agents and musculoskeletal disease nodes — if so, this batch of predictions should be flagged as systematic false positives and excluded from the repurposing pipeline.
- **Pipeline-level filter:** Consider implementing a pre-filter that excludes diagnostic agents (ATC code V08: Contrast media) from the repurposing candidate set, as these compounds lack therapeutic pharmacodynamics by design.
- **CDSCO regulatory review:** If future imaging applications of Iopromide in India are planned, obtain the CDSCO package insert for class-specific safety information (contrast-induced nephropathy, hypersensitivity protocols).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

