---
layout: default
title: Phenytoin
parent: High Evidence (L1-L2)
nav_order: 660
evidence_level: L2
indication_count: 10
---

# Phenytoin
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Phenytoin: From Epilepsy to Trigeminal Neuralgia

## One-Sentence Summary

Phenytoin is a voltage-gated sodium channel blocker originally established as a first-line anticonvulsant for epilepsy and seizure disorders. Among ten TxGNN-predicted indications reviewed, **Trigeminal Neuralgia** is the only candidate backed by genuine clinical evidence — **1 completed clinical trial**, a 144-patient retrospective cohort, a case series, and **19 supporting publications** including a European Academy of Neurology guideline. (Note: TxGNN's single highest-scoring prediction, "trigeminal nerve neoplasm," was screened out — its own evidence review found the literature hits were a keyword mismatch on "trigeminal" with no oncologic relevance, and several other high-scoring reflex-epilepsy predictions similarly lack human evidence.)

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy / seizure disorders (anticonvulsant) — established use referenced throughout the evidence base; formal registry indication text not available |
| Predicted New Indication | Trigeminal Neuralgia |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for phenytoin was not available in the registry source (DrugBank MOA lookup flagged as a data gap). Based on known pharmacology cited across the collected literature, phenytoin is a voltage-gated sodium channel blocker in the hydantoin anticonvulsant class — the same broad mechanism used for decades to control abnormal, high-frequency neuronal discharge in epilepsy.

Trigeminal neuralgia shares this pathophysiological signature: it is driven by aberrant, high-frequency ectopic discharge in the trigeminal ganglion/root, typically from vascular compression and focal demyelination. The first-line drugs for trigeminal neuralgia, carbamazepine and oxcarbazepine, work through the identical sodium-channel-blocking mechanism as phenytoin — which is why phenytoin is mechanistically plausible as a second-line or rescue option when oral first-line agents fail or cannot be tolerated (e.g., during severe exacerbations with impaired oral intake).

This is not purely theoretical: IV phenytoin already has real-world use as rescue therapy for acute trigeminal neuralgia exacerbations, reflected in the clinical trial and cohort evidence below. This existing off-label practice pattern is the strongest support for the TxGNN prediction, distinguishing it from the other nine candidates in this evidence pack, most of which (reflex/rare seizure subtypes, trigeminal nerve neoplasm, beta-ketothiolase deficiency) were flagged by their own evidence review as lacking any human data or having only coincidental keyword matches.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03712254](https://clinicaltrials.gov/study/NCT03712254) | N/A | Completed | 15 | Prospective study of IV phenytoin for acute exacerbations of trigeminal neuralgia; addresses the gap left by oral-only first-line agents (carbamazepine/oxcarbazepine) during severe flares. Pilot/observational design, not randomized. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35469475](https://pubmed.ncbi.nlm.nih.gov/35469475/) | 2022 | Cohort | Cephalalgia | Retrospective analysis of 144 cases comparing IV lacosamide and IV phenytoin for acute TN exacerbations |
| [32981076](https://pubmed.ncbi.nlm.nih.gov/32981076/) | 2020 | Case series | Headache | IV phenytoin as acute rescue treatment for TN crisis; institutional cohort |
| [28761370](https://pubmed.ncbi.nlm.nih.gov/28761370/) | 2017 | Review | Journal of Pain Research | Evidence-based comparison of phenytoin and carbamazepine in TN treatment |
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | European Journal of Neurology | European Academy of Neurology guideline on TN diagnosis and management |
| [19445753](https://pubmed.ncbi.nlm.nih.gov/19445753/) | 2009 | Review | BMJ Clinical Evidence | Overview of TN clinical presentation and treatment evidence |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Molecular Pain | TN pathophysiology through pharmacological treatment options |
| [29114270](https://pubmed.ncbi.nlm.nih.gov/29114270/) | 2017 | Review | Asian Journal of Neurosurgery | TN clinical features, mechanisms, and management overview |
| [11903537](https://pubmed.ncbi.nlm.nih.gov/11903537/) | 2001 | Review | Headache | Antiepileptic drugs in cluster headache and trigeminal neuralgia |
| [6487105](https://pubmed.ncbi.nlm.nih.gov/6487105/) | 1984 | Review | Archives of Neurology | Etiology and pathogenesis concepts underlying pharmacologic treatment |
| [15062534](https://pubmed.ncbi.nlm.nih.gov/15062534/) | 2004 | Review | Neurologic Clinics | TN and glossopharyngeal neuralgia treatment approaches |

---

## India Market Information

Phenytoin currently has **0 registrations** on file and is marked **not marketed** in this dataset. No license records are available to summarize.

---

## Safety Considerations

- **Drug Interactions**: 390 total interactions on record (source: DDInter), predominantly Moderate severity. Notable examples relevant to a TN patient population (often co-managed for pain, GI protection, and metabolic conditions): Omeprazole, Metronidazole, Doxycycline, Dexamethasone, Hydrocortisone, Metformin, Aprepitant, Morphine (all Moderate), and Acetylsalicylic acid (Minor). Given the breadth of interactions, a full interaction screen against the patient's concurrent medications is required before use.

Detailed package-insert warnings and contraindications were not available in this evidence pack (flagged as a **Blocking**-severity data gap — TFDA/CDSCO label text has not yet been retrieved). This must be resolved before any safety sign-off.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Trigeminal neuralgia is the only one of the ten TxGNN-predicted indications supported by an actual clinical trial, a sizeable retrospective cohort, and a case series, all converging with the mechanistic rationale (shared sodium-channel-blocking action with first-line TN drugs) and existing off-label rescue-therapy practice. However, evidence is limited to non-randomized pilot/observational studies, and critical safety and regulatory data are still missing.

**To proceed, the following is needed:**
- Package insert warnings/contraindications (currently a Blocking data gap — required before any S1 safety screening)
- Detailed DrugBank/MOA pharmacology data to formally confirm the sodium-channel mechanism
- Randomized controlled trial data for phenytoin in trigeminal neuralgia (current evidence is observational/pilot only)
- Confirmation of India market/regulatory registration pathway, since phenytoin is currently unmarketed with zero licenses on file
- Full concomitant-medication interaction review given the 390 recorded DDIs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

