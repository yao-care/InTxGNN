---
layout: default
title: Ranolazine
parent: Model Prediction Only (L5)
nav_order: 727
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Ranolazine: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not stated in the Indian license records"
monitor_inn: "Ranolazine"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ranolazine
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

## Ranolazine: From Chronic Angina to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Ranolazine is an anti-anginal drug that is widely marketed in India as a single-ingredient product. The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but the prediction is computational only: **0 clinical trials** and **0 publications** currently support it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Indian license records (approved indication text is empty for all registrations) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ranolazine is generally known as a late sodium current (INaLate) inhibitor used for angina, but this could not be confirmed from the compiled data, and its efficacy in the original indication is not documented here.

NSIAD is a rare disorder caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2). These mutations cause water retention and low blood sodium (hyponatremia) even though vasopressin levels are not elevated. No direct pathway linking late sodium current inhibition to V2 receptor signalling or renal water handling has been established.

The very high TxGNN score (0.996) therefore comes from knowledge-graph link prediction, probably through shared network neighbours such as ion-transport or channel-related genes. It is not a validated mechanism. The prediction should be treated as a hypothesis only.

## Safety Considerations

- **Knowledge-graph contraindication signals** (derived from drug-disease edges in the knowledge graph, not from label text): long QT syndrome, familial long QT syndrome, torsades de pointes, kidney disease, pyoureter, cirrhosis of liver.
- **Drug Interactions**: 233 interactions were recorded. Major-level interactions among those listed include:
  - Aprepitant
  - Dexamethasone
  - Clarithromycin
  - Dolasetron
  - Eliglustat

  Moderate-level examples include famotidine, metformin, loperamide, canagliflozin, dapagliflozin and empagliflozin. Interactions likely involve CYP3A4/P-gp pathways and QT prolongation, and would need careful assessment in a hyponatremic population.

Please refer to the package insert for label warnings and contraindications, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on model output (Evidence Level L5), with no clinical trials or literature, no established mechanistic link to V2 receptor biology, and safety signals (QT-related and renal contraindications) that are relevant to the target population.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian licences (currently blocking safety screening)
- Confirmed mechanism of action data, and a plausible mechanistic link to AVPR2 or renal water handling
- Preclinical or in vitro evidence testing ranolazine in NSIAD-relevant models
- A literature and clinical trial search for any supporting evidence
- A pharmacokinetic and QT-risk assessment in patients with hyponatremia or renal impairment
- Assessment of route compatibility (oral extended-release tablets are the only forms marketed)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

