---
layout: default
title: Lobeglitazone
parent: Model Prediction Only (L5)
nav_order: 496
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Lobeglitazone: predicted new indication Focal stiff limb syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Lobeglitazone"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia"]
---

# Lobeglitazone
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

## Lobeglitazone: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome
{: .text-alpha }

## One-Sentence Summary

Lobeglitazone is a PPAR-gamma agonist (thiazolidinedione) originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**,
but **no clinical trials and no publications** currently support this direction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (from the knowledge graph; the India license record does not state an indication) |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.17% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, lobeglitazone is a thiazolidinedione that activates PPAR-gamma. This improves insulin sensitivity and has anti-inflammatory effects, and its efficacy in type 2 diabetes is the basis of its current use.

Focal stiff limb syndrome is a rare variant of the stiff-person spectrum. It is usually considered autoimmune and is linked to impaired GABAergic or glycinergic inhibition. The only conceivable route to a benefit is PPAR-gamma-mediated immunomodulation, which is speculative and unvalidated. No direct mechanistic link has been established.

The high TxGNN score (99.17%) reflects a pattern found by the model in the knowledge graph. It is not evidence of efficacy.

Other predictions produced for this drug have equally weak support:
- **Classic stiff person syndrome** (score 99.17%): associated with anti-GAD65 autoimmunity and with autoimmune comorbidities such as type 1 diabetes. Any benefit would be hypothetical, and glycemic management is a separate matter from disease modification.
- **Thiamine-responsive dysfunction syndrome** (score 99.10%): involves defective thiamine transport. Insulin sensitization might address the diabetic component but would not correct the underlying defect.
- **Opsismodysplasia** (score 99.08%): a skeletal dysplasia caused by INPPL1 mutations. Thiazolidinediones are associated with reduced bone mass and increased fracture risk, which is a potential safety concern in this condition.

All four predictions are at evidence level L5 with a Hold recommendation.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 133365 | Lobg Tablet (Glenmark Pharmaceuticals Ltd) | Strip of 10 tablets (oral) | Not stated in the license record |

## Safety Considerations

Please refer to the package insert for safety information.

One point from the compiled data: thiazolidinediones as a class are associated with reduced bone mass and increased fracture risk. This matters most for any skeletal indication such as opsismodysplasia.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication rests only on a model score. There are no clinical trials or publications, no established mechanistic link, and the safety data are incomplete. The evidence is insufficient to justify moving forward.

**To proceed, the following is needed:**
- Mechanism of action data for lobeglitazone (for example, from DrugBank) to allow a proper mechanistic-link analysis
- Package insert warnings and contraindications from the India regulatory source, which are required before any safety screening
- Any preclinical or clinical evidence linking PPAR-gamma agonism to stiff-person spectrum disorders
- A review of whether the bone-safety signal of thiazolidinediones is relevant to the intended population
- Confirmation of route compatibility and the approved indication text for the licensed product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

