---
layout: default
title: Indomethacin
parent: Model Prediction Only (L5)
nav_order: 432
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Indomethacin"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "WHIM syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "brachyolmia", "myosclerosis", "juvenile idiopathic arthritis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid nodulosis"]
description: "Indomethacin: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). In India: at least 20 listed products"
---

# Indomethacin
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

## Indomethacin: Brachydactyly-syndactyly syndrome
{: .text-alpha }

## One-Sentence Summary

Indomethacin is a nonsteroidal anti-inflammatory drug (NSAID) used for inflammatory joint and soft-tissue conditions such as rheumatoid arthritis, ankylosing spondylitis, gout, osteoarthritis and bursitis. It is also used to close patent ductus arteriosus.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, a rare congenital limb malformation.
However, there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for indomethacin: "Indomethacin has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of INDOCIN, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Indocin (indomethacin) prescribing information, Zyla Life Sciences US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=73878376-1d24-423b-9f37-3666e83c95da), label version 2024-12-16; accessed 2026-11-19.) Indomethacin belongs to the NSAID class and is generally understood to reduce prostaglandin-driven inflammation by inhibiting cyclooxygenase (COX) enzymes. This is why it works in inflammatory arthritis and gout.

Brachydactyly-syndactyly syndrome, however, is a rare congenital limb malformation with a genetic developmental basis. It is not an inflammatory disease, and no mechanistic link between COX inhibition and limb patterning has been established. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The rationale for this prediction is therefore weak. It should be treated as a computational signal only, with no biological or clinical support at present.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Indomethacin is marketed in India with 20 valid single-ingredient registrations and no cancelled ones. The approved indication text is not specified for any of them.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 5352 | Ancap 75mg Capsule SR | Strip of 10 capsule sr | Valid |
| 13012 | Artid 75mg Capsule SR | Strip of 10 capsule sr | Valid |
| 38633 | Cinmin-SR Capsule | Strip of 10 capsule sr | Valid |
| 62390 | DavaIndia Indomethacin 25mg Capsule | Strip of 10 capsules | Valid |
| 62999 | Dotgesic 75mg Capsule SR | Strip of 10 capsule sr | Valid |
| 63620 | Dolitol 75 SR Tablet | Strip of 10 tablet sr | Valid |
| 107709 | Indocap SR Capsule | Strip of 10 capsule sr | Valid |
| 108143 | Inmecin 50mg Capsule | Strip of 10 capsules | Valid |
| 108247 | Indomax-SR Capsule | Strip of 10 capsule er | Valid |
| 108477 | Inmeth Suppositories | Strip of 5 suppositories | Valid |
| 108574 | Indovent 75mg Capsule SR | Strip of 10 capsule sr | Valid |
| 108577 | Inocin 25mg Capsule | Strip of 8 capsules | Valid |
| 108760 | Idicin 25mg Capsule | Strip of 10 capsules | Valid |
| 108850 | Indobest 25mg Tablet | Strip of 10 tablets | Valid |
| 108913 | Indofen 25mg Tablet | Strip of 10 tablets | Valid |
| 108966 | Inmecin 75mg Capsule | Strip of 10 capsules | Valid |
| 109975 | Indometh 75mg Tablet SR | Strip of 10 tablet sr | Valid |
| 110796 | Indoriv 25mg Capsule | Strip of 10 capsules | Valid |
| 110921 | Indolous 75 Capsule ER | Strip of 10 capsule er | Valid |
| 136316 | Microcid 75mg Capsule | Strip of 10 capsules | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Available forms are mainly oral (tablets, capsules, sustained- and extended-release) plus rectal suppositories.

## Safety Considerations

- **Drug Interactions**: 252 interactions were recorded, mostly minor or moderate. Notable moderate-level interactions include:
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide)
  - Acetylsalicylic acid
  - Metformin and sulfonylureas (chlorpropamide, glimepiride)
  - Mesalazine and balsalazide
  - Aprepitant
  - Potassium salts (potassium citrate, potassium bicarbonate)

  Minor interactions include H2 blockers (famotidine, ranitidine, cimetidine).
- **Conditions flagged as contraindication-related in the knowledge graph** (not label text): this is a general NSAID-type signal and should be verified against the package insert.
  - Cardiovascular: hypertension, myocardial infarction, heart disease
  - Gastrointestinal: peptic and gastric ulcers, ulcerative colitis, inflammatory bowel disease
  - Renal and hepatic: kidney disease, liver disease
  - Bleeding and blood: coagulation disorders, thrombocytopenia, intracerebral hemorrhage
  - Respiratory: asthma
  - Neurological: epilepsy

Please refer to the package insert for authoritative warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no literature, and no plausible mechanistic link between COX inhibition and a genetic limb malformation. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Indomethacin carries meaningful cardiovascular, gastrointestinal and renal risks that are not justified by any evidence of benefit here.

**To proceed, the following is needed:**
- Detailed mechanism of action data, and any biological evidence linking prostaglandin pathways to this syndrome
- Package insert warnings and contraindications for the marketed Indian products
- Any preclinical or case-level evidence in this condition

**Note on other predictions:** Among the other top-ranked predictions, juvenile idiopathic arthritis (rank 8) has the most support (L3, older reviews and one 1978 double-blind comparison). However, this is an established symptomatic NSAID use rather than a novel repurposing, and it does not show disease modification.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Indocin (indomethacin) prescribing information, Zyla Life Sciences US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=73878376-1d24-423b-9f37-3666e83c95da) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

