---
layout: default
title: Tranylcypromine
parent: 僅模型預測 (L5)
nav_order: 848
evidence_level: L5
indication_count: 10
---

# Tranylcypromine
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

# Tranylcypromine: From Treatment-Resistant Depression to Melancholia

> **Screening note:** This Evidence Pack contains 10 TxGNN-predicted indications for tranylcypromine (candidate batch `TW-DB00752-multi`). The single highest-scoring model output (*benign paroxysmal torticollis of infancy*, score 99.67%) is explicitly flagged in its own rationale as a likely knowledge-graph embedding false positive — no mechanistic link, no trials, no literature. TxGNN scores cluster very close to 1.0 across many unrelated diseases, so raw rank is not a reliable filter on its own. This report instead centers on **Melancholia**, the candidate with the strongest evidence tier (L2) among the batch, and briefly summarizes the rest for completeness.

---

## One-Sentence Summary

> Tranylcypromine is a classic irreversible monoamine oxidase inhibitor (MAOI) whose established clinical use is treatment-resistant/atypical major depression.
> The TxGNN model — after evidence triage — supports repositioning toward **Melancholia** (a severe depressive subtype),
> a finding that is best understood as the model **rediscovering an already-known indication** rather than a novel hypothesis,
> supported by **direct clinical studies including a double-blind RCT** and a dedicated 1984 trial titled "Treatment of melancholia with tranylcypromine."

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder / treatment-resistant depression (derived from literature in this pack; formal Taiwan license text unavailable — drug is not TFDA-marketed) |
| Predicted New Indication | Melancholia |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L2 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The structured `original_moa` field is a data gap, but the literature within this evidence pack consistently and repeatedly describes tranylcypromine as a **classic, irreversible, non-selective monoamine oxidase inhibitor (MAO-A/B)**, used for major depressive disorder and specifically for treatment-resistant/atypical depression (e.g., PMID 36482163, PMID 35837681). By inhibiting MAO, it increases synaptic availability of serotonin, norepinephrine, and dopamine.

Melancholia is not a distinct disease but a **severe, endogenous subtype of major depressive disorder** characterized by profound anhedonia, psychomotor disturbance, and diurnal mood variation. Since tranylcypromine's original indication and melancholia share the identical underlying pathophysiology (monoamine dysregulation) and identical treatment mechanism (MAO inhibition), this is mechanistically the most defensible finding in the batch — effectively confirming known pharmacology rather than proposing a new biological hypothesis.

