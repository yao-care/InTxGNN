---
layout: default
title: Ferric Carboxymaltose
parent: Model Prediction Only (L5)
nav_order: 344
evidence_level: L5
indication_count: 10
---

# Ferric Carboxymaltose
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Ferric carboxymaltose: From Iron Deficiency Anemia to Bronchitis

## One-Sentence Summary

Ferric carboxymaltose is an intravenous iron replacement product globally used to treat iron deficiency anemia. The TxGNN model's top-ranked prediction is **Bronchitis**, but this signal is currently supported by **0 clinical trials** and **0 publications** — it is a pure model output with no empirical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (drug not marketed in India, `total_licenses: 0`); globally indicated as an IV iron replacement for iron deficiency anemia |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.00% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug in the evidence pack (flagged as data gap DG002, High severity). Based on general pharmacological knowledge, ferric carboxymaltose is a colloidal iron-carbohydrate complex used to replenish iron stores intravenously; it has no established anti-inflammatory, antimicrobial, or bronchodilatory pathway that would mechanistically connect it to bronchitis.

The model's own rationale for this prediction states explicitly: *"無已知機轉關聯，KG 分數推測缺乏臨床或文獻支持"* (no known mechanistic association; the KG score is speculative and lacks clinical or literature support). This is reflected in the evidence level (L5 — model prediction only) and decision stage (S0/Hold).

For context, the #2-ranked candidate — **thrombotic disease** (score 98.04%) — has meaningfully stronger, though still preliminary, support: a completed Phase 4 RCT (n=1,003) and 3 literature reports on iron-deficiency-associated thrombocytosis, placing it at Evidence Level L3. Reviewers evaluating this drug's repurposing potential may want to prioritize that direction over bronchitis, given the current evidence gap for the top-ranked prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Ferric carboxymaltose is not currently marketed in India — no licenses are recorded in the evidence pack (`market_status: Not marketed`, `total_licenses: 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Bronchitis) is a pure computational signal (L5) with no supporting clinical trials, no literature, and no plausible mechanistic hypothesis — the model's own rationale confirms this. There is currently no basis to advance this specific candidate.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001 — Blocking; required before any S1 safety review can proceed)
- Mechanism of action data (DG002 — High priority)
- Preclinical or mechanistic evidence linking iron repletion to bronchitis pathophysiology
- Consider redirecting evaluation effort toward the rank-2 candidate, thrombotic disease, which currently has stronger (L3) preliminary evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

