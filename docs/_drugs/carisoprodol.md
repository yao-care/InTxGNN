---
layout: default
title: Carisoprodol
parent: Model Prediction Only (L5)
nav_order: 149
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Carisoprodol: predicted new indication Insomnia (evidence level L5). Approved use: Not stated in the India license data (carisoprodol is generally known…"
monitor_inn: "Carisoprodol"
predicted_indications: ["insomnia (disease)"]
---

# Carisoprodol
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

# Carisoprodol: From Muscle Relaxation to Insomnia

## One-Sentence Summary

Carisoprodol is a centrally acting skeletal muscle relaxant that is marketed in India as single-ingredient tablets.
The TxGNN model predicts it may be effective for **insomnia**,
but there are currently **no registered clinical trials** and only **1 loosely related publication** supporting this direction, so the prediction rests almost entirely on computation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India license data (carisoprodol is generally known as a skeletal muscle relaxant) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, carisoprodol is a centrally acting muscle relaxant. Its active metabolite, meprobamate, modulates GABA-A receptors and has sedative and anxiolytic properties.

This sedative profile could plausibly be relevant to insomnia. However, this is background pharmacology and is not supported by the evidence compiled here. The high TxGNN score (99.02%) is a computational prediction only and does not confirm clinical benefit.

Safety is also a concern for this use. Carisoprodol has abuse and dependence potential, and it has 158 recorded drug interactions, many involving CNS depressants that are commonly co-prescribed to people with insomnia.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22963024](https://pubmed.ncbi.nlm.nih.gov/22963024/) | 2012 | Review | American Family Physician | Review of nocturnal leg cramps, which can cause severe insomnia. It does not directly evaluate carisoprodol for insomnia. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 7469 | Aciprodol 350mg Tablet | Strip of 10 tablets | Not stated |
| Registration No. 34745 | Carisoma Compound Tablet | Strip of 10 tablets | Not stated |
| Registration No. 35669 | Carisoma 350mg Tablet | Strip of 10 tablets | Not stated |
| Registration No. 38228 | Carisol 350mg Tablet | Strip of 10 tablets | Not stated |
| Registration No. 117195 | Korisuma Tablet | Strip of 10 tablets | Not stated |

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: The TxGNN knowledge graph links carisoprodol to contraindications in many conditions, including:
  - Epilepsy
  - Kidney disease and liver disease
  - Respiratory failure
  - Substance abuse/dependence
  - Adrenal insufficiency (including Addison disease)
  - Hypothyroidism
  - Sudden cardiac arrest and heart conduction disease
  - Thrombocytopenia, hemophilia and anemia
  - Peptic ulcer disease and inflammatory bowel disease
  - Gout
  - Hypotensive disorder
  - Benign prostatic hyperplasia
- **Drug Interactions**: 158 interactions are recorded. The main ones are:
  - **Major**: Morphine (including liposomal morphine)
  - **Moderate**: Dronabinol, nabilone, metoclopramide, opium, sibutramine, difenoxin and diphenoxylate

  Combining carisoprodol with opioids and other CNS depressants raises concern for additive sedation and respiratory depression.

Please refer to the package insert for full safety information, as label-based warnings were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a computational score (Evidence Level L5). There are no clinical trials, and the single publication found does not evaluate carisoprodol for insomnia. Abuse and dependence potential and the many CNS-depressant interactions add substantial safety concerns for a chronic sleep indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source, since this is a blocking gap for safety screening
- Mechanism of action data (for example, from DrugBank) to support a mechanistic link to insomnia
- Clinical or observational evidence on carisoprodol or meprobamate for insomnia
- A risk assessment for abuse, dependence and co-prescribed CNS depressants in the insomnia population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

