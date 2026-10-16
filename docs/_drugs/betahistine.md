---
layout: default
title: Betahistine
parent: Model Prediction Only (L5)
nav_order: 105
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Betahistine: predicted new indication Restless legs syndrome (evidence level L5). Approved use: Meniere disease, endolymphatic hydrops"
monitor_inn: "Betahistine"
predicted_indications: ["restless legs syndrome", "active cochlear Meniere disease", "active vestibular Meniere disease", "active cochleovestibular Meniere disease", "otosclerosis", "peripheral vertigo", "age-related hearing impairment", "vertigo, benign recurrent, 2", "autosomal recessive hyperinsulinism due to Kir6.2 deficiency", "hyperinsulinemic hypoglycemia, familial"]
---

# Betahistine
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

# Betahistine: From Meniere Disease to Restless Legs Syndrome

## One-Sentence Summary

Betahistine is a histamine-analogue drug originally used to treat Meniere disease and endolymphatic hydrops.
The TxGNN model's top-ranked prediction is **restless legs syndrome**, but this is a model prediction only, with **no clinical trials and no publications** behind it.
The better-supported predictions are on-label or close to it, such as **peripheral vertigo**, which has a randomized trial, a meta-analysis and Cochrane reviews.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Meniere disease, endolymphatic hydrops |
| Predicted New Indication | Restless legs syndrome (rank 1) |
| TxGNN Prediction Score | 98.51% |
| Evidence Level | L5 (for the top-ranked indication) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold (top-ranked indication); Proceed with Guardrails for peripheral vertigo and vestibular Meniere disease |

Other predicted indications in the data compiled for this report:

| Rank | Predicted Indication | Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 2 | Active cochlear Meniere disease | 98.34% | L4 | Research Question |
| 3 | Active vestibular Meniere disease | 98.34% | L3 | Proceed with Guardrails |
| 4 | Active cochleovestibular Meniere disease | 98.34% | L5 | Hold |
| 5 | Otosclerosis | 98.19% | L4 | Hold |
| 6 | Peripheral vertigo | 98.07% | L2 | Proceed with Guardrails |
| 7 | Age-related hearing impairment | 97.93% | L5 | Hold |
| 8 | Vertigo, benign recurrent, 2 | 97.78% | L2 | Research Question |
| 9 | Autosomal recessive hyperinsulinism (Kir6.2 deficiency) | 97.77% | L5 | Hold |
| 10 | Hyperinsulinemic hypoglycemia, familial | 97.32% | L5 | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. From the literature supplied, betahistine is a weak histamine H1 receptor agonist and a stronger H3 receptor antagonist (inverse agonist). These actions are thought to increase inner-ear (cochlear) microcirculation and promote vestibular compensation.

For restless legs syndrome, the link is speculative. Central histaminergic signalling has been discussed in sleep-wake and dopaminergic regulation, but nothing in the supplied data supports it. The high score most likely reflects network relationships in the knowledge graph rather than direct biological evidence.

Several lower-ranked predictions are much better grounded. Active vestibular, cochlear and cochleovestibular Meniere disease are subtypes of the original indication. Peripheral vertigo and benign recurrent vertigo are closely related vestibular conditions where betahistine is already widely used. The hyperinsulinism predictions (ranks 9 and 10) have no apparent mechanistic connection to betahistine and are probably network artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications.

## Literature Evidence

