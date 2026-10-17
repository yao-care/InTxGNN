---
layout: default
title: Amantadine
parent: Model Prediction Only (L5)
nav_order: 44
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Amantadine: predicted new indication Rasmussen subacute encephalitis (evidence level L5). Approved use: Parkinson disease and related parkinsonian and dystonic disorders"
monitor_inn: "Amantadine"
predicted_indications: ["Rasmussen subacute encephalitis", "transaldolase deficiency", "myelitis", "PLA2G6-associated neurodegeneration"]
---

# Amantadine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Amantadine: From Parkinson Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Amantadine was originally used to treat Parkinson disease and related movement disorders.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**,
but **no clinical trials and no publications** currently support this specific prediction (the signal is model-based only).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease and related parkinsonian and dystonic disorders (the approved indication text for the Indian licences is not available) |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, amantadine is an NMDA receptor antagonist with dopaminergic activity, and its efficacy in Parkinson disease and related movement disorders is established. Mechanistically, it may be applicable to Rasmussen encephalitis.

Rasmussen encephalitis is a rare, progressive inflammatory brain disease that causes severe seizures and loss of function on one side of the brain. Glutamate receptor-mediated excitotoxicity and autoimmune mechanisms have been proposed in this disease. NMDA receptor antagonism could therefore plausibly be relevant. This link is theoretical and unverified, and the prediction rests on the model score alone.

For context, other top-ranked predictions are myelitis (score 99.24%, indirect evidence from post-polio syndrome fatigue studies) and PLA2G6-associated neurodegeneration (score 99.23%, extrapolated from a case report in a related disorder). Both rank below Rasmussen encephalitis by score but have some literature, whereas Rasmussen encephalitis has none.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 39651 | Comantrel 100 Capsule | Strip of 10 capsules | Not stated |
| 73591 | Ensorex 100mg Capsule | Strip of 15 capsules | Not stated |
| 38074 | Comantrel-T Tablet | Strip of 10 tablets | Not stated |
| 174876 | Parkitidin ER 193 Tablet | Strip of 10 extended-release tablets | Not stated |
| 73243 | Ensorex 50mg Tablet | Strip of 15 tablets | Not stated |

All 12 registrations are valid single-ingredient products (none cancelled). Only the first 5 are listed here.

---

## Safety Considerations

- **Contraindications / disease associations flagged in the knowledge graph** (not label text): multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, epilepsy, kidney disease, pyoureter, congestive heart failure, psychotic disorder, schizophreniform disorder, mental disorder, schizoaffective disorder, melanoma, angle-closure glaucoma, closed-angle glaucoma, substance-related disorder, substance abuse/dependence, atopic eczema, dermatitis.
  - Epilepsy is particularly relevant, because seizures are the dominant feature of Rasmussen encephalitis.
- **Drug Interactions**: 93 interactions were identified in total. Notable examples:
  - **Major**: bupropion.
  - **Moderate**: anticholinergic agents (atropine, scopolamine, hyoscyamine, glycopyrronium, dicyclomine, clidinium, mepenzolate, methscopolamine, propantheline, trospium), metoclopramide, and bowel-preparation products (polyethylene glycol with electrolytes, picosulfuric acid, sodium sulfate).

Please refer to the package insert for label warnings, as these were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials or publications for Rasmussen encephalitis, so the evidence is model-based only (L5). The knowledge graph also lists epilepsy as a contraindication, which needs careful consideration in a seizure-dominant disease.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) and a documented link to Rasmussen encephalitis pathology
- A targeted literature search for amantadine or NMDA antagonists in Rasmussen encephalitis, and a search for registered trials
- Package insert warnings and contraindications from Indian manufacturers, including approved indication text
- A safety assessment of amantadine in patients with epilepsy
- Consideration of the other predictions (myelitis, PLA2G6-associated neurodegeneration) as research questions, since they have some indirect literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

