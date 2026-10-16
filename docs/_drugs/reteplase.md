---
layout: default
title: Reteplase
parent: Moderate Evidence (L3-L4)
nav_order: 735
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Reteplase: predicted new indication Posterolateral myocardial infarction (evidence level L4). Approved use: Myocardial infarction, coronary thrombosis"
---

# Reteplase
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

# Reteplase: From Myocardial Infarction to Posterolateral Myocardial Infarction

## One-Sentence Summary

Reteplase is a recombinant tissue plasminogen activator (a clot-dissolving drug) originally used to treat myocardial infarction and coronary thrombosis.
The TxGNN model predicts it may be effective for **posterolateral myocardial infarction**, but this is an anatomical subtype of the already-approved indication rather than a true new use.
Evidence is thin: **0 registered clinical trials** and **1 publication** (a case report), so the support is essentially model prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myocardial infarction, coronary thrombosis (hemoglobinopathy is also listed in the knowledge graph) |
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, reteplase is a recombinant tissue plasminogen activator that converts plasminogen to plasmin and dissolves fibrin clots in occluded coronary arteries. Its efficacy in acute myocardial infarction is established, and mechanistically it applies to any infarction caused by a thrombus in a coronary artery.

Posterolateral myocardial infarction is defined by the part of the heart wall affected, not by a different disease process. It therefore falls under the existing myocardial infarction indication. The very high TxGNN score most likely reflects its closeness to the parent myocardial infarction node in the knowledge graph. For this reason it is not a true repurposing candidate.

Other predictions in the list are weaker still:
- **Coronary stenosis** has the most reteplase-specific literature, but this comes from the facilitated-PCI era, and that strategy has since fallen out of favor.
- **Septal myocardial infarction** is another subtype of the approved indication.
- **Thrombophilias** (heparin cofactor 2 deficiency, antithrombin deficiency type 2) would benefit from thrombolysis only during an acute thrombotic event, not for the underlying disorder.
- **Congenital coronary anomaly, beta-thalassemia, chromosome 16 partial deletion and glucophosphate isomerase deficiency hemolytic anemia** have no plausible disease-modifying role for a fibrinolytic and are likely graph artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21351226](https://pubmed.ncbi.nlm.nih.gov/21351226/) | 2011 | Case report | Catheter Cardiovasc Interv | Primary PCI of an unprotected left main with mini-crush drug-eluting stents, facilitated by intracoronary reteplase, in a patient with posterolateral acute MI. It does not evaluate reteplase efficacy. |

Related literature for other predicted indications (not for posterolateral MI) includes:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15800019](https://pubmed.ncbi.nlm.nih.gov/15800019/) | 2005 | Cohort (secondary analysis of trial data) | Eur Heart J | GUSTO-V: relationship between aPTT and outcomes after standard-dose reteplase or half-dose reteplase plus abciximab (coronary stenosis). |
| [11079647](https://pubmed.ncbi.nlm.nih.gov/11079647/) | 2000 | Clinical trial | J Am Coll Cardiol | SPEED (GUSTO-4 pilot): early PCI after reteplase with or without abciximab in acute MI (coronary stenosis). |
| [16786798](https://pubmed.ncbi.nlm.nih.gov/16786798/) | 2005 | Case report | Przegl Lek | Reteplase plus abciximab in a patient with inferior and right ventricular MI and congenital atrial septal defect (septal MI). Context is only indirect. |
| [34512848](https://pubmed.ncbi.nlm.nih.gov/34512848/) | 2021 | Review/case report | Pan Afr Med J | De Winter ECG pattern in spontaneous coronary artery dissection (congenital coronary anomaly). Not a reteplase study. |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 185024 | Retefast 18mg Injection (Cipla Ltd) | Vial of 10 ml injection | Not stated in the data compiled |
| 236830 | Vascium 18mg Injection (Emcure Pharmaceuticals Ltd) | Vial of 1 injection | Not stated in the data compiled |
| 184768 | Retefuse 18mg Injection (Lupin Ltd) | Packet of 1 injection | Not stated in the data compiled |
| 186122 | Retefast Kit (Cipla Ltd) | Box of 1 injection | Not stated in the data compiled |

All four registrations are valid single-ingredient injectable products.

---

## Safety Considerations

**Drug Interactions:** 137 interactions were identified. Examples with a **Major** level include:
- Abciximab
- Apixaban
- Betrixaban
- Acalabrutinib
- Avapritinib
- Deferasirox
- Ibritumomab tiuxetan
- Tositumomab

Examples with a **Moderate** level include:
- Acetylsalicylic acid
- Ibuprofen
- Ketorolac
- Celecoxib
- Aminocaproic acid
- Omega-3 fatty acids
- Fenfluramine, dexfenfluramine and sibutramine

Most of these involve additive bleeding risk with anticoagulants, antiplatelets and NSAIDs.

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predictions are subtypes of myocardial infarction, which reteplase already covers, so they add little as repurposing opportunities. No clinical trials were found, and the literature consists mainly of case reports and older facilitated-PCI studies. The more distant predictions have no plausible mechanism.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian products (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A decision on whether the subtype predictions need separate evaluation, since they fall under the existing label
- Reteplase-specific trial or registry evidence for any indication that is genuinely outside the current label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

