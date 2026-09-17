---
layout: default
title: Quetiapine
parent: Moderate Evidence (L3-L4)
nav_order: 708
evidence_level: L4
indication_count: 10
---

# Quetiapine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Quetiapine: From Schizophrenia/Bipolar Disorder to Trichotillomania

## One-Sentence Summary

Quetiapine is a widely used atypical antipsychotic, most commonly indicated for schizophrenia and bipolar disorder. Among the ten highest-scoring TxGNN predictions in this evidence pack, only **Trichotillomania** is backed by actual literature — 7 publications, including case reports and reviews specifically describing quetiapine use in this condition — while the other nine candidates (including the numerically top-ranked "retinal dystrophy with extraocular anomalies") have no supporting trials or literature and are flagged by the evidence pack itself as co-occurrence noise. This report therefore focuses on the Trichotillomania candidate as the only one with a defensible evidence base.

> **Note on candidate selection**: `predicted_indications[0]` by raw TxGNN score is "retinal dystrophy with or without extraocular anomalies" (score 99.57%), but its own `repurposing_rationale` states there is no mechanistic link and the associated literature is unrelated ophthalmology case reports. Presenting that candidate as the lead finding would be misleading, so this report evaluates the rank-8 candidate (Trichotillomania), which is the only one the evidence pack itself upgrades from "Hold" to "Research Question."

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (no Taiwan license records); quetiapine is generally used for schizophrenia and bipolar disorder |
| Predicted New Indication | Trichotillomania |
| TxGNN Prediction Score | 99.38% (internal rank 9,900 of ~17,081 diseases scored) |
| Evidence Level | L4 |
| Taiwan Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, quetiapine is a second-generation (atypical) antipsychotic that antagonizes 5-HT2A, D2, H1, and α1-adrenergic receptors, with well-established efficacy in schizophrenia and bipolar disorder, and as adjunct therapy in major depressive disorder.

Trichotillomania (hair-pulling disorder) is classified within the obsessive-compulsive and related disorders / impulse-control spectrum. The proposed rationale is that quetiapine's serotonin-dopamine modulation may reduce compulsive/impulsive hair-pulling behavior, analogous to how atypical antipsychotics are used as augmentation therapy in OCD-spectrum conditions. This is a plausible mechanistic hypothesis, but it is not a validated receptor-target-to-pathology link — it is inferred by analogy to other impulse-control disorders.

Notably, the literature evidence is mixed: alongside case reports describing benefit, one publication (PMID 11212595) reports quetiapine **exacerbating** obsessive-compulsive symptoms, including trichotillomania, in a patient with pre-existing OCD. This bidirectional signal underscores that the evidence base is exploratory and inconsistent, consistent with the L4 evidence level and "Research Question" (not "Go") status assigned in the evidence pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12405081](https://pubmed.ncbi.nlm.nih.gov/12405081/) | 2002 | Review | Psychiatry | Overview of trichotillomania pharmacotherapy; describes a favorable clinical response to quetiapine in a 33-year-old case |
| [19142421](https://pubmed.ncbi.nlm.nih.gov/19142421/) | 2008 | Case Report | Rev Bras Psiquiatr | Direct case report of quetiapine used to treat trichotillomania |
| [20833945](https://pubmed.ncbi.nlm.nih.gov/20833945/) | 2010 | Case Report/Review | Psychosomatics | Case of recurrent Rapunzel syndrome and trichotillomania with literature review |
| [11212595](https://pubmed.ncbi.nlm.nih.gov/11212595/) | 2001 | Case Report/Review | J Psychiatry Neurosci | **Counter-evidence**: reports quetiapine exacerbating obsessive-compulsive symptoms, including trichotillomania, in a patient with OCD/bipolar disorder |
| [27840761](https://pubmed.ncbi.nlm.nih.gov/27840761/) | 2016 | Case Report | Case Rep Psychiatry | Trichotillomania as a manifestation of dementia; not specific to quetiapine treatment |
| [38797877](https://pubmed.ncbi.nlm.nih.gov/38797877/) | 2025 | Review | Int J Dermatol | Broad review of pharmacological treatment options for trichotillomania; notes lack of standardized guidelines |
| [17484394](https://pubmed.ncbi.nlm.nih.gov/17484394/) | 2006 | Review | J Pract Nursing | General treatment overview of trichotillomania |

---

## Taiwan Market Information

Quetiapine currently has no marketing authorization records in this evidence pack (`market_status: Not marketed`, 0 registrations). No product/formulation data is available.

---

## Safety Considerations

**Drug Interactions** (from DDI database, 356 total interactions on file; key examples):
- **Major**: Bupropion, Morphine
- **Moderate**: Acarbose, Famotidine, Epinephrine, Metformin, Pioglitazone, Loperamide, Aprepitant, Atropine, Dexamethasone, and other agents (metabolic, anticholinergic, and CNS-depressant classes represented)

Detailed prescribing warnings and contraindications are not available in this evidence pack (Blocking data gap, DG001 — TFDA label warnings/contraindications not yet retrieved).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for the trichotillomania indication is limited to case reports and narrative reviews (no controlled or registered clinical trials), with at least one publication reporting a worsening of related symptoms rather than benefit. Combined with the drug's non-marketed status in Taiwan and a blocking gap in TFDA safety labeling, the evidence does not yet support advancing beyond a research hypothesis.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (blocking gap, DG001)
- Confirmed mechanism-of-action data (DG002)
- A prospective or controlled study specifically evaluating quetiapine in trichotillomania to resolve the conflicting case-level signals
- Reassessment of the other 9 top-scoring TxGNN candidates, none of which currently have supporting evidence and should remain at Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

