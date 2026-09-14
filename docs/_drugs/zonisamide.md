---
layout: default
title: Zonisamide
parent: 僅模型預測 (L5)
nav_order: 903
evidence_level: L5
indication_count: 10
---

# Zonisamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Using no additional skills — this is a direct content-generation task per an explicit, fully-specified prompt template; no coding/debugging/brainstorming skill applies.

Note before the report: the Evidence Pack contains **10 candidate indications** for zonisamide, not one. The literal `predicted_indications[0]` (Tourette syndrome) has TxGNN score 99.85% but **zero clinical trials, zero literature, evidence level L5, recommendation Hold** — it is a pure embedding artifact. The same is true for trichotillomania, Prinzmetal angina, and conjunctivitis. Two other top-ranked "predictions" (methemoglobinemia / methemoglobinemia alpha type / reductase deficiency) are flagged in the data itself as likely **inverse safety signals** (zonisamide is a known sulfonamide trigger of methemoglobinemia, not a treatment for it) — reporting these as "repurposing opportunities" would be misleading.

The only candidate with real evidentiary weight (L1, two completed Phase 3 RCTs, decision stage S3) is **absence epilepsy**. As the person responsible for this report, I am building it around that candidate rather than the raw top TxGNN score, and flagging the rest below.

---

# Zonisamide: From Partial Epilepsy to Absence Epilepsy

## One-Sentence Summary

> Zonisamide is a sulfonamide-derivative anticonvulsant established as monotherapy for newly diagnosed partial (focal) epilepsy.
> Among 10 TxGNN-predicted indications for this drug, the strongest-evidenced signal is **Absence Epilepsy**,
> supported by **4 clinical trials (2 completed Phase 3 RCTs)** and **20 publications**, including seizure-type-specific case series.
> Note: the drug's raw #1 TxGNN score (Tourette syndrome) and two other top-ranked hits (methemoglobinemia) carry no supporting evidence or are likely safety-direction artifacts — see Conclusion.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in formal India regulatory data (data gap); per literature in this pack, zonisamide is an established antiepileptic for partial/focal seizures |
| Predicted New Indication | Absence Epilepsy |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, a formal DrugBank mechanism-of-action record is not available (data gap DG002). However, the literature reviewed in this evidence pack consistently describes zonisamide as a broad-spectrum antiepileptic that blocks voltage-gated Na⁺ channels and **T-type Ca²⁺ channels**, and modulates glutamate/GABA release. T-type Ca²⁺ channel blockade is specifically relevant to absence seizures, which arise from abnormal thalamocortical oscillatory circuits — this is the same target class exploited by first-line absence therapies (ethosuximide, valproate).

Because zonisamide's core approved use is anticonvulsant therapy, the relationship between the original and predicted indications is not a cross-disease repurposing leap — it is a **within-epilepsy extension** from partial seizures to a different seizure type (absence seizures) that shares the same class of drug target. Case series literature already report use in refractory juvenile absence epilepsy and juvenile myoclonic epilepsy, giving this prediction a mechanistic and empirical basis stronger than a typical de novo repurposing hypothesis.