This is reinforced by a closely related candidate in the same batch, **"neurotic depression"** (a legacy diagnostic term for non-endogenous depression), which independently reached the same evidence tier (L2) with an RCT directly comparing tranylcypromine to another MAOI (PMID 8127928). Both candidates converge on the same conclusion: TxGNN is correctly recovering tranylcypromine's core antidepressant pharmacology, even though the term "melancholia"/"neurotic depression" no longer appears as a formal indication label.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (no ClinicalTrials.gov or ICTRP entries for this indication in the pack; evidence below is derived from published literature, several of which are controlled trials predating trial-registry requirements).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6691499](https://pubmed.ncbi.nlm.nih.gov/6691499/) | 1984 | Open-label study | Am J Psychiatry | 9 of 12 DSM-III melancholia outpatients responded to tranylcypromine; responders had lower baseline and post-treatment depression severity — direct evidence for this exact indication |
| [8127928](https://pubmed.ncbi.nlm.nih.gov/8127928/) | 1993 | RCT (double-blind) | Pharmacopsychiatry | Tranylcypromine (n=79) vs. moclobemide (n=81) in depressed patients — head-to-head efficacy/safety comparison of an established MAOI |
| [6342565](https://pubmed.ncbi.nlm.nih.gov/6342565/) | 1983 | RCT (double-blind, controlled) | Arch Gen Psychiatry | Amitriptyline vs. tranylcypromine vs. combination in 60 DSM-III major depression patients; all arms improved equally, combination not superior |
| [28579071](https://pubmed.ncbi.nlm.nih.gov/28579071/) | 2017 | Review / Meta-analysis | Eur Neuropsychopharmacol | Two-part review of tranylcypromine pharmacodynamics/pharmacokinetics plus meta-analysis of controlled depression trials |
| [23359339](https://pubmed.ncbi.nlm.nih.gov/23359339/) | 2013 | Systematic Review | Pharmacopsychiatry | Systematic review of withdrawal/discontinuation phenomena after abrupt tranylcypromine cessation — relevant to abuse/dependence risk |
| [3522559](https://pubmed.ncbi.nlm.nih.gov/3522559/) | 1986 | Cohort (from 2 controlled trials) | J Clin Psychiatry | In 58 major depressive episode patients across two 4-week controlled trials, greater baseline severity, psychomotor retardation, and weight loss predicted better tranylcypromine response — a melancholia-like symptom profile |
| [35837681](https://pubmed.ncbi.nlm.nih.gov/35837681/) | 2023 | Review (clinical guide) | CNS Spectrums | Consensus-based prescriber's guide (70+ international experts) to classic MAOIs (phenelzine, tranylcypromine, isocarboxazid) for treatment-resistant depression |
| [34369903](https://pubmed.ncbi.nlm.nih.gov/34369903/) | 2021 | Case series | J Clin Psychopharmacol | Tranylcypromine + mirtazapine combination in difficult-to-treat depression; notes serotonin syndrome risk with most other antidepressant combinations |
| [15061154](https://pubmed.ncbi.nlm.nih.gov/15061154/) | 2004 | Study protocol | Control Clin Trials | STAR*D trial design — establishes the treatment-resistant depression context in which MAOIs like tranylcypromine are typically positioned |
| [1636815](https://pubmed.ncbi.nlm.nih.gov/1636815/) | 1992 | Review (clinical) | Am J Psychiatry | Serotonin syndrome review — key safety context for tranylcypromine combination therapy |

---

## Taiwan Market Information

Tranylcypromine currently holds **no TFDA drug license in Taiwan** (`market_status: 未上市`, 0 registrations). No product-level authorization table is available.

---

## Safety Considerations

**Drug Interactions** (source: DDInter, 151 total documented interactions; sample of 20 provided):
- **Major severity** — avoid: Isometheptene, Bupropion, Morphine, Lorcaserin, Diethylpropion, Dolasetron, Palonosetron, Phentermine. These are consistent with tranylcypromine's known MAOI risk profile (hypertensive crisis, serotonin syndrome).
- **Moderate severity**: Epinephrine, Chlorpropamide, Picosulfuric acid, Polyethylene glycol (3350 with electrolytes), Glimepiride, Repaglinide, Sodium sulfate, Dronabinol, Insulin aspart.
- **Minor severity**: Hyoscyamine, Atropine, Dicyclomine.

**Critical data gap**: TFDA package insert warnings and contraindications are not yet available (`DG001`, severity: **Blocking**). Per the data gap log, this precludes completion of the S1 safety pre-screen and must be resolved before formal safety sign-off, notwithstanding the favorable efficacy evidence above.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Melancholia (and the closely related "neurotic depression") reflects tranylcypromine's own established MAOI antidepressant mechanism, supported by multiple controlled/RCT-level studies (L2 evidence) — this is a low-novelty, high-confidence rediscovery rather than a speculative repositioning. However, a Blocking-severity safety data gap (missing TFDA label warnings/contraindications) prevents a full safety sign-off, and the drug is currently unregistered in Taiwan.

**To proceed, the following is needed:**
- Resolve DG001: obtain and parse TFDA (or comparable foreign) package insert for warnings/contraindications before S1 safety clearance
- Formally document MOA (DG002) via DrugBank API query, even though literature-derived MOA is already reasonably clear
- Given zero Taiwan licenses, confirm regulatory pathway (new registration vs. named-patient/orphan import) before any indication-expansion planning
- Given the MAOI dietary/drug interaction burden (tyramine reaction, serotonin syndrome, hypertensive crisis with the Major-tier interactions listed above), any clinical protocol must include a structured interaction/washout checklist

**Note on the other 8 batch candidates:** benign paroxysmal torticollis of infancy, Ohdo syndrome and variants, blepharophimosis–intellectual disability syndrome (Ohdo type), ligneous conjunctivitis, and Keppen-Lubinsky syndrome are all L5/S0/**Hold** — no mechanistic plausibility, no trials, no literature; treat as KG noise. Dysthymic disorder, agoraphobia, and neurotic disorder are L3, S1–S2/**Research Question** — plausible MAOI-class rationale but evidence is class-level or historical (pre-1990s case reports/reviews) rather than drug-specific controlled data; not recommended for advancement without further targeted literature review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

