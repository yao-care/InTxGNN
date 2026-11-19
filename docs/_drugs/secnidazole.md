---
layout: default
title: Secnidazole
parent: Model Prediction Only (L5)
nav_order: 765
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-03
monitor_inn: "Secnidazole"
predicted_indications: ["postmenopausal atrophic vaginitis", "ulceration of vulva", "vaginal discharge", "vulvar neoplasm", "leukoplakia of vagina", "vulvovaginal candidiasis"]
description: "Secnidazole: predicted new indication Postmenopausal atrophic vaginitis (evidence level L5). In India: at least 20 listed products"
---

# Secnidazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Secnidazole: Postmenopausal atrophic vaginitis
{: .text-alpha }

## One-Sentence Summary

Secnidazole is a 5-nitroimidazole antimicrobial that is marketed in India as a single-ingredient product.
The TxGNN model predicts it may be effective for **postmenopausal atrophic vaginitis**, with a score of 0.9970.
**No clinical trials and no publications** currently support this prediction, so it rests on the model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Postmenopausal atrophic vaginitis |
| TxGNN Prediction Score | 0.9970 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for secnidazole: "SOLOSEC is a nitroimidazole antimicrobial drug. […] Secnidazole, like other 5-nitroimidazoles, enters the bacterial and Trichomonas cells where the nitro group is reduced by nitroreductase enzyme(s) leading to the production of radical anions and a series of intermediates, depletion of thiols, DNA damage, and death of susceptible isolates of Gram positive bacteria, Gram negative bacteria and T. vaginalis." ([DailyMed: Solosec (secnidazole) prescribing information, Evofem Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=056485b6-8bba-4a21-ae00-cdb4e7ae4bfa), label version 2026-10-30; accessed 2026-11-19.) As a 5-nitroimidazole, secnidazole is generally understood to be reduced inside anaerobic bacteria and protozoa into reactive intermediates that damage microbial DNA.

Postmenopausal atrophic vaginitis is mainly driven by estrogen deficiency and thinning of the vaginal lining, not by a nitroimidazole-sensitive pathogen. That leaves no clear mechanistic link to secnidazole's antimicrobial activity.

The high score most likely reflects the disease's closeness to other vaginal conditions in the model's network, not a demonstrated biological rationale. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Secnidazole is marketed in India, and every licence in the local records is valid. The records may be partial. The five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 79025 | Etisec 1000mg Powder (Novartis India Ltd) | Box of 1 gm powder | Not stated in the licence record |
| 209678 | Secnitor 500mg Tablet (Torrent Pharmaceuticals Ltd) | Strip of 4 tablets | Not stated in the licence record |
| 6655 | Ambiform 1000mg Tablet (Glaxo SmithKline Pharmaceuticals Ltd) | Strip of 2 tablets | Not stated in the licence record |
| 199619 | Secnil Forte Tablet (Abbott) | Strip of 2 tablets | Not stated in the licence record |
| 75329 | Entosec 1000mg Tablet (Cipla Ltd) | Strip of 2 tablets | Not stated in the licence record |

## Safety Considerations

- **Drug Interactions**: The interaction query found 92 interacting drugs. The 20 reviewed here are all rated Moderate. They include:
  - other nitroimidazoles (metronidazole, tinidazole);
  - statins (rosuvastatin, simvastatin, atorvastatin);
  - amiodarone and levodopa;
  - several anticancer agents (paclitaxel, cabazitaxel, carboplatin, bortezomib, carfilzomib, brentuximab vedotin, trastuzumab emtansine);
  - adalimumab, certolizumab pegol and auranofin;
  - radioactive iodide (I-123, I-131) and picosulfuric acid.

Warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for them.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no trials or publications behind it, and its mechanism does not fit the estrogen-deficiency basis of the disease. The evidence level is L5.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis for why an antimicrobial would help an estrogen-deficiency condition, ideally with preclinical data
- Any clinical or observational data on secnidazole in postmenopausal vaginal symptoms
- Package insert warnings and contraindications for the marketed products
- Detailed mechanism of action data

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Solosec (secnidazole) prescribing information, Evofem Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=056485b6-8bba-4a21-ae00-cdb4e7ae4bfa) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

