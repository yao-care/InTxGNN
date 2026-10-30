---
layout: default
title: Thiamine
parent: Model Prediction Only (L5)
nav_order: 829
evidence_level: L5
indication_count: 3
monitor_inn: "Thiamine"
predicted_indications: ["resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "primary hereditary glaucoma", "open-angle glaucoma"]
last_modified_at: 2026-10-30
description: "Thiamine: predicted new indication resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta (evidence level L5). Approved use: Not available"
---

# Thiamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Thiamine: From an Unspecified Original Indication to resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta
{: .text-alpha }

## One-Sentence Summary

Thiamine (vitamin B1) is marketed in India mainly as injectable products, but the data compiled for this report contain no approved indication text, so its original licensed use cannot be stated.
The TxGNN model ranks **resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta** first (score 0.9943) and **primary hereditary glaucoma** second. This report focuses on **open-angle glaucoma**, the only candidate with any published literature, where **0 clinical trials** and **6 publications** were found. Most of these publications are observational or only tangentially related.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the licence records) |
| Predicted New Indication | Top-ranked: resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta. Best-supported: open-angle glaucoma |
| TxGNN Prediction Score | 0.9943 (top-ranked); 0.9936 (open-angle glaucoma) |
| Evidence Level | L5 (see note below) |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | At least 20 (the list may be partial) |
| Recommended Decision | Hold |

**Note on evidence level:** The open-angle glaucoma candidate has one 1979 observational study that directly examines thiamine in chronic open-angle glaucoma, but it only compares blood levels. It does not test thiamine as a treatment. The other papers address glaucoma biology, niacin, or nutrient intake generally. No cited study evaluates thiamine as a treatment for the predicted disease, so the ceiling rule gives L5.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Thiamine is a vitamin that acts as a cofactor for enzymes of carbohydrate metabolism, such as pyruvate dehydrogenase and transketolase. This role in cellular energy production is general background knowledge rather than data compiled for this report.

**Open-angle glaucoma:** The link is plausible but indirect. Mitochondrial dysfunction and oxidative stress are implicated in retinal ganglion cell loss and trabecular meshwork dysfunction. A 1979 study of 38 glaucoma patients and 12 controls reported significantly lower blood thiamine in the patients (P < 0.001). This shows an association with nutritional status only. It does not show that giving thiamine changes intraocular pressure or disease course.

**Top-ranked and second-ranked predictions:** No mechanistic link is identifiable for thyroid hormone resistance, which is a monogenic disorder of the receptor that thiamine is not known to affect. Primary hereditary glaucoma is driven mainly by genetic defects in aqueous outflow development, which thiamine is not known to correct. Neither candidate has any trial or publication, so these predictions rest on the TxGNN model (deep learning) score alone.

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the three predicted indications.

## Literature Evidence

For open-angle glaucoma (abstracts were truncated, so the summaries below rely on titles and the visible text):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [485004](https://pubmed.ncbi.nlm.nih.gov/485004/) | 1979 | Observational | Annals of Ophthalmology | Patients with chronic open-angle glaucoma (n=38) had significantly lower blood thiamine than controls (n=12); no difference in ascorbic acid; poor thiamine absorption noted |
| [32214001](https://pubmed.ncbi.nlm.nih.gov/32214001/) | 2020 | Cross-sectional | Nutrients | Korean national survey on obesity, nutrient supply and primary open-angle glaucoma |
| [29565276](https://pubmed.ncbi.nlm.nih.gov/29565276/) | 2018 | Cross-sectional | Nutrients | Dietary niacin (not thiamine) and open-angle glaucoma in Korean survey data |
| [40402521](https://pubmed.ncbi.nlm.nih.gov/40402521/) | 2025 | Metabolomic profiling | Investigative Ophthalmology & Visual Science | Aqueous humor metabolomics in glaucoma patients; metabolites with anti-inflammatory and neuroprotective potential tested in mice |
| [30025119](https://pubmed.ncbi.nlm.nih.gov/30025119/) | 2018 | Molecular profiling | Investigative Ophthalmology & Visual Science | microRNA profiles in glaucomatous optic neuropathy |
| [41889963](https://pubmed.ncbi.nlm.nih.gov/41889963/) | 2026 | Preclinical (preprint) | bioRxiv | MIF-CD74 signaling in trabecular meshwork dysfunction in glaucoma |

## India Market Information

At least 20 licences are recorded for single-ingredient thiamine products (the list may be partial). None of the records include approved indication text. Five examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 136127 | Macraberin Forte Injection | Vial of 2 ml injection | Not stated in records |
| 218000 | Thi 100mg Injection | Vial of 2 ml injection | Not stated in records |
| 157754 | Nexmin 100mg Injection | Vial of 2 ml injection | Not stated in records |
| 28629 | B Colex Injection | Vial of 1 ml injection | Not stated in records |
| 248276 | Zeba Syrup | Bottle of 200 ml syrup | Not stated in records |

Nearly all listed products are injectables. The only exception is one oral syrup.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN scores are very high (about 0.9940), but no clinical trial supports any of the three predictions. For open-angle glaucoma the literature shows only an association between low blood thiamine and disease, which is not evidence of treatment benefit. The two higher-ranked predictions have no identifiable mechanistic link.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications for the India licences
- Mechanism of action data from DrugBank
- A controlled study or well-designed trial of thiamine supplementation in open-angle glaucoma (intraocular pressure and visual field outcomes)
- Review of full abstracts and full texts, since this assessment relied on truncated abstracts
- Route and formulation assessment, since the marketed products are mostly injectables
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

