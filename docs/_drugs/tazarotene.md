---
layout: default
title: Tazarotene
parent: Model Prediction Only (L5)
nav_order: 808
evidence_level: L5
indication_count: 3
---

# Tazarotene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Tazarotene: From Psoriasis to Seborrheic Dermatitis

## One-Sentence Summary

Tazarotene is a topical retinoid originally used to treat psoriasis, parapsoriasis and acne.
The TxGNN model predicts it may be effective for **Seborrheic Dermatitis**,
but **no clinical trials or publications** currently support this specific prediction, so it rests on computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriasis, parapsoriasis, acne (from the knowledge graph; no approved indication text is available in the India registrations) |
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 12 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tazarotene is a topical retinoid (a RAR-beta/gamma agonist), its use in psoriasis and acne is established, and mechanistically it may be applicable to seborrheic dermatitis. This link is inferred from general knowledge of the drug class and is not confirmed by the data compiled for this report.

Retinoids normalise keratinocyte differentiation and reduce hyperproliferation. These processes overlap with the skin pathology of psoriasis and acne, and could plausibly extend to seborrheic dermatitis, which is also an inflammatory, scaling skin condition.

One caution is tolerability. Retinoid-related skin irritation could be a problem on already inflamed seborrheic skin.

Two other predictions were also generated, and both are weaker than the lead one:
- **Seborrheic keratosis** (score 99.51%, evidence level L4): two publications exist, a 2023 systematic review of topical treatments and a 2004 comparative study of cryosurgery against topical calcipotriene, tazarotene and imiquimod. Only titles and brief abstracts were available, so whether tazarotene showed efficacy is unclear. It is best treated as a research question.
- **Vulvar inverted follicular keratosis** (score 99.38%, evidence level L5): no evidence. It is a rare benign lesion usually treated by excision, and the vulvar site raises mucosal irritation concerns.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for seborrheic dermatitis.

For reference, the literature found for the second-ranked prediction (seborrheic keratosis) is listed below:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36215682](https://pubmed.ncbi.nlm.nih.gov/36215682/) | 2023 | Systematic review | J Dermatol Treat | Reviewed 26 reports on the efficacy and safety of topical treatments for seborrheic keratoses; the available summary does not state tazarotene-specific results |
| [15090020](https://pubmed.ncbi.nlm.nih.gov/15090020/) | 2004 | Cohort | Int J Dermatol | Compared standard cryosurgery with topical calcipotriene, tazarotene and imiquimod for seborrheic keratoses; outcome not stated in the available summary |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 217875 | Texara Forte Cream | Tube of 15 gm cream | Not stated |
| 222490 | Tazotop Cream | Tube of 15 gm cream | Not stated |
| 123853 | La Tez 0.1% Cream | Tube of 15 gm cream | Not stated |
| 217368 | Texara Gel | Tube of 15 gm gel | Not stated |
| 220266 | Tazotop Forte Cream | Tube of 15 gm cream | Not stated |

There are 12 valid single-ingredient registrations in total, all topical creams or gels.

## Safety Considerations

- **Knowledge-graph contraindications** (not taken from label text): photoparoxysmal response, photosensitivity disease, sunburn.
- **Drug Interactions**: 25 interactions were recorded, all with an unknown severity level. Examples include doxycycline, minocycline, tretinoin, adapalene, clobetasol, tacrolimus, diclofenac, citalopram and duloxetine. The combination with other retinoids (tretinoin, adapalene) and with tetracyclines deserves particular attention.

Please also refer to the package insert for full safety information, as warnings and contraindications from the label were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for seborrheic dermatitis is very high, but there are no clinical trials or publications behind it (L5, model prediction only). Mechanistic plausibility is inferred from the drug class, and irritation on inflamed skin is a real tolerability concern.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank to support the mechanistic link
- Package insert warnings and contraindications from the India registrations
- A targeted literature search for tazarotene in seborrheic dermatitis, and a review of the full text of the 2023 and 2004 seborrheic keratosis papers to check whether tazarotene was effective
- Confirmation of the approved indications on the India registrations
- Early-phase tolerability and dose-finding data on seborrheic skin, given the irritation risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

