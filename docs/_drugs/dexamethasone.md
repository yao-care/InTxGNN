---
layout: default
title: Dexamethasone
parent: Model Prediction Only (L5)
nav_order: 249
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Dexamethasone"
predicted_indications: ["alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "alopecia universalis onychodystrophy vitiligo", "prolapse of lacrimal gland"]
description: "Dexamethasone: predicted new indication Alopecia mucinosa (evidence level L5). In India: at least 20 listed products"
---

# Dexamethasone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Dexamethasone: Alopecia mucinosa
{: .text-alpha }

## One-Sentence Summary

Dexamethasone is a synthetic glucocorticoid with anti-inflammatory and immunosuppressive activity.
The TxGNN model predicts it may be useful for **alopecia mucinosa**, but **no clinical trials and no publications** were found to support this prediction. It rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Alopecia mucinosa |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for dexamethasone: "Dexamethasone is a corticosteroid with anti-inflammatory effects and low mineralocorticoid activity. The precise mechanism of action in multiple myeloma is unknown. Dexamethasone induces apoptosis of multiple myeloma cells." ([DailyMed: Hemady (dexamethasone) prescribing information, Edenbridge Pharmaceuticals LLC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6b9cf32c-6d60-4853-bbfd-2304ffc2c129), label version 2026-01-09; accessed 2026-11-19.) As a glucocorticoid, it is generally understood to suppress inflammatory signalling and reduce immune-cell infiltration.

Alopecia mucinosa (follicular mucinosis) is characterised by mucin deposits around hair follicles together with an inflammatory cell infiltrate. A corticosteroid's anti-inflammatory action could plausibly act on this infiltrate, which is the reasoning behind the model's high score.

This is a theoretical rationale only. No trial, case series or other publication on dexamethasone in this condition was provided. Route suitability is also unassessed: the locally recorded dexamethasone products are injectable, oral and eye-drop forms, and no skin-directed form is recorded.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Dexamethasone is marketed in India as a single-ingredient product. All licences in the local records are valid and none are cancelled.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 27815 | Biodexone 4mg Injection | Vial of 2 ml Injection | Valid |
| 58248 | Dexona Tablet | Strip of 30 tablets | Valid |
| 59780 | Dexamethasone 4mg Injection | Vial of 20 ml Injection | Valid |
| 60193 | Dexomet Tablet | Strip of 10 tablets | Valid |
| 60684 | Dexam 8mg Tablet | Strip of 8 tablets | Valid |
| 62555 | Dexagee Injection 2ml | Vial of 8 injections | Valid |
| 63069 | Decon Injection | Vial of 10 ml Injection | Valid |
| 63585 | Dexalife 8mg Injection | Vial of 2 ml Injection | Valid |
| 63609 | Decdak St 0.5mg Tablet | Strip of 10 tablets | Valid |
| 63988 | Dexroid 4mg Injection | Vial of 2 ml Injection | Valid |
| 64364 | Demisone 4mg Injection | Vial of 10 ml Injection | Valid |
| 65348 | Decamycin 4mg Injection | Vial of 20 ml Injection | Valid |
| 65493 | Dekadin 8mg Injection | Vial of 2 ml Injection | Valid |
| 66222 | Dexacort Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 68468 | Dexford 8mg Tablet | Strip of 10 tablets | Valid |
| 157233 | Nebracin BM 0.1%/0.3% Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 188382 | Ravicort 4mg Injection | Vial of 2 ml Injection | Valid |
| 220480 | Tocin D Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 241707 | Wymesone 4mg Injection | Vial of 2 ml Injection | Valid |
| 252860 | Zyzone 4mg Injection | Vial of 10 ml Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

---

## Safety Considerations

- **Drug Interactions**: The interaction database lists 913 interacting drugs for dexamethasone. Examples:
  - **Major**: fentanyl, adalimumab
  - **Moderate**: paclitaxel, abemaciclib, zidovudine, nifedipine, ibuprofen, ketorolac, acetazolamide, isotretinoin
  - **Minor**: dolutegravir, lidocaine, formoterol

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. No clinical trials or publications address dexamethasone in alopecia mucinosa, so the evidence level is L5. The anti-inflammatory rationale is plausible but unverified.

**To proceed, the following is needed:**
- A systematic literature search for corticosteroid use in alopecia mucinosa, including case reports and case series
- Mechanism-of-action data for dexamethasone to support the mechanistic link
- Assessment of which route of administration would suit this condition, compared with the locally available injectable, oral and eye-drop forms
- Package insert warnings and contraindications from the local licence holders, to support a safety review
- A review of the drug interaction profile (including the major interactions above) for the likely patient population

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for dexamethasone are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Hemady (dexamethasone) prescribing information, Edenbridge Pharmaceuticals LLC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6b9cf32c-6d60-4853-bbfd-2304ffc2c129) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

