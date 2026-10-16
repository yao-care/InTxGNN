---
layout: default
title: Reserpine
parent: Model Prediction Only (L5)
nav_order: 734
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Reserpine: predicted new indication Treatment-refractory schizophrenia (evidence level L5). Approved use: Hypertension and psychotic disorders"
monitor_inn: "Reserpine"
predicted_indications: ["treatment-refractory schizophrenia"]
---

# Reserpine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Reserpine: From Hypertension and Psychotic Disorders to Treatment-Refractory Schizophrenia

## One-Sentence Summary

Reserpine is an older drug originally used to treat hypertension and psychotic disorders, including schizophrenia.
The TxGNN model predicts it may be effective for **treatment-refractory schizophrenia**,
but **no clinical trials or publications** were found in the data compiled for this report, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and psychotic disorders (from the knowledge graph; the India licence lists no indication text) |
| Predicted New Indication | Treatment-refractory schizophrenia |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Reserpine irreversibly inhibits vesicular monoamine transporter 2 (VMAT2). This depletes presynaptic stores of dopamine, norepinephrine and serotonin. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description comes from general pharmacological knowledge.

Dopamine depletion is consistent with antipsychotic activity. Reserpine was used historically as an early antipsychotic in schizophrenia and other psychotic disorders, and these conditions are already among its original indications. Treatment-refractory schizophrenia is a subgroup of the same disease, which probably explains the high model score.

The score is a computational prediction only. It likely reflects the drug's link to related psychotic disorders, not independent evidence of benefit in refractory disease. Reserpine's historical efficacy was modest compared with later antipsychotics. Its adverse effects (depression, sedation, hypotension, extrapyramidal symptoms) are a particular concern in a population that is already hard to treat.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 5857 | Adelphane 0.1mg/10mg Tablet (Novartis India Ltd) | Strip of 10 tablets (oral) | Not stated |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these are model-derived associations, not package insert text):
  - Liver: liver failure, liver disease, cirrhosis, hepatic coma, hepatic encephalopathy
  - Kidney: kidney disease, anuria, nephrocalcinosis, pyoureter
  - Gastrointestinal: peptic ulcer disease, pancreatitis, gallbladder disease
  - Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, gout, hyperuricemia, hypercalcemia, hyperparathyroidism, potassium deficiency, phosphorus metabolism disease
  - Neuropsychiatric: epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder
  - Other: hypotensive disorder, systemic lupus erythematosus, neonatal jaundice, slow acetylation
- **Drug Interactions**: 103 interactions were recorded. The 20 listed in the data were all of Moderate severity:
  - Corticosteroids: hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide
  - Antidiabetic agents: canagliflozin, dapagliflozin, empagliflozin, chlorpropamide, glimepiride, repaglinide, insulin aspart, degludec, detemir and glargine
  - Sympathomimetics and stimulants: epinephrine, bupropion, diethylpropion, phentermine
  - Other: dronabinol

The concern about depression and dysthymic disorder is especially relevant for a psychiatric population.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model (Evidence Level L5), with no trials or publications for the refractory subgroup. Reserpine's modest historical efficacy and its adverse-effect profile weigh against advancing it for a difficult-to-treat population without further evidence.

**To proceed, the following is needed:**
- A systematic literature search for historical and recent reserpine studies in refractory schizophrenia
- Package insert warnings and contraindications for the India-marketed product (these are currently missing, which blocks safety screening)
- Confirmed mechanism-of-action data from DrugBank
- A comparison against current standard options for refractory schizophrenia, such as clozapine
- A risk assessment of depression, hypotension and extrapyramidal effects, with a monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

