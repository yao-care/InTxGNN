---
layout: default
title: Safinamide
parent: Model Prediction Only (L5)
nav_order: 760
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-20
monitor_inn: "Safinamide"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration"]
description: "Safinamide: predicted new indication Rasmussen subacute encephalitis (evidence level L5). In India: 6 listed products (6 not discontinued)"
---

# Safinamide
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

## Safinamide: Rasmussen subacute encephalitis
{: .text-alpha }

## One-Sentence Summary

Safinamide is a reversible MAO-B inhibitor, originally used to treat Parkinson disease and related parkinsonian syndromes.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**,
but **no clinical trials and no publications** currently support this direction. It is a model-based prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (6 of 6) – CDSCO approval status is not included in this data |
| Number of Listed Products | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for safinamide: "The precise mechanism by which XADAGO exerts its therapeutic effects in PD is unknown. XADAGO is an inhibitor of monoamine oxidase B (MAO-B). Inhibition of MAO-B activity, by blocking the catabolism of dopamine, is thought to result in an increase in dopamine levels and a subsequent increase in dopaminergic activity in the brain." ([DailyMed: Xadago (safinamide mesylate) prescribing information, MDD US Operations LLC, a subsidiary of Supernus Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c4d65f28-983f-42b4-bb23-023ae0fe81b2), label version 2026-10-05; accessed 2026-11-19.) Based on known pharmacology, safinamide is a reversible MAO-B inhibitor that also blocks voltage-gated sodium channels and modulates glutamate release. Its efficacy in Parkinson disease is established.

Rasmussen encephalitis is a rare, immune-mediated chronic encephalitis. It causes inflammation in one cerebral hemisphere and refractory focal seizures. In theory, sodium channel blockade and reduced glutamate release could dampen neuronal hyperexcitability and seizures. However, nothing suggests safinamide addresses the underlying T-cell-mediated pathology, so the mechanistic link is speculative. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Two other candidates were also predicted:
- **Myelitis** (score 0.9946): the possible rationale is neuroprotection through glutamate inhibition, sodium channel blockade and reduced oxidative stress. This is untested in myelitis, and the causes of myelitis vary widely.
- **PLA2G6-associated neurodegeneration** (score 0.9922): the parkinsonian features overlap with safinamide's original use, so symptomatic benefit in later-onset cases with parkinsonism is plausible. This is the most coherent of the three, but there is still no direct evidence, and disease-modifying effects are unsupported.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 247222 | Zafimove 100 Tablet (Torrent Pharmaceuticals Ltd) | Strip of 10 tablets | Not listed |
| 201255 | Safion 100mg Tablet (Intas Pharmaceuticals Ltd) | Strip of 10 tablets | Not listed |
| 243852 | Xafinact 100 Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not listed |
| 243785 | Xafinact 50 Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not listed |
| 246661 | Zafimove 50mg Tablet (Torrent Pharmaceuticals Ltd) | Strip of 10 tablets | Not listed |

One further registration, 200331 (Safion 50mg Tablet, Intas Pharmaceuticals Ltd), is also valid. All six registrations are single-ingredient oral tablets.

## Safety Considerations

**Drug Interactions**: 110 interactions were identified in total. The first 20 retrieved include one Major and 19 Moderate interactions.
- **Major**: Bupropion
- **Moderate, antidiabetic agents**: chlorpropamide, glimepiride, acetohexamide, nateglinide, repaglinide, empagliflozin, and multiple insulin products (aspart, degludec, detemir, glargine, glulisine, human isophane, human regular, human inhaled rapid-acting)
- **Moderate, other**: isometheptene, diethylpropion, phentermine, metoclopramide, rosuvastatin

Please refer to the package insert for warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials or publications and the mechanistic link is speculative. The evidence level is L5. Package insert warnings and contraindications are also missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source
- Detailed mechanism of action data (for example from DrugBank)
- A literature and trial search for Rasmussen encephalitis, and for PLA2G6-associated neurodegeneration, which is the most plausible alternative candidate
- Preclinical or mechanistic evidence showing an effect on the immune-mediated pathology
- Route and dosage compatibility assessment for the new indication

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Xadago (safinamide mesylate) prescribing information, MDD US Operations LLC, a subsidiary of Supernus Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c4d65f28-983f-42b4-bb23-023ae0fe81b2) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

