---
layout: default
title: Sodium Fluoride
parent: Model Prediction Only (L5)
nav_order: 780
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Sodium Fluoride: predicted new indication Epiglottitis (evidence level L5). Approved use: Vitamin deficiency disorder"
monitor_inn: "Sodium fluoride"
predicted_indications: ["epiglottitis", "urinary tract infection (disease)", "gonococcal urethritis", "Ureaplasma urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "laryngitis"]
---

# Sodium Fluoride
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

## Sodium Fluoride: From Vitamin Deficiency Disorder to Epiglottitis
{: .text-alpha }

## One-Sentence Summary

Sodium fluoride is originally associated with vitamin deficiency disorder in the underlying knowledge graph, and it is marketed in India in tablet, injectable and dental varnish forms.
The TxGNN model predicts it may be effective for **epiglottitis**, but **no clinical trials and no publications** support this prediction.
The prediction is a model output only and has no mechanistic or clinical backing in the data compiled for this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin deficiency disorder (from the knowledge graph; no approved indication text is available in the Indian licence records) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sodium fluoride is a fluoride salt used mainly in oral and dental products and as a mineral supplement, and no plausible link to its original indication of vitamin deficiency disorder has been established in the data.

Epiglottitis is an acute infection of the epiglottis, typically caused by bacteria such as *Haemophilus influenzae* type b. It is treated with airway management and systemic antibiotics. Sodium fluoride has no recognised antibacterial role in this setting.

The high score most likely reflects similarity in the knowledge-graph neighbourhood, not a real biological mechanism. Several other top predictions are infections (urinary tract infection, gonococcal urethritis, Ureaplasma urethritis, xanthogranulomatous pyelonephritis), and two of them share an identical score. This pattern points to a graph artifact rather than a disease-specific signal. The prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for epiglottitis.

A search for the lower-ranked prediction, laryngitis, returned four publications. None shows therapeutic evidence, and they are keyword-level matches only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29245332](https://pubmed.ncbi.nlm.nih.gov/29245332/) | 2017 | Case report | Medicine | Elevated 18F-NaF PET-CT uptake in the cricoid cartilage of a patient with laryngeal carcinoma (diagnostic imaging, not treatment) |
| [42721223](https://pubmed.ncbi.nlm.nih.gov/42721223/) | 2026 | Imaging study | Cartilage | [18F]NaF and [18F]FDG PET/CT used to assess calcification and glucose metabolism in thyroid cartilage with age |
| [24178785](https://pubmed.ncbi.nlm.nih.gov/24178785/) | 2013 | Animal toxicology | Biol Trace Elem Res | High dietary fluorine suppressed intestinal development in broilers |
| [235491](https://pubmed.ncbi.nlm.nih.gov/235491/) | 1975 | In vitro | Infect Immun | Ammonium chloride protected cultured cells from diphtheria toxin (not related to fluoride therapy) |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 162335 | Otoflour Tablet | Strip of 10 tablets | Not specified |
| 151622 | Nunaf Tablet | Strip of 10 tablets | Not specified |
| 86376 | Fluoritop SR Dental Varnish 1.5 ml | Bottle of 1 paint | Not specified |
| 59448 | D Flour Tablet | Strip of 10 tablets | Not specified |
| 84203 | Florocid Injection | Ampoule of 8 injections | Not specified |

All five registrations are valid single-ingredient products.

---

## Safety Considerations

- **Contraindications (from knowledge-graph associations, not label text)**: kidney disease, nephrolithiasis, nephrocalcinosis, acute urate nephropathy, nephrolithiasis susceptibility caused by SLC26A1, pyoureter, sarcoidosis, hyperparathyroidism, osteitis fibrosa, hypercalcemia disease, phosphorus metabolism disease, constipation disorder, lytic metastatic bone lesion, and dental fluorosis.

Please refer to the package insert for further safety information, including warnings and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no supporting literature and no plausible mechanism. Epiglottitis already has well-established treatment, and the knowledge-graph contraindications (notably renal conditions) add caution.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) and a testable antibacterial or anti-inflammatory rationale
- Package insert warnings and contraindications for the Indian products
- Preclinical or in vitro evidence for activity relevant to epiglottitis
- Confirmation of the approved indications and routes of administration for the registered products
- Review of whether the high-scoring infection predictions reflect a graph artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

