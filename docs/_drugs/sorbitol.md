---
layout: default
title: Sorbitol
parent: Model Prediction Only (L5)
nav_order: 784
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Sorbitol: predicted new indication Exercise-induced malignant hyperthermia (evidence level L5). Approved use: Not available"
monitor_inn: "Sorbitol"
predicted_indications: ["exercise-induced malignant hyperthermia"]
---

# Sorbitol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Sorbitol: From an Unspecified Original Indication to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Sorbitol is a sugar alcohol used as an osmotic agent, laxative and excipient. In India it is marketed as an infusion product, but no approved indication text is available.
The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the registration record contains no approved indication text) |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sorbitol is a sugar alcohol used as an osmotic agent, laxative and pharmaceutical excipient. No original indication is documented for the Indian registration, so the relationship between an original and a new indication cannot be established.

No biological pathway is known to link sorbitol to malignant hyperthermia. That condition is typically driven by dysregulated calcium release in skeletal muscle (RYR1 or CACNA1S variants), and the standard treatment is dantrolene. The high score may reflect graph proximity or shared-neighbour artifacts, such as sorbitol's use as an excipient or osmotic agent in related formulations, rather than a true therapeutic effect. This should be treated as a hypothesis only, requiring mechanistic validation before any further consideration.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 38111 | Celemix Infusion (Claris Lifesciences Ltd) | Bottle of 1000 ml infusion | Not stated |

## Safety Considerations

- **Contraindications (from the TxGNN knowledge graph, not label text)**: Active peptic ulcer disease.
- **Drug Interactions** (2 found):
  - **Tolevamer**: Major
  - **Lamivudine**: Moderate

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high model prediction score. There are no clinical trials or publications, no documented mechanism, and no known biological link between sorbitol and malignant hyperthermia. The standard treatment (dantrolene) works through a different pathway.

**To proceed, the following is needed:**
- Mechanism of action data for sorbitol and a plausible biological link to skeletal-muscle calcium dysregulation
- The approved indication and the package insert warnings and contraindications for the Indian product (Registration No. 38111)
- Preclinical or literature evidence supporting any effect in malignant hyperthermia
- Assessment of whether the prediction is an artifact of sorbitol's role as an excipient or osmotic agent in the knowledge graph
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

