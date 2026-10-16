---
layout: default
title: Mannitol
parent: Model Prediction Only (L5)
nav_order: 514
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Mannitol: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Brain edema, intracranial hypertension, ocular hypertension…"
monitor_inn: "Mannitol"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "acute pulmonary heart disease", "exercise-induced malignant hyperthermia", "malignant hyperthermia, susceptibility to", "familial periodic paralysis", "hypokalemic periodic paralysis", "congenital multicore myopathy with external ophthalmoplegia", "moderate multiminicore disease with hand involvement", "nephrogenic diabetes insipidus", "King-Denborough syndrome"]
---

# Mannitol
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

# Mannitol: From Intracranial Hypertension and Cerebral Edema to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol is an osmotic agent originally used for conditions such as brain edema, intracranial hypertension, ocular hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis**, but there are **no clinical trials** and only **1 general review** behind this prediction, so it is a model prediction with essentially no direct evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Brain edema, intracranial hypertension, ocular hypertension, pseudotumor cerebri, congestive heart failure, cystic fibrosis (knowledge-graph indications; the India licences carry no indication text) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mannitol is an osmotic diuretic. Its efficacy in reducing brain and tissue edema and intracranial pressure is established, and mechanistically it may be applicable to disorders of water balance.

In theory, osmotic diuresis could promote free-water excretion in a condition of excess water retention. However, mannitol can also worsen hyponatremia through translocational effects (water shifting out of cells and diluting serum sodium). The only linked paper is a general review of pitfalls in evaluating hyponatremia and is not specific to this disease. The high TxGNN score therefore remains a hypothesis and is not supported by disease-specific evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | Eur J Intern Med | Ten common pitfalls in evaluating hyponatremia; both under- and over-treatment can cause serious harm. Not specific to mannitol or this disease. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 3476 | Axatol 20IU Infusion | Bottle of 100 ml infusion | Not stated |
| 87612 | Fabitol 20% Infusion | Bottle of 100 ml infusion | Not stated |
| 134062 | Manitol 20% Infusion | Bottle of 350 ml infusion | Not stated |
| 134615 | Mannitol IP 20% Infusion | Bottle of 350 ml infusion | Not stated |
| 135356 | Manogyl 10% Infusion | Bottle of 100 ml infusion | Not stated |

Eight valid single-ingredient licences are registered in total; the five above are shown.

## Safety Considerations

- **Contraindication signals from the knowledge graph** (model-derived associations, not label text): liver failure, hepatic coma and encephalopathy, anuria, impaired renal function, intracranial hemorrhage, pulmonary edema, porphyria, and several blood disorders (thrombocytopenia, neutropenia, agranulocytosis, anemia).
- **Drug interactions**: 249 interactions were found. Major: **amikacin**. Moderate examples include lamivudine, formoterol, salbutamol, benazepril, captopril, carbamazepine, citalopram, canagliflozin, dapagliflozin, cisatracurium and iodinated contrast agents (iothalamic acid, diatrizoate).
- **Condition-specific concern**: osmotic loading can expand intravascular volume and precipitate pulmonary edema. Mannitol could also worsen free-water loss or sodium imbalance in water-balance disorders.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials and no disease-specific literature. The mechanism is plausible only in theory and may even be counterproductive, because mannitol can worsen hyponatremia.

**To proceed, the following is needed:**
- Mechanism of action data and a clear mechanistic argument for this disease
- Disease-specific preclinical or clinical evidence
- Package insert warnings and contraindications for the India-marketed products (a blocking gap for safety screening)
- A safety review covering sodium and volume effects and the knowledge-graph contraindication signals

---

### Other Predicted Indications (for reference)

All other candidates also score 99.6% or higher but remain at **Hold** (one is flagged "Research Question"), with no clinical trials.

| Rank | Predicted Indication | Evidence Level | Note |
|---|---|---|---|
| 2 | Acute pulmonary heart disease | L4 | Only indirect literature, and osmotic loading may precipitate pulmonary edema |
| 3 | Exercise-induced malignant hyperthermia | L5 | No literature |
| 4 | Malignant hyperthermia susceptibility | L4 | Mannitol is only a supportive agent or dantrolene excipient |
| 5 | Familial periodic paralysis | L4 | Mannitol serves as a potassium vehicle, not a disease-modifying therapy |
| 6 | Hypokalemic periodic paralysis | L4 | Supportive vehicle use; case-level evidence only |
| 7 | Congenital multicore myopathy with external ophthalmoplegia | L5 | Likely reflects shared RYR1 network; no literature |
| 8 | Moderate multiminicore disease with hand involvement | L5 | Likely reflects shared RYR1 network; no literature |
| 9 | Nephrogenic diabetes insipidus | L5 | Mechanistically unlikely, since osmotic diuresis may worsen polyuria |
| 10 | King-Denborough syndrome | L5 | Network proximity to malignant hyperthermia only |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

