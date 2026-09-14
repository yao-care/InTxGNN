---
layout: default
title: Tiagabine
parent: 僅模型預測 (L5)
nav_order: 826
evidence_level: L5
indication_count: 1
---

# Tiagabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Tiagabine: From Partial Seizures to Visual Epilepsy

## One-Sentence Summary

> Tiagabine is a GABA reuptake inhibitor originally developed as an adjunctive (add-on) therapy for partial-onset seizures.
> The TxGNN model predicts it may be effective for **Visual Epilepsy**,
> but this is currently supported by only **1 clinical trial** (non-specific to this subtype) and **~18 publications**, most of which address tiagabine's general antiepileptic mechanism rather than visual epilepsy specifically — including one literature signal raising a **safety concern (visual field constriction)** that runs counter to the proposed indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Partial seizures (adjunctive/add-on therapy) — inferred from known mechanism of action; no India license record found (drug is not marketed locally) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.25% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Tiagabine is a selective GABA reuptake inhibitor (GAT-1 inhibitor) that raises extracellular GABA concentration at the synapse. This is a well-established antiepileptic mechanism, and it is the basis for tiagabine's original approval as adjunctive therapy for partial-onset seizures.

"Visual epilepsy" is not a precisely defined disease entity — it likely refers to photosensitive or occipital-lobe epilepsy presenting with visual ictal symptoms. As a subtype of epilepsy, it plausibly falls within the broad therapeutic scope of GABAergic seizure control, which is the mechanistic basis for the TxGNN model's prediction. However, none of the available evidence differentiates tiagabine's efficacy specifically for this visual seizure subtype — the supporting mechanism is a general extrapolation from tiagabine's known antiepileptic action rather than subtype-specific data.

More importantly, the literature includes a specific safety signal: tiagabine (like vigabatrin) has been associated with **visual field constriction** in some patients. This creates a direct tension with positioning the drug as a treatment *for* visual epilepsy — the mechanistic plausibility for seizure control in general does not resolve this potential conflict, and it is a key reason the evidence level remains low (L4) and the recommendation is to Hold pending further clarification.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Observational "Liceo Study" assessing new AEDs (including tiagabine) as first-choice add-on (bitherapy) in focal epilepsy under real-world conditions. Not specific to visual epilepsy — provides only general add-on efficacy support (relevance grade: B). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22592677](https://pubmed.ncbi.nlm.nih.gov/22592677/) | 2012 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Reviews tiagabine as add-on therapy for drug-resistant partial epilepsy; establishes general efficacy evidence base for the drug's original indication. |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Practice Guideline | Neurology | AAN/AES guideline update on efficacy/tolerability of newer AEDs (including tiagabine) for new-onset epilepsy. |
| [12588906](https://pubmed.ncbi.nlm.nih.gov/12588906/) | 2003 | Review/Safety Signal | J Neurol Neurosurg Psychiatry | Directly discusses vigabatrin and tiagabine in relation to visual field effects — the key safety signal relevant to a "visual epilepsy" indication. |
| [17560495](https://pubmed.ncbi.nlm.nih.gov/17560495/) | 2007 | Review | Pediatric Neurology | Reviews visual adverse effects (visual field/color vision deficits) associated with antiepileptic drugs, including newer agents like tiagabine. |
| [32120063](https://pubmed.ncbi.nlm.nih.gov/32120063/) | 2020 | Review | Neuropharmacology | Comprehensive review of mechanisms of action of currently used antiseizure drugs, including tiagabine's GABA-uptake inhibition. |
| [11520315](https://pubmed.ncbi.nlm.nih.gov/11520315/) | 2001 | Review | Epilepsia | Reviews GABAergic mechanisms underlying seizure generation and control, providing mechanistic context for tiagabine's action. |
| [10530690](https://pubmed.ncbi.nlm.nih.gov/10530690/) | 1999 | Review | Epilepsia | Comprehensive review of tiagabine pharmacology, efficacy as add-on therapy for partial seizures, and safety profile. |
| [9097364](https://pubmed.ncbi.nlm.nih.gov/9097364/) | 1997 | Review | Semin Pediatr Neurol | Reviews tiagabine's efficacy against partial seizures in adults/adolescents, with preliminary pediatric data. |
| [15094857](https://pubmed.ncbi.nlm.nih.gov/15094857/) | 1998 | Review | Drugs of Today | Reviews tiagabine's GABA-uptake inhibition mechanism, efficacy in seizure models, and lack of significant drug interactions. |
| [25825412](https://pubmed.ncbi.nlm.nih.gov/25825412/) | 2016 | Toxicology/Safety Report | Hum Exp Toxicol | Reviews tiagabine toxicity trends reported to US poison centers (2000–2012), including FDA warnings on seizure risk in non-epileptic patients. |

---

## India Market Information

Tiagabine is currently **not registered or marketed in India** (0 authorizations on record). No local product license or approved indication text is available for review.

---

## Safety Considerations

**Drug Interactions:**
The interaction database lists 97 known interactions for tiagabine. Notable moderate-severity interactions include:

| Interacting Drug | Severity |
|---|---|
| Aprepitant | Moderate |
| Morphine | Moderate |
| Morphine (liposomal) | Moderate |
| Opium | Moderate |
| Dronabinol | Moderate |
| Nabilone | Moderate |
| Metoclopramide | Moderate |

These moderate interactions are predominantly with CNS-active/opioid and cannabinoid agents, suggesting a potential for additive CNS depression. A further set of interactions (e.g., Pantoprazole, Doxycycline, Metformin, Omeprazole, Ranitidine, Ondansetron, Simvastatin) are flagged as "Unknown" severity in the source database and would require dedicated review before clinical use.

**Note:** Detailed local warnings and contraindications (package insert-level data) are not yet available — this is a blocking data gap (DG001) and must be resolved before any safety pre-assessment (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level for this prediction is L4 — a single non-specific Phase 4 observational trial plus mechanism-based literature, with no evidence directly targeting "visual epilepsy" as a distinct entity. Compounding this, the literature contains a specific safety signal (visual field constriction associated with tiagabine) that conflicts with the proposed indication and must be resolved before proceeding.

**To proceed, the following is needed:**
- Complete package insert data (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed original mechanism of action documentation from DrugBank (DG002)
- A clear clinical definition/diagnostic criteria for "visual epilepsy" as a target population
- Dedicated evaluation of the visual-field safety signal before considering this indication further, given the direct conflict with a "visual" positioning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

