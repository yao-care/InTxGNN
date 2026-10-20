---
layout: default
title: Chlorthalidone
parent: Model Prediction Only (L5)
nav_order: 177
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Chlorthalidone: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Hypertensive disorder, hypertension, congestive heart failure"
monitor_inn: "Chlorthalidone"
predicted_indications: ["primary hereditary glaucoma", "open-angle glaucoma", "malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease", "acute pulmonary heart disease", "congenital hypotrichosis milia"]
---

# Chlorthalidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Chlorthalidone: From Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Chlorthalidone is a thiazide-like diuretic originally used to treat hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**,
but **no clinical trials and no relevant publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder, hypertension, congestive heart failure |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, chlorthalidone is a thiazide-like diuretic. Its efficacy in hypertension and heart failure is well established, but its mechanistic applicability to primary hereditary glaucoma is not supported by the data compiled for this report.

Chlorthalidone has no established role in lowering intraocular pressure or in the genetic pathways of hereditary glaucoma. The high score is more likely driven by network proximity to other diuretics or carbonic anhydrase inhibitors, which has not been validated.

A related prediction, **open-angle glaucoma** (score 99.90%), has a weak theoretical basis. Chlorthalidone has mild carbonic anhydrase inhibitory activity that could relate to aqueous humor dynamics, but no clinical or literature evidence supports it, and systemic diuretics are not an established glaucoma therapy.

Among the other top-ranked predictions, the more biologically plausible ones are extensions of the hypertension indication:

- **Malignant renovascular hypertension** and **malignant hypertensive renal disease** (both 99.89%): these are plausible extensions of the approved indication, but there is no supporting evidence. These are severe, hypertensive-emergency-type settings where chlorthalidone is not a standard agent. Volume depletion may also further activate the renin-angiotensin system.
- **Chronic pulmonary heart disease** (99.82%): this is the only prediction with some indirect support, a 1967 clinical report of chlorthalidone in congestive heart failure caused by chronic cor pulmonale. It reflects symptomatic volume management, not disease modification.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for the lead prediction (primary hereditary glaucoma). The following publications were linked to other predicted indications:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5597001](https://pubmed.ncbi.nlm.nih.gov/5597001/) | 1967 | Clinical study (historical, likely uncontrolled) | La Clinica terapeutica | Diuretic therapy with chlorthalidone in congestive heart failure caused by chronic cor pulmonale (linked to chronic pulmonary heart disease) |
| [28711447](https://pubmed.ncbi.nlm.nih.gov/28711447/) | 2017 | Review | JACC. Heart failure | Review of the transition from hypertension to heart failure; only indirectly relevant |
| [14288313](https://pubmed.ncbi.nlm.nih.gov/14288313/) | 1965 | Basic research (insect physiology) | Journal of cellular and comparative physiology | Active ion transport in the Cecropia moth midgut; not relevant to human disease |

## India Market Information

Registered products (5 of 20 listed). Approved indication text is not available for these registrations.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 43685 | Chlorvix 6.5mg Tablet | Strip of 15 tablets | Not available |
| 46155 | CT-Don 12.5 Tablet | Strip of 10 tablets | Not available |
| 216514 | Telma-MCT 25/12.5 Tablet ER | Strip of 10 extended-release tablets | Not available |
| 122021 | Lupiclor 12.5 Tablet | Strip of 10 tablets | Not available |
| 49839 | Chlortag 6.25mg Tablet | Strip of 10 tablets | Not available |

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):** The drug-disease contraindication data flag the following conditions, grouped here for readability:

- **Renal and metabolic:** kidney disease, anuria, pyoureter, potassium deficiency, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, gout, hyperuricemia
- **Hepatic and digestive:** liver failure, pancreatitis, peptic ulcer disease
- **Cardiovascular:** myocardial infarction, coronary thrombosis, sudden cardiac arrest
- **Endocrine:** type 2 diabetes mellitus, diabetes mellitus
- **Respiratory and immune:** asthma (intrinsic and allergic), systemic lupus erythematosus (including pediatric)
- **Skin:** psoriasis, parapsoriasis
- **Neuropsychiatric:** epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder
- **Other:** hemoglobinopathy

**Drug Interactions:** 210 interactions were recorded. Among those listed, the most clinically significant are:

- **Major:** cisapride, dolasetron
- **Moderate:** acarbose, alogliptin, albiglutide, metformin (antidiabetic agents), amphotericin B, hydrocortisone, dexamethasone, triamcinolone, beclomethasone dipropionate (corticosteroids), omeprazole, rabeprazole, bupropion, morphine, cholecalciferol
- **Minor:** doxycycline, hyoscyamine, atropine

Package insert warnings and contraindications were not retrieved. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The primary hereditary glaucoma prediction has a very high model score (99.92%) but no clinical trials, no literature, and no plausible mechanistic link. Chlorthalidone is not an established treatment for any form of glaucoma, so the prediction is likely a network artifact. Package insert safety data have not been retrieved, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank)
- Package insert warnings and contraindications for the India-registered products
- Preclinical or mechanistic studies of chlorthalidone on intraocular pressure or aqueous humor dynamics
- If the team wants to pursue a more plausible direction, a focused review of chronic pulmonary heart disease (the only prediction with indirect clinical support) or of the hypertension-related predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

