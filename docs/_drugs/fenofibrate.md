---
layout: default
title: Fenofibrate
parent: Model Prediction Only (L5)
nav_order: 344
evidence_level: L5
indication_count: 1
monitor_inn: "Fenofibrate"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-30
description: "Fenofibrate: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Hypertriglyceridemia and related hyperlipidaemias"
---

# Fenofibrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Fenofibrate: From Hypertriglyceridemia to Cholesterol-Ester Transfer Protein Deficiency
{: .text-alpha }

## One-Sentence Summary

Fenofibrate is a lipid-lowering drug whose recorded uses in the knowledge graph centre on hypertriglyceridemia and other hyperlipidaemias.
The TxGNN model predicts it may be effective for **cholesterol-ester transfer protein (CETP) deficiency**, but there are **0 clinical trials** and only **3 publications** (all preclinical or mechanistic, none directly studying this disease), so the evidence is model-driven.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertriglyceridemia and related hyperlipidaemias (relations recorded in the knowledge graph; the licence records compiled for this report contain no indication text) |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | At least 20 licences (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, fenofibrate is a PPAR-alpha agonist that lowers triglycerides and raises HDL cholesterol, partly by increasing expression of apolipoprotein A-I/A-II and phospholipid transfer protein (PLTP).

CETP deficiency is a condition of markedly elevated HDL cholesterol with impaired cholesteryl ester transfer. The link to fenofibrate is indirect: PPAR-alpha agonism acts on the same lipoprotein remodelling pathway (for example, HDL enlargement through PLTP induction in mice). Preclinical work combining CETP inhibition with PPAR-alpha agonism shows additive HDL-raising effects.

However, CETP deficiency is already a high-HDL state, so raising HDL further is not an evident therapeutic goal, and the clinical rationale for treating it with fenofibrate is unclear. The high score most likely reflects network proximity of lipid-metabolism genes (PPARA, CETP, PLTP) rather than a defined therapeutic need.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20332533](https://pubmed.ncbi.nlm.nih.gov/20332533/) | 2010 | Preclinical | J Cardiovasc Pharmacol Ther | In human ApoB100/CETP transgenic mice, CETP inhibition (torcetrapib) and PPAR-alpha agonism (fenofibrate) raised HDL cholesterol and lowered LDL cholesterol |
| [11342537](https://pubmed.ncbi.nlm.nih.gov/11342537/) | 2001 | Mechanistic | J Biol Chem | Fenofibrate induced the PLTP gene, accounting for HDL enlargement in treated mice |
| [30271349](https://pubmed.ncbi.nlm.nih.gov/30271349/) | 2018 | Mechanistic/cohort-type | Front Physiol | Plasma HDL did not correlate with fecal cholesterol or cholesterol efflux capacity, suggesting HDL function matters more than HDL level |

Currently no clinical trials are registered for this prediction.

## India Market Information

At least 20 licences were found (the list may be partial). All 20 listed are valid. None of the records include approved-indication text, and the product names suggest they are mostly fixed-dose combinations with a statin, so they should not be taken as describing fenofibrate alone. Five examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 228618 | Thunor F 75mg/10mg Tablet | Strip of 10 tablets | Not stated in records |
| 185695 | Rosovas F 160mg/10mg Tablet | Strip of 10 tablets | Not stated in records |
| 120868 | Lipicard 160 Tablet | Strip of 10 tablets | Not stated in records |
| 104604 | Hivast F 145mg/10mg Tablet | Strip of 10 tablets | Not stated in records |
| 85904 | Finabate 145mg Tablet | Strip of 10 tablets | Not stated in records |

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** contraindication links include liver failure and liver disease, pancreatitis, gallbladder disease and cholelithiasis, thrombocytopenia, myopathy and rhabdomyolysis, impaired renal function, anaemia, and leukopenia and neutropenia (including several congenital neutropenia syndromes).
- **Drug Interactions:** 199 interactions were recorded. The listed ones are all moderate, and include sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), many insulin products, chenodeoxycholic acid, and esomeprazole.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication directly studies fenofibrate in CETP deficiency; the three cited papers are preclinical or mechanistic. The high TxGNN score appears to reflect gene-network proximity, and since the condition already involves high HDL, a therapeutic need is not apparent.

**To proceed, the following is needed:**
- A clear clinical rationale showing a treatment goal in CETP deficiency
- Mechanism of action data for fenofibrate
- Package insert warnings and contraindications from the India licence holders
- Clinical or human data directly in CETP-deficient patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

