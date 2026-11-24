---
layout: default
title: Betamethasone
parent: Moderate Evidence (L3-L4)
nav_order: 106
evidence_level: L4
indication_count: 7
last_modified_at: 2026-11-24
monitor_inn: "Betamethasone"
predicted_indications: ["alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions"]
description: "Betamethasone: predicted new indication Alopecia mucinosa (evidence level L4). In India: at least 20 listed products"
---

# Betamethasone
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

## Betamethasone: Alopecia mucinosa
{: .text-alpha }

## One-Sentence Summary

Betamethasone is a potent corticosteroid with anti-inflammatory and immunosuppressive activity.
The TxGNN model predicts it may be effective for **alopecia mucinosa**, but there are **0 clinical trials** and only **1 publication** (a 1964 case series) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Alopecia mucinosa |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L4 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for betamethasone: "Corticosteroids play a role in cellular signaling, immune function, inflammation, and protein regulation; however, the precise mechanism of action of SERNIVO Spray in psoriasis is unknown." ([DailyMed: Sernivo (betamethasone dipropionate) prescribing information, Primus Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b1b3d1b0-da9b-11eb-ad76-0800200c9a66), label version 2026-04-22; accessed 2026-11-19.) Betamethasone belongs to the glucocorticoid class, whose members suppress inflammatory signalling and immune cell activity.

Alopecia mucinosa (follicular mucinosis) involves perifollicular inflammation and mucin deposition in hair follicles. An anti-inflammatory corticosteroid is therefore a plausible fit mechanistically. However, the link rests on general pharmacological reasoning. The only supporting publication is a 1964 case series, and no modern data exist.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14164963](https://pubmed.ncbi.nlm.nih.gov/14164963/) | 1964 | Case series | Archives of dermatology | Report of three cases of follicular mucinosis (alopecia mucinosa) with a review of therapy. No abstract is available, and the report does not provide modern efficacy data for betamethasone. |

## India Market Information

At least 20 valid single-ingredient licences are recorded, and the list may be partial. Licence records carry no approved-indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 25777 | Betnesol Oral Drops | Packet of 15 ml Oral Drops | Valid |
| 26149 | Betamine Forte Tablet | Strip of 10 tablets | Valid |
| 26850 | Besole 0.5mg Tablet | Strip of 10 tablets | Valid |
| 27072 | Betnevin 4mg Injection | Vial of 1 ml Injection | Valid |
| 27244 | Betacon 0.5mg Tablet | Strip of 10 tablets | Valid |
| 27357 | Betalar S 0.5mg Tablet | Strip of 10 tablets | Valid |
| 27657 | Betanij 0.5mg Tablet | Strip of 10 tablets | Valid |
| 28818 | Betni White 0.5mg Tablet | Bottle of 100 tablets | Valid |
| 29922 | Betalide 0.5mg Tablet | Strip of 10 tablets | Valid |
| 38129 | Celestone 0.5mg Oral Drops | Bottle of 10 ml Oral Drops | Valid |
| 47964 | Cortisal Ointment | Tube of 20 gm Ointment | Valid |
| 97239 | Glysalic Ointment | Tube of 20 gm Ointment | Valid |
| 139463 | Mycopar Cream | Tube of 5 gm Cream | Valid |
| 142994 | Medilan Retard Tablet | Strip of 10 tablets | Valid |
| 182866 | Quadriline Ointment | Tube of 15 gm Ointment | Valid |
| 183000 | Quadriderm AF Ointment | Tube of 5 gm Ointment | Valid |
| 183264 | Quadrim Mix Cream | Tube of 10 gm Cream | Valid |
| 205875 | Solubet 5mg Injection | Vial of 1 ml Injection | Valid |
| 209788 | Solubin N Ointment | Tube of 5 gm Ointment | Valid |
| 231281 | Uniderm NF Cream | Tube of 5 gm Cream | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Other formulations on the market include ointments and oral drops.

## Safety Considerations

- **Drug Interactions**: 451 interactions are recorded. Examples include adalimumab (Major), and zidovudine, isotretinoin, acarbose, acebutolol, acetazolamide, ketorolac, nifedipine, ibuprofen and ethinylestradiol (all Moderate).
- **Conditions of concern**: Betamethasone has recorded contraindication relations with hypertension, congestive heart failure, hyperglycemia, epilepsy, herpes simplex virus keratitis, measles, and several pituitary hormone deficiency disorders. These are not taken from label text.

Please also refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the only evidence is a 1964 case series with no trials and no modern data. No cited study directly shows betamethasone efficacy in alopecia mucinosa, so the evidence is too weak to support advancing. By the evidence rules, the level should therefore be treated as L5 (model prediction only); the L4 shown above comes from the dataset's own scoring and should be downgraded on review.

**To proceed, the following is needed:**
- Controlled or at least modern observational studies of corticosteroids in follicular mucinosis
- Detailed mechanism of action data
- Package insert warnings and contraindications from the local regulator
- A safety plan covering the interaction and contraindication findings above, especially for long-term or systemic use

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not currently available for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Sernivo (betamethasone dipropionate) prescribing information, Primus Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b1b3d1b0-da9b-11eb-ad76-0800200c9a66) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

