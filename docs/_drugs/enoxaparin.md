---
layout: default
title: Enoxaparin
parent: Model Prediction Only (L5)
nav_order: 307
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Enoxaparin: predicted new indication Thrombophilia due to protein C deficiency, autosomal recessive (evidence level L5). Approved use: Pulmonary embolism, disseminated intravascular coagulation…"
monitor_inn: "Enoxaparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive"]
---

# Enoxaparin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Enoxaparin: From Pulmonary Embolism and Related Coagulation Disorders to Thrombophilia due to Protein C Deficiency, Autosomal Recessive
{: .text-alpha }

## One-Sentence Summary

Enoxaparin is a low-molecular-weight heparin originally used for thrombosis-related conditions such as pulmonary embolism, disseminated intravascular coagulation and purpura fulminans.
The TxGNN model predicts it may be effective for **thrombophilia due to protein C deficiency, autosomal recessive**,
but currently there are **no registered clinical trials and no publications** in the compiled data supporting this specific prediction, so the evidence rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, disseminated intravascular coagulation, purpura fulminans, acquired purpura fulminans (from the knowledge graph; no approved indication text is recorded in the India licence data) |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, enoxaparin is a low-molecular-weight heparin that potentiates antithrombin and mainly inhibits factor Xa. This reduces thrombin generation and so limits clot formation.

In severe (homozygous or compound heterozygous) protein C deficiency, the protein C anticoagulant pathway is lost and thrombin generation goes unchecked. This typically presents as neonatal purpura fulminans. Enoxaparin's existing indications include purpura fulminans and acquired purpura fulminans, which are closely related protein C pathway disorders. The score for this prediction (0.9958) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Two caveats apply. The mechanism-of-action field is missing, and the TxGNN score is a computational prediction only. No trials or publications were supplied for this specific indication, so clinical use in protein C deficiency cannot be verified from the available data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Enoxaparin has 20 valid single-ingredient registrations and no cancelled ones. Approved indication text is not recorded for any of them. The first five are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 74006 | Encoxel 40 Injection | Prefilled syringe, 0.4 ml injection | Not recorded |
| 188112 | Renoxa 60mg Injection | Vial, 1 ml injection | Not recorded |
| 80787 | Enoxijet 60 Injection | Prefilled syringe, 0.6 ml injection | Not recorded |
| 138259 | Macparin 60mg Injection | Vial, 0.6 ml injection | Not recorded |
| 191232 | RB 40mg Injection | Vial, 1 injection | Not recorded |

## Safety Considerations

- **Contraindications (associations, not label text)**: liver failure, haematologic disease, thrombocytopenia, heparin-induced thrombocytopenia, blood coagulation disease, haemophilia, antithrombin III deficiency, Glanzmann thrombasthenia, qualitative platelet defect, intracranial or intracerebral haemorrhage, placental abruption, active peptic ulcer disease, ulcerative colitis, inflammatory bowel disease, biliary tract disease, obstructive jaundice, infective endocarditis (including subacute bacterial endocarditis), retinal disease (including diabetic and hypertensive retinopathy, retinitis, diabetic cataract), osteoporosis (including postmenopausal), and arteriosclerosis obliterans.
- **Drug Interactions**: 174 interactions are recorded. Major ones among the 20 listed include:
  - Antiplatelet and anti-inflammatory drugs: acetylsalicylic acid, ibuprofen, ketorolac, abciximab
  - Thrombolytic: alteplase
  - Other drugs: deferasirox, acalabrutinib, trastuzumab emtansine, ibritumomab tiuxetan, tositumomab
  
  Moderate interactions include dexfenfluramine, fenfluramine, sibutramine, sugammadex, aliskiren, radioactive iodide (I-123 and I-131) and topical diclofenac. Most major interactions involve additive bleeding risk.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high and the mechanism is plausible, given the link to purpura fulminans. However, there are no clinical trials or publications for this indication (Evidence Level L5). Package insert warnings and contraindications are also missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India Pharma website
- Mechanism of action data from DrugBank
- A literature and trial search for enoxaparin or low-molecular-weight heparin in severe congenital protein C deficiency and neonatal purpura fulminans
- A bleeding-risk assessment that accounts for the major drug interactions and the contraindication associations above
- Confirmation of the approved indications on the India licences
- Route and formulation compatibility assessment for the target population, including neonates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