By contrast, the mechanistic rationale offered for Tourette syndrome, trichotillomania, and Prinzmetal angina in this pack is explicitly labeled as speculative cross-system extrapolation with no direct supporting studies, and the methemoglobinemia-related predictions are noted as likely representing a known **adverse-effect direction** (sulfonamide-induced methemoglobinemia) rather than a treatment indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00477295](https://clinicaltrials.gov/study/NCT00477295) | Phase 3 | Completed | 583 | Multicentre RCT comparing zonisamide vs. carbamazepine monotherapy in newly diagnosed partial epilepsy; direct efficacy/safety evidence for zonisamide (Grade A) |
| [NCT00848549](https://clinicaltrials.gov/study/NCT00848549) | Phase 3 | Completed | 295 | Double-blind extension study assessing long-term safety and efficacy durability of zonisamide monotherapy in newly diagnosed partial seizures (Grade A) |
| [NCT07443241](https://clinicaltrials.gov/study/NCT07443241) | N/A | Completed | 779 | Retrospective study of sex-specific differences in status epilepticus; not a zonisamide intervention trial (Grade C, low relevance) |
| [NCT04939675](https://clinicaltrials.gov/study/NCT04939675) | N/A | Unknown | 40 | Feasibility study for an epilepsy screening questionnaire; not a drug efficacy trial (Grade C, low relevance) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15847848](https://pubmed.ncbi.nlm.nih.gov/15847848/) | 2005 | Review | Epilepsy Research | Chart review of 45 patients ≤18y with absence seizures: 51.1% became seizure-free on zonisamide, supporting efficacy specifically in absence seizures |
| [24907183](https://pubmed.ncbi.nlm.nih.gov/24907183/) | 2014 | Cohort | Epilepsy Research | Zonisamide effective in drug-resistant juvenile absence epilepsy (JAE) |
| [15634623](https://pubmed.ncbi.nlm.nih.gov/15634623/) | 2004 | Cohort | Epileptic Disorders | Retrospective review of 15 juvenile myoclonic epilepsy patients (including absence seizures) treated with zonisamide |
| [34941639](https://pubmed.ncbi.nlm.nih.gov/34941639/) | 2021 | Review | Pediatric Reports | Review of therapeutic options for childhood absence epilepsy, including newer AEDs |
| [34289757](https://pubmed.ncbi.nlm.nih.gov/34289757/) | 2021 | Review | Expert Rev Clin Pharmacol | Therapeutic approach to difficult-to-treat typical absence seizures across idiopathic generalized epilepsies |
| [35363878](https://pubmed.ncbi.nlm.nih.gov/35363878/) | 2022 | Review (Cochrane) | Cochrane Database Syst Rev | Network meta-analysis of AED monotherapy for epilepsy including zonisamide, individual participant data |
| [23350722](https://pubmed.ncbi.nlm.nih.gov/23350722/) | 2013 | Review | Epilepsia | Updated ILAE evidence review of AED efficacy/effectiveness as initial monotherapy across seizure types and syndromes |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Review (AAN/AES Guideline) | Neurology | Practice guideline update on efficacy/tolerability of newer AEDs for treatment of new-onset epilepsy |
| [16341290](https://pubmed.ncbi.nlm.nih.gov/16341290/) | 2005 | Review | Drugs of Today | Review of zonisamide's use in epilepsy therapy, including efficacy in absence seizures among other seizure types |
| [15832611](https://pubmed.ncbi.nlm.nih.gov/15832611/) | 2005 | Cohort | Journal of Child Neurology | Retrospective chart review of 68 children treated with zonisamide monotherapy/adjunctive therapy across seizure types |

## India Market Information

Zonisamide currently holds **no marketing authorization in India** (0 registrations, market status: Not Marketed). No license records are available to summarize.

## Safety Considerations

**Drug Interactions**: The DDI query returned 154 total interactions. Notable **Major**-level interactions include a cluster of anticholinergic agents — Methscopolamine, Hyoscyamine, Atropine, Scopolamine, Glycopyrronium, Clidinium, Dicyclomine, Trospium, Mepenzolate, and Propantheline — as well as **Metformin**. Notable **Moderate**-level interactions include Aprepitant, Morphine, Dexamethasone, Cimetidine, Clarithromycin, Dronabinol, Nabilone, Metoclopramide, and Miconazole.

(Key warnings and contraindications from the formal India label are not yet available in this evidence pack — see Next Steps.)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Absence Epilepsy specifically)

**Rationale:**
Two completed Phase 3 trials plus a decade-plus body of cohort/case-series literature on zonisamide across absence, juvenile myoclonic, and generalized epilepsy syndromes provide L1-level support for this indication, and the mechanism (T-type Ca²⁺ channel blockade) is directly relevant to absence-seizure pathophysiology. This is best framed as a seizure-type label extension rather than a novel disease repurposing.

**To proceed, the following is needed:**
- Official India-approved package insert / label (warnings, contraindications) — currently a **blocking** data gap (DG001), required before any safety pre-screen (S1)
- Formal DrugBank-sourced mechanism-of-action record (DG002)
- A market-entry pathway assessment, since zonisamide has zero existing India registrations
- Confirmation of anticholinergic and metformin co-prescription risk in the target absence-epilepsy population, given the Major-level DDIs identified

**Other candidates in this evidence pack, for the record:**
- **Manic/Bipolar Affective Disorder** (L2, Research Question) — one RCT positive (PMID 22506436) but contradicted by case reports of zonisamide-induced mania/psychosis; mechanistically plausible but directionally inconsistent, needs further review before any decision.
- **Fibromyalgia**, **Tourette syndrome**, **trichotillomania**, **Prinzmetal angina**, **conjunctivitis** — all Hold, L4/L5, no or withdrawn trial support.
- **Methemoglobinemia / methemoglobinemia alpha type / methemoglobin reductase deficiency** — these should **not** be treated as repurposing candidates; they most likely reflect the knowledge graph capturing a known adverse-effect relationship (sulfonamide-induced methemoglobinemia) in the wrong direction. Recommend routing these to safety/pharmacovigilance review rather than the repurposing pipeline.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

