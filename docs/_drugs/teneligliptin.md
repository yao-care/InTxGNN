---
layout: default
title: Teneligliptin
parent: Model Prediction Only (L5)
nav_order: 816
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-30
description: "Teneligliptin: predicted new indication Opsismodysplasia (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Teneligliptin"
predicted_indications: ["opsismodysplasia", "thiamine-responsive dysfunction syndrome", "focal stiff limb syndrome", "classic stiff person syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
---

# Teneligliptin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Teneligliptin: From Type 2 Diabetes Mellitus to Opsismodysplasia
{: .text-alpha }

## One-Sentence Summary

Teneligliptin is a DPP-4 inhibitor originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **opsismodysplasia**, a rare skeletal dysplasia,
but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction is based on computation only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, teneligliptin targets dipeptidyl peptidase 4 (DPP4) and also acts on the related enzymes DPP8 and DPP9. Its efficacy in type 2 diabetes is established, and it is approved for that use in Japan and South Korea.

Opsismodysplasia is a rare skeletal dysplasia caused by INPPL1 (SHIP2) mutations, which affect PI3K/AKT signaling and endochondral ossification. No direct mechanistic link between DPP-4 inhibition and this pathway has been established. The high TxGNN score (0.994) is a computational association only, and the missing mechanism-of-action data further limits mechanistic reasoning.

Other predictions for this drug follow a similar pattern. They include thiamine-responsive dysfunction syndrome, classic stiff person syndrome, focal stiff limb syndrome and several localized lipodystrophies (drug-induced, centrifugal, pressure-induced and idiopathic). Most appear to be driven by links to diabetes, such as comorbidity or insulin injection context, rather than by evidence of therapeutic benefit. None has any supporting clinical trial or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Teneligliptin is marketed in India as oral single-ingredient tablets. The data compiled for this report show 20 valid registrations and no cancelled ones. The approved indication text is not available for these entries. The five main registrations are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 220836 | Tenepace Tablet | Strip of 10 tablets | Meyer Organics Pvt Ltd |
| 221924 | Teniglip 20mg Tablet | Strip of 10 tablets | Biodiscovery Lifesciences Pvt Ltd |
| 204429 | Supraglip Tablet | Strip of 10 tablets | Oaknet Healthcare Pvt Ltd |
| 246699 | Zita-Pio Tablet | Strip of 10 tablets | Glenmark Pharmaceuticals Ltd |
| 215017 | Tendia Tablet | Strip of 15 tablets | Eris Lifesciences Ltd |

## Safety Considerations

- **Drug Interactions**: No drug-drug interactions are recorded. The three entries retrieved are pharmacological targets of teneligliptin (DPP4, DPP8 and DPP9), not interacting drugs.

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature and no plausible mechanistic link between DPP-4 inhibition and opsismodysplasia (Evidence Level L5). The same is true for all other predicted indications.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank, to support mechanistic analysis
- Package insert warnings and contraindications from the India regulatory source, which are needed for safety screening
- Preclinical or mechanistic studies testing whether DPP-4 inhibition affects INPPL1/SHIP2-related PI3K/AKT signaling or endochondral ossification
- Assessment of route compatibility and similarity to the original indication, both still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

