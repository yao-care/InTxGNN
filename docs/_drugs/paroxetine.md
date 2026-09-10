---
layout: default
title: Paroxetine
parent: 僅模型預測 (L5)
nav_order: 642
evidence_level: L5
indication_count: 1
---

# Paroxetine
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

# Paroxetine: From Unrecorded Original Indication to Ohdo Syndrome and Variants

## One-Sentence Summary

Paroxetine is an SSRI-class antidepressant (per the evidence pack's mechanistic notes), though its specific original approved indication and mechanism of action are not recorded in this evidence pack. The TxGNN model predicts a possible link to **Ohdo Syndrome and Variants**, a rare congenital malformation syndrome, but this prediction is currently supported by **0 clinical trials** and **0 publications** — model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (data gap) |
| Predicted New Indication | Ohdo Syndrome and Variants |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why Is This Prediction Reasonable?

Detailed mechanism of action data for paroxetine is not available in this evidence pack ([Data Gap]). Based on the information present, paroxetine is described as an SSRI-class antidepressant, acting primarily via inhibition of presynaptic serotonin reuptake (SERT inhibition).

Ohdo syndrome and its variants are a group of rare congenital multiple-malformation disorders caused by germline mutations in chromatin-modifying/transcriptional-regulation genes (e.g., *KAT6B*, *KAT6A*, *MED12*, *DDX3X*), which disrupt craniofacial and skeletal development during embryogenesis. There is no established pharmacological or mechanistic pathway connecting SSRI activity to these developmental gene pathways.

Given the absence of a plausible mechanistic link and the absence of any supporting clinical or literature evidence, this candidate should be treated as a high-scoring but mechanistically unsupported TxGNN association — potentially a false positive arising from graph-topology proximity rather than genuine biological relevance.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

**Drug Interactions**: The evidence pack records 327 total documented interactions for paroxetine. Notable examples include:

| Interacting Drug | Severity |
|---|---|
| Bupropion | Major |
| Lorcaserin | Major |
| Diethylpropion | Major |
| Dolasetron | Major |
| Eliglustat | Major |
| Palonosetron | Major |
| Phentermine | Major |
| Morphine | Moderate |
| Acetylsalicylic acid | Moderate |
| Clarithromycin | Moderate |
| Cimetidine | Moderate |
| Chlorpropamide | Moderate |
| Glimepiride | Moderate |
| Repaglinide | Moderate |
| Dronabinol | Moderate |
| Eluxadoline | Moderate |
| Picosulfuric acid | Moderate |
| Polyethylene glycol (3350 w/ electrolytes) | Moderate |
| Sodium sulfate | Moderate |
| Aprepitant | Minor |

TFDA label warnings and contraindications are not currently available in this evidence pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking-severity data gap (TFDA label warnings/contraindications unavailable) prevents this candidate from clearing the S1 safety screening stage. Independently, the predicted indication itself has no supporting clinical trials or literature (L5 — prediction only) and no plausible mechanistic rationale connecting SSRI pharmacology to a chromatin-regulation congenital malformation syndrome. Paroxetine is also not currently marketed in Taiwan (0 registrations).

**To proceed, the following is needed:**
- TFDA product label (PDF) parsed for warnings/contraindications (DG001)
- DrugBank MOA data to properly assess mechanistic plausibility (DG002)
- Independent expert review of the mechanistic rationale before any further evidence collection is commissioned for this drug–indication pair
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

