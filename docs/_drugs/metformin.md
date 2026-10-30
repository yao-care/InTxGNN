---
layout: default
title: Metformin
parent: Model Prediction Only (L5)
nav_order: 532
evidence_level: L5
indication_count: 5
monitor_inn: "Metformin"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
last_modified_at: 2026-10-30
description: "Metformin: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
---

# Metformin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Metformin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome
{: .text-alpha }

## One-Sentence Summary

Metformin is a widely used oral glucose-lowering medicine. According to the knowledge graph, its recorded indications are type 2 diabetes mellitus and diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**, but **no clinical trials and no publications** were found to support this prediction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (relation recorded in the knowledge graph; the licence records contain no approved indication text) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | At least 20 licences (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Metformin is known to act mainly by activating AMPK and reducing hepatic glucose production, with mild immunomodulatory effects. These actions are not established to be linked to the pathology of stiff person syndrome.

Stiff person syndrome is an autoimmune disorder of GABAergic neurotransmission, usually with anti-GAD65 antibodies. The only plausible connection is that anti-GAD antibodies are also seen alongside autoimmune diabetes. That link is indirect and is not a therapeutic rationale for the neurological disease.

The second-ranked prediction, focal stiff limb syndrome, has an identical score (0.9945). The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The prediction should be treated as a hypothesis for screening only.

Other lower-ranked predictions have the same limitation, with no supporting studies:

| Rank | Predicted Disease | Score | Comment |
|---|---|---|---|
| 2 | Focal stiff limb syndrome | 0.9945 | Variant of the stiff person spectrum; same mechanistic gap |
| 3 | Opsismodysplasia | 0.9940 | Speculative PI3K/AKT pathway link (INPPL1/SHIP2); paediatric skeletal disorder |
| 4 | Thiamine-responsive dysfunction syndrome | 0.9940 | Link is to diabetes as a symptom, not the underlying defect |
| 5 | Drug-induced localized lipodystrophy | 0.9906 | Plausible insulin-sensitisation link, but the condition is a local tissue reaction |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

At least 20 valid licences are recorded for metformin-containing products, and the list may be partial. None of the licence records includes approved indication text. Up to 5 are shown below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 195976 | Ramyglyn M 500mg/20mg Tablet | Strip of 10 tablets | Not stated in the licence record |
| 94183 | Galvus Met 50mg/500mg Tablet | Strip of 15 tablets | Not stated in the licence record |
| 75709 | Endoformin 1000mg Tablet SR | Strip of 10 sustained-release tablets | Not stated in the licence record |
| 226264 | Tenlivas M 1000mg/20mg Tablet ER | Strip of 10 extended-release tablets | Not stated in the licence record |
| 81184 | Efiglin-M 1000 Tablet SR | Strip of 15 sustained-release tablets | Not stated in the licence record |

All listed forms are oral.

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** Contraindication relations are recorded for liver failure, liver disease, kidney disease, pancreatitis, gallbladder disease, congestive heart failure, adrenocortical insufficiency, thymus gland disease, pyoureter, and a range of pituitary hormone deficiency and hypogonadotropic hypogonadism conditions (including Kallmann syndrome and Sheehan syndrome). These come from the graph, not from the package insert, and should be confirmed against the label.
- **Drug interactions:** 642 interactions are recorded. Major-level examples include **acetazolamide** and **ethanol**. Moderate-level examples include dolutegravir, abemaciclib, phenylephrine, ranitidine, formoterol, pseudoephedrine, ketorolac, nifedipine, epinephrine, ibuprofen, ethinylestradiol, hydrocortisone, salbutamol, hydrochlorothiazide and acetohexamide.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a TxGNN model (deep learning) score alone. No trial or publication addresses classic stiff person syndrome, and no established mechanistic link exists between metformin and its autoimmune GABAergic pathology. The evidence level is therefore L5.

**To proceed, the following is needed:**
- Preclinical or mechanistic evidence connecting metformin to the stiff person syndrome pathway
- A literature and trial search specific to stiff person syndrome and metformin
- Mechanism of action data for metformin from DrugBank
- Package insert warnings and contraindications from the India regulatory source, to allow safety screening
- Review of the identical scores (0.9945) for classic stiff person syndrome and focal stiff limb syndrome, since the TxGNN model (deep learning) may reflect similarities it learned between related diseases, not biological evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

