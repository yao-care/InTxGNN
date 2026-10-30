---
layout: default
title: Isotretinoin
parent: Model Prediction Only (L5)
nav_order: 454
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
monitor_inn: "Isotretinoin"
predicted_indications: ["malignant hypertensive renal disease"]
description: "Isotretinoin: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Isotretinoin
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

## Isotretinoin: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

This listing conflicts with its known clinical use in severe recalcitrant nodular acne and may be a data-mapping artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9901 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Isotretinoin is a retinoid. Retinoid signalling has been studied in vascular and renal biology, but this is a hypothesis and not established evidence for treating malignant renovascular hypertension.

A second prediction, malignant hypertensive renal disease, has an identical score (0.9901).

Overall, no supported mechanistic link exists between isotretinoin and malignant renovascular hypertension. The high score should be read as a model output only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Twenty valid single-ingredient registrations are on record. The five main ones are listed below. None of them has approved indication text on file.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 97044 | Gloret 10mg Tablet | Strip of 10 tablets | Not specified |
| 109591 | Isozit 20mg Soft Gelatin Capsule | Strip of 10 soft gelatin capsules | Not specified |
| 109482 | Isina 20mg Capsule | Strip of 10 capsules | Not specified |
| 241821 | Wontret 20mg Tablet | Strip of 10 tablets | Not specified |
| 200705 | Sotret NF 24mg Capsule | Strip of 10 soft gelatin capsules | Not specified |

All products are oral forms (tablets and capsules).

---

## Safety Considerations

- **Contraindications recorded in the knowledge graph** (graph relationships, not label text):
  - Psychiatric: anxiety disorder, neurotic disorder, dysthymic disorder, psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder
  - Liver, kidney and pancreas: liver disease, kidney disease, pancreatitis, gallbladder disease, pyoureter
  - Metabolic and bone: diabetes mellitus, diabetic ketoacidosis, potassium deficiency disease, hyperuricemia, osteoporosis, postmenopausal osteoporosis
  - Immune, blood and vascular: inflammatory bowel disease, systemic lupus erythematosus (including paediatric), neutropenia, agranulocytosis, hypotensive disorder
  - Angioedema (all types): acquired, hereditary, hereditary with C1Inh deficiency, non-histaminic, and RAAS-blocker-induced
- **Known safety concerns** (from the repurposing assessment): teratogenicity (boxed warning, iPLEDGE REMS), hypertriglyceridaemia and hepatotoxicity. In a kidney-related hypertensive condition, isotretinoin may worsen the dyslipidaemia that is common in kidney disease.
- **Drug Interactions**: 98 interactions are recorded. The Major-level ones among those listed are:
  - Doxycycline
  - Minocycline
  - Tetracycline
  - Vitamin A

  Moderate-level interactions include:
  - Corticosteroids (betamethasone, budesonide, dexamethasone, hydrocortisone, prednisolone, prednisone, triamcinolone)
  - Warfarin and dicoumarol
  - Naltrexone
  - Ethanol
  - Ivacaftor and lumacaftor
  - Nitisinone
  - Fostamatinib
  - Abametapir (topical)

Package insert warnings and contraindications could not be obtained for this report. Please refer to the package insert for label safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only model-based support (L5), with no clinical trials and no literature. The drug's known safety profile (teratogenicity, lipid elevation, hepatotoxicity, many interactions) is unfavourable for a severe hypertensive condition.

**To proceed, the following is needed:**
- Verification of the original indication mapping (isotretinoin's known use is acne)
- Mechanism of action data (for example from DrugBank) to assess any link between retinoid signalling and renovascular or hypertensive renal disease
- Package insert warnings and contraindications from Indian sources, to allow safety screening
- Preclinical or clinical evidence that retinoids affect malignant renovascular hypertension
- A benefit-risk analysis covering teratogenicity, lipid effects and liver and kidney safety in this patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

