---
layout: default
title: Sotalol
parent: Model Prediction Only (L5)
nav_order: 785
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
description: "Sotalol: predicted new indication Sick sinus syndrome 2, autosomal dominant (evidence level L5). Approved use: Atrial fibrillation"
monitor_inn: "Sotalol"
predicted_indications: ["sick sinus syndrome 2, autosomal dominant", "Wildervanck syndrome", "sarcoglycanopathy", "stroke disorder", "manic bipolar affective disorder", "macrocephaly, dysmorphic facies, and psychomotor retardation"]
---

# Sotalol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Sotalol: From Atrial Fibrillation to Sick Sinus Syndrome 2, Autosomal Dominant
{: .text-alpha }

## One-Sentence Summary

Sotalol is a beta-blocker with class III antiarrhythmic activity, originally used to treat atrial fibrillation.
The TxGNN model predicts it may be effective for **sick sinus syndrome 2, autosomal dominant**, but **no clinical trials and no publications** support this prediction. The mechanistic review also suggests the prediction may be unsafe rather than therapeutic.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation |
| Predicted New Indication | Sick sinus syndrome 2, autosomal dominant |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (5 of 5) – CDSCO approval status is not included in this data |
| Number of Listed Products | 5 (valid: 5) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for sotalol: "Sotalol has both beta-adrenoreceptor blocking (Vaughan Williams Class II) and cardiac action potential duration prolongation (Vaughan Williams Class III) antiarrhythmic properties. The two isomers of sotalol have similar Class III antiarrhythmic effects, while the l-isomer is responsible for virtually all of the beta-blocking activity." ([DailyMed: Betapace (sotalol hydrochloride) prescribing information, Legacy Pharma USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a6a7702f-36c9-45db-b640-453dc324baee), label version 2024-12-16; accessed 2026-11-19.) From general pharmacology, sotalol combines beta-adrenergic blockade with potassium channel blockade (class III antiarrhythmic activity). Together these slow the sinus rate and atrioventricular conduction, which is why it is effective for atrial fibrillation.

The predicted indication is not mechanistically reasonable. Sick sinus syndrome 2 is linked to HCN4 variants that cause sinus node dysfunction. Further slowing of sinus node activity would be expected to worsen the condition, and sotalol is generally contraindicated in sick sinus syndrome without a pacemaker. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases (both conditions are rhythm disorders), not biological evidence or therapeutic plausibility.

Other predictions in the list have no better support:
- **Stroke disorder** (rank 4) is the only prediction with any evidence. The link is indirect, through rhythm control in atrial fibrillation, a major cause of cardioembolic stroke. It has not been shown that sotalol reduces stroke independently of anticoagulation.
- **Manic bipolar affective disorder**: the only literature concerns QT-related drug interactions, not benefit.
- **Wildervanck syndrome, sarcoglycanopathy, macrocephaly with dysmorphic facies and psychomotor retardation, and obsolete susceptibility to ischemic stroke**: prediction only, with no plausible mechanistic link and no evidence.

---

## Clinical Trial Evidence

Currently no clinical trials are registered for the top-ranked prediction (sick sinus syndrome 2).

For reference, the only trial found across the predicted indications relates to the rank 4 prediction (stroke disorder) and is indirect evidence:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00007605](https://clinicaltrials.gov/study/NCT00007605) | Phase 3 | Completed | 706 | CSP #399: amiodarone and sotalol for maintaining sinus rhythm in atrial fibrillation. It is relevant to the approved indication, but stroke is not clearly a primary endpoint. |

---

## Literature Evidence

Currently no related literature is available for the top-ranked prediction (sick sinus syndrome 2).

For reference, the most relevant publications retrieved for the indirect stroke-related prediction are listed below. They concern atrial fibrillation management, not stroke prevention by sotalol:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14678921](https://pubmed.ncbi.nlm.nih.gov/14678921/) | 2003 | Guideline | Ann Intern Med | AAFP/ACP guideline on management of newly detected atrial fibrillation |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Cohort | Circ Arrhythm Electrophysiol | Dronedarone vs sotalol in antiarrhythmic drug-naive veterans with atrial fibrillation |
| [37777295](https://pubmed.ncbi.nlm.nih.gov/37777295/) | 2023 | Guideline review | Am J Cardiol | Guideline recommendations on antiarrhythmic drug selection in atrial fibrillation |
| [25430048](https://pubmed.ncbi.nlm.nih.gov/25430048/) | 2014 | Review | BMJ Clin Evid | Acute-onset atrial fibrillation; it increases the risk of stroke and heart failure |
| [9358515](https://pubmed.ncbi.nlm.nih.gov/9358515/) | 1997 | Review | Pacing Clin Electrophysiol | Complications of atrial fibrillation, including embolic stroke risk |
| [29954667](https://pubmed.ncbi.nlm.nih.gov/29954667/) | 2019 | Observational study | Int J Cardiol | Efficacy and adverse effects of sotalol in adults with congenital heart disease |
| [1281807](https://pubmed.ncbi.nlm.nih.gov/1281807/) | 1992 | Clinical study | Int J Cardiol | Sotalol suppressed complex ventricular arrhythmias in 50 to 60% of treatment attempts |

---

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 199996 | Sotalar 40 Tablet | Strip of 10 tablets | Valid |
| 200738 | Solet Tablet | Strip of 10 tablets | Valid |
| 202987 | Sotagard 40mg Tablet | Strip of 10 tablets | Valid |
| 207068 | Sotagard 80mg Tablet | Strip of 10 tablets | Valid |
| 207185 | Sotalar 80mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

All five registrations are valid single-ingredient oral tablets.

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: The knowledge graph links sotalol to contraindications in the following conditions:
  - **Cardiac rhythm and conduction:** long QT syndrome (including familial), torsades de pointes, atrioventricular block, sick sinus syndrome (including familial)
  - **Respiratory and allergic:** asthma (intrinsic and allergic), bronchial disease, anaphylaxis
  - **Metabolic:** potassium deficiency disease, diabetes mellitus, diabetic ketoacidosis
  - **Other:** hypotensive disorder, impaired renal function disease

  **Sick sinus syndrome, the top predicted indication, is itself on this contraindication list.**
- **Drug Interactions**: 288 interactions were identified. Major-level interactions include:
  - Epinephrine
  - Clarithromycin
  - Picosulfuric acid
  - Polyethylene glycol (3350 with electrolytes)

  Many others are moderate, for example famotidine, cimetidine, loperamide, bupropion, morphine, atropine, canagliflozin, dapagliflozin and chlorpropamide.
- **Additional concerns**: Sotalol carries proarrhythmic risk (QT prolongation, torsades de pointes). Combination with other QT-prolonging drugs, such as some antipsychotics, adds to this risk.

Package insert warnings and contraindications for the Indian products were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (sick sinus syndrome 2) rests on model score alone (L5), with no trials or literature. It conflicts with sotalol's pharmacology and with its listed contraindication in sick sinus syndrome. The other predictions have no direct evidence. The only indirect signal is stroke risk reduction through atrial fibrillation rhythm control, which is better treated as a research question than a repurposing candidate.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian products, which are currently missing and block safety screening
- Detailed mechanism of action data (for example from DrugBank)
- For the stroke direction, trials with stroke as a primary endpoint that separate any sotalol effect from anticoagulation
- Review of whether the sick sinus syndrome prediction should be discarded as a likely TxGNN model (deep learning) artefact

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Betapace (sotalol hydrochloride) prescribing information, Legacy Pharma USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a6a7702f-36c9-45db-b640-453dc324baee) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

