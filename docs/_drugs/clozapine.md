---
layout: default
title: Clozapine
parent: 僅模型預測 (L5)
nav_order: 205
evidence_level: L5
indication_count: 10
---

# Clozapine
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

Using the report template directly (this is a structured content-generation task, not a coding/build task, so no engineering skill applies) — drafting the Clozapine evaluation report from the evidence pack.

A few judgment calls, flagged here rather than folded silently into the report:
- The evidence pack's own field is `taiwan_regulatory` (candidate_id `TW-...`, gap items reference "TFDA") — I labeled market sections "Taiwan" rather than the template's literal "India," since printing "India" against Taiwan-sourced data would be a factual error.
- `predicted_indications[0]` (manic bipolar affective disorder, L2) is used as the headline indication per the template's literal instruction, but "bipolar disorder" (rank 5) and "psychotic disorder" (rank 9) in the same pack carry stronger L1 evidence — noted in the Conclusion rather than silently substituted.
- `original_indications` and `original_moa` are empty/`[Data Gap]` in this pack; I used Clozapine's well-established global original indication (treatment-resistant schizophrenia) for the title/context, explicitly marked as general pharmacological knowledge rather than TFDA-sourced data, since Taiwan has zero license records (drug not marketed there).

---

# Clozapine: From Treatment-Resistant Schizophrenia to Manic Bipolar Affective Disorder

## One-Sentence Summary

Clozapine is a second-generation (atypical) antipsychotic globally established for treatment-resistant schizophrenia, though it currently holds no marketing license in Taiwan. The TxGNN model's top-ranked prediction is that it may be effective for **manic bipolar affective disorder**, with **6 clinical trials** and **20 publications** currently identified in support of this direction — though the strongest bipolar-spectrum evidence in this evidence pack actually sits under the broader "bipolar disorder" label (see Conclusion).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment-resistant schizophrenia (general pharmacological knowledge; no Taiwan-specific indication text available — drug not marketed locally) |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank-sourced mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on established pharmacological knowledge, Clozapine is an atypical antipsychotic combining dopamine D2/D4 and serotonin 5-HT2A receptor antagonism, along with activity at histaminergic, cholinergic, and adrenergic receptors. Its efficacy in treatment-resistant schizophrenia is well proven, and this same D2/5-HT2A antagonist profile underlies the antimanic and mood-stabilizing effects seen across other atypical antipsychotics.

