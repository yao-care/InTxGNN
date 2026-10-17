---
layout: default
title: Metformin
parent: Model Prediction Only (L5)
nav_order: 532
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Metformin: predicted new indication Focal stiff limb syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Metformin"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
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

# Metformin: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Metformin is a widely used oral medicine originally indicated for type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**,
but **no clinical trials and no publications** were found to support this prediction, so it rests on the model's graph-based score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, metformin is an established oral antidiabetic agent, its efficacy in type 2 diabetes is proven, and its commonly described actions (AMPK activation, reduced hepatic glucose production, modest immunomodulation) are the only basis for any mechanistic argument in the new indication.

Focal stiff limb syndrome belongs to the stiff person spectrum, which involves impaired GABAergic inhibition and often anti-GAD65 autoimmunity. No established link exists between metformin's known actions and this pathology. The high score most likely reflects a shared autoimmune or GAD65/diabetes comorbidity pattern in the knowledge graph, not a demonstrated therapeutic mechanism.

Other top-ranked predictions show the same pattern: classic stiff person syndrome (99.45%), opsismodysplasia (99.40%), thiamine-responsive dysfunction syndrome (99.40%) and drug-induced localized lipodystrophy (99.06%). All are L5 with no supporting studies. Of these, drug-induced localized lipodystrophy is the most biologically plausible, because metformin has been studied for insulin sensitization in other lipodystrophy forms. It would still need a targeted literature search.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Metformin has 20 valid registrations in India (all single-ingredient entries per the regulatory data). Approved indication text was not provided for these products. Five representative authorizations:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 195976 | Ramyglyn M 500mg/20mg Tablet | Strip of 10 tablets | Ramylabs Health Care |
| 94183 | Galvus Met 50mg/500mg Tablet | Strip of 15 tablets | Novartis India Ltd |
| 75709 | Endoformin 1000mg Tablet SR | Strip of 10 SR tablets | Precia Pharma |
| 226264 | Tenlivas M 1000mg/20mg Tablet ER | Strip of 10 ER tablets | Kasnav Pharma |
| 215983 | Torglip M SR 500 Tablet | Strip of 10 SR tablets | Torrent Pharmaceuticals Ltd |

All products are oral tablets (immediate-release, SR, ER, XR and PR forms).

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: liver failure, liver disease, kidney disease, pancreatitis, gallbladder disease, congestive heart failure, adrenocortical insufficiency, thymus gland disease, pyoureter, and a range of pituitary deficiency and hypogonadotropic hypogonadism conditions (including hypopituitarism, Kallmann syndrome and Sheehan syndrome).
- **Drug Interactions**: 642 interactions were recorded. Major-level examples include **acetazolamide** and **ethanol**. Moderate-level examples include dolutegravir, abemaciclib, phenylephrine, ranitidine, formoterol, pseudoephedrine, ketorolac, nifedipine, epinephrine, ibuprofen, ethinylestradiol, hydrocortisone, salbutamol and hydrochlorothiazide.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a graph-based model score. There are no clinical trials or publications, and no recognised mechanistic link between metformin and focal stiff limb syndrome. The score likely reflects diabetes/GAD65 autoimmunity comorbidity rather than a therapeutic effect.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently blocking for safety screening)
- Detailed mechanism of action data (MOA)
- A targeted literature and trial search for metformin in stiff person spectrum disorders
- Preclinical or mechanistic evidence for any link to GABAergic or autoimmune pathways
- A comparison against alternative predictions (e.g., drug-induced localized lipodystrophy) that may have a more plausible mechanism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

