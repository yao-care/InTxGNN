---
layout: default
title: Quinidine
parent: 僅模型預測 (L5)
nav_order: 710
evidence_level: L5
indication_count: 1
---

# Quinidine
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

# Quinidine: From Cardiac Arrhythmia to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Quinidine is a Class Ia antiarrhythmic, classically used to treat cardiac arrhythmias by blocking cardiac sodium channels (Nav1.5) and inhibiting CYP2D6/CYP3A4.
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-generated hypothesis only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cardiac arrhythmia (Class Ia antiarrhythmic); official label text not available (data gap) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.27% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Quinidine is not available in this evidence pack (marked as a data gap). Based on known pharmacology, Quinidine is a Class Ia antiarrhythmic whose primary mechanism is blockade of the cardiac sodium channel (Nav1.5), with secondary inhibition of CYP2D6 and CYP3A4. It is also used off-label in Andersen-Tawil syndrome, a channelopathy involving the Kir2.1 potassium channel.

NSIAD, by contrast, is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2), leading to constitutive receptor activation independent of circulating vasopressin. There is no established pharmacological or mechanistic pathway connecting Nav1.5 sodium channel blockade or CYP enzyme inhibition to AVPR2 signaling.

This prediction therefore appears to rest solely on TxGNN's knowledge-graph embedding similarity (rank 11,396 among candidates) rather than any known or plausible mechanistic link. Without a biological rationale and with no supporting trials or literature, this candidate should be treated as an early-stage, low-confidence hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Quinidine currently has no marketing authorization registered in Taiwan (0 licenses on file); market status is 未上市 (Not Marketed).

## Safety Considerations

- **Drug Interactions**: A drug interaction query returned 345 total interactions for Quinidine. Notable **Major**-level interactions identified include Loperamide, Clarithromycin, Picosulfuric acid, Polyethylene glycol (3350 with electrolytes), Dolasetron, Eliglustat, and Palonosetron. Additional **Moderate**-level interactions include Famotidine, Ranitidine, Metformin, Aprepitant, Acetylsalicylic acid, Cimetidine, and several others.

Detailed warnings and contraindications are not yet available — please refer to the package insert once obtained.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no supporting clinical trials or literature (Evidence Level L5, decision stage S0), and the proposed mechanistic link between Quinidine's known pharmacology and NSIAD's AVPR2-driven pathology is not established. Quinidine is also not currently marketed in Taiwan, and TFDA label warnings/contraindications (flagged as a **Blocking** data gap, DG001) are missing, preventing any safety pre-assessment.

**To proceed, the following is needed:**
- TFDA package insert/label data (warnings and contraindications) — required to clear the safety pre-assessment gate (DG001)
- Confirmed mechanism of action data from DrugBank (DG002), specifically any evidence of AVPR2 pathway interaction
- Preclinical or mechanistic studies exploring Quinidine's effect on vasopressin V2 receptor signaling
- Ongoing monitoring for emerging clinical trials or case reports in NSIAD before reconsidering this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

