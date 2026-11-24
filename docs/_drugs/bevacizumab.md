---
layout: default
title: Bevacizumab
parent: Model Prediction Only (L5)
nav_order: 108
evidence_level: L5
indication_count: 10
monitor_inn: "Bevacizumab"
predicted_indications: ["epiglottis neoplasm", "benign neoplasm of tongue", "tumor of testis and paratestis", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "cystic neoplasm", "nasal cavity inverting papilloma", "mesenchymoma", "schwannoma of jugular foramen"]
last_modified_at: 2026-11-24
description: "Bevacizumab: predicted new indication epiglottis neoplasm (evidence level L5). In India: at least 20 listed products"
---

# Bevacizumab
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

## Bevacizumab: Anti-VEGF-A monoclonal antibody → epiglottis neoplasm
{: .text-alpha }

## One-Sentence Summary

Bevacizumab is a monoclonal antibody that blocks VEGF-A, a driver of tumour blood vessel growth, and it is marketed in India.
The TxGNN model predicts it may be effective for **epiglottis neoplasm**, with a score of 0.9990.
At present there are **no clinical trials and no publications** for this specific disease, so the support is model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | epiglottis neoplasm |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for bevacizumab: "Bevacizumab products bind VEGF and prevent the interaction of VEGF to its receptors (Flt-1 and KDR) on the surface of endothelial cells. The interaction of VEGF with its receptors leads to endothelial cell proliferation and new blood vessel formation in in vitro models of angiogenesis." ([DailyMed: Vegzelma (bevacizumab-adcd) prescribing information, CELLTRION USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4cdcccda-7b9a-49d0-ac50-f4605a3c0ebe), label version 2026-08-21; accessed 2026-11-19.) Based on general knowledge, bevacizumab binds VEGF-A and limits the growth of new blood vessels that tumours depend on.

Epiglottis neoplasms arise in the head and neck region. Head and neck tumours are often rich in blood vessels, so blocking VEGF is a plausible approach. This reasoning is speculative here. No study in the compiled data tests bevacizumab in epiglottis tumours, and the prediction score is the only support.

## Clinical Trial Evidence

Currently no related clinical trials registered for epiglottis neoplasm.

## Literature Evidence

Currently no related literature available for epiglottis neoplasm.

## India Market Information

The licence list may be partial. The licences below are a selection of the 20 valid single-ingredient registrations; no indication text is recorded for them.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 6204 | Abevmy 100mg Injection | Vial of 4 ml Injection | Valid |
| 13400 | Avastimab 400mg Injection | Vial of 16 ml Injection | Valid |
| 13987 | Avastimab 100mg Injection | Vial of 4 ml Injection | Valid |
| 15010 | Avangio Injection | Vial of 16 ml Injection | Valid |
| 21559 | Avangio Injection | Vial of 4 ml Injection | Valid |
| 26616 | Bevatas 100 Injection | Vial of 4 ml Solution for Infusion | Valid |
| 27136 | Bevacirel 100mg Injection | Vial of 4 ml Injection | Valid |
| 27457 | Bryxta 100 Injection | Vial of 1 Injection | Valid |
| 27992 | Bryxta 300 Injection | Vial of 12 ml Injection | Valid |
| 28516 | Bevarest 400 Injection | Vial of 16 ml Injection | Valid |
| 29353 | Bevacizab Injection | Vial of 4 ml Injection | Valid |
| 29717 | Bevacizab Injection | Vial of 16 ml Injection | Valid |
| 31461 | Bevnexxa 400mg Injection | Vial of 16 ml Injection | Valid |
| 36203 | Cizumab 400 Solution for Infusion | Vial of 16 ml Solution for Infusion | Valid |
| 110852 | Ivzumab 400 Solution for Injection | Vial of 16 ml Solution for Injection | Valid |
| 116518 | Krabeva 400mg Injection | Vial of 1 Injection | Valid |
| 116540 | Krabeva 100mg Injection | Vial of 4 ml Injection | Valid |
| 233880 | Versavo 400 Solution for Infusion | Vial of 16 ml Solution for Infusion | Valid |
| 234792 | Versavo 100 Solution for Infusion | Vial of 4 ml Solution for Infusion | Valid |
| 247719 | Zybev 100mg Injection | Vial of 4 ml Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-VEGF monoclonal antibody) |
| Myelosuppression Risk | Low as a single agent; please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Low |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 22 interactions were identified in the data compiled for this report. The main ones rated Major are deferiprone, samarium (153Sm) lexidronam, panitumumab, sunitinib and thalidomide. Others are rated Moderate, including bisphosphonates (alendronic, risedronic, etidronic, pamidronic, ibandronate and tiludronic acids), filgrastim, pegfilgrastim, sargramostim, palifermin, idelalisib, romosozumab, radium Ra 223 dichloride, strontium chloride Sr-89 and sodium phosphate P32.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (0.9990), but no trial or publication studies bevacizumab in epiglottis neoplasm. Evidence is therefore at L5 (model prediction only).

**To proceed, the following is needed:**
- Search for clinical or preclinical data on bevacizumab in laryngeal and epiglottic tumours
- Detailed mechanism-of-action data
- Package insert warnings and contraindications from the Indian licence holders
- A safety review of the major drug interactions, especially with sunitinib, panitumumab and thalidomide

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vegzelma (bevacizumab-adcd) prescribing information, CELLTRION USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4cdcccda-7b9a-49d0-ac50-f4605a3c0ebe) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

