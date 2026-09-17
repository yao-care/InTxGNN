---
layout: default
title: Prucalopride
parent: Model Prediction Only (L5)
nav_order: 703
evidence_level: L5
indication_count: 10
---

# Prucalopride
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

# Prucalopride: From Chronic Idiopathic Constipation to Hypoalphalipoproteinemia

## One-Sentence Summary

Prucalopride is a highly selective 5-HT4 receptor agonist; a formal "original indication" field was not available in the regulatory data, but internal rationale notes in this evidence pack identify it as approved for **chronic idiopathic constipation**. The TxGNN model assigns a very high prediction score (**99.82%**) for **Hypoalphalipoproteinemia**, but this direction is currently supported by **0 clinical trials** and **0 publications** — the model's own mechanistic rationale explicitly states there is no known pharmacological link between 5-HT4 agonism and lipoprotein metabolism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Idiopathic Constipation (from evidence-pack rationale text; not present in formal `original_indications`/license fields — data gap) |
| Predicted New Indication | Hypoalphalipoproteinemia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for prucalopride is not available (`original_moa` is a data gap). Based on known pharmacology, prucalopride acts as a 5-HT4 receptor agonist that stimulates cholinergic enteric neurons to enhance colonic motility, with proven efficacy in chronic idiopathic constipation.

For Hypoalphalipoproteinemia, however, the evidence pack's own repurposing rationale is explicit that **no mechanistic connection exists**: "Prucalopride is a 5-HT4 receptor agonist acting on gastrointestinal motility, with no known pharmacological mechanistic link to lipoprotein metabolism (HDL-related disease)." There is no plausible pathway from 5-HT4-mediated gut motility to HDL/lipoprotein regulation, and the prediction is not corroborated by any clinical trial or literature evidence — it reflects the TxGNN model's knowledge-graph score alone.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Prucalopride currently has **no marketing authorization in India** (0 registrations, market status: Not Marketed). No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (Label warnings, contraindications, and DDI data are not available in this evidence pack — flagged as a **Blocking** data gap requiring TFDA/CDSCO label retrieval before any S1 safety assessment.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is evidence level L5 — a model prediction with no supporting clinical trials, no literature, and no plausible mechanistic rationale linking the drug's known pharmacology to the predicted indication. There is no basis to advance this candidate beyond the model-scoring stage.

**To proceed, the following is needed:**
- Mechanistic or preclinical evidence connecting 5-HT4 agonism to lipoprotein/HDL metabolism
- Any observational or case-level data on lipid parameters in patients treated with prucalopride
- DrugBank MOA confirmation (currently a High-severity data gap)
- TFDA/CDSCO label data — warnings, contraindications, DDI (currently a Blocking data gap; required before any safety screening)

**Note:** Within the same evidence pack, two other candidates — Amyloidosis (rank 6) and Primary Amyloidosis (rank 9) — reach evidence level L4 / decision stage S1 ("Research Question"), supported by literature on GI motility disorders associated with amyloid-related autonomic neuropathy. These may warrant separate evaluation as they carry a stronger (though still indirect) mechanistic rationale than Hypoalphalipoproteinemia.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

