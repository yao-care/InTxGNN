---
layout: default
title: Olanzapine
parent: Model Prediction Only (L5)
nav_order: 615
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
monitor_inn: "Olanzapine"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia"]
description: "Olanzapine: predicted new indication Benign paroxysmal torticollis of infancy (evidence level L5). In India: at least 20 listed products"
---

# Olanzapine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Olanzapine: Benign paroxysmal torticollis of infancy
{: .text-alpha }

## One-Sentence Summary

Olanzapine is an antipsychotic originally used to treat schizophrenia, bipolar disorder, and depressive and anxiety disorders.
The TxGNN model predicts it may be effective for **benign paroxysmal torticollis of infancy**,
but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Benign paroxysmal torticollis of infancy |
| TxGNN Prediction Score | 0.9954 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for olanzapine: "The mechanism of action of olanzapine, in the listed indications, is unclear. However, the efficacy of olanzapine in schizophrenia could be mediated through a combination of dopamine and serotonin type 2 (5HT 2 ) antagonism." ([DailyMed: Weltruza (olanzapine) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a23e99c7-fb76-46d2-95af-e03d5a4d1f2c), label version 2026-10-26; accessed 2026-11-19.) Olanzapine is generally known as a dopamine D2 and serotonin 5-HT2A antagonist, and its efficacy in psychotic and mood disorders is established.

The predicted condition is a rare, self-limiting paroxysmal movement disorder of infancy. It is related to the migraine spectrum and to CACNA1A channelopathy. There is no established link between this condition and olanzapine's receptor pharmacology. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Olanzapine is also poorly suited to infants because of its metabolic and sedative adverse effects, and the condition usually resolves on its own. The prediction should therefore be treated as a weak, hypothesis-only signal.

For context, two other predictions for this drug have more supporting evidence (both L3, "Research Question"):
- **Agoraphobia** (score 0.9947): a 12-week open-label olanzapine augmentation trial in treatment-resistant panic disorder (31 patients), plus case reports.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Twenty valid single-ingredient registrations are on record (no cancelled licences). The approved indication text is blank in the data compiled for this report. Five representative registrations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 167725 | Olafast 20mg Tablet (Jagsam Pharma) | Strip of 10 tablets | Not stated |
| 168855 | Olace 20mg Tablet (La Pharmaceuticals) | Strip of 10 tablets | Not stated |
| 115118 | Jpine 5mg Tablet (Jpee Drugs) | Strip of 10 tablets | Not stated |
| 167659 | Oliza Pet 10mg Tablet (Intas Pharmaceuticals Ltd) | Strip of 30 tablets | Not stated |
| 128536 | Lanopin 10mg Tablet MD (Molekule India Pvt Ltd) | Strip of 10 tablets (MD) | Not stated |

All registered products are oral tablets.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for label safety information.

- **Contraindication and caution signals from the knowledge graph** (these are graph edges, not label text). Conditions flagged include:
  - Cardiovascular and cerebrovascular: orthostatic hypotension, stroke and cerebral infarction, myocardial infarction.
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hyperlipidaemia, obesity.
  - Haematological: neutropenia, agranulocytosis.
  - Hepatic: liver failure, liver disease, cirrhosis.
  - Neurological and other: epilepsy, benign prostatic hyperplasia.
- **Drug Interactions**: 338 interactions were identified. Major-level interactions include:
  - Bupropion
  - Morphine
  - Potassium citrate

  Moderate-level examples include metformin and other antidiabetic agents, anticholinergics (atropine, hyoscyamine, glycopyrronium), famotidine, clarithromycin, and epinephrine.

The metabolic and sedative effects of olanzapine are especially concerning in infants.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials or publications, no plausible mechanistic link, and an unfavourable risk-benefit profile in infants for a usually self-limiting condition.

**To proceed, the following is needed:**
- Any mechanistic or clinical rationale linking olanzapine to this condition (none is currently apparent)
- Detailed mechanism of action data
- Package insert warnings and contraindications from the India regulatory source
- Consider redirecting effort to the better-supported predictions (agoraphobia and dysthymic disorder), which warrant controlled studies and a metabolic risk-benefit assessment against established first-line options

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Weltruza (olanzapine) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a23e99c7-fb76-46d2-95af-e03d5a4d1f2c) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

