---
layout: default
title: Benzoyl Peroxide
parent: 僅模型預測 (L5)
nav_order: 100
evidence_level: L5
indication_count: 4
---

# Benzoyl Peroxide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Benzoyl Peroxide: From Acne Vulgaris to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Benzoyl peroxide (BPO) is a well-established topical antibacterial and keratolytic agent, widely used for the treatment of acne vulgaris.
The TxGNN model predicts it may be effective for **Vulvar Inverted Follicular Keratosis**,
with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acne vulgaris (widely recognized clinical use; not listed in current Indian regulatory data) |
| Predicted New Indication | Vulvar Inverted Follicular Keratosis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, benzoyl peroxide is a topical oxidizing agent with two primary activities: **(1) antibacterial action** — it releases free radical oxygen that oxidizes bacterial proteins, substantially reducing *Cutibacterium acnes* colonization on the skin surface; **(2) keratolytic action** — it promotes epidermal desquamation and reduces follicular plugging, making it effective against conditions involving abnormal keratinization.

Vulvar inverted follicular keratosis (VIFK) is a rare, benign neoplastic lesion characterized by an endophytic squamous proliferation with distinctive squamous eddies (whorls of squamous cells). While BPO's keratolytic properties might conceptually apply to hyperkeratotic follicular conditions, VIFK's underlying pathology is fundamentally different — it represents a true benign squamoproliferative tumor rather than a condition driven by chronic bacterial infection or simple reactive hyperkeratosis. The pathological hallmark is a structured neoplastic growth, not follicular obstruction or microbial dysbiosis.

The TxGNN knowledge graph likely captured a structural node similarity between "follicular keratosis"-type conditions and BPO's known interactions, generating this high-score prediction. However, the mechanistic link is considered weak: BPO has no known anti-neoplastic mechanism, and there is no biological rationale for it to resolve established VIFK lesions. This signal is best interpreted as a hypothesis-generating artifact of the graph topology rather than a clinically actionable prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Benzoyl peroxide has **no current registrations** with the Indian regulatory authority (CDSCO) based on available data. The drug is classified as **Not Marketed** in India.

> Note: BPO is widely available as an over-the-counter and prescription topical agent in many other markets (US, EU, Australia). The absence of CDSCO registrations in this dataset may reflect data coverage limitations and should be verified directly with CDSCO records.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data including key warnings, contraindications, and drug interactions were not available in this Evidence Pack. Retrieval of the CDSCO/TFDA package insert PDF is recommended as a remediation step before proceeding to any safety assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN prediction score is exceptionally high (99.92%), this score reflects the model's graph-structural inference and does not correspond to clinical evidence. Vulvar inverted follicular keratosis is a rare benign squamous neoplasm with a pathological mechanism that is biologically distinct from BPO's known keratolytic and antibacterial targets; no supporting clinical trials or literature have been identified for this indication.

**To proceed, the following is needed:**
- **MOA data retrieval**: Query DrugBank API for complete mechanism of action, pharmacodynamics, and targets for DB09096
- **Safety profile completion**: Download and parse the CDSCO/TFDA package insert PDF to obtain contraindications, key warnings, and DDI data
- **Biological plausibility review**: Commission a dermatopathology expert opinion on whether any aspect of BPO's mechanism (oxidative stress reduction, keratolysis) could intersect with VIFK pathogenesis
- **Indication re-prioritization**: Consider redirecting evaluation effort toward rank 4 (**Acne Keloid / Acne Keloidalis Nuchae**), which carries partial supporting evidence (1 clinical trial, 2 publications) and a stronger mechanistic rationale for BPO's anti-inflammatory and keratolytic properties
- **India market verification**: Confirm CDSCO registration status through direct database query, as OTC BPO products may be marketed without formal registration records in this dataset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

