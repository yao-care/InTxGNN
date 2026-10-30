---
layout: default
title: Parnaparin
parent: Model Prediction Only (L5)
nav_order: 647
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
monitor_inn: "Parnaparin"
predicted_indications: ["breast fibrocystic disease", "thrombophilia due to protein C deficiency, autosomal recessive", "benign mammary dysplasia"]
description: "Parnaparin: predicted new indication Breast fibrocystic disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Parnaparin
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

## Parnaparin: Breast fibrocystic disease
{: .text-alpha }

## One-Sentence Summary

Parnaparin is a low-molecular-weight heparin (LMWH), originally associated with pulmonary embolism, disseminated intravascular coagulation and purpura fulminans.
The TxGNN model predicts it may be effective for **breast fibrocystic disease**, but **no clinical trials and no publications** currently support this prediction, so it is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Breast fibrocystic disease |
| TxGNN Prediction Score | 0.9921 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (4 of 4) – CDSCO approval status is not included in this data |
| Number of Registrations | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, parnaparin is a low-molecular-weight heparin, a class with anticoagulant activity and some reported anti-inflammatory and endothelial effects. Its efficacy in thrombotic and coagulation disorders is the basis of its original indications.

A plausible link between this class and fibrocystic breast disease, a benign, hormone-driven condition, is not established in the data compiled for this report. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The third-ranked prediction, benign mammary dysplasia (score 0.9903), is essentially the same condition as fibrocystic breast disease. It likely reflects the same signal and should not be counted as independent corroboration.

A more biologically coherent alternative is the second-ranked prediction, **thrombophilia due to protein C deficiency (autosomal recessive)**, with a score of 0.9911. Parnaparin's original indications (purpura fulminans, DIC) are closely related to severe protein C deficiency, and heparin anticoagulation is a recognized supportive approach there. It also has no trials or publications supplied, so it remains at L5 and Hold. A targeted literature search on LMWH in congenital protein C deficiency is worthwhile.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 85837 | Fluxum 3200IU Injection (USV Ltd) | Vial of 1 ml injection | Not stated |
| 89540 | Fluxium Injection (Swiss Pharma Pvt Ltd) | Vial of 1 ml injection | Not stated |
| 88762 | Fluxum 6400IU Injection (USV Ltd) | Vial of 1 ml injection | Not stated |
| 87668 | Fluxum 4250IU Injection (USV Ltd) | Vial of 1 ml injection | Not stated |

All four registrations are valid single-ingredient injectable products.

## Safety Considerations

The following contraindication-related conditions come from the drug-disease knowledge graph, not from package insert text:

- **Bleeding and coagulation disorders**: hemophilia, blood coagulation disease, thrombocytopenia, heparin-induced thrombocytopenia, Glanzmann thrombasthenia, qualitative platelet defect, antithrombin III deficiency, hematologic disease
- **Haemorrhage risk**: intracranial hemorrhage, intracerebral hemorrhage, placental abruption
- **Gastrointestinal and hepatobiliary**: active peptic ulcer disease, ulcerative colitis, inflammatory bowel disease, liver failure, biliary tract disease, obstructive jaundice
- **Eye and vascular**: retinal disease, retinitis, diabetic retinopathy, hypertensive retinopathy, diabetic cataract, arteriosclerosis obliterans
- **Infection**: infective endocarditis, endocarditis, subacute bacterial endocarditis
- **Bone**: osteoporosis, postmenopausal osteoporosis

No drug interaction data were found. Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for breast fibrocystic disease rests solely on a model score, with no trials, no literature and no established mechanistic rationale. The two breast-related predictions are duplicates of one signal.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India Pharma source (a blocking gap for safety screening)
- Mechanism of action data for parnaparin from DrugBank
- A targeted literature and trial search for LMWH in fibrocystic breast disease, and in congenital protein C deficiency as the more plausible candidate
- Route compatibility and indication similarity assessment (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

