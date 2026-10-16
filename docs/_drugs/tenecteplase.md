---
layout: default
title: Tenecteplase
parent: Moderate Evidence (L3-L4)
nav_order: 815
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Tenecteplase: predicted new indication Posteroinferior myocardial infarction (evidence level L4). Approved use: Myocardial infarction, coronary thrombosis"
monitor_inn: "Tenecteplase"
predicted_indications: ["posteroinferior myocardial infarction", "posterolateral myocardial infarction", "septal myocardial infarction", "congenital coronary artery anomaly", "coronary stenosis", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyropoikilocytosis, hereditary", "pyruvate kinase deficiency of red cells"]
---

# Tenecteplase
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Tenecteplase: From Myocardial Infarction to Posteroinferior Myocardial Infarction

## One-Sentence Summary

Tenecteplase is a fibrin-specific thrombolytic (clot-dissolving) drug, originally used to treat acute myocardial infarction and coronary thrombosis.
The TxGNN model predicts it may be effective for **posteroinferior myocardial infarction**, but this is an anatomical subtype of the approved indication, and **no clinical trials or publications** were retrieved specifically for it.
Evidence is therefore indirect, inferred from the parent indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myocardial infarction, coronary thrombosis (the approved indication text in the Indian licence records is empty) |
| Predicted New Indication | Posteroinferior myocardial infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 9 |
| Recommended Decision | Hold (research question only) |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, tenecteplase is a fibrin-specific tissue plasminogen activator. It converts plasminogen to plasmin at the site of a fibrin clot and dissolves the occlusive coronary thrombus that causes infarction.

Posteroinferior myocardial infarction is an anatomical subtype of myocardial infarction, which is already an established indication. The high TxGNN score most likely reflects this overlap with the approved indication rather than a new repurposing signal. The mechanism applies in principle, because the same clot-lysis effect would be needed in whichever coronary artery is blocked.

Other top-ranked predictions follow the same pattern. Posterolateral and septal myocardial infarction are also subtypes of the approved indication. Coronary stenosis has limited supportive data. The remaining predictions (congenital coronary anomaly, chromosome 16p partial deletion, beta-thalassemia, and red cell enzyme or membrane disorders) have no identified mechanistic or clinical support. They appear to be artefacts of knowledge-graph proximity to the original hemoglobinopathy association.

## Clinical Trial Evidence

Currently no related clinical trials registered for posteroinferior myocardial infarction.

## Literature Evidence

Currently no related literature available for posteroinferior myocardial infarction.

For context, the literature retrieved for other predicted indications is limited in strength:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16053952](https://pubmed.ncbi.nlm.nih.gov/16053952/) | 2005 | Trial (classified as meta-analysis) | J Am Coll Cardiol | CAPITAL AMI: tenecteplase-facilitated angioplasty compared with tenecteplase alone in high-risk STEMI (coronary stenosis candidate) |
| [31870492](https://pubmed.ncbi.nlm.nih.gov/31870492/) | 2020 | Randomized feasibility study (40 patients) | Am J Cardiol | ICE T-TIMI 49: low-dose intracoronary tenecteplase during primary PCI for STEMI was feasible and safe (coronary stenosis candidate) |
| [16139127](https://pubmed.ncbi.nlm.nih.gov/16139127/) | 2005 | Cohort | J Am Coll Cardiol | Intracoronary fibrin-specific lytic infusion to facilitate recanalization of chronic total occlusion (coronary stenosis candidate) |
| [23975441](https://pubmed.ncbi.nlm.nih.gov/23975441/) | 2014 | Case series (classified as review) | J Thromb Thrombolysis | Weight-adjusted tenecteplase in 30 patients with acute pulmonary embolism (septal MI candidate; weakly relevant) |
| [18183355](https://pubmed.ncbi.nlm.nih.gov/18183355/) | 2009 | Case report | J Thromb Thrombolysis | Pulmonary embolism mimicking septal MI, treated with tenecteplase (septal MI candidate) |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 216966 | Tenectelex 40mg Injection (Abbott Healthcare) | Vial of 1 injection | Not stated in the compiled data |
| 216255 | Telyse 40mg Injection (Cipla) | Vial of 1 injection | Not stated in the compiled data |
| 215711 | Tenecterel 40mg Injection Kit (Reliance Life Sciences) | Box of 1 injection | Not stated in the compiled data |
| 134905 | Metalyse 40mg Injection (Boehringer Ingelheim) | Vial of 1 injection | Not stated in the compiled data |
| 236600 | Velix 50mg Injection (Emcure) | Vial of 1 injection | Not stated in the compiled data |

Nine valid single-ingredient licences are registered in total. Gennova Biopharmaceuticals holds three of them (Elaxim 30, Elaxim 40 and Tenectase 20), and Reliance Life Sciences holds a second one (Tenecterel 30mg).

## Safety Considerations

- **Drug Interactions**: 137 interactions were identified. The main ones include:
  - **Major**: abciximab, apixaban, betrixaban, acalabrutinib, avapritinib, deferasirox, ibritumomab tiuxetan, tositumomab. Most of these involve additive bleeding risk.
  - **Moderate**: acetylsalicylic acid, ibuprofen, ketorolac, celecoxib, topical diclofenac, aminocaproic acid, omega-3 fatty acids, fenfluramine, dexfenfluramine, sibutramine.

Please refer to the package insert for warnings and contraindications. As a thrombolytic, tenecteplase carries a known bleeding risk that needs careful evaluation.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Posteroinferior myocardial infarction is a subtype of an indication tenecteplase already covers, so the high TxGNN score adds little new information. No trials or publications specific to this subtype were retrieved. The evidence is model prediction plus inference from the parent indication (L4). The package insert safety data are also missing, which blocks progression past initial safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator or manufacturers, plus the approved indication text for each licence
- Detailed mechanism of action data (for example from DrugBank)
- Subtype-specific analyses from existing myocardial infarction thrombolysis trials, to check whether posteroinferior MI is already covered by the approved indication
- A bleeding-risk assessment that takes the major and moderate interactions with antiplatelet and anticoagulant drugs into account
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

