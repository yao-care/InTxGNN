---
layout: default
title: Progesterone
parent: 僅模型預測 (L5)
nav_order: 504
evidence_level: L5
indication_count: 10
---

# Progesterone
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

# Progesterone: From an Undocumented Original Indication to Amenorrhea

## One-Sentence Summary

Progesterone (DrugBank ID: DB00396) is an endogenous steroid hormone; however, this evidence pack contains no record of an original approved indication or India market registration for it. The TxGNN model predicts it may be effective for **Amenorrhea**, with an extremely high confidence score (**99.9996%**), but currently **0 clinical trials** and **0 publications** in this dataset directly support this specific prediction — meaning the prediction is mechanistically compelling but evidentially untested.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented — Progesterone has no registered license or approved indication text in this evidence pack |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.9996% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Progesterone is not available from DrugBank in this evidence pack (data gap, High severity — DG002). Based on established pharmacology, Progesterone is the key hormone of the luteal phase of the menstrual cycle: its physiological decline ("withdrawal") triggers endometrial shedding and menstrual bleeding.

This is directly relevant to the predicted indication. Clinically, the **"progesterone withdrawal test"** is a standard diagnostic and therapeutic maneuver for secondary amenorrhea — administering progesterone and then stopping it is used both to confirm adequate estrogen priming of the endometrium and to induce a withdrawal bleed. This gives the TxGNN prediction (score 0.99999, the highest-ranked candidate in this dataset) a strong mechanistic rationale.

That said, the mechanistic strength is not matched by empirical evidence: the query log shows the ClinicalTrials.gov, ICTRP, and PubMed searches for "Progesterone" + "amenorrhea (disease)" all returned **zero results**. Given how well-established progesterone use is for amenorrhea in real-world practice, this is most plausibly a **search/indexing gap** in the data collection pipeline (e.g., query terms not matching how this indication is coded in trial registries or literature databases) rather than a true absence of evidence. This should be verified before the evidence level is treated as final.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

**Drug Interactions**: A completed DDI query identified **163 total interactions** for Progesterone. The interactions sampled in this evidence pack are predominantly rated **Moderate** severity and are concentrated among antidiabetic agents, including:
- Metformin, Acarbose, Chlorpropamide, Glimepiride, Repaglinide, Pioglitazone
- DPP-4 inhibitors: Alogliptin, Saxagliptin
- SGLT2 inhibitors: Canagliflozin, Dapagliflozin, Empagliflozin
- GLP-1 agonists: Albiglutide, Dulaglutide, Liraglutide, Semaglutide
- Insulins: Insulin aspart, Insulin degludec, Insulin detemir
- Also: Aprepitant, Clarithromycin

This pattern is consistent with progesterone's known tendency to reduce insulin sensitivity and antagonize glycemic control — patients on antidiabetic therapy would need blood glucose monitoring if progesterone is co-administered. With 163 total interactions on file and only a subset reviewed here, a full interaction screen against the patient's medication list is recommended before use.

No key warnings or contraindications data are currently available for Progesterone in this evidence pack (Blocking data gap — DG001: TFDA/local label warnings and contraindications have not yet been retrieved).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for amenorrhea carries the highest TxGNN confidence score in the entire candidate set and a credible mechanistic basis, but it is currently backed by zero clinical trials and zero publications (Evidence Level L5), and a **Blocking**-severity data gap (missing local label warnings/contraindications) prevents this candidate from entering safety pre-screening (S1). Under the current evidence base, this does not meet the bar to proceed.

**To proceed, the following is needed:**
- Retrieve TFDA/India label warnings and contraindications (resolves Blocking gap DG001) to enable S1 safety screening
- Confirm mechanism of action via DrugBank API (resolves High-severity gap DG002)
- Re-run the ClinicalTrials.gov/ICTRP/PubMed searches for "amenorrhea" with expanded synonyms (e.g., "secondary amenorrhea," "progesterone withdrawal test," "oligomenorrhea") to rule out a false-negative search result before finalizing the L5 rating
- Confirm original indication and regulatory status, since no license or approved indication text exists for this drug in the current dataset
- As a lower-risk alternative, consider prioritizing **benign mammary dysplasia** (rank 3, Evidence Level L3, S2) or **cervix endometriosis** (rank 5, Evidence Level L3, S2) from this same evidence pack — both have at least one completed clinical trial and multiple literature sources, offering a stronger near-term evidentiary base than amenorrhea while the above gaps are resolved
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

