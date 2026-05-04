---
layout: default
title: Butenafine
parent: 僅模型預測 (L5)
nav_order: 126
evidence_level: L5
indication_count: 5
---

# Butenafine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Butenafine: From Superficial Dermatophytosis to Cutaneous Candidiasis

## One-Sentence Summary

Butenafine is a benzylamine antifungal agent with established efficacy against superficial dermatophyte infections (tinea pedis, tinea corporis, tinea cruris), used clinically in Japan and other markets.
The TxGNN model predicts it may be effective for **Cutaneous Candidiasis**,
with **0 registered clinical trials** and **3 publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Superficial dermatophytosis (tinea pedis, tinea corporis, tinea cruris) |
| Predicted New Indication | Cutaneous Candidiasis |
| TxGNN Prediction Score | 99.33% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the evidence pack. Based on published literature, Butenafine hydrochloride is a **synthetic benzylamine antifungal derivative** — a class known to inhibit squalene epoxidase, an enzyme essential for ergosterol biosynthesis in fungal cell membranes. Ergosterol depletion disrupts membrane integrity and leads to fungicidal activity, particularly against dermatophytes, aspergilli, dimorphic fungi, and dematiaceous fungi (PMID 18624686). This mechanism is chemically analogous to allylamines such as terbinafine, but the benzylamine scaffold confers a distinct pharmacokinetic profile and prolonged post-treatment activity.

The prediction from TxGNN is biologically plausible: both dermatophytoses and cutaneous candidiasis are **superficial fungal infections affecting the skin**, sharing overlapping tissue tropism and pathophysiological features. An antifungal agent effective against dermatophytes (which cause tinea species) could reasonably demonstrate activity against Candida species in the cutaneous compartment, since both depend on ergosterol-rich membranes. Indeed, butenafine has been reviewed among "novel antimycotics" with potential application for cutaneous and mucosal diseases beyond pure dermatophyte infections (PMID 11893219).

One animal study specifically tested efficacy against **cutaneous candidiasis in guinea pigs** (PMID 11302816), providing preclinical biological plausibility. However, direct clinical trial evidence in humans with cutaneous candidiasis remains absent, which limits the current evidence classification to L4.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Butenafine in cutaneous candidiasis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11302816](https://pubmed.ncbi.nlm.nih.gov/11302816/) | 2001 | Preclinical (Animal) | Antimicrobial Agents and Chemotherapy | In vitro and in vivo (guinea pig) evaluation of KP-103 vs. comparators including butenafine; therapeutic efficacy tested against both plantar tinea pedis and **cutaneous candidiasis** models |
| [11893219](https://pubmed.ncbi.nlm.nih.gov/11893219/) | 2002 | Review | American Journal of Clinical Dermatology | Review of six novel antimycotics including butenafine; discusses potential applications for **human cutaneous and mucosal fungal diseases**, including candidiasis context |
| [24196340](https://pubmed.ncbi.nlm.nih.gov/24196340/) | 2013 | Review | Journal of Drugs in Dermatology | Optimization of topical antifungal therapy for superficial cutaneous fungal infections caused by dermatophytes and **yeasts**; positions butenafine among available agents |

---

## India Market Information

Butenafine (DB01091) currently has **no registered licenses** in the Indian market. No authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction data, key warnings, or contraindication records were retrievable during the evidence collection period (query date: 2026-03-27). Formal CDSCO prescribing information review is required before any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Butenafine is pharmacologically well-characterized as a benzylamine antifungal with squalene epoxidase inhibition as its core mechanism, and the TxGNN prediction score of 99.33% for cutaneous candidiasis is mechanistically coherent. However, the drug is **not currently marketed in India**, and direct human clinical evidence for cutaneous candidiasis is absent — only one animal preclinical study and two narrative reviews were identified. Without any clinical trial data and with all safety records flagged as data gaps, regulatory and clinical development risk cannot be adequately assessed.

**To proceed, the following is needed:**

- **Safety package**: Obtain full prescribing information (package insert / SmPC) from markets where butenafine is approved (e.g., Japan, USA — Mentax®) to assess contraindications, warnings, and drug interactions
- **MOA confirmation**: Query DrugBank API to formally document the mechanism of action (squalene epoxidase inhibition) for the evidence dossier
- **Human clinical evidence**: Conduct a systematic literature search to identify any human studies on butenafine specifically for Candida skin infections (not just dermatophytes)
- **Regulatory feasibility**: Assess CDSCO pathway for introducing a non-marketed antifungal topical agent; evaluate whether existing global approvals (US FDA approval for tinea pedis) could support an accelerated bridging strategy
- **In vitro MIC data**: Verify butenafine's minimum inhibitory concentration (MIC) against common cutaneous Candida species (C. albicans, C. tropicalis) to confirm antifungal spectrum
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

