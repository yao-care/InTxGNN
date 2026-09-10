---
layout: default
title: Cycloserine
parent: 僅模型預測 (L5)
nav_order: 217
evidence_level: L5
indication_count: 7
---

# Cycloserine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cycloserine: From Tuberculosis to Irritable Bowel Syndrome

## One-Sentence Summary

Cycloserine is a second-line antitubercular agent (D-alanine racemase/ligase inhibitor) used historically for multidrug-resistant pulmonary tuberculosis, and it is currently **not marketed in Taiwan**. The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome**, with a very high prediction score (**99.95%**), but this is currently supported by **zero clinical trials** and **zero publications** — the evidence pack itself flags no known mechanistic link to this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (multidrug-resistant pulmonary TB) — inferred from literature within this evidence pack; no official TFDA-approved indication text is available since the drug is unregistered in Taiwan |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is currently a data gap (DG002). Based on information available within this evidence pack, Cycloserine is known to act as an inhibitor of bacterial D-alanine racemase/ligase (its antitubercular mechanism) and separately as a partial agonist at the NMDA receptor — a property exploited in several psychiatric/neurological trials referenced elsewhere in this pack (e.g., PTSD, bipolar depression).

Neither of these two known mechanisms has an established link to irritable bowel syndrome pathophysiology (gut motility or brain-gut axis signaling). The evidence pack's own rationale for this candidate is explicit on this point: *"No known mechanistic link; cycloserine's antibacterial and NMDA partial-agonist activity has no direct connection to IBS gut motility/brain-gut axis pathophysiology — this is a pure TxGNN computational prediction with no clinical trial or literature support."*

In other words, the high TxGNN score reflects a statistical association learned from the knowledge graph rather than a biologically or clinically substantiated hypothesis. Note also that among the other candidates in this pack, insomnia (rank 5) has comparatively more real-world evidence (3 trials, 2 case reports) — but that evidence points toward cycloserine **causing** insomnia as an adverse effect during TB treatment, not treating it, which is the opposite of a repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

**Drug Interactions** (from DDI database, 11 total interactions identified):

- **Major**: Bupropion, Ethanol, Iohexol, Iopamidol
- **Moderate**: Picosulfuric acid, Polyethylene glycol (3350 with electrolytes), Sodium sulfate, Caffeine, Dicoumarol, Warfarin, Lindane

Detailed key warnings and contraindications are a data gap (DG001, Blocking severity) pending TFDA label retrieval — please refer to the package insert once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The IBS prediction (TxGNN score 99.95%) is a pure model-derived association (L5) with no supporting mechanistic rationale, clinical trials, or literature — the evidence pack itself states there is no known biological connection. Combined with the drug not being marketed in Taiwan and two Blocking/High-severity data gaps (TFDA label, MOA), this candidate does not meet the bar to advance past S0.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA label warnings/contraindications) — currently Blocking for any safety review
- Resolve DG002 (confirmed mechanism of action via DrugBank)
- Preclinical or mechanistic studies linking cycloserine's NMDA/antibacterial activity to gut motility or visceral hypersensitivity pathways relevant to IBS
- At minimum, one exploratory clinical study or case series in IBS patients before this candidate can move beyond S0/Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

