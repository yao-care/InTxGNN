---
layout: default
title: Doxofylline
parent: Model Prediction Only (L5)
nav_order: 288
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Doxofylline: predicted new indication Pierre Robin syndrome associated with a chromosomal anomaly (evidence level L5). Approved use: Not stated in the India licence records. Published literature desc…"
monitor_inn: "Doxofylline"
predicted_indications: ["Pierre Robin syndrome associated with a chromosomal anomaly", "Laubry-Pezzi syndrome", "Jeune syndrome situs inversus", "genetic syndromic Pierre Robin syndrome", "orofacial clefting syndrome", "partial deletion of the long arm of chromosome 7", "disorder of fucoglycosan synthesis", "partial deletion of the long arm of chromosome 22", "heart disease", "pulmonary valve disease"]
---

# Doxofylline
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

## Doxofylline: From Asthma and COPD to Pierre Robin Syndrome Associated with a Chromosomal Anomaly
{: .text-alpha }

## One-Sentence Summary

Doxofylline is a xanthine bronchodilator used for respiratory disease (asthma and chronic obstructive pulmonary disease).
The TxGNN model predicts it may be effective for **Pierre Robin syndrome associated with a chromosomal anomaly**,
but **no clinical trials and no publications** currently support this prediction. It is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India licence records. Published literature describes use in asthma and COPD |
| Predicted New Indication | Pierre Robin syndrome associated with a chromosomal anomaly |
| TxGNN Prediction Score | 0.9954 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From the published literature, doxofylline is a methylxanthine bronchodilator. It is thought to act through phosphodiesterase inhibition, with weaker binding to adenosine A1 and A2 receptors than theophylline. This may explain its better cardiovascular tolerability.

The predicted indication is a craniofacial developmental condition linked to a chromosomal anomaly. It is not a respiratory-smooth-muscle disorder, and no plausible mechanistic link to doxofylline was identified. A bronchodilator would not be expected to alter the developmental or genetic basis of this syndrome. The high score (0.9954, rank 7922) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so this prediction should be treated with considerable caution.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for this predicted indication.

## India Market Information

Twenty valid single-ingredient registrations are on record. The licence records do not include approved indication text. Five representative authorisations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 62957 | Doxo M 400mg/10mg Tablet | Strip of 10 tablets | Not stated |
| 64027 | Doxygrap 400mg Tablet | Strip of 10 tablets | Not stated |
| 196133 | Roaron M 400mg/10mg Tablet SR | Strip of 10 sustained-release tablets | Not stated |
| 60384 | Doxside AM Tablet | Strip of 10 tablets | Not stated |
| 79950 | Evomont D 400mg/10mg Tablet | Strip of 10 tablets | Not stated |

All products are oral tablets. The registered product names suggest that some are fixed-dose combinations, although the records classify all of them as single-ingredient.

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction data are available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials or publications for this indication, and no plausible mechanistic link between a xanthine bronchodilator and a chromosomal craniofacial syndrome. Doxofylline is already widely marketed in India, but only for respiratory use.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) and a biological rationale linking doxofylline to the pathology of the syndrome
- Package insert warnings and contraindications from the India regulatory source
- Original approved indication text from the licence records
- Any preclinical or clinical evidence specific to this condition

## Other Predictions Reviewed

The other nine top-ranked predictions were also reviewed. None has supporting clinical trials. Only the "heart disease" prediction shows any indirect evidence, and it is graded L4 as a research question rather than a candidate for development.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Laubry-Pezzi syndrome | 0.9954 | L5 | Structural cardiac defect; no mechanistic link |
| 3 | Jeune syndrome situs inversus | 0.9954 | L5 | Skeletal ciliopathy; at most theoretical symptom relief |
| 4 | Genetic syndromic Pierre Robin syndrome | 0.9953 | L5 | No mechanistic link |
| 5 | Orofacial clefting syndrome | 0.9953 | L5 | Developmental malformation; no mechanistic link |
| 6 | Partial deletion of the long arm of chromosome 7 | 0.9953 | L5 | No pharmacological rationale |
| 7 | Disorder of fucoglycosan synthesis | 0.9952 | L5 | Retrieved literature covers asthma/COPD only |
| 8 | Partial deletion of the long arm of chromosome 22 | 0.9952 | L5 | No pharmacological rationale |
| 9 | Heart disease | 0.9950 | L4 | Indirect evidence only (research question) |
| 10 | Pulmonary valve disease | 0.9950 | L5 | Structural valve disorder; no rationale |

For heart disease, the available evidence concerns cardiovascular safety. Doxofylline shows fewer cardiostimulant effects than theophylline ([PMID 2781149](https://pubmed.ncbi.nlm.nih.gov/2781149/), [PMID 11268710](https://pubmed.ncbi.nlm.nih.gov/11268710/)). A 1993 randomised, double-blind trial in chronic heart failure with hypoxaemia ([PMID 8088931](https://pubmed.ncbi.nlm.nih.gov/8088931/)) compared methylxanthines in 48 patients. Because it does not establish that doxofylline treats heart disease, it does not support this indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

