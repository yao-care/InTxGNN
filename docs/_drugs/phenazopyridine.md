---
layout: default
title: Phenazopyridine
parent: Model Prediction Only (L5)
nav_order: 660
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Phenazopyridine: predicted new indication Bronchitis (evidence level L5). Approved use: Not stated in the registration records compiled for this report"
monitor_inn: "Phenazopyridine"
predicted_indications: ["bronchitis"]
---

# Phenazopyridine
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

## Phenazopyridine: From Urinary Tract Symptom Relief to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Phenazopyridine is an oral urinary tract analgesic that is marketed in India under 2 valid registrations.
The TxGNN model predicts it may be effective for **bronchitis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records compiled for this report |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9923 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (2 of 2) – CDSCO approval status is not included in this data |
| Number of Listed Products | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Phenazopyridine is generally understood as a urinary tract analgesic that acts locally on the urothelium, but its exact mechanism is not well characterized.

A credible mechanistic link to bronchitis has not been established. The drug has no known anti-inflammatory, antimicrobial, mucolytic or bronchodilatory activity relevant to bronchial disease, and its original use (symptomatic relief of urinary tract discomfort) is unrelated to respiratory illness.

The high score (0.9923) is a TxGNN model (deep learning) prediction only. It may reflect network-structure artifacts, such as shared neighbours with other drugs or genes, rather than a true biological relationship. No clinical or preclinical data in the compiled dataset support the prediction.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 177628 | Phenodyne 100mg Tablet | Strip of 10 tablets | Not stated |
| 173624 | Pyridium 200 Tablet | Strip of 10 tablets | Not stated |

Both registrations are valid single-ingredient oral products (manufacturers: Remedial Healthcare; A. Menarini India Pvt Ltd).

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these are model-derived drug–disease links, not label text): hypertension, liver failure and liver disease, kidney disease, inherited porphyria, COPD, hematologic disease (thrombocytopenia, neutropenia, agranulocytosis, anemia), hepatic encephalopathy, benign prostatic hyperplasia, coronary artery disease, sleep apnea syndromes, anxiety and related disorders, and substance abuse/dependence. Several of these (COPD, sleep apnea, hypoventilation syndromes) are relevant to a respiratory population.
- **Additional concerns:** methemoglobinemia, hemolysis in G6PD deficiency and renal impairment are known risks that would weigh against use in a respiratory population without clear justification.
- **Drug interactions:** 24 interactions were identified in total. The two **Major** ones are **leflunomide** and **nitrous acid**. Most of the remaining are Moderate, including naltrexone, methotrexate, topical/ophthalmic local anaesthetics (lidocaine, benzocaine, tetracaine, oxybuprocaine, cinchocaine), cocaine, asparaginase, pegaspargase, brentuximab vedotin, clofarabine, idelalisib and interferon beta-1a/1b.

Package insert warnings and contraindications were not available for this report; please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or literature, no established mechanistic link, and the safety profile adds concerns for respiratory patients. The evidence level is L5.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indication text for the Indian products
- Mechanism of action data (e.g. from DrugBank) and an assessment of any plausible link to bronchial disease
- Preclinical or observational evidence showing any benefit in bronchitis
- Review of route and formulation compatibility for a respiratory indication
- A safety assessment covering methemoglobinemia, hemolysis and renal/hepatic risks in the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

