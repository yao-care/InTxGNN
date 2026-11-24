---
layout: default
title: Loperamide
parent: Model Prediction Only (L5)
nav_order: 499
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Loperamide: predicted new indication Acute contagious conjunctivitis (evidence level L5). Approved use: Diarrheal disease, dysentery"
monitor_inn: "Loperamide"
predicted_indications: ["acute contagious conjunctivitis", "amebic dysentery", "conjunctivitis", "gastroduodenitis", "pseudomembranous conjunctivitis", "parasitic conjunctivitis", "conjunctival folliculosis", "chronic follicular conjunctivitis", "serous conjunctivitis except viral", "Angelucci syndrome"]
---

# Loperamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Loperamide: From Diarrheal Disease to Acute Contagious Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Loperamide is a peripherally acting anti-diarrheal drug, originally used to treat diarrheal disease and dysentery.
The TxGNN model predicts it may be effective for **acute contagious conjunctivitis**, but this is a model-only prediction with **0 clinical trials** and **0 publications** supporting it.
The prediction has no plausible biological rationale and should be treated with strong caution.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diarrheal disease, dysentery |
| Predicted New Indication | Acute contagious conjunctivitis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for loperamide: "In vitro and animal studies show that loperamide hydrochloride capsules act by slowing intestinal motility and by affecting water and electrolyte movement through the bowel. Loperamide binds to the opiate receptor in the gut wall." ([DailyMed: loperamide hydrochloride prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=74b9893a-18c3-4117-85c2-edab8e7b3b3b), label version 2026-07-09; accessed 2026-11-19.) Based on known pharmacology, loperamide is a peripheral mu-opioid receptor agonist that acts on gut myenteric neurons to reduce motility and secretion. Its CNS penetration is limited by P-glycoprotein efflux.

The original indications (diarrheal disease, dysentery) are gastrointestinal, while the predicted indication is an eye infection. No mechanistic link was identified: loperamide has no known antimicrobial or anti-inflammatory activity on the ocular surface, and neither systemic nor topical ocular delivery is established.

The very high score (0.9997) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Several other conjunctivitis subtypes received nearly identical scores (for example conjunctivitis at 0.9987, pseudomembranous conjunctivitis at 0.9965, parasitic conjunctivitis at 0.9965 and chronic follicular conjunctivitis at 0.9965), which suggests the signal comes from similarities the model learned between related diseases rather than disease-specific biology. Among the other top-10 predictions, the closest to the original use is amebic dysentery (0.9995), but the available literature points toward harm rather than benefit (see Safety Considerations).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for acute contagious conjunctivitis.

---

## India Market Information

Loperamide is marketed in India as an oral product, with 20 valid registrations and none cancelled. Approved indication text is not available for these registrations.

<!-- review:begin in-lic-20261124c-loperamide-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Loperamide is marketed in India as an oral single-ingredient product, with 20 valid registrations and none cancelled." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-loperamide-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 955 | Akme-Entoquol Tablet | Strip of 20 tablets | Valid |
| 63650 | Diarlop 2mg Capsule | Strip of 10 capsules | Valid |
| 73584 | Eldomac 2mg Capsule | Strip of 10 capsules | Valid |
| 83118 | Entocidal 2mg Tablet | Strip of 10 tablets | Valid |
| 106588 | HG Mide 2mg Capsule | Strip of 10 capsules | Valid |
| 107712 | Imodium Capsule | Strip of 4 capsules | Valid |
| 121348 | Lopro 2mg Tablet | Strip of 10 tablets | Valid |
| 121552 | Lomide 2mg Tablet | Strip of 10 tablets | Valid |
| 121644 | Lopra Tablet | Strip of 10 tablets | Valid |
| 121870 | Loramyl 2mg Tablet | Strip of 10 tablets | Valid |
| 122803 | Lopidus Capsule | Strip of 10 capsules | Valid |
| 124268 | Lomide Tablet | Strip of 10 tablets | Valid |
| 124564 | Lopide Capsule | Strip of 10 capsules | Valid |
| 125297 | Loperazee 2 Capsule | Strip of 10 capsules | Valid |
| 125941 | Lomid M Syrup | Bottle of 30 ml Syrup | Valid |
| 129092 | Lomide 2mg Tablet | Strip of 10 tablets | Valid |
| 131003 | Lopoper 2mg Capsule | Strip of 10 capsules | Valid |
| 159267 | Nitilop 2mg Tablet | Strip of 10 tablets | Valid |
| 184200 | Ridol 2mg Tablet | Strip of 10 tablets | Valid |
| 199872 | Sestil AD 2mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

No ophthalmic formulation is registered.

---

## Safety Considerations

- **Contraindications (from knowledge-graph disease associations, not label text)**: liver disease, gallbladder disease, paralytic ileus, intestinal obstruction, familial visceral myopathy, dysentery, infectious diarrheal disease, intestinal infectious disease.
- **Drug Interactions**: 591 interactions are recorded. Examples classed as Major: abiraterone, ranitidine, fosamprenavir, gemfibrozil. Examples classed as Moderate: codeine, dihydrocodeine, tramadol, chlorpheniramine, cetirizine, ethanol, salbutamol.
- **Safety signals in the literature**:
  - A case report describes fulminant amoebic colitis (toxic megacolon) after heavy loperamide use, consistent with the known caution against antimotility agents in invasive dysentery.
  - A 2026 case report describes loperamide-induced respiratory depression in a patient with severe chemotherapy-related gastrointestinal inflammation. Impaired mucosal barrier or efflux may raise systemic exposure.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for acute contagious conjunctivitis rests on a model score alone (L5), with no trials, no literature and no plausible mechanism. The related predictions in the top 10 are either equally unsupported or carry safety signals.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis for ocular activity, plus evidence of an ocular delivery route (none exists today)
- Preclinical studies in ocular infection or inflammation models
- Mechanism of action data and package insert warnings and contraindications for the India registrations
- Re-evaluation of the model prediction for artifacts from similarities the model learned between related diseases, given the near-identical scores across conjunctivitis subtypes

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: loperamide hydrochloride prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=74b9893a-18c3-4117-85c2-edab8e7b3b3b) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

