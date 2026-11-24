---
layout: default
title: Cefuroxime
parent: Model Prediction Only (L5)
nav_order: 162
evidence_level: L5
indication_count: 8
monitor_inn: "Cefuroxime"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "Peptostreptococcus infectious disease", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy"]
last_modified_at: 2026-11-24
description: "Cefuroxime: predicted new indication hyperamylasemia (evidence level L5). In India: at least 20 listed products"
---

# Cefuroxime
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Cefuroxime: beta-lactam cell-wall synthesis inhibitor (second-generation cephalosporin) → hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Cefuroxime is a second-generation cephalosporin antibiotic that inhibits bacterial cell-wall synthesis.
The TxGNN model predicts it may be associated with **hyperamylasemia**, but **no clinical trials and no publications** were found for this disease, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | hyperamylasemia |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for cefuroxime: "Cefuroxime is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Cefuroxime has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: cefuroxime sodium prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a145288-733a-4966-b7ae-dc96eb103d8c), label version 2025-03-27; accessed 2026-11-19.) Cefuroxime belongs to the beta-lactam class of antibiotics, which act by blocking bacterial cell-wall synthesis.

This mechanism has no known connection to amylase metabolism. Nothing suggests that an antibacterial agent would change serum amylase levels or treat a condition defined by raised amylase. The score is a model-based prediction only, likely reflecting proximity in a network of biomedical relationships rather than a real biological effect. We therefore regard the mechanistic rationale as absent.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Cefuroxime is marketed in India. The data compiled for this report list 20 valid licences, none cancelled; this list may be partial. The licence records carry no approved-indication text. Products come as tablets, syrup, dry syrup and powder for injection.

<!-- review:begin in-lic-20261124-cefuroxime-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The data compiled for this report list 20 valid licences, all for single-ingredient products and none cancelled; this list may be partial." Removed: it described the products as single-ingredient (or as having no combination products), which does not match the Indian medicine data (the Indian Medicine Dataset): some of the recorded products are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124-cefuroxime-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 15798 | Aksicef 250mg Tablet | Strip of 6 tablets | Valid |
| 18745 | Acctum 125mg Syrup | Bottle of 30 ml Syrup | Valid |
| 39549 | Cefstal 500 Tablet | Strip of 10 tablets | Valid |
| 42230 | Cefuko 500mg Tablet | Strip of 10 tablets | Valid |
| 46688 | Cefuture 500 Tablet | Strip of 10 tablets | Valid |
| 47389 | Cefuraz 500mg Tablet | Strip of 10 tablets | Valid |
| 49401 | Cefuset 250mg Tablet | Strip of 10 tablets | Valid |
| 54213 | Cefumex 250mg Tablet | Strip of 10 tablets | Valid |
| 63659 | Dicef CV 500mg/125mg Tablet | Strip of 6 tablets | Valid |
| 85488 | Furocef 250mg Tablet | Strip of 10 tablets | Valid |
| 92876 | Furopea CV 500mg/125mg Tablet | Strip of 6 tablets | Valid |
| 93293 | Furix 250mg Tablet | Strip of 10 tablets | Valid |
| 107117 | Horoxime 250mg Tablet | Strip of 10 tablets | Valid |
| 109865 | I M Sure 500mg Tablet | Strip of 10 tablets | Valid |
| 146188 | Mutum 250mg Tablet | Strip of 10 tablets | Valid |
| 148139 | Meroxime 250mg Tablet | Strip of 6 tablets | Valid |
| 191766 | Relicef 1.5gm Injection | Vial of 1 Powder for Injection | Valid |
| 194008 | Roxime 125mg Dry Syrup | Bottle of 30 ml Dry Syrup | Valid |
| 211321 | Svcef 250mg Tablet | Strip of 4 tablets | Valid |
| 242935 | Wanocef CV 500mg/125mg Tablet | Strip of 6 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 143 interactions were recorded. Those listed are of moderate level, including:
  - Acid-lowering agents: famotidine, ranitidine, cimetidine, nizatidine, omeprazole, esomeprazole, lansoprazole, pantoprazole, rabeprazole, dexlansoprazole
  - Antacids: aluminium hydroxide, calcium carbonate, magnesium hydroxide, magnesium oxide, magnesium carbonate, magaldrate
  - Aminoglycosides: kanamycin, neomycin
  - Others: balsalazide

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by no clinical trials or publications, and there is no plausible mechanism linking cefuroxime to hyperamylasemia. Evidence level is L5.

**To proceed, the following is needed:**
- Any clinical or mechanistic evidence directly studying cefuroxime in hyperamylasemia
- Mechanism of action data and package insert warnings and contraindications for cefuroxime
- A clear clinical rationale for why a drug of this class would be used for this condition

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: cefuroxime sodium prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a145288-733a-4966-b7ae-dc96eb103d8c) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

