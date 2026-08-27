---
layout: default
title: Glatiramer
parent: 僅模型預測 (L5)
nav_order: 312
evidence_level: L5
indication_count: 10
---

# Glatiramer
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

# Glatiramer: From Multiple Sclerosis to Hemoglobinopathy

## One-Sentence Summary

> Glatiramer acetate is a synthetic polypeptide immunomodulator best known as a first-line disease-modifying therapy for relapsing-remitting multiple sclerosis. The TxGNN model assigns a high raw score to **Hemoglobinopathy** as a potential new indication, but this signal is currently backed by **0 clinical trials** and only **1 loosely related publication** that does not actually discuss glatiramer's use in hemoglobinopathy — indicating the prediction is not yet supported by real-world evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Sclerosis (relapsing-remitting) — inferred from literature context; no India/Taiwan label text available (drug not marketed) |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for glatiramer is not available in the evidence pack (flagged as a High-severity data gap, DG002). Based on generally known pharmacology, glatiramer acetate is believed to act by shifting T-cell responses away from a pro-inflammatory Th1 profile toward an anti-inflammatory Th2/regulatory profile, reducing autoimmune attack on CNS myelin in multiple sclerosis.

Hemoglobinopathies (e.g., thalassemias, sickle cell disease) are structural or synthesis defects of the hemoglobin gene — a fundamentally different disease category rooted in genetic/hematologic pathology rather than autoimmune CNS inflammation. There is no established biological pathway linking glatiramer's peripheral T-cell immunomodulatory activity to hemoglobin gene expression or red blood cell structure/function.

The single literature record returned for this pairing (PMID 28372806) does not actually support the prediction: it describes immune disorders arising after **natalizumab** discontinuation — a different MS drug — in a patient whose medical history happened to include beta-thalassemia. The overlap appears to be an incidental keyword match (the patient's past history) rather than evidence of a therapeutic relationship between glatiramer and hemoglobinopathy. This is consistent with the evidence pack's own assessment that no plausible mechanistic link exists between the two.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28372806](https://pubmed.ncbi.nlm.nih.gov/28372806/) | 2017 | Case Report | Revue neurologique | Describes multiple immune disorders following **natalizumab** (not glatiramer) discontinuation in an MS patient with a prior history of beta-thalassemia, bulimia, and asthma. Does not evaluate glatiramer's efficacy in hemoglobinopathy; the connection to this indication appears coincidental. |

---

## Safety Considerations

- **Drug Interactions**: Major interaction identified between **Glatiramer** and **Natalizumab** (source: DDInter). Co-administration should be evaluated carefully if both agents are considered in an MS treatment context.

*Detailed label warnings and contraindications for glatiramer could not be retrieved (TFDA label data is a Blocking-severity gap — see Next Steps).*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted association between glatiramer and hemoglobinopathy lacks a plausible biological mechanism, has zero clinical trial support, and its sole literature citation does not actually address this drug-disease pairing — it is most likely a spurious match driven by an unrelated patient history detail. Combined with glatiramer's absence from the India/Taiwan market (0 registrations), there is currently no basis to advance this candidate beyond exploratory screening.

**To proceed, the following is needed:**
- TFDA/local regulatory label data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action (MOA) from DrugBank or primary literature — currently a High-severity data gap (DG002)
- A biologically plausible hypothesis (e.g., via a specific molecular pathway) connecting T-cell immunomodulation to hemoglobin synthesis/structure, before further evidence collection is warranted
- If this candidate is deprioritized, evaluation resources may be better directed at other ranked predictions in this evidence pack (e.g., female breast carcinoma, rank 3) — though note those are also currently supported only by cancer-risk/safety-monitoring studies in MS patients, not efficacy data, and were independently scored "Hold" as well.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

