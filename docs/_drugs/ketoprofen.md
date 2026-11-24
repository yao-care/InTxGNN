---
layout: default
title: Ketoprofen
parent: Model Prediction Only (L5)
nav_order: 463
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Ketoprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "WHIM syndrome", "juvenile arthritis due to defect in LACC1"]
description: "Ketoprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). In India: at least 20 listed products"
---

# Ketoprofen
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

## Ketoprofen: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Ketoprofen is a non-steroidal anti-inflammatory drug (NSAID) originally used for arthritis conditions such as rheumatoid arthritis and osteoarthritis.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It rests on a model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for ketoprofen: "In anti-inflammatory models ketoprofen has been shown to have inhibitory effects on prostaglandin and leukotriene synthesis, to have antibradykinin activity, as well as to have lysosomal membrane-stabilizing action. However, its mode of action, like that of other non-steroidal anti-inflammatory drugs, is not fully understood." ([DailyMed: Orudis (ketoprofen) prescribing information, Allegis Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=47d0b808-7142-c7a9-e063-6394a90a6e0d), label version 2026-01-07; accessed 2026-11-19.) Based on known information, ketoprofen is an NSAID that inhibits cyclooxygenase (COX) enzymes and reduces prostaglandin-mediated inflammation and pain. Its efficacy in arthritis conditions is established.

For the top-ranked prediction, the mechanistic link is **not supported**. Acromesomelic dysplasia, Hunter-Thompson type is a skeletal dysplasia caused by loss-of-function mutations in CDMP1/GDF5. COX inhibition is not expected to correct this genetic defect. The very high TxGNN score (0.9998) is a model output only, with no trial or literature backing.

Several lower-ranked predictions are more coherent with ketoprofen's pharmacology, though none has supporting studies in the data compiled for this report:
- **Juvenile arthritis due to defect in LACC1** (score 0.9974): NSAIDs are commonly used for symptom control in juvenile arthritis, but the link is indirect and symptomatic.
- **Pseudoachondroplasia** (score 0.9995): ketoprofen might relieve joint pain and inflammation, but it would not modify the underlying disease.
- **Myosclerosis** (score 0.9998): a weak, speculative link through symptomatic anti-inflammatory and analgesic effects.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 108219 | Infen Plaster | Packet of 3 transdermal patches | Valid |
| 109215 | Infen MR 25mg/4mg Tablet | Strip of 10 tablets | Valid |
| 115737 | Ketoplast Plaster | Packet of 7 transdermal patches | Valid |
| 115862 | Ketoplast Plus Plaster | Packet of 7 transdermal patches | Valid |
| 115867 | Ketopatch 30mg Transdermal Patch | Packet of 1 Transdermal Patch | Valid |
| 116005 | Ketofen 100mg Tablet | Strip of 10 tablets | Valid |
| 116293 | Ketoflex 100mg/4mg Tablet | Strip of 10 tablets | Valid |
| 116695 | Ketofen 50mg Tablet | Strip of 10 tablets | Valid |
| 117451 | Ketolice Tablet | Strip of 10 tablets | Valid |
| 117561 | Ketoskip Tablet | Strip of 10 tablets | Valid |
| 117563 | Ketomex TH 50mg/4mg Tablet | Strip of 10 tablets | Valid |
| 117623 | Ketomex 50mg Tablet | Strip of 10 tablets | Valid |
| 118239 | Ketonid MR 50mg/4mg Tablet | Strip of 10 tablets | Valid |
| 121320 | Lupiflex 4 Tablet | Strip of 10 tablets | Valid |
| 121924 | Lupiflex 8 Tablet | Strip of 10 tablets | Valid |
| 164666 | Ostofen 50mg Capsule | Strip of 10 capsules | Valid |
| 191216 | Redufen 50mg Tablet | Strip of 10 tablets | Valid |
| 192710 | Redufen 100mg Tablet | Strip of 10 tablets | Valid |
| 204471 | Spifen MR 50mg/4mg Tablet | Strip of 10 tablets | Valid |
| 236233 | Vofane 5mg Injection | Vial of 10 ml Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

A total of 20 valid registrations exist. Formulations include oral capsules and tablets, transdermal patches and plasters, and an injection.

<!-- review:begin in-lic-20261124c-ketoprofen-1 -->

> **Review correction (2026-11-24)**: Originally stated: "A total of 20 valid single-ingredient registrations exist." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-ketoprofen-1 -->

## Safety Considerations

- **Contraindications (from the TxGNN model (deep learning), not label text; these may reflect similarities the model learned between related diseases, not biological evidence)**: hypertension and hypertensive disorder, liver failure, kidney disease, peptic ulcer disease (including active), blood coagulation disease, myocardial infarction, coronary thrombosis, cardiovascular and heart disease, hemoglobinopathy, pyoureter.
- **Drug Interactions**: 226 interactions were identified in total. Examples from the compiled list:
  - *Moderate*: acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), metformin, glimepiride, chlorpropamide, mesalazine, balsalazide, naltrexone, potassium citrate and bicarbonate, picosulfuric acid, polyethylene glycol with electrolytes.
  - *Minor*: famotidine, ranitidine, cimetidine, linaclotide.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a model score, with no clinical trials or literature, and no plausible mechanistic link between COX inhibition and the genetic basis of acromesomelic dysplasia, Hunter-Thompson type. The knowledge-graph contraindications (cardiovascular, renal, hepatic, gastrointestinal) also warrant caution.

**To proceed, the following is needed:**
- Mechanism of action data for ketoprofen
- Package insert warnings and contraindications for the Indian market
- A dedicated literature and trial search for the more plausible candidates, especially spondyloarthropathy and LACC1-related juvenile arthritis, which are better suited as research questions than the top-ranked prediction
- Confirmation of the approved indications in the India licence records

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Orudis (ketoprofen) prescribing information, Allegis Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=47d0b808-7142-c7a9-e063-6394a90a6e0d) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

