---
layout: default
title: Risperidone
parent: 僅模型預測 (L5)
nav_order: 738
evidence_level: L5
indication_count: 6
---

# Risperidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Risperidone: From Schizophrenia/Bipolar Mania to Major Affective Disorder

## One-Sentence Summary

> Risperidone is a second-generation (atypical) antipsychotic originally used to treat schizophrenia and bipolar mania.
> The TxGNN model predicts it may also be effective for **Major Affective Disorder** (adjunctive therapy in bipolar disorder and treatment-resistant depression),
> with **36 clinical trials** and **20 publications** currently supporting this direction — the strongest-evidenced signal among six candidate indications screened in this evidence pack.

*Note: This evidence pack ("TW-DB00734-multi") contains six TxGNN-predicted indications ranked by raw prediction score. Four of them (gaze palsy with progressive scoliosis, Asperger susceptibility, amelocerebrohypohidrotic syndrome, and — to a lesser extent — Phelan-McDermid syndrome) are rare genetic/neurodevelopmental conditions with little to no supporting clinical evidence (L4–L5, "Hold"). This report focuses on the two candidates with actionable evidence: **Major Affective Disorder** (L1, primary focus below) and **Trichotillomania** (L3, secondary — see note in Conclusion).*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia / Bipolar Mania (not recorded in the supplied Taiwan regulatory data — see data gap below) |
| Predicted New Indication | Major Affective Disorder (bipolar disorder / treatment-resistant depression, adjunctive use) |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L1 |
| Taiwan Market Status | 未上市 (Not Marketed) per available regulatory data |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation was not available in this evidence pack (flagged as a High-severity data gap). However, the evidence pack's own repurposing rationale identifies Risperidone's established pharmacology: it is a dual dopamine D2 / serotonin 5-HT2A receptor antagonist. This mechanism is the pharmacological basis for its approved use in schizophrenia and bipolar mania.

Major affective disorder — encompassing bipolar disorder and treatment-resistant major depressive disorder (MDD) — shares overlapping neurobiology with psychotic and manic states, particularly dysregulated dopaminergic and serotonergic signaling in mood circuits. D2/5-HT2A antagonism is the established mechanistic basis for second-generation antipsychotics' role as antidepressant/mood-stabilizer augmentation agents, which is already reflected in clinical guidelines (e.g., FDA-approved SGA augmentation for MDD in other agents of this class).

