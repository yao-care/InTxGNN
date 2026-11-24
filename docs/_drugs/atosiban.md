---
layout: default
title: Atosiban
parent: Model Prediction Only (L5)
nav_order: 81
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Atosiban"
predicted_indications: ["primary hereditary glaucoma", "open-angle glaucoma", "congenital hypotrichosis milia", "alopecia", "hypotrichosis simplex of the scalp", "vascular disease", "diffuse alopecia areata", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "visceral calciphylaxis"]
description: "Atosiban: predicted new indication Primary hereditary glaucoma (evidence level L5). In India: 2 listed products (2 not discontinued)"
---

# Atosiban
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Atosiban: Primary hereditary glaucoma
{: .text-alpha }

## One-Sentence Summary

Atosiban is an oxytocin/vasopressin receptor antagonist marketed in India as an injectable tocolytic, used to delay preterm birth.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, but **no clinical trials and no publications** currently support this prediction, so it is a model-only hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (2 of 2) – CDSCO approval status is not included in this data |
| Number of Listed Products | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of atosiban as: Oxytocin receptor antagonist ([ChEMBL CHEMBL382301 (atosiban): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL382301), CC BY-SA 3.0; accessed 2026-11-19.) From pharmacology reference data, atosiban is a peptide that binds the oxytocin receptor (OXTR) and the vasopressin V1A, V1B and V2 receptors. Its established clinical use is to delay birth in women 24 to 33 weeks pregnant who show signs of preterm labour.

The link to primary hereditary glaucoma is weak. This condition is a genetic disorder of trabecular meshwork or angle development, and receptor antagonism has no clear rationale for it. A speculative connection might exist through oxytocin/vasopressin effects on ocular blood flow or aqueous humour dynamics, but no supporting data were found. A systemic, parenterally given peptide also faces delivery and pharmacokinetic barriers for eye use. The high score (0.9992) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The same model also ranks open-angle glaucoma (0.9992) second, and several hair disorders (alopecia, hypotrichosis, alopecia areata) and vascular conditions among the top ten. None has trial or literature support. Only "vascular disease" has indirect preclinical literature, which mostly studies oxytocin (not atosiban) in rat heart models. It is an L4 research question and not a treatment case.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for primary hereditary glaucoma.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 216021 | Tosiban 37.5mg Injection | Vial of 5 ml Injection | Valid |
| 216817 | Tosiban 6.75mg Injection | Vial of 0.9 ml Solution for Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions / Receptor Binding**: Pharmacology data list atosiban binding to the vasopressin V1A, V1B and V2 receptors and the oxytocin receptor. No specific drug-drug interactions are listed.
- **Related Safety Signal**: A cohort study (PMID 30646165, JAMA Netw Open, 2018) linked tocolytic exposure to intraventricular haemorrhage and death in preterm infants. This concerns tocolytics as a class and is relevant to the obstetric use rather than to glaucoma.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a TxGNN model (deep learning) score alone, which may reflect similarities the model learned between related diseases, not biological evidence, with no trials, no publications and no plausible mechanistic link to a genetic developmental glaucoma. The Indian licence records also lack indication text and the package insert safety data are not yet available.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and an assessment of any oxytocin/vasopressin role in intraocular pressure regulation
- Preclinical evidence (for example ocular receptor expression or animal glaucoma models)
- A feasibility assessment of ocular delivery for a peptide, since current products are systemic injections
- Package insert warnings and contraindications from the manufacturer or the Indian regulator
- Approved indication text for the two Indian licences

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL382301 (atosiban): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL382301) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

