---
layout: default
title: Alteplase
parent: Model Prediction Only (L5)
nav_order: 41
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Alteplase: predicted new indication Posteroinferior myocardial infarction (evidence level L5). Approved use: Pulmonary embolism, stroke, myocardial infarction, coronary thrombosis"
monitor_inn: "Alteplase"
predicted_indications: ["heparin cofactor 2 deficiency", "congenital coronary artery anomaly", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "coronary stenosis"]
---

# Alteplase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Alteplase: From Myocardial Infarction and Pulmonary Embolism to Posteroinferior Myocardial Infarction

## One-Sentence Summary

Alteplase is a clot-dissolving (thrombolytic) drug originally used for acute myocardial infarction, pulmonary embolism and stroke.
The TxGNN model predicts it may be effective for **posteroinferior myocardial infarction**, but **no clinical trials or publications** specific to this subtype are currently available.
The prediction mostly restates the existing myocardial infarction indication rather than offering a new repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, stroke, myocardial infarction, coronary thrombosis (no approved indication text available in the India licence records) |
| Predicted New Indication | Posteroinferior myocardial infarction |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Alteplase is a recombinant tissue plasminogen activator. Its fibrinolytic action is well established: it converts plasminogen to plasmin, which breaks down fibrin clots. Its efficacy in acute myocardial infarction is proven, and mechanistically it may be applicable to other coronary thrombotic events.

Posteroinferior myocardial infarction is an anatomical subtype of myocardial infarction, the setting in which alteplase is already used. Lysing the occluding coronary thrombus is therefore mechanistically plausible.

The high score most likely reflects this closeness to the parent indication. It is not independent evidence of a new use. No trials or publications specific to this subtype were found.

## Other Predicted Indications (Context)

The model also ranked the following indications. None has strong evidence.

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Posterolateral myocardial infarction | 99.79% | L5 | Subtype of approved MI indication; no specific evidence |
| Septal myocardial infarction | 99.77% | L4 | Three indirect publications; overlaps with existing indication |
| Heparin cofactor 2 deficiency | 99.72% | L5 | Would treat acute clots only, not the deficiency |
| Congenital coronary artery anomaly | 99.64% | L5 | Structural defect; alteplase would not treat it |
| Factor 5 excess with spontaneous thrombosis | 99.56% | L5 | Symptomatic use only |
| Antithrombin deficiency type 2 | 99.56% | L5 | Heparin resistance complicates care; no specific evidence |
| Thrombophilia | 99.43% | L4 | Case reports and one Phase 2 trial |
| Coronary stenosis | 99.14% | L3 | Older studies, heavily overlapping with MI |

## Clinical Trial Evidence

Currently no related clinical trials are registered for posteroinferior myocardial infarction.

For reference, one trial was found for a lower-ranked prediction (thrombophilia):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05540834](https://clinicaltrials.gov/study/NCT05540834) | Phase 2 | Recruiting | 70 | Safety, dose-finding and efficacy of tPA guided by bedside viscoelastic clotting tests in critically ill patients with a pro-thrombotic acute respiratory failure; no results yet, and relevance to thrombophilia is uncertain |

## Literature Evidence

Currently no related literature is available for posteroinferior myocardial infarction.

For reference, the most relevant publications found for related predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8299637](https://pubmed.ncbi.nlm.nih.gov/8299637/) | 1993 | RCT | Eur Heart J | Double-blind trial in 80 patients with rest chest pain: alteplase vs placebo |
| [1782951](https://pubmed.ncbi.nlm.nih.gov/1782951/) | 1991 | RCT | Eur Heart J | Alteplase vs placebo in 36 patients with refractory unstable angina awaiting angioplasty |
| [19069338](https://pubmed.ncbi.nlm.nih.gov/19069338/) | 2008 | Comparative study | Srp Arh Celok Lek | Streptokinase vs alteplase, ECG and angiographic reperfusion signs in STEMI |
| [8721695](https://pubmed.ncbi.nlm.nih.gov/8721695/) | 1996 | Clinical study | Cathet Cardiovasc Diagn | Lesion-directed alteplase with intracoronary heparin in 45 unstable angina patients with coronary thrombus |
| [22094974](https://pubmed.ncbi.nlm.nih.gov/22094974/) | 2012 | Pilot study | J Thromb Thrombolysis | Early PCI after half-dose alteplase in Chinese STEMI patients |
| [8763515](https://pubmed.ncbi.nlm.nih.gov/8763515/) | 1996 | Clinical study | Rev Port Cardiol | Effect of late alteplase thrombolysis on left ventricular function in MI |
| [2118432](https://pubmed.ncbi.nlm.nih.gov/2118432/) | 1990 | Review | Circulation | Review of thrombolytic treatment in acute MI |
| [41876387](https://pubmed.ncbi.nlm.nih.gov/41876387/) | 2026 | Case report | Catheter Cardiovasc Interv | Systemic thrombolysis resistance in antithrombin III deficiency, rescued by catheter-directed thrombolysis |

Most of these studies are old and concern the already approved MI indication or unstable angina. They are indirect evidence for the predicted subtype.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 393 | Actilyse 50mg Injection (Boehringer Ingelheim) | Vial of 1 Injection | Not listed in the records |
| 1276 | Actilyse 20mg Injection (Boehringer Ingelheim) | Bottle of 20 ml Injection | Not listed in the records |

## Safety Considerations

**Drug Interactions**: 140 interactions were identified. Examples:
- **Major**: abciximab, acalabrutinib, apixaban, fondaparinux, anisindione, deferasirox, ibritumomab tiuxetan, tositumomab. These mainly raise bleeding risk.
- **Moderate**: acetylsalicylic acid, ibuprofen, ketorolac, fluvoxamine, fosinopril, aminocaproic acid, aprotinin, fenfluramine, dexfenfluramine, sibutramine.

Bleeding is the central concern when alteplase is combined with anticoagulants, antiplatelets or NSAIDs. For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Posteroinferior myocardial infarction is a subtype of an indication alteplase already has. There is no subtype-specific trial or literature, and the high TxGNN score is not independent evidence. Of the other predictions, thrombophilia and coronary stenosis have the most supporting material, but it is indirect, mostly case reports and old studies.

**To proceed, the following is needed:**
- Subtype-specific clinical data (e.g., analyses of existing MI trials by infarct location)
- Mechanism of action data
- Package insert warnings and contraindications, and approved indication text for the two India registrations
- A bleeding-risk assessment, particularly for combinations with anticoagulants and antiplatelets
- If a new-use direction is pursued, a focused review of thrombophilia and thrombolytic resistance (e.g., in antithrombin deficiency) as a more distinct repurposing question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

