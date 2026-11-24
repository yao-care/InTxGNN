---
layout: default
title: Biotin
parent: Model Prediction Only (L5)
nav_order: 111
evidence_level: L5
indication_count: 2
monitor_inn: "Biotin"
predicted_indications: ["dyspepsia", "gastroparesis (disease)"]
last_modified_at: 2026-11-24
description: "Biotin: predicted new indication dyspepsia (evidence level L5). In India: 18 listed products (18 not discontinued)"
---

# Biotin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Biotin: Vitamin B7, a carboxylase cofactor → dyspepsia
{: .text-alpha }

## One-Sentence Summary

Biotin (vitamin B7) is a cofactor for carboxylase enzymes involved in carbohydrate, fat and amino acid metabolism. The TxGNN model predicts it may be useful for **dyspepsia**, with a score of 0.9943. However, **no clinical trials** and **no publications that show biotin treating dyspepsia** are available, so this remains a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | dyspepsia |
| TxGNN Prediction Score | 0.9943 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (18 of 18) – CDSCO approval status is not included in this data |
| Number of Listed Products | 18 (valid: 18) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general knowledge, biotin is a cofactor for carboxylases that take part in carbohydrate, fat and amino acid metabolism. Deficiency can cause gastrointestinal symptoms such as nausea and loss of appetite.

This gives only a loose, indirect link to dyspepsia. It would apply at most in a deficiency state, not in general functional dyspepsia. No supporting mechanism specific to dyspepsia is established in the available data, so the prediction should be treated as hypothesis-generating.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the retrieved publications shows that biotin treats dyspepsia. The only biotin-related item is a case report in which dyspepsia was the reason for an amino acid formula diet, and biotin deficiency followed.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Case report | The Journal of Dermatology | A 5-month-old infant diagnosed with dyspepsia as a neonate and fed only an amino acid formula developed biotin deficiency (alopecia, scaly dermatitis) with low serum and urine biotin. This is deficiency caused by diet, not treatment of dyspepsia. |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Clinical article | Eksperimental'naia i klinicheskaia gastroenterologiia | A prebiotic and vitamin supplement (biotin is one of many ingredients) was studied for gut microbiota disorders in patients with lung disease on antibiotics. It is not specific to biotin or dyspepsia. |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Observational | International Journal of Molecular Medicine | Stomach antral endocrine cells in irritable bowel syndrome. Not related to biotin. |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Observational | World Journal of Gastrointestinal Endoscopy | Endocrine cells in the stomach's oxyntic mucosa in irritable bowel syndrome. Not related to biotin. |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Observational | Journal of Clinical Pathology | Interleukin 10 in Helicobacter pylori gastritis. Not related to biotin. |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Observational | Kidney International | Small bowel T cells and stress protein in IgA nephropathy. Not related to biotin. |

---

## India Market Information

Biotin is marketed in India; all its recorded licences are valid and none are cancelled. The licence records carry no approved indication text.

<!-- review:begin in-lic-20261106-biotin-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Biotin is marketed in India, with 18 valid single-ingredient licences and none cancelled." Removed: it described the products as single-ingredient or combination products in a way that did not match the Indian medicine data (the Indian Medicine Dataset as of 2026-11-06). Revised 2026-11-24: the hard-coded number of records and the wording about the old table were dropped; the Quick Overview and the product table under India Market Information show the current figures. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261106-biotin-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 2561 | Actihair 5mg/5mg Tablet | Strip of 10 tablets | Valid |
| 26474 | Bio Hairr-F Tablet | Strip of 10 tablets | Valid |
| 26648 | Bio-CP Tablet | Strip of 10 tablets | Valid |
| 27432 | Biovib 5mg Tablet | Strip of 10 tablets | Valid |
| 27618 | Bkosa-F Tablet | Strip of 10 tablets | Valid |
| 27674 | Bitvin-F 10mg/1mg Tablet | Strip of 10 tablets | Valid |
| 27963 | B7F 5mg/1mg Tablet | Strip of 15 tablets | Valid |
| 84957 | Folliriz 10mg/1mg Tablet | Strip of 10 tablets | Valid |
| 85165 | Folivern-Plus Tablet | Strip of 10 tablets | Valid |
| 85762 | F 1 Rise Plus Tablet | Strip of 10 tablets | Valid |
| 86266 | Finrest-B 10mg/1mg Tablet | Strip of 10 tablets | Valid |
| 104428 | Hair-O-Tin Plus Tablet | Strip of 10 tablets | Valid |
| 115809 | Kerashine-F Tablet | Strip of 10 tablets | Valid |
| 152874 | Nexotin 5mg Tablet | Strip of 10 tablets | Valid |
| 216489 | Tinfal Plus 5mg/1mg Tablet | Strip of 10 tablets | Valid |
| 217989 | Tressotin 10mg Tablet | Strip of 10 tablets | Valid |
| 233561 | Vitahix 5 Tablet | Strip of 10 tablets | Valid |
| 243923 | Xtin Plus Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

---

## Safety Considerations

Label warnings and contraindications are not available in the data compiled for this report; please refer to the package insert. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score. There are no clinical trials, and no cited study shows biotin treating dyspepsia. The mechanism data are missing, and the link to dyspepsia is indirect at best.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological link between biotin and dyspepsia
- Clinical or observational studies that directly examine biotin in dyspepsia
- Package insert warnings and contraindications from the India regulatory source for safety screening

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "single-ingredient" | Corrected (revised 2026-11-24; earlier version kept in the record) | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

