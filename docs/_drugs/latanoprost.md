---
layout: default
title: Latanoprost
parent: Model Prediction Only (L5)
nav_order: 473
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Latanoprost: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Open-angle glaucoma"
---

# Latanoprost
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

# Latanoprost: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Latanoprost is a prostaglandin eye drop originally used to treat open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**,
but currently **no clinical trials** and **no publications** support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma; ocular hypertension |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, latanoprost is a prostaglandin F2-alpha analogue that lowers intraocular pressure by increasing uveoscleral outflow. Its efficacy in open-angle glaucoma is established, so a mechanistic overlap with other glaucomas is plausible.

However, primary hereditary glaucoma (for example, primary congenital glaucoma) is typically driven by developmental abnormalities of the trabecular meshwork and anterior chamber angle, and it often requires surgery. The prediction is likely driven by the closeness of this disease to the approved indication (open-angle glaucoma) in the knowledge graph, rather than by new biology.

**Other predicted candidates.** The model also ranked nine other conditions. Most have no clear mechanistic link (for example, visceral calciphylaxis, the three thoracic outlet syndromes, angiodysplasia of the stomach, blue toe syndrome and lymphangiectasis). The most mechanistically credible one is **hypotrichosis simplex of the scalp** (score 99.81%), because prostaglandin F2-alpha analogues are known to prolong the hair growth phase and stimulate eyelash growth. This is class-level reasoning only, and no supporting trials or literature were found. Congenital hypotrichosis milia (99.71%) is a similar but more speculative case.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 127735 | Latochek 5mg Eye Drop | Packet of 5 ml Eye Drop | Not specified |
| 108470 | Ioprost Eye Drop | Packet of 1 ml Eye Drop | Not specified |
| 121113 | Latoprost Eye Drop | Packet of 2.5 ml Ophthalmic Solution | Not specified |
| 121652 | Lacoma PF Eye Drop BAK Free | Bottle of 2.5 ml Eye Drop | Not specified |
| 243783 | Xalatan Eye Drop | Packet of 2.5 ml Eye Drop | Not specified |

A total of 20 valid single-ingredient registrations exist. All are ophthalmic eye drops or ophthalmic solutions.

## Safety Considerations

- **Conditions flagged as contraindication-related in the knowledge graph**: uveitis, iris disease, ciliary body disease, panuveitis, macular retinal edema, cystoid macular edema, iritis, conjunctivitis (including acute contagious conjunctivitis). These come from drug-disease relationship data, not from label text, and should be verified against the package insert.
- **Drug Interactions**: 121 potential interactions are recorded, but none has a severity level assigned. Examples include calcitriol, glimepiride, doxycycline, atropine, triamcinolone, prednisone, simvastatin and metformin. Given the low systemic exposure of topical ophthalmic use, their clinical relevance is unclear.

Please refer to the package insert for warnings and formal contraindications, as label information was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no clinical trials or literature behind it (Evidence Level L5). The biology of hereditary glaucoma, which is usually developmental and surgical, differs from that of the approved indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulatory source (a blocking gap for safety screening)
- Detailed mechanism of action data (for example, from DrugBank)
- A literature and trial search specific to latanoprost in primary hereditary or congenital glaucoma
- If pursuing a non-glaucoma direction, a focused evaluation of hypotrichosis (hair or lash growth) as the most mechanistically plausible alternative
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

