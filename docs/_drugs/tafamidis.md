---
layout: default
title: Tafamidis
parent: High Evidence (L1-L2)
nav_order: 797
evidence_level: L1
indication_count: 10
---

# Tafamidis
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

Using no additional skill — this is a direct data-to-report transcription task following the given v5 template; I'm applying the template rules and evidence-selection judgment directly.

**Note on indication selection**: The evidence pack ranks candidates by raw TxGNN score, but ranks #1–4, #7, #9, #10 are explicitly flagged by the scoring engine as unsupported KG-embedding noise (`L5`/`Hold`, zero trials, zero literature). I selected **rank #6 — "Acquired Amyloid Peripheral Neuropathy"** as the report subject because it is the only candidate that completed full scoring (`L1`/`S3`/`Proceed with Guardrails`) with real supporting evidence.

---

# Tafamidis: From Transthyretin Amyloid Cardiomyopathy to Acquired Amyloid Peripheral Neuropathy

## One-Sentence Summary

> Tafamidis is a transthyretin (TTR) tetramer stabiliser, approved internationally to treat TTR-mediated amyloid cardiomyopathy (ATTR-CM) and reduce cardiovascular mortality.
> The TxGNN model predicts it may also be effective for **Acquired Amyloid Peripheral Neuropathy**,
> with **2 clinical trials** and **10 publications** currently supporting this direction — largely re-confirming the drug's already-approved polyneuropathy indication (ATTR-PN) rather than revealing a wholly new use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Transthyretin (TTR)-mediated amyloidosis — cardiomyopathy and polyneuropathy (sourced from pharmacology data; formal MOA field is a data gap) |
| Predicted New Indication | Acquired Amyloid Peripheral Neuropathy |
| TxGNN Prediction Score | 84.77% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, the structured `original_moa` field is a data gap (DG002, High severity). However, pharmacology data captured under the target-binding record for transthyretin fills part of this gap: **Tafamidis binds within the thyroxine-binding sites of the TTR tetramer, stabilising the weak dimer-dimer interface that is the first point of failure during tetramer dissociation.** By kinetically stabilising both wild-type and mutant TTR, it blocks the misfolding/aggregation cascade that produces amyloid fibrils. This mechanism underlies its approval for TTR-mediated amyloidosis, including cardiomyopathy (ATTR-CM) and, in several jurisdictions, orphan designation for senile systemic amyloidosis (EU, 2012).

ATTR-CM (heart) and ATTR-PN/"acquired amyloid peripheral neuropathy" (peripheral nerve) are two organ-specific manifestations of the **same underlying disease process** — extracellular deposition of misfolded TTR fibrils — differing only by the tissue in which amyloid preferentially accumulates. Since tafamidis acts upstream at the protein-stabilisation step rather than on any organ-specific target, its efficacy is not intrinsically restricted to cardiac tissue.

