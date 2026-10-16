---
layout: default
title: Raltegravir
parent: Moderate Evidence (L3-L4)
nav_order: 721
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Raltegravir: predicted new indication Simian immunodeficiency virus infection (evidence level L4). Approved use: HIV infection, AIDS"
monitor_inn: "Raltegravir"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Raltegravir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Raltegravir: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Raltegravir is an HIV-1 integrase inhibitor, originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**,
but there are **no registered clinical trials** and the **15 publications** compiled for this report are almost entirely preclinical (animal and laboratory) studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection, AIDS |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Raltegravir is an integrase strand transfer inhibitor (INSTI). It blocks the step in which HIV-1 inserts its genetic material into the host cell's DNA. Detailed mechanism-of-action data were not available in the data compiled for this report, but this is the well-known class mechanism.

SIV is a close lentiviral relative of HIV and carries a homologous integrase enzyme, so INSTIs are expected to inhibit it too. Preclinical work supports this. In SIV-infected macaques, regimens built around raltegravir suppressed viral replication, and studies of resistance mutations showed that SIV responds to integrase inhibitors in a similar way to HIV.

There is an important limitation. SIV infection is a veterinary and research-model condition, not a human therapeutic indication. It is essentially an extension of the approved HIV indication and offers little new repurposing value for human patients. Its main use is as a preclinical surrogate for studying HIV.

Two other predictions were also generated, and neither has supporting evidence:
- **Feline acquired immunodeficiency syndrome** (score 99.78%): the FIV integrase is plausibly related to HIV's, but no trials or literature were found. The high score likely reflects network similarity to the HIV and SIV indications rather than independent evidence.
- **A genetic neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 99.77%): no mechanistic link to integrase inhibition was identified. The score is likely a graph-based artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The 15 publications compiled for this report are preclinical; none is an RCT or a human clinical study. The most relevant ones are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20233398](https://pubmed.ncbi.nlm.nih.gov/20233398/) | 2010 | Preclinical (animal model) | Retrovirology | Raltegravir plus two nucleoside/nucleotide reverse transcriptase inhibitors worked as a new treatment approach in SIVmac251-infected macaques, providing a model for studying viral persistence |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal study | PLoS Pathogens | A highly intensified multidrug regimen gave long-term viral suppression and restricted the viral reservoir in a simian AIDS model |
| [24622515](https://pubmed.ncbi.nlm.nih.gov/24622515/) | 2014 | Preclinical (animal model) | Science Translational Medicine | Topical integrase inhibitors protected macaques from vaginal SHIV infection when given after exposure |
| [29643246](https://pubmed.ncbi.nlm.nih.gov/29643246/) | 2018 | Preclinical (animal model) | Journal of Virology | Studied 2-LTR circle dynamics in SIV-infected macaques treated with an integrase inhibitor, with and without CD8+ cells |
| [29466356](https://pubmed.ncbi.nlm.nih.gov/29466356/) | 2018 | Preclinical (animal model) | PLoS One | Resistance mutations emerged in SIV-infected macaques on non-suppressive therapy that included raltegravir intensification |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Preclinical (animal model) | mBio | Lentiviral infection persisted in the brain despite effective antiretroviral therapy |
| [24920794](https://pubmed.ncbi.nlm.nih.gov/24920794/) | 2014 | Preclinical (in vitro) | Journal of Virology | HIV-1 integrase resistance mutations introduced into SIVmac239 changed susceptibility to INSTIs |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | Preclinical (in vitro) | Journal of Virology | SIVmac239 developed resistance mutations to INSTIs that were similar to those seen in HIV |
| [25583721](https://pubmed.ncbi.nlm.nih.gov/25583721/) | 2015 | Preclinical (in vitro) | Antimicrob Agents Chemother | Simian-tropic HIV proposed as a model for studying integrase inhibitor resistance |
| [32166319](https://pubmed.ncbi.nlm.nih.gov/32166319/) | 2020 | Preclinical (in vitro) | Clin Infect Dis | Dolutegravir and raltegravir showed proadipogenic and profibrotic effects and induced insulin resistance in human and simian adipose tissue and in human adipocytes |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 247013 | Zepdon 400mg Tablet (Cipla Ltd) | Bottle of 60 tablets | Not stated in the available data |
| 108290 | Isentress 400mg Tablet (MSD Pharmaceuticals Pvt Ltd) | Bottle of 60 tablets | Not stated in the available data |

## Safety Considerations

- **Disease associations from the knowledge graph** (these come from graph data, not label text): myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, rhabdomyolysis, and nodular fasciitis are flagged as contraindication-type associations.
- **Drug Interactions**: 36 interactions were identified in total. Among the 20 reviewed:
  - **Major**: zinc sulfate, zinc acetate, aluminum hydroxide, calcium carbonate. These are polyvalent-cation products, which can reduce raltegravir absorption.
  - **Moderate**: magnesium oxide, magnesium sulfate, magnesium chloride, orlistat.
  - **Minor**: acid-reducing drugs (famotidine, ranitidine, cimetidine, nizatidine, omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole), pioglitazone, and dexamethasone.

Package insert warnings and contraindications were not available, so please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic fit with SIV is strong, but the evidence is entirely preclinical (L4), and SIV infection is a research-model condition rather than a human indication. It adds little repurposing value beyond the already approved HIV indication. The other two predictions have no supporting evidence at all.

**To proceed, the following is needed:**
- Clarify whether SIV or FIV infection has any real therapeutic use, such as veterinary development, or whether it should only be treated as a research model
- Detailed mechanism of action data
- Package insert warnings and contraindications from the India Pharma source
- Review of the knowledge-graph muscle-related contraindication signals against the approved label
- Look for repurposing candidates with human disease relevance, rather than relying on these high-scoring but non-human or unsupported predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

