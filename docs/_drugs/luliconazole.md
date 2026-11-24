---
layout: default
title: Luliconazole
parent: Model Prediction Only (L5)
nav_order: 509
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "Luliconazole"
predicted_indications: ["endothrix infectious disease", "ectothrix infectious disease"]
description: "Luliconazole: predicted new indication Endothrix infectious disease (evidence level L5). In India: at least 20 listed products"
---

# Luliconazole
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

## Luliconazole: Endothrix infectious disease
{: .text-alpha }

## One-Sentence Summary

Luliconazole is a topical azole antifungal used for skin fungal infections. The TxGNN model predicts it may be effective for **endothrix infectious disease**, but currently there are **no clinical trials and no publications** supporting this direction, so the evidence rests on the model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Endothrix infectious disease |
| TxGNN Prediction Score | 0.9910 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for luliconazole: "LUZU Cream, 1% is an azole antifungal. […] Luliconazole is an antifungal that belongs to the azole class. Although the exact mechanism of action against dermatophytes is unknown, luliconazole appears to inhibit ergosterol synthesis by inhibiting the enzyme lanosterol demethylase." ([DailyMed: Luzu (luliconazole) prescribing information, Bausch Health US, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a7016010-ce43-4c09-8d21-aeb697ffed31), label version 2020-04-01; accessed 2026-11-19.) Luliconazole belongs to the azole class of antifungals, which act against fungal cells, and it is used on the skin as a cream or lotion.

Endothrix infections (for example, those caused by *Trichophyton tonsurans*) are dermatophyte infections in which the fungus grows inside the hair shaft. Because dermatophytes are generally susceptible to azoles, activity is biologically plausible.

There is an important limitation. Fungus inside the hair shaft may be hard for a topical product to reach, and systemic therapy is usually the standard approach for this type of infection. At this stage the support is a model prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Luliconazole is marketed in India as a single-ingredient product. The data compiled for this report show 20 valid single-ingredient licences and no cancelled ones; the list may be partial. The licence records carry no indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 79882 | Elcozol 1% Cream | Tube of 10 gm Cream | Valid |
| 110335 | Imiderm 1% Cream | Tube of 15 gm Cream | Valid |
| 110516 | Iclaben Cream | Tube of 10 gm Cream | Valid |
| 121032 | Lulifin Lotion | Bottle of 10 ml Lotion | Valid |
| 121555 | Lulimac Cream | Tube of 20 gm Cream | Valid |
| 121984 | Ludura Lotion | Bottle of 30 ml Lotion | Valid |
| 123334 | Lulicad Cream | Tube of 20 gm Cream | Valid |
| 123876 | Lucoz Lotion | Bottle of 15 ml Lotion | Valid |
| 126510 | Lucoz Lotion | Bottle of 30 ml Lotion | Valid |
| 126953 | Lutriben Lotion | Bottle of 15 ml Lotion | Valid |
| 127415 | Lucaf 1% Cream | Tube of 20 gm Cream | Valid |
| 127531 | Luliporus Lotion | Bottle of 30 ml Lotion | Valid |
| 128413 | Lulijen Lotion | Bottle of 15 ml Lotion | Valid |
| 128762 | Lufrox Cream | Tube of 10 gm Cream | Valid |
| 129660 | Lulisun Cream | Tube of 20 gm Cream | Valid |
| 130052 | Luliton 1% Cream | Tube of 20 gm Cream | Valid |
| 130683 | Lulidan Lotion | Bottle of 15 ml Lotion | Valid |
| 131155 | Lulitez 1% Cream | Tube of 15 gm Cream | Valid |
| 131824 | Lucit Care 1% Cream | Tube of 20 gm Cream | Valid |
| 248083 | Zole 1% Cream | Tube of 50 gm Cream | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no clinical trials or publications for endothrix infectious disease, so the evidence level is L5. Limited penetration of a topical product into the hair shaft further weakens the case.

**To proceed, the following is needed:**
- Laboratory data showing luliconazole activity against endothrix-causing dermatophytes
- Evidence that topical delivery reaches the hair shaft, or an assessment of whether a systemic route would be required
- Mechanism of action data
- Package insert warnings and contraindications for the safety review

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Luzu (luliconazole) prescribing information, Bausch Health US, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a7016010-ce43-4c09-8d21-aeb697ffed31) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

