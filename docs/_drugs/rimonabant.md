---
layout: default
title: Rimonabant
parent: Model Prediction Only (L5)
nav_order: 742
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Rimonabant: predicted new indication Hypervitaminosis (evidence level L5). Approved use: Obesity disorder"
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Rimonabant: From Obesity to Hypervitaminosis

## One-Sentence Summary

Rimonabant is a CB1 receptor blocker originally used to treat obesity, including monogenic obesity.
The TxGNN model predicts it may be effective for **hypervitaminosis**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** currently supporting it.
The evidence is weak, and no plausible mechanistic link has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity disorder; monogenic obesity (the India licence records contain no approved-indication text) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, rimonabant is a CB1 receptor blocker (it also acts on GPR55) whose use in obesity is established, but no clear mechanism links CB1 antagonism to hypervitaminosis.

The high TxGNN score is a graph-based prediction only. No clinical trials or literature were retrieved to support it, so the prediction should be treated as a hypothesis, not a finding.

### Other Predictions Reviewed

The model also produced six lower-ranked predictions. None has clinical trial evidence, and all are at Evidence Level L5 with a recommendation of Hold.

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|------|------|------|
| 2 | Proximal 16p11.2 microdeletion syndrome | 99.997% | The deletion is associated with obesity and metabolic features, so the link is conceptually plausible but unvalidated. Rimonabant's psychiatric adverse events are a major concern in a population with neurodevelopmental comorbidity. |
| 3 | Obsolete hypertelorism (disease) | 99.992% | No plausible mechanism. The ontology term is obsolete, so this is likely a knowledge-graph artifact. |
| 4 | Frontorhiny | 99.989% | No known link to the endocannabinoid system. |
| 5 | Pentosuria | 99.398% | Benign metabolic condition that generally needs no treatment. |
| 6 | Insomnia (disease) | 99.271% | Rimonabant is known to cause insomnia and sleep disturbance, so a therapeutic role is unfavourable. |
| 7 | Lethal polymalformative syndrome, Boissel type | 99.049% | Lethal prenatal condition, so repurposing is impractical. |

For insomnia, the single paper retrieved (PMID 19548858, a 2009 review in *Expert Opinion on Investigational Drugs*) concerns tesofensine, a different weight-loss agent. It is not direct evidence for rimonabant.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top prediction, hypervitaminosis.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 189128 | Ribafit 20mg Tablet (Lupin Ltd) | Strip of 10 tablets | Not stated in the data |
| 166255 | Oberim 20mg Tablet (Intas Pharmaceuticals Ltd) | Strip of 10 tablets | Not stated in the data |
| 165980 | Obitone 20mg Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not stated in the data |
| 64889 | Defat 20mg Tablet (Torrent Pharmaceuticals Ltd) | Strip of 10 tablets | Not stated in the data |
| 191760 | Rimobest 20mg Tablet (Aristo Pharmaceuticals Pvt Ltd) | Strip of 10 tablets | Not stated in the data |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

