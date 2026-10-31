---
layout: default
title: Trioxsalen
parent: Model Prediction Only (L5)
nav_order: 869
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
monitor_inn: "trioxsalen"
predicted_indications: ["vaginitis (disease)", "leukoplakia of vagina", "vaginal discharge", "bacterial vaginosis", "vulvar inverted follicular keratosis", "postmenopausal atrophic vaginitis", "vulvitis", "vulvovaginitis", "ulceration of vulva", "vulvar neoplasm"]
description: "Trioxsalen: predicted new indication Vaginitis (disease) (evidence level L5). Approved use: Not recorded in the local data"
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

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, trioxsalen is a psoralen. When combined with UVA light, it intercalates into DNA and forms photoadducts, which produces antiproliferative and photosensitizing effects. This is the basis for its use in vitiligo and other photo-responsive skin conditions.

A plausible link between this mechanism and vaginitis is weak. Vaginitis is mainly infectious or inflammatory, and UVA exposure of the vaginal mucosa is impractical. The very high TxGNN score (0.9978) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top-ranked predictions are all genital or vulvovaginal conditions: leukoplakia of vagina (0.9974), vaginal discharge (0.9973), bacterial vaginosis (0.9969), vulvar inverted follicular keratosis (0.9966), postmenopausal atrophic vaginitis (0.9965), vulvitis (0.9965), vulvovaginitis (0.9961), ulceration of vulva (0.9954) and vulvar neoplasm (0.9952). Each has a TxGNN score ≥ 0.99, and none has any clinical trial or literature support. A few have a loose conceptual link through psoralen effects on epidermal proliferation or immune modulation (for example vulvitis and vulvar inverted follicular keratosis). Others, such as bacterial vaginosis and atrophic vaginitis, have no pathway connection to this drug.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Twenty single-ingredient oral tablet licences are valid, and none is cancelled. Approved indication text is not available for any of them. The five main authorisations are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 151997 | Neosoralen 5mg Tablet | Strip of 10 tablets | Mac Laboratories Ltd |
| 151053 | Neosoralen Forte 25mg Tablet | Strip of 10 tablets | Mac Laboratories Ltd |
| 218741 | Trioxol 25mg Tablet | Strip of 10 tablets | Ampra Pharmaceuticals |
| 218490 | Troid 5mg Tablet | Strip of 10 tablets | Resilient Cosmecueticals Pvt Ltd |
| 204533 | Sensitex 5mg Tablet | Strip of 10 tablets | Kivi Labs Ltd |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

