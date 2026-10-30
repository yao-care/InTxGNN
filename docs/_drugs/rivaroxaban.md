---
layout: default
title: Rivaroxaban
parent: Model Prediction Only (L5)
nav_order: 747
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
description: "Rivaroxaban: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not available"
monitor_inn: "Rivaroxaban"
predicted_indications: ["rheumatoid arthritis", "gout", "HIV infectious disease", "brachydactyly-syndactyly syndrome"]
---

# Rivaroxaban
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

## Rivaroxaban: From Thromboembolic Disease to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Rivaroxaban is an oral Factor Xa inhibitor (anticoagulant) that is widely marketed in India; the data compiled for this report do not list its approved indication text.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but **no clinical trials** and **no publications testing rivaroxaban in this disease** currently support the prediction.
The evidence is model-prediction only and should be treated as a hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (approved indication text is blank in all registrations) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9957 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, rivaroxaban belongs to the direct oral anticoagulant class that inhibits Factor Xa, and it is used to prevent and treat thrombosis. Mechanistically, it may be applicable to rheumatoid arthritis, but only at the hypothesis level.

A plausible biological rationale exists. Inflammation and autoimmunity are linked to a hypercoagulable state, and Factor Xa and thrombin signalling (for example via PAR-1/PAR-2) may contribute to synovial inflammation. Rheumatoid arthritis also carries an elevated risk of venous thromboembolism, so anticoagulants may be used in these patients for thrombosis. That is a different question from whether the drug modifies the disease itself.

The TxGNN score is very high, but the retrieved literature does not test rivaroxaban in rheumatoid arthritis. The prediction should not be read as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Review of diagnosis and treatment of lower extremity venous thromboembolism; background on thrombosis, not rheumatoid arthritis |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | La Revue de medecine interne | Thrombin generation assay in autoimmune disease; conceptually relevant to the rationale, but not evidence of efficacy |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PloS one | Adherence to rivaroxaban versus apixaban in non-valvular atrial fibrillation; not related to rheumatoid arthritis |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Case report | Cureus | Perioperative thromboembolic cerebral infarction in an 88-year-old woman with atrial fibrillation on anticoagulation, who also had rheumatoid arthritis and took oral steroids |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 185549 | Rivoxamac 15mg Tablet | Strip of 10 tablets | Not stated |
| 185361 | Rivared 15mg Tablet | Strip of 10 tablets | Not stated |
| 243926 | Xarelto 20mg Tablet | Box of 98 tablets | Not stated |
| 155933 | Nanotril 10mg Tablet | Strip of 10 tablets | Not stated |
| 185545 | Rivalto 20mg Tablet | Strip of 14 tablets | Not stated |

The data list 20 valid single-ingredient registrations in total; the five above are shown as examples.

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: liver failure, kidney disease, pyoureter, liver disease, gallbladder disease, blood coagulation disease.
- **Drug Interactions**: 313 interactions were identified. Major-level interactions include:
  - Acetylsalicylic acid
  - Cobicistat
  - Deferasirox
  - Ibritumomab tiuxetan
  - Tositumomab (I-131)

  Moderate-level examples include aprepitant, dexamethasone, cimetidine, clarithromycin, eliglustat, miconazole, clotrimazole and sugammadex.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no clinical trials and no literature testing rivaroxaban in rheumatoid arthritis. The biological rationale is hypothesis-level only, so the evidence is L5.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications for the India registrations
- Detailed mechanism of action data
- Preclinical or mechanistic studies of Factor Xa/thrombin signalling in synovial inflammation
- Evidence of disease-modifying benefit, beyond thrombosis prevention, in rheumatoid arthritis
- A bleeding-risk assessment for the target population, including concomitant steroids, NSAIDs and aspirin

---

## Other Predicted Indications (for reference)

The same analysis also produced the following lower-priority predictions. None is supported by direct efficacy evidence, and all are currently **Hold**.

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Gout | 0.9951 | L5 | No trials; the retrieved papers cover a benzbromarone–CYP interaction and a varicose vein case, neither supporting efficacy |
| HIV infectious disease | 0.9917 | L4 | One Phase 2 trial (NCT00786422) is a DVT/PE study with a CYP3A4 inducer and not an HIV trial; the literature addresses safe co-administration and bleeding risk with antiretrovirals, not treatment of HIV |
| Brachydactyly-syndactyly syndrome | 0.9910 | L5 | No trials or literature; no plausible mechanistic link |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

