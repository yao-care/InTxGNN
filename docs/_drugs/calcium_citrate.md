---
layout: default
title: Calcium Citrate
parent: Model Prediction Only (L5)
nav_order: 134
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Calcium Citrate: predicted new indication Hemoglobinopathy (evidence level L5). Approved use: Not stated in the available licence data"
---

# Calcium Citrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Calcium Citrate: From a Calcium Supplement to Hemoglobinopathy

## One-Sentence Summary

Calcium citrate is a calcium supplement and citrate source, marketed in India as oral tablets. No approved indication text is available in the data compiled for this report.
The TxGNN model predicts it may be effective for **hemoglobinopathy** with a very high score, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence data |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Calcium citrate is a calcium supplement and citrate source. Calcium plays a central role in bone metabolism, and calcium and vitamin D deficiency or inadequate intake is common.

The data compiled for this report found **no clear mechanistic link** between calcium citrate and hemoglobinopathy. Calcium and bone health matter in thalassemia-related osteoporosis, but that is supportive care, not a disease-modifying effect on the underlying blood disorder. The high TxGNN score therefore appears to reflect knowledge-graph proximity rather than a pharmacological rationale.

Other top-ranked predictions show the same pattern: several are other hematologic conditions (beta-thalassemia, a rare glycolytic enzyme deficiency, a chromosome 16p deletion) that likely cluster together in the network, and none has trial or literature support. The most evidence-rich prediction is myocardial infarction (4 publications, none a clinical trial of calcium citrate for MI). Its evidence is mixed: a preclinical rat study of citrate pretreatment in ischemia/reperfusion injury, alongside debate over whether calcium supplements raise cardiovascular risk.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for hemoglobinopathy.

For reference, the literature found for the second-ranked prediction (myocardial infarction) is indirect and does not support the hemoglobinopathy prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25147494](https://pubmed.ncbi.nlm.nih.gov/25147494/) | 2014 | Review | Food & Nutrition Research | Calcium and vitamin D are essential for bone metabolism; deficiency or inadequate intake is common |
| [27813585](https://pubmed.ncbi.nlm.nih.gov/27813585/) | 2016 | Preclinical (rat model) | Genetics and Molecular Research | Citrate pretreatment studied for effects on ventricular arrhythmia and caspase-3 expression in ischemia/reperfusion injury |
| [24619106](https://pubmed.ncbi.nlm.nih.gov/24619106/) | 2014 | Physiological study | European Journal of Clinical Nutrition | Acute oral calcium load effects on arterial properties and endothelial function in healthy subjects; addresses vascular safety, not MI outcomes |
| [33668039](https://pubmed.ncbi.nlm.nih.gov/33668039/) | 2021 | Bioinformatics | Aging | LncRNA-mRNA co-expression analysis for MI biomarkers; not specific to calcium citrate |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 59815 | Dotshine Plus Tablet | Strip of 10 tablets | Not stated |
| 247567 | Zadilex Tablet | Strip of 10 tablets | Not stated |
| 37757 | Calcilead-HD Tablet | Strip of 10 tablets | Not stated |
| 217118 | Tenz-Cal Tablet | Strip of 10 tablets | Not stated |
| 137164 | Muscobon Tablet | Strip of 10 tablets | Not stated |

All 8 registrations are valid single-ingredient licences for oral tablets; the five above are shown.

---

## Safety Considerations

- **Drug Interactions**: 84 interactions were identified in total. The data compiled for this report lists a sample of 20, including:
  - **Major**: Dolutegravir, Bictegravir
  - **Moderate**: Doxycycline, Tetracycline, bisphosphonates (Alendronic acid, Risedronic acid, Ibandronate), calcium channel blockers (Nifedipine, Amlodipine, Diltiazem), beta-blockers (Acebutolol, Atenolol, Betaxolol, Bisoprolol, Carvedilol), thiazide diuretics (Hydrochlorothiazide, Chlorothiazide), Baloxavir marboxil, and topical vitamin D analogues (Calcipotriol, Calcitriol)

- **Cardiovascular consideration**: Calcium supplements have been debated for a possible cardiovascular risk. Calcium also acts as a coagulation cofactor, so a theoretical pro-thrombotic concern exists rather than a therapeutic benefit.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or literature and no plausible disease-modifying mechanism for hemoglobinopathy. Calcium citrate's role in thalassemia is limited to supportive bone care, which is not a repurposing indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator's materials, to enable safety screening
- Mechanism of action data (for example, from DrugBank)
- Any clinical or mechanistic evidence linking calcium citrate to hemoglobinopathy beyond supportive bone care
- Approved indication text for the registered products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

