---
layout: default
title: Oxiconazole
parent: 僅模型預測 (L5)
nav_order: 623
evidence_level: L5
indication_count: 1
---

# Oxiconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Oxiconazole: From Topical Antifungal (Dermatophytosis) to Cutaneous Candidiasis

## One-Sentence Summary

Oxiconazole is a topical imidazole antifungal traditionally used against dermatophyte skin infections (tinea/dermatomycosis). The TxGNN model predicts it may also be effective for **Cutaneous Candidiasis**, a prediction consistent with the well-established class-level mechanism of azole antifungals, though it is currently supported only by **5 publications** and **no registered clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Topical antifungal for dermatophyte/tinea skin infections (no Taiwan license data available — drug not marketed) |
| Predicted New Indication | Cutaneous Candidiasis |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed drug-specific mechanism of action data for oxiconazole is not available in the record. Based on known pharmacology, oxiconazole belongs to the imidazole class of topical antifungals, which inhibit fungal CYP51 (14α-demethylase), blocking ergosterol biosynthesis and disrupting fungal cell membrane integrity. This is a well-established, class-level mechanism shared across imidazole antifungals (e.g., econazole, bifonazole).

Dermatophyte infections (the drug's traditional use area) and cutaneous candidiasis are both superficial fungal skin infections, and imidazole antifungals as a class are already known to have activity against both dermatophytes and *Candida albicans*. This makes the TxGNN prediction a mechanistically well-founded extension rather than a novel hypothesis — it aligns with existing pharmacological knowledge of the azole class rather than proposing an unprecedented mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6382000](https://pubmed.ncbi.nlm.nih.gov/6382000/) | 1984 | Cohort | Mykosen | Direct comparison of oxiconazole and econazole in dermatomycoses |
| [24196340](https://pubmed.ncbi.nlm.nih.gov/24196340/) | 2013 | Review | J Drugs Dermatol | Overview of topical antifungal therapy for superficial cutaneous fungal infections, including dermatophyte and yeast pathogens |
| [10439936](https://pubmed.ncbi.nlm.nih.gov/10439936/) | 1999 | Review | Drugs | Review of allylamine/azole-class antifungal efficacy against dermatophytes and *Candida albicans* |
| [2670516](https://pubmed.ncbi.nlm.nih.gov/2670516/) | 1989 | Review | Drugs | Review of bifonazole (imidazole class) activity against dermatophytes, yeasts, and dimorphic fungi |
| [7501581](https://pubmed.ncbi.nlm.nih.gov/7501581/) | 1995 | Review | Postgraduate Medicine | Clinical approach to superficial fungal and candidal skin infections, including topical antifungal treatment options |

---

## Taiwan Market Information

Oxiconazole is currently not marketed in Taiwan — no license registrations are on record (total_licenses = 0).

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA label warnings, contraindications, and drug interaction data are currently unavailable and marked as a **Blocking** data gap — see Conclusion.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between oxiconazole's established antifungal activity and cutaneous candidiasis is pharmacologically sound and supported by class-level literature (L3, observational/review evidence), but there are no clinical trials specifically testing this indication and the drug is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (Blocking gap — required before any S1 safety pre-assessment can proceed; obtain via TFDA label PDF)
- Detailed drug-specific mechanism of action data (High priority gap — query DrugBank API)
- Drug-drug interaction (DDI) data (currently not found)
- Evaluation of feasibility for Taiwan market entry, given the drug has no existing local license
- Dedicated clinical trials or case series evaluating oxiconazole specifically for cutaneous candidiasis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