No literature is available for the top-ranked indication (restless legs syndrome). The table below covers the best-supported prediction, **peripheral vertigo**.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26797774](https://pubmed.ncbi.nlm.nih.gov/26797774/) | 2016 | RCT | BMJ | BEMED trial: long-term, multicentre, double-blind, placebo-controlled, dose-defining study of betahistine in Meniere disease. A 2017 commentary (PMID 28850992) notes it did not show significantly fewer vertigo attacks than placebo |
| [36827524](https://pubmed.ncbi.nlm.nih.gov/36827524/) | 2023 | Systematic Review | Cochrane Database Syst Rev | Systemic pharmacological interventions for Meniere disease, including betahistine |
| [27327415](https://pubmed.ncbi.nlm.nih.gov/27327415/) | 2016 | Systematic Review | Cochrane Database Syst Rev | Betahistine versus placebo for vertigo symptoms of various causes |
| [23778722](https://pubmed.ncbi.nlm.nih.gov/23778722/) | 2014 | Meta-analysis | Eur Arch Otorhinolaryngol | Meta-analysis of 12 double-blind, placebo-controlled studies in vestibular vertigo and Meniere disease |
| [26245698](https://pubmed.ncbi.nlm.nih.gov/26245698/) | 2015 | Review | Acta Otolaryngol | Reports betahistine as effective and safe in Meniere disease, BPPV, vestibular neuronitis and other peripheral vertigo |
| [41487075](https://pubmed.ncbi.nlm.nih.gov/41487075/) | 2026 | RCT | J Otolaryngol Head Neck Surg | EGb 761 versus betahistine in dizziness/vertigo of unclear cause |
| [37000080](https://pubmed.ncbi.nlm.nih.gov/37000080/) | 2023 | Meta-analysis | Medicine | Epley maneuver plus betahistine in posterior canal BPPV |
| [41038567](https://pubmed.ncbi.nlm.nih.gov/41038567/) | 2025 | Systematic Review | Acta Otorrinolaringol Esp | Cinnarizine/dimenhydrinate combination versus betahistine in vertigo |
| [26688903](https://pubmed.ncbi.nlm.nih.gov/26688903/) | 2015 | Safety note | Prescrire Int | Report on hallucinations with betahistine |
| [25709150](https://pubmed.ncbi.nlm.nih.gov/25709150/) | 2014 | Clinical study | Acta Otorhinolaryngol Ital | Cinnarizine plus betahistine in Meniere disease patients poorly responsive to betahistine alone |

Supporting mechanistic work on the cochlear subtype: [26139562](https://pubmed.ncbi.nlm.nih.gov/26139562/) (2015, Audiol Neurootol) on H3-heteroreceptors and cochlear blood flow, and [28818391](https://pubmed.ncbi.nlm.nih.gov/28818391/) (2017, Life Sci) on a pericyte/precapillary arteriole mechanism. These are preclinical and are not clinical efficacy evidence.

## India Market Information

Betahistine is marketed in India as single-ingredient oral tablets, with 20 valid registrations and none cancelled. The approved-indication text is not recorded for any of them. The table lists five of the registrations.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 62543 | Dvert 16mg Tablet | Strip of 10 tablets | Lia Life Sciences Pvt Ltd |
| 246608 | Zevert 16 Tablet DT | Strip of 10 tablet DT | Intas Pharmaceuticals Ltd |
| 238299 | Vergone 48mg Tablet SR | Strip of 10 tablet SR | Ardent Life Sciences Pvt Ltd |
| 26551 | Bvert OD 24mg Tablet CR | Strip of 10 tablet CR | Icon Life Sciences |
| 26228 | B-Stil 16 Tablet | Strip of 10 tablets | Abbott |

Strengths across the 20 registrations range from 8 mg to 48 mg. Formulations include standard, dispersible (DT), sustained-release (SR) and controlled-release (CR) tablets.

## Safety Considerations

Please refer to the package insert for safety information. No label warnings, contraindications or drug-interaction records were available in the compiled data. A 2015 Prescrire note (PMID 26688903) raised the possibility of hallucinations with betahistine; this has not been assessed further here.

## Conclusion and Next Steps

**Decision: Hold** for the top-ranked prediction (restless legs syndrome). **Proceed with Guardrails** for peripheral vertigo and vestibular Meniere disease.

**Rationale:**
- Restless legs syndrome, age-related hearing impairment and the two hyperinsulinism entries have only a model score and no supporting trials or literature, so they should not move forward.
- Peripheral vertigo and vestibular Meniere disease have more evidence (a randomized trial, a meta-analysis and Cochrane reviews), but these are essentially on-label uses rather than true repurposing. The evidence is also mixed: the BEMED trial did not show a significant benefit over placebo for vertigo attacks.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulatory sources (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- For restless legs syndrome: any mechanistic or clinical rationale before further consideration
- For vertigo and Meniere disease: confirmation of dose-dependence and efficacy using clinical-trial-grade endpoints, while avoiding over-generalizing from Meniere disease to all peripheral vertigo
- For cochlear Meniere disease: clinical data on hearing and tinnitus outcomes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

