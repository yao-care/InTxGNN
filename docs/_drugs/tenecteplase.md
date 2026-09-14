---
layout: default
title: Tenecteplase
parent: 僅模型預測 (L5)
nav_order: 808
evidence_level: L5
indication_count: 10
---

# Tenecteplase
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

# Tenecteplase: From ST-Elevation Myocardial Infarction to Posteroinferior Myocardial Infarction

## One-Sentence Summary

> Tenecteplase is a fibrin-specific thrombolytic (recombinant tissue plasminogen activator) whose established clinical role — evident throughout this evidence pack's rationale text — is dissolving clots in ST-elevation myocardial infarction (STEMI).
> The TxGNN model predicts it may be effective for **Posteroinferior Myocardial Infarction**, an anatomical subtype of STEMI,
> but currently **0 clinical trials** and **0 publications** specifically address this disease term — the high score appears to reflect ontology granularity rather than a novel mechanistic finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in India licensing data (drug is not marketed); evidence-pack rationale identifies the established use as ST-elevation myocardial infarction (STEMI) thrombolysis |
| Predicted New Indication | Posteroinferior Myocardial Infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| India Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (MOA: flagged as a Data Gap, remediation pending via DrugBank API). Based on the rationale attached to this prediction, tenecteplase is a fibrin-specific plasminogen activator used for thrombolysis, and its proven efficacy is in ST-elevation myocardial infarction (STEMI). "Posteroinferior myocardial infarction" is not a separate disease from a treatment standpoint — it is an anatomical/ECG-localization label describing infarction involving the inferior and posterior left ventricular walls, a subtype that already falls squarely within the standard STEMI reperfusion indication.

The evidence pack's own rationale is explicit on this point: it characterizes the top four ranked predictions (posteroinferior MI, posterolateral MI, septal MI, and congenital coronary artery anomaly) as reflecting "本體顆粒度問題" (ontology granularity issues) rather than genuine mechanistic gaps. Because the knowledge graph's disease vocabulary encodes each anatomical MI subtype as a distinct node, TxGNN assigns them nearly identical, very high scores (~99.85–99.87%) — not because of subtype-specific evidence, but because tenecteplase's thrombolytic mechanism mechanistically covers all STEMI presentations equally. This also explains the absence of dedicated trials: clinical studies are conducted and reported under the broader "STEMI" umbrella, not stratified by ECG-localized anatomical subtype.

One related candidate in the same pack — coronary stenosis (rank 5, intracoronary low-dose tenecteplase adjunct to primary PCI) — does have a completed Phase 2 RCT (ICE-T/ICE-T-TIMI-49, n=40) and is scored at evidence level L2 with a "Proceed with Guardrails" recommendation. That candidate represents the more clinically actionable signal in this evidence pack; posteroinferior MI, by contrast, should be read as confirmation of existing practice rather than a new repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

Tenecteplase currently has **no registered licenses in India** (`total_licenses: 0`, `market_status: 未上市`). No product registrations, brand names, or approved-indication text are available in this evidence pack.

---

## Safety Considerations

Key warnings and contraindications are not currently available for this evidence pack (flagged as a Blocking data gap — DG001: TFDA/India label warnings and contraindications, pending PDF label retrieval and parsing).

**Drug Interactions**: 137 total interactions identified (source: DDInter). Notable **Major**-severity interactions include: Deferasirox, Ibritumomab tiuxetan, Tositumomab, Tositumomab (I-131), Abciximab, Acalabrutinib, Apixaban, Avapritinib, and Betrixaban — largely reflecting additive bleeding risk with other anticoagulants/antiplatelets and immunoconjugates. **Moderate**-severity interactions include NSAIDs (Ibuprofen, Ketorolac, Ketorolac ophthalmic, Diclofenac topical, Celecoxib), antiplatelet/appetite agents (Acetylsalicylic acid, Dexfenfluramine, Fenfluramine, Sibutramine), Aminocaproic acid, and Omega-3 fatty acids — consistent with tenecteplase's known bleeding-risk profile as a thrombolytic agent.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (posteroinferior MI) has zero supporting clinical trials or literature, and the evidence pack's own analysis attributes the high TxGNN score to disease-ontology granularity rather than a distinct mechanistic finding — it is effectively re-stating tenecteplase's known STEMI indication under a more granular anatomical label. The drug is also not currently registered in India, and core safety data (label warnings/contraindications) is blocked pending retrieval.

**To proceed, the following is needed:**
- TFDA/India product label (warnings, contraindications) — Blocking gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank — High-priority gap (DG002)
- Clarification of whether "posteroinferior MI" should be evaluated as a distinct research question or merged with the existing STEMI indication in the ontology
- If pursuing a genuinely actionable signal from this pack, prioritize the **coronary stenosis / intracoronary adjunctive tenecteplase during PCI** candidate (L2, completed Phase 2 RCT) over the anatomical MI-subtype predictions
- India regulatory pathway assessment, given the drug currently has no local registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

