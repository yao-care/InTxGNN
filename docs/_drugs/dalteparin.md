---
layout: default
title: Dalteparin
parent: Model Prediction Only (L5)
nav_order: 229
evidence_level: L5
indication_count: 5
---

# Dalteparin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Dalteparin: From Pulmonary Embolism and Related Coagulation Disorders to Thrombophilia due to Protein C Deficiency

## One-Sentence Summary

Dalteparin is a low-molecular-weight heparin (LMWH) originally used for thrombotic and coagulation disorders such as pulmonary embolism, disseminated intravascular coagulation and purpura fulminans.
The TxGNN model predicts it may be useful for **autosomal recessive thrombophilia due to protein C deficiency**, but this is a **model prediction only**, with **no clinical trials and no publications** currently supporting this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, disseminated intravascular coagulation, purpura fulminans, acquired purpura fulminans (from the knowledge graph; the India licence records contain no indication text) |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, dalteparin is a low-molecular-weight heparin that potentiates antithrombin and inhibits factor Xa. This makes it biologically plausible for a prothrombotic state such as protein C deficiency.

The prediction is also consistent with one of dalteparin's knowledge-graph indications, purpura fulminans. This is a severe skin and clotting complication that is a classic manifestation of homozygous (severe) protein C deficiency. The two conditions share a common thrombotic pathway, which probably explains the high score.

However, the score is a network-based prediction and is not backed by any trial or publication. Standard management of severe protein C deficiency relies on protein C replacement together with anticoagulation. Any role for dalteparin would first need to be defined through a dedicated literature review.

Other predicted indications are weaker:
- **Atypical haemolytic-uraemic syndrome with thrombomodulin anomaly (99.34%)**: anticoagulation is mechanistically conceivable, but standard care is complement inhibition and heparin has no established efficacy. Renal impairment would also complicate dosing of a renally cleared LMWH.
- **Primary release disorder of platelets (99.67%) and pseudo-von Willebrand disease (99.52%)**: these are bleeding disorders, and an anticoagulant would be expected to worsen bleeding. These predictions are likely artefacts of network proximity.
- **Painful neuropathy (99.19%)**: no mechanistic link is identified.

---

## Clinical Trial Evidence

Currently no clinical trials are registered for the top predicted indication.

For reference, the only trial linked to the predictions (listed under painful neuropathy, rank 5) is not direct evidence for any predicted indication:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00445328](https://clinicaltrials.gov/study/NCT00445328) | Phase 4 | Terminated | 84 | Dalteparin vs unfractionated heparin for VTE prevention in hospitalised acutely ill medical patients; not a neuropathy or pain study, and terminated early |

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 84330 | Fragmin 5000IU Injection (Pfizer Ltd) | Prefilled syringe of 0.2 ml solution for injection | Not stated in the licence record |
| 85639 | Fragmin 10000IU Injection (Pfizer Ltd) | Prefilled syringe of 1 ml injection | Not stated in the licence record |
| 84416 | Fragmin 2500IU Injection (Pfizer Ltd) | Prefilled syringe of 0.2 ml solution for injection | Not stated in the licence record |
| 62004 | Daltehep 5000IU Injection (Gland Pharma Limited) | Vial of 2 ml injection | Not stated in the licence record |
| 67971 | Daltepin 2500IU Injection (Intas Pharmaceuticals Ltd) | Vial of 1 ml injection | Not stated in the licence record |

There are 10 valid single-ingredient registrations in total. All are injectable products, and none have been cancelled.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (these come from drug–disease network links, not from package insert text):
- **Bleeding and platelet disorders**: thrombocytopenia, heparin-induced thrombocytopenia, haemophilia, blood coagulation disease, antithrombin III deficiency, Glanzmann thrombasthenia, qualitative platelet defect, haematologic disease
- **Haemorrhage risk**: intracranial and intracerebral haemorrhage, placental abruption, active peptic ulcer disease, ulcerative colitis and inflammatory bowel disease
- **Hepatobiliary**: liver failure, biliary tract disease, obstructive jaundice
- **Eye disease with haemorrhage risk**: diabetic retinopathy, hypertensive retinopathy, retinal disease, retinitis, diabetic cataract
- **Infection and other**: infective, subacute bacterial and general endocarditis; osteoporosis (including postmenopausal); arteriosclerosis obliterans

**Drug Interactions**: 174 interactions were identified. Major-level examples include:
- Antiplatelets and NSAIDs: acetylsalicylic acid, abciximab, ketorolac, ibuprofen
- Other anticoagulants: fondaparinux
- Others: acalabrutinib, deferasirox, trastuzumab emtansine, ibritumomab tiuxetan, tositumomab

Moderate-level examples include fluvoxamine, fosinopril, sugammadex, fenfluramine, dexfenfluramine, sibutramine and radioactive iodide.

Package insert warnings and contraindications were not available. Please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (L5), with no clinical trials or publications for protein C deficiency thrombophilia. The mechanism is plausible, but standard care (protein C replacement plus anticoagulation) already exists. Several predicted indications are bleeding disorders where an anticoagulant could cause harm. The product is widely marketed in India, but its package insert safety data are missing.

**To proceed, the following is needed:**
- A targeted literature review on LMWH use in severe protein C deficiency and purpura fulminans (case reports, guidelines)
- Package insert warnings and contraindications from the India regulatory source
- Detailed mechanism of action data (e.g., from DrugBank)
- Approved indication text for the India licences
- Route and dosing assessment for the target population, including renal function considerations
- A bleeding-risk and drug-interaction management plan, particularly for antiplatelet and NSAID co-medication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

