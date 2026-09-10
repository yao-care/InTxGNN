---
layout: default
title: Hydrocortisone
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 10
---

# Hydrocortisone
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

Using data-report principles (output reflects source data faithfully, no fabrication) since this is a structured evidence-to-report task with a fixed template — proceeding directly to compose it.

# Hydrocortisone: From Corticosteroid Anti-Inflammatory Therapy to Alopecia Areata

## One-Sentence Summary

Hydrocortisone is a glucocorticoid receptor agonist with established anti-inflammatory and immunomodulatory activity; no India/Taiwan market approval data is currently on file for its original indication(s). The TxGNN model predicts it may be effective for **Alopecia Areata**, supported by **4 clinical trials** (including a completed Phase 3 RCT using hydrocortisone itself as the active comparator) and **20 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no India/Taiwan license records on file (see India Market Information) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| India Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for hydrocortisone is not available in a structured field (DG002, High severity). However, the evidence pack's repurposing rationale describes hydrocortisone as a **glucocorticoid receptor agonist** with anti-inflammatory and immunomodulatory properties. In alopecia areata, autoimmune-mediated T-cell attack against hair follicles disrupts the follicle's normal "immune privilege." Glucocorticoid signaling can suppress this local T-cell activity and help restore that immune privilege.

This is not a novel mechanistic hypothesis — topical and intralesional corticosteroids (including hydrocortisone) are already part of routine clinical management for alopecia areata. This is corroborated directly in the evidence: a completed Phase 3 RCT (NCT01453686) used **Hydrocortisone 1% cream** as the active comparator against clobetasol propionate in pediatric AA patients, and multiple historical case series (1956–1966) specifically document intradermal/intracutaneous hydrocortisone injection for AA. The TxGNN prediction therefore aligns with decades of documented clinical use of hydrocortisone in this indication, rather than representing a mechanistically unprecedented repurposing candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Completed | 41 | RCT comparing Clobetasol Propionate 0.05% cream vs. **Hydrocortisone 1% cream** in children with alopecia areata; hydrocortisone used as the active control arm. |
| [NCT00484679](https://clinicaltrials.gov/study/NCT00484679) | Phase 2 | Completed | 18 | Evaluated adrenal function impact of intralesional triamcinolone acetonide (same corticosteroid class) in AA patients — supports class-level rationale rather than hydrocortisone itself. |
| [NCT06551818](https://clinicaltrials.gov/study/NCT06551818) | N/A | Not Yet Recruiting | 72 | Four-arm dose-response, placebo-controlled study of hair growth products in androgenic alopecia; title does not confirm a hydrocortisone-containing arm. |
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | Completed | 380 | Studied effects of abnormal steroid metabolome on bone strength/density and body composition, not an AA efficacy trial; only indirectly relevant via steroid exposure. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | RCT | JAMA Dermatology | Randomized trial: clobetasol propionate 0.05% vs. hydrocortisone 1% for alopecia areata in children. |
| [36718837](https://pubmed.ncbi.nlm.nih.gov/36718837/) | 2023 | Systematic Review/Meta-analysis | Journal of Cosmetic Dermatology | Reviews AA treatment landscape (fractional laser ± other therapies); no FDA-approved device exists for baldness, framing corticosteroids among current options. |
| [38501938](https://pubmed.ncbi.nlm.nih.gov/38501938/) | 2024 | Cohort/Clinical Study | Clinical and Experimental Dermatology | Retrospective analysis of topical corticosteroid under occlusion for severe pediatric AA (including alopecia totalis/universalis), where treatment options are otherwise limited. |
| [28516731](https://pubmed.ncbi.nlm.nih.gov/28516731/) | 2017 | Review | J Eur Acad Dermatol Venereol | Reviews the role of HPA-axis activity and cortisol/MSH production in AA pathophysiology. |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Case Series | Medical Times | Early case series treating alopecia areata, partialis, and totalis with cortisone, hydrocortisone, prednisone, and prednisolone. |
| [13610145](https://pubmed.ncbi.nlm.nih.gov/13610145/) | 1958 | Case Report | Der Hautarzt | Reports hair regrowth in alopecia areata and alopecia maligna following intracutaneous hydrocortisone injection. |
| [5989830](https://pubmed.ncbi.nlm.nih.gov/5989830/) | 1966 | Case Report | Vestnik Dermatologii i Venerologii | Treatment of AA and total alopecia via intracutaneous hydrocortisone injections. |
| [14158891](https://pubmed.ncbi.nlm.nih.gov/14158891/) | 1963 | Case Report | Actas Dermo-Sifiliograficas | Treatment of alopecia areata with intradermal hydrocortisone injections. |
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Case Report | J Am Acad Dermatol | Describes 4 cases of congenital alopecia areata treated with minoxidil and topical agents; background context on disease course. |
| [39506493](https://pubmed.ncbi.nlm.nih.gov/39506493/) | 2025 | Exploratory Clinical Study | Journal of Cosmetic Dermatology | Notes psychological stress triggers dermatoses including alopecia areata via cortisol/epinephrine release — mechanistic background on cortisol's role in disease pathogenesis. |

---

## India Market Information

No drug license or registration records are currently on file for hydrocortisone in this market — `taiwan_regulatory.market_status` is **未上市 (Not Marketed)** with **0** registrations. Original indication and formulation data cannot be extracted until this gap is resolved.

---

## Safety Considerations

- **Drug Interactions**: 722 total interactions on file (DDInter). Notable examples include a **Major**-level interaction with **Adalimumab**, and multiple **Moderate**-level interactions including Zidovudine, Isotretinoin, Acarbose, Acebutolol, Acetazolamide, Ketorolac, Nifedipine, Ibuprofen, Ethinylestradiol, and several vaccine antigens (e.g., tetanus toxoid, adenovirus antigen), reflecting hydrocortisone's broad immunosuppressive and metabolic interaction profile. Given the volume (722 total), a full interaction screen against the patient's concurrent medication list is required before use.

Key warnings and contraindications are not available in this evidence pack (DG001, Blocking severity) — please refer to the official package insert for this information once sourced from the regulatory agency.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The lead candidate indication (alopecia areata) is supported by an L1 evidence level, including a completed Phase 3 RCT that used hydrocortisone itself as an active treatment arm, plus a multi-decade documented history of corticosteroid (including hydrocortisone) use in this condition. This is a mechanistically well-precedented repurposing candidate rather than a purely model-driven speculation. Note that among the other 9 TxGNN-predicted indications in this evidence pack (e.g., alopecia mucinosa, telogen effluvium, idiopathic steroid-sensitive nephrotic syndrome), only idiopathic steroid-sensitive nephrotic syndrome reaches a moderate evidence tier (L3, "Research Question"); the remainder are L4–L5 with a "Hold" recommendation due to absent or indirect literature/trial support.

**To proceed, the following is needed:**
- TFDA/local regulatory label — warnings, contraindications, and precautions (DG001, blocking S1 safety screening)
- Structured mechanism-of-action documentation (DG002)
- Local market registration and dosage-form data for this jurisdiction (currently 未上市/not marketed with 0 licenses)
- Formal DDI risk-tiering against likely AA co-medications (e.g., other immunomodulators) given the 722-interaction dataset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

