---
layout: default
title: Olopatadine
parent: Model Prediction Only (L5)
nav_order: 618
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Olopatadine: predicted new indication Rosacea conjunctivitis (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, atopic conjunctivitis…"
monitor_inn: "Olopatadine"
predicted_indications: ["rosacea conjunctivitis"]
---

# Olopatadine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Olopatadine: From Allergic Rhinitis and Allergic Conjunctivitis to Rosacea Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Olopatadine is an antiallergic drug originally used for allergic rhinitis, vasomotor rhinitis, and several forms of allergic conjunctivitis (atopic, papillary, and vernal).
The TxGNN model predicts it may be effective for **rosacea conjunctivitis**,
but at present there are **no registered clinical trials and no publications** supporting this direction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for olopatadine: "Olopatadine is a histamine H 1 receptor antagonist. The antihistaminic activity of olopatadine has been documented in isolated tissues, animal models, and humans." ([DailyMed: olopatadine hydrochloride prescribing information, Apotex Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3aa27224-7b72-38eb-0c21-b8d73525ee85), label version 2026-09-15; accessed 2026-11-19.) Based on known information, olopatadine is marketed as a histamine H1 antagonist and mast cell stabilizer. It is used for allergic conjunctivitis, and mechanistically it may be applicable to rosacea conjunctivitis.

Rosacea conjunctivitis involves inflammation of the ocular surface. Olopatadine could plausibly reduce ocular surface inflammation and itching. This is an inference from general pharmacology and is not supported by the data compiled for this report.

The high TxGNN score (0.9941) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should be read as a computational signal, not as proof of efficacy. In addition, rosacea conjunctivitis is driven largely by meibomian gland dysfunction and non-allergic inflammation, so an antihistamine may address only part of the disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Olopatadine is marketed in India as single-ingredient products, with 20 valid registrations and none cancelled. Both oral tablets and ophthalmic solutions are available. The data compiled for this report do not include approved indication text for any of them.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 4747 | Alerchek OD Ophthalmic Solution | Packet of 3 ml Ophthalmic Solution | Valid |
| 5691 | Allenil 5mg Tablet | Strip of 10 tablets | Valid |
| 61470 | Dolpat 5mg Tablet | Strip of 10 tablets | Valid |
| 61853 | Dynolap 5 Tablet | Strip of 10 tablets | Valid |
| 105194 | Histadin 5mg Tablet | Strip of 10 tablets | Valid |
| 163387 | Olax Tablet | Strip of 10 tablets | Valid |
| 164346 | Olabest 5mg Tablet | Strip of 10 tablets | Valid |
| 164682 | Olax 5mg Tablet | Strip of 10 tablets | Valid |
| 164803 | Opta 5mg Tablet | Strip of 10 tablets | Valid |
| 165192 | Olozest 5mg Tablet | Strip of 10 tablets | Valid |
| 165719 | Olobet 5mg Tablet | Strip of 10 tablets | Valid |
| 168131 | Olohyd 5mg Tablet | Strip of 10 tablets | Valid |
| 168207 | Olatry 5mg Tablet | Strip of 10 tablets | Valid |
| 168725 | Olofur 5mg Tablet | Strip of 10 tablets | Valid |
| 169679 | Olobet 2.5mg Tablet | Strip of 10 tablets | Valid |
| 170159 | Olydus 5mg Tablet | Strip of 10 tablets | Valid |
| 174208 | Patadin Tablet | Strip of 10 tablets | Valid |
| 175802 | Pataone Eye Drop | Bottle of 5 ml Ophthalmic Solution | Valid |
| 179646 | Petadol Eye Drop | Bottle of 5 ml Ophthalmic Solution | Valid |
| 241448 | Winolap 5 Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** lower respiratory tract disease, paranasal sinus disease, nasal cavity disease, and upper respiratory tract disease. These come from computational drug-disease contraindication edges and should be verified against the approved labelling.
- **Drug Interactions:** The interaction screen returned 112 potential interacting drugs, but the severity level is unclassified for all of them. Examples include pantoprazole, omeprazole, lansoprazole, cimetidine, metformin, simvastatin, rosuvastatin, prednisone, prednisolone, hydrocortisone, triamcinolone, epinephrine, doxycycline, and tetracycline. Clinical significance must be assessed individually.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or publications supporting it (Evidence Level L5). The mechanism data and the package-insert safety information needed for safety screening are also missing.

**To proceed, the following is needed:**
- Obtain the Indian package insert (warnings and contraindications) for the safety screening
- Obtain detailed mechanism of action data from DrugBank
- Conduct a literature and trial search for olopatadine or antihistamine/mast cell stabilizer use in ocular rosacea
- Confirm that an ophthalmic route is suitable for the target use, since the registered products include both oral tablets and eye drops
- Classify the severity of the 112 potential drug interactions

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: olopatadine hydrochloride prescribing information, Apotex Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3aa27224-7b72-38eb-0c21-b8d73525ee85) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

