---
layout: default
title: Ascorbic Acid
parent: Model Prediction Only (L5)
nav_order: 73
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Ascorbic Acid: predicted new indication Non-syndromic esophageal malformation (evidence level L5). Approved use: Ascorbic acid deficiency"
monitor_inn: "Ascorbic acid"
predicted_indications: ["non-syndromic esophageal malformation", "esophageal disease", "congenital prothrombin deficiency", "injury", "biotin metabolic disease", "perinatal disease", "florid cemento-osseous dysplasia", "segmental odontomaxillary dysplasia", "disease by subcellular system affected"]
---

# Ascorbic Acid
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

## Ascorbic Acid: From Ascorbic Acid Deficiency (Scurvy) to Non-syndromic Esophageal Malformation
{: .text-alpha }

## One-Sentence Summary

Ascorbic acid (vitamin C) is originally used to prevent and treat vitamin C deficiency and scurvy.
The TxGNN model predicts it may be effective for **non-syndromic esophageal malformation**, but this is a model prediction only, with **no clinical trials** and **no publications** currently supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ascorbic acid deficiency; scurvy |
| Predicted New Indication | Non-syndromic esophageal malformation |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for ascorbic acid: "The exact mechanism of action of ascorbic acid for the treatment of symptoms and signs of scurvy (a disorder caused by severe deficiency in vitamin C) is unknown; however, administration of ascorbic acid in patients with scurvy is thought to restore the body pool of ascorbic acid." ([DailyMed: ascorbic acid prescribing information, Zydus Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f0b683f8-189b-4a3f-9ffe-f91df6d798b6), label version 2026-09-03; accessed 2026-11-19.) Based on known information, ascorbic acid is a single-ingredient vitamin. Its efficacy in correcting vitamin C deficiency and scurvy is well established. It is also known as an antioxidant and as a cofactor in collagen synthesis.

Non-syndromic esophageal malformation is a structural congenital defect that arises during embryonic development. No plausible mechanism has been identified by which ascorbic acid could correct or treat such a defect. The very high score (0.9996) reflects how the model links this drug to the disease, not biological or clinical support. The reliability of this prediction is therefore low, and it should be treated only as a hypothesis for screening.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Ascorbic acid is widely marketed in India. There are 20 valid registrations, none cancelled. Dosage forms include injections, chewable tablets and oral drops. The data compiled for this report do not include approved indication text.

<!-- review:begin in-lic-20261124c-ascorbic_acid-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Ascorbic acid is widely marketed in India as a single-ingredient product." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-ascorbic_acid-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 2484 | Aquasol C Oral Drops | Bottle of 30 ml Oral Drops | Valid |
| 4921 | Ascovit C 1500mg Injection | Vial of 6 ml Injection | Valid |
| 6754 | Ascovar Injection | Vial of 6 ml Injection | Valid |
| 9616 | Ascochew Chewable Tablet Orange | Strip of 10 Chewable Tablets | Valid |
| 24614 | Ascorcee 1500mg Injection | Vial of 1 Injection | Valid |
| 35742 | CZ 360 Chewable Tablet Orange | Strip of 15 Chewable Tablets | Valid |
| 45702 | Cefedge-C Injection | Vial of 6 ml Injection | Valid |
| 110331 | Inlime-CZ Chewable Tablet Orange | Bottle of 30 Chewable Tablets | Valid |
| 124072 | Limcor Chewable Tablet Orange | Bottle of 30 Chewable Tablets | Valid |
| 163740 | Ovit-Cee Injection | Vial of 6 ml Injection | Valid |
| 166156 | Oxistox 12 Injection | Box of 2 injections | Valid |
| 193832 | Ross Vee C 500mg Injection | Vial of 1 Injection | Valid |
| 200650 | Scorbix 1.5gm Injection | Vial of 3 ml Injection | Valid |
| 201798 | Scorbia-XT Injection | Box of 1 Injection | Valid |
| 203069 | Scornix Injection | Vial of 6 ml Injection | Valid |
| 233351 | Vitamin C Injection | Vial of 1.5 ml Injection | Valid |
| 242077 | W-Vit-Plus Injection Combipack | Box of 1 Injection | Valid |
| 246648 | Zascor Chewable Tablet Lemon & Honey Sugar Free | Strip of 15 Chewable Tablets | Valid |
| 246805 | Zincee Chewable Tablet | Strip of 20 Chewable Tablets | Valid |
| 247785 | Zu-C Injection | Ampoule of 5 ml Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

---

## Safety Considerations

- **Disease associations from the TxGNN model (deep learning), not label text:** The TxGNN model (deep learning) may reflect similarities it learned between related diseases, not biological evidence. It lists contraindication relationships between ascorbic acid and several conditions. Examples include kidney disease, anuria, nephrocalcinosis, primary hyperoxaluria, hereditary hemochromatosis, sickle cell anemia, diabetes mellitus, peptic ulcer disease, liver disease, and hypercalcemia. These should be confirmed against the official package insert.
- **Drug Interactions:** 25 interactions were recorded in total. The moderate-level interactions among those listed are:
  - Amphetamine
  - Dextroamphetamine
  - Lisdexamfetamine
  - Metamfetamine
  - Benzphetamine
  - Aluminum hydroxide
  - Bortezomib
  - Deferoxamine

  Minor interactions include paclitaxel, cisplatin, doxorubicin, ethinylestradiol, and pseudoephedrine.

Please refer to the package insert for complete warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for non-syndromic esophageal malformation rests solely on the model score. There are no clinical trials, no literature, and no plausible mechanism for correcting a congenital structural defect with ascorbic acid.

**Other predictions for this drug:** Several other predicted indications have more supporting evidence and may be better candidates.
- **Perinatal disease:** L3, a small trial in neonatal hypoxic-ischemic encephalopathy.
- **Injury:** L2, with Phase 2 trials in sepsis- and COVID-19-related lung injury.

**To proceed, the following is needed:**
- Mechanism of action data for ascorbic acid
- Package insert warnings and contraindications from the India Pharma source
- A biological rationale connecting ascorbic acid to esophageal development, if this indication is to be pursued
- Prioritization of better-supported indications before any further work on this one

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: ascorbic acid prescribing information, Zydus Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f0b683f8-189b-4a3f-9ffe-f91df6d798b6) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

