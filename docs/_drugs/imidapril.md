---
layout: default
title: Imidapril
parent: Model Prediction Only (L5)
nav_order: 426
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Imidapril: predicted new indication Pulmonary hypertension with unclear multifactorial mechanism (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "Imidapril"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "Braddock syndrome"]
---

# Imidapril
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

## Imidapril: From Hypertension to Pulmonary Hypertension (Unclear Multifactorial Mechanism)
{: .text-alpha }

## One-Sentence Summary

Imidapril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, imidapril is an ACE inhibitor prodrug, converted in the body to its active form imidaprilat. It lowers angiotensin II and reduces systemic vascular resistance, which explains its efficacy in hypertension.

A theoretical link to pulmonary hypertension exists through the renin-angiotensin system, which may play a role in pulmonary vascular remodelling. However, this link rests on general class knowledge only. ACE inhibitors have not shown reliable benefit in pulmonary arterial hypertension, and the high TxGNN score is a computational prediction without clinical confirmation.

Other predicted indications were also reviewed. All have the same L5 evidence level and a Hold recommendation:

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.78% | Possible RAS involvement, but systemic vasodilation could worsen ventilation-perfusion matching in hypoxic lung disease |
| 3 | Malignant hypertensive renal disease | 99.76% | Close to the approved indication and biologically plausible, but it is a subtype of hypertension, usually managed with parenteral agents, with a risk of acute kidney injury |
| 4 | Malignant renovascular hypertension | 99.76% | Strongly RAS-driven, but ACE inhibitors can precipitate acute renal failure in bilateral renal artery stenosis or a solitary kidney |
| 5 | Braddock syndrome | 99.70% | No evident mechanistic rationale; likely reflects knowledge-graph proximity |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 224165 | Tanatril 10mg Tablet | Strip of 10 tablets | Not specified |
| 220107 | Tanatril 5mg Tablet | Strip of 10 tablets | Not specified |

Both licences are valid single-ingredient oral products from Elder Pharmaceuticals Ltd.

## Safety Considerations

- **Drug Interactions**: The only interaction entry compiled is pharmacological, with the target angiotensin-converting enzyme (ACE), which reflects its mechanism of action. No drug-drug interaction severity levels were available.
- **Class-related cautions (from the repurposing assessment)**: ACE inhibitors carry a risk of acute kidney injury or acute renal failure in bilateral renal artery stenosis or a solitary kidney. In hypoxic lung disease, systemic vasodilation may worsen ventilation-perfusion matching.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting clinical trials or publications (L5). The mechanistic link is theoretical, and ACE inhibitors have not shown reliable benefit in pulmonary arterial hypertension. Package insert safety data are also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India Pharma source (a blocking gap for safety screening)
- Detailed mechanism of action data (MOA) from DrugBank
- Preclinical or clinical evidence for imidapril in pulmonary hypertension
- Assessment of renal and haemodynamic safety in the target population
- Route compatibility and similarity-to-original-indication analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

