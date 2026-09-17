---
layout: default
title: Topiramate
parent: Moderate Evidence (L3-L4)
nav_order: 841
evidence_level: L3
indication_count: 9
---

# Topiramate
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **9** 
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

# Topiramate: From Broad-Spectrum Epilepsy Treatment to Visual Epilepsy (and Related Reflex Seizure Subtypes)

## One-Sentence Summary

> Topiramate is a well-established broad-spectrum antiepileptic drug. This evidence pack screened **9 candidate indications** via TxGNN, most representing rare reflex-epilepsy subtypes rather than a wholly new disease area.
> The strongest signal is **Visual Epilepsy**, supported by **4 clinical trials** and **20 publications** (Evidence Level L3), while several other candidates (e.g., trigeminal nerve neoplasm, orgasm-induced seizures) have **zero supporting evidence** and are flagged in the data itself as likely false-positive pairings.

---

## Quick Overview

*(For the lead candidate — Visual Epilepsy — the strongest evidenced prediction in this pack)*

| Item | Content |
|------|------|
| Original Indication | Not available — Topiramate is not currently marketed in India, so no approved indication text exists in this evidence pack. Its established use as a broad-spectrum antiepileptic is referenced throughout the supporting evidence. |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Screened Candidates Overview

TxGNN returned 9 disease candidates for Topiramate. Evidence strength varies enormously — most are ultra-rare reflex-epilepsy subtypes with no dedicated literature:

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------------|-----------------|-----------------|-----------------|
| 1 | Trigeminal nerve neoplasm | 99.70% | L5 | S0 | Hold |
| 2 | **Visual epilepsy** | 99.28% | **L3** | S2 | **Proceed with Guardrails** |
| 3 | Eating seizures | 99.21% | L4 | S0 | Hold |
| 4 | Orgasm-induced seizures | 99.21% | L5 | S0 | Hold |
| 5 | Audiogenic seizures | 99.21% | L4 | S1 | Research Question |
| 6 | **Thinking seizures** | 99.21% | **L3** | S2 | **Proceed with Guardrails** |
| 7 | Micturition-induced seizures | 99.21% | L5 | S0 | Hold |
| 8 | Startle epilepsy | 99.21% | L5 | S0 | Hold |
| 9 | Reading seizures | 99.09% | L3 | S1 | Research Question |

**Note on Rank 1**: The top-scored candidate, "trigeminal nerve neoplasm," has no clinical trial or literature evidence at all, and the evidence pack's own mechanistic rationale explicitly labels it as "a probable false-positive pairing from the KG algorithm." It is not carried forward as the report's primary subject.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for Topiramate is not available in this evidence pack (flagged as Data Gap DG002, High severity). Based on the evidence that *is* available, Topiramate is consistently described across trials and literature as a **broad-spectrum antiepileptic drug** acting through multiple mechanisms — voltage-gated sodium channel blockade, GABA-A potentiation, AMPA/kainate receptor antagonism, and carbonic anhydrase inhibition.

The candidates in this pack are not a genuinely new therapeutic area — they are largely **reflex epilepsy subtypes** (seizures triggered by specific stimuli such as light, sound, reading, or eating) that fall within the broader epilepsy spectrum Topiramate already treats. For **Visual Epilepsy** specifically, the underlying rationale states: *"Topiramate's broad-spectrum antiepileptic mechanism (multi-channel/receptor modulation) is already established to suppress multiple seizure types; photosensitive/visually-triggered epilepsy represents an extension subtype within its existing indication scope, rather than a novel mechanistic hypothesis."*

This is corroborated by supporting trial data: a large completed Phase 3 RCT (NCT00231556, n=750) demonstrates efficacy of topiramate monotherapy in newly diagnosed/recurrent epilepsy, and the SANAD RCT (PMID 17382828, Lancet 2007) confirms topiramate's efficacy across generalized/unclassifiable seizure types — the same broad category that visual, thinking, and reading-triggered seizures fall under. The mechanistic plausibility is therefore high, though no trial to date has specifically isolated the visually-triggered subtype as a primary endpoint.

---

## Clinical Trial Evidence

