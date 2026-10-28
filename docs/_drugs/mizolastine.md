---
layout: default
title: Mizolastine
parent: Model Prediction Only (L5)
nav_order: 563
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Mizolastine"
predicted_indications: ["acute intermittent porphyria", "psychogenic movement disorders", "lingual-facial-buccal dyskinesia", "chronic tic disorder", "extrapyramidal and movement disease", "benign shuddering attacks", "primary orthostatic tremor", "tremor-nystagmus-duodenal ulcer syndrome", "benign paroxysmal tonic upgaze of childhood with ataxia", "carbamoyl phosphate synthetase I deficiency disease"]
description: "Mizolastine: predicted new indication Acute intermittent porphyria (evidence level L5). Approved use: Not recorded in the local data"
---

# Mizolastine
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

## Mizolastine: Acute intermittent porphyria
{: .text-alpha }

## One-Sentence Summary

Mizolastine is a second-generation H1 antihistamine, originally used to treat allergic rhinitis and vasomotor rhinitis.
The TxGNN model predicts it may be effective for **acute intermittent porphyria**, but this is a computational prediction only,
with **0 clinical trials** and **0 publications** currently supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acute intermittent porphyria |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mizolastine is a second-generation H1 receptor antagonist. Its use in allergic and vasomotor rhinitis is established, but the data compiled for this report do not show a mechanistic route to the predicted indication.

Acute intermittent porphyria is a metabolic disorder of heme biosynthesis, and no plausible antihistamine-related mechanism is evident. The high TxGNN score (0.9976) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Safety is also a concern. Many drugs are porphyrinogenic, and the porphyria safety of mizolastine is not established in the data compiled for this report.

**Other predicted indications (all L5, all Hold):** The model also ranks nine other conditions highly. None has clinical trial or literature support.

| Rank | Predicted Indication | TxGNN Score | Comment |
|---|---|---|---|
| 2 | Psychogenic movement disorders | 0.9971 | H1 antagonism has no known direct relevance |
| 3 | Lingual-facial-buccal dyskinesia | 0.9971 | Speculative central histaminergic link; mizolastine has limited CNS penetration |
| 4 | Chronic tic disorder | 0.9971 | Histamine H3 pathways have been explored, but mizolastine acts on H1 |
| 5 | Extrapyramidal and movement disease | 0.9970 | Broad category; no specific mechanism |
| 6 | Benign shuddering attacks | 0.9970 | Benign, self-limiting condition; unfavourable risk-benefit |
| 7 | Primary orthostatic tremor | 0.9969 | No known antihistamine mechanism |
| 8 | Tremor-nystagmus-duodenal ulcer syndrome | 0.9969 | Extremely rare; H2 blockers, not H1, are relevant to ulcers |
| 9 | Benign paroxysmal tonic upgaze of childhood with ataxia | 0.9968 | Rare channelopathy-associated condition; no link to H1 |
| 10 | Carbamoyl phosphate synthetase I deficiency disease | 0.9947 | Inborn urea cycle disorder; no plausible link |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 72480 | Elina Tablet MR (Dr Reddy's Laboratories Ltd) | Modified-release tablet (strip of 15) | Not stated in the license record |

## Safety Considerations

Please refer to the package insert for safety information.

The only interaction record compiled is pharmacological: mizolastine acts on the human H1 receptor (HRH1). It is not a drug-drug interaction, and no drug-drug interaction data are available. Mizolastine is not approved in the US.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone, with no clinical trials, no literature and no supported mechanism. Porphyria safety is unknown, which makes the lead indication a particular concern. The same applies to the other nine predicted indications.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India-marketed product. This is a blocking gap for safety screening and can be addressed by downloading and parsing the manufacturer's package insert.
- Mechanism of action data, for example from DrugBank, to allow a proper mechanistic-link analysis.
- Specific assessment of whether mizolastine is porphyrinogenic, before any further work on acute intermittent porphyria.
- A systematic search of clinical trials and literature for each predicted indication, and an indication-level assessment of route and formulation compatibility (not yet evaluated).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

