---
layout: default
title: Ticagrelor
parent: Model Prediction Only (L5)
nav_order: 835
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
monitor_inn: "Ticagrelor"
predicted_indications: ["intracranial arteriosclerosis", "Monckeberg arteriosclerosis", "priapism", "ischemic disease", "May-Thurner syndrome", "livedo reticularis", "vascular ectasia", "angiodysplasia", "venous thromboembolism"]
description: "Ticagrelor: predicted new indication Intracranial arteriosclerosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Ticagrelor
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

## Ticagrelor: Intracranial arteriosclerosis
{: .text-alpha }

## One-Sentence Summary

Ticagrelor is an oral antiplatelet drug originally used for acute coronary syndrome and peripheral arterial disease.
The TxGNN model predicts it may be effective for **intracranial arteriosclerosis**, but the supporting evidence is still early: **2 clinical trials** (neither with results yet) and **2 publications** (one cohort study and one trial-design paper).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Intracranial arteriosclerosis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 (observational cohort data only; the Phase 3 trial has not reported results) |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ticagrelor is a P2Y12 receptor antagonist, and its efficacy in acute coronary syndrome is established. Mechanistically, it may apply to intracranial arteriosclerosis.

Both conditions involve platelet-driven clot formation on atherosclerotic plaques. Blocking P2Y12 reduces platelet aggregation and thrombus formation, which is plausible for secondary stroke prevention in symptomatic intracranial atherosclerotic stenosis. Ticagrelor binds reversibly and does not need liver activation through CYP2C19. It may therefore help patients who respond poorly to clopidogrel because of CYP2C19 loss-of-function variants.

This is a mechanistic argument, not proof of benefit. The key question is whether ticagrelor-based regimens beat the current standard (clopidogrel plus aspirin), and large trials are still under way.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) (CAPTIVA) | Phase 3 | Active, not recruiting | 1683 | Tests whether rivaroxaban, ticagrelor, or both beat clopidogrel for lowering 1-year ischemic stroke, intracerebral hemorrhage, or vascular death in intracranial atherosclerotic stenosis. Results not yet available (expected completion Jan 2027). |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | Not applicable | Recruiting | 100 | Pilot study of genotype-guided P2Y12 inhibitor selection (which includes ticagrelor) versus conventional clopidogrel in symptomatic intracranial atherosclerotic disease. No results yet. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohort | Journal of Neurointerventional Surgery | Reports experience with ticagrelor 60 mg twice daily plus aspirin 81 mg versus the standard aspirin and clopidogrel regimen for intracranial stenting. |
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | Trial design paper | International Journal of Stroke | Describes the design and early progress of CAPTIVA. Symptomatic intracranial atherosclerotic stenosis carries a high recurrent stroke risk up to 12 months despite clopidogrel plus aspirin, which motivates testing other combinations. |

## India Market Information

Twenty single-ingredient registrations are valid and none are cancelled. The licence records do not include approved-indication text. Five representative authorizations:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 25738 | Brilinta 90mg Tablet | Strip of 14 tablets | AstraZeneca |
| 215591 | Ticaflo 90mg Tablet | Strip of 14 tablets | Dr Reddy's Laboratories Ltd |
| 217628 | Ticasave 60mg Tablet | Strip of 14 tablets | Eris Lifesciences Ltd |
| 215684 | Torplat 60 Tablet | Strip of 14 tablets | Torrent Pharmaceuticals Ltd |
| 556 | Axcer 60mg Tablet | Strip of 14 tablets | Sun Pharmaceutical Industries Ltd |

## Safety Considerations

- **Contraindications (not label text)**: liver failure, liver disease, gallbladder disease, and intracranial hemorrhage. Intracranial hemorrhage matters most here, because patients with intracranial atherosclerosis are at risk of it and CAPTIVA counts it as a primary outcome.
- **Drug Interactions**: 423 interactions were identified.
  - **Major**: clarithromycin.
  - **Moderate examples**: aspirin, morphine, simvastatin, dexamethasone, budesonide, aprepitant, saxagliptin, and miconazole.
  - **Minor examples**: naloxegol and prucalopride.
  - Aspirin is the planned partner drug in most regimens, so the additive bleeding risk needs attention.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and the model score is high. However, the only Phase 3 trial (CAPTIVA) has not reported results, and the other trial is a small pilot. The only published clinical data are a single cohort study and a trial-design paper. No completed randomized trial supports ticagrelor in this indication. Bleeding risk, especially intracranial hemorrhage, is a real concern in this population.

**To proceed, the following is needed:**
- CAPTIVA results, expected around 2027
- Package insert warnings and contraindications for the India-marketed products, since safety screening cannot proceed without them
- Detailed mechanism of action data
- A bleeding-risk assessment specific to patients with intracranial atherosclerotic disease, including the aspirin combination and CYP3A inhibitor interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

