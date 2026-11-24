---
layout: default
title: Dicyclomine
parent: Model Prediction Only (L5)
nav_order: 263
evidence_level: L5
indication_count: 2
monitor_inn: "Dicyclomine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)"]
last_modified_at: 2026-11-24
description: "Dicyclomine: predicted new indication cauda equina syndrome (evidence level L5). In India: at least 20 listed products"
---

# Dicyclomine
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

## Dicyclomine: Antimuscarinic antispasmodic → cauda equina syndrome
{: .text-alpha }

## One-Sentence Summary

Dicyclomine is an antimuscarinic antispasmodic that relaxes smooth muscle.
The TxGNN model predicts it may be useful for **cauda equina syndrome**, with a score of **0.9966**.
There are currently **no clinical trials and no publications** supporting this direction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | cauda equina syndrome |
| TxGNN Prediction Score | 0.9966 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for dicyclomine: "Dicyclomine relieves smooth muscle spasm of the gastrointestinal tract. Animal studies indicate that this action is achieved via a dual mechanism: a specific anticholinergic effect (antimuscarinic) at the acetylcholine-receptor sites with approximately 1/8 the milligram potency of atropine ( in vitro, guinea pig ileum); and a direct effect upon smooth muscle (musculotropic) as evidenced by dicyclomine’s antagonism of bradykinin- and histamine-induced spasms of the isolated guinea pig ileum." ([DailyMed: dicyclomine hydrochloride prescribing information, Slate Run Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e20a1ccf-2f3a-4872-811e-d93fb56b8e83), label version 2026-11-13; accessed 2026-11-19.) Based on its known drug class, dicyclomine is an antimuscarinic/antispasmodic agent that relaxes smooth muscle.

A plausible but unverified link is symptomatic relief of the neurogenic bladder and bowel dysfunction (detrusor overactivity, spasm) that can accompany cauda equina syndrome. It would not treat the underlying nerve root compression, which requires urgent surgical decompression.

The prediction is a model output only. No studies were found that examine dicyclomine in this disease. Anticholinergics can also worsen urinary retention, which is common in cauda equina syndrome with an areflexic bladder, so safety is a specific concern.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Dicyclomine is marketed in India. All 20 licences in the data compiled for this report are valid, and none are cancelled. The list may be partial. The licence records carry no approved-indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 31947 | Brenum 10 mg/40 mg Drop | Packet of 10 ml Drop | Valid |
| 35066 | Colispas Paed Oral Drops | Packet of 10 ml Oral Drops | Valid |
| 35486 | Cyclomin 20mg Tablet | Strip of 10 tablets | Valid |
| 41667 | Cyclomax Plus 20mg/325mg Tablet | Strip of 10 tablets | Valid |
| 42039 | Clospas Oral Drops | Bottle of 15 ml Oral Drops | Valid |
| 44825 | Cefospas Tablet | Strip of 10 tablets | Valid |
| 53091 | Cyclod P 20mg/325mg Tablet | Strip of 10 tablets | Valid |
| 65724 | Dicdic-P Tablet | Strip of 10 tablets | Valid |
| 96726 | Glenpar Spas Tablet | Strip of 10 tablets | Valid |
| 114514 | Jonyspas Plus 20mg/250mg Tablet | Strip of 10 tablets | Valid |
| 183488 | Qspam 20mg/325mg Tablet | Strip of 10 tablets | Valid |
| 187821 | Remigan 10 mg/40 mg Drop | Packet of 15 ml Drop | Valid |
| 197344 | Ranic DH 10mg/150mg Tablet | Strip of 10 tablets | Valid |
| 198905 | Renalpane 10mg/250mg Tablet | Strip of 10 tablets | Valid |
| 201309 | Spam M 10mg/250mg Tablet | Strip of 10 tablets | Valid |
| 206238 | Sarispas M 20mg/250mg Tablet | Strip of 10 tablets | Valid |
| 209194 | Spascare DS 20 mg/250 mg Tablet | Strip of 10 tablets | Valid |
| 210511 | Spasmosar 10mg/250mg Tablet | Strip of 10 tablets | Valid |
| 212603 | Spaspres 10mg/250mg Tablet | Strip of 10 tablets | Valid |
| 221552 | Topspas Injection | Vial of 2 ml Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 344 interactions are recorded. Examples of moderate-level interactions include botulinum toxin type A, fentanyl, chlorpheniramine, codeine, tramadol, amitriptyline, hyoscyamine, loperamide, and ethanol. Additive anticholinergic and sedative effects are the main concern.
- **Disease-related cautions** (from drug-disease contraindication records, not label text): glaucoma (angle-closure), benign prostatic hyperplasia, liver and kidney disease, hepatic encephalopathy, porphyria, coronary artery disease, hypertension, and blood disorders such as neutropenia, agranulocytosis, thrombocytopenia, and anemia.
- Anticholinergic action may worsen urinary retention, which is relevant in cauda equina syndrome.

Please also refer to the package insert for label warnings and contraindications, which are not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score (0.9966) but no supporting trials or literature, and the proposed use would only address symptoms, not the underlying cause. The anticholinergic effect on urinary retention is a specific safety concern.

**To proceed, the following is needed:**
- Published or registered studies of dicyclomine in cauda equina syndrome or closely related neurogenic bladder/bowel dysfunction
- Mechanism of action data
- Package insert warnings and contraindications for the India-marketed products
- A safety assessment of urinary retention risk in this population

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: dicyclomine hydrochloride prescribing information, Slate Run Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e20a1ccf-2f3a-4872-811e-d93fb56b8e83) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

