---
layout: default
title: Metaxalone
parent: Model Prediction Only (L5)
nav_order: 531
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Metaxalone: predicted new indication Infectious otitis media (evidence level L5). Approved use: Not stated in the data compiled for this report (metaxalone is genera…"
monitor_inn: "Metaxalone"
drugbank_id: DB00660
predicted_indications: ["infectious otitis media", "endocarditis", "endocardial fibroelastosis"]
---

# Metaxalone
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

## Metaxalone: From Skeletal Muscle Relaxation to Infectious Otitis Media
{: .text-alpha }

## One-Sentence Summary

Metaxalone is a centrally acting skeletal muscle relaxant that is marketed in India as a single-ingredient oral tablet.
The TxGNN model predicts it may be effective for **infectious otitis media**,
but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (metaxalone is generally known as a skeletal muscle relaxant) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 0.9906 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for metaxalone: "The mechanism of action of metaxalone in humans has not been established, but may be due to general central nervous system (CNS) depression. Metaxalone has no direct action on the contractile mechanism of striated muscle, the motor end plate, or the nerve fiber." ([DailyMed: metaxalone prescribing information, Misemer Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d0276e7b-a1c9-61f3-e053-2a95a90ae3aa), label version 2026-11-12; accessed 2026-11-19.) Metaxalone is a centrally acting skeletal muscle relaxant, and its exact mechanism is incompletely characterized.

The review of the prediction found no established mechanistic link to infectious otitis media. Metaxalone has no known antimicrobial, anti-inflammatory, or Eustachian tube-related activity. The high score (0.9906) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is not backed by any trial or literature evidence.

Two other predictions were also generated, and neither is supported by evidence:
- **Endocarditis** (score 0.9902): no plausible mechanistic link, because infective endocarditis is treated with targeted antimicrobial therapy and metaxalone has no antibacterial or cardiac-specific activity.
- **Endocardial fibroelastosis** (score 0.9900): no identified mechanistic link, and pediatric safety data for metaxalone are limited.

All three predictions are rated L5 and Hold.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 84259 | Flexura 400 Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not from label text): liver failure, acute liver failure, hepatitis, hemolytic anemia.
- **Drug Interactions**: 53 interactions are recorded. The Major-level ones among those listed are:
  - Morphine (including liposomal morphine)
  - Codeine
  - Hydrocodone

  Moderate-level interactions include:
  - Cannabinoids (dronabinol, nabilone)
  - Naltrexone
  - Metoclopramide
  - Opium
  - Sibutramine
  - Ethanol
  - Sedating antihistamines (promethazine, chlorpheniramine, cetirizine, brompheniramine, carbinoxamine, clemastine, mepyramine, doxylamine)
  - Dextromethorphan

  Many of these are central nervous system depressants, so additive sedation is a likely concern.

Package insert warnings and contraindications were not available, so please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based only on a model score. There are no clinical trials or publications, no mechanistic link to otitis media, and the package insert safety data are missing. The evidence level is L5.

**To proceed, the following is needed:**
- The India package insert (warnings, contraindications, approved indication), obtained from the India Pharma website. This is currently a blocking gap for safety screening.
- Mechanism of action data for metaxalone from DrugBank, to allow a mechanistic-link analysis.
- Any preclinical or clinical evidence linking metaxalone to infectious otitis media. Without it, the prediction should not advance.
- A review of the knowledge-graph liver-related contraindication signals and the CNS-depressant interactions if the project is reconsidered.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: metaxalone prescribing information, Misemer Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d0276e7b-a1c9-61f3-e053-2a95a90ae3aa) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

