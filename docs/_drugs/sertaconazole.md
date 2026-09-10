---
layout: default
title: Sertaconazole
parent: 僅模型預測 (L5)
nav_order: 762
evidence_level: L5
indication_count: 10
---

# Sertaconazole
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

# Sertaconazole: From Superficial Fungal Infections to Dermatophytosis of Groin and Perianal Area

## One-Sentence Summary

> Sertaconazole is a topical imidazole antifungal already established internationally for superficial fungal skin infections (dermatophytosis, cutaneous candidiasis, pityriasis versicolor), though it is **not currently marketed in India** and no formal original-indication record exists in this evidence pack.
> The TxGNN model's top-ranked prediction is **Dermatophytosis of Groin and Perianal Area (tinea cruris)**, but **no clinical trials or literature were retrieved under this specific disease term** — evidence for closely related indications (tinea corporis, cutaneous candidiasis, superficial mycosis) is substantial and should be considered alongside this top prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (India: not marketed; no formal dossier indication text on file). Independent literature in this pack identifies sertaconazole as an established topical antifungal for dermatophytosis, cutaneous candidiasis, and pityriasis versicolor. |
| Predicted New Indication | Dermatophytosis of Groin and Perianal Area (tinea cruris) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature retrieved for this specific term) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the structured drug record for this evidence pack (flagged as a High-severity data gap requiring DrugBank API lookup). However, the literature collected under related predicted indications in this same pack (e.g., PMID 19275277, PMID 23566144, PMID 21746955) consistently describes sertaconazole as a third-generation imidazole antifungal with a **dual mechanism**: at standard concentrations it inhibits 14-α-lanosterol demethylase, blocking ergosterol synthesis (fungistatic effect); at higher concentrations, its distinctive benzothiophene ring allows direct binding to non-sterol lipids in the fungal cell membrane, increasing permeability and producing a fungicidal effect. This dual action, plus reported anti-inflammatory and antipruritic properties, distinguishes it from older azoles.

Dermatophytosis of the groin and perianal area (tinea cruris) is caused by the same dermatophyte genera (*Trichophyton*, *Epidermophyton*) responsible for tinea corporis and tinea pedis — indications for which this evidence pack already contains strong RCT-level support (see Rank 2 below). Notably, the review by Croxtall & Plosker (PMID 19275277, included under the Rank 2/Rank 7/Rank 9 evidence pools of this same pack) explicitly lists **tinea cruris** among sertaconazole's EU-approved indications for dermatophytosis. This suggests the top-ranked prediction may reflect an indication that is **already clinically supported for this drug class**, rather than a genuinely novel repurposing signal — the absence of literature under this exact disease term likely reflects a search-term/taxonomy gap rather than a true absence of supporting evidence.

Given the shared pathogen spectrum, shared topical route, and shared drug class rationale, the mechanistic plausibility for this prediction is high — but this report can only formally credit evidence that was actually retrieved and linked to this specific disease term.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available under this specific disease term.

*Note: Substantial literature exists for the closely related indication "tinea corporis" (Rank 2) and "superficial mycosis" (Rank 7) elsewhere in this evidence pack — see below for reference, as these may inform the clinical plausibility of this prediction.*

### Closely Related Indication: Tinea Corporis (Rank 2, Score 99.94%, Evidence Level L2)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24249898](https://pubmed.ncbi.nlm.nih.gov/24249898/) | 2013 | RCT | Indian J Dermatol | Comparative trial: terbinafine 1% cream vs sertaconazole 2% cream in tinea corporis/cruris |
| [34760651](https://pubmed.ncbi.nlm.nih.gov/34760651/) | 2021 | RCT | Perspect Clin Res | Sertaconazole 2% vs luliconazole 1% cream in dermatophytoses — efficacy, safety, cost-effectiveness |
| [24249897](https://pubmed.ncbi.nlm.nih.gov/24249897/) | 2013 | RCT | Indian J Dermatol | Sertaconazole 2% vs butenafine 1% in tinea infections |
| [25386455](https://pubmed.ncbi.nlm.nih.gov/25386455/) | 2014 | Observational | J Clin Diagn Res | Sertaconazole vs clotrimazole in tinea corporis |
| [28066103](https://pubmed.ncbi.nlm.nih.gov/28066103/) | 2016 | RCT | Indian J Pharmacol | Once-daily sertaconazole vs terbinafine in localized dermatophytosis |
| [30409926](https://pubmed.ncbi.nlm.nih.gov/30409926/) | 2019 | RCT | Indian J Dermatol Venereol Leprol | Amorolfine 0.25% vs sertaconazole 2% cream in limited dermatophytosis |
| [19275277](https://pubmed.ncbi.nlm.nih.gov/19275277/) | 2009 | Review | Drugs | Confirms EU approval for dermatophytosis including tinea cruris |

---

## India Market Information

Sertaconazole is **not currently marketed in India** (`market_status: 未上市`, `total_licenses: 0`). No product registrations, brand names, or approved indication texts are on file in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack — TFDA-equivalent label data (warnings/contraindications) is flagged as a **Blocking** data gap that must be resolved before any S1 safety pre-assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (dermatophytosis of groin and perianal area) has no directly linked clinical trial or literature evidence in this pack, meeting only the L5 (model-prediction-only) threshold. While mechanistic plausibility is high — and closely related indications (tinea corporis, cutaneous candidiasis, superficial mycosis, pityriasis versicolor) carry L2-level RCT support — a Hold is warranted for this specific term pending confirmation that the search-term gap, not a true absence of evidence, explains the empty evidence set.

**To proceed, the following is needed:**
- Resolve **DG001** (Blocking): obtain TFDA/regulatory label warnings and contraindications before any safety pre-assessment (S1) can begin.
- Resolve **DG002** (High): obtain formal MOA data via DrugBank API to support mechanistic-relevance scoring.
- Re-run literature/trial search using synonym terms ("tinea cruris", "jock itch", "groin dermatophytosis") to confirm whether the apparent evidence gap for the top prediction is a taxonomy artifact.
- If confirmed as equivalent to tinea cruris, re-evaluate this indication using the L2-level evidence already available for tinea corporis and superficial mycosis in this same pack.
- Confirm India market-entry regulatory pathway, since the drug currently holds zero registrations.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

