---
layout: default
title: Haloperidol
parent: Model Prediction Only (L5)
nav_order: 406
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Haloperidol"
predicted_indications: ["congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited", "syndromic myopia", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "atypical glycine encephalopathy"]
description: "Haloperidol: predicted new indication Congenital disorder of glycosylation with defective fucosylation (evidence level L5). In India: at least 20 listed products"
---

# Haloperidol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Haloperidol: Congenital disorder of glycosylation with defective fucosylation
{: .text-alpha }

## One-Sentence Summary

Haloperidol is a dopamine D2-blocking antipsychotic, originally used for psychotic disorders, schizophrenia and Tourette syndrome.
The TxGNN model predicts it may be effective for **congenital disorder of glycosylation with defective fucosylation**,
but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Congenital disorder of glycosylation with defective fucosylation |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for haloperidol: "The mechanism of action of haloperidol decanoate for the treatment of schizophrenia in adults is unclear. However, its effect in schizophrenia could be mediated through its activity as an antagonist at central dopamine type 2 receptors." ([DailyMed: haloperidol decanoate prescribing information, BluePoint Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3d011250-a517-4c27-8ce3-d59d441ea61c), label version 2026-11-03; accessed 2026-11-19.) Haloperidol is generally understood as a high-affinity dopamine D2 receptor antagonist, and its efficacy in psychotic disorders is well established.

No plausible mechanistic link could be identified between D2 antagonism and defective fucosylation, a congenital metabolic disorder of protein glycosylation. The high score (0.9991) is a model output only. Haloperidol could at most offer symptomatic help for neuropsychiatric features, which would not be disease-modifying. This prediction should therefore be treated as a hypothesis with no supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Haloperidol has 20 valid single-ingredient registrations in India, all oral tablets. The records compiled for this report do not include approved indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 2760 | Agidol Plus 1.5mg Tablet | Strip of 10 tablets | Valid |
| 13755 | Agidol 3 Tablet | Strip of 10 tablets | Valid |
| 30375 | Bondol 5mg Tablet | Strip of 10 tablets | Valid |
| 30750 | Benzydol 5 mg/2 mg Tablet | Strip of 10 tablets | Valid |
| 70174 | Dolcin 1.5mg Tablet | Strip of 10 tablets | Valid |
| 104792 | Hexidol Plus 5 mg/2 mg Tablet | Strip of 10 tablets | Valid |
| 104799 | Halo 10mg Tablet | Strip of 10 tablets | Valid |
| 104898 | Hypnodol 5mg Tablet | Strip of 10 tablets | Valid |
| 105789 | Halodias DT 0.25 Tablet | Strip of 10 tablet dt | Valid |
| 106385 | Halodyl 1.5mg Tablet | Strip of 10 tablets | Valid |
| 106480 | Helinase 1.5mg Tablet | Strip of 10 tablets | Valid |
| 106516 | Halopace 5mg Tablet | Strip of 10 tablets | Valid |
| 106941 | Halpido 5 Tablet | Strip of 10 tablets | Valid |
| 140751 | Mindol Plus 5mg/2mg Tablet | Strip of 10 tablets | Valid |
| 142809 | Mindwel 5mg Tablet | Strip of 10 tablets | Valid |
| 142907 | Mindol 5mg Tablet | Strip of 10 tablets | Valid |
| 217511 | Talendol 0.25mg Tablet | Strip of 10 tablets | Valid |
| 219523 | Typidol 5mg Tablet | Strip of 10 tablets | Valid |
| 224993 | Trikonace 0.25mg Tablet | Strip of 10 tablets | Valid |
| 242596 | Worin 10mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Contraindication-related conditions** (drug-disease associations compiled for this report, not label text):
  - Cardiac and neurological: long QT syndrome (including familial), torsades de pointes, epilepsy, basal ganglia disease, neuroleptic malignant syndrome.
  - Haematological: neutropenia, leukopenia, agranulocytosis and congenital neutropenia syndromes.
  - Metabolic and other: liver disease, gallbladder disease, hypothyroidism, potassium deficiency, hypotensive disorder, female breast carcinoma.
- **Drug Interactions**: 303 interactions were recorded. Major-level examples include bupropion, morphine, clarithromycin and dolasetron. Moderate-level examples include famotidine, epinephrine, hydrocortisone, amphotericin B and several anticholinergics.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score, with no clinical trials, no literature and no plausible mechanistic link to haloperidol's D2 antagonism. The patient group is also vulnerable, and haloperidol carries QT, extrapyramidal and haematological risks, so there is no basis to proceed.

**To proceed, the following is needed:**
- Mechanistic or preclinical evidence linking haloperidol to the fucosylation pathway
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications from the Indian regulator
- A safety plan covering QT prolongation, extrapyramidal symptoms and the high interaction burden

It has completed Phase 3 trials (for example NCT00129220, a haloperidol-controlled olanzapine trial) and network meta-analyses (2022, 2025), and carries an L1 rating and a "Proceed with Guardrails" recommendation. It is closer to established clinical use than to novel repurposing. It would be a more productive candidate for evaluation than the prediction in this report.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: haloperidol decanoate prescribing information, BluePoint Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3d011250-a517-4c27-8ce3-d59d441ea61c) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

