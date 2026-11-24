---
layout: default
title: Dexlansoprazole
parent: Model Prediction Only (L5)
nav_order: 253
evidence_level: L5
indication_count: 4
monitor_inn: "Dexlansoprazole"
predicted_indications: ["gastroduodenitis", "duodenal obstruction", "achlorhydria", "leather-bottle stomach"]
last_modified_at: 2026-11-24
description: "Dexlansoprazole: predicted new indication gastroduodenitis (evidence level L5). In India: 11 listed products (11 not discontinued)"
---

# Dexlansoprazole
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

## Dexlansoprazole: proton pump inhibitor → gastroduodenitis
{: .text-alpha }

## One-Sentence Summary

Dexlansoprazole is a proton pump inhibitor, an acid-suppressing drug taken as a modified-release capsule.
The TxGNN model predicts it may be effective for **gastroduodenitis**, but the data compiled for this report contain **no clinical trials and no publications** for this disease.
The prediction is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | gastroduodenitis |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (11 of 11) – CDSCO approval status is not included in this data |
| Number of Listed Products | 11 (valid: 11) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for dexlansoprazole: "Dexlansoprazole belongs to a class of antisecretory compounds, the substituted benzimidazoles, that suppress gastric acid secretion by specific inhibition of the (H +, K + )-ATPase at the secretory surface of the gastric parietal cell. Because this enzyme is regarded as the acid (proton) pump within the parietal cell, dexlansoprazole has been characterized as a gastric proton-pump inhibitor, in that it blocks the final step of acid production." ([DailyMed: Dexlansoprazole Delayed Release (dexlansoprazole) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=55c550b4-eb8b-4e69-9c09-fa5125a52e65), label version 2026-11-04; accessed 2026-11-19.) Dexlansoprazole belongs to the proton pump inhibitor class, which reduces gastric acid secretion.

Gastroduodenitis is an inflammation of the stomach and duodenal lining. Acid suppression could plausibly ease symptoms of acid-related mucosal inflammation, because less acid reaches the irritated tissue. This is a reasoned hypothesis and has not been tested in any trial or publication supplied here.

The high score of 0.9998 reflects a computational prediction. It should not be read as evidence of clinical benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 58342 | Deltone Capsule MR | Strip of 10 capsule mr | Valid |
| 58377 | DDR 60 Capsule MR | Strip of 10 capsule mr | Valid |
| 58423 | DDR 30 Capsule MR | Strip of 10 capsule mr | Valid |
| 58458 | Deltone 30mg Capsule | Strip of 10 capsules | Valid |
| 59177 | Dexolan Capsule MR | Strip of 10 capsule mr | Valid |
| 59750 | Dexolan 30 Capsule MR | Strip of 10 capsule mr | Valid |
| 61132 | Duabit Capsule MR | Strip of 7 capsule mr | Valid |
| 64032 | Dexsofighter 60 Capsule MR | Strip of 10 capsule mr | Valid |
| 122168 | Lanfil DX 60 Capsule MR | Strip of 10 capsule mr | Valid |
| 124062 | Lantas-DX 60 Capsule MR | Strip of 10 capsule mr | Valid |
| 124848 | Lantas-DX 30 Capsule MR | Strip of 10 capsule mr | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

All 11 licences are currently valid, and none is cancelled.

## Safety Considerations

- **Drug Interactions**: 118 interactions were found in the interaction query. Examples:
  - **Major**: acalabrutinib, atazanavir
  - **Moderate**: fosamprenavir, foscarnet, fostamatinib, furosemide, gefitinib, hydrochlorothiazide, amphotericin B, amikacin, amphetamine, ampicillin, bosutinib, bumetanide
  - **Minor**: acetylsalicylic acid, axitinib, brivaracetam, cyanocobalamin

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for them.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for gastroduodenitis is a model prediction, with no clinical trials or publications. This places the evidence at L5. A plausible acid-suppression rationale is not enough to move forward.

**To proceed, the following is needed:**
- Clinical or observational studies that directly address gastroduodenitis
- Detailed mechanism-of-action data
- Package insert warnings and contraindications, to allow a safety review
- A review of the major interactions (acalabrutinib, atazanavir) for the intended patient population

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Dexlansoprazole Delayed Release (dexlansoprazole) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=55c550b4-eb8b-4e69-9c09-fa5125a52e65) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

