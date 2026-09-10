---
layout: default
title: Sparfloxacin
parent: 僅模型預測 (L5)
nav_order: 779
evidence_level: L5
indication_count: 9
---

# Sparfloxacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Sparfloxacin: From Unknown Original Indication to Hyperamylasemia

## One-Sentence Summary

> Sparfloxacin is a fluoroquinolone-class antibacterial agent (inhibiting bacterial DNA gyrase/topoisomerase IV per class knowledge); its specific original approved indication is not captured in this evidence pack.
> The TxGNN model predicts it may be effective for **Hyperamylasemia**, but this is a **model-only prediction (L5)** — the evidence pack itself notes no clinical trials, no literature, and **no plausible mechanistic link**, and flags the signal as possibly reflecting knowledge-graph node proximity rather than real biology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this pack (Data Gap); known generically as a fluoroquinolone-class antibacterial |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 (model prediction only, no supporting trials/literature, no mechanistic link) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa` is a Data Gap in this pack). Based on other fields in the evidence pack, Sparfloxacin is described as a fluoroquinolone-class antibiotic that inhibits bacterial DNA gyrase/topoisomerase IV — a mechanism relevant to treating bacterial infections, not to metabolic/enzymatic conditions like hyperamylasemia.

For the top-ranked prediction, the pack's own rationale is explicit: *"無明確機轉關聯。Hyperamylasemia 多與胰臟/唾液腺病理相關，抗生素類藥物無已知直接作用路徑，此預測可能反映知識圖譜節點鄰近性而非真實生物學訊號"* — i.e., there is no known biological pathway connecting a DNA gyrase inhibitor to pancreatic/salivary-gland amylase overproduction, and the high TxGNN score likely reflects graph topology rather than pharmacology.

Notably, among the 9 ranked candidates in this pack, only **septicemic plague** (rank 8) has class-level mechanistic plausibility — other fluoroquinolones (ciprofloxacin, levofloxacin) are approved for *Yersinia pestis* infection, and one loosely related PMID (antibiotic persistence in uropathogenic *E. coli*) was retrieved — though no sparfloxacin-specific evidence exists there either. This does not change the assessment of the rank-1 candidate (hyperamylasemia), which remains mechanistically unsupported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

No marketing authorizations are registered for Sparfloxacin in Taiwan (market status: 未上市 / not marketed; total licenses: 0).

---

## Safety Considerations

**Drug Interactions**: The evidence pack contains 239 recorded interactions. Major-severity interactions identified include:

| Interacting Drug | Level | Source |
|---|---|---|
| Hydrocortisone | Major | ddinter |
| Bupropion | Major | ddinter |
| Triamcinolone | Major | ddinter |
| Dexamethasone | Major | ddinter |
| Betamethasone | Major | ddinter |
| Chlorpropamide | Major | ddinter |

Additional Moderate-level interactions (partial list, 239 total recorded): Acarbose, Famotidine, Albiglutide, Alogliptin, Metformin, Pioglitazone, Loperamide, Acetylsalicylic acid, Balsalazide, Bisacodyl, Calcium Phosphate, Calcium acetate, Canagliflozin, Potassium citrate.

Key warnings and contraindications for Sparfloxacin are not available in this pack (Data Gap DG001, flagged as **Blocking** — this prevents a full S1 safety assessment). Please refer to the official package insert once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (hyperamylasemia) has no supporting clinical trials, no literature, and no plausible mechanistic link — the evidence pack itself flags this as a likely knowledge-graph artifact rather than a genuine biological signal. Combined with the drug's unmarketed status in Taiwan (0 licenses) and a blocking data gap on TFDA label warnings/contraindications, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking — required before any S1 safety screening)
- Confirmed mechanism of action data (DG002)
- If pursuing an antibacterial-indication angle instead, consider re-evaluating **septicemic plague** (rank 8), which has class-level mechanistic plausibility (fluoroquinolone class effect against *Yersinia pestis*), though sparfloxacin-specific evidence would still need to be generated
- Independent biological/literature review to confirm or rule out the hyperamylasemia signal before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

