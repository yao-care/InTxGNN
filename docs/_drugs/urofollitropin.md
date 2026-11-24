---
layout: default
title: Urofollitropin
parent: Model Prediction Only (L5)
nav_order: 876
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Urofollitropin: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the licence records compiled for this report (ovulation…"
monitor_inn: "Urofollitropin"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "cauda equina syndrome", "His bundle tachycardia", "restless legs syndrome", "obsolete neurogenic bladder (disease)", "multifocal atrial tachycardia (disease)", "postural orthostatic tachycardia syndrome", "Raynaud disease"]
---

# Urofollitropin
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

## Urofollitropin: From Ovulation Induction and Ovarian Stimulation to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Urofollitropin is a urinary-derived follicle-stimulating hormone (FSH) preparation, used for ovulation induction and ovarian stimulation in fertility treatment.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are currently **no clinical trials and no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records compiled for this report (ovulation induction and ovarian stimulation, based on the drug class) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of urofollitropin as: Follicle stimulating hormone receptor agonist ([ChEMBL CHEMBL1201520 (urofollitropin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1201520), CC BY-SA 3.0; accessed 2026-11-19.) Based on known information, urofollitropin is a gonadotropin (FSH) preparation derived from urine. Its efficacy in ovarian stimulation is established, but no mechanistic route to migraine has been demonstrated.

The link between the two conditions is weak. A hormonal-fluctuation hypothesis, such as menstrual-related migraine, is conceivable. However, gonadotropin stimulation would more plausibly provoke headache than treat it. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other top-ranked predictions are similarly unsupported. These include migraine with brainstem aura, cauda equina syndrome, His bundle tachycardia, restless legs syndrome, and Raynaud disease. None has clinical or literature data, and none has an identified mechanistic link to FSH receptor signalling.

## India Market Information

Twenty single-ingredient injectable registrations are valid. The licence records compiled for this report contain no approved indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 43754 | Coefsh HP 75IU Injection | Vial of 1 Injection | Valid |
| 73478 | Eema Fsh 75IU Injection | Vial of 1 Injection | Valid |
| 74798 | Euvifol-HP 150IU Injection | Vial of 1 ml Injection | Valid |
| 85292 | Fostine 75 Injection | Vial of 2 ml Injection | Valid |
| 85490 | Foliculin HP 75IU Injection | Vial of 1 Injection | Valid |
| 85820 | Foliculin HP 150IU Injection | Vial of 1 Injection | Valid |
| 86785 | Follicare 150IU HP Injection | Vial of 1 Injection | Valid |
| 91401 | Ftrop 150IU Injection | Vial of 1 Injection | Valid |
| 91951 | Fergonad F 150IU Injection | Vial of 1 Injection | Valid |
| 93101 | Ftrop 75IU Injection | Vial of 1 ml Injection | Valid |
| 108704 | Inceptova FSH Injection | Vial of 1 Injection | Valid |
| 109943 | Intas Fsh 150I.U Injection | Vial of 1 Injection | Valid |
| 121715 | Lupi-Fsh 150 Injection | Vial of 2 ml Injection | Valid |
| 125167 | Lupi Rfsh 300IU Injection | Vial of 1 ml Injection | Valid |
| 127791 | Lupi Rfsh 900IU Injection | Vial of 1 ml Injection | Valid |
| 134997 | MY Fsh 150 Injection | Vial of 1 Injection | Valid |
| 166561 | Ovitropin FSH 150IU Injection | Box of 1 Injection | Valid |
| 167837 | Ovitropin FSH 75IU Injection | Box of 1 Injection | Valid |
| 201051 | Sitrodin 75IU Injection | Vial of 1 ml Injection | Valid |
| 248088 | ZY Fsh HP 75 Injection | Vial of 1 Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: One interaction is recorded. **Ganirelix** has a Moderate-level interaction with urofollitropin (source: DDInter).

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction has a very high model score but no supporting clinical trials or publications, and no plausible mechanism. Gonadotropin stimulation may instead worsen headache. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulatory sources
- Approved indication text for the registered products
- Detailed mechanism of action data
- A mechanistic hypothesis and preclinical or observational data linking FSH to migraine, for example in menstrual-related migraine
- A safety assessment of headache or migraine as a known adverse effect of gonadotropins

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL1201520 (urofollitropin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1201520) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

