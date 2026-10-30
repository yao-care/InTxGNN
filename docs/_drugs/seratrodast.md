---
layout: default
title: Seratrodast
parent: Model Prediction Only (L5)
nav_order: 768
evidence_level: L5
indication_count: 9
monitor_inn: "Seratrodast"
predicted_indications: ["migraine disorder", "pulmonary hypertension", "rheumatoid arthritis", "migraine with brainstem aura", "kyphoscoliotic heart disease", "brachydactyly-syndactyly syndrome", "leprosy", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "atrophoderma vermiculata"]
last_modified_at: 2026-10-30
description: "Seratrodast: predicted new indication Migraine disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Seratrodast
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Seratrodast: Migraine disorder
{: .text-alpha }

## One-Sentence Summary

Seratrodast is a thromboxane A2 receptor antagonist that is marketed in India as an oral tablet, although the licence records in the data compiled for this report do not state an approved indication.
The TxGNN model predicts it may be useful for **migraine disorder**, but **no clinical trials and no publications** currently support this prediction.
It is a model-based prediction only, so the evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9954 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (3 of 3) – CDSCO approval status is not included in this data |
| Number of Registrations | 3 (valid: 3) |
| Number of Approvals | 3 licences (single-ingredient products) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Seratrodast is generally described as a thromboxane A2 receptor antagonist, and it is marketed in Japan for asthma. That description is general background and is not taken from the Indian licence records.

Thromboxane and other eicosanoids have been loosely linked to vascular tone and platelet activation, which are relevant to migraine. This link is speculative. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, and it is not evidence of efficacy.

Other diseases on the prediction list show a similar pattern:
- **Pulmonary hypertension** (score 0.9947) has the most biologically plausible rationale. Thromboxane A2 is a potent vasoconstrictor and promotes vascular remodelling. The only supporting item is a 1998 narrative review of eicosanoids in paediatric practice, which is indirect and does not test seratrodast.
- **Rheumatoid arthritis** (0.9945) has a general eicosanoid-inflammation rationale, but thromboxane receptor antagonism is not an established anti-rheumatic mechanism.
- **Migraine with brainstem aura** (0.9943) and **kyphoscoliotic heart disease** (0.9939) score highly according to the TxGNN model (deep learning); these scores may reflect similarities the model learned between related diseases (migraine and pulmonary hypertension respectively), not biological evidence.
- **Brachydactyly-syndactyly syndrome, leprosy, colobomatous microphthalmia-rhizomelic dysplasia syndrome and atrophoderma vermiculata** have no plausible mechanistic link identified and are likely TxGNN model (deep learning) artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For migraine disorder, currently no related literature available.

For the second-ranked prediction, pulmonary hypertension, one indirect item exists:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9711442](https://pubmed.ncbi.nlm.nih.gov/9711442/) | 1998 | Review | Drugs | Narrative review of eicosanoids (prostaglandins, thromboxane, leukotrienes) and their inhibitors in paediatric practice; does not test seratrodast directly |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 200144 | Seretra 80 Tablet (Zuventus Healthcare Ltd) | Strip of 10 tablets | Not stated in the licence record |
| Registration No. 202314 | Seradair 80mg Tablet (Fourrts India Laboratories Pvt Ltd) | Strip of 10 tablets | Not stated in the licence record |
| Registration No. 1874 | Alatro Tablet (Lupin Ltd) | Strip of 10 tablets | Not stated in the licence record |

All three licences are valid single-ingredient products, and all are for oral use.

---

## Safety Considerations

Please refer to the package insert for safety information. No warning, contraindication or drug interaction data were available in the data compiled for this report, and the package insert has not yet been obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction rests only on a model score. No clinical trials or publications address migraine, so the evidence level is L5. Safety information and the approved indication are also missing.

**To proceed, the following is needed:**
- Obtain and review the package insert for the Indian products to confirm the approved indication, warnings and contraindications (this is currently a blocking gap).
- Obtain mechanism of action data from DrugBank.
- Search for preclinical or clinical studies of thromboxane receptor antagonism in migraine.
- If a repurposing direction is pursued, consider pulmonary hypertension as a research question, since it has the most plausible mechanism. A direct study of seratrodast in that condition is still needed.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

