---
layout: default
title: Dexmedetomidine
parent: Model Prediction Only (L5)
nav_order: 254
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
description: "Dexmedetomidine: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not stated in the licence data (injectable dexmedetomidine is general…"
monitor_inn: "Dexmedetomidine"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "migraine disorder", "migraine with brainstem aura", "headache disorder", "trigeminal autonomic cephalalgia"]
---

# Dexmedetomidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Dexmedetomidine: From Sedation (Original Indication Not Specified in Licence Data) to nephrogenic syndrome of inappropriate antidiuresis
{: .text-alpha }

## One-Sentence Summary

Dexmedetomidine is an alpha-2 adrenergic agonist marketed in India as an injectable. It is used for sedation, although the licence data compiled for this report contain no approved indication text.
The TxGNN model's top-ranked prediction is **nephrogenic syndrome of inappropriate antidiuresis**, but this has no supporting evidence and a weak mechanistic rationale. The best-supported direction is **headache disorder** (rank 4), with **4 related clinical trials** (3 of them on post-dural puncture headache) and **2 randomized trials plus 1 systematic review** in the literature.

> Note: The sections below follow the top-ranked prediction as required by the report format. A short comparison with the better-supported headache and migraine predictions is included in the conclusion.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data (injectable dexmedetomidine is generally used for sedation) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9960 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 16 of 16) |
| Number of Registrations | 16 (valid: 16) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Dexmedetomidine is a selective alpha-2 adrenergic agonist. This class can suppress vasopressin release and promote water excretion (aquaresis), which is the only conceptual link to a condition of excess antidiuresis.

However, nephrogenic SIAD is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2), which act downstream of vasopressin secretion. Lowering vasopressin would not be expected to correct a receptor-level defect. The mechanistic rationale is therefore weak, and the prediction is likely a model artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered for nephrogenic syndrome of inappropriate antidiuresis.

For context, trials found for the better-supported predictions:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04910477](https://clinicaltrials.gov/study/NCT04910477) | Phase 3 | Completed | 90 | Nebulized dexmedetomidine vs neostigmine/atropine vs saline for post-dural puncture headache after cesarean section (headache disorder) |
| [NCT04327726](https://clinicaltrials.gov/study/NCT04327726) | NA | Completed | 43 | Nebulized dexmedetomidine for post-dural puncture headache in parturients (headache disorder) |
| [NCT06470854](https://clinicaltrials.gov/study/NCT06470854) | NA | Completed | 50 | Nebulized dexmedetomidine vs bilateral greater occipital nerve block for post-dural puncture headache (headache disorder) |
| [NCT07769255](https://clinicaltrials.gov/study/NCT07769255) | NA | Recruiting | 146 | Nebulized dexmedetomidine on central sensitization and chronification in migraine (migraine disorder) |

## Literature Evidence

Currently no related literature available for nephrogenic syndrome of inappropriate antidiuresis.

For context, the main publications for the headache disorder prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36651373](https://pubmed.ncbi.nlm.nih.gov/36651373/) | 2023 | RCT | Minerva Anestesiol | Nebulized dexmedetomidine vs neostigmine/atropine for post-dural puncture headache after cesarean section |
| [33993346](https://pubmed.ncbi.nlm.nih.gov/33993346/) | 2021 | RCT | J Anesth | Nebulized dexmedetomidine added to conservative PDPH management, with cerebral hemodynamics assessed by transcranial Doppler |
| [41120897](https://pubmed.ncbi.nlm.nih.gov/41120897/) | 2025 | Systematic review | BMC Anesthesiol | Meta-analysis of efficacy and safety of nebulized dexmedetomidine for PDPH after cesarean delivery |
| [39799300](https://pubmed.ncbi.nlm.nih.gov/39799300/) | 2025 | Case report | BMC Anesthesiol | Two cases of obstetric PDPH treated with nebulized dexmedetomidine |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 58943 | Dextomid 50mcg Injection | Vial of 1 ml injection | Not stated |
| 69363 | Dexglan 100mcg Injection | Vial of 2 ml injection | Not stated |
| 59924 | Dextomid 200mcg Injection | Vial of 2 ml injection | Not stated |
| 244099 | Xamdex 100mcg Injection | Vial of 2 ml injection | Not stated |
| 146844 | Medetofix 100 Injection | Ampoule of 1 ml injection | Not stated |

There are 16 valid single-ingredient registrations in total, all injectable.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease links, not label text): hypertensive disorder, hypertension, kidney disease, pyoureter, liver disease, gallbladder disease, diabetes mellitus, diabetic ketoacidosis, hypotensive disorder, atrioventricular block.
- **Drug Interactions**: 59 interactions were recorded. Moderate-level interactions include morphine (including liposomal), opium, dronabinol, nabilone, diphenoxylate, papaverine, sibutramine, ethanol, amyl nitrite, diazoxide and phentolamine. This is consistent with additive sedative or blood-pressure effects. Several others (e.g., pantoprazole, vancomycin, atropine) are of unknown severity.
- For brainstem-related headache subtypes, sedative and bradycardic effects could confound neurological assessment.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (nephrogenic SIAD) rests on a model score alone, with no trials or literature, and the mechanism is contradicted by the receptor-level cause of the disease. By contrast, headache disorder (L2, Research Question) has completed trials and two RCTs, but this evidence is limited to post-dural puncture headache, a secondary headache with distinct pathophysiology, so it does not support primary headache disorders. Migraine (L5, Research Question) has one recruiting trial (N=146) and only hypothesis-level support.

**To proceed, the following is needed:**
- India package insert warnings, contraindications and approved indications (a blocking data gap for safety screening)
- Mechanism of action data from DrugBank
- For headache: a larger multicentre confirmatory RCT of nebulized dexmedetomidine in post-dural puncture headache, and results from the migraine trial NCT07769255
- Route compatibility assessment: all Indian products are injectables, while the headache and migraine evidence uses a nebulized route
- No further work on nephrogenic SIAD unless a credible mechanistic or preclinical rationale emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

