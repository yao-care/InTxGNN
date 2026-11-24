---
layout: default
title: Tetrabenazine
parent: Model Prediction Only (L5)
nav_order: 826
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Tetrabenazine: predicted new indication Polycystic kidney disease 3 with or without polycystic liver disease (evidence level L5). Approved use: Huntington disease (also Huntington disease-like syndro…"
monitor_inn: "Tetrabenazine"
predicted_indications: ["polycystic kidney disease 3 with or without polycystic liver disease", "renal-hepatic-pancreatic dysplasia", "Joubert syndrome with renal defect", "karyomegalic interstitial nephritis", "thoracic malformation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "acute intermittent porphyria", "adult familial nephronophthisis-spastic quadriparesia syndrome", "atypical glycine encephalopathy", "congenital disorder of glycosylation with defective fucosylation"]
---

# Tetrabenazine
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

## Tetrabenazine: polycystic kidney disease 3 with or without polycystic liver disease
{: .text-alpha }

## One-Sentence Summary

Tetrabenazine is a VMAT2 inhibitor originally used for Huntington disease and related hyperkinetic movement disorders.
The TxGNN model predicts it may be effective for **polycystic kidney disease 3 with or without polycystic liver disease**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the TxGNN model (deep learning) score alone, which may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Huntington disease (also Huntington disease-like syndromes, juvenile Huntington disease, McLeod neuroacanthocytosis syndrome) |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (5 of 5) – CDSCO approval status is not included in this data |
| Number of Listed Products | 5 (valid: 5) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for tetrabenazine: "The precise mechanism by which XENAZINE (tetrabenazine) exerts its anti-chorea effects is unknown but is believed to be related to its effect as a reversible depletor of monoamines (such as dopamine, serotonin, norepinephrine, and histamine) from nerve terminals. Tetrabenazine reversibly inhibits the human vesicular monoamine transporter type 2 (VMAT2) (K i ≈ 100 nM), resulting in decreased uptake of monoamines into synaptic vesicles and depletion of monoamine stores." ([DailyMed: Xenazine (tetrabenazine) prescribing information, Lundbeck Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ac768bab-8afa-4446-bc7f-caeeffec0cda), label version 2026-11-06; accessed 2026-11-19.) Based on known information, tetrabenazine is a reversible VMAT2 inhibitor that depletes presynaptic monoamines. This is how it controls hyperkinetic movements in Huntington disease and related disorders.

Polycystic kidney/liver disease (the GANAB/PRKCSH-related form) is driven by cilia and polycystin dysfunction, which is unrelated to monoamine handling. No clear mechanistic link between the original and the predicted indication was identified. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence; it should be treated as a hypothesis, not as support for clinical use.

The other top-ranked predictions (for example renal-hepatic-pancreatic dysplasia, Joubert syndrome with renal defect, karyomegalic interstitial nephritis) show the same pattern. Most are ciliopathies or metabolic and developmental disorders with no plausible connection to VMAT2 inhibition. Joubert syndrome is the only one where symptomatic control of movement abnormalities is theoretically conceivable, and even there no evidence suggests an effect on the underlying disease or the renal defect.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 847 | Atrest 25 Tablet | Strip of 10 tablets | Valid |
| 977 | Atrest 12.5 Tablet | Strip of 10 tablets | Valid |
| 184214 | Revocon Tablet | Strip of 10 tablets | Valid |
| 215195 | Ticstop Tablet | Strip of 10 tablets | Valid |
| 216822 | Ticfree Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

All five registrations are valid single-ingredient oral tablets. None are cancelled.

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**:
  - Neurological and autonomic: multiple system atrophy, orthostatic hypotension, postural orthostatic tachycardia syndrome, hypotensive disorder, Parkinson disease and parkinsonian disorder
  - Cardiac: long QT syndrome (including familial), torsades de pointes
  - Psychiatric: anxiety disorder, neurotic disorder, dysthymic disorder
  - Hepatic and biliary: liver disease, gallbladder disease
  - Movement disorders: tardive dyskinesia, lingual-facial-buccal dyskinesia, drug-induced akathisia
  - Endocrine: hyperprolactinemia (including familial and acquired forms) and prolactin-producing pituitary tumor
- **Drug Interactions**: 168 interactions were identified. Major-level interactions among those reviewed include:
  - Bupropion
  - Dolasetron
  - Metoclopramide

  Moderate-level interactions include famotidine, loperamide, morphine, lorcaserin, clarithromycin, levofloxacin, and several laxative and bowel-preparation agents. The QT-related contraindication signals and the interactions with QT-prolonging agents (such as dolasetron, clarithromycin, levofloxacin) deserve particular attention.
- **Other**: For acute intermittent porphyria (rank 7), the CNS depressant effects and the interaction profile could be an added safety concern.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications (Evidence Level L5), and there is no plausible mechanistic link between VMAT2 inhibition and cilia/polycystin-driven polycystic kidney and liver disease. The drug also carries notable safety signals, including QT-related and hypotension-related concerns. None of the top 10 predictions reached beyond Hold.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank, to allow a proper mechanistic-link analysis
- Package insert warnings and contraindications from the India regulatory source, needed before any safety screening
- Preclinical evidence (for example cell or animal models of polycystic kidney disease) showing a plausible biological effect
- Targeted literature search for any link between monoaminergic pathways and polycystic kidney disease
- Review of the approved indication text, which is blank in all five registrations

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Xenazine (tetrabenazine) prescribing information, Lundbeck Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ac768bab-8afa-4446-bc7f-caeeffec0cda) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

