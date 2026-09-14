---
layout: default
title: Vildagliptin
parent: 僅模型預測 (L5)
nav_order: 880
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

Using no additional skill — this is a direct content-generation task fully specified by the report template already provided; I'll produce the Markdown report directly from the Evidence Pack.

Note before the report: this Evidence Pack lists **10** TxGNN-predicted indications for Vildagliptin, not one. Nine of them (ranks 1–9: focal stiff limb syndrome, classic stiff person syndrome, thiamine-responsive dysfunction syndrome, opsismodysplasia, and four lipodystrophy variants, pancreatic agenesis) score higher than rank 10, but the Evidence Pack's own `repurposing_rationale` explicitly flags them as knowledge-graph artifacts / false positives with zero supporting trials or literature (all L5/Hold). Only rank 10 — **Type 1 Diabetes Mellitus** — has real clinical trial and literature support (L2/S2). I built the report around that indication rather than the literal top-ranked score, since reporting a zero-evidence prediction as the headline would misrepresent the drug's actual repurposing potential. The screened-out candidates are summarized separately below so nothing is hidden.

---

# Vildagliptin: From Type 2 Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

> Vildagliptin is a DPP-4 inhibitor originally used to manage type 2 diabetes mellitus (T2DM).
> Among the model's predictions, the only one with actual supporting evidence is **Type 1 Diabetes Mellitus (T1DM)**,
> where DPP-4 inhibition may help preserve β-cell function and stabilize glucagon counterregulation,
> supported by **3 T1DM-specific clinical trials** and **10+ relevant publications** (including one RCT).
> Nine other higher-scoring TxGNN predictions (e.g., stiff person syndrome, various lipodystrophies) were reviewed and excluded — they have no clinical trials, no literature, and are flagged by the evidence pipeline itself as likely false positives.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (per pharmacology profile data; no India/Taiwan approved label text available — drug not marketed there) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.37% (rank 10,073 of full candidate list) |
| Evidence Level | L2 |
| India Market Status | ✗ Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

DrugBank's structured MOA field is not populated for this drug, but pharmacological target-binding data in the Evidence Pack fill the gap directly: vildagliptin binds **dipeptidyl peptidase-4 (DPP4)** as its primary target, with additional (lower-affinity, off-target) activity against **DPP8**, **DPP9**, and **TRPV4**. As a DPP-4 inhibitor, it blocks degradation of the endogenous incretins GLP-1 and GIP, which enhances glucose-dependent insulin secretion and suppresses inappropriate glucagon release — the established mechanism underlying its approved use in T2DM.

The rationale for exploring T1DM rests on the same incretin axis, applied to a different pathophysiology. T1DM is primarily autoimmune β-cell destruction rather than insulin resistance, but published mechanistic and clinical work shows vildagliptin also suppresses glucagon during hyperglycemia and sustains glucagon counterregulation during hypoglycemia in T1DM patients (PMID 22855332), and preclinical models suggest a possible β-cell protective/neogenic effect in residual β-cell populations (PMID 25395211, 23523961). A completed RCT combining vildagliptin with rapamycin specifically tested β-cell function recovery in long-standing T1DM (PMID 33124663).

This is fundamentally an off-label mechanistic extension — β-cell preservation and glucagon modulation in an autoimmune disease — rather than a direct extrapolation of the T2DM efficacy data. The evidence base is real but early-stage (small trials, mixed endpoints, no confirmatory Phase 3 in T1DM), which is reflected in the L2/S2 "Research Question" classification assigned in the Evidence Pack.

