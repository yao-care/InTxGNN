---
layout: default
title: Spironolactone
parent: 僅模型預測 (L5)
nav_order: 780
evidence_level: L5
indication_count: 2
---

# Spironolactone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Spironolactone: From Aldosterone-Antagonist Diuretic Therapy to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

> Spironolactone is a well-established aldosterone receptor antagonist (potassium-sparing diuretic) used internationally for edema, hypertension, and heart failure.
> The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model output with no external corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not present in current regulatory dataset (drug is not marketed here); internationally known as an aldosterone antagonist for edema, hypertension, and heart failure |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, Spironolactone is an aldosterone receptor antagonist with additional antiandrogenic activity, and is used off-label for **androgenetic alopecia** by blocking the androgen receptor and reducing DHT activity. This is a legitimate, mechanistically grounded repurposing precedent.

However, the disease predicted here — **hypotrichosis simplex of the scalp** — is a different entity: an autosomal dominant *congenital* hair-loss disorder most commonly linked to **APCDD1 mutations** and dysregulation of the **Wnt signaling pathway**, not androgen-driven miniaturization. There is no known biochemical pathway connecting aldosterone/androgen-receptor blockade to Wnt-pathway–mediated congenital hypotrichosis.

The most likely explanation is that TxGNN's prediction is driven by **phenotypic surface similarity** ("hair thinning/loss" as a shared symptom node) rather than a true shared molecular mechanism — a known limitation of knowledge-graph embedding models when a drug already has strong ties to superficially similar phenotypes (in this case, androgenetic alopecia). A second, lower-confidence candidate from the same evidence pack — *congenital hypotrichosis milia* — shows the identical pattern: a rare genetic hair-and-skin disorder with no plausible link to Spironolactone's known pharmacology, reinforcing that this is likely a graph-topology artifact rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Spironolactone is currently **not marketed** under this regulatory dataset (0 registrations, 0 licenses on file), so no authorization table can be produced.

---

## Safety Considerations

- **Drug Interactions**: 272 known interactions on record (DDInter). Notable examples:
  - **Major**: Loperamide
  - **Moderate**: Hydrocortisone, Metformin, Bupropion, Triamcinolone, Morphine, Dexamethasone, Betamethasone, Bisacodyl, Budesonide, Castor oil, Dronabinol, Exenatide, and SGLT2 inhibitors (Canagliflozin, Dapagliflozin, Empagliflozin, Ertugliflozin)
  - **Minor**: Doxycycline, Acetylsalicylic acid, Fidaxomicin

Label-level key warnings and contraindications are not yet available for this drug (blocking data gap — see below); please refer to the official package insert once obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN similarity score, the mechanistic basis is weak (androgen/aldosterone pathway vs. a Wnt-pathway congenital genetic disorder), there is zero clinical trial or literature support, and the drug is not currently marketed in this jurisdiction. This is an L5, model-only signal that does not meet the bar for further evaluation.

**To proceed, the following is needed:**
- TFDA (or equivalent local regulator) package insert data — warnings and contraindications (blocking gap, DG001)
- Confirmed mechanism of action via DrugBank API (DG002)
- Any preclinical or genetic evidence linking androgen/mineralocorticoid receptor modulation to Wnt-pathway hair follicle biology
- At minimum, case-level or preclinical evidence specific to hypotrichosis simplex of the scalp before this candidate can move beyond Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

