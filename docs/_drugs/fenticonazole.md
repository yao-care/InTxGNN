---
layout: default
title: Fenticonazole
parent: Model Prediction Only (L5)
nav_order: 346
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "Fenticonazole"
predicted_indications: ["trichomonal vulvovaginitis", "postmenopausal atrophic vaginitis", "vulvitis", "herpetic vulvovaginitis"]
description: "Fenticonazole: predicted new indication Trichomonal vulvovaginitis (evidence level L5). In India: at least 20 listed products"
---

# Fenticonazole
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

## Fenticonazole: Trichomonal vulvovaginitis
{: .text-alpha }

## One-Sentence Summary

Fenticonazole is a topical imidazole antifungal, marketed in India as vaginal capsules and a vaginal cream.
The TxGNN model predicts it may be useful for **trichomonal vulvovaginitis**, with a score of 0.9950.
No clinical trials and no publications specific to this disease were found, so the prediction is supported by model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Trichomonal vulvovaginitis |
| TxGNN Prediction Score | 0.9950 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. From the literature, fenticonazole is an imidazole derivative with broad antimycotic activity. It is described as acting in three ways: inhibiting secretion of acid protease by *Candida albicans*, damaging the cytoplasmic membrane, and blocking cytochrome oxidases and peroxidases. It has also been described as having some antibacterial action.

Some imidazoles have shown in vitro activity against *Trichomonas*, which gives a plausible but unconfirmed link to trichomonal infection. However, the retrieved papers concern vulvovaginal infection in general, mainly candidal. They do not show efficacy specific to trichomonal infection. The high score is a model prediction and should not be read as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No retrieved paper studies trichomonal vulvovaginitis as its own endpoint. The two papers below are the closest and are listed for context only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15216954](https://pubmed.ncbi.nlm.nih.gov/15216954/) | 2004 | Open-label multicenter pilot study | J Chemother | 101 women with single or mixed vulvovaginal infections (including *Trichomonas vaginalis*) received 1 g fenticonazole ovules on days 1 and 3; trichomonad-specific results are not given in the retrieved abstract |
| [18840006](https://pubmed.ncbi.nlm.nih.gov/18840006/) | 2008 | Review | Drugs | Review of topical fenticonazole in dermatology and gynaecology; describes antifungal mechanisms and some antibacterial action |

## India Market Information

At least 20 valid single-ingredient licences are recorded.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 34871 | Cosfen Vaginal Cream | Tube of 30 gm Vaginal Cream | Valid |
| 35154 | Cosfen Vaginal Capsule | Strip of 1 Vaginal Capsule | Valid |
| 35552 | Cosfen Vaginal Capsule | Strip of 2 Vaginal Capsules | Valid |
| 84154 | Fenza Vaginal Capsule | Strip of 2 Vaginal Capsules | Valid |
| 84206 | Fentin Vaginal Capsule | Strip of 1 Vaginal Capsule | Valid |
| 84567 | Fegus Vaginal Capsule | Strip of 1 Vaginal Capsule | Valid |
| 84635 | Fentigliv 600mg Vaginal Capsule | Strip of 1 Vaginal Capsule | Valid |
| 84737 | Fentozac 600mg Vaginal Capsule | Packet of 1 Vaginal Capsule | Valid |
| 84742 | Fenticad Vaginal Capsule | Strip of 1 Vaginal Capsule | Valid |
| 84796 | Fenti Vaginal Capsule | Strip of 1 Vaginal Capsule | Valid |
| 84925 | Fentistat Vaginal Capsule | Strip of 1 Vaginal Capsule | Valid |
| 85035 | Fentispor 600mg Capsule | Strip of 1 Capsule | Valid |
| 85766 | Fentisafe Softgel | Strip of 1 Vaginal Capsule | Valid |
| 86100 | Fivasa Vaginal Capsule | Strip of 1 Vaginal Capsule | Valid |
| 86655 | Fentisurge Vaginal Capsule | Strip of 1 Vaginal Capsule | Valid |
| 87128 | Fentiguard 600mg Vaginal Capsule | Strip of 1 Vaginal Capsule | Valid |
| 88679 | Fentifung 600mg Vaginal Capsule | Strip of 1 Vaginal Capsule | Valid |
| 134187 | Mifenti Vaginal Capsule | Strip of 1 Vaginal Capsule | Valid |
| 219550 | Tinilact FZ Softgel Capsule | Strip of 1 Vaginal Capsule | Valid |
| 236968 | VYI Fem Vaginal Capsule | Strip of 1 Vaginal Capsule | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. No trial or publication directly studies trichomonal vulvovaginitis, and the mechanistic link is only plausible.

**To proceed, the following is needed:**
- In vitro activity data of fenticonazole against *Trichomonas vaginalis*
- Clinical data with trichomonad-specific endpoints, including subgroup results from existing mixed-infection studies
- Mechanism-of-action data from DrugBank
- Package insert warnings and contraindications from the India regulator

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

