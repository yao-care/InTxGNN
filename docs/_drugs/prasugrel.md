---
layout: default
title: Prasugrel
parent: Model Prediction Only (L5)
nav_order: 694
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Prasugrel: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Acute coronary syndrome"
---

# Prasugrel
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

# Prasugrel: From Acute Coronary Syndrome to Pulmonary Hypertension

## One-Sentence Summary

Prasugrel is an antiplatelet drug originally used to treat acute coronary syndrome.
The TxGNN model ranks **pulmonary hypertension** as its top predicted new indication, but **no clinical trials and no relevant publications** currently support it.
The most evidence-backed alternative direction in the same prediction list is **migraine** (especially with patent foramen ovale), supported by 2 clinical trials and small retrospective and pilot studies, none specific to prasugrel.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute coronary syndrome |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, prasugrel is a P2Y12 receptor antagonist that inhibits platelet aggregation. Its efficacy in acute coronary syndrome is established.

The link to pulmonary hypertension is theoretical. Platelet activation and in-situ thrombosis may contribute to pulmonary vascular remodeling, so an antiplatelet drug could plausibly play a role. However, no direct evidence supports this. The two publications retrieved concern clopidogrel adherence after ACS and background therapy before COVID-19 infection, and neither addresses pulmonary hypertension.

Other predictions in the list have stronger indirect support. For migraine, especially with patent foramen ovale (PFO), thienopyridines (clopidogrel and prasugrel) have been reported to reduce migraine in some patients. The proposed explanation is that platelet-derived mediators or small emboli bypass the lung filter through the PFO. This evidence is hypothesis-generating and is not specific to prasugrel.

## Clinical Trial Evidence

Currently no clinical trials are registered for pulmonary hypertension.

For reference, trials found for the migraine prediction (second-ranked):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07629635](https://clinicaltrials.gov/study/NCT07629635) | Phase 3 | Recruiting | 32 | PFO-directed therapy for migraine cessation; the brief summary mentions prasugrel, but it is unclear whether prasugrel is a study arm |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | N/A | Terminated | 7 | Gore Cardioform septal occluder device for migraine; non-drug and uninformative for prasugrel |

## Literature Evidence

Two publications were retrieved for pulmonary hypertension, but neither is relevant to it:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort | Curr Med Res Opin | Factors associated with clopidogrel use and adherence after PCI in ACS; not related to pulmonary hypertension |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohort | Kardiologiia | Effect of pre-infection background therapy on COVID-19 outcomes (ACTIV registry); not related to pulmonary hypertension |

Related literature for the migraine predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospective review | Neurology | Off-label thienopyridine therapy in migraineurs with PFO |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Open-label pilot | Neurology | Ticagrelor (a related P2Y12 inhibitor, not prasugrel) for refractory migraine with PFO; motivated by earlier observations with clopidogrel and prasugrel |
| [42722054](https://pubmed.ncbi.nlm.nih.gov/42722054/) | 2026 | Preclinical | Eur J Pharmacol | Prasugrel reduced pentylenetetrazol-induced kindling in mice; concerns epilepsy rather than migraine |

## India Market Information

Prasugrel is marketed in India as single-ingredient oral tablets, with 20 valid registrations and none cancelled. Approved indication text is not available for these licences. Five representative registrations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 73214 | Effient 10mg Tablet (Eli Lilly and Company India) | Strip of 14 tablets | Not available |
| 191389 | Redigrel 10mg Tablet (Dr Reddy's Laboratories) | Strip of 10 tablets | Not available |
| 174545 | Prasuvas 10 Tablet (Cipla) | Strip of 10 tablets | Not available |
| 173695 | Prax 10 Tablet (Torrent Pharmaceuticals) | Strip of 10 tablets | Not available |
| 179565 | Prasugrin 10 Tablet (Zydus Cadila) | Strip of 10 tablets | Not available |

## Safety Considerations

- **Contraindications (from knowledge-graph drug-disease links, not label text)**: liver failure, hypotensive disorder, blood coagulation disease, stroke disorder, cerebrovascular disorder, cerebral infarction, injury, thrombocytopenic purpura, intracranial hemorrhage, transient ischemic attack, vertebrobasilar insufficiency.
- **Drug Interactions** (100 interactions recorded; selected):
  - **Major**: deferasirox, ibritumomab tiuxetan.
  - **Moderate**: acetylsalicylic acid (aspirin), morphine, opium, fenfluramine, dexfenfluramine, sibutramine.
  - **Minor**: proton pump inhibitors (omeprazole, esomeprazole, pantoprazole, lansoprazole, dexlansoprazole, rabeprazole), H2 blockers (famotidine, ranitidine, cimetidine, nizatidine), bupropion.

Please refer to the package insert for label warnings, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pulmonary hypertension prediction rests on a high model score alone (L5), with no trials, no relevant literature, and only a theoretical mechanism. The migraine direction (L3) is more promising but is hypothesis-generating and not prasugrel-specific. Bleeding-related contraindications and interactions also demand caution for any new use.

**To proceed, the following is needed:**
- Mechanism of action data for prasugrel
- Package insert warnings and contraindications from India-marketed labels
- Targeted literature and preclinical review on P2Y12 inhibition in pulmonary hypertension
- For migraine: confirmation of whether prasugrel is an intervention arm in NCT07629635, and prasugrel-specific data in migraineurs with PFO
- A benefit-risk assessment of bleeding in the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

