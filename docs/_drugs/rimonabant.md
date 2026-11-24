---
layout: default
title: Rimonabant
parent: Model Prediction Only (L5)
nav_order: 742
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
description: "Rimonabant: predicted new indication Hypervitaminosis (evidence level L5). Approved use: Obesity disorder"
monitor_inn: "Rimonabant"
predicted_indications: ["hypervitaminosis", "proximal 16p11.2 microdeletion syndrome", "obsolete hypertelorism (disease)", "frontorhiny", "pentosuria", "insomnia (disease)", "lethal polymalformative syndrome, Boissel type"]
---

# Rimonabant
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

## Rimonabant: From Obesity to Hypervitaminosis
{: .text-alpha }

## One-Sentence Summary

Rimonabant is a CB1 receptor blocker originally used to treat obesity, including monogenic obesity.
The TxGNN model (deep learning) predicts it may be effective for **hypervitaminosis**, but this score may reflect similarities the model learned between related diseases, not biological evidence, with **0 clinical trials** and **0 publications** currently supporting it.
The evidence is weak, and no plausible mechanistic link has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity disorder; monogenic obesity (the India licence records contain no approved-indication text) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (9 of 9) – CDSCO approval status is not included in this data |
| Number of Listed Products | 9 (valid: 9) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of rimonabant as: Cannabinoid CB1 receptor antagonist ([ChEMBL CHEMBL111 (rimonabant): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL111), CC BY-SA 3.0; accessed 2026-11-19.) Based on known information, rimonabant is a CB1 receptor blocker (it also acts on GPR55) whose use in obesity is established, but no clear mechanism links CB1 antagonism to hypervitaminosis.

The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No clinical trials or literature were retrieved to support it, so the prediction should be treated as a hypothesis, not a finding.

### Other Predictions Reviewed

The model also produced six lower-ranked predictions. None has clinical trial evidence, and all are at Evidence Level L5 with a recommendation of Hold.

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|------|------|------|
| 2 | Proximal 16p11.2 microdeletion syndrome | 1.0000 | The deletion is associated with obesity and metabolic features, so the link is conceptually plausible but unvalidated. Rimonabant's psychiatric adverse events are a major concern in a population with neurodevelopmental comorbidity. |
| 3 | Obsolete hypertelorism (disease) | 1.0000 | No plausible mechanism. The ontology term is obsolete, so this is likely a TxGNN model (deep learning) artifact. |
| 4 | Frontorhiny | 0.9999 | No known link to the endocannabinoid system. |
| 5 | Pentosuria | 0.9940 | Benign metabolic condition that generally needs no treatment. |
| 6 | Insomnia (disease) | 0.9927 | Rimonabant is known to cause insomnia and sleep disturbance, so a therapeutic role is unfavourable. |
| 7 | Lethal polymalformative syndrome, Boissel type | 0.9905 | Lethal prenatal condition, so repurposing is impractical. |

For insomnia, the single paper retrieved (PMID 19548858, a 2009 review in *Expert Opinion on Investigational Drugs*) concerns tesofensine, a different weight-loss agent. It is not direct evidence for rimonabant.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top prediction, hypervitaminosis.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 64889 | Defat 20mg Tablet | Strip of 10 tablets | Valid |
| 165980 | Obitone 20mg Tablet | Strip of 10 tablets | Valid |
| 166255 | Oberim 20mg Tablet | Strip of 10 tablets | Valid |
| 189128 | Ribafit 20mg Tablet | Strip of 10 tablets | Valid |
| 190232 | Rimtrim 20mg Tablet | Strip of 10 tablets | Valid |
| 191728 | Riomont 20mg Tablet | Strip of 10 tablets | Valid |
| 191760 | Rimobest 20mg Tablet | Strip of 10 tablets | Valid |
| 193150 | Rimoslim 20mg Tablet | Strip of 10 tablets | Valid |
| 195146 | Rimofit 20mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

Nine valid single-ingredient registrations exist in total, all oral tablets, and none is cancelled.

## Safety Considerations

- **Psychiatric adverse events**: Rimonabant was withdrawn in many markets because of depression, anxiety and suicidality. This is a major concern for any new use, especially in populations with neurodevelopmental comorbidity.
- **Sleep disturbance**: Rimonabant is known to cause insomnia and sleep disturbance as an adverse effect.
- **Pharmacological targets**: CB1 receptor (CNR1) and GPR55. No drug-drug interactions with other medicines were identified in the data compiled for this report.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, hypervitaminosis, rests only on a model score, with no trials, no literature and no plausible mechanism. Rimonabant's known psychiatric safety problems further argue against pursuing it without strong supporting evidence.

**To proceed, the following is needed:**
- Mechanism of action data to assess whether CB1 antagonism could plausibly relate to hypervitaminosis
- Package insert warnings and contraindications from the India regulatory source (a blocking gap for safety screening)
- Any preclinical or clinical evidence for the predicted indications. The 16p11.2 microdeletion prediction is the most biologically plausible and could be examined first, with a rigorous psychiatric risk assessment.
- Confirmation of the approved indication text for the India registrations

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL111 (rimonabant): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL111) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

