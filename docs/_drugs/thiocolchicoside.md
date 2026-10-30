---
layout: default
title: Thiocolchicoside
parent: Model Prediction Only (L5)
nav_order: 830
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
description: "Thiocolchicoside: predicted new indication Insomnia (evidence level L5). Approved use: Not stated in the registration data compiled for this report (the dru…"
monitor_inn: "Thiocolchicoside"
predicted_indications: ["insomnia (disease)", "alcohol withdrawal delirium"]
---

# Thiocolchicoside
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Thiocolchicoside: From Muscle Relaxant Use to Insomnia
{: .text-alpha }

## One-Sentence Summary

Thiocolchicoside is a muscle relaxant that is currently marketed in India under 20 valid registrations.
The TxGNN model predicts it may be effective for **insomnia**, but **no clinical trials and no publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data compiled for this report (the drug is generally described as a muscle relaxant) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology knowledge, thiocolchicoside is a muscle relaxant that is reported to act on GABA-A receptors (as an antagonist) and glycine receptors. It can also have effects on the central nervous system, and it is known to lower the seizure threshold.

A link to sleep regulation through GABAergic or glycinergic modulation is conceivable, but it is speculative. The direction of effect is unclear: the drug could be sleep-promoting, or it could be arousing or pro-convulsant. No trial or publication supports this link, and the reasoning rests on general pharmacology knowledge only.

A second prediction, **alcohol withdrawal delirium** (score 0.9921, also L5, Hold), was also generated. It is conceptually relevant because alcohol withdrawal involves GABA hypofunction. However, GABA-A antagonism and pro-convulsant potential would be a safety concern in a condition that already carries seizure risk, so the predicted benefit may be mechanistically contradictory. Benzodiazepines are also the established standard of care.

## India Market Information

All 20 registrations are valid single-ingredient entries. Approved indication text is not recorded in the data compiled for this report. The first 5 are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 221416 | Thionip AP 4mg/100mg/325mg Tablet | Strip of 10 tablets | Not recorded |
| 54302 | Cuflam PTH 4mg/100mg/325mg Tablet | Strip of 10 tablets | Not recorded |
| 219450 | Thionaid-P Tablet | Strip of 10 tablets | Not recorded |
| 222549 | T Mr 8mg Capsule | Strip of 10 capsules | Not recorded |
| 65424 | D Pain TC Capsule | Strip of 10 capsules | Not recorded |

All forms are oral (tablets, capsules and soft gelatin capsules).

## Safety Considerations

Please refer to the package insert for safety information.

Based on general pharmacology knowledge (not the compiled data), thiocolchicoside may lower the seizure threshold. This is particularly relevant to the alcohol withdrawal delirium prediction, and it also calls for caution in any CNS-related repurposing.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no supporting clinical trials or literature (L5). The mechanism is unclear, and the possible pro-convulsant effect makes the direction of benefit uncertain.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator (needed before any safety screening)
- Mechanism of action data, for example from DrugBank
- Preclinical or early clinical evidence of a sleep-related effect, including its direction
- A seizure-risk assessment, especially before considering alcohol withdrawal delirium
- Registered indication text for the marketed products, to confirm the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

