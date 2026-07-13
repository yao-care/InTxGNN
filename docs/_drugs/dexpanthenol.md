---
layout: default
title: Dexpanthenol
parent: 僅模型預測 (L5)
nav_order: 218
evidence_level: L5
indication_count: 7
---

# Dexpanthenol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Dexpanthenol: From Wound Healing & Skin Protection to Anorectal Stricture

## One-Sentence Summary

Dexpanthenol (provitamin B5) is a widely used topical wound-healing and skin-protective agent — marketed globally as Bepanthen® and Bepantol® — with no registered product currently in India.
The TxGNN model predicts potential therapeutic value across 7 indications, with **Anorectal Stricture** ranked highest by prediction score (99.72%); however, this and most other top-ranked predictions carry **no clinical trial or literature support (L5)**.
The most evidence-backed finding in this pack is the skin eruption (exanthem) indication at rank 6, supported by **1 completed Phase III RCT** of Bepanthen® cream — though this largely reflects an extension of Dexpanthenol's established topical use rather than a novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record in India (globally recognised use: topical wound healing, skin barrier protection, dry eye) |
| Predicted New Indication (Rank 1) | Anorectal Stricture |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 (Rank 1 – Anorectal Stricture); L2 available for Rank 6 (Exanthem) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed MOA data is not currently available in this Evidence Pack. Based on established pharmacology, Dexpanthenol is a prodrug that is converted in vivo to pantothenic acid (vitamin B5), which then serves as the biosynthetic precursor to Coenzyme A (CoA). Through CoA, Dexpanthenol participates in fatty acid synthesis, lipid metabolism, and energy production — processes that are fundamental to cell proliferation, epithelial repair, and maintenance of barrier integrity. Topically applied, it also directly stimulates keratinocyte proliferation and upregulates ceramide synthesis to restore the lipid barrier.

For Anorectal Stricture specifically, the theoretical link rests on these tissue-repair properties: promoting mucosal epithelial healing along the anorectal wall. However, anorectal stricture is a primarily structural/mechanical condition whose standard of care is endoscopic or surgical dilation. Pharmacological adjuncts serve a very limited role. The high TxGNN score (0.9972) is most likely attributable to **graph neighbourhood clustering bias** — the anorectal disease node cluster in the knowledge graph — rather than a genuine pharmacological connection. No clinical trials or literature support this link.

Of all seven predictions in this pack, **Proctitis (rank 5)** and **Exanthem (rank 6)** carry the most mechanistically coherent rationale. Dexpanthenol's documented anti-inflammatory effects (downregulation of IL-1β and TNF-α via NF-κB modulation) and mucosal-repair capacity are directly relevant to proctitis pathophysiology; its well-established role in skin barrier restoration underpins the exanthem prediction, confirmed by an existing Phase III RCT.

---

## Clinical Trial Evidence

> **Note:** The top-ranked predicted indication (Anorectal Stricture) has no registered clinical trials. The five trials below were retrieved for **Exanthem (Rank 6)** and represent the only clinical evidence in this Evidence Pack. Grade A/B trials are highlighted.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01136005](https://clinicaltrials.gov/study/NCT01136005) | Phase 3 | Completed | 160 | **[Grade A — Direct Evidence]** Phase III randomised double-blind RCT of **Bepanthen® cream (dexpanthenol)** vs. Cetomacrogol cream for prevention of papulopustular skin eruption in patients receiving EGFR inhibitors (EGFRI). Represents the highest-grade direct clinical evidence for Dexpanthenol's topical efficacy in inflammatory skin reactions. Outcome data should be confirmed via the full ClinicalTrials.gov record. |
| [NCT03852563](https://clinicaltrials.gov/study/NCT03852563) | N/A | Completed | 33 | **[Grade B — Direct Evidence]** Evaluated **Bepantol® cream (dexpanthenol)** for safety and efficacy in skin recovery following ablative laser dermatological procedures; assessed redness, irritation, and softness. Small sample, non-randomised design; provides supportive evidence for post-procedural skin repair. |
| [NCT05699122](https://clinicaltrials.gov/study/NCT05699122) | N/A | Completed | 16 | **[Grade C]** Evaluated low-level laser therapy for incontinence-associated dermatitis in elderly patients. Dexpanthenol, if present, likely served as a control or adjunct barrier product rather than the primary intervention. Very small sample; limited relevance to exanthem. |
| [NCT03866447](https://clinicaltrials.gov/study/NCT03866447) | Phase 4 | Unknown | 80 | **[Grade C]** Investigated vitamin D and topical analogues in acne vulgaris. Dexpanthenol's role (possibly as vehicle base) is unclear; trial status is unknown (may have been lost to follow-up). Research question does not align with exanthem. |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | Terminated | 49 | **[Grade C]** Evaluated imiquimod gel formulations for actinic cheilitis. Dexpanthenol was not a primary study drug; trial was terminated early. Minimal relevance to this drug or indication. |

---

## Literature Evidence

Currently no related literature is available for any of the 7 predicted indications based on the PubMed queries performed in this Evidence Pack.

---

## India Market Information

Dexpanthenol is currently **not registered in India**. No marketing authorisation records are available.

*For reference: Dexpanthenol is marketed internationally under brands including Bepanthen® and Bepantol® (Bayer) in topical cream, ophthalmic solution, and injectable forms. Any India market entry would require a complete CDSCO new drug application.*

---

## Safety Considerations

Safety data for Dexpanthenol was not retrievable through the sources queried in this Evidence Pack (TFDA/CDSCO package insert not available; no DDI interactions found).

Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-ranked TxGNN prediction (Anorectal Stricture) carries L5 evidence and is mechanistically implausible as a standalone drug indication — the high model score most likely reflects graph topology artefact rather than pharmacological signal. While a completed Phase III RCT (NCT01136005) supports Dexpanthenol's topical use for EGFRI-related skin eruption (exanthem, rank 6), this largely extends an already-established clinical role rather than demonstrating a genuinely novel repurposing opportunity. No India regulatory registration exists, and critical safety documentation (CDSCO/TFDA package insert) is missing, blocking formal safety assessment.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Obtain and parse the TFDA/CDSCO package insert PDF to complete safety screening before any S1 assessment can proceed
- **Resolve DG002 (High):** Query the DrugBank API for complete MOA, pharmacokinetics, and toxicity data to support mechanistic rationale analysis
- **Clarify exanthem disease definition:** Confirm whether NCT01136005's endpoint (EGFRI-associated papulopustular eruption) falls within TxGNN's "exanthem" node definition; if confirmed, the evidence level upgrades to L2 for that specific indication
- **Targeted literature search for ophthalmic use:** Conduct a focused PubMed search for dexpanthenol eye drops and punctate epithelial keratoconjunctivitis (rank 7, currently L4) — external evidence likely exists and may upgrade its evidence level
- **Commission proctitis feasibility review:** Rank 5 (Proctitis) represents the most mechanistically coherent novel indication; initiate a systematic literature review and assess feasibility for a Phase I/II pilot study as a topical rectal preparation
- **India regulatory gap analysis:** Conduct a CDSCO new drug application feasibility assessment if market entry is under consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

