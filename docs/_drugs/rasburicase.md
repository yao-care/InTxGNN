---
layout: default
title: Rasburicase
parent: 僅模型預測 (L5)
nav_order: 722
evidence_level: L5
indication_count: 10
---

# Rasburicase
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

Using no additional skill — this is a direct content-generation task governed entirely by the report-writing prompt already supplied.

---

# Rasburicase: From Unspecified Original Indication to Renal Hypouricemia

## One-Sentence Summary

> Rasburicase's original approved indication and mechanism of action are not documented in the currently available data. The TxGNN model's top-ranked prediction points to **Renal Hypouricemia**, but this pairing is mechanistically implausible — the drug's known pharmacological effect (lowering serum uric acid) runs in the *opposite* direction of the predicted disease's pathology (excessive renal uric acid loss) — and it is currently backed by **zero clinical trials and zero publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in available data (data gap) |
| Predicted New Indication | Renal Hypouricemia (hypouricemia, renal) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Rasburicase is not available in the current evidence pack, and no original approved indication is on record. This is flagged as a **Blocking** data gap (DG001 – TFDA label/warnings) and a **High**-severity gap (DG002 – MOA), meaning the drug cannot yet complete a full safety pre-assessment.

More importantly, the top-ranked prediction itself does not hold up mechanistically. Renal Hypouricemia is a condition of *abnormally low* serum uric acid caused by defective renal urate reabsorption. Rasburicase's documented pharmacological identity is as a **urate-oxidase enzyme that actively reduces serum uric acid** — the same direction as the disease pathology, not the opposite of it. Applying a uric-acid-lowering agent to a low-uric-acid condition is not just unsupported, it is directionally counter-indicated. The evaluation notes for this candidate explicitly flag it as a likely **false positive** arising from TxGNN's knowledge-graph proximity around the "uric acid metabolism" node, rather than a genuine repurposing signal.

A more mechanistically coherent candidate exists further down the ranked list: **rank 2, HGPRT partial deficiency (Kelley-Seegmiller syndrome)**. This condition causes purine salvage pathway blockage and uric acid *overproduction* — the same direction Rasburicase is known to act on. That candidate has been staged as a "Research Question" (S1) rather than "Hold," reflecting its higher plausibility, though it still has no supporting trials or literature. If this evaluation is to proceed, the HGPRT-deficiency candidate — not the current rank-1 pairing — is the more defensible starting point.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Rasburicase currently has **no marketing authorization records in Taiwan** — market status is "Not Marketed" with 0 registered licenses on file. No product name, dosage form, or approved-indication text is available to summarize.

---

## Safety Considerations

- **Drug Interactions**: 13 interactions on record. Two are classified **Major**: co-administration with **Prilocaine** and with **Nitrous acid**. The remaining 11 are classified **Moderate**, predominantly involving local/topical anesthetics — Tetracaine (ophthalmic/topical), Lidocaine (topical/ophthalmic), Benzocaine (topical), Cocaine (topical/nasal), Proparacaine (ophthalmic), Oxybuprocaine (ophthalmic), Cinchocaine (topical) — plus **Idelalisib**.

Key warnings and contraindications are not available in the current data (marked as data gaps) and are therefore omitted; please refer to the official package insert once obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Renal Hypouricemia) is mechanistically implausible and most likely a knowledge-graph false positive; it should not be pursued as presented. Combined with two unresolved data gaps — missing TFDA label/warning data (Blocking) and missing MOA data (High) — the candidate as currently framed cannot pass initial safety screening (S1).

**To proceed, the following is needed:**
- TFDA label/warnings and contraindications for Rasburicase (resolves DG001, required before any S1 safety assessment)
- Confirmed mechanism of action from DrugBank or equivalent primary source (resolves DG002)
- Re-scope the repurposing hypothesis toward the mechanistically coherent candidate — **HGPRT partial deficiency (Kelley-Seegmiller syndrome)** — and seek case series, retrospective studies, or preclinical evidence, since no clinical or literature evidence currently exists for it either
- If Renal Hypouricemia is to remain under consideration at all, an explicit clinical/biological rationale must be provided to justify a uric-acid-lowering agent in a uric-acid-wasting condition; absent that, this candidate should be formally excluded rather than carried forward
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

