---
layout: default
title: Darunavir
parent: Model Prediction Only (L5)
nav_order: 234
evidence_level: L5
indication_count: 4
monitor_inn: "Darunavir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-10-30
description: "Darunavir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease"
---

# Darunavir
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

## Darunavir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Darunavir is an HIV protease inhibitor whose original uses, as recorded in the knowledge graph, are HIV infectious disease and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, a veterinary condition.
There are **0 clinical trials** and **0 publications** directly studying this disease, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (relation recorded in the knowledge graph; the licence records compiled for this report contain no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (8 of 8) – CDSCO approval status is not included in this data |
| Number of Listed Products | 8 (valid: 8) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, darunavir belongs to the HIV protease inhibitor class. Its use against HIV and AIDS is recorded in the knowledge graph, and mechanistically it may be applicable to related lentiviral diseases.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV-1, so a conceptual rationale for protease inhibition exists. However, FIV protease differs from HIV-1 protease in substrate specificity and inhibitor sensitivity. No data compiled for this report show darunavir activity against FIV protease.

The high TxGNN score is a model prediction only. This is also a veterinary indication and is not directly relevant to human drug repurposing.

Other predictions in the list are weaker:
- **Simian immunodeficiency virus (SIV) infection** (score 0.9997) has four publications, all nonhuman primate studies of combination antiretroviral therapy. These are indirect: they concern SIV rather than feline disease, and darunavir's contribution cannot be isolated from the combinations. Under the evidence rules, no cited study directly addresses the top-ranked disease, so it stays at L5.
- **A rare neurodevelopmental disorder with ataxic gait** (score 0.9997) has no plausible mechanistic link and likely reflects network-proximity artefacts.
- **Obsolete familial combined hyperlipidemia** (score 0.9919) has only an adverse-effect link, since protease inhibitors can cause dyslipidemia. The disease term is obsolete in the ontology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for feline acquired immunodeficiency syndrome.

For the related prediction, simian immunodeficiency virus infection, the following nonhuman primate studies were found. They are indirect evidence and do not study the predicted disease:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Preclinical (nonhuman primate) | PloS one | Suppressive combination antiretroviral therapy plus the histone deacetylase inhibitor SAHA in SIV-infected Chinese rhesus macaques, as a model of the viral reservoir |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Preclinical (nonhuman primate) | AIDS Res Hum Retroviruses | Comparison of two coformulated injectable combination antiretroviral regimens in SIV-infected rhesus macaques |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Preclinical (nonhuman primate) | AIDS | Auranofin restricted the viral reservoir in the monkey AIDS model and contained viral load after ART suspension |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Preclinical (nonhuman primate) | PLoS Pathogens | A highly intensified ART regimen induced long-term viral suppression and restricted the viral reservoir in a simian AIDS model |

The supplied abstracts are truncated, so whether darunavir is part of these regimens should be verified.

---

## India Market Information

At least the following authorisations are recorded (8 single-ingredient licences, all valid, none cancelled). The licence records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 63782 | Danavir 600 Tablet | Bottle of 60 tablets | Not stated in licence record |
| Registration No. 66955 | Danavir 300mg Tablet | Bottle of 30 tablets | Not stated in licence record |
| Registration No. 236379 | Virem 600mg Tablet | Bottle of 60 tablets | Not stated in licence record |
| Registration No. 238628 | Virem 300mg Tablet | Bottle of 120 tablets | Not stated in licence record |
| Registration No. 59933 | Daruvir 600mg Tablet | Bottle of 60 tablets | Not stated in licence record |

All products are oral tablets.

---

## Safety Considerations

- **Contraindications recorded in the knowledge graph (not label text):** liver failure, liver disease, cirrhosis of liver, gallbladder disease, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, chronic hepatitis B virus infection, hepatitis C virus infection (acute and chronic), hypertriglyceridemia, hemophilia, and symptomatic hemophilia in female carriers.
- **Drug interactions:** 209 interactions were identified. Most of those listed are Moderate, including:
  - antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, saxagliptin, canagliflozin, dapagliflozin, chlorpropamide, acetohexamide, albiglutide)
  - corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone)
  - aprepitant and clarithromycin
  
  **Cisapride is a Major interaction.**
- **Metabolic note:** protease inhibitors are associated with dyslipidemia and glucose disturbance. This matters particularly for the hyperlipidemia prediction.

Package insert warnings and contraindications were not available for this report; please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for feline acquired immunodeficiency syndrome is supported only by a model score, with no directly relevant trials or publications (L5). It is also a veterinary indication. The related SIV literature is indirect and preclinical.

**To proceed, the following is needed:**
- Mechanism of action data for darunavir
- Evidence of darunavir activity against FIV protease (in vitro enzyme or cell assays)
- Package insert warnings and contraindications from the Indian regulator, which are currently missing and block safety screening
- Verification of the regimen composition in the SIV studies, to see whether darunavir was actually used
- Confirmation of whether a veterinary indication falls within the scope of this repurposing programme
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

