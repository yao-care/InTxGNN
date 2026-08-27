---
layout: default
title: Triptorelin
parent: 僅模型預測 (L5)
nav_order: 508
evidence_level: L5
indication_count: 10
---

# Triptorelin
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

# Triptorelin: From Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Triptorelin is a synthetic GnRH (gonadotropin-releasing hormone) agonist, used internationally as a first-line treatment for hormone-sensitive conditions including prostate cancer, endometriosis, and central precocious puberty (CPP), acting by suppressing pituitary gonadotropin secretion and downstream sex hormone production.
The TxGNN model's highest-ranked prediction suggests potential utility in **Hypertrichosis (generalised excessive hair growth)**,
with only **1 publication** currently available — a 2026 case report in which triptorelin was co-administered for gender-affirming therapy, not as a treatment for hypertrichosis itself.
Given the L5 evidence level, absent mechanistic rationale, and the adverse-event nature of the sole literature, the recommended decision is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer / Endometriosis / Central precocious puberty (hormone-sensitive conditions; no India registrations on record) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Triptorelin is a synthetic decapeptide analogue of GnRH. When administered continuously rather than in pulsatile fashion, it causes sustained pituitary GnRH receptor stimulation followed by receptor downregulation. This leads to suppressed LH and FSH secretion, and ultimately reduces gonadal sex hormone production (testosterone in males, oestrogens in females) — the core mechanism behind its use in androgen-driven prostate cancer and oestrogen-driven endometriosis.

The predicted link to hypertrichosis is mechanistically tenuous. Triptorelin's androgen-lowering effect could theoretically reduce androgen-dependent excessive hair growth (i.e., **hirsutism**). However, **hypertrichosis is clinically and pathophysiologically distinct from hirsutism**: it is a non-androgen-dependent, generalised excess hair growth driven by genetic mutations (e.g., ABCA5, FGF5), drug side effects (ciclosporin, minoxidil, phenytoin), or systemic metabolic disease. Suppressing the GnRH–gonadal axis does not address the underlying pathology of hypertrichosis.

The sole available publication (PMID 41822646, 2026) actually works against this prediction: it describes a transgender woman who developed **ciclosporin-induced generalised hypertrichosis while already receiving triptorelin** as a testosterone blocker, demonstrating that profound androgen suppression was insufficient to prevent drug-triggered hypertrichosis. This is an adverse event report, not a therapeutic study. The TxGNN prediction most likely reflects topological proximity between GnRH-related nodes and hair-disorder nodes in the knowledge graph rather than any clinically meaningful repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Triptorelin in Hypertrichosis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [41822646](https://pubmed.ncbi.nlm.nih.gov/41822646/) | 2026 | Case Report | Cureus | A 25-year-old transgender woman receiving triptorelin + estradiol for gender-affirming therapy developed generalised hypertrichosis after starting ciclosporin for psoriasis. The case illustrates that ciclosporin can induce hypertrichosis even under conditions of profound androgen suppression. This is an adverse event report — it does not evaluate or support triptorelin as a therapeutic agent for hypertrichosis. |

---

## Safety Considerations

**Drug Interactions:** 262 interactions identified in the DDInter database. Clinically notable examples include:

- **Major:** Dolasetron — risk of additive QT interval prolongation; avoid co-administration or monitor ECG closely
- **Moderate (selected):** Metformin, Acarbose, Glimepiride, Pioglitazone, Chlorpropamide, Canagliflozin, Dapagliflozin, Empagliflozin, Saxagliptin, Alogliptin, Albiglutide, Dulaglutide, Palonosetron, Clarithromycin, Loperamide, Bisacodyl, Picosulfuric acid, Polyethylene glycol with electrolytes

Complete warnings and contraindications were not captured in this evidence pack. Please refer to the official package insert (e.g., Decapeptyl® or Trelstar® SmPC/PI) for full prescribing safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.997%), the hypertrichosis prediction for Triptorelin reflects knowledge-graph topology rather than biological plausibility. No clinical trials exist, the sole literature is an adverse event case report that contradicts therapeutic utility, and the drug's mechanism of action (gonadotropin suppression) does not address the non-androgen-dependent pathophysiology of generalised hypertrichosis.

**To proceed for Hypertrichosis, the following would be needed:**
- Preclinical evidence demonstrating a mechanistic role for GnRH signalling in hypertrichosis pathogenesis
- Subtype analysis to determine whether any specific hypertrichosis variant has an androgen-dependent component
- Prospective clinical studies specifically evaluating triptorelin in hypertrichosis patients

---

> ⚠️ **Secondary Finding of High Clinical Relevance**
>
> Among all 10 predicted indications in this evidence pack, **Precocious Puberty** (rank 8) carries an evidence profile that diverges sharply from the top prediction:
>
> | Item | Content |
> |------|---------|
> | TxGNN Score | 99.887% |
> | Evidence Level | **L1** (multiple completed Phase 3 RCTs) |
> | Clinical Trials | 11 (including ≥6 completed Phase 3 studies across 1-month, 3-month, and 6-month formulations) |
> | Publications | 20 (Phase 3 trials, meta-analyses, cohort studies, diagnostic studies) |
> | Recommendation | **Proceed with Guardrails** |
>
> Triptorelin (Decapeptyl®/Trelstar®) is already a regulatory-approved first-line GnRH agonist for central precocious puberty (CPP) in the EU, US, China, and multiple other jurisdictions. Multiple completed Phase 3 trials — including large Chinese paediatric studies (NCT04736602, NCT05029622) — confirm efficacy and safety across 1-month, 3-month, and 6-month prolonged-release formulations. Given that India currently has **zero registrations** for Triptorelin despite a well-established global evidence base and an unmet paediatric need in CPP, this indication represents the most actionable market and regulatory priority identified in this analysis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

