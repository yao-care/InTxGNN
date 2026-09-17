---
layout: default
title: Tenofovir Disoproxil
parent: Moderate Evidence (L3-L4)
nav_order: 811
evidence_level: L3
indication_count: 4
---

# Tenofovir Disoproxil
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **4** 
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

Using no additional skill — this is a direct content-generation task against an explicit template (report prompt), not a coding/debugging/brainstorming task.

I reviewed the evidence pack in detail. A few things stand out that the report needs to state plainly rather than paper over: `original_indications` is empty and `original_moa` is a data gap, `taiwan_regulatory` shows the drug is **not marketed** (0 licenses), safety data is entirely a data gap flagged as **Blocking** (DG001), and — most importantly — the top-ranked "predicted indication" (`simian immunodeficiency virus infection`) is an **animal-model disease ontology term, not a human clinical indication**; the evidence pack's own `repurposing_rationale` says so explicitly. I'm reflecting this honestly in the report rather than guessing at real-world MOA/indication data not present in the pack.

---

# Tenofovir Disoproxil: From Undocumented Original Indication to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Tenofovir disoproxil's original indication is not documented in this evidence pack (the drug is currently **not marketed** in the covered registry, with 0 licenses on file). The TxGNN model's top-ranked association is with **Simian Immunodeficiency Virus Infection (SIV)** — a veterinary/animal-model disease entity rather than a human clinical indication — supported by **2 low-relevance clinical trials** and **20 publications**, nearly all of which are non-human macaque challenge studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented (no license records found; `original_indications` is empty in this evidence pack) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection (animal-model disease entity) |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| India/Taiwan Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for tenofovir disoproxil in this evidence pack (`original_moa` is a documented data gap). Based on the supporting evidence attached to this prediction, tenofovir is a nucleotide reverse transcriptase inhibitor (NRTI) that blocks reverse transcriptase activity. SIV, like HIV, belongs to the *Lentivirus* genus, which gives the underlying mechanistic analogy some biological plausibility — tenofovir's reverse-transcriptase-inhibiting mechanism is not species-specific to HIV.

However, the evidence pack itself flags an important caveat that this report must surface rather than obscure: **"simian immunodeficiency virus infection" is a disease-ontology term describing an animal model, not a human clinical indication.** The scientifically meaningful, translatable signal buried in this prediction is tenofovir's established role in **HIV pre-exposure prophylaxis (PrEP)** — an indication that is already part of tenofovir's approved clinical use, not a genuinely novel repurposing opportunity. The clinical trials and macaque-challenge literature returned here largely represent supporting mechanistic/preclinical evidence for that existing PrEP use, rather than evidence for a new human disease target.

A structurally similar issue affects the model's rank-2 candidate ("feline acquired immunodeficiency syndrome," a veterinary FIV indication) and ranks 3–4, which have no supporting evidence at all (L5, one against an obsolete disease term). This pattern suggests the current TxGNN disease vocabulary is not adequately filtered to exclude non-human disease ontology terms for this drug, and the resulting top-ranked predictions should be treated as a knowledge-graph topology artifact rather than a genuine new-indication signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | N/A | Withdrawn | 0 | HIV decay-kinetics study using raltegravir (not tenofovir); withdrawn. Graded C relevance — unrelated to SIV or tenofovir specifically. |
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Vedolizumab + ART for HIV virological remission in humans; small n, status unknown. Graded C relevance — not an SIV or tenofovir-specific trial. |

Both trials returned by the search were graded **C (low relevance)** by the evidence classifier — neither directly studies tenofovir in an SIV context.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20874040](https://pubmed.ncbi.nlm.nih.gov/20874040/) | 2010 | RCT (Human PrEP), Tier 1 | Pharmacotherapy | Review of systemic PrEP rationale for HIV prevention — the only tier-1, human-relevant reference in the evidence set |
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Animal Model (Macaque) | Nature Communications | Early ART initiation with long-acting TAF/FTC + cabotegravir/rilpivirine achieved SHIV remission in macaques |
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Animal Model (Macaque) | J Infect Dis | TAF/elvitegravir vaginal inserts gave extended post-exposure protection against SHIV in macaques |
| [36477356](https://pubmed.ncbi.nlm.nih.gov/36477356/) | 2022 | Animal Model (Macaque), Tier 2 | JCI Insight | Hypo-osmolar rectal tenofovir douche prevented SHIV acquisition in macaques |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Animal Model (Macaque) | J Infect Dis | Oral TAF ± FTC prevented vaginal SHIV infection in macaques |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Animal Model (Macaque), Tier 2 | J Infect Dis | Oral FTC + TAF chemoprophylaxis protected macaques from rectal SHIV infection |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Animal Model (Macaque), Tier 2 | J Infect Dis | FTC/TDF prevented vaginal SHIV infection in macaques even with concurrent chlamydia/trichomonas co-infection |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Animal Model (Macaque), Tier 2 | J Infect Dis | FTC/TDF prophylaxis remained effective against a tenofovir-resistant (K65R) SHIV strain in macaques |
| [22072766](https://pubmed.ncbi.nlm.nih.gov/22072766/) | 2012 | Animal Model (Macaque), Tier 2 | J Virology | 1% tenofovir vaginal gel gave durable protection against SHIV in macaques, correlated with tissue drug levels |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | Animal Model (Infant Macaque) | J Acquir Immune Defic Syndr | Oral TDF and topical tenofovir prodrug protected infant macaques from repeated oral SIV challenge (mother-to-infant transmission model) |

All literature except the single 2010 human-PrEP review is drawn from non-human macaque SHIV/SIV challenge models — consistent, mechanistically informative preclinical evidence, but not direct human clinical evidence for a "new indication."

---

## India/Taiwan Market Information

No license records are available for tenofovir disoproxil in this evidence pack — `taiwan_regulatory.licenses` is empty and `market_status` is recorded as **Not marketed (Not Marketed)**, with 0 total registrations. No product-level authorization table can be produced from the data provided.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** `key_warnings`, `contraindications`, and DDI data are all unavailable in this evidence pack. This has been flagged internally as a **Blocking** data gap (missing official label warnings/contraindications), which prevents a preliminary safety assessment (S1) for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked "new indication" (SIV infection) is an animal-model disease-ontology term, not a human clinical indication — it does not represent a genuine repurposing opportunity as framed, and the underlying translatable signal (HIV PrEP) is already an existing use of tenofovir rather than novel.
- A **Blocking**-severity data gap exists on official label warnings/contraindications, which prevents any preliminary safety evaluation (S1) regardless of indication merit.
- Mechanism-of-action data is missing, and the drug currently has zero market registrations in the covered registry.
- Ranks 2–4 in this same prediction set are similarly problematic (a veterinary FIV indication with no clinical evidence, and two L5 candidates with no supporting evidence at all, one against an obsolete disease term) — indicating a systematic disease-vocabulary filtering issue for this drug rather than isolated noise.

**To proceed, the following is needed:**
- Resolve DG001: obtain official label warnings/contraindications (TFDA or equivalent) before any safety pre-assessment can begin
- Resolve DG002: retrieve confirmed MOA from DrugBank to support mechanistic-link analysis
- Re-run disease mapping with a human-disease-only filter (e.g., restrict to MONDO/ICD-11 human clinical terms) to exclude animal-model ontology artifacts like SIV/FIV from the candidate list
- If HIV PrEP expansion is the intended real-world target, reframe the candidate against the actual human indication and pull evidence specific to that indication rather than the SIV proxy term
- Confirm current registration/licensing status and pathway if this drug is being considered for market entry under any indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