*(Visual Epilepsy candidate)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00231556](https://clinicaltrials.gov/study/NCT00231556) | Phase 3 | Completed | 750 | Randomized, double-blind, monotherapy trial comparing two topiramate doses in newly diagnosed/recurrent epilepsy — high-quality direct evidence for broad-spectrum efficacy, though not visual-epilepsy specific. |
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Prospective observational "Liceo Study" assessing new AEDs (including topiramate) as first-choice bitherapy in focal epilepsy. |
| [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Phase 4 | Unknown | 40 | Study of levetiracetam for neonatal seizures; topiramate mentioned as an emerging alternative AED — only indirectly relevant. |
| [NCT03803046](https://clinicaltrials.gov/study/NCT03803046) | N/A | Terminated | 1 | Terminated pediatric study on cognitive impact of benzodiazepine withdrawal after epilepsy surgery — low relevance to topiramate/visual epilepsy specifically. |

---

## Literature Evidence

*(Visual Epilepsy candidate, prioritized RCT > Systematic Review > Review > Cohort)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17382828](https://pubmed.ncbi.nlm.nih.gov/17382828/) | 2007 | RCT | Lancet | SANAD trial: compares valproate, lamotrigine, and topiramate in generalized/unclassifiable epilepsy — long-term effectiveness data. |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematic Review/NMA | J Neurology | Network meta-analysis of antiseizure medications (incl. topiramate) for idiopathic generalized epilepsies. |
| [34817852](https://pubmed.ncbi.nlm.nih.gov/34817852/) | 2021 | Cochrane Review | Cochrane Database Syst Rev | Updated systematic review of topiramate for juvenile myoclonic epilepsy (JME). |
| [15811478](https://pubmed.ncbi.nlm.nih.gov/15811478/) | 2005 | Review | Clinical Therapeutics | Efficacy of topiramate monotherapy for epilepsy and migraine prevention; dosing/titration guidance. |
| [29424067](https://pubmed.ncbi.nlm.nih.gov/29424067/) | 2018 | Cohort | Clin Exp Pharmacol Physiol | Cross-sectional study on topiramate plasma concentration and seizure frequency in drug-resistant epilepsy. |
| [35421622](https://pubmed.ncbi.nlm.nih.gov/35421622/) | 2022 | Review | Seizure | Molecular mechanisms of topiramate and its clinical value in epilepsy, including comorbidities (migraine, obesity). |
| [18193927](https://pubmed.ncbi.nlm.nih.gov/18193927/) | 2008 | Review | CNS Drugs | "Spotlight on topiramate in epilepsy" — established efficacy in generalized tonic-clonic, partial, and Lennox-Gastaut seizures. |
| [17641254](https://pubmed.ncbi.nlm.nih.gov/17641254/) | 2007 | Double-blind study | J Child Neurology | Topiramate monotherapy in 470 newly diagnosed pediatric/adolescent epilepsy patients, incl. 151 children 6–15 yrs. |
| [33350762](https://pubmed.ncbi.nlm.nih.gov/33350762/) | 2020 | Prospective Study | Medicine | Effectiveness of dose-escalated topiramate mono/add-on therapy in neurosurgery-related epilepsy. |
| [10530697](https://pubmed.ncbi.nlm.nih.gov/10530697/) | 1999 | Review | Epilepsia | Early review establishing topiramate efficacy as adjunctive/monotherapy across multiple seizure types. |

---

## India Market Information

Topiramate is currently **not marketed in India** (0 registrations on file in this evidence pack). No approved indication text is available for comparison against the predicted new indication.

---

## Safety Considerations

**Drug Interactions**: The evidence pack records **187 total interactions**. Among the sampled entries, the following are classified as **Major**:

- Metformin, Hyoscyamine, Atropine, Scopolamine, Glycopyrronium, Clidinium, Dicyclomine, Mepenzolate, Methscopolamine, Propantheline, Trospium

Moderate-level interactions in the sample include Pioglitazone, Morphine, Dronabinol, Phentermine, Metoclopramide, Glyburide, and others. Many of the Major interactions cluster around **anticholinergic agents**, consistent with topiramate's known metabolic acidosis/carbonic anhydrase inhibition profile warranting caution in combination therapy.

Key warnings and contraindications from the official package insert are **not yet available** in this evidence pack (Data Gap DG001, Blocking severity) — please refer to the official label once retrieved.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(for the Visual Epilepsy / Thinking Seizures cluster — L3 evidence, S2 decision stage)*

**Rationale:**
- Visual epilepsy and thinking-induced seizures are supported by multiple Phase 3/4 trials and Cochrane-level systematic reviews confirming topiramate's broad-spectrum antiepileptic efficacy, and they fall within its existing mechanistic indication scope rather than requiring a novel efficacy hypothesis.
- The remaining 6 of 9 candidates (trigeminal nerve neoplasm, orgasm-induced, micturition-induced, and startle-induced seizures) have **no clinical or literature evidence** and should remain on **Hold** — they appear to be low-confidence KG artifacts rather than genuine repurposing signals.

**To proceed, the following is needed:**
- TFDA/regulatory package insert (warnings & contraindications) — currently a **Blocking** data gap that prevents safety pre-assessment (S1)
- Detailed mechanism of action (MOA) data from DrugBank
- Reflex-epilepsy-subtype-specific trial data (visual/photosensitive, cognitive, or reading-triggered seizures currently lack dedicated prospective trials — existing evidence is extrapolated from general epilepsy populations)
- India market entry assessment, since the product currently holds zero local registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

