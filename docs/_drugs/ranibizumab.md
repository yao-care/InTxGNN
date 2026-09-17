---
layout: default
title: Ranibizumab
parent: High Evidence (L1-L2)
nav_order: 718
evidence_level: L1
indication_count: 10
---

# Ranibizumab
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Ranibizumab: From Anti-VEGF Ophthalmic Therapy to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Ranibizumab is an anti-VEGF-A Fab fragment used in ophthalmology to suppress pathological neovascularization and vascular permeability; the evidence pack does not document a specific Taiwan-approved original indication, as the drug currently holds **no marketing authorization in Taiwan**.
> The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy (NPDR)**,
> with **0 registered clinical trials in this evidence pack** but **19 supporting publications**, including a 2025 Phase 3 RCT (the Pavilion trial) conducted specifically in this population.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack — drug not yet marketed in Taiwan |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The formal `original_moa` field in this evidence pack is a data gap, but the underlying mechanism is well characterized from supporting evidence: Ranibizumab is a recombinant humanized anti-VEGF-A Fab fragment. VEGF-A is the central driver of neovascularization and vascular permeability increase in diabetic retinopathy — the same pathway ranibizumab was designed and clinically validated to block.

Severe NPDR sits on the same disease continuum as the indications ranibizumab has already been extensively studied in (diabetic macular edema, proliferative diabetic retinopathy), sharing an identical VEGF-driven pathophysiology. Landmark Phase 3 trial programs — RIDE/RISE, DRCR Protocol S/Protocol I — have already demonstrated that anti-VEGF therapy slows or reverses diabetic retinopathy severity scores, and this mechanistic link is directly reinforced by the 2025 Pavilion RCT, which tested a ranibizumab-specific delivery system in NPDR without macular edema.

It is worth noting that in several jurisdictions, anti-VEGF therapy (including ranibizumab) is already an approved option for severe NPDR — meaning this is less a novel "drug repurposing" hypothesis and more a case where local (Taiwan) regulatory and evidence documentation has not caught up with an already mechanistically and clinically validated use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this evidence pack. (Note: pivotal trial data — e.g., the Pavilion RCT and RIDE/RISE — is present in the Literature Evidence section below rather than as structured clinical trial records.)

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmology | Pavilion RCT: refillable port delivery system for continuous intravitreal ranibizumab release vs monitoring alone in NPDR without macular edema |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2024 | Systematic Review/Meta-analysis | Health Technol Assess | Anti-VEGF agents vs laser photocoagulation across the diabetic retinopathy spectrum |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | Cohort (RIDE/RISE post-hoc RCT analysis) | Clin Ophthalmol | Identifies predictors of early DR regression with ranibizumab in RIDE/RISE trials |
| [35417296](https://pubmed.ncbi.nlm.nih.gov/35417296/) | 2022 | Cohort (RIDE/RISE post-hoc) | Ophthalmic Surg Lasers Imaging Retina | Characterizes natural DR progression in untreated fellow eyes, supporting anti-VEGF treatment rationale |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | Cohort (RIDE/RISE open-label extension) | BMJ Open Ophthalmol | Effect of less-aggressive ranibizumab dosing on DR Severity Scale (DRSS) scores |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | RCT extension (DRCR Protocol I, 5-year) | Retina | 5-year changes in DR severity in eyes treated with ranibizumab for DME |
| [28448655](https://pubmed.ncbi.nlm.nih.gov/28448655/) | 2017 | Secondary analysis of RCT | JAMA Ophthalmology | 2-year DR change comparing aflibercept, bevacizumab, and ranibizumab |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opin Biol Ther | Overview of ranibizumab's efficacy in diabetic retinopathy |
| [40347224](https://pubmed.ncbi.nlm.nih.gov/40347224/) | 2025 | Systematic Review/Economic Analysis | Health Technol Assess | Companion economic analysis of anti-VEGF vs laser photocoagulation in DR |
| [31669065](https://pubmed.ncbi.nlm.nih.gov/31669065/) | 2019 | Review | J Diabetes Complications | Advances in DR treatment, including the role of VEGF-A blockade |

---

## Taiwan Market Information

Ranibizumab currently holds **no marketing authorization in Taiwan** (market status: Not marketed / Not Marketed; 0 registered licenses). No product registration records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-interaction data were all flagged as data gaps in this evidence pack — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is strong and independently validated by Phase 3-level RCT evidence (Pavilion trial, RIDE/RISE, DRCR Protocol I/S) directly in diabetic retinopathy populations, and anti-VEGF therapy for severe NPDR is already an approved indication in several other jurisdictions. However, the drug is not currently marketed in Taiwan, and Taiwan-specific safety documentation (TFDA label warnings/contraindications) is an unresolved **Blocking** data gap (DG001), which must be closed before any Taiwan-market clinical or regulatory action.

**To proceed, the following is needed:**
- Obtain and parse the TFDA package insert (warnings, contraindications) — Blocking gap DG001
- Complete formal MOA documentation via DrugBank API — High-priority gap DG002
- Assess Taiwan market-entry pathway (new registration, since 0 licenses currently exist)
- Confirm route/formulation compatibility for intravitreal administration in the local regulatory context

**Note on other candidates:** Nine additional candidates in this evidence pack (various cataract subtypes and hemorrhagic disease of newborn) were also screened but classified **Hold** — they lack biological plausibility relative to ranibizumab's anti-VEGF mechanism and have little to no supporting literature; several appear to reflect diabetes-comorbidity clustering noise in the knowledge graph rather than genuine causal signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

