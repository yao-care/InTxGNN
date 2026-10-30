---
layout: default
title: Clopidogrel
parent: Model Prediction Only (L5)
nav_order: 204
evidence_level: L5
indication_count: 7
monitor_inn: "Clopidogrel"
predicted_indications: ["migraine with brainstem aura", "migraine disorder", "osteoarthritis", "tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis", "rheumatoid arthritis"]
last_modified_at: 2026-10-30
description: "Clopidogrel: predicted new indication migraine with brainstem aura (evidence level L5). Approved use: Not recorded in the local data"
---

# Clopidogrel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Clopidogrel: P2Y12 platelet inhibitor → migraine with brainstem aura (migraine with brainstem aura)
{: .text-alpha }

## One-Sentence Summary

Clopidogrel is an antiplatelet drug that blocks the platelet P2Y12 receptor. The TxGNN model predicts it may be effective for **migraine with brainstem aura**. The data compiled for this report contain **no registered clinical trials** and **16 publications** for this specific subtype; the studies are mostly about migraine with aura in people with patent foramen ovale (PFO), so the evidence is indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | migraine with brainstem aura |
| TxGNN Prediction Score | 0.9944 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Clopidogrel is generally known as an inhibitor of P2Y12-mediated platelet activation. The proposed link to migraine is that platelet activation and paradoxical microembolism through a right-to-left shunt, such as PFO, may release vasoactive and serotonergic mediators that trigger migraine with aura.

Most supporting papers study migraine with aura in PFO or after septal closure, not brainstem aura specifically. Brainstem aura is a subset of migraine with aura, so the link is plausible but indirect. No cited study directly examines migraine with brainstem aura, so the evidence level stays at L5 (model prediction with no direct study of this disease).

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine with brainstem aura.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | Pilot RCT | Cephalalgia | Pilot randomised trial of clopidogrel as migraine prophylaxis, prompted by anecdotal reports of benefit |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic review | Headache | Reviews the evidence on antithrombotic drugs for migraine prevention |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Cohort | J Investig Med | Clopidogrel 75 mg/day added for 3 and 6 months in drug-refractory migraine with PFO |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Cohort | Heart | Clopidogrel reduced migraine with aura after closure of PFO and atrial septal defects |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Open-label pilot | Neurology | Ticagrelor (a related P2Y12 inhibitor) in refractory migraine with PFO |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospective review | Neurology | Off-label thienopyridine use in migraineurs with PFO |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Retrospective review | Cephalalgia | Clopidogrel as primary therapy for migraineurs with right-to-left shunt |
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT (device) | Eur Heart J | PFO closure in migraine with aura; tests a device, not a drug |
| [15966922](https://pubmed.ncbi.nlm.nih.gov/15966922/) | 2005 | Case series | J Interv Cardiol | Severe migraine after atrial septal defect closure relieved by clopidogrel 300 mg |
| [22992406](https://pubmed.ncbi.nlm.nih.gov/22992406/) | 2012 | Case report | Cephalalgia | Post-closure migraine in which ticlopidine, an analogue, was effective |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 207334 | Superclop 150mg Tablet | Strip of 10 tablets | Not recorded |
| 79476 | Ecogrel 75 Tablet | Strip of 10 tablets | Not recorded |
| 248252 | Zeter Tablet | Strip of 10 tablets | Not recorded |
| 52987 | Clopergrel 75mg Tablet | Strip of 10 tablets | Not recorded |
| 33954 | Clopitab Tablet | Strip of 15 tablets | Not recorded |

The list shows only some of the records and may be partial.

## Safety Considerations

- **Contraindication-type conditions (recorded in the model's reference data, not label text)**: acute liver failure, hepatitis, blood coagulation disease, injury, thrombocytopenic purpura, active peptic ulcer disease, intracranial hemorrhage.
- **Drug Interactions**: 614 interactions are recorded. Major-level examples include rabeprazole, omeprazole, esomeprazole, pioglitazone, loperamide and repaglinide. Moderate-level examples include acetylsalicylic acid, morphine, bupropion, cimetidine and clarithromycin.
- Bleeding risk is a general concern for antiplatelet therapy and would need guardrails in any repurposing study.

Please also refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study cited here directly addresses migraine with brainstem aura. The supporting data come from migraine with aura in PFO or post-septal-closure settings, which are indirect. The prediction score is high (0.9944), but it is not enough on its own.

**To proceed, the following is needed:**
- Direct clinical evidence in migraine with brainstem aura, or a rationale for extending findings from PFO-associated migraine with aura
- Detailed mechanism-of-action data
- Package-insert warnings and contraindications from local labelling
- A bleeding-risk and drug-interaction management plan for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

