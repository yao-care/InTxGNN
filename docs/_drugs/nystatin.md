---
layout: default
title: Nystatin
parent: Model Prediction Only (L5)
nav_order: 610
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-20
monitor_inn: "Nystatin"
predicted_indications: ["disease of orbital region", "disease of orbital part of eye adnexa", "cystic teratoma", "spinal cord dermoid cyst", "postmenopausal atrophic vaginitis", "biotin metabolic disease", "vulvitis", "commissural lip fistula", "osteoradionecrosis of the mandible"]
description: "Nystatin: predicted new indication Disease of orbital region (evidence level L5). In India: 1 listed product (1 not discontinued)"
---

# Nystatin
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

## Nystatin: Disease of orbital region
{: .text-alpha }

## One-Sentence Summary

Nystatin is a topical polyene antifungal. The TxGNN model ranks **disease of orbital region** as its top predicted new indication (score 0.9990), but **no study directly addresses this disease**: the single linked trial tests an unrelated product in retinal disease, and no literature was found. This is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Disease of orbital region |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for nystatin: "Nystatin acts by binding to sterols in the cell membrane of susceptible Candida species with a resultant change in membrane permeability allowing leakage of intracellular components. Nystatin exhibits no appreciable activity against bacteria, protozoa, or viruses." ([DailyMed: Nystatin Oral Suspension (nystatin) prescribing information, Xttrium Laboratories, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4a670371-d373-1ba6-e063-6394a90a13b6), label version 2026-02-06; accessed 2026-11-19.) As a class, polyene antifungals bind ergosterol in fungal cell membranes, forming pores that kill the fungus. That activity is relevant to fungal infection of the skin and mucosa.

No plausible mechanistic link to disease of orbital region was identified. The only associated trial (NCT03178149) tests ASP7317 in geographic atrophy secondary to age-related macular degeneration. It does not involve nystatin and concerns the retina rather than the orbit. The high score is therefore not supported by clinical evidence and should be treated as a computational signal only.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03178149](https://clinicaltrials.gov/study/NCT03178149) | Phase 1 | Recruiting | 42 | Dose-escalation safety study of ASP7317 in geographic atrophy secondary to age-related macular degeneration. Does not involve nystatin and does not study orbital disease; the match appears spurious. |

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 151372 | Nistin 100000IU Ointment (Jawa Pharmaceuticals Pvt Ltd) | Tube of 3 g ointment | Not stated in the registration record |

One valid single-ingredient licence is on record, and the drug is marketed.

## Safety Considerations

- **Drug Interactions**: 347 potential interactions are recorded, all with an unspecified severity level. Examples include cyclosporine, fluconazole, erythromycin, azithromycin, tramadol, lorazepam, bortezomib, sildenafil, valsartan and ramipril.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the model score. No study, trial or literature addresses nystatin in disease of orbital region, and the one linked trial is unrelated. There is no mechanistic basis for efficacy in this condition.

**To proceed, the following is needed:**
- Any direct preclinical or clinical evidence of nystatin in orbital disease
- Mechanism-of-action data and a rationale for the orbital site, including route feasibility (the available product is a topical ointment)
- Package insert warnings and contraindications for the local product

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for nystatin are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Nystatin Oral Suspension (nystatin) prescribing information, Xttrium Laboratories, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4a670371-d373-1ba6-e063-6394a90a13b6) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

