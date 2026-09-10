---
layout: default
title: Olanzapine
parent: 僅模型預測 (L5)
nav_order: 610
evidence_level: L5
indication_count: 3
---

# Olanzapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Olanzapine: From Schizophrenia/Bipolar Disorder to Dysthymic Disorder

## One-Sentence Summary

Olanzapine is a second-generation (atypical) antipsychotic historically used for schizophrenia and bipolar disorder. Among the three indications TxGNN predicted, **Dysthymic Disorder** is the only one with actual supporting evidence — **5 publications**, though **no dedicated clinical trials** — and is therefore the focus of this report, even though it ranks third by raw TxGNN score. The two higher-scoring predictions were screened out (see note below) because they carry zero evidence and, in one case, a serious safety concern.

> **Note on candidate selection:** TxGNN's top two scored predictions — *benign paroxysmal torticollis of infancy* (99.54%) and *agoraphobia* (99.47%) — returned **zero** clinical trials or literature on cross-check, and the pack's own mechanistic-link analysis flags the torticollis prediction as a likely spurious knowledge-graph artifact with no plausible pharmacology, additionally noting the serious safety risk of using an antipsychotic in infants. Both are scored `S0 / Hold` in the source data and are not carried forward as the headline candidate. Dysthymic Disorder (99.28%, rank 3) is used instead as it is the only candidate that reached `S1` with real evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia / Bipolar Disorder (general drug-class knowledge; original_moa/indications not available in this evidence pack) |
| Predicted New Indication | Dysthymic Disorder |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L3 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (flagged as a Blocking/High data gap in the evidence pack). Based on generally known pharmacology, olanzapine is a second-generation antipsychotic with 5-HT2A/5-HT2C antagonism and weak 5-HT1A agonism, in addition to its D2 antagonism. This serotonergic receptor-modulating profile is the same mechanistic basis underlying its already-established use in the olanzapine-fluoxetine combination (Symbyax) for treatment-resistant depression, which lends some biological plausibility to a role in mood disorders more broadly, including dysthymic disorder (persistent low-grade depressive symptoms).

That said, dysthymia is a chronic, low-intensity depressive condition typically managed with antidepressants and psychotherapy; atypical antipsychotics are more commonly used as an *augmentation* strategy rather than monotherapy. The literature identified below supports this pattern — it centers on antipsychotic augmentation in depressive/personality-disorder contexts rather than dysthymia as a primary target — so the mechanistic story is coherent but the specific fit to dysthymic disorder remains indirect. Sedation and metabolic side effects (weight gain, dyslipidemia) also weigh against long-term use for a chronic, low-severity condition and need explicit risk-benefit justification.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10578457](https://pubmed.ncbi.nlm.nih.gov/10578457/) | 1999 | Open-label cohort | Biological Psychiatry | Open-label olanzapine trial in borderline personality disorder with comorbid dysthymia; supports tolerability/efficacy signal in this comorbid population |
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Reviews second-generation antipsychotics, including olanzapine, as augmentation for major depressive disorder and dysthymia |
| [22938165](https://pubmed.ncbi.nlm.nih.gov/22938165/) | 2012 | Review | Bipolar Disorders | Evidence-based options for treatment-resistant bipolar disorder; contextualizes antipsychotic use in mood disorders |
| [11920152](https://pubmed.ncbi.nlm.nih.gov/11920152/) | 2002 | Review | Molecular Psychiatry | Reviews substituted benzamides' shared mechanistic rationale across dysthymic disorder and schizophrenia negative symptoms — relevant analog for olanzapine's dual-mechanism logic |
| [34727399](https://pubmed.ncbi.nlm.nih.gov/34727399/) | 2021 | Systematic Review / Meta-analysis | Human Psychopharmacology | Meta-analysis of amisulpride (related atypical antipsychotic) for depressive symptoms across psychiatric disorders |

## Taiwan Market Information

No Olanzapine license/product registrations are present in this evidence pack (`total_licenses = 0`, market status: Not Marketed).

## Safety Considerations

- **Drug Interactions**: 338 total interactions documented. Major-severity interactions include **Bupropion**, **Morphine**, and **Potassium citrate**. Multiple Moderate-severity interactions involve antidiabetic agents (Metformin, Canagliflozin, Dapagliflozin, Alogliptin, Albiglutide, Chlorpropamide) — notable given olanzapine's known metabolic/glycemic risk profile and worth specific attention in any repurposing safety plan.

*(Key warnings and contraindications are not available in this evidence pack — flagged as a Blocking data gap; see Conclusion below.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L3 (systematic review / cohort only, no RCTs or trials specific to dysthymic disorder), the drug is not currently marketed in Taiwan, and TFDA label warnings/contraindications — required to clear the S1 safety gate — are a **Blocking** data gap. The mechanistic rationale is plausible but indirect, so this remains a research question rather than a near-term repurposing candidate.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (Blocking gap, DG001) — required before any S1 safety evaluation can complete
- Confirmed mechanism of action documentation (High gap, DG002) to substantiate the mechanistic-link argument
- A dedicated clinical trial or controlled study in dysthymic disorder, since current literature only addresses adjacent conditions (BPD comorbid dysthymia, MDD augmentation)
- Metabolic/glycemic risk-benefit assessment given olanzapine's DDI profile with antidiabetic agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

