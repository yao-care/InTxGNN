---
layout: default
title: Empagliflozin
parent: Model Prediction Only (L5)
nav_order: 303
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Empagliflozin: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Empagliflozin"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia"]
---

# Empagliflozin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Empagliflozin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome
{: .text-alpha }

## One-Sentence Summary

Empagliflozin is an oral SGLT2 inhibitor originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Empagliflozin is known to be an SGLT2 inhibitor that lowers blood glucose by blocking glucose reabsorption in the kidney. Its efficacy in type 2 diabetes is well established, but that mechanism has no demonstrated link to the new indication.

Stiff person syndrome is an autoimmune neurological disorder involving GABAergic signalling and antibodies against glutamic acid decarboxylase (GAD65). A possible connection exists through the association of GAD65 autoimmunity with type 1 diabetes and other autoimmune conditions. This link is indirect and speculative, and no supported mechanistic link was identified.

The prediction should be treated with caution. The closely related prediction, focal stiff limb syndrome, receives an identical score (99.06%), which suggests the model is propagating a shared disease-neighbourhood signal rather than independent evidence. The third-ranked prediction, opsismodysplasia (score 99.03%), is also unsupported by any trials or publications.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Twenty valid single-ingredient registrations are on file. The main ones are listed below. The data compiled for this report contain no approved indication text for these products.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 113870 | Jardiance 10mg Tablet | Strip of 10 tablets | Boehringer Ingelheim |
| 113866 | Jardiance 25mg Tablet | Strip of 10 tablets | Boehringer Ingelheim |
| 94211 | Glyxambi 25mg/5mg Tablet | Strip of 10 tablets | Boehringer Ingelheim |
| 72505 | Empaone 10mg Tablet | Strip of 10 tablets | MSN Laboratories |
| 162085 | Oboravo 10mg Tablet | Strip of 10 tablets | Cipla Ltd |

## Safety Considerations

- **Drug Interactions**: 369 interactions were identified in total. Examples at Moderate level include phenylephrine, acebutolol, acetazolamide, formoterol, pseudoephedrine, nifedipine, epinephrine, ethinylestradiol, hydrocortisone, salbutamol, ethanol, furosemide and fosinopril. Minor-level examples include topical hydrocortisone and topical alclometasone.

Please refer to the package insert for warnings and contraindications, as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications (evidence level L5), no verified mechanistic link, and the drug's package insert safety data are not yet available. A high TxGNN score alone is not enough to justify moving forward.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India Pharma source, which currently block safety screening
- Mechanism of action data from DrugBank, to allow a proper mechanistic-link analysis
- A literature and trial search specific to stiff person syndrome and SGLT2 inhibitors, including preclinical or mechanistic studies
- Assessment of whether the identical scores for classic stiff person syndrome and focal stiff limb syndrome reflect a model artefact
- Review of the safety profile in the target population, given that stiff person syndrome patients often have autoimmune comorbidities
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

