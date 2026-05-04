---
layout: default
title: Ademetionine
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 10
---

# Ademetionine
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

# Ademetionine: From Hepatic Support to Acne

## One-Sentence Summary

Ademetionine (S-Adenosylmethionine, SAMe) is a naturally occurring compound serving as the body's universal methyl donor, widely used internationally as a pharmaceutical and dietary supplement for liver disease and mood disorders.
The TxGNN model predicts it may also be effective for **Acne**, with **1 clinical trial** (conducted in a combination supplement context) currently providing supporting evidence.
Notably, the Rank 2 prediction — **Colonic Neoplasm** — carries substantially stronger evidence (1 clinical trial + 20 publications, Evidence Level L2) and warrants parallel consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no local registration; SAMe internationally used for intrahepatic cholestasis and depression) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Ademetionine in this Evidence Pack. Based on known information, Ademetionine (SAMe) is the body's principal biological methyl donor, generated through the methionine cycle, and serves as a critical upstream precursor to glutathione — the cell's primary antioxidant defense molecule. In markets where it is approved as a pharmaceutical (e.g., Italy, Germany), SAMe is indicated for intrahepatic cholestasis, depression, and osteoarthritis.

Acne vulgaris involves two interconnected pathological processes: (1) oxidative stress within sebaceous glands, and (2) pro-inflammatory signaling (IL-1β, TNF-α) triggered by *Cutibacterium acnes*. SAMe's role as a glutathione precursor could theoretically reduce oxidative burden at the skin level, while its documented anti-inflammatory properties may dampen acne-associated cytokine activity. However, this mechanistic rationale is general in nature — it applies broadly to any oxidative or inflammatory condition — and is not acne-specific.

The sole supporting clinical trial (NCT05340634) tested a multi-component combination product (Metionac: ALA + NAC + Vitamin B6 + SAMe) in patients with Polycystic Ovary Syndrome (PCOS), a condition commonly manifesting with acne as a secondary feature. Since SAMe was only one of several active antioxidant ingredients, its individual contribution to any observed skin improvement cannot be isolated. This substantially limits the strength of attribution.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05340634](https://clinicaltrials.gov/study/NCT05340634) | Phase 4 | Completed | 90 | Combination antioxidant supplement (ALA, NAC, Vitamin B6, SAMe) evaluated for metabolic and endocrine improvement in PCOS; acne is a recognised manifestation of PCOS but was not the primary endpoint; SAMe's individual contribution to skin improvement cannot be isolated from other components |

---

## India Market Information

Ademetionine has no registered products on record in the local market (0 authorizations found). The drug is not currently marketed.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The sole clinical evidence is a completed Phase 4 trial evaluating a multi-component combination supplement in PCOS patients — a study design that precludes any direct attribution of benefit to SAMe alone. While the antioxidant and anti-inflammatory mechanisms are biologically plausible, they are non-specific and insufficient to support advancement without dedicated SAMe monotherapy data in acne populations.

**To proceed, the following is needed:**
- A dedicated clinical study evaluating SAMe as a primary intervention specifically for acne vulgaris (monotherapy or with clearly defined contribution)
- Mechanistic studies confirming SAMe's direct effect on sebaceous gland oxidative stress and *C. acnes*-induced IL-1β/TNF-α signaling
- Full safety profile including key warnings, contraindications, and drug interactions (retrieve from package insert PDF or DrugBank API for DB00118)
- MOA documentation from DrugBank (DB00118) to enable mechanistic linkage analysis
- Regulatory classification review in India: prescription drug vs. dietary supplement status
- **Recommended parallel action:** Advance Rank 2 prediction (Colonic Neoplasm, Evidence Level L2) to a separate full evaluation report, as that indication is supported by substantially stronger and more direct evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

