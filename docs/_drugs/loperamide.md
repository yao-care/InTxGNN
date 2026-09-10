---
layout: default
title: Loperamide
parent: 僅模型預測 (L5)
nav_order: 494
evidence_level: L5
indication_count: 10
---

# Loperamide
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

# Loperamide: From Antidiarrheal Use to Acute Contagious Conjunctivitis

## One-Sentence Summary

Loperamide (DB00836) is a peripheral opioid-receptor agonist widely used as an antidiarrheal; the evidence pack does not include a sourced original-indication text, but this is well-established background knowledge, not a claim from the dataset.
The TxGNN model predicts a possible new application in **Acute Contagious Conjunctivitis**, with a very high raw prediction score (99.97%) but **zero clinical trials and zero literature** currently supporting this direction.
Given the complete absence of supporting evidence and no plausible mechanistic link between a gut-selective opioid agonist and ocular infection, this prediction should be treated as low-confidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in evidence pack (regulatory/indication fields empty); commonly known as an antidiarrheal agent |
| Predicted New Indication | Acute Contagious Conjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (`original_moa: [Data Gap]`). Loperamide is generally known to act as a peripheral μ-opioid receptor agonist in the gut wall, slowing intestinal motility; it does not cross the blood-brain barrier appreciably and has no established ocular or anti-infective pharmacology.

There is no mechanistic pathway connecting loperamide's gut-motility effect to acute contagious conjunctivitis, which is typically caused by viral or bacterial infection and treated with topical antimicrobials or antivirals, not opioid-receptor agents.

Notably, this evidence pack's own scoring of several other top-10 predictions (ranks 5–10) — all conjunctivitis-related diseases with nearly identical TxGNN scores (~0.996) — were explicitly flagged by prior analysis as "graph embedding noise from a clustered conjunctivitis node group" with recommendation "Hold." Rank 1 (this indication) shares the same evidence pattern (zero clinical trials, zero literature) and an even higher score, making it very likely part of the same structural artifact rather than a genuine biological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

**Drug Interactions** (from DDI database, 591 total interactions on file; representative Major-level interactions):
- **Abiraterone** — Major
- **Ranitidine** — Major
- **Fosamprenavir** — Major
- **Gemfibrozil** — Major

Representative Moderate-level interactions include Chlorpheniramine, Dihydrocodeine, Codeine, Tramadol, Ethanol, and several others (591 total interactions on record).

Key warnings and contraindications are not available in this evidence pack (marked as data gaps). Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication has no clinical trial or literature support, no plausible mechanistic rationale, and matches the same score/evidence pattern already identified elsewhere in this dataset as likely graph-structure noise rather than a genuine repurposing signal. This does not meet even the minimum bar (L4/L3) for further evaluation.

**To proceed, the following is needed:**
- TFDA/regulatory label (warnings, contraindications) — currently a Blocking data gap (DG001), required before any S1 safety screening
- Confirmed mechanism of action (DG001/DG002) to properly assess biological plausibility
- If ranks 2 ("amebic dysentery") or 4 ("gastroduodenitis") are of interest instead, those have supporting literature and a more plausible GI-related mechanistic link, and would warrant separate evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

