---
layout: default
title: Isosorbide Dinitrate
parent: Model Prediction Only (L5)
nav_order: 452
evidence_level: L5
indication_count: 10
monitor_inn: "Isosorbide dinitrate"
predicted_indications: ["alopecia", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "pulmonary hypertension", "diffuse alopecia areata", "vascular disease", "hypertrichosis (disease)", "kyphoscoliotic heart disease", "visceral calciphylaxis", "venous thoracic outlet syndrome"]
last_modified_at: 2026-10-30
description: "Isosorbide Dinitrate: predicted new indication Alopecia (evidence level L5). Approved use: Not stated in the licence records"
---

# Isosorbide Dinitrate
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

## Isosorbide Dinitrate: From a Marketed Nitrate Vasodilator (Indication Not Stated in Licence Records) to Alopecia
{: .text-alpha }

## One-Sentence Summary

Isosorbide dinitrate is a nitric oxide (NO) donor that is marketed in India under many licences, but the licence records compiled for this report do not state an approved indication. The TxGNN model predicts it may be useful for **alopecia**, with a very high score. There are **0 clinical trials** and **0 publications** for this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | At least 20 (the list may be partial) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Isosorbide dinitrate is generally understood as an NO donor. NO release raises cGMP and relaxes vascular smooth muscle.

A speculative link is that this vasodilation could improve scalp blood flow, which would be conceptually similar to how minoxidil is thought to act. The very high score likely reflects network proximity to other vasoactive drugs rather than direct biological evidence. No trial or publication supports the link, so it should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other Predicted Indications With More Evidence

Alopecia is the top-ranked prediction, but two lower-ranked predictions have supporting data.

| Predicted Indication | TxGNN Score | Evidence Level | Supporting Data | Assessment |
|------|------|------|------|------|
| Pulmonary hypertension | 0.9998 | L3 | No registered trials; about 20 publications, mostly small hemodynamic studies (1979–1996) and recent work (2017 animal study, 2025 bolus study) showing lower pulmonary artery pressure | Research question. There is no outcome evidence of clinical benefit. Hypoxemia and hypotension are concerns. |
| Vascular disease | 0.9997 | L5 under the strict rule | Six trials listed, only one of which tests isosorbide dinitrate directly: NCT02789033, a Phase 3 trial (n=68, completed) of isosorbide dinitrate spray with chitosan in diabetic foot ulcers. Literature is mostly on coronary and general hemodynamics. | The category is broad and the trial studies diabetic foot ulcer, not "vascular disease" itself. The data pack's L2 grade is not supported under the rule that a study must address the predicted disease directly. |

The remaining predictions are all model-only (L5): congenital hypotrichosis milia, hypotrichosis simplex of the scalp, diffuse alopecia areata, hypertrichosis, kyphoscoliotic heart disease, visceral calciphylaxis and venous thoracic outlet syndrome.

---

## India Market Information

At least 20 valid single-ingredient licences were found, and the list may be partial. The licence records do not include approved indication text. The 5 main entries are shown below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 200688 | Sorbitrate HF Tablet | Strip of 10 tablets | Abbott |
| 199607 | Sorbitrate 10 Tablet | Strip of 50 tablets | Abbott |
| 199525 | Sorbitrate 5 Tablet | Strip of 50 sublingual tablets | Abbott |
| 50750 | Cardicap 20mg Capsule TR | Strip of 25 capsules (TR) | Sun Pharmaceutical Industries Ltd |
| 107825 | Isordil 10 Tablet | Strip of 10 tablets | Ipca Laboratories Ltd |

All listed forms are oral, including sublingual, tablet, capsule and controlled-release forms. No topical form appears in the records.

---

## Safety Considerations

Label warnings and contraindications are not available in the compiled data. Please refer to the package insert for these.

- **Contraindication relations recorded in the knowledge graph (not label text):** hypotensive disorder, hypertrophic cardiomyopathy, coronary artery disease, myocardial infarction, stroke and cerebrovascular disorders, cerebral infarction, intracerebral hemorrhage, intracranial hypertension, pseudotumor cerebri, anemia and hemoglobinopathy, hyperthyroidism and Graves disease, and slow acetylation. These are database associations and should be checked against the official label.
- **Drug interactions:** 141 interactions were found. Moderate-level ones include bupropion, morphine, opium, dronabinol, nabilone, sapropterin, and the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin). Rosiglitazone is also moderate. Omeprazole is minor.
- **Other concerns noted in the analysis:** nitrate tolerance, hypotension, and concomitant PDE5 inhibitors (contraindicated).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The alopecia prediction has no supporting trials or publications, and the vasodilation hypothesis is speculative. The evidence level is L5. Safety data are incomplete, and the knowledge-graph contraindication list is long.

**To proceed, the following is needed:**
- Mechanistic and preclinical evidence linking NO donors to hair growth or scalp perfusion
- Package insert warnings and contraindications from the India licences, and the approved indication text
- Mechanism of action data from DrugBank
- A formulation and route plan, since all marketed forms are oral or sublingual and a scalp indication would likely need a topical product
- If the team wants a better-supported direction, re-prioritizing pulmonary hypertension (L3) or diabetic foot ulcer (NCT02789033, with its results verified) for further review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

