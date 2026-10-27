---
layout: default
title: Carbetocin
parent: Model Prediction Only (L5)
nav_order: 144
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Carbetocin: predicted new indication Isotretinoin-like syndrome (evidence level L5). Approved use: Prader-Willi syndrome, Noonan syndrome"
monitor_inn: "Carbetocin"
predicted_indications: ["isotretinoin-like syndrome", "Goodman syndrome"]
---

# Carbetocin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Carbetocin: From Prader-Willi Syndrome to Isotretinoin-like Syndrome
{: .text-alpha }

## One-Sentence Summary

Carbetocin is a long-acting oxytocin analogue, originally associated with Prader-Willi syndrome and Noonan syndrome in the knowledge graph, and used clinically to prevent postpartum haemorrhage due to uterine atony.
The TxGNN model predicts it may be effective for **isotretinoin-like syndrome**,
but **no clinical trials and no publications** currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prader-Willi syndrome, Noonan syndrome (knowledge graph; no approved indication text is available for the Indian licences) |
| Predicted New Indication | Isotretinoin-like syndrome |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, carbetocin is a long-acting oxytocin analogue that acts on the oxytocin receptor (OXTR). Pharmacology data show it is used to prevent postpartum haemorrhage due to uterine atony. An intranasal formulation (LV-101) has been developed as a treatment for Prader-Willi syndrome, aiming to reduce the extreme hunger that leads to hyperphagia.

The original indications (Prader-Willi syndrome, Noonan syndrome) are developmental or genetic syndromes. The high TxGNN score most likely reflects network proximity to other syndromic or congenital disorders rather than validated biology. No mechanistic link between oxytocin-receptor signalling and isotretinoin-like syndrome can be established from the data compiled for this report, so any rationale would be speculative.

For reference, a second prediction, **Goodman syndrome** (score 99.06%), has the same limitations. It is a rare congenital disorder with no known oxytocin-receptor-related pathophysiology, and it also has no supporting trials or literature (Evidence Level L5, Hold).

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 35607 | Cinomac 100mcg Injection (Macleods Pharmaceuticals) | Vial of 1 ml injection | Not stated |
| 73959 | Ecbosure 100mcg Injection (Torrent Pharmaceuticals) | Vial of 1 injection | Not stated |
| 184721 | Riligol Injection (Abbott) | Vial of 1 ml injection | Not stated |
| 34497 | Caritec Solution for Injection (Sun Pharmaceutical Industries) | Vial of 1 ml solution for injection | Not stated |

## Safety Considerations

- **Drug Interactions**: The interaction query returned one pharmacology entry, the oxytocin receptor (OXTR), which is carbetocin's target. It is not a drug-drug interaction. No other interacting drugs were identified.

Please refer to the package insert for further safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score. No clinical trials or literature were found, no mechanistic link can be established, and the package insert safety data are missing. Evidence Level is L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian products, obtained from the manufacturer or regulator
- Detailed mechanism of action data, to assess any biological link to isotretinoin-like syndrome
- A literature and trial search, plus a plausibility review of the disease association
- Assessment of route compatibility, since all marketed products are injectables
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

