---
layout: default
title: Acenocoumarol
parent: Model Prediction Only (L5)
nav_order: 17
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
description: "Acenocoumarol: predicted new indication Heparin cofactor 2 deficiency (evidence level L5). Approved use: Pulmonary embolism, thrombophilia"
monitor_inn: "Acenocoumarol"
predicted_indications: ["heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2"]
---

# Acenocoumarol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Acenocoumarol: From Pulmonary Embolism and Thrombophilia to Heparin Cofactor 2 Deficiency
{: .text-alpha }

## One-Sentence Summary

Acenocoumarol is an oral vitamin K antagonist anticoagulant, originally used for pulmonary embolism and thrombophilia.
The TxGNN model predicts it may be effective for **Heparin Cofactor 2 Deficiency**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, thrombophilia |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Acenocoumarol is a vitamin K antagonist. It inhibits vitamin K epoxide reductase (VKORC1), which reduces the synthesis of functional clotting factors II, VII, IX and X. This lowers thrombin generation. (This mechanism comes from general pharmacological knowledge and the repurposing analysis; the mechanism-of-action field in the data compiled for this report is empty.)

Heparin cofactor II deficiency is an inherited thrombophilia in which thrombin inhibition by dermatan sulfate and heparin is impaired. The original indications of acenocoumarol, thrombophilia and pulmonary embolism, share the same underlying problem of excessive thrombin activity. Reducing thrombin generation through vitamin K antagonism is therefore mechanistically plausible.

The two other top predictions follow the same logic:
- **Factor 5 excess with spontaneous thrombosis** (score 0.9978): vitamin K antagonists dampen the coagulation cascade downstream of factor V. Warfarin-class drugs are already used in factor V Leiden thrombosis.
- **Antithrombin deficiency type 2** (score 0.9977): oral vitamin K antagonists are a standard long-term option for hereditary antithrombin deficiency after initial heparin therapy.

All three predictions are model outputs with no supporting trial or literature records in the data compiled for this report.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 5385 | Aceno 3mg Tablet (Zydus Cadila) | Strip of 10 tablets | Not stated |
| 3994 | Artiflo 1 Tablet (Zuventus Healthcare Ltd) | Strip of 10 tablets | Not stated |
| 6843 | Artiflo 3mg Tablet (Zuventus Healthcare Ltd) | Strip of 10 tablets | Not stated |
| 159505 | Nicofax 3mg Tablet (Chemo Healthcare Pvt Ltd) | Strip of 10 tablets | Not stated |
| 153768 | Nicomalom 3 Tablet (Steris Healthcare Pvt Ltd) | Strip of 10 tablets | Not stated |

All 20 registrations are valid single-ingredient oral tablets; none are cancelled. The five above are shown as examples.

## Safety Considerations

**Drug Interactions**: The interaction screen found 117 potential interacting drugs. Severity levels are not classified in the source. Examples include:
- Acetylsalicylic acid
- Metronidazole
- Corticosteroids (prednisone, prednisolone, hydrocortisone, dexamethasone, budesonide)
- Proton pump inhibitors (omeprazole, pantoprazole, lansoprazole)
- Statins (simvastatin, rosuvastatin)
- Metformin, morphine, vancomycin, calcitriol, ranitidine, rosiglitazone, lactulose, potassium chloride

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, and the mechanistic link is coherent with acenocoumarol's established use in thrombophilia. However, there are no clinical trials or literature for this indication, so the evidence is at L5 (model prediction only). Safety data from the package insert are also missing.

**To proceed, the following is needed:**
- Targeted search for clinical and literature evidence on vitamin K antagonist use in heparin cofactor II deficiency (and the related factor V and antithrombin type 2 predictions)
- Mechanism of action data from DrugBank
- Package insert warnings and contraindications from the Indian regulatory sources, to allow safety screening
- Severity classification of the drug interactions, especially with antiplatelet agents, corticosteroids and antibiotics
- Route and formulation compatibility check (currently only oral tablets are marketed)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

