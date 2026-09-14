---
layout: default
title: Tolmetin
parent: 僅模型預測 (L5)
nav_order: 838
evidence_level: L5
indication_count: 10
---

# Tolmetin
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

# Tolmetin: From NSAID Use to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

> Tolmetin is a non-steroidal anti-inflammatory drug (NSAID), historically used for rheumatoid arthritis, osteoarthritis, and juvenile rheumatoid arthritis.
> The TxGNN model's top-ranked prediction is **Acromesomelic dysplasia, Hunter-Thompson type**, but this is supported by **0 clinical trials** and **0 publications**,
> and the evidence pack's own mechanistic assessment flags this as a likely knowledge-graph embedding artifact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in India regulatory data; internationally known for rheumatoid arthritis, osteoarthritis, and juvenile rheumatoid arthritis (NSAID class) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for Tolmetin is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, Tolmetin is an NSAID that inhibits COX-1/COX-2 enzymes, reducing prostaglandin synthesis to produce anti-inflammatory and analgesic effects.

The top-ranked TxGNN prediction, however, does **not** have a plausible mechanistic link to this MOA. Acromesomelic dysplasia, Hunter-Thompson type is a rare monogenic skeletal dysplasia caused by *GDF5* mutations, with no established inflammatory or COX-pathway pathology. The evidence pack's own rationale explicitly states this is "極可能為知識圖譜嵌入雜訊（embedding artifact）" — most likely graph-embedding noise rather than a real pharmacological signal. The same caveat applies to ranks 2–6, 8, 9, and 10 in this candidate set, all of which are rare genetic/developmental syndromes without inflammatory pathology.

Among the ten predictions reviewed, only **rheumatoid factor-positive polyarticular juvenile idiopathic arthritis** (rank 7, score 99.75%) shows a mechanistically coherent link: Tolmetin's COX inhibition is consistent with its historical clinical use in juvenile rheumatoid arthritis. This candidate reached Evidence Level L4 / Decision Stage S1 ("Research Question"), notably higher than the top-ranked candidate, though it still lacks direct trial or literature support in this dataset.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

Tolmetin is currently not marketed in India (0 registrations); no license or approved-indication records are available in this evidence pack.

---

## Safety Considerations

- **Drug Interactions**: 153 total interactions identified (DDInter). Notable **Moderate**-level interactions include:
  - Corticosteroids (Hydrocortisone, Triamcinolone, Dexamethasone, Betamethasone, Budesonide) — combined use with NSAIDs may increase GI bleeding/ulceration risk
  - Other NSAIDs/analgesics (Acetylsalicylic acid)
  - Antidiabetic agents (Metformin, Chlorpropamide, Glimepiride)
  - Aminosalicylates (Mesalazine, Balsalazide)
  - Potassium supplements (Potassium citrate, Potassium bicarbonate)
  - Naltrexone

  **Minor**-level interactions include H2-antagonists (Famotidine, Ranitidine, Cimetidine) and Linaclotide.

Detailed key warnings and contraindications (TFDA/India label) are not yet available — this is flagged as a **Blocking** data gap (DG001) and must be resolved before any safety-stage review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has a very high TxGNN score but no supporting clinical or literature evidence, and its own mechanistic assessment identifies it as likely model noise rather than a genuine signal. Combined with the absence of India market presence, MOA data, and label safety data (Blocking data gap DG001), this candidate does not meet the bar to advance.

**To proceed, the following is needed:**
- India/TFDA label warnings and contraindications (DG001, Blocking) — required before any S1 safety review
- Confirmed mechanism of action data (DG002, High) — required to validate or rule out mechanistic plausibility
- Independent validation of the rank-1 prediction (e.g., re-run with alternative embedding/model) given the self-flagged noise concern
- If pursuing an alternative direction: clinical trial and literature search specifically for Tolmetin in rheumatoid factor-positive polyarticular juvenile idiopathic arthritis (rank 7), which currently has the strongest mechanistic rationale in this candidate set despite lacking direct evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

