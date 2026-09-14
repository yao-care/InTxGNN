---
layout: default
title: Zafirlukast
parent: 僅模型預測 (L5)
nav_order: 892
evidence_level: L5
indication_count: 2
---

# Zafirlukast
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Zafirlukast: From Chronic Asthma to Bronchitis

## One-Sentence Summary

> Zafirlukast is a selective cysteinyl leukotriene (CysLT1) receptor antagonist, globally established for the prophylaxis and treatment of chronic asthma. The TxGNN model predicts it may be effective for **Bronchitis**, but this is currently supported by **0 clinical trials** and **0 publications** — the prediction rests entirely on knowledge-graph inference, not observed evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic asthma (prophylaxis and treatment) — established in global literature; not documented in India regulatory filings, as the drug is not marketed there |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured DrugBank field for this candidate (data gap DG002). Based on literature evidence collected in this pack, Zafirlukast is a competitive, selective antagonist of the cysteinyl leukotrienes LTC4, LTD4, and LTE4 at the CysLT1 receptor, producing bronchodilation and anti-inflammatory effects. Its efficacy in chronic asthma has been demonstrated in multiple placebo-controlled trials referenced in the evidence pack (e.g., PMID 9463793, 11270943, 9647606).

The TxGNN model's high score (99.93%) for bronchitis appears to be an extrapolation from this asthma-related anti-inflammatory/bronchodilator mechanism to other airway inflammatory conditions via knowledge-graph association, rather than a direct causal signal. However, the model-generated rationale itself flags an important caveat: acute and chronic bronchitis are predominantly driven by viral infection or smoking-related airway irritation, and a direct causal link between the CysLT1 pathway and bronchitis pathophysiology is not currently supported by evidence — the mechanistic connection is indirect.

Notably, a second, lower-ranked candidate in this evidence pack — **obstructive lung disease / COPD** (TxGNN score 99.17%) — has substantially stronger support: 20 literature citations, including a small randomized controlled trial specifically testing zafirlukast's bronchodilator effect in COPD patients (PMID 23741166) and a crossover trial in severe COPD (PMID 12877822). This suggests that if airway-disease repurposing is of interest, COPD may be a more evidence-backed direction than bronchitis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

Zafirlukast is **not currently marketed in India** — the regulatory database shows 0 registered licenses, so no authorization, product, or approved-indication records are available for this drug in this market.

---

## Safety Considerations

**Drug Interactions**: The evidence pack records **376 total documented interactions** for zafirlukast. Among the sampled entries provided:

| Interacting Drug | Severity |
|---|---|
| Aprepitant | Moderate |
| Acetylsalicylic acid | Moderate |
| Metronidazole | Moderate |
| Budesonide | Moderate |
| Budesonide (nasal) | Moderate |
| Saxagliptin | Moderate |
| Eliglustat | Moderate |
| Naltrexone | Moderate |
| Nateglinide | Moderate |
| Nitisinone | Moderate |
| Repaglinide | Moderate |
| Rosuvastatin | Moderate |
| Simvastatin | Moderate |
| Tinidazole | Moderate |
| Sibutramine | Minor |
| Pantoprazole | Unknown |
| Mesalazine | Unknown |
| Morphine | Unknown |
| Metformin | Unknown |
| Omeprazole | Unknown |

Notably, several Moderate-level interactions involve statins (rosuvastatin, simvastatin) and antidiabetic agents (saxagliptin, nateglinide, repaglinide) — relevant given zafirlukast's known CYP2C9 inhibition profile.

Key warnings and contraindications data (TFDA/India label-level information) are currently missing — this is flagged as a **Blocking** data gap (DG001) and must be resolved before any safety pre-screening (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction is supported only by a high TxGNN score (L5 — model prediction only), with zero clinical trials and zero literature directly connecting zafirlukast to bronchitis. The model's own rationale acknowledges the mechanistic link is indirect, since bronchitis etiology (viral/smoking-related) does not clearly map onto the CysLT1 pathway.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/India label warnings and contraindications before any S1 safety screening
- Resolve DG002: confirm formal MOA via DrugBank API query
- Direct preclinical or clinical evidence linking CysLT1 antagonism to bronchitis pathophysiology
- Consider evaluating **obstructive lung disease/COPD** instead — it scores nearly as high (99.17%) and already has 20 supporting publications, including an RCT and a crossover trial in COPD patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

