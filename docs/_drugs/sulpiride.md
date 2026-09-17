---
layout: default
title: Sulpiride
parent: Model Prediction Only (L5)
nav_order: 792
evidence_level: L5
indication_count: 9
---

# Sulpiride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

Using the drug-repurposing-report template directly (no coding/debugging skill applies here — this is a pure content-generation task against a fully specified format).

---

# Sulpiride: From Schizophrenia/Depression to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

> Sulpiride is a D₂/D₃ dopamine receptor antagonist historically used for schizophrenia, depression, and anxiety (never FDA/EMA-approved; not currently marketed in India).
> The TxGNN model's top prediction is **Retinal Dystrophy with or without Extraocular Anomalies**, a rare congenital eye disorder,
> but this is supported by **0 clinical trials** and **no literature that actually links Sulpiride to the disease** — the strongest available "evidence" is a high model confidence score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in India regulatory data; per DrugBank pharmacology profile, used for schizophrenia, depression, anxiety (adults) and behavioural problems (children) — no FDA/EMA approval on record |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on known pharmacology data, Sulpiride acts as a selective antagonist at D₂ and D₃ dopamine receptors, with weak off-target affinity for three carbonic anhydrase isoforms (CA1, CA7, CA12). It has historically been used for schizophrenia, depression, and anxiety in adults, and behavioural problems in children, though it has never received FDA or EMA marketing authorization.

Retinal dystrophy with or without extraocular anomalies — the top-ranked predicted indication — is a genetically driven congenital eye disorder, typically caused by mutations in retinal developmental genes. There is no established pharmacological pathway connecting dopamine receptor antagonism or weak carbonic anhydrase inhibition to correction of a congenital structural retinal defect.

Based on the evidence review, this prediction is very likely a knowledge-graph artifact rather than a genuine repurposing signal: none of the 15 retrieved publications mention Sulpiride — all simply describe clinical features of congenital ocular/orbital disorders with no therapeutic context. The same pattern — a high TxGNN confidence score paired with zero clinical trials, no supporting literature, and a congenital/monogenic disease mechanism unlikely to respond to pharmacotherapy — repeats across all nine top-ranked predicted indications for this drug (ranks 2–9), which include hydranencephaly, X-linked myopia, Charcot-Marie-Tooth disease type 1G, and several other rare structural or single-gene developmental disorders. This consistent pattern across the whole ranked list further supports a sparse-node/model-artifact explanation rather than a true biological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Overview of orbital infections; no mention of Sulpiride or pharmacotherapy |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Clinical approach to diplopia; unrelated to Sulpiride |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Congenital ptosis pathophysiology; no drug therapy discussed |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital lens shape anomalies; developmental biology only |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler syndrome vitreoretinal degeneration; genetic/structural, no pharmacotherapy |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Imaging classification of pediatric orbital/ocular lesions; no treatment data |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Review | Archives of Ophthalmology | Orbital arteriovenous malformations management; unrelated mechanism |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | American Journal of Ophthalmology | Unilateral cryptophthalmia case description; no drug relevance |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | Journal of Neuro-Ophthalmology | Congenital trochlear-oculomotor synkinesis case; no pharmacotherapy |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case Report | Optometry and Vision Science | Congenital extraocular muscle fibrosis case; no drug relevance |

**Note:** All 15 retrieved publications discuss the clinical features of congenital eye/orbital disorders. None address Sulpiride, dopaminergic mechanisms, or any pharmacological intervention.

---

## India Market Information

Sulpiride is not currently marketed or registered in India — 0 authorizations on file.

---

## Safety Considerations

- **Pharmacological Targets (per DrugBank pharmacology data)**: Sulpiride is a selective antagonist at D₂ and D₃ dopamine receptors (target genes: DRD2, DRD3), with additional weak, likely clinically insignificant affinity for carbonic anhydrase isoforms CA1, CA7, and CA12.
- Key warnings and contraindications for this drug are not yet available (Data Gap DG001, flagged **Blocking**) — this must be resolved from the official India/TFDA package insert before any S1 safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every one of the nine top-ranked TxGNN predictions for Sulpiride is scored "Hold" — high model confidence is not matched by any clinical trial or Sulpiride-specific literature, and the predicted diseases are predominantly monogenic/congenital structural disorders with no plausible pharmacological reversibility. Separately, the missing package-insert warnings/contraindications (DG001, Blocking) independently prevent this candidate from entering a formal S1 safety evaluation regardless of prediction strength.

**To proceed, the following is needed:**
- Retrieve TFDA/India label warnings and contraindications (DG001 — blocking; required before any S1 review)
- Confirm mechanism of action from DrugBank/primary literature (DG002)
- Independently assess whether the TxGNN model's high scores for this drug reflect a genuine biological signal or a knowledge-graph sparsity artifact, given the consistent absence of trials/literature across the full ranked list
- If any indication is to be pursued further, prioritize one with an actual mechanistic or epidemiological rationale rather than the current top-ranked congenital/genetic disease candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

