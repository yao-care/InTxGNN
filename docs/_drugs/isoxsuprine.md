---
layout: default
title: Isoxsuprine
parent: Model Prediction Only (L5)
nav_order: 455
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
monitor_inn: "Isoxsuprine"
predicted_indications: ["benign prostatic hyperplasia (disease)", "venous thoracic outlet syndrome", "arterial thoracic outlet syndrome", "blue toe syndrome", "atheroembolism of kidney", "hemangioendothelioma", "angiodysplasia of stomach", "respiratory failure", "neurogenic thoracic outlet syndrome", "idiopathic spontaneous coronary artery dissection"]
description: "Isoxsuprine: predicted new indication Benign prostatic hyperplasia (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Isoxsuprine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Isoxsuprine: Benign prostatic hyperplasia (disease)
{: .text-alpha }

## One-Sentence Summary

Isoxsuprine is a vasodilator originally used for cerebrovascular disorder, vascular disease and Raynaud disease.
The TxGNN model predicts it may be effective for **benign prostatic hyperplasia (BPH)**,
but **no clinical trials and no directly relevant publications** currently support this prediction, so it rests on the computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Benign prostatic hyperplasia (disease) |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Isoxsuprine is generally known as a beta-adrenergic agonist with direct vascular smooth muscle relaxant activity, consistent with its use in peripheral and cerebral vascular conditions.

A possible link to BPH would be relaxation of smooth muscle in the prostate and bladder neck. However, BPH is mainly treated with alpha-1 blockade or 5-alpha-reductase inhibition, and beta-agonism is not an established mechanism for it. The very high TxGNN score is a computational prediction only and is not backed by trials or literature, so the mechanistic rationale remains weak.

Other top-ranked predictions (arterial, venous and neurogenic thoracic outlet syndrome, blue toe syndrome, renal atheroembolism, hemangioendothelioma, gastric angiodysplasia, respiratory failure, spontaneous coronary artery dissection) are also L5 predictions with no supporting clinical evidence. Several carry mechanistic or safety concerns. For example, a vasodilator could worsen angiodysplasia, and a beta-agonist is the opposite of the beta-blockers favored in coronary artery dissection.

## India Market Information

Isoxsuprine is marketed in India with 20 valid single-ingredient registrations. The compiled data contain no approved indication text for these products. Main examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 28536 | BIOPRIN 10MG TABLET | Strip of 10 tablets | Not stated in available data |
| 215478 | Tidilan 20 Tablet | Strip of 30 tablets | Not stated in available data |
| 89898 | Feprox 40mg Tablet SR | Strip of 10 SR tablets | Not stated in available data |
| 30521 | BIOPRIM 40MG TABLET SR | Strip of 10 SR tablets | Not stated in available data |
| 240203 | Vasodilan 40mg Tablet ER | Strip of 10 ER tablets | Not stated in available data |

All products are oral tablets (standard, sustained-release or extended-release).

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: hypotensive disorder.
- **Drug Interactions**: 20 interactions were identified, all graded Moderate. Main ones include:
  - SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin
  - Prostacyclin-class vasodilators: epoprostenol, iloprost, selexipag, treprostinil
  - Phenothiazine-type antihistamines and antiemetics: promethazine, methdilazine, thiethylperazine, alimemazine
  - Other: amifostine, nitrous acid, pentoxifylline, brimonidine (ophthalmic and topical), topical minoxidil, ozanimod, procarbazine
  
  Many of these overlap in blood-pressure-lowering effects.

Please refer to the package insert for warnings and other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The BPH prediction is supported only by the model score (L5). There are no clinical trials or relevant publications, the mechanism is not established, and the vasodilator and hypotensive effects add a safety consideration.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a clearer rationale for prostate or bladder-neck smooth muscle effects
- Preclinical or early clinical evidence of isoxsuprine in BPH or lower urinary tract symptoms
- Package insert warnings and contraindications from the India licence documents
- A safety assessment of hypotension and the interactions above, particularly in older men likely to be on antihypertensives or other BPH drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

