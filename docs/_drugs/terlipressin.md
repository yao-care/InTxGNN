---
layout: default
title: Terlipressin
parent: 僅模型預測 (L5)
nav_order: 818
evidence_level: L5
indication_count: 10
---

# Terlipressin
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

# Terlipressin: From Variceal Bleeding and Hepatorenal Syndrome to Open-Angle Glaucoma

## One-Sentence Summary

Terlipressin is a synthetic vasopressin analogue historically used to control acute variceal bleeding and hepatorenal syndrome in patients with liver cirrhosis. The TxGNN model predicts it may be effective for **Open-Angle Glaucoma**, but this direction is currently supported by **zero clinical trials** and **zero published literature** — it is a pure knowledge-graph association without pharmacological or clinical backing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute variceal bleeding / hepatorenal syndrome (established clinical use; formal India label text not available) |
| Predicted New Indication | Open-Angle Glaucoma |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (data gap, high severity). Based on established clinical knowledge, terlipressin is a V1 vasopressin-receptor agonist whose therapeutic value comes from potent splanchnic vasoconstriction, which is why it is used for variceal hemorrhage and hepatorenal syndrome — conditions driven by portal hypertension and systemic vasodilation in cirrhosis.

There is no clinical or mechanistic evidence connecting this V1-agonist vasoconstrictive action to intraocular pressure reduction in open-angle glaucoma. The high TxGNN score reflects a purely statistical knowledge-graph association rather than established pharmacology. If anything, systemic vasoconstrictors could theoretically raise rather than lower intraocular pressure, which runs counter to the therapeutic goal in glaucoma. As the evidence pack's own rationale notes, this prediction has "no pharmacological plausibility" supporting the connection.

Given the complete absence of clinical trials, literature, or mechanistic rationale, this candidate should be treated as a low-confidence model artifact rather than a genuine repurposing signal at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

Terlipressin is not currently marketed in India — the evidence pack shows a market status of "未上市" (Not Marketed) with 0 registered licenses. No authorization records are available for extraction.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there are no clinical trials, no supporting literature, and no mechanistic rationale linking terlipressin's V1-agonist vasoconstrictive action to intraocular pressure reduction — this is an L5, S0-stage prediction with no evidentiary support. Note also that other predictions for this drug (e.g., rank 3, pulmonary hypertension in the context of cirrhosis, L3/S1 with cohort-level literature) show meaningfully stronger evidence and may warrant separate evaluation.

**To proceed, the following is needed:**
- Confirmed mechanism of action data (DG002, currently a data gap)
- TFDA/CDSCO label warnings and contraindications (DG001, blocking gap for safety review)
- Preclinical or mechanistic studies on vasopressin agonists and intraocular pressure
- Any real-world or case-level evidence before advancing past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

