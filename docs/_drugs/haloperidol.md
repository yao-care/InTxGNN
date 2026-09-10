---
layout: default
title: Haloperidol
parent: 僅模型預測 (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

# Haloperidol: From Antipsychotic Therapy to Manic Bipolar Affective Disorder

> **Note on candidate selection:** This Evidence Pack lists 10 TxGNN-predicted indications for Haloperidol. Nine of them (ranks 1–9, including the highest-scoring "congenital disorder of glycosylation with defective fucosylation") have **zero** clinical trial or literature support, no mechanistic rationale, and are scored L5/Hold. Only **Manic Bipolar Affective Disorder** (rank 10 by raw TxGNN score, but the only actionable candidate) is backed by real clinical and literature evidence. This report focuses on that candidate.

---

## One-Sentence Summary

Haloperidol is a first-generation (typical) antipsychotic; a formal record of its original approved indication and mechanism of action was not available in this Evidence Pack (flagged as data gaps DG001/DG002). The TxGNN model — together with real-world evidence — supports its use in **Manic Bipolar Affective Disorder**, with **9 clinical trials** and **20 publications** currently identified, several of which use haloperidol directly as an active comparator or add-on therapy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in Evidence Pack (data gap — see DG001/DG002); drug is documented across the evidence as a first-generation antipsychotic |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.83% (raw rank 3651 of all TxGNN drug–disease pairs) |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed, formal mechanism-of-action documentation for Haloperidol is not available in this Evidence Pack (DG002, High severity). Based on the information collected from clinical trial and literature evidence, Haloperidol is a typical (first-generation) antipsychotic that acts primarily through central D2 dopamine receptor antagonism, rapidly suppressing dopaminergic activity in the limbic system.

This D2-antagonist mechanism is pharmacologically the same core pathway exploited by second-generation antipsychotics (risperidone, olanzapine, aripiprazole) that are established treatments for acute manic episodes in Bipolar I Disorder. Several Phase 3 trials in this Evidence Pack use haloperidol directly as the active comparator against these newer agents (e.g., risperidone vs. placebo vs. haloperidol; olanzapine vs. placebo vs. haloperidol), indicating haloperidol's antimanic efficacy is already an accepted clinical benchmark rather than a purely theoretical extrapolation.

Unlike the other nine TxGNN-predicted candidates for this drug — which have no supporting trials, no literature, and no plausible mechanistic link (e.g., retinal dystrophy, X-linked myopia, Charcot-Marie-Tooth disease) — the mania indication is grounded in an established pharmacological class effect and a substantial body of comparative clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00253162](https://clinicaltrials.gov/study/NCT00253162) | Phase 3 | Completed | 439 | Risperidone vs. placebo vs. haloperidol in manic episodes of Bipolar I Disorder; haloperidol used as active comparator for maintenance efficacy at 12 weeks |
| [NCT00253149](https://clinicaltrials.gov/study/NCT00253149) | Phase 3 | Completed | 158 | Risperidone add-on to mood stabilizers vs. placebo vs. haloperidol in manic phase of bipolar disorder |
| [NCT00097266](https://clinicaltrials.gov/study/NCT00097266) | Phase 3 | Completed | 615 | Multicenter, double-blind, placebo-controlled study of aripiprazole monotherapy in acute mania; haloperidol-referenced comparative framework |
| [NCT00129220](https://clinicaltrials.gov/study/NCT00129220) | Phase 3 | Completed | 224 | Placebo- and haloperidol-controlled double-blind trial of olanzapine in manic or mixed episodes of Bipolar I Disorder |
| [NCT00126009](https://clinicaltrials.gov/study/NCT00126009) | Phase 2 | Completed | 120 | Valproate-amisulpride vs. valproate-haloperidol combination in bipolar I manic episode; efficacy and safety comparison |
| [NCT04327843](https://clinicaltrials.gov/study/NCT04327843) | Phase 3 | Completed | 22 | Long-acting injectable antipsychotics with adherence-focused behavioral program for chronic psychotic disorders in Tanzania |
| [NCT03541031](https://clinicaltrials.gov/study/NCT03541031) | N/A | Unknown | 120 | Micronutrient/fish oil adjunctive supplementation allowing lower conventional medication doses in bipolar disorder |
| [NCT06049953](https://clinicaltrials.gov/study/NCT06049953) | N/A | Recruiting | 200 | Observational study of antenatal antipsychotic exposure on maternal/infant outcomes in severe mental illness |
| [NCT00767715](https://clinicaltrials.gov/study/NCT00767715) | Phase 4 | Terminated | 11 | Olanzapine vs. conventional antipsychotics for acute mania cost/efficacy comparison in Sweden (terminated early) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34642461](https://pubmed.ncbi.nlm.nih.gov/34642461/) | 2022 | Network Meta-analysis | Molecular Psychiatry | Systematic review/network meta-analysis of oral monotherapy RCTs (incl. haloperidol) for acute bipolar mania, comparing efficacy, acceptability, tolerability |
| [22134043](https://pubmed.ncbi.nlm.nih.gov/22134043/) | 2012 | RCT | Journal of Affective Disorders | Randomized, double-blind, placebo- and haloperidol-controlled study of olanzapine in Japanese patients with manic/mixed Bipolar I episodes |
| [369472](https://pubmed.ncbi.nlm.nih.gov/369472/) | 1979 | RCT | Archives of General Psychiatry | Double-blind controlled trial of lithium plus haloperidol vs. placebo plus haloperidol in excited schizo-affective disorder |
| [36789916](https://pubmed.ncbi.nlm.nih.gov/36789916/) | 2023 | Review | BMJ Mental Health | Comparison of antipsychotic dose equivalents between acute bipolar mania and schizophrenia |
| [19454110](https://pubmed.ncbi.nlm.nih.gov/19454110/) | 2007 | Review | BMJ Clinical Evidence | Overview of bipolar disorder epidemiology, prognosis, and treatment approaches |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Review | Acta Psychiatrica Scandinavica | Evidence-based treatment options and clinical management suggestions for manic episodes |
| [17627670](https://pubmed.ncbi.nlm.nih.gov/17627670/) | 2007 | Review | CNS Drug Reviews | Review of ziprasidone clinical trials for schizophrenia and bipolar disorder, including haloperidol-referenced data |
| [22070611](https://pubmed.ncbi.nlm.nih.gov/22070611/) | 2012 | Review | CNS Neuroscience & Therapeutics | Refractoriness in bipolar disorder; notes haloperidol as an add-on option for partial responders to lithium/valproate |
| [10343182](https://pubmed.ncbi.nlm.nih.gov/10343182/) | 1999 | Clinical Study | Neuropsychobiology | Lithium and haloperidol treatments differently affect leukocyte Gαs protein levels in bipolar affective disorder |
| [22161387](https://pubmed.ncbi.nlm.nih.gov/22161387/) | 2011 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Oxcarbazepine for acute affective episodes in bipolar disorder |

---

## Safety Considerations

**Drug Interactions:** Of 303 total documented interactions, the following major-severity interactions were identified in the evidence sample: **Bupropion**, **Morphine**, **Clarithromycin**, and **Dolasetron** (all Major level). Additional moderate-level interactions include Famotidine, Epinephrine, Hydrocortisone, Amphotericin B, Loperamide, Atropine, Aprepitant, Clarithromycin-class agents, and several anticholinergic/GI motility drugs. Given that bipolar mania patients are frequently on polypharmacy (mood stabilizers, other antipsychotics), these interactions warrant screening prior to prescribing.

Formal key warnings and contraindications were not available in this Evidence Pack (see DG001, Blocking severity) — please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Manic Bipolar Affective Disorder is supported by an L1 evidence level (multiple completed Phase 3 RCTs using haloperidol as an active comparator or add-on therapy) and a coherent D2-antagonist mechanistic rationale consistent with the established antimanic class effect. However, the drug currently has no market registration status recorded, and critical safety documentation (label warnings, contraindications) is an unresolved blocking data gap.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain formal package insert / regulatory label warnings and contraindications
- Resolve DG002 (High): obtain confirmed mechanism-of-action documentation from DrugBank
- Confirm original approved indication(s) and any existing regulatory filing status for Haloperidol locally
- Clinical review of Major-level drug interactions (Bupropion, Morphine, Clarithromycin, Dolasetron) in the context of typical bipolar mania comedication regimens
- Note: the other 9 TxGNN-ranked candidate indications for this drug carry no supporting evidence (L5/Hold) and should not be advanced without new data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

