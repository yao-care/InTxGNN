---
layout: default
title: Cetirizine
parent: Model Prediction Only (L5)
nav_order: 166
evidence_level: L5
indication_count: 3
monitor_inn: "Cetirizine"
predicted_indications: ["nasal cavity disease", "rosacea conjunctivitis", "recalcitrant atopic dermatitis"]
last_modified_at: 2026-11-24
description: "Cetirizine: predicted new indication nasal cavity disease (evidence level L5). In India: at least 20 listed products"
---

# Cetirizine
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

## Cetirizine: H1 receptor antagonist (antihistamine) → nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Cetirizine is an H1-receptor antagonist antihistamine marketed in India in many products.
The TxGNN model predicts it may be effective for **nasal cavity disease**, a broad and non-specific term.
Currently **no clinical trials** and **5 publications** (mostly reviews and unrelated preclinical work) are linked to this prediction, so the evidence is limited.

<!-- review:begin in-lic-20261124c-cetirizine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Cetirizine is an H1-receptor antagonist antihistamine marketed in India in many single-ingredient products." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-cetirizine-1 -->

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | nasal cavity disease |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Cetirizine blocks histamine H1 receptors, which are found on nerve endings, smooth muscle and glandular cells. According to the Mechanism of Action section of the US FDA-approved prescribing information for cetirizine: "Cetirizine hydrochloride, a human metabolite of hydroxyzine, is an antihistamine; its principal effects are mediated via selective inhibition of peripheral H 1 -receptors. The antihistaminic activity of cetirizine hydrochloride has been clearly documented in a variety of animal and human models." ([DailyMed: Quzyttir (cetirizine hydrochloride) prescribing information, ESTEVE PHARMACEUTICALS, S.A.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=573770f6-b76e-f6ba-e063-6294a90aa54d), label version 2026-09-22; accessed 2026-11-19.) Published reviews also describe additional anti-allergic effects of H1 antagonists, such as reduced eosinophil chemotaxis and mediator release.

These properties are relevant to allergic and inflammatory conditions of the nose. However, "nasal cavity disease" is a very broad term. The best-supported part of it, allergic rhinitis, is already covered by existing use of the drug. Any new value would therefore have to come from other inflammatory nasal or sinus conditions, which the prediction does not specify.

Because no cited study directly examines cetirizine in a defined nasal cavity disease beyond what is already known, the evidence level is set at L5 (model prediction with no direct study).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11291777](https://pubmed.ncbi.nlm.nih.gov/11291777/) | 2000 | Review | Allergy | H1-receptor antagonists act mainly by blocking histamine receptors, but may also have additional anti-allergic effects in allergic rhinitis |
| [37970776](https://pubmed.ncbi.nlm.nih.gov/37970776/) | 2023 | Review | Vestnik otorinolaringologii | Treatment of nose and paranasal sinus inflammation should follow the underlying pathogenesis, aiming to reduce swelling and mucus |
| [35818943](https://pubmed.ncbi.nlm.nih.gov/35818943/) | 2022 | Review | Vestnik otorinolaringologii | Modern H1 antihistamines in patients with allergic rhinitis who also have acute respiratory infections |
| [36116201](https://pubmed.ncbi.nlm.nih.gov/36116201/) | 2022 | Preclinical (mouse, unrelated intervention) | Phytomedicine | Herbal capsule studied in a mouse model of allergic rhinitis; not about cetirizine |
| [9301130](https://pubmed.ncbi.nlm.nih.gov/9301130/) | 1997 | Preclinical (different drug) | Arerugi | Betotastine tested in experimental allergic rhinitis; cetirizine used as a comparator that dose-dependently reduced the response |

## India Market Information

The data list at least 20 valid licences, and the list may be partial. No approved-indication text is recorded for these licences.

<!-- review:begin in-lic-20261124c-cetirizine-2 -->

> **Review correction (2026-11-24)**: Originally stated: "The data list at least 20 valid single-ingredient licences, and the list may be partial." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-cetirizine-2 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 12883 | Acrecet 10mg Tablet | Strip of 10 tablets | Valid |
| 29352 | B Cet 10mg Tablet | Strip of 10 tablets | Valid |
| 37543 | Cetcip Cold 5mg Tablet | Strip of 10 tablets | Valid |
| 37732 | Ce 10mg Tablet | Strip of 10 tablets | Valid |
| 39401 | Cozymin Vapocaps Capsule | Strip of 10 capsules | Valid |
| 47523 | Conicet 10mg Tablet | Strip of 10 tablets | Valid |
| 47774 | Ceter 10mg Tablet DT | Strip of 10 tablet dt | Valid |
| 49794 | Cetinof Syrup | Bottle of 60 ml Syrup | Valid |
| 50088 | Cetrinat 10mg Tablet | Strip of 10 tablets | Valid |
| 50813 | Cetrimark 10mg Tablet | Strip of 10 tablets | Valid |
| 51283 | Ciszine 10mg Tablet | Strip of 10 tablets | Valid |
| 51370 | Cetrish 10mg Tablet | Strip of 10 tablets | Valid |
| 52831 | Cetnir Syrup | Bottle of 60 ml Syrup | Valid |
| 116914 | Kolcare Tablet | Strip of 10 tablets | Valid |
| 140303 | Mcet 10mg Tablet | Strip of 10 tablets | Valid |
| 158949 | No-Aller 10mg Tablet | Strip of 10 tablets | Valid |
| 178553 | Pcp Forte 5mg/325mg/5mg Tablet | Strip of 10 tablets | Valid |
| 205627 | Stencold Syrup | Bottle of 30 ml Syrup | Valid |
| 221204 | Trizine P 5mg/325mg/10mg Tablet | Strip of 10 tablets | Valid |
| 225306 | Trig AR Syrup | Bottle of 100 ml Syrup | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 570 interactions were recorded. Those listed as moderate include bupropion, dronabinol, loperamide, metoclopramide, morphine, nabilone, opium, sibutramine, difenoxin and diphenoxylate. Several others (e.g. calcitriol, vitamin A, phentermine, pantoprazole, glimepiride) have an unknown severity level.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but "nasal cavity disease" is too broad to act on. No clinical trials exist, and the cited literature consists of reviews and unrelated preclinical studies. The best-supported use, allergic rhinitis, is already covered.

**To proceed, the following is needed:**
- A specific nasal or sinus condition, beyond allergic rhinitis, to test
- Clinical studies that directly examine cetirizine in that condition
- Package insert warnings and contraindications from the India label
- Detailed mechanism-of-action data

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data were not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Quzyttir (cetirizine hydrochloride) prescribing information, ESTEVE PHARMACEUTICALS, S.A.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=573770f6-b76e-f6ba-e063-6294a90aa54d) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

