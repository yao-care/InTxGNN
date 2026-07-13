---
layout: default
title: Ivabradine
parent: 僅模型預測 (L5)
nav_order: 330
evidence_level: L5
indication_count: 6
---

# Ivabradine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Ivabradine: From Chronic Heart Failure to Hypertrichosis

## One-Sentence Summary

Ivabradine is a selective HCN channel (If current) blocker approved globally for chronic heart failure and chronic stable angina, reducing resting heart rate without affecting cardiac contractility.
The TxGNN model predicts it may be effective for **Hypertrichosis (excessive hair growth)**, however this is supported by **0 clinical trials** and **0 publications** — making this a low-confidence, model-only prediction.
The mechanistic rationale is considered a probable knowledge graph false positive, and independent biological validation would be required before this direction can be pursued.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic heart failure, chronic stable angina (not registered in India) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacology, Ivabradine selectively blocks the hyperpolarization-activated cyclic nucleotide-gated (HCN) channel — specifically the If ("funny") current in sinoatrial node pacemaker cells — thereby slowing heart rate in a dose-dependent manner without impairing myocardial contractility or conduction. This mechanism underpins its approved use in heart failure with reduced ejection fraction (HFrEF) and chronic stable angina.

The predicted link between Ivabradine and hypertrichosis is mechanistically weak. While HCN channels have minimal reported expression in hair follicle tissue, no direct causal evidence connects HCN channel blockade to hair growth regulation. The more likely explanation for this TxGNN prediction is an indirect knowledge graph topology artefact: Minoxidil — another cardiovascular drug (vasodilator) — is well known to cause hypertrichosis as a side effect, potentially placing cardiovascular drug nodes in close proximity to hypertrichosis nodes within the graph. This proximity-driven scoring represents graph noise rather than a true biological connection.

In summary, no mechanistic pathway linking Ivabradine's HCN channel blockade to hair follicle biology has been identified. This prediction is assessed as a probable false positive arising from knowledge graph topology, not from pharmacological plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

**Drug Interactions (138 total identified; top interactions listed below):**

| Interacting Drug | Severity | Source |
|------------------|----------|--------|
| Aprepitant | **Major** | DDInter |
| Clarithromycin | **Major** | DDInter |
| Cobicistat | **Major** | DDInter |
| Cisapride | **Major** | DDInter |
| Clotrimazole | **Major** | DDInter |
| Dolasetron | **Major** | DDInter |
| Granisetron | **Major** | DDInter |
| Levofloxacin | **Major** | DDInter |
| Ondansetron | **Major** | DDInter |
| Palonosetron | **Major** | DDInter |
| Papaverine | **Major** | DDInter |
| Famotidine | Moderate | DDInter |
| Ranitidine | Moderate | DDInter |
| Dexamethasone | Moderate | DDInter |
| Cimetidine | Moderate | DDInter |
| Miconazole | Moderate | DDInter |
| Nizatidine | Moderate | DDInter |
| Troglitazone | Moderate | DDInter |
| Metreleptin | Moderate | DDInter |
| Ranitidine (bismuth citrate) | Moderate | DDInter |

> Note: Package insert warnings and contraindications were not available in this evidence pack. Please refer to the official prescribing information for complete safety data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure model prediction (Evidence Level L5) with zero supporting clinical trials and zero supporting literature. The proposed mechanistic link between HCN channel blockade and hypertrichosis is biologically implausible and most likely represents a knowledge graph noise artefact driven by Minoxidil's proximity in the drug–disease network. Pursuing this candidate without any biological basis would not represent efficient use of research resources.

**To proceed, the following is needed:**
- **Mechanistic validation**: Confirm whether HCN channels play any role in hair follicle cycling or hair shaft growth, ideally through a targeted literature review and wet-lab feasibility assessment
- **KG path audit**: Trace the exact knowledge graph reasoning path to determine if the prediction is driven by Minoxidil–hypertrichosis proximity (graph noise) or a genuine Ivabradine-specific signal
- **MOA data**: Retrieve full DrugBank mechanistic data for Ivabradine (currently missing) to support rigorous target–indication matching
- **India regulatory data**: Download the TFDA/CDSCO package insert PDF to obtain approved indications, contraindications, and key warnings
- **Re-score after data gaps are closed**: Once DG001 (warnings/contraindications) and DG002 (MOA) are resolved, re-run the safety pre-screening before reconsidering this or other predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

