---
layout: default
title: Naproxen
parent: Model Prediction Only (L5)
nav_order: 579
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "Naproxen"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome"]
description: "Naproxen: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). In India: at least 20 listed products"
---

# Naproxen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Naproxen: Brachydactyly-syndactyly syndrome
{: .text-alpha }

## One-Sentence Summary

Naproxen is a non-steroidal anti-inflammatory drug (NSAID) originally used for conditions such as rheumatoid arthritis, osteoarthritis, ankylosing spondylitis, gout, bursitis, tendinitis and migraine.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 0.9935 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for naproxen: "Naproxen has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of NAPRELAN, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Naprelan (naproxen sodium) prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b8a51c9a-488e-4377-a041-436f6a2f8893), label version 2026-01-08; accessed 2026-11-19.) Naproxen is generally known as a non-selective COX inhibitor with anti-inflammatory and analgesic effects, and its efficacy in inflammatory joint and pain conditions is established.

Brachydactyly-syndactyly syndrome, however, is a congenital skeletal malformation with a developmental and genetic basis. Blocking prostaglandin synthesis is not expected to correct a structural limb patterning defect, so no mechanistic link is supported by the available data. The high score (0.9935) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other three top-ranked predictions show the same pattern. All are rare congenital developmental syndromes, with no trials or literature:
- Colobomatous microphthalmia-rhizomelic dysplasia syndrome (0.9922)
- Acromesomelic dysplasia, Hunter-Thompson type (0.9917)
- Brachyolmia-amelogenesis imperfecta syndrome (0.9906)

At most, naproxen might relieve joint pain symptomatically in some of these patients, which is not a repurposing claim.

## India Market Information

Naproxen has 20 valid single-ingredient registrations and no cancelled ones. The data compiled for this report do not include approved indication text for these products.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 1660 | Arthopan 250mg Tablet | Strip of 10 tablets | Valid |
| 34499 | Comig 500 Tablet | Strip of 10 tablets | Valid |
| 49278 | Cronta 250mg Tablet | Strip of 10 tablets | Valid |
| 59099 | Domstal NP 250mg/10mg Tablet | Strip of 10 tablets | Valid |
| 150316 | Naxdom 250 Tablet | Strip of 15 tablets | Valid |
| 151203 | Naprosyn 125mg Suspension | Bottle of 60 ml Suspension | Valid |
| 151300 | Naprox 250 D Tablet | Strip of 10 tablets | Valid |
| 152315 | Napsea Tablet | Strip of 10 tablets | Valid |
| 152536 | Naprolet D 250mg/10mg Tablet | Strip of 10 tablets | Valid |
| 153567 | Napaid-D Tablet | Strip of 10 tablets | Valid |
| 153658 | Nippo D 500mg/10mg Tablet | Strip of 10 tablets | Valid |
| 153983 | Nalyxan 250mg Tablet | Strip of 10 tablets | Valid |
| 154286 | Napican 250mg/10mg Tablet | Strip of 10 tablets | Valid |
| 155747 | Napnet D 250mg/10mg Tablet | Strip of 10 tablets | Valid |
| 158243 | Napseep 500mg/10mg Tablet | Strip of 10 tablets | Valid |
| 174354 | Proxidom 250mg Tablet | Strip of 10 tablets | Valid |
| 174635 | Proxzol 500mg/20mg Tablet | Strip of 10 tablets | Valid |
| 236381 | Vomigra 250mg/10mg Tablet | Strip of 10 tablets | Valid |
| 238096 | Volprox 500mg/10mg Tablet | Strip of 10 tablets | Valid |
| 244550 | Xenap 250 Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Available forms are oral tablets and an oral suspension. Several registrations are fixed-dose products (for example, the "D" and "250mg/10mg" products), and the Indian Medicine Dataset lists a second active ingredient for them.

<!-- review:begin in-lic-20261124b-naproxen-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Several registrations are fixed-dose products, although the data classify all as single-ingredient (for example, the "D" and "250mg/10mg" products)." Revised: the sentence said the data classify these products as single-ingredient, but the Indian Medicine Dataset lists a second active ingredient for several of them (they are fixed-dose combinations). Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124b-naproxen-1 -->

## Safety Considerations

- **Contraindications / disease associations (knowledge graph, not label text)**: Naproxen is linked to the following conditions, grouped by area:
  - Cardiovascular: hypertension, congestive heart failure, coronary artery disease, coronary atherosclerosis, myocardial infarction, coronary thrombosis, stroke, cerebrovascular disorder, cerebral infarction
  - Liver and kidney: liver failure, liver disease, kidney disease, gallbladder disease
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, obesity, osteoporosis
  - Blood: blood coagulation disease, anaemia, hemoglobinopathy
  - Other: epilepsy, benign prostatic hyperplasia, substance abuse/dependence
- **Drug Interactions**: 309 interactions are recorded. The 20 listed in the data are all Moderate-level and include:
  - Acid-lowering agents: famotidine, ranitidine, cimetidine, rabeprazole, dexlansoprazole
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
  - Other: acetylsalicylic acid, metformin, chlorpropamide, mesalazine, balsalazide, aprepitant, potassium citrate, potassium bicarbonate

Please refer to the package insert for warnings and formal contraindications, as label-based data were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (L5), with no clinical trials or publications, and there is no plausible mechanistic link between COX inhibition and correcting a congenital skeletal malformation. The cardiovascular, renal, hepatic and gastrointestinal risk profile of naproxen further weakens any case for use in this setting.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) and a documented rationale linking it to the disease's biology
- Any preclinical, case-based or clinical evidence in this or related syndromes
- Package insert warnings and contraindications for the India products
- Route and formulation compatibility assessment
- Confirmation of whether any benefit would be only symptomatic (joint pain) rather than disease-modifying

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Naprelan (naproxen sodium) prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b8a51c9a-488e-4377-a041-436f6a2f8893) |
| 2026-11-24 | Revised: the single-ingredient classification | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

