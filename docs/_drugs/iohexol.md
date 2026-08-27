---
layout: default
title: Iohexol
parent: 僅模型預測 (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
---

# Iohexol
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

# Iohexol: From Contrast Imaging Agent to Insomnia

## One-Sentence Summary

Iohexol is a non-ionic iodinated contrast medium widely used in diagnostic radiology — including myelography, angiography, and body cavity imaging — rather than a conventional therapeutic drug.
The TxGNN model predicts it may be relevant to **Insomnia**, achieving a model score of **99.87%**,
yet **zero clinical trials and zero publications** specifically support this as a therapeutic direction; the high score almost certainly reflects a knowledge graph false positive.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Iodinated contrast agent for medical imaging (myelography, angiography, CT) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Iohexol is a low-osmolality, non-ionic iodinated contrast agent. Its only pharmacological mechanism is X-ray attenuation via the high atomic weight of iodine — it does not bind to receptors, modulate neurotransmitters, or exert any physiological effect beyond transient osmotic load during excretion. It is considered pharmacologically inert for therapeutic purposes.

Insomnia is a disorder of sleep initiation or maintenance, typically managed through GABAergic agents (benzodiazepines, Z-drugs), melatonin agonists, orexin receptor antagonists, or behavioural therapies. There is no plausible mechanistic bridge between iohexol's contrast properties and central nervous system sleep regulation.

The TxGNN high prediction score (99.87%) almost certainly originates from knowledge graph co-occurrence artefacts: patients undergoing contrast imaging procedures (e.g., CT, myelography) have documented comorbidities including anxiety and sleep disorders, creating indirect graph edges. This is a characteristic false positive pattern for diagnostic-tool compounds in KG-based repurposing models — the model conflates clinical co-occurrence with therapeutic relevance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Iohexol in insomnia.

---

## Literature Evidence

Currently no related literature available for Iohexol in insomnia.

---

## India Market Information

Iohexol has no registered products in India at this time (0 authorisations on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Appendix: All Predicted Indications — Pattern Analysis

All 10 TxGNN-predicted indications for iohexol share a common verdict. The table below summarises the full prediction list to document the systematic evaluation:

| Rank | Predicted Indication | TxGNN Score | Trials | Publications | Evidence Level | Decision | Key Reason for Rejection |
|------|---------------------|-------------|--------|--------------|---------------|----------|--------------------------|
| 1 | Insomnia | 99.87% | 0 | 0 | L5 | Hold | No CNS/sleep mechanism; KG co-occurrence artefact |
| 2 | Anxiety | 99.25% | 6 (all Grade C) | 6 (all off-target) | L5 | Hold | All trials use iohexol as GFR probe or imaging tool, not anxiety treatment |
| 3 | Rheumatoid Arthritis | 98.87% | 1 (Phase 1, GFR probe) | 0 | L5 | Hold | NCT01484561 uses iohexol to measure renal clearance, not treat RA |
| 4 | Antithrombin Deficiency Type 2 | 98.75% | 0 | 0 | L5 | Hold | No anticoagulant mechanism; vascular imaging co-occurrence |
| 5 | Factor V Excess / Spontaneous Thrombosis | 98.73% | 0 | 0 | L5 | Hold | No anticoagulant activity; indirect KG vascular-imaging linkage |
| 6 | Sleep Disorder (Initiating and Maintaining) | 98.61% | 0 | 0 | L5 | Hold | Duplicate of Rank 1 in different terminology (SNOMED) |
| 7 | Heparin Cofactor 2 Deficiency | 98.61% | 0 | 0 | L5 | Hold | Rare coagulopathy; no protein-supplementation mechanism |
| 8 | Fibromyalgia | 98.46% | 0 | 0 | L5 | Hold | Central sensitisation disorder; no analgesic/neuromodulatory mechanism |
| 9 | Conjunctivitis | 98.45% | 0 | 0 | L5 | Hold | No ophthalmic formulation; theoretical iodine antimicrobial effect unvalidated |
| 10 | Tendinitis | 98.44% | 0 | 14 (all imaging use) | L5 | Hold | All 14 publications use iohexol for arthrography/tenography diagnosis; steroid co-injected is the therapeutic agent |

---

## Conclusion and Next Steps

**Decision: Hold (across all 10 predicted indications)**

**Rationale:**
Iohexol is a pharmacologically inert contrast medium with no therapeutic mechanism applicable to any of the 10 TxGNN-predicted indications. All retrieved clinical trials (7 total) and publications (20 total) use iohexol exclusively as a diagnostic tool — a GFR measurement probe, an imaging contrast agent, or an arthrographic medium — never as the therapeutic intervention. The uniformly high TxGNN scores reflect a systematic knowledge graph artefact: patients requiring contrast imaging often carry comorbidities (insomnia, anxiety, chronic kidney disease, rheumatic conditions), creating false co-occurrence edges in the KG. This is a recognised limitation of graph-based repurposing models applied to diagnostic agents.

**To proceed, the following would be needed:**

- **Fundamental reassessment**: Iohexol should be flagged at the pipeline ingestion level as a diagnostic agent and excluded from therapeutic repurposing candidate lists
- **Model calibration**: The KG should be annotated to distinguish diagnostic-use compounds from therapeutic compounds, preventing similar false positives for other contrast media (iopamidol, iodixanol, gadolinium chelates, etc.)
- **Root cause analysis**: Investigate which KG node/edge types are generating the co-occurrence signal to improve future prediction specificity for this drug class

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