**Other TxGNN predictions screened out:** The nine higher-scoring candidates (focal stiff limb syndrome, classic stiff person syndrome, thiamine-responsive dysfunction syndrome, opsismodysplasia, four localized lipodystrophy subtypes, and pancreatic agenesis) all carry an L5/Hold rating with no clinical trials or literature. Per the pack's own rationale notes, several of these appear to be driven by a generic "diabetes comorbidity" path in the knowledge graph rather than any DPP-4-specific mechanism, and in the case of pancreatic agenesis, the retrieved literature was a keyword mismatch (general DPP-4 pancreatic safety studies, not the congenital disorder itself). These are not carried forward in this report.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01147276](https://clinicaltrials.gov/study/NCT01147276) | Phase 4 | Completed | 28 | Vildagliptin's effect on glucagon counterregulation during hypoglycemia in T1DM patients — directly relevant T1DM trial |
| [NCT06021119](https://clinicaltrials.gov/study/NCT06021119) | Phase 3 | Completed | 50 | Add-on vildagliptin reduced Ramadan Iftar-related glycemic excursions in adolescents/young adults with T1DM on a hybrid closed-loop system |
| [NCT06348706](https://clinicaltrials.gov/study/NCT06348706) | Phase 3 | Completed | 60 | DPP-4 inhibitor supplementation evaluated for non-alcoholic steatohepatitis in adolescents with T1DM |
| [NCT00099853](https://clinicaltrials.gov/study/NCT00099853) | Phase 3 | Completed | 362 | Low relevance — T2DM population (vildagliptin + pioglitazone), not T1DM |
| [NCT01472432](https://clinicaltrials.gov/study/NCT01472432) | Phase 4 | Completed | 106 | Low relevance — T2DM chronic foot ulcer healing, not T1DM |
| [NCT02475499](https://clinicaltrials.gov/study/NCT02475499) | N/A | Completed | 886,172 | Low relevance — T2DM population, pancreatic cancer risk observational study |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33124663](https://pubmed.ncbi.nlm.nih.gov/33124663/) | 2021 | RCT | J Clin Endocrinol Metab | Rapamycin + vildagliptin double-blind RCT testing β-cell function recovery in long-standing T1DM |
| [38057844](https://pubmed.ncbi.nlm.nih.gov/38057844/) | 2023 | Cohort/Clinical | Diabetol Metab Syndr | Adjunctive oral vildagliptin reduced Iftar-related glycemic excursions in T1DM adolescents/young adults on AHCL system |
| [30848158](https://pubmed.ncbi.nlm.nih.gov/30848158/) | 2019 | Review | Expert Opin Investig Drugs | DPP-4 inhibitors show β-cell protective and renal effects in both T2DM and T1DM |
| [22855332](https://pubmed.ncbi.nlm.nih.gov/22855332/) | 2012 | Clinical study | J Clin Endocrinol Metab | Vildagliptin reduces glucagon during hyperglycemia and sustains glucagon counterregulation during hypoglycemia in T1DM |
| [31781045](https://pubmed.ncbi.nlm.nih.gov/31781045/) | 2019 | Mechanism review | Front Endocrinol | Reviews GLP-1/GIP actions underlying vildagliptin's insulin-secretion effects |
| [39318059](https://pubmed.ncbi.nlm.nih.gov/39318059/) | 2024 | RCT | Diabetes Obes Metab | Vildagliptin add-on effects on MMP-14, liver stiffness, and subclinical atherosclerosis in adolescents with T1DM and NASH |
| [25395211](https://pubmed.ncbi.nlm.nih.gov/25395211/) | 2015 | Preclinical (rat) | Curr Pharm Biotechnol | Vildagliptin induces β-cell neogenesis and improves lipid profile in a later phase of experimental T1DM |
| [23523961](https://pubmed.ncbi.nlm.nih.gov/23523961/) | 2013 | Preclinical (rat) | Arch Med Res | Vildagliptin ameliorates oxidative stress and β-cell destruction in T1DM rats |
| [18597213](https://pubmed.ncbi.nlm.nih.gov/18597213/) | 2008 | Clinical study | Horm Metab Res | Effect of vildagliptin on meal-related glucagon concentration in T1DM patients |
| [21727749](https://pubmed.ncbi.nlm.nih.gov/21727749/) | 2011 | Review | Ann Saudi Med | Reviews glycemic therapy options during Ramadan fasting, including DPP-4 inhibitors in T1DM/T2DM |

## India Market Information

Vildagliptin currently has **no market authorization in India** (`market_status: 未上市`, 0 registered licenses). No product registration data is available to summarize.

## Safety Considerations

Formal safety warnings and contraindications are not available in this Evidence Pack (labeled data gap, source: TFDA/India labeling — not yet retrieved). Pharmacological target-binding data indicate vildagliptin is selective for DPP4 over the related enzymes DPP8 and DPP9; off-target DPP8/9 inhibition has historically been a toxicity concern flagged for compounds in this class during nonclinical development, so selectivity margin is worth confirming once label data is available. No clinical drug-drug interaction data (as opposed to target-binding pharmacology) was returned.

Please refer to the package insert for full prescribing safety information once it is available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The drug carries a **blocking data gap** — TFDA/India label warnings and contraindications are unavailable, so no S1 safety review can be completed — and it is not currently marketed in India at all (0 registrations). Independent of the T1DM evidence quality, this alone precludes moving forward at this time.

**To proceed, the following is needed:**
- Retrieve TFDA/India label warnings and contraindications (DG001, Blocking) before any S1 safety screening
- Obtain formal MOA documentation from DrugBank (DG002, High) to replace the inferred pharmacology-profile summary used in this report
- If pursuing the T1DM signal specifically: seek larger confirmatory trials (current strongest evidence is one small RCT, PMID 33124663) before treating this as more than a research hypothesis
- Formally document exclusion rationale for the 9 lower-quality TxGNN predictions (ranks 1–9) so they are not mistakenly re-surfaced as high-score candidates in future automated scans
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

