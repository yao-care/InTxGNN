---
layout: default
title: Atosiban
parent: Model Prediction Only (L5)
nav_order: 81
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Atosiban: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Delaying preterm birth in adult pregnant women (tocolysis). The India…"
monitor_inn: "Atosiban"
predicted_indications: ["primary hereditary glaucoma", "open-angle glaucoma", "congenital hypotrichosis milia", "alopecia", "hypotrichosis simplex of the scalp", "vascular disease", "diffuse alopecia areata", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "visceral calciphylaxis"]
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Atosiban: From Preterm Labour (Tocolysis) to Primary Hereditary Glaucoma

## One-Sentence Summary

Atosiban is an oxytocin/vasopressin receptor antagonist marketed in India as an injectable tocolytic, used to delay preterm birth.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, but **no clinical trials and no publications** currently support this prediction, so it is a model-only hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Delaying preterm birth in adult pregnant women (tocolysis). The Indian licence records contain no indication text, so this comes from pharmacology reference data. |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. From pharmacology reference data, atosiban is a peptide that binds the oxytocin receptor (OXTR) and the vasopressin V1A, V1B and V2 receptors. Its established clinical use is to delay birth in women 24 to 33 weeks pregnant who show signs of preterm labour.

The link to primary hereditary glaucoma is weak. This condition is a genetic disorder of trabecular meshwork or angle development, and receptor antagonism has no clear rationale for it. A speculative connection might exist through oxytocin/vasopressin effects on ocular blood flow or aqueous humour dynamics, but no supporting data were found. A systemic, parenterally given peptide also faces delivery and pharmacokinetic barriers for eye use. The high score (0.999) reflects a graph-based prediction only.

The same model also ranks open-angle glaucoma (99.92%) second, and several hair disorders (alopecia, hypotrichosis, alopecia areata) and vascular conditions among the top ten. None has trial or literature support. Only "vascular disease" has indirect preclinical literature, which mostly studies oxytocin (not atosiban) in rat heart models. It is an L4 research question and not a treatment case.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for primary hereditary glaucoma.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 216021 | Tosiban 37.5mg Injection (Zuventus Healthcare Ltd) | Vial of 5 ml injection | Not stated in licence record |
| 216817 | Tosiban 6.75mg Injection (Zuventus Healthcare Ltd) | Vial of 0.9 ml solution for injection | Not stated in licence record |

## Safety Considerations

- **Drug Interactions / Receptor Binding**: Pharmacology data list atosiban binding to the vasopressin V1A, V1B and V2 receptors and the oxytocin receptor. No specific drug-drug interactions are listed.
- **Related Safety Signal**: A cohort study (PMID 30646165, JAMA Netw Open, 2018) linked tocolytic exposure to intraventricular haemorrhage and death in preterm infants. This concerns tocolytics as a class and is relevant to the obstetric use rather than to glaucoma.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph score alone, with no trials, no publications and no plausible mechanistic link to a genetic developmental glaucoma. The Indian licence records also lack indication text and the package insert safety data are not yet available.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and an assessment of any oxytocin/vasopressin role in intraocular pressure regulation
- Preclinical evidence (for example ocular receptor expression or animal glaucoma models)
- A feasibility assessment of ocular delivery for a peptide, since current products are systemic injections
- Package insert warnings and contraindications from the manufacturer or the Indian regulator
- Approved indication text for the two Indian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

