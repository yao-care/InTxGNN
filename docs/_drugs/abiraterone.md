---
layout: default
title: Abiraterone
parent: Model Prediction Only (L5)
nav_order: 14
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Abiraterone: predicted new indication Migraine disorder (evidence level L5). Approved use: Not recorded in the compiled license data"
---

# Abiraterone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Abiraterone: From Prostate Cancer (Not Recorded in License Data) to Migraine Disorder

## One-Sentence Summary

Abiraterone is an oral drug marketed in India under 20 valid registrations. The license data compiled for this report does not record an approved indication. The TxGNN model predicts it may be effective for **migraine disorder**, but **no clinical trials and no relevant publications** currently support this prediction. It is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the compiled license data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 98.81% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, abiraterone inhibits CYP17A1 and suppresses the synthesis of androgens and cortisol precursors. Its clinical use is in prostate cancer, where it is co-administered with prednisone. The retrieved publications about it are all prostate cancer studies.

The link between this mechanism and migraine is speculative. Hormonal modulation could theoretically influence migraine, but no mechanistic or clinical evidence has been established. The high score (0.988) most likely reflects proximity in the knowledge graph, not a demonstrated pharmacological rationale.

The other top predictions are also unsupported:

- **Migraine-related terms** (susceptibility phenotype, brainstem aura): these appear to be redundant ontology neighbours of the main migraine prediction.
- **Pulmonary hypertension:** this has only a loose theoretical link through sex-hormone signalling. The five retrieved publications are all about prostate cancer and are not relevant evidence. Abiraterone's mineralocorticoid excess can cause fluid retention and hypertension, which is a safety concern.
- **Rheumatoid arthritis:** the anti-inflammatory effect comes from co-administered prednisone, not abiraterone, and androgen suppression could be unfavourable.
- **Leprosy, nephrogenic syndrome of inappropriate antidiuresis, kyphoscoliotic heart disease, atrophoderma vermiculata, ulerythema ophryogenesis:** no plausible mechanism or evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for migraine disorder.

## India Market Information

There are 20 valid single-ingredient registrations, with no combination products and no cancelled registrations. The compiled data contains no approved indication text. Five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2882 | Ahabir Tablet (Hetero Drugs Ltd) | Bottle of 120 tablets | Not recorded |
| 8568 | Abtmed 250mg Tablet (Medicamen Biotech Ltd) | Bottle of 30 tablets | Not recorded |
| 246845 | Zelgor 500mg Tablet (Sun Pharmaceutical Industries Ltd) | Bottle of 60 tablets | Not recorded |
| 20160 | Abstet Tablet (Biocon) | Strip of 30 tablets | Not recorded |
| 247367 | Zabpro 500mg Tablet (Ipca Laboratories Ltd) | Bottle of 60 tablets | Not recorded |

All products are oral tablets.

## Cytotoxicity

Abiraterone is used as an anticancer hormonal therapy for prostate cancer. It is a CYP17A1 inhibitor, not a conventional cytotoxic chemotherapy.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted hormonal therapy (CYP17A1 inhibitor), not conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; liver function, blood pressure, fluid status and potassium are commonly monitored |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions:** The interaction screen returned 100 interacting drugs. The first 20 returned include:
  - **Major:** cisapride, dolasetron, eliglustat, loperamide
  - **Moderate:** bisacodyl, castor oil, clarithromycin, dexfenfluramine, eluxadoline, famotidine, fenfluramine, glycerin, granisetron, lactitol, lactulose, levofloxacin, magnesium citrate, magnesium hydroxide, metoclopramide
  - **Minor:** metronidazole
- **Other concerns noted during evaluation:** Mineralocorticoid excess may cause fluid retention and hypertension. This is relevant to the cardiopulmonary predictions (pulmonary hypertension, kyphoscoliotic heart disease).

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predictions are model outputs only (L5), with no clinical trials and no relevant literature. The mechanistic link to migraine is speculative, and the safety data needed for screening is incomplete.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently blocking safety screening)
- Approved indication text and mechanism of action data
- Preclinical or mechanistic evidence linking CYP17A1 inhibition or hormonal modulation to migraine
- A targeted literature search specific to migraine, since the retrieved publications are all prostate cancer studies
- Assessment of route compatibility and the cardiovascular risk of mineralocorticoid excess in the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

