---
layout: default
title: Vilazodone
parent: Model Prediction Only (L5)
nav_order: 888
evidence_level: L5
indication_count: 7
monitor_inn: "Vilazodone"
predicted_indications: ["neurotic disorder", "obsessive-compulsive disorder", "agoraphobia", "benign paroxysmal torticollis of infancy", "Keppen-Lubinsky syndrome", "Ohdo syndrome and variants", "histrionic personality disorder (disease)"]
last_modified_at: 2026-10-31
description: "Vilazodone: predicted new indication Neurotic disorder (evidence level L5). Approved use: Unipolar depression, endogenous depression, major depressive disorder…"
---

# Vilazodone
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

## Vilazodone: From Depression and Anxiety Disorders to Neurotic Disorder
{: .text-alpha }

## One-Sentence Summary

Vilazodone is an antidepressant.
The TxGNN model predicts it may be effective for **neurotic disorder**, but **no clinical trials and no publications** directly study this disease, so the prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unipolar depression, endogenous depression, major depressive disorder, anxiety disorder (relations recorded in the knowledge graph; the local licence records contain no approved-indication text) |
| Predicted New Indication | Neurotic disorder |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, vilazodone is an antidepressant used in depression and anxiety disorders, and mechanistically it may be applicable to neurotic disorder. Any mechanistic description beyond this is not supported by the supplied data.

Neurotic disorder is a broad, legacy diagnostic category. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

No trials or publications were found for neurotic disorder, so this rationale remains a hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for neurotic disorder.

For context, other predicted indications have limited literature. For obsessive-compulsive disorder (rank 2, score 0.9972), three general reviews were retrieved. None appears to be a vilazodone-specific study:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Review | Expert Opin Pharmacother | Review of double-blind studies of serotonergic antidepressants in OCD |
| [40955264](https://pubmed.ncbi.nlm.nih.gov/40955264/) | 2025 | Review | Cureus | Management of antidepressant-induced sexual dysfunction |
| [26472602](https://pubmed.ncbi.nlm.nih.gov/26472602/) | 2016 | Review | Ann Pharm Fr | Historical and current psychopharmacology of anxiety and depression |

---

## India Market Information

At least 20 valid single-ingredient licences were found; the list may be partial. The records contain no approved-indication text. Five examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 233856 | Vilano 40 Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not stated in the records |
| 233519 | Vilano 20 Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not stated in the records |
| 233655 | Vilazine 20 Tablet (Intas Pharmaceuticals Ltd) | Strip of 10 tablets | Not stated in the records |
| 233825 | Vilarest 20 Tablet (Cipla Ltd) | Strip of 10 tablets | Not stated in the records |
| 233783 | Vilodon 20 Tablet (MSN Laboratories) | Strip of 10 tablets | Not stated in the records |

---

## Safety Considerations

- **Relations recorded in the knowledge graph as contraindications (not label text):** epilepsy, bipolar disorder, major affective disorder, blood coagulation disease, neuroleptic malignant syndrome, inappropriate ADH syndrome, nephrogenic syndrome of inappropriate antidiuresis, serotonin syndrome.
- **Drug Interactions:** 171 interactions were recorded. Major-level examples include bupropion, lorcaserin, clarithromycin, diethylpropion, dolasetron, palonosetron and phentermine. Moderate-level examples include pioglitazone, aprepitant, morphine, acetylsalicylic acid, dexamethasone, glimepiride and several insulins.

Package insert warnings and contraindications were not available; please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for neurotic disorder has a high model score but no supporting trials or publications, so it stays at evidence level L5. The category is broad and overlaps with conditions already linked to vilazodone, so the score may reflect ontology proximity rather than new evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator's records
- Mechanism of action data (e.g. from DrugBank)
- Clinical trials or publications that directly study vilazodone in neurotic disorder, or in more specific conditions within it
- Clarification of the approved indications from licence or label text
- A review of the major drug interactions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

