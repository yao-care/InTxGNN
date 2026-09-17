---
layout: default
title: Reserpine
parent: Model Prediction Only (L5)
nav_order: 727
evidence_level: L5
indication_count: 1
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

Using the drug-repurposing evaluation report template to generate this report from the Evidence Pack.

# Reserpine: From Hypertension to Treatment-Refractory Schizophrenia

## One-Sentence Summary

> Reserpine is a VMAT2 inhibitor historically used to treat hypertension (and, before chlorpromazine, as an early antipsychotic). The TxGNN model predicts it may be effective for **treatment-refractory schizophrenia**, but this prediction is currently supported by **no clinical trials and no publications** — it is a model-only hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (historical; no Taiwan label/registration text available — see Data Gap DG001) |
| Predicted New Indication | Treatment-refractory schizophrenia |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | **L5** (model prediction only, no supporting trials/literature) |
| Taiwan Market Status | Not marketed (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (Data Gap DG002). Based on the mechanistic rationale supplied with this candidate, Reserpine is a **VMAT2 (vesicular monoamine transporter 2) inhibitor** that depletes presynaptic vesicular stores of dopamine, norepinephrine, and serotonin.

This mechanism aligns with the dopamine-depletion theory underlying first-generation antipsychotics from the 1950s–60s. In fact, Reserpine was one of the earliest agents used for schizophrenia, predating chlorpromazine. This gives the prediction theoretical biological plausibility for dopamine-hyperactivity-related, treatment-refractory schizophrenia.

However, the same irreversible monoamine-depletion mechanism is well known to induce severe depression, extrapyramidal symptoms, and elevated suicide risk. For this reason, modern psychiatry has completely abandoned Reserpine for psychiatric use. The mechanistic plausibility therefore comes with a significant, already-recognized safety liability that must be weighed against any repurposing rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Reserpine currently has **no active registrations in Taiwan** (market status: Not marketed / Not marketed; total licenses: 0). No approved product label or indication text is available for reference (Data Gap DG001 — TFDA label/warnings not yet retrieved).

---

## Safety Considerations

- **Drug Interactions**: DDI screening identified **103 total interactions**. Representative moderate-level interactions include:

| Interacting Drug | Level | Category |
|---|---|---|
| Epinephrine | Moderate | Sympathomimetic — risk of exaggerated pressor response |
| Hydrocortisone / Dexamethasone / Betamethasone / Budesonide / Triamcinolone | Moderate | Corticosteroids |
| Bupropion / Dronabinol / Diethylpropion / Phentermine | Moderate | CNS/appetite stimulants |
| Canagliflozin / Dapagliflozin / Empagliflozin / Glimepiride / Repaglinide / Chlorpropamide | Moderate | Antidiabetics (SGLT2i, sulfonylureas, glinides) |
| Insulin aspart / degludec / detemir / glargine | Moderate | Insulin analogues |

(20 of 103 total interactions shown; all classified as Moderate severity by DDInter.)

No package-insert-level key warnings or contraindications are currently available (Data Gap DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an **L5, model-prediction-only** candidate with zero supporting clinical trials or literature, no Taiwan market presence, and no confirmed MOA or label safety data. The known historical risk profile of Reserpine (severe depression, EPS, suicide risk) as a psychiatric agent further weighs against proceeding without stronger evidence.

**To proceed, the following is needed:**
- TFDA/official label data — warnings and contraindications (DG001, Blocking)
- Confirmed MOA from DrugBank API (DG002, High)
- Targeted literature/clinical trial search specifically for Reserpine + treatment-refractory schizophrenia
- A formal psychiatric safety risk assessment (depression/suicidality, EPS) before any further evaluation stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

