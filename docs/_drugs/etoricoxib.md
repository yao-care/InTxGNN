---
layout: default
title: Etoricoxib
parent: 僅模型預測 (L5)
nav_order: 329
evidence_level: L5
indication_count: 10
---

# Etoricoxib
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

# Etoricoxib: From Arthritis/Pain to Migraine Disorder

## One-Sentence Summary

Etoricoxib is a selective COX-2 inhibitor known for treating osteoarthritis, rheumatoid arthritis, ankylosing spondylitis, acute pain and gout.
The TxGNN model predicts it may be effective for **Migraine Disorder**,
but this ranking is currently supported by **0 clinical trials** and **0 publications** — it is a pure computational prediction with no direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, chronic low back pain, ankylosing spondylitis, acute pain, gout (per pharmacology database; not a TFDA-registered indication) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the current evidence pack. Based on the pharmacology data that is available, etoricoxib is a synthetic, selective cyclooxygenase-2 (COX-2 / PTGS2) inhibitor, clinically used for rheumatoid arthritis, osteoarthritis, chronic lower back pain, ankylosing spondylitis, acute pain and gout.

The predicted link to migraine disorder is described in the evidence pack itself as "purely a TxGNN knowledge-graph embedding similarity prediction." There is a theoretical mechanistic rationale — prostaglandins generated via the COX-2 pathway are implicated in neurogenic inflammation and neurovascular signaling, which plays a role in migraine pathophysiology — but this connection has **not** been tested directly for etoricoxib in migraine disorder: no clinical trials and no literature were retrieved for this specific disease term.

Notably, related but lower-ranked predictions in this same evidence pack (headache disorder, rank 9; trigeminal autonomic cephalalgia, rank 10) do have real, if weak, supporting evidence — several case reports and one case series describe etoricoxib/celecoxib responsiveness in indomethacin-responsive headache syndromes (e.g., primary stabbing headache, cough headache), which lends indirect, class-level plausibility to a COX-2-inhibitor/headache-pathway link. However, "migraine disorder" itself, the top-ranked candidate, has no such corroborating evidence and should not be conflated with these adjacent, better-evidenced entities.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

Etoricoxib currently has **0 registrations** and is **not marketed** in Taiwan (source: taiwan_regulatory dataset); no license records are available to summarize.

---

## Safety Considerations

- **Drug Interactions**: The safety database record for etoricoxib describes its pharmacological target (COX-2 / PTGS2 gene, human) rather than a specific interacting drug or DDI severity level; no actionable drug-pair interaction data is currently available.

Formal key warnings and contraindications are not available in the current evidence pack. Please refer to the package insert for complete safety information. Separately, unrelated literature surfaced during evidence collection for other candidate indications flags known class-level COX-2 inhibitor safety signals worth keeping in view — a case report of etoricoxib-induced life-threatening hyperkalemia and acute kidney injury (in combination with telmisartan and a low-sodium diet), and a case report of possible etoricoxib-associated reversible cerebral vasoconstriction syndrome — consistent with the established cardiovascular/renal risk profile of selective COX-2 inhibitors.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (migraine disorder) is supported only by a TxGNN model score with zero clinical trials and zero literature — this is an L5, model-only signal per the evidence pack's own scoring, insufficient to advance past initial screening.

**To proceed, the following is needed:**
- TFDA/manufacturer label data on warnings, contraindications, and confirmed original indications (currently blocking, per DG001)
- Confirmed mechanism-of-action documentation (currently a data gap, per DG002)
- Targeted literature/clinical-trial search specifically on "etoricoxib" AND "migraine" to confirm the absence of evidence is not a search-term artifact
- If pursuing the COX-2/headache-pathway angle at all, consider re-scoping toward the better-evidenced adjacent candidates (headache disorder, trigeminal autonomic cephalalgia) rather than migraine disorder itself, and note their evidence is limited to case reports/case series only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

