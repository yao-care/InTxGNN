---
layout: default
title: Anidulafungin
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 10
---

# Anidulafungin
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

# Anidulafungin: From Fungal Infections to Impetigo

## One-Sentence Summary

Anidulafungin is an echinocandin-class antifungal agent approved internationally for the treatment of candidemia and invasive *Candida* infections (no India registration on record).
The TxGNN model predicts it may be effective for **Impetigo**, yet **no supporting clinical trials or literature** currently exist for this indication.
The mechanistic basis for this prediction is absent — impetigo is a bacterial skin infection, and anidulafungin's target (β-1,3-glucan synthase) is entirely fungus-specific.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Invasive candidiasis / candidemia (India regulatory data unavailable; based on international approvals) |
| Predicted New Indication | Impetigo |
| TxGNN Prediction Score | 98.85% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Anidulafungin belongs to the echinocandin class of antifungals. It works by non-competitively inhibiting **β-1,3-glucan synthase**, the enzyme responsible for assembling the β-glucan polymer layer in fungal cell walls. This target is entirely absent in bacteria and human cells, making it one of the more selective antifungal mechanisms known.

Impetigo is a superficial bacterial skin infection caused primarily by *Staphylococcus aureus* and *Streptococcus pyogenes* — both Gram-positive bacteria that do not possess β-1,3-glucan synthase. There is no established biochemical pathway through which anidulafungin could inhibit, neutralise, or modulate the virulence of these pathogens.

The high TxGNN score (98.85%) is likely a **knowledge graph topology artefact** rather than a true pharmacological signal. Notably, 9 out of 10 top-ranked predictions in this analysis share the same pattern — high scores assigned to bacterial infections and pleural malignancies — all without mechanistic support. This cluster pattern strongly suggests the model is capturing the anatomical proximity of skin and pleural disease nodes in the knowledge graph, not genuine drug efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Anidulafungin currently has **no approved registrations in India** (0 licenses on record). The drug is marketed in other jurisdictions (e.g., under the brand name **Eraxis** in the US and EU) for invasive candidiasis and candidemia, but has not entered the Indian market as of the data cut-off date (2026-04-05).

---

## Safety Considerations

**Drug Interactions:**

| Interacting Drug | Severity | Details |
|-----------------|----------|---------|
| Cyclosporine | Minor | Minor pharmacokinetic interaction reported. Clinical significance is limited; routine monitoring is recommended when used together. |

Please refer to the full package insert for complete warnings and contraindications (these data were not available in this evidence pack and are classified as a blocking data gap).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, there is no mechanistic basis, clinical trial, or published literature supporting anidulafungin for impetigo. The antifungal mechanism (β-1,3-glucan synthase inhibition) is entirely irrelevant to the Gram-positive bacteria that cause this condition, and the high score is most plausibly explained by knowledge graph topology rather than drug activity.

**Broader pattern note:** All 10 top-ranked predictions in this report are "Hold" (9 at L5; 1 at L4 with a single pharmacokinetic study for pleural empyema in immunocompromised patients). This systematic pattern suggests a potential graph topology bias for Anidulafungin in the current TxGNN model, warranting further investigation before any indication is advanced.

**To proceed, the following is needed:**

- Retrieval of India CDSCO / full package insert to resolve the blocking safety data gap (warnings, contraindications)
- Formal mechanistic review: does any published in vitro or in vivo evidence suggest antibacterial or immunomodulatory activity for echinocandins?
- Knowledge graph bias audit: assess whether the pleural/skin disease node cluster artificially inflates scores for this drug
- If the pleural empyema signal (Rank 4, L4) is of interest, a targeted PK/PD analysis for fungal empyema in immunosuppressed populations would be the most scientifically defensible next step

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

