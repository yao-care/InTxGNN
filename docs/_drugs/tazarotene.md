---
layout: default
title: Tazarotene
parent: 僅模型預測 (L5)
nav_order: 801
evidence_level: L5
indication_count: 3
---

# Tazarotene
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Tazarotene: From Unclear Original Indication (Data Gap) to Seborrheic Dermatitis

## One-Sentence Summary

> Tazarotene (DrugBank DB00799) does not currently have a marketed product or license record in India, and its original approved indication and mechanism of action are not available in this Evidence Pack.
> The TxGNN model predicts it may be effective for **Seborrheic Dermatitis**,
> but this direction is currently supported by only **1 loosely related clinical trial** and **no direct literature**, so the evidence base is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No data available (original_indications and India license records are both empty) |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 (model prediction only; the one associated trial studies acne vulgaris, not seborrheic dermatitis, and has Unknown status) |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Tazarotene in this Evidence Pack (`original_moa: [Data Gap]`), and no original indication is recorded either. Based on general pharmacological knowledge, Tazarotene is a third-generation topical retinoid (retinoic acid receptor agonist) commonly used for dermatological conditions such as acne vulgaris and plaque psoriasis — this is background context, not something confirmed by the Evidence Pack itself.

Mechanistically, a retinoid's normalization of keratinocyte differentiation and anti-inflammatory activity could plausibly extend to other keratinization/inflammatory skin disorders, which offers a biological rationale for the seborrheic dermatitis prediction. However, the single clinical trial captured under this indication (NCT06281782) actually studies **acne vulgaris** with platelet-rich plasma plus topical retinoids — it does not directly investigate seborrheic dermatitis. This is a meaningful gap between the predicted indication and the supporting evidence, and should be treated as indirect, class-level evidence at best.

It is worth noting that the second-ranked prediction, **seborrheic keratosis** (score 99.51%), is supported by two directly relevant publications, including a comparative study of topical tazarotene vs. cryosurgery/calcipotriene/imiquimod for seborrheic keratosis (PMID 15090020) and a 2023 systematic review of topical treatments for seborrheic keratosis (PMID 36215682). This may represent a mechanistically closer and better-evidenced alternative candidate worth parallel evaluation.

---

## Clinical Trial Evidence

*(For predicted indication: Seborrheic Dermatitis)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06281782](https://clinicaltrials.gov/study/NCT06281782) | NA | Unknown | 40 | Randomized trial of platelet-rich plasma + topical retinoids vs. topical retinoids alone **in acne vulgaris** — not a direct study of seborrheic dermatitis; relevance to the predicted indication is indirect (shared drug class only) |

---

## Literature Evidence

*(For predicted indication: Seborrheic Dermatitis)*

Currently no related literature available.

---

## Safety Considerations

- **Drug Interactions**: 25 potential interactions identified via DDInter (severity level not classified in source data). Interacting drugs include: Doxycycline, Omeprazole, Minocycline, Cetirizine, Montelukast, Fluticasone, Salbutamol, Citalopram, Levothyroxine, Rofecoxib, Hydroxyzine, Diclofenac, Etodolac, Adapalene, Duloxetine, Tretinoin, Clobetasol, Tacrolimus, Cyclobenzaprine, Doxepin, and others. Since interaction levels are marked "Unknown," clinical significance cannot be assessed from this data alone.

Detailed warnings and contraindications are not currently available (data gap DG001, flagged as Blocking) — please refer to an official product label once one becomes available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The drug has a Blocking data gap on label warnings/contraindications (DG001), preventing any S1 safety pre-assessment, and the evidence for the top-ranked predicted indication (seborrheic dermatitis) is weak — the only associated trial is unrelated in disease scope and has unknown status. Combined with zero market presence in India, there is currently insufficient basis to proceed.

**To proceed, the following is needed:**
- Resolve DG001: obtain official label warnings/contraindications (source: national regulatory agency label PDF)
- Resolve DG002: obtain confirmed mechanism of action from DrugBank
- Re-run evidence search specifically targeting "tazarotene AND seborrheic dermatitis" to confirm whether direct clinical/literature support exists
- Evaluate the seborrheic keratosis candidate (rank 2) in parallel, as it currently has stronger directly-relevant literature evidence
- Classify DDI severity levels (currently all "Unknown") before any interaction-based risk assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

