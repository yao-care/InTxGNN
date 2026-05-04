---
layout: default
title: Choline Salicylate
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Choline Salicylate
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

# Choline Salicylate: From Analgesic/Anti-inflammatory Use to Prinzmetal Angina

## One-Sentence Summary

Choline salicylate is a salicylate-class compound with analgesic and anti-inflammatory properties, related to aspirin in its pharmacological mechanism.
The TxGNN model predicts it may be effective for **Prinzmetal Angina** (variant angina due to coronary vasospasm),
with **0 clinical trials** and **0 publications** directly supporting this indication — evidence currently rests at the mechanistic hypothesis stage only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in India; salicylate-class analgesic/anti-inflammatory (class-level knowledge) |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological knowledge, choline salicylate is a choline salt of salicylic acid — a member of the same drug family as aspirin. Like other salicylates, it exerts analgesic, antipyretic, and anti-inflammatory effects primarily through cyclooxygenase (COX) inhibition. The choline salt formulation is thought to produce less gastrointestinal mucosal irritation compared to acetylsalicylic acid, which gives it a theoretical tolerability advantage.

The proposed mechanistic link to Prinzmetal angina relies on COX-1 inhibition reducing thromboxane A2 (TXA2) — a potent coronary vasoconstrictor and platelet aggregator. Lower TXA2 levels could theoretically attenuate the vasospasm episodes that define Prinzmetal angina. This reasoning parallels the well-established use of low-dose aspirin in atherothrombotic cardiovascular disease, where antiplatelet effects are the primary benefit.

However, this rationale carries significant caveats. High-dose salicylate therapy simultaneously suppresses prostacyclin (PGI2) — a natural vasodilator — which could offset or reverse any vasodilatory benefit. More importantly, all relevant cardiovascular evidence derives from aspirin studies; there is no direct research on choline salicylate in coronary vasospasm. The TxGNN prediction is mechanistically plausible but remains purely theoretical at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Choline salicylate is currently not registered or marketed in India. No authorization records are available in the regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN confidence score (99.84%), there are zero clinical trials and zero publications directly investigating choline salicylate in Prinzmetal angina. Combined with no India regulatory history, absent safety documentation, and a mechanism inferred entirely from aspirin class-effect data rather than from the compound itself, the evidence base does not support moving forward at this time.

**To proceed, the following is needed:**

- **MOA verification**: Retrieve choline salicylate mechanism of action from DrugBank API (DB14006) to confirm COX pathway relevance
- **Safety package**: Download and parse the CDSCO / FDA package insert for key warnings, contraindications, and drug interaction profile — currently a blocking data gap (DG001)
- **Salicylate class literature review**: Search specifically for aspirin or salicylate use in Prinzmetal angina / coronary vasospasm as a class-effect reference point before investing in choline salicylate-specific research
- **PK/PD feasibility**: Assess whether oral choline salicylate achieves plasma concentrations sufficient for cardiovascular COX-1 inhibition, since current formulations are primarily used for local analgesic effects
- **Regulatory pathway scoping**: Given zero India registrations, evaluate whether any global reference market (EU, US, Japan) has approved choline salicylate for a cardiovascular indication before initiating repurposing activities
- **Consider rank 2 (Rheumatoid Arthritis) as a higher-priority target**: The RA indication has stronger historical and mechanistic grounding — salicylates were the standard RA treatment before DMARDs — and may present a more tractable starting point for a Choline salicylate repurposing program

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