Mania and psychosis share substantial neurobiological overlap (dopaminergic dysregulation in both), which supports the mechanistic plausibility of the TxGNN prediction. This is reinforced by direct clinical evidence: a completed Phase 2 double-blind trial (NCT00029458) specifically tested clozapine in treatment-resistant manic bipolar patients, and clozapine is already used clinically, off-label, in mania and bipolar disorder refractory to standard mood stabilizers and other antipsychotics. Notably, the same evidence pack shows even stronger, more mature evidence (L1, completed Phase 3 RCT) for the broader "bipolar disorder" label, suggesting the mechanistic link is genuine but that the specific "manic" subtype diagnosis is still under-studied relative to bipolar disorder as a whole.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00029458](https://clinicaltrials.gov/study/NCT00029458) | Phase 2 | Completed | 42 | Double-blind study of clozapine safety/efficacy in treatment-resistant manic phase of bipolar disorder |
| [NCT05603104](https://clinicaltrials.gov/study/NCT05603104) | Phase 3 | Recruiting | 1254 | Intensified pharmacological treatment (including antipsychotics) for schizophrenia, MDD and bipolar depression after first-line treatment failure |
| [NCT07047651](https://clinicaltrials.gov/study/NCT07047651) | Phase 4 | Recruiting | 40 | Pharmacotherapy combined with recovery-oriented psychosocial programs for treatment-resistant schizophrenia and treatment-resistant bipolar disorder |
| [NCT06993662](https://clinicaltrials.gov/study/NCT06993662) | Phase 1 | Active, not recruiting | 107 | Combined pharmacotherapy and cognitive behavioral therapy for mental health disorders in private practice |
| [NCT07398365](https://clinicaltrials.gov/study/NCT07398365) | N/A | Recruiting | 100 | Observational phenotyping of general adult psychiatry inpatients |
| [NCT03651674](https://clinicaltrials.gov/study/NCT03651674) | N/A | Unknown | 200 | MRI study of brain structure/function changes after ECT in schizophrenia and bipolar disorder |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32182485](https://pubmed.ncbi.nlm.nih.gov/32182485/) | 2020 | Systematic Review/Meta-analysis | Journal of Psychiatric Research | Assesses clinical efficacy and adverse effect profile of clozapine in bipolar disorder |
| [33719158](https://pubmed.ncbi.nlm.nih.gov/33719158/) | 2021 | Review | Bipolar Disorders | Summarizes current evidence and open questions on clozapine for bipolar disorder |
| [25346322](https://pubmed.ncbi.nlm.nih.gov/25346322/) | 2015 | Systematic Review | Bipolar Disorders | Evaluates efficacy and safety of clozapine for treatment-resistant bipolar disorder |
| [31488793](https://pubmed.ncbi.nlm.nih.gov/31488793/) | 2019 | Review | Psychiatria Danubina | Discusses clozapine's anti-suicidal and anti-aggressive properties as a potential treatment for suicidality in bipolar disorder |
| [37068038](https://pubmed.ncbi.nlm.nih.gov/37068038/) | 2023 | Cohort (Asian multi-center prescribing study) | Journal of Clinical Psychopharmacology | Pharmacoepidemiological patterns of clozapine use for bipolar disorder in Asia |
| [16432528](https://pubmed.ncbi.nlm.nih.gov/16432528/) | 2006 | Review | Molecular Psychiatry | Reviews treatment-resistant bipolar disorder management including clozapine's role |
| [11280956](https://pubmed.ncbi.nlm.nih.gov/11280956/) | 2001 | Review | Bulletin of the Menninger Clinic | Reviews pharmacotherapy options for treatment-resistant bipolar disorder |
| [40174308](https://pubmed.ncbi.nlm.nih.gov/40174308/) | 2025 | Cohort (nationwide retrospective) | Journal of Psychiatric Research | Real-world Korean cohort evaluating anti-suicidal effectiveness of clozapine, lithium, and valproate in schizophrenia/bipolar disorder |
| [31567198](https://pubmed.ncbi.nlm.nih.gov/31567198/) | 2021 | Review | American Journal of Therapeutics | Discusses rapid clozapine titration protocols in schizophrenia and bipolar disorder |
| [10682225](https://pubmed.ncbi.nlm.nih.gov/10682225/) | 2000 | Case series | Clinical Neuropharmacology | Review of 36 patients treated with combined ECT-clozapine therapy, 67% benefit rate |

---

## Taiwan Market Information

Clozapine currently holds **no marketing authorization in Taiwan** (0 registrations on file in this evidence pack), so no license table is presented.

---

## Safety Considerations

**Drug Interactions**: Query returned 449 total interactions. Notable **Major**-level interactions include Bupropion, Morphine, and Potassium citrate. Multiple **Moderate**-level interactions were also identified, including Metformin, Omeprazole, Cimetidine, Famotidine, and several antidiabetic agents (Acarbose, Alogliptin, Canagliflozin, Pioglitazone, Chlorpropamide).

Please refer to the package insert for full warnings and contraindications — this data is not currently available in the evidence pack (Blocking gap, DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking-severity data gap (DG001: TFDA label warnings/contraindications) prevents even an initial safety assessment (S1) for this drug, regardless of efficacy evidence.
- Evidence specific to the "manic bipolar affective disorder" subtype is limited to one completed Phase 2 RCT (n=42) and an ongoing Phase 3 trial not exclusively focused on this population — L2 evidence.
- Clozapine has zero existing marketing authorization in Taiwan, meaning any repurposing pathway would require a full new registration rather than a label extension.
- Note: within this same evidence pack, the broader **"bipolar disorder"** and **"psychotic disorder"** labels both carry **L1** evidence (completed Phase 3 RCTs, e.g., NCT00036582) and a **Proceed with Guardrails** recommendation — these are stronger near-term candidates than the narrower manic subtype evaluated here.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (resolve DG001 — blocking)
- DrugBank mechanism-of-action data (resolve DG002)
- Re-evaluation prioritizing the "bipolar disorder" and "psychotic disorder" predictions, which already meet L1 evidence thresholds
- Given Clozapine's known agranulocytosis risk class, a hematological monitoring plan will be required before any clinical development step, once official labeling data is obtained
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

