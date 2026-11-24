---
layout: default
title: Trioxsalen
parent: Model Prediction Only (L5)
nav_order: 869
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "trioxsalen"
predicted_indications: ["vaginitis (disease)", "leukoplakia of vagina", "vaginal discharge", "bacterial vaginosis", "vulvar inverted follicular keratosis", "postmenopausal atrophic vaginitis", "vulvitis", "vulvovaginitis", "ulceration of vulva", "vulvar neoplasm"]
description: "Trioxsalen: predicted new indication Vaginitis (disease) (evidence level L5). In India: at least 20 listed products"
---

# Trioxsalen
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

## Trioxsalen: Vaginitis (disease)
{: .text-alpha }

## One-Sentence Summary

Trioxsalen is a psoralen compound originally used for vitiligo and photosensitivity-related conditions, typically together with UVA light.
The TxGNN model predicts it may be effective for **vaginitis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Vaginitis (disease) |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of trioxsalen as: DNA inhibitor ([ChEMBL CHEMBL1475 (trioxsalen): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1475), CC BY-SA 3.0; accessed 2026-11-19.) Based on general pharmacology, trioxsalen is a psoralen. When combined with UVA light, it intercalates into DNA and forms photoadducts, which produces antiproliferative and photosensitizing effects. This is the basis for its use in vitiligo and other photo-responsive skin conditions.

A plausible link between this mechanism and vaginitis is weak. Vaginitis is mainly infectious or inflammatory, and UVA exposure of the vaginal mucosa is impractical. The very high TxGNN score (0.9978) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top-ranked predictions are all genital or vulvovaginal conditions: leukoplakia of vagina (0.9974), vaginal discharge (0.9973), bacterial vaginosis (0.9969), vulvar inverted follicular keratosis (0.9966), postmenopausal atrophic vaginitis (0.9965), vulvitis (0.9965), vulvovaginitis (0.9961), ulceration of vulva (0.9954) and vulvar neoplasm (0.9952). Each has a TxGNN score ≥ 0.99, and none has any clinical trial or literature support. A few have a loose conceptual link through psoralen effects on epidermal proliferation or immune modulation (for example vulvitis and vulvar inverted follicular keratosis). Others, such as bacterial vaginosis and atrophic vaginitis, have no pathway connection to this drug.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Twenty single-ingredient oral tablet licences are valid, and none is cancelled. Approved indication text is not available for any of them.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 15607 | Amosan 25mg Tablet | Strip of 10 tablets | Valid |
| 62231 | Dsorolin Tablet | Strip of 10 tablets | Valid |
| 125525 | Lucoderm 25 Tablet | Strip of 10 tablets | Valid |
| 151053 | Neosoralen Forte 25mg Tablet | Strip of 10 tablets | Valid |
| 151633 | Neosol Forte 25mg Tablet | Strip of 10 tablets | Valid |
| 151997 | Neosoralen 5mg Tablet | Strip of 10 tablets | Valid |
| 153130 | Neosorlen XXV 25mg Tablet | Strip of 10 tablets | Valid |
| 155465 | Neosorlen V 5mg Tablet | Strip of 10 tablets | Valid |
| 155729 | Neosal 5mg Tablet | Strip of 10 tablets | Valid |
| 176688 | Promelan Forte 25mg Tablet | Strip of 10 tablets | Valid |
| 177237 | Psoratop 25mg Tablet | Strip of 10 tablets | Valid |
| 204533 | Sensitex 5mg Tablet | Strip of 10 tablets | Valid |
| 217771 | Trilen Tablet | Strip of 10 tablets | Valid |
| 218065 | Tribest 25mg Tablet | Strip of 10 tablets | Valid |
| 218490 | Troid 5mg Tablet | Strip of 10 tablets | Valid |
| 218741 | Trioxol 25mg Tablet | Strip of 10 tablets | Valid |
| 220133 | Trixalen 25mg Tablet | Strip of 10 tablets | Valid |
| 224291 | Triligo Forte 25mg Tablet | Strip of 10 tablets | Valid |
| 233869 | Vitrex 25mg Tablet | Strip of 10 tablets | Valid |
| 234833 | Vitiline 25mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

**Drug Interactions** (5 moderate-level interactions identified):
- Methoxsalen
- Aminolevulinic acid (topical)
- Methyl aminolevulinate (topical)
- Porfimer sodium
- Verteporfin

These are mostly other photosensitizing agents, so combined use may increase photosensitivity.

**Class-level concerns from the mechanism assessment:** Psoralens combined with UVA are mutagenic and carcinogenic, with a documented skin cancer risk after PUVA, including on genital skin. A photosensitizing, DNA-damaging agent could also impair mucosal healing.

Please refer to the package insert for other safety information, such as warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or publications, the mechanistic link to vaginitis is implausible, and the carcinogenicity and photosensitivity risks on genital mucosa make the risk-benefit profile unfavourable.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence for a genital or vulvovaginal indication
- Assessment of route feasibility, since only oral tablets are marketed and UVA delivery to the vaginal mucosa is impractical
- A reassessment of whether other predicted indications with a closer link to the original photo-responsive skin use (for example vulvitis) merit review

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL1475 (trioxsalen): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1475) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

