---
layout: default
title: Ardeparin
parent: Model Prediction Only (L5)
nav_order: 66
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Ardeparin: predicted new indication Thrombophilia due to protein C deficiency, autosomal recessive (evidence level L5). Approved use: Pulmonary embolism, disseminated intravascular coagulation…"
monitor_inn: "Ardeparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive", "primary release disorder of platelets", "pseudo-von Willebrand disease", "atypical hemolytic-uremic syndrome with thrombomodulin anomaly", "neuropathy, painful", "thrombotic thrombocytopenic purpura"]
---

# Ardeparin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Ardeparin: From Pulmonary Embolism to Thrombophilia due to Protein C Deficiency (Autosomal Recessive)

## One-Sentence Summary

Ardeparin is a low-molecular-weight heparin (LMWH) anticoagulant, originally associated with pulmonary embolism, disseminated intravascular coagulation, and purpura fulminans.
The TxGNN model predicts it may be useful for **thrombophilia due to protein C deficiency, autosomal recessive**, but **no clinical trials and no publications** were found to support this prediction, so it remains a model-based research question.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, disseminated intravascular coagulation, purpura fulminans (from knowledge graph indication links; the India licence text is blank) |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data are not available in the data compiled for this report. Based on general knowledge, ardeparin is a low-molecular-weight heparin that enhances antithrombin III activity and inhibits factor Xa and thrombin.

Purpura fulminans is among its original indications, and it is the classic acute complication of severe (homozygous) protein C deficiency. This gives a plausible clinical-context link: anticoagulation is used as an adjunct alongside protein C replacement. The high TxGNN score is therefore not mechanistically implausible.

However, the prediction rests on the model alone. No trials or literature were found for this indication. Ardeparin also has limited availability in many markets, so in practice other LMWHs may be preferred.

### Other predicted indications (for context)

All other predictions ranked in the top six also lack trials and literature, and most are mechanistically doubtful:

| Rank | Predicted Indication | Score | Assessment |
|---|---|---|---|
| 2 | Primary release disorder of platelets | 99.83% | No clear rationale; a bleeding-type platelet defect where an anticoagulant would likely be harmful. Hold |
| 3 | Pseudo-von Willebrand disease | 99.75% | Bleeding disorder; anticoagulant expected to worsen bleeding. Hold |
| 4 | Atypical hemolytic-uremic syndrome with thrombomodulin anomaly | 99.74% | Speculative complement-modulating link; standard care is complement inhibition. Research question |
| 5 | Painful neuropathy | 99.62% | No evident mechanism; likely a graph artefact. Hold |
| 6 | Thrombotic thrombocytopenic purpura | 99.40% | Mechanism does not match; bleeding risk with severe thrombocytopenia. Hold |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 130372 | Lomoparin 3500IU Injection (Biological E Ltd) | Vial of 1 ml injection | Not stated in the available licence data |

Only one registration (single-ingredient, valid, injectable) is on record.

## Safety Considerations

**Contraindications (from knowledge graph drug-disease links, not label text):**
- Bleeding and coagulation disorders: hemophilia, blood coagulation disease, Glanzmann thrombasthenia, qualitative platelet defect, antithrombin III deficiency
- Thrombocytopenia, including heparin-induced thrombocytopenia
- Haemorrhagic conditions: intracranial hemorrhage, intracerebral hemorrhage, placental abruption
- Gastrointestinal conditions: active peptic ulcer disease, ulcerative colitis, inflammatory bowel disease
- Hepatic and biliary conditions: liver failure, biliary tract disease, obstructive jaundice
- Eye conditions: retinal disease, retinitis, diabetic retinopathy, hypertensive retinopathy, diabetic cataract
- Infective endocarditis (including subacute bacterial endocarditis)
- Other: osteoporosis, postmenopausal osteoporosis, arteriosclerosis obliterans, hematologic disease

**Drug Interactions:** 76 interactions were identified. The listed ones are mostly **Major** and involve other agents that affect clotting or platelets, so bleeding risk is the main concern:
- Acetylsalicylic acid, clopidogrel, cilostazol, dipyridamole, abciximab, cangrelor, caplacizumab
- Apixaban, betrixaban, bivalirudin, antithrombin III human, alteplase
- Deferasirox, ibritumomab tiuxetan, tositumomab (I-131)

Moderate interactions include fenfluramine, sibutramine, sugammadex, and iodide I-123/I-131.

Package insert warnings and contraindications were not available. Please refer to the package insert for label-based safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for protein C deficiency is biologically plausible, given the link to purpura fulminans, but it has no supporting trials or literature (evidence level L5). Safety screening cannot proceed without the package insert, and the product's licence record has no approved indication text.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for Lomoparin (blocking gap)
- Detailed mechanism of action data
- A systematic literature and trial search on LMWH use in severe protein C deficiency and purpura fulminans
- A comparison against other LMWHs with better availability and clinical data
- Clarification of the approved indication for licence 130372
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

