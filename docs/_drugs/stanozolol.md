---
layout: default
title: Stanozolol
parent: Model Prediction Only (L5)
nav_order: 789
evidence_level: L5
indication_count: 9
monitor_inn: "Stanozolol"
predicted_indications: ["serpinopathy with toxic serpin polymerization", "fetal erythroblastosis", "Peyronie disease", "renal tubular acidosis", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "complement component C1s deficiency", "focal myositis", "idiopathic eosinophilic myositis"]
last_modified_at: 2026-11-24
description: "Stanozolol: predicted new indication Serpinopathy with toxic serpin polymerization (evidence level L5). In India: 10 listed products (10 not discontinued)"
---

# Stanozolol
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

## Stanozolol: Serpinopathy with toxic serpin polymerization
{: .text-alpha }

## One-Sentence Summary

Stanozolol is a synthetic anabolic-androgenic steroid that is marketed in India as oral and injectable products.
The TxGNN model predicts it may be relevant to **serpinopathy with toxic serpin polymerization**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Serpinopathy with toxic serpin polymerization |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (10 of 10) – CDSCO approval status is not included in this data |
| Number of Listed Products | 10 (valid: 10) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of stanozolol as: Androgen Receptor agonist ([ChEMBL CHEMBL2079587 (stanozolol): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2079587), CC BY-SA 3.0; accessed 2026-11-19.) Based on its drug class, stanozolol is an androgen receptor agonist that changes gene expression in the liver. It could therefore alter the production of hepatic serpin proteins. That is the only conceivable link to this disease.

This link is speculative and may even point the wrong way. In toxic polymerization disorders, such as alpha-1 antitrypsin deficiency, higher expression of a mutant serpin could worsen aggregation and liver injury. The high model score has no supporting trial or publication, so it should be treated as a hypothesis for laboratory investigation, not as a treatment signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Stanozolol is marketed in India, and all of the single-ingredient licences in the local data are valid. Approved-indication text is not recorded in the local data.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 96382 | Ganzol 2mg Tablet | Strip of 10 tablets | Valid |
| 133612 | Menabol Tablet | Strip of 20 tablets | Valid |
| 134969 | Menabol 2mg Tablet | Strip of 10 tablets | Valid |
| 150720 | Neurabol Capsule | Strip of 10 capsules | Valid |
| 152285 | Neuro bal 2mg Capsule | Strip of 10 capsules | Valid |
| 201612 | Stanza 20 Tablet | Strip of 10 tablets | Valid |
| 201784 | Stazol 50 Injection | Ampoule of 1 ml Injection | Valid |
| 202402 | Stanosafe 2mg Tablet | Strip of 30 tablets | Valid |
| 203547 | Stenfil 2mg Tablet | Strip of 10 tablets | Valid |
| 217404 | Tanzol 2mg Capsule | Strip of 10 capsules | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Disease conditions flagged as contraindications** (from the data compiled for this report, not from label text): kidney disease, liver disease, gallbladder disease, nephrotic syndrome, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, prostate cancer, hypercalcemia and nephrocalcinosis, and heart and coronary artery disease.
- **Drug interactions**: 69 interactions are recorded.
  - Carfilzomib is rated **Major**.
  - Moderate interactions include the corticosteroids hydrocortisone, dexamethasone, betamethasone, triamcinolone and budesonide. Others include cyclosporine, chlorpropamide, clofarabine, cannabidiol and asparaginase products.
- **General class concerns**: anabolic-androgenic steroids are associated with liver toxicity and muscle injury, and they are contraindicated in pregnancy because of fetal virilization. Package insert warnings were not available for this report, so please consult the insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials or publications for this disease, so the evidence level is L5. The only conceivable mechanism is speculative and may worsen the disease, and the safety profile of this drug class is unfavorable.

**To proceed, the following is needed:**
- Mechanism-of-action data for stanozolol.
- Preclinical evidence on how stanozolol affects expression, folding and polymerization of the relevant serpin.
- Package insert warnings and contraindications from the Indian licences.
- A risk assessment for liver toxicity, given the disease's liver involvement.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for stanozolol are not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL2079587 (stanozolol): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2079587) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