This mechanistic plausibility is strongly reinforced by direct evidence: multiple completed Phase 3 RCTs test Risperidone specifically as monotherapy or augmentation in bipolar disorder and treatment-resistant depression, and several systematic reviews/meta-analyses (Cochrane, network meta-analyses) confirm efficacy signals for antipsychotic augmentation in this population. This is a mechanistically coherent and evidence-mature repurposing candidate, not merely a graph-similarity artifact.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00095134](https://clinicaltrials.gov/study/NCT00095134) | Phase 3 | Completed | 630 | Double-blind adjunctive Risperidone vs. placebo in MDD with sub-optimal antidepressant response |
| [NCT00391222](https://clinicaltrials.gov/study/NCT00391222) | Phase 3 | Completed | 585 | Risperidone LAI vs. placebo for prevention of mood episodes in bipolar I disorder |
| [NCT00044681](https://clinicaltrials.gov/study/NCT00044681) | Phase 3 | Completed | 258 | Risperidone augmentation of SSRI monotherapy in unipolar treatment-resistant depression, incl. long-term maintenance effect |
| [NCT00107939](https://clinicaltrials.gov/study/NCT00107939) | Phase 3 | Completed | 453 | Adjunctive therapy trial in bipolar I mania; atypical antipsychotics incl. Risperidone as background therapy |
| [NCT00057681](https://clinicaltrials.gov/study/NCT00057681) | Phase 3 | Completed | 379 | TEAM Study — lithium, valproate, and Risperidone compared in pediatric/adolescent bipolar mania |
| [NCT00176202](https://clinicaltrials.gov/study/NCT00176202) | Phase 3 | Completed | 65 | Risperidone vs. divalproex sodium with MRI assessment of circuitry in pediatric bipolar disorder |
| [NCT00277654](https://clinicaltrials.gov/study/NCT00277654) | Phase 3 | Completed | 111 | Randomized, double-blind, placebo-controlled Risperidone monotherapy in bipolar disorder with comorbid anxiety |
| [NCT00221403](https://clinicaltrials.gov/study/NCT00221403) | Phase 3 | Completed | 46 | Placebo-controlled trial of valproate and Risperidone in young children with bipolar disorder |
| [NCT00174577](https://clinicaltrials.gov/study/NCT00174577) | Phase 3 | Unknown | 84 | Risperidone augmentation in antidepressant partial/non-responders |
| [NCT01282632](https://clinicaltrials.gov/study/NCT01282632) | Phase 1/2 | Completed | 42 | Pilot comparison of Risperidone vs. olanzapine as antidepressant add-on in treatment-resistant depression |

*26 additional trials (mostly schizophrenia-focused, imaging/biomarker studies, or indirect comparator trials) were identified but are less directly relevant; full list available on request.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17975181](https://pubmed.ncbi.nlm.nih.gov/17975181/) | 2007 | RCT | Annals of Internal Medicine | Randomized trial of Risperidone for treatment-refractory major depressive disorder |
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Second-generation antipsychotics, incl. Risperidone, for MDD and dysthymia |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Systematic Review/Network Meta-analysis | J Affective Disorders | Comparative efficacy/discontinuation of augmentation agents (incl. Risperidone) in treatment-resistant depression |
| [35861202](https://pubmed.ncbi.nlm.nih.gov/35861202/) | 2023 | Systematic Review/Meta-analysis | J Psychopharmacology | Augmentation/combination treatments for early-stage treatment-resistant depression |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Systematic Review/Meta-analysis | Psychological Medicine | Efficacy and tolerability of antipsychotics (monotherapy and adjunctive) in MDD |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | Review | J Psychopharmacology | Comparative efficacy/tolerability: antidepressants + second-generation antipsychotics vs. esketamine vs. lithium |
| [24919175](https://pubmed.ncbi.nlm.nih.gov/24919175/) | 2014 | Meta-analysis | Braz J Med Biol Res | Efficacy/tolerability of antidepressant + atypical antipsychotic augmentation (17 trials, n=3807) in MDD |
| [25295435](https://pubmed.ncbi.nlm.nih.gov/25295435/) | 2014 | Nationwide population-based study | J Clinical Psychiatry | Real-world effectiveness of aripiprazole/olanzapine/quetiapine/Risperidone augmentation for MDD |
| [20486830](https://pubmed.ncbi.nlm.nih.gov/20486830/) | 2010 | Review | Expert Opin Pharmacother | Risperidone long-acting injection as monotherapy/adjunct in bipolar I maintenance treatment |
| [7545159](https://pubmed.ncbi.nlm.nih.gov/7545159/) | 1995 | Early clinical study | J Clinical Psychiatry | Early report on Risperidone's potential in affective illness beyond schizophrenia |

---

## Taiwan Market Information

No active registration records were found in the supplied regulatory dataset (0 licenses, market status "未上市"). This should be treated with caution: Risperidone is a globally established, long-marketed antipsychotic, and this "not marketed" status may reflect a data gap in the source registry (see DG001 below) rather than genuine absence from the Taiwan market. **This must be verified against the TFDA database directly before finalizing any regulatory conclusion.**

---

## Safety Considerations

- **Drug Interactions**: 362 documented interactions on file. Notable **Major**-severity interactions include **Bupropion** and **Morphine**. Numerous **Moderate**-severity interactions were identified with antidiabetic agents (Metformin, Alogliptin, Albiglutide, Canagliflozin), anticholinergics (Atropine, Hyoscyamine, Glycopyrronium, Clidinium), H2-blockers (Famotidine), and Epinephrine/Hydrocortisone. A **Minor** interaction was noted with Ranitidine.

Key warnings, contraindications, and TFDA package-insert data were not available in this evidence pack — please refer to the official package insert for full safety information once located.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Major Affective Disorder is supported by an L1 evidence level — multiple completed Phase 3 RCTs (including large trials with n=630 and n=585) plus several systematic reviews/meta-analyses consistently support Risperidone's efficacy as an augmentation or mood-stabilizing agent, and the D2/5-HT2A mechanism is well established for this use. However, blocking data gaps in local regulatory/safety documentation prevent an unconditional "Go."

**To proceed, the following is needed:**
- TFDA package-insert warnings and contraindications (DG001, **Blocking** — required before S1 safety review can proceed)
- Formal mechanism-of-action documentation from DrugBank (DG002)
- Verification of actual Taiwan market/registration status, given the discrepancy between "0 registrations" on file and Risperidone's known global availability
- A monitoring plan addressing the Major-severity interactions (Bupropion, Morphine) and the broader anticholinergic/antidiabetic interaction burden

**Secondary research question worth tracking:** Trichotillomania (L3, "Research Question") — supported by ~10 case reports/series over 25+ years showing consistent response signals as SSRI-augmentation therapy, but lacks controlled trial data. Not actionable for guideline-level repurposing yet, but warrants a dedicated small RCT if resources allow.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