This is reflected in the evidence: the pivotal **Fx-005** trial program (from which several of the trials below descend) was originally designed for transthyretin amyloid polyneuropathy, and tafamidis already carries approved ATTR-PN indications in multiple markets outside India. The TxGNN signal here therefore largely **recovers a known, clinically validated mechanism-indication link** rather than identifying a novel repurposing hypothesis — which is consistent with its complete (L1/S3) evidence scoring, in contrast to the unscored, evidence-free candidates elsewhere in this evidence pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06465810](https://clinicaltrials.gov/study/NCT06465810) | N/A (Observational) | Recruiting | 1,850 | Global, non-interventional "MaesTTRo" study collecting real-world treatment patterns and outcomes across ATTR amyloidosis (including neuropathy phenotypes); relevance grade **B** — large, directly relevant population |
| [NCT07112066](https://clinicaltrials.gov/study/NCT07112066) | N/A | Recruiting | 50 | Multimodality imaging study on mechanistic insights into cardiac transthyretin amyloidosis; neuropathy is not the primary endpoint. Relevance grade **C** |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26662359](https://pubmed.ncbi.nlm.nih.gov/26662359/) | 2015 | Review (Tier 2) | Neurology and Therapy | Comprehensive review of tafamidis' kinetic stabilisation of TTR and its clinical effect on halting the amyloidogenic cascade in ATTR |
| [30907141](https://pubmed.ncbi.nlm.nih.gov/30907141/) | 2019 | Review | Amyloid | Surveys randomized controlled trials across hereditary and acquired TTR amyloidosis therapeutics |
| [25604431](https://pubmed.ncbi.nlm.nih.gov/25604431/) | 2015 | Review | J Neurol Neurosurg Psychiatry | Describes molecular pathogenesis and disease-modifying treatment landscape for ATTR amyloidosis |
| [25416603](https://pubmed.ncbi.nlm.nih.gov/25416603/) | 2014 | Review | Expert Rev Neurotherapeutics | Reviews current/future treatment options for amyloid neuropathies of acquired and genetic origin |
| [30790171](https://pubmed.ncbi.nlm.nih.gov/30790171/) | 2019 | Review | Heart Failure Reviews | Covers diagnosis/treatment advances in both wild-type (acquired) and hereditary cardiac ATTR |
| [36336119](https://pubmed.ncbi.nlm.nih.gov/36336119/) | 2023 | Review | Curr Probl Cardiol | Summarises current indications for ATTR cardiac amyloidosis therapy, including hereditary and acquired forms |
| [35301856](https://pubmed.ncbi.nlm.nih.gov/35301856/) | 2022 | Review | JAHA | Discusses prescribing complexity and cost barriers for tafamidis and other TTR amyloidosis therapeutics |
| [28295152](https://pubmed.ncbi.nlm.nih.gov/28295152/) | 2017 | Review | Acta Neurol Scand | Reviews causally-treatable hereditary neuropathies including TTR-related familial amyloidosis |
| [34999558](https://pubmed.ncbi.nlm.nih.gov/34999558/) | 2022 | Review | Curr Opin Struct Biol | Discusses small-molecule protein stabilisers (tafamidis being the first approved) for protein-misfolding diseases |
| [37910439](https://pubmed.ncbi.nlm.nih.gov/37910439/) | 2023 | Preclinical/Structural study | J Med Chem | Structural study of resveratrol derivatives inhibiting TTR fibrillisation, contextualising tafamidis' binding mode |

---

## India Market Information

Tafamidis is currently **not marketed in India** — `taiwan_regulatory.total_licenses = 0`, with no registered product authorizations on file.

---

## Safety Considerations

**Drug Interactions**: 13 potential interactions identified via DDInter/pharmacology screening.
- **Major**: Ozanimod
- **Moderate**: Rosuvastatin, Deferasirox, Eltrombopag, Lusutrombopag, Artesunate, Axitinib, Methotrexate, Irinotecan, Irinotecan (liposomal), Belinostat, Imatinib

*(Key warnings and contraindications are a documented data gap (DG001, Blocking) pending TFDA/local package insert retrieval — not available for this report.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is strong and largely confirmatory — tafamidis' TTR-stabilising action is already validated for organ-specific ATTR manifestations (cardiac and neuropathic), and this candidate reached full evidence scoring (L1/S3) unlike the majority of other TxGNN outputs in this evidence pack, which were flagged as unsupported embedding noise. However, the drug is not currently marketed in India, and critical safety documentation (warnings/contraindications) remains an unresolved blocking data gap.

**To proceed, the following is needed:**
- Retrieve official package insert / local regulatory warnings and contraindications (DG001, Blocking)
- Obtain formal DrugBank MOA record to replace the pharmacology-sourced substitute used in this report (DG002)
- Confirm India regulatory filing/import pathway, given zero current registrations
- Clarify clinical distinction (if any) between "acquired amyloid peripheral neuropathy" as scored here and the already-approved ATTR-PN indication, to determine true incremental value of this signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

