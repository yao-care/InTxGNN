---
layout: default
title: Calcipotriol
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 10
---

# Calcipotriol
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

# Calcipotriol: From Psoriasis to Seborrheic Keratosis

## One-Sentence Summary

Calcipotriol is a synthetic vitamin D3 analogue approved internationally for the treatment of plaque psoriasis, acting through the Vitamin D Receptor (VDR) to regulate keratinocyte differentiation and inhibit inflammatory signalling.
The TxGNN model predicts it may be effective for **Seborrheic Keratosis**, but there are currently **no clinical trials** and **no publications** directly supporting this specific direction.
This prediction is at the model-only stage and requires substantial mechanistic and clinical validation before further exploration is warranted.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Plaque psoriasis |
| Predicted New Indication | Seborrheic Keratosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Calcipotriol is a synthetic analogue of calcitriol (active vitamin D3) that binds to the Vitamin D Receptor (VDR), a nuclear receptor expressed on keratinocytes and immune cells. VDR activation inhibits keratinocyte hyperproliferation, promotes cellular differentiation, and suppresses pro-inflammatory cytokines (notably IL-17 and IL-23) — all of which underpin its effectiveness in psoriasis therapy.

Seborrheic keratosis (SK) is a common benign epidermal overgrowth characterised by keratinocyte hyperproliferation, frequently driven by activating somatic mutations in FGFR3 and PIK3CA signalling pathways. At a superficial level, a rationale exists: Calcipotriol inhibits keratinocyte proliferation, and SK involves keratinocyte overproduction. However, this reasoning does not hold under scrutiny.

SK is a genetically driven benign neoplasm — its proliferative driver is not inflammatory hyperproliferation (as in psoriasis) but rather oncogenic signalling through the FGFR3/PIK3CA axis, which VDR activation does not directly antagonise. Furthermore, SK carries negligible malignant transformation risk, so the unmet clinical need for a therapeutic agent is minimal. The high TxGNN prediction score most likely reflects the model generalising across "keratinising skin disorders" rather than detecting a disease-specific mechanistic link. Without published literature or clinical trial data, this prediction cannot be advanced beyond a hypothesis-generating finding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Calcipotriol is currently **not marketed in India**. No drug licences have been issued by CDSCO for this compound as of the data cut-off date (2026-04-10).

---

## Safety Considerations

**Drug Interactions**: The DDinter database has flagged **84 potential drug interactions** for Calcipotriol. All interactions are currently classified as **Unknown severity**, which limits their direct clinical utility for risk stratification. Flagged drug classes include:

- Corticosteroids: Prednisone, Prednisolone, Hydrocortisone, Triamcinolone
- Proton pump inhibitors: Omeprazole, Pantoprazole, Lansoprazole, Rabeprazole
- Antibiotics: Doxycycline, Clarithromycin, Vancomycin
- Antidiabetics: Metformin, Rosiglitazone, Glyburide
- Others: Aspirin, Simvastatin, Sulfasalazine, Morphine, Bupropion, Clotrimazole

Please refer to the package insert for complete warnings and contraindications, as those data are currently unavailable in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.96%), this score reflects model generalisation across keratinocyte-related skin disorders rather than a disease-specific mechanistic connection. Seborrheic keratosis is driven by FGFR3/PIK3CA mutation, not by the VDR-regulated inflammatory pathways Calcipotriol modulates; the unmet clinical need is also minimal given SK's benign and non-malignant nature. With zero supporting clinical trials and zero relevant publications, there is no evidence base to justify further investment.

**To proceed, the following is needed:**

- **Mechanistic validation**: In vitro studies using SK-derived keratinocyte models (FGFR3/PIK3CA-mutant cell lines) to determine whether VDR activation has any measurable impact on SK-type proliferative signalling
- **Epidemiological signal**: Any observational evidence that long-term Calcipotriol users show altered SK incidence or lesion regression
- **Clinical need assessment**: A formal determination of whether a therapeutic gap exists for SK, given its benign course and low treatment priority
- **MOA data retrieval**: Query DrugBank API to obtain the complete pharmacological profile of Calcipotriol (Data Gap DG002)
- **Safety profile completion**: Retrieve CDSCO prescribing information to assess warnings and contraindications (Data Gap DG001)
- **Consider reprioritising**: Among the top 10 predicted indications, **Vulvitis (rank 4)** and **Vulvar Neoplasm (rank 5)** have published literature support (PMID [22968059](https://pubmed.ncbi.nlm.nih.gov/22968059/) and [30785593](https://pubmed.ncbi.nlm.nih.gov/30785593/) respectively) and stronger mechanistic rationale as psoriasis-extension and EMPD chemosensitisation targets — these may be higher-yield candidates for a full evidence deep-dive

---

> ⚠️ **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

