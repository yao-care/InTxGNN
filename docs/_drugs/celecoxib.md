---
layout: default
title: Celecoxib
parent: Model Prediction Only (L5)
nav_order: 163
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-31
description: "Celecoxib: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, ankylosing spondylitis, osteoarthritis…"
monitor_inn: "Celecoxib"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "hypermobility of coccyx", "brachyolmia", "rheumatoid nodulosis", "WHIM syndrome"]
---

# Celecoxib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Celecoxib: From Inflammatory Arthritis to Acromesomelic Dysplasia, Hunter-Thompson Type
{: .text-alpha }

## One-Sentence Summary

Celecoxib is a COX-2 inhibitor (an anti-inflammatory painkiller) originally used for arthritis, including rheumatoid arthritis, ankylosing spondylitis, osteoarthritis and juvenile idiopathic arthritis.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder.
The score is high, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, ankylosing spondylitis, osteoarthritis, juvenile idiopathic arthritis (the Indian licence records contain no approved-indication text, so this comes from the drug's known indication data) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for celecoxib: "Celecoxib has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of celecoxib is believed to be due to inhibition of prostaglandin synthesis, primarily via inhibition of COX-2. Celecoxib is a potent inhibitor of prostaglandin synthesis in vitro." ([DailyMed: Vyscoxa (celecoxib) prescribing information, Carwin Pharmaceutical Associates, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5094d47e-f791-4190-9397-b7500143a74d), label version 2025-07-31; accessed 2026-11-19.) Celecoxib is known as a selective COX-2 inhibitor that reduces prostaglandin-mediated inflammation and pain. It is proven in several inflammatory arthropathies.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare genetic skeletal dysplasia caused by loss-of-function variants in the *CDMP1/GDF5* gene. The underlying defect is in BMP/GDF signalling, which controls limb bone growth. COX-2 inhibition is not known to act on this pathway, and no clear mechanistic link was identified.

The high score most likely reflects the model's network proximity between celecoxib and arthropathy or skeletal phenotypes, not a biological rationale. The prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Celecoxib is marketed in India as a single-ingredient oral product, with 20 valid registrations and none cancelled. The data compiled for this report do not include approved-indication text for these licences. Five main registrations:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 206039 | Sionara 200mg Capsule | Strip of 10 capsules | Alembic Pharmaceuticals Ltd |
| 109396 | Icel 200mg Capsule | Strip of 10 capsules | Zydus Cadila |
| 39656 | Celicx 200 Capsule | Strip of 10 capsules | Goldenlad Pharmaceutical Pvt Ltd |
| 34934 | Coxib 90mg Tablet | Strip of 10 tablets | Micro Labs Ltd |
| 189254 | Revibra 200mg Capsule | Strip of 10 capsules | Dr Reddy's Laboratories Ltd |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these come from drug-disease relationships, not package insert text): hypertension, kidney disease, liver disease, gallbladder disease, congestive heart failure, active peptic ulcer disease, asthma, stroke and other cerebrovascular disorders, myocardial infarction and other cardiovascular or heart disease, anaemia, hemoglobinopathy, and substance abuse/dependence.
- **Drug Interactions**: 646 interactions are recorded, which is a large burden.
  - **Major**: eliglustat.
  - **Moderate (examples)**: hydrocortisone, metformin, sulfonylureas (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide), nateglinide, exenatide, cimetidine, levofloxacin, metronidazole, kanamycin, naltrexone, mesalazine, balsalazide, olsalazine, fenfluramine, dexfenfluramine.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. There are no trials or publications, and no plausible mechanism links COX-2 inhibition to the *GDF5*-related skeletal defect. The safety profile (cardiovascular, gastrointestinal and renal signals) offers no offsetting benefit for this indication.

**To proceed, the following is needed:**
- Mechanistic or preclinical evidence that COX-2 inhibition affects GDF5/BMP signalling or limb growth in this disorder
- Detailed mechanism of action data for celecoxib
- Package insert warnings and contraindications from the Indian labels
- A safety assessment relevant to the likely patient population, including paediatric use

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vyscoxa (celecoxib) prescribing information, Carwin Pharmaceutical Associates, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5094d47e-f791-4190-9397-b7500143a74d) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

