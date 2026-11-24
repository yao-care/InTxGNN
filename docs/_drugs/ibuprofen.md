---
layout: default
title: Ibuprofen
parent: Model Prediction Only (L5)
nav_order: 418
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
monitor_inn: "Ibuprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
description: "Ibuprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). In India: at least 20 listed products"
---

# Ibuprofen
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

## Ibuprofen: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Ibuprofen is a non-steroidal anti-inflammatory drug (NSAID) originally used for rheumatoid arthritis, osteoarthritis, headache, juvenile idiopathic arthritis and patent ductus arteriosus.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction is based on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for ibuprofen: "Ibuprofen has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of CALDOLOR, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Caldolor (ibuprofen) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1eaa7790-f1a1-4f51-b10a-cbbaf033f684), label version 2026-01-29; accessed 2026-11-19.) Ibuprofen is generally known as a non-selective cyclooxygenase (COX) inhibitor with anti-inflammatory and analgesic effects, and it is established in arthritis and musculoskeletal pain.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare skeletal dysplasia caused by loss-of-function variants in the CDMP1/GDF5 gene, which disrupt cartilage and bone development. COX inhibition has no plausible way to correct this developmental defect. The prediction most likely reflects the model's network proximity to musculoskeletal and arthropathy indications rather than a biological rationale. At best, ibuprofen might relieve joint pain symptomatically, which is not a disease-modifying effect.

Other top-ranked predictions show the same pattern (all L5, all Hold): brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, brachyolmia, brachydactyly-syndactyly syndrome, pseudoachondroplasia, and colobomatous microphthalmia-rhizomelic dysplasia syndrome. Of these, pseudoachondroplasia (secondary joint pain) and myosclerosis (musculoskeletal pain) have only a speculative symptomatic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 41347 | Corflam Gel | Tube of 15 gm Gel | Valid |
| 70886 | Dualflam F 400mg/500mg Tablet | Strip of 10 tablets | Valid |
| 73770 | Endopar Oral Suspension | Bottle of 60 ml Oral Suspension | Valid |
| 108439 | Ibufen Tablet | Strip of 10 tablets | Valid |
| 108700 | Ibu 400mg Tablet | Strip of 10 tablets | Valid |
| 108824 | Ibucet 400 mg/500 mg Tablet | Strip of 10 tablets | Valid |
| 108868 | Ibuset Syrup | Bottle of 60 ml Syrup | Valid |
| 109340 | Ibuflam 400mg/500mg Tablet | Strip of 10 tablets | Valid |
| 110190 | Infanil 400 mg/325 mg Tablet | Strip of 10 tablets | Valid |
| 110356 | I Par 100mg/125mg Syrup | Bottle of 60 ml Syrup | Valid |
| 112546 | Ibugrap 400mg Tablet | Strip of 10 tablets | Valid |
| 112858 | Ibumolin Suspension | Bottle of 60 ml Suspension | Valid |
| 135215 | Metagesic SS Tablet | Strip of 10 tablets | Valid |
| 142023 | Medigesic Plus Tablet | Strip of 10 tablets | Valid |
| 148363 | Methoprofen Tablet | Strip of 10 tablets | Valid |
| 160600 | Nilflam Suspension | Bottle of 60 ml Suspension | Valid |
| 176406 | Paa Tablet | Strip of 15 tablets | Valid |
| 182028 | Paramag IP 400mg/325mg Tablet | Strip of 10 tablets | Valid |
| 217554 | Tolfen Tablet | Strip of 10 tablets | Valid |
| 244612 | Xtragesic 75mg/500mg Suspension | Bottle of 60 ml Suspension | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All 20 registrations are valid licences. Dosage forms include oral tablets, suspensions, syrups and a topical gel.

<!-- review:begin in-lic-20261124-ibuprofen-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All 20 registrations are valid single-ingredient licences." Removed: it described the products as single-ingredient (or as having no combination products), which does not match the Indian medicine data (the Indian Medicine Dataset): some of the recorded products are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124-ibuprofen-1 -->

---

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):**
Hypertension, liver failure and liver disease, kidney disease, peptic ulcer disease, inflammatory bowel disease, thrombocytopenia, blood coagulation disease, stroke and cerebrovascular disorders, myocardial infarction, diabetes mellitus and diabetic ketoacidosis, epilepsy, COPD, systemic lupus erythematosus, hypothyroidism, gallbladder disease, potassium deficiency, benign prostatic hyperplasia, hypotensive disorder, and substance abuse/dependence.

**Drug Interactions:** 687 interactions were recorded. Main examples:
- **Major:** Acetylsalicylic acid
- **Moderate:** Corticosteroids (betamethasone, budesonide, dexamethasone, hydrocortisone), sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), exenatide, aprepitant, balsalazide, fenfluramine and dexfenfluramine, kanamycin, levofloxacin
- **Minor:** Famotidine, ranitidine, cimetidine

Please refer to the package insert for label-based warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (0.9974), with no clinical trials or publications. There is no plausible mechanism linking COX inhibition to correction of a GDF5-related developmental skeletal defect. Ibuprofen's safety profile is also considerable for a chronic use in a rare paediatric-onset condition.

**To proceed, the following is needed:**
- Mechanism of action data for ibuprofen, to allow mechanistic-link analysis
- Package insert warnings and contraindications from the India licences, which are required before safety screening
- Any preclinical or clinical evidence for ibuprofen in GDF5/CDMP1-related skeletal dysplasia
- Route and dosage-form compatibility assessment for the proposed use
- If the aim is symptomatic pain relief, a focused review of ibuprofen in secondary joint pain in skeletal dysplasias (such as pseudoachondroplasia) may be more productive than this top-ranked candidate

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Indian medicine data (the Indian Medicine Dataset used by this site). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Caldolor (ibuprofen) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1eaa7790-f1a1-4f51-b10a-cbbaf033f684) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

