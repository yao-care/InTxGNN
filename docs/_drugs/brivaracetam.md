---
layout: default
title: Brivaracetam
parent: Model Prediction Only (L5)
nav_order: 117
evidence_level: L5
indication_count: 1
monitor_inn: "Brivaracetam"
predicted_indications: ["beta-ketothiolase deficiency"]
last_modified_at: 2026-11-24
description: "Brivaracetam: predicted new indication beta-ketothiolase deficiency (evidence level L5). In India: at least 20 listed products"
---

# Brivaracetam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Brivaracetam: SV2A modulator (antiseizure drug) → beta-ketothiolase deficiency
{: .text-alpha }

## One-Sentence Summary

Brivaracetam is an antiseizure medicine that acts on the synaptic vesicle protein SV2A.
The TxGNN model predicts it may be relevant to **beta-ketothiolase deficiency**, but **no clinical trials and no publications** were found to support this direction, so it rests on the model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | beta-ketothiolase deficiency |
| TxGNN Prediction Score | 0.9914 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for brivaracetam: "The precise mechanism by which BRIVIACT exerts its anticonvulsant activity is not known. Brivaracetam displays a high and selective affinity for synaptic vesicle protein 2A (SV2A) in the brain, which may contribute to the anticonvulsant effect." ([DailyMed: Briviact (brivaracetam) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3cf2f439-0e97-443e-8e33-25ecef616f6c), label version 2026-11-05; accessed 2026-11-19.) Based on general knowledge, brivaracetam binds the synaptic vesicle protein SV2A and is used as an antiseizure drug.

Beta-ketothiolase deficiency is an inborn error of ketone body and isoleucine metabolism caused by an enzyme defect. It is not primarily a seizure disorder, and SV2A modulation has no plausible mechanistic connection to this enzyme defect. The high score is most likely an artifact of the model rather than a true therapeutic signal, and no clinical or literature evidence supports it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

At least 20 valid single-ingredient licences are recorded.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 25833 | Britzilam 50 Tablet | Strip of 15 tablets | Valid |
| 25994 | Britam 50 Tablet | Strip of 10 tablets | Valid |
| 26026 | Brivgard 50 Tablet | Strip of 10 tablets | Valid |
| 26061 | Brivapride 50mg Tablet | Strip of 10 tablets | Valid |
| 26357 | Brivanext 50mg Tablet | Strip of 10 tablets | Valid |
| 26427 | Briv 25mg Tablet | Strip of 10 tablets | Valid |
| 26854 | Briviact 75mg Tablet | Strip of 14 tablets | Valid |
| 26977 | Brivajoy 100 Tablet | Strip of 14 tablets | Valid |
| 27346 | Brivissa 50 Tablet | Strip of 10 tablets | Valid |
| 27411 | Brivetam 50 Tablet | Strip of 14 tablets | Valid |
| 27865 | Brivanext 25 Tablet | Strip of 10 tablets | Valid |
| 28184 | Brivatab 100mg Tablet | Strip of 10 tablets | Valid |
| 28397 | Brivatab 25mg Tablet | Strip of 10 tablets | Valid |
| 28419 | Brivup 10mg Injection | Vial of 5 ml Injection | Valid |
| 28471 | Bripca 75mg Tablet | Strip of 14 tablets | Valid |
| 29576 | Bivogrid 50mg Tablet | Strip of 10 tablets | Valid |
| 29863 | Brivatop 50mg Tablet | Strip of 10 tablets | Valid |
| 233993 | Vivocet 50 Tablet | Strip of 15 tablets | Valid |
| 236024 | Vivocet 25mg Tablet | Strip of 14 tablets | Valid |
| 236616 | Vivocet 75 Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 69 interactions are recorded. Examples at moderate level include morphine, opium, dronabinol, nabilone, metoclopramide, promethazine, clopidogrel, ethanol, sibutramine, difenoxin and diphenoxylate (additive central nervous system effects are a general concern with sedating agents). Minor-level examples include proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, pantoprazole, dexlansoprazole), tolbutamide, chlorpropamide and cilostazol.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting trials or publications, and there is no plausible mechanistic link between SV2A modulation and this metabolic enzyme defect. It should not advance on the current evidence.

**To proceed, the following is needed:**
- Any preclinical or clinical study that directly addresses beta-ketothiolase deficiency
- A credible mechanistic rationale linking brivaracetam to the disease
- Detailed mechanism of action data
- Package insert warnings and contraindications from the India licences

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for brivaracetam is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Briviact (brivaracetam) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3cf2f439-0e97-443e-8e33-25ecef616f6c) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

