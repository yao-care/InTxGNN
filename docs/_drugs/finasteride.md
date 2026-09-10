---
layout: default
title: Finasteride
parent: 僅模型預測 (L5)
nav_order: 351
evidence_level: L5
indication_count: 6
---

# Finasteride
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

# Finasteride: From Androgenetic Alopecia to Hypertrichosis

## One-Sentence Summary

Finasteride is a 5α-reductase inhibitor established for androgen-dependent hair loss (androgenetic alopecia) and benign prostatic hyperplasia. The TxGNN model predicts a possible role in **Hypertrichosis**, with **1 loosely related clinical trial** and **4 review articles** currently available — but the evidence is preclinical/mechanism-level rather than direct RCT support, and the drug is not currently marketed in India.

*Note: TxGNN's top-ranked candidate (Ambras type hypertrichosis, score 99.99%) was excluded from this report — it has zero supporting trials or literature, and the evidence pack itself flags it as likely knowledge-graph noise (a congenital, non-androgen-dependent condition with no mechanistic link to 5α-reductase inhibition). Hypertrichosis (disease) at rank 2 is the only candidate with any supporting evidence and is used here instead.*

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Androgenetic alopecia (male pattern hair loss) — per literature evidence in this pack; no India-approved indication text is available since the drug is not marketed in India |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.99% (0.99993) |
| Evidence Level | L4 (mechanism/preclinical + off-label clinical experience, no dedicated RCT) |
| India Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in structured form (flagged as a High-severity data gap). Based on known pharmacology, finasteride is a type 1/2 5α-reductase inhibitor that blocks conversion of testosterone to dihydrotestosterone (DHT), the mechanism underlying its efficacy in androgen-dependent hair loss.

Hypertrichosis is a broad, heterogeneous category. Its androgen-dependent subtype — hirsutism — shares the same DHT pathway that finasteride already modulates, and off-label clinical experience using finasteride in women with hirsutism has been documented in the literature retrieved here. This gives a plausible, if indirect, mechanistic rationale: lowering DHT could theoretically dampen androgen-driven excess hair growth, the inverse effect of what finasteride achieves on the scalp in androgenetic alopecia.

However, hypertrichosis as a whole also includes non-androgen-dependent forms (congenital, drug-induced, metabolic, paraneoplastic), where this mechanism does not apply. None of the retrieved literature or trials directly studied finasteride in a hypertrichosis/hirsutism population — the connection is inferred from review-level commentary, not tested outcomes.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04293822](https://clinicaltrials.gov/study/NCT04293822) | Phase 4 | Unknown | 60 | Compares topical cetirizine gel vs. minoxidil 5% gel for androgenetic alopecia (hair loss, not hypertrichosis). Does not test finasteride. Retrieved only via topical proximity in the hair-disease knowledge graph (relevance grade C); not direct supporting evidence. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12942187](https://pubmed.ncbi.nlm.nih.gov/12942187/) | 2003 | Review | Der Hautarzt | Notes finasteride's established role in male pattern hair loss alongside laser hair removal for hypertrichosis/hirsutism, without testing finasteride for the latter. |
| [12223963](https://pubmed.ncbi.nlm.nih.gov/12223963/) | 2002 | Review | Annales de dermatologie et de venereologie | Distinguishes hypertrichosis (non-androgen-dependent) from hirsutism (androgen-dependent); lists iatrogenic, metabolic, and paraneoplastic causes of hypertrichosis. |
| [10330884](https://pubmed.ncbi.nlm.nih.gov/10330884/) | 1999 | Review | Therapeutische Umschau | Reviews oral treatment options, including antiandrogens, for androgenetic alopecia and hirsutism. |
| [12444520](https://pubmed.ncbi.nlm.nih.gov/12444520/) | 2002 | Review | Der Hautarzt | Describes TrichoScan, a digital hair-analysis tool for monitoring hair loss/growth treatment response; general methodology, not disease-specific efficacy data. |

## India Market Information

Finasteride is currently **not marketed in India** (0 registrations on file), so no license or approved-indication data is available for this evidence pack.

## Safety Considerations

- **Drug Interactions**: 321 potential interactions identified via the DDInter database; severity levels are not classified in the source data ("Unknown"). Representative interacting drugs include Calcitriol, Doxycycline, Clotrimazole, Dolasetron, Dicyclomine, Chlorhexidine, Famotidine, Acetylsalicylic acid, Amoxicillin, Bupropion, Pantoprazole, Glimepiride, Mesalazine, Acarbose, Morphine, Metformin, Omeprazole, Sucralfate, Palonosetron, and Rosiglitazone.

Official warnings and contraindications (e.g., from a local product label) are not available in this evidence pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (DHT suppression) plausibly applies only to the androgen-dependent subset (hirsutism) of the broader hypertrichosis category, and no clinical trial or study directly tests finasteride in this population — evidence is L4 (mechanism/review-level only). The drug is also unmarketed in India, and safety-critical data (label warnings, contraindications) is a Blocking-severity gap that prevents a proper S1 safety evaluation.

**To proceed, the following is needed:**
- Official product label / warnings and contraindications data (currently blocking safety review)
- Confirmed mechanism of action documentation (currently a data gap)
- Narrow the target population from "hypertrichosis" to specifically androgen-dependent hirsutism, where the mechanistic link is strongest
- A dedicated clinical study (even small/observational) testing finasteride in hirsutism, since current literature is review-level only
- DDI severity classification, since all 321 interactions are currently listed as "Unknown" level
- Regulatory pathway assessment given the drug is not currently marketed in India
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

