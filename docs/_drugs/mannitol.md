---
layout: default
title: Mannitol
parent: Model Prediction Only (L5)
nav_order: 514
evidence_level: L5
indication_count: 9
monitor_inn: "Mannitol"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "acute pulmonary heart disease", "exercise-induced malignant hyperthermia", "familial periodic paralysis", "hypokalemic periodic paralysis", "congenital multicore myopathy with external ophthalmoplegia", "moderate multiminicore disease with hand involvement", "nephrogenic diabetes insipidus", "central core myopathy"]
last_modified_at: 2026-10-23
description: "Mannitol: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Relations recorded in the knowledge graph (not label text): congestiv…"
---

# Mannitol
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

## Mannitol: From Intracranial Pressure and Edema Control to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Mannitol is an osmotic agent given by infusion.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis**, but there are **0 clinical trials** and only **1 general review** that does not address mannitol treatment, so the evidence is model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relations recorded in the knowledge graph (not label text): congestive heart failure, brain edema, ocular hypertension, pseudotumor cerebri, intracranial hypertension, cystic fibrosis. The licence records contain no approved indication text. |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 8 of 8) |
| Number of Registrations | 8 (valid: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Mannitol is known as an osmotic agent: it stays largely in the blood and extracellular fluid, draws water out of tissue, and increases urine output. This is why it is associated with brain edema and raised intracranial or intraocular pressure.

The predicted disease is a gain-of-function disorder of the vasopressin V2 receptor (AVPR2), in which the kidney retains water and the patient develops low blood sodium. The link to mannitol is weak. Hyponatremia management depends on osmolar and water balance, but mannitol would add an osmotic load and is not an established therapy for this condition. The high TxGNN score is a computational prediction, not evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | General review of common pitfalls in evaluating hyponatremia; does not address mannitol treatment or this specific disease |

## India Market Information

The licence records contain no approved indication text. All eight licences are single-ingredient mannitol infusions.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 3476 | Axatol 20IU Infusion | Bottle of 100 ml infusion | Not stated |
| 87612 | Fabitol 20% Infusion | Bottle of 100 ml infusion | Not stated |
| 134062 | Manitol 20% Infusion | Bottle of 350 ml infusion | Not stated |
| 134615 | Mannitol IP 20% Infusion | Bottle of 350 ml infusion | Not stated |
| 135356 | Manogyl 10% Infusion | Bottle of 100 ml infusion | Not stated |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report, so please refer to the package insert for label safety information.

- **Knowledge-graph contraindication relations (not label text):** liver failure, hepatic coma and encephalopathy, liver disease, anuria, impaired renal function, pulmonary edema, intracranial hemorrhage, thrombocytopenia, neutropenia, agranulocytosis, anemia, porphyria, gallbladder disease, sleep apnea syndromes, anxiety and related disorders, and substance-related disorders.
- **Drug interactions:** 249 interactions were recorded. Examples include a Major interaction with amikacin, and Moderate interactions with lamivudine, formoterol, salbutamol, captopril, benazepril, carbamazepine, citalopram, canagliflozin and dapagliflozin.
- **Disease-specific concern:** mannitol causes osmotic diuresis and can expand intravascular volume. For this predicted indication, this adds an osmotic load and could worsen the underlying water and sodium imbalance.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score. No trials exist, the single paper does not study mannitol in this disease, and the osmotic action does not logically fit a disorder of excess water retention.

**To proceed, the following is needed:**
- Label warnings and contraindications from the India package inserts
- Mechanism of action data
- A mechanistic or preclinical rationale showing why an osmotic diuretic could help in AVPR2 gain-of-function disease
- Any case-level or clinical data on mannitol use in this condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

