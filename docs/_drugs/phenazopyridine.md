---
layout: default
title: Phenazopyridine
parent: 僅模型預測 (L5)
nav_order: 653
evidence_level: L5
indication_count: 1
---

# Phenazopyridine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Phenazopyridine: From Urinary Tract Infection Symptom Relief to Bronchitis

## One-Sentence Summary

Phenazopyridine is an azo-dye urinary tract analgesic used to relieve dysuria, urgency, and pain caused by urinary tract infection; it has no marketing authorization in Taiwan. The TxGNN model predicts a possible new use for **Bronchitis** with a high raw score (99.23%), but this is currently supported by **zero clinical trials** and **zero publications**, and the evidence pack's own mechanistic assessment suggests this is most likely a knowledge-graph false positive rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection–related dysuria, urgency, and pain (urinary analgesic) — no Taiwan license record exists to confirm formal labeled indication |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.23% (rank 11,844) |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for phenazopyridine is not available (flagged as a High-severity data gap). Based on known clinical use, phenazopyridine is taken orally, excreted renally, and exerts a local analgesic effect on the bladder/urethral mucosa — it is used solely to relieve the burning, urgency, and pain of urinary tract infection. Its exact molecular mechanism has never been fully elucidated.

There is no known pharmacological pathway connecting this urinary-tract local analgesic effect to bronchitis (a respiratory tract infection/inflammation) — phenazopyridine has no established anti-inflammatory, bronchodilatory, antimicrobial, or antitussive/expectorant activity. The original indication (urinary system) and the predicted new indication (respiratory system) do not share an obvious anatomical, mechanistic, or therapeutic-class relationship.

Given the absence of any supporting clinical trials, literature, or plausible mechanistic link, the most likely explanation is that this is a **false-positive association in the knowledge graph** — potentially arising from indirect comorbidity or adverse-event edges connecting "urinary symptoms" and "respiratory symptoms" nodes, rather than a real pharmacological relationship. This assessment is consistent with the evidence pack's own repurposing rationale and its "Hold" recommendation at decision stage S0.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Phenazopyridine currently holds **no marketing license in Taiwan** (0 registrations, market status: 未上市). No product, dosage form, or approved-indication data is available.

---

## Safety Considerations

- **Drug Interactions**: 24 documented interactions in total (source: DDInter). Notable entries include:

| Interacting Drug | Level |
|---|---|
| Nitrous acid | Major |
| Leflunomide | Major |
| Naltrexone | Moderate |
| Methotrexate | Moderate |
| Lidocaine (topical/ophthalmic) | Moderate |
| Benzocaine (topical) | Moderate |
| Cocaine (nasal/topical) | Moderate |
| Tetracaine (ophthalmic/topical) | Moderate |
| Oxybuprocaine (ophthalmic) | Moderate |
| Cinchocaine (topical) | Moderate |
| Asparaginase Escherichia coli | Moderate |
| Brentuximab vedotin | Moderate |
| Clofarabine | Moderate |
| Idelalisib | Moderate |
| Interferon beta-1a / beta-1b | Moderate |
| Pegaspargase | Moderate |

Package-insert warnings and contraindications are currently unavailable (Blocking data gap — TFDA label not yet obtained), so this information cannot be assessed at this time.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on TxGNN score alone (L5, no clinical or literature support), and the mechanistic review found no plausible pathway linking a urinary-tract analgesic to bronchitis — the signal is most likely a false positive from indirect knowledge-graph edges. In addition, the drug is not marketed in Taiwan and TFDA label safety data is missing (Blocking gap), which by itself prevents even an initial safety screen (S1).

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently Blocking
- Confirmed mechanism of action (DrugBank or primary literature) — currently High-severity gap
- At minimum, preclinical or mechanistic evidence connecting phenazopyridine to respiratory tract pathology before any further evaluation stage is considered
- Independent confirmation that the KG edge is not an artifact (e.g., re-run prediction excluding shared adverse-event/comorbidity edges)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

