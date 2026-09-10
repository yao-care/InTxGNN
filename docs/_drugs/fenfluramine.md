---
layout: default
title: Fenfluramine
parent: 僅模型預測 (L5)
nav_order: 340
evidence_level: L5
indication_count: 4
---

# Fenfluramine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Fenfluramine: From Undocumented Original Indication to Proximal 16p11.2 Microdeletion Syndrome

## One-Sentence Summary

The evidence pack does not document fenfluramine's original approved indication or mechanism of action.
The TxGNN model predicts a possible association with **proximal 16p11.2 microdeletion syndrome** (score **99.93%**),
but **zero clinical trials** and **zero publications** currently support this direction, and the evidence pack's own mechanistic review flags the prediction as likely knowledge-graph noise rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack |
| Predicted New Indication | Proximal 16p11.2 microdeletion syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only, no trials or literature) |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for fenfluramine is not available in this evidence pack (marked as a High-severity data gap, DG002). What can be extracted from the evidence pack's own repurposing analysis is that fenfluramine acts as a serotonin releasing agent / reuptake inhibitor, with pharmacological activity centered on the appetite-regulation center and the 5-HT2C receptor.

Proximal 16p11.2 microdeletion syndrome, by contrast, is a structural chromosomal copy-number disorder presenting with developmental delay, obesity, and autism-spectrum features. Its pathophysiology stems from gene-dosage imbalance rather than a receptor or pathway that can be pharmacologically modulated. The evidence pack's own mechanistic assessment explicitly concludes there is **no direct mechanistic correspondence** between fenfluramine's serotonergic activity and the root cause of this syndrome, and suggests the high TxGNN score likely reflects an over-weighted "obesity/appetite phenotype" node association in the knowledge graph rather than a genuine therapeutic signal.

The remaining top-ranked candidates (hypervitaminosis, obsolete hypertelorism, frontorhiny) were assessed with the same conclusion — each lacks any plausible mechanistic pathway connecting fenfluramine's known pharmacology to the candidate disease, and each is attributed to probable graph co-occurrence noise rather than biological plausibility. This pattern across all four top-ranked predictions is itself a notable finding and warrants review of the underlying prediction/ranking methodology before further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

No India market authorizations found — fenfluramine is currently **not marketed** in India (total registrations: 0).

---

## Safety Considerations

**Drug Interactions**: A DDI query returned 303 total interactions on record. Notable **Major**-severity interactions include:
- Fentanyl
- Dextromethorphan
- Tramadol
- Alfentanil
- Almotriptan

Additional **Moderate**-severity interactions include Abciximab, Abiraterone, Acalabrutinib, Acarbose, Dihydrocodeine, Codeine, Formoterol, Ketorolac, Trastuzumab emtansine, Ibuprofen, Albiglutide, Salbutamol, Ethanol, and Alogliptin/Pioglitazone, among others (303 total).

Label-level warnings and contraindications are not available in this evidence pack (data gap DG001, Blocking severity) — please refer to the official package insert once obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four top-ranked predicted indications are Evidence Level L5 (no clinical trials, no literature), and the evidence pack's own mechanistic review concludes none of them have a plausible biological link to fenfluramine's known pharmacology — the high TxGNN scores are assessed as likely artifacts of knowledge-graph co-occurrence rather than genuine repurposing signals. In addition, a Blocking-severity data gap (missing TFDA/label safety data) prevents even an initial S1 safety evaluation.

**To proceed, the following is needed:**
- TFDA (or relevant regulatory) package insert warnings/contraindications (DG001, Blocking)
- Confirmed mechanism of action data from DrugBank or equivalent source (DG002, High)
- Documentation of fenfluramine's original approved indication(s)
- Re-review of the TxGNN prediction/ranking methodology, given that all top 4 candidates were independently flagged as mechanistically implausible
- If lower-ranked candidates exist with stronger mechanistic rationale, prioritize those for evaluation instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

