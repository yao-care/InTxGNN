---
layout: default
title: Dobutamine
parent: Model Prediction Only (L5)
nav_order: 278
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Dobutamine: predicted new indication Alopecia (evidence level L5). Approved use: Not stated in the India license data compiled for this report"
monitor_inn: "Dobutamine"
predicted_indications: ["alopecia", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "open-angle glaucoma", "Raynaud disease", "primary hereditary glaucoma", "headache disorder", "hypertrichosis (disease)", "migraine disorder"]
---

# Dobutamine
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

## Dobutamine: From Acute Cardiac Decompensation to Alopecia
{: .text-alpha }

## One-Sentence Summary

Dobutamine is an injectable beta-1 adrenergic inotrope, used in hospital settings to support heart function.
The TxGNN model predicts it may be effective for **alopecia**, but the prediction has **no registered clinical trials** and **no relevant supporting publications**.
The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, rather than a real therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India license data compiled for this report |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, dobutamine is a beta-1 adrenergic agonist (inotrope) given by intravenous infusion. It is generally used for short-term cardiac support.

The prediction is **not mechanistically convincing**. Dobutamine has no known role in hair follicle biology. The one publication retrieved is a veterinary case report of heart failure caused by minoxidil intoxication in a cat. Dobutamine was used there only to treat hypotension. It describes the cardiotoxicity of a hair-growth drug and says nothing about dobutamine treating alopecia. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Minoxidil is a vasodilator used for alopecia.

The other predicted indications are no stronger. They include hypotrichosis simplex of the scalp, congenital hypotrichosis milia, diffuse alopecia areata, open-angle glaucoma, Raynaud disease, headache disorder, hypertrichosis and migraine disorder. All are rated L5 and Hold, with no trials and no therapeutic literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | Case report (veterinary) | Journal of Veterinary Cardiology | Heart failure from minoxidil intoxication in a cat; dobutamine was used to manage hypotension. It is not evidence of efficacy for alopecia. |

---

## India Market Information

All 20 registrations are single-ingredient injectables with valid status. The license data compiled for this report contains no approved indication text. Five representative authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 43828 | Cardiforce 250mg Injection | Vial of 20 ml Injection | Not stated |
| 60084 | Dobutam Injection | Ampoule of 5 ml Injection | Not stated |
| 33298 | Butim 250mg Injection | Ampoule of 5 ml Injection | Not stated |
| 59465 | Dobutrex 250mg Injection | Vial of 50 ml Injection | Not stated |
| 42217 | Cardiject 50mg Injection | Vial of 4 ml Injection | Not stated |

---

## Safety Considerations

- **Disease contraindications flagged in the knowledge graph** (derived from graph edges, not label text): hypertension and hypertensive disorder, atrial fibrillation, aortic stenosis (including aortic valve disease and supravalvular aortic stenosis), myocardial infarction and coronary thrombosis, hypertrophic cardiomyopathy (including the familial form), potassium deficiency disease, and hemoglobinopathy.
- **Drug interactions**: 99 interactions were identified in total. All 20 listed are rated Moderate. Many involve glucose-lowering agents, including acarbose, metformin, pioglitazone, canagliflozin, dapagliflozin, empagliflozin, linagliptin, semaglutide, liraglutide, repaglinide, chlorpropamide and insulins. Others include cimetidine, vancomycin, phentermine and diethylpropion.

Package insert warnings and contraindications were not available, so please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5). There are no clinical trials and no therapeutic literature, and there is no plausible mechanism linking a beta-1 agonist given by IV infusion to hair disorders. The only paper is a veterinary report about minoxidil toxicity. The knowledge-graph contraindications also include several cardiovascular conditions.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India Pharma source (a blocking gap for safety screening)
- Mechanism of action data for dobutamine
- A credible mechanistic hypothesis and preclinical data for hair-related disorders
- Assessment of route compatibility, since dobutamine is available only as an injectable, and of benefit-risk for a non-life-threatening condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

