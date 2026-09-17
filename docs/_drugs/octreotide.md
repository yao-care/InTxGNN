---
layout: default
title: Octreotide
parent: Model Prediction Only (L5)
nav_order: 607
evidence_level: L5
indication_count: 10
---

# Octreotide
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

# Octreotide: From Somatostatin-Analog Therapy to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Octreotide is a somatostatin analog; the original approved indication is not recorded in this dataset (the drug is currently not marketed in Taiwan). The TxGNN model's top-ranked prediction is **Vulvar Inverted Follicular Keratosis**, but this candidate is currently supported by **0 clinical trials** and **0 publications** — it is a pure model score with no corroborating evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — `original_indications` is empty and no MOA data is recorded (DG002) |
| Predicted New Indication | Vulvar Inverted Follicular Keratosis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | Not marketed (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for octreotide is not available in this dataset (flagged as data gap DG002, High severity). Other entries in this evidence pack indicate octreotide acts as a somatostatin analog capable of suppressing pituitary and gastroenteropancreatic hormone secretion (e.g., ACTH suppression), but none of this pharmacology has any documented connection to follicular/keratinocyte proliferation pathology.

For this specific top-ranked candidate, the evidence pack's own mechanistic assessment is explicit: *"No known relationship exists between somatostatin receptor signaling and the pathology of follicular hyperkeratosis; the high TxGNN score is likely a non-specific association from knowledge-graph embeddings (possibly via skin/tumor-related nodes), with no clinical or literature support."* In other words, the model itself flags this prediction as biologically implausible rather than mechanistically reasonable.

For transparency: the dataset also contains lower-ranked candidates with at least partial literature support (e.g., rank 4, Addison disease, L4/S1) — but their rationale text explicitly notes octreotide's ACTH-suppressing effect would work *against* the treatment direction needed in adrenal insufficiency. None of the ten candidates in this pack currently present a coherent, evidence-backed repurposing rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Taiwan Market Information

Octreotide is currently not marketed in Taiwan (`market_status: Not marketed`, 0 registrations). No license records are available.

## Safety Considerations

Key warnings and contraindications are not available in this dataset (blocked by data gap DG001 — TFDA label warnings/contraindications, Blocking severity; this prevents entry into the S1 safety pre-assessment stage).

**Drug Interactions**: 272 interactions are on record. The illustrative subset provided is uniformly classified as **Moderate** severity (source: ddinter) and is concentrated in antidiabetic agents — consistent with octreotide's known effect on glucose homeostasis:
- Insulins: glargine, degludec, detemir, aspart, glulisine, regular, isophane (inhalation)
- GLP-1 agonists: Semaglutide, Dulaglutide, Albiglutide
- SGLT2 inhibitors: Dapagliflozin, Canagliflozin, Empagliflozin
- Sulfonylureas: Glimepiride, Chlorpropamide
- DPP-4 inhibitors: Alogliptin, Linagliptin
- Biguanide: Metformin
- Alpha-glucosidase inhibitor: Acarbose

Blood glucose monitoring should be anticipated when octreotide is combined with any of these agents, pending full label review.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN candidate (Vulvar Inverted Follicular Keratosis) has zero clinical trial or literature support and is explicitly flagged by the evidence pack's own mechanistic analysis as a likely non-specific graph-embedding artifact rather than a biologically plausible signal. Combined with the Blocking-severity gap in TFDA label safety data (DG001), this candidate cannot proceed past the initial hypothesis stage.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking) — required before any S1 safety pre-assessment
- Verified mechanism of action data (DG002, High)
- Any preclinical, case-report, or trial evidence specifically linking somatostatin receptor pathways to follicular/keratinocyte pathology
- If this indication cannot be substantiated, evaluate other candidates in the same prediction set (e.g., rank 4, Addison disease) with a corrected mechanistic direction, since the current data actually points toward a risk of harm rather than benefit for that candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

