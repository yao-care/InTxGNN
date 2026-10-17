---
layout: default
title: Ambrisentan
parent: Model Prediction Only (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ambrisentan: predicted new indication Pulmonary arteriovenous malformation (evidence level L5). Approved use: Pulmonary arterial hypertension"
monitor_inn: "Ambrisentan"
predicted_indications: ["pulmonary arteriovenous malformation (disease)", "malformation syndrome with odontal and/or periodontal component", "hypotrichosis simplex of the scalp", "hypertrichosis (disease)", "syndrome with a Dandy-Walker malformation as major feature"]
---

# Ambrisentan
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

# Ambrisentan: From Pulmonary Arterial Hypertension to Pulmonary Arterial Hypertension Associated with Connective Tissue Disease

## One-Sentence Summary

Ambrisentan is an oral endothelin receptor antagonist, originally used to treat pulmonary arterial hypertension (PAH).
The TxGNN model's top-ranked prediction is pulmonary arteriovenous malformation, but that prediction is weak. The best-supported candidate is **PAH associated with connective tissue disease**, which has **2 clinical trials** and **19 publications** behind it.
This subtype largely falls under the existing PAH indication, so it is better viewed as a subgroup refinement than a wholly new use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension |
| Predicted New Indication | Pulmonary arteriovenous malformation (TxGNN rank 1); PAH associated with connective tissue disease is the best-supported candidate (rank 4) |
| TxGNN Prediction Score | 99.41% (rank 1); 99.30% (rank 4) |
| Evidence Level | L5 for the rank 1 prediction (L4 per the data compiled; a single case report); L2 for the rank 4 candidate |
| India Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold for rank 1; Proceed with Guardrails for PAH associated with connective tissue disease |

Note: The original indication comes from the TxGNN knowledge graph. The Indian licence records contain no approved indication text.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on the literature, ambrisentan is a selective endothelin type A receptor antagonist. Endothelin-1 drives vasoconstriction and vascular remodelling in PAH, and its efficacy in PAH is established.

**Rank 1 (pulmonary arteriovenous malformation):** This prediction is not well supported. The only linked paper is a case report of PAH in a patient with hereditary haemorrhagic telangiectasia. It describes PAH occurring alongside a vascular malformation disorder and does not show that ambrisentan treats pulmonary AVMs. Endothelin receptor antagonism is not an established way to close or prevent AVMs. The high score probably reflects network proximity to PAH. There is also a theoretical caution that pulmonary vasodilation could alter shunt physiology.

**Rank 4 (PAH associated with connective tissue disease):** Endothelial dysfunction and endothelin-mediated vasoconstriction and remodelling are central to this subtype, including in systemic sclerosis. This is the same pathway ambrisentan blocks in its approved indication. Two clinical trials and several meta-analyses and subgroup analyses (including from the AMBITION and ARIES-E studies) support its use here.

Other PAH subtypes (congenital heart disease, HIV, schistosomiasis, chronic haemolytic anaemia) share the same pathway. Their evidence ranges from small observational studies to nothing at all. The remaining predictions (malformation syndrome with odontal/periodontal component, hypotrichosis simplex, hypertrichosis, Dandy-Walker syndrome) have no plausible mechanism and are likely model artifacts.

## Clinical Trial Evidence

Trials linked to the best-supported candidate, PAH associated with connective tissue disease. No clinical trials are registered for the rank 1 prediction or for the other predictions.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02290613](https://clinicaltrials.gov/study/NCT02290613) | Phase 2 | Completed | 38 | Randomised, double-blind, placebo-controlled proof-of-concept trial of early treatment in borderline PAH associated with systemic sclerosis |
| [NCT01042158](https://clinicaltrials.gov/study/NCT01042158) | Phase 4 | Completed | 25 | 36-week open-label single-arm study of ambrisentan plus tadalafil in scleroderma-associated PAH, assessing 6-minute walk distance, NYHA class and haemodynamics |

## Literature Evidence

Selected publications for PAH associated with connective tissue disease, plus the single paper linked to the rank 1 prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic review/meta-analysis | Intern Emerg Med | Meta-analysis of RCT subgroup data on treatments for PAH in connective tissue disease |
| [23906950](https://pubmed.ncbi.nlm.nih.gov/23906950/) | 2013 | Meta-analysis | BMJ Open | Meta-analysis of clinical trials in connective tissue disease-associated PAH; the optimal treatment is not yet established |
| [32161055](https://pubmed.ncbi.nlm.nih.gov/32161055/) | 2020 | Post hoc analysis | Ann Rheum Dis | Initial ambrisentan plus tadalafil combination versus monotherapy in connective tissue disease-associated PAH (AMBITION) |
| [28039187](https://pubmed.ncbi.nlm.nih.gov/28039187/) | 2017 | Subgroup analysis | Ann Rheum Dis | AMBITION subgroup analysis of initial combination therapy in connective tissue disease-associated PAH |
| [27492539](https://pubmed.ncbi.nlm.nih.gov/27492539/) | 2016 | Subgroup analysis | Respir Med | Three-year efficacy and safety of ambrisentan in connective tissue disease-associated PAH (ARIES-E) |
| [26360334](https://pubmed.ncbi.nlm.nih.gov/26360334/) | 2015 | Clinical study | Am J Respir Crit Care Med | Up-front ambrisentan and tadalafil combination in scleroderma-associated PAH |
| [28425346](https://pubmed.ncbi.nlm.nih.gov/28425346/) | 2017 | Review | Ther Adv Respir Dis | Drug profile; ambrisentan is approved for idiopathic, heritable and connective tissue disease-associated PAH |
| [21371683](https://pubmed.ncbi.nlm.nih.gov/21371683/) | 2011 | Cohort | Am J Cardiol | Ambrisentan in PAH due to congenital heart disease (Eisenmenger syndrome); early experience (congenital heart disease subtype) |
| [34921523](https://pubmed.ncbi.nlm.nih.gov/34921523/) | 2022 | Cohort/safety study | Pediatr Pulmonol | Safety and tolerability of ambrisentan plus tadalafil in children with PAH (congenital heart disease subtype) |
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Case report | World J Clin Cases | PAH in a patient with hereditary haemorrhagic telangiectasia; not evidence that ambrisentan treats pulmonary AVMs (rank 1 prediction) |

## India Market Information

Ten valid single-ingredient registrations are on record; the five main ones are shown. None of the records carries approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 72527 | Endobloc T Combipack (Cipla Ltd) | Packet of 20 tablets | Not stated |
| 247591 | Zambri 5mg Tablet (Zydus Cadila) | Strip of 10 tablets | Not stated |
| 611 | Ambrican 5 Tablet (Lupin Ltd) | Strip of 10 tablets | Not stated |
| 249050 | Zambri 10mg Tablet (Zydus Cadila) | Strip of 10 tablets | Not stated |
| 109448 | Ibitan 5mg Tablet (Indiabulls Pharmaceutical Ltd) | Strip of 10 tablets | Not stated |

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** congestive heart failure, anaemia, macrocytic anaemia, pulmonary veno-occlusive disease.
- **Embryo-fetal toxicity:** Ambrisentan is teratogenic (boxed warning), which makes it inappropriate for developmental disorders.
- **Fluid retention and anaemia:** These are known adverse effects and need careful consideration in haemolytic anaemia populations and in connective tissue disease.
- **Drug Interactions:** 112 interactions were recorded. Moderate-level interactions include canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, eliglustat and naltrexone. Minor-level interactions include clarithromycin, miconazole and omeprazole. Interactions with antiretrovirals should be assessed before use in HIV-associated PAH.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold for pulmonary arteriovenous malformation (rank 1); Proceed with Guardrails for PAH associated with connective tissue disease (rank 4)**

**Rationale:**
- The top-ranked prediction rests on one case report, has no plausible mechanism and carries a theoretical shunt-physiology concern, so it should not advance.
- PAH associated with connective tissue disease has two completed small trials, meta-analyses and AMBITION/ARIES-E subgroup data. It is already covered by the general PAH indication, so the remaining work is subgroup-specific.
- PAH associated with congenital heart disease (L3) and HIV (L4) are research questions based on observational evidence only. PAH associated with chronic haemolytic anaemia or schistosomiasis, and the non-PAH predictions, have no supporting evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian licence holders (currently missing; this blocks safety screening)
- Mechanism of action data from DrugBank
- Subgroup-specific monitoring plan for fluid retention and coexisting interstitial lung disease in connective tissue disease
- A Phase 3 or larger randomised study specific to connective tissue disease-associated PAH, if a formal new indication is sought
- Antiretroviral interaction assessment if HIV-associated PAH is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

