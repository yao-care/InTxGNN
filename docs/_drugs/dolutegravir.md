---
layout: default
title: Dolutegravir
parent: Model Prediction Only (L5)
nav_order: 281
evidence_level: L5
indication_count: 3
monitor_inn: "Dolutegravir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-30
description: "Dolutegravir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease, AIDS"
---

# Dolutegravir
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

## Dolutegravir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Dolutegravir is an HIV integrase inhibitor, originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV)**, but this is a veterinary indication.
There are **0 clinical trials** and **1 publication** (a preclinical study of a combination regimen in cats), so the evidence is model prediction only for this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease, AIDS (relations recorded in the knowledge graph; the local licence records contain no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (4 of 4) – CDSCO approval status is not included in this data |
| Number of Listed Products | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, dolutegravir belongs to the integrase strand transfer inhibitor class. Its activity in HIV infection is recorded in the knowledge graph, and mechanistically it may be applicable to related lentiviral infections.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV and has its own integrase enzyme, so inhibition is biologically plausible. However, the one retrieved publication tested a three-drug combination (dolutegravir, tenofovir, emtricitabine) in FIV-infected cats. It does not show what dolutegravir alone contributes. The very high TxGNN score is a computational prediction and probably reflects similarity to HIV.

FIV is also an animal disease, so human clinical development pathways do not apply. The evidence level is L5 because no cited study establishes dolutegravir-specific efficacy against this disease.

Two other predictions were also generated:
- **Simian immunodeficiency virus infection** (score 0.9985): macaque studies, including dolutegravir monotherapy in SIV-infected macaques, support a shared integrase target. This is a research and model-system use, not a human therapeutic indication.
- **A rare neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 0.9980): no mechanistic link, trials or literature were found. This is probably a TxGNN model (deep learning) artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Preclinical/veterinary study | Viruses | Evaluated pharmacokinetics and clinical outcomes of combination antiretroviral therapy (dolutegravir, tenofovir, emtricitabine) in FIV-infected domestic cats; no definitive therapy currently exists for FIV |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 233352 | Viropil Tablet | Bottle of 30 tablets | Not stated in the records |
| Registration No. 199998 | Spegra Tablet | Bottle of 30 tablets | Not stated in the records |
| Registration No. 107978 | Instgra Tablet | Bottle of 30 tablets | Not stated in the records |
| Registration No. 35654 | Cipanec 50mg/300mg/300mg Tablet | Bottle of 30 tablets | Not stated in the records |

## Safety Considerations

**Drug Interactions**: 62 interactions are recorded. Examples include:
- **Major**: aluminium hydroxide, attapulgite, kaolin, magaldrate, iron, and multiple calcium salts (acetate, carbonate, citrate, glubionate, gluconate, lactate, phosphate) and magnesium salts (carbonate, chloride, citrate). These are mostly polyvalent cation products that can bind dolutegravir and reduce absorption.
- **Minor**: aprepitant, cimetidine, clarithromycin, clotrimazole, dexamethasone.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only evidence for feline AIDS is a single veterinary study of a combination regimen, which cannot isolate dolutegravir's effect. The high TxGNN score is a prediction only, and FIV is not a human indication.

**To proceed, the following is needed:**
- Dolutegravir-specific efficacy data in FIV-infected animals
- Mechanism of action data
- Package insert warnings and contraindications from the Indian regulatory source
- A decision on whether the goal is veterinary development or use as a research model, since neither is a human therapeutic pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

