---
layout: default
title: Panitumumab
parent: 僅模型預測 (L5)
nav_order: 635
evidence_level: L5
indication_count: 2
---

# Panitumumab
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

# Panitumumab: From Metastatic Colorectal Cancer to Drug-Induced Osteoporosis

## One-Sentence Summary

Panitumumab is a fully human IgG2 monoclonal antibody targeting EGFR, originally used for metastatic colorectal cancer. The TxGNN model predicts it may be effective for **drug-induced osteoporosis** (score 99.13%), but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests on the model score alone. A second candidate, severe nonproliferative diabetic retinopathy (score 99.05%), is similarly unsupported by any trial or literature evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic colorectal cancer (per model rationale; not independently confirmed — original_moa/indication fields are data gaps) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.13% |
| Evidence Level | L5 (model prediction only, no trials or literature) |
| India Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for panitumumab is not directly available in the drug record (flagged as a data gap). Based on the rationale accompanying the prediction, panitumumab is described as a fully human IgG2 monoclonal antibody that blocks EGFR ligand binding to inhibit tumour cell proliferation, used in metastatic colorectal cancer.

For the top-ranked prediction — drug-induced osteoporosis — the proposed link relies on literature suggesting EGFR signalling has *some* regulatory role in osteoblast/osteoclast differentiation. This is described explicitly as an indirect, speculative pathway connection rather than a demonstrated pharmacological effect: there is no experimental or clinical data showing panitumumab affects bone density or contributes to (or protects against) drug-induced osteoporosis.

A second, lower-ranked candidate also emerged from the model — severe nonproliferative diabetic retinopathy (score 99.05%) — but the rationale for this one is weaker still: diabetic retinopathy is primarily driven by VEGF-mediated neovascularization and vascular permeability, not EGFR signalling, and known ocular adverse effects of anti-EGFR therapy (e.g., keratitis, eyelash abnormalities) are toxicities, not therapeutic mechanisms. The mismatch between panitumumab's target (EGFR) and the disease's primary driver (VEGF) makes this candidate mechanistically implausible.

In both cases, the prediction score comes from the TxGNN model alone, with no corroborating trial, literature, or case-report evidence, and the underlying original MOA/indication data for panitumumab itself is incomplete in this evidence pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

Panitumumab is not currently marketed in Taiwan (market_status: 未上市) and holds no registered licenses (total_licenses: 0). No authorization records are available to list.

---

## Cytotoxicity

Panitumumab is an antineoplastic agent (anti-EGFR monoclonal antibody used in metastatic colorectal cancer, corroborated by major DDI flags with other oncology agents such as bevacizumab and irinotecan).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-EGFR monoclonal antibody, non-conventional cytotoxic) |
| Myelosuppression Risk | Low — anti-EGFR mAbs are not primarily myelosuppressive; hematologic toxicity is not the dominant safety concern for this class |
| Emetogenicity Classification | Low — monoclonal antibodies generally carry minimal emetogenic potential |
| Monitoring Items | Serum magnesium/electrolytes (EGFR-inhibitor–associated hypomagnesemia), skin toxicity, infusion-related reactions, renal function |
| Handling Protection | Please refer to the package insert warnings and precautions for specific handling requirements |

---

## Safety Considerations

**Drug Interactions**: DDI screening returned 27 total interactions (20 detailed below), notably including several **Major**-severity interactions relevant to oncology co-medication and QT-prolonging agents:

- **Major**: Amiodarone, Arsenic trioxide, Bevacizumab, Dofetilide, Dronedarone, Droperidol, Aminolevulinic acid, Irinotecan, Irinotecan (liposomal), Levacetylmethadol
- **Moderate**: Rabeprazole, Omeprazole, Dexlansoprazole, Esomeprazole, Lansoprazole, Pantoprazole, Methoxsalen, Aminolevulinic acid (topical), Disopyramide, Idelalisib

Key warnings and contraindications for panitumumab could not be assessed — TFDA label/warning data is a **blocking data gap (DG001)** and must be resolved before any safety evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications are supported only by the TxGNN model score (L5, no trials, no literature), and one (diabetic retinopathy) has a mechanistically implausible target mismatch (EGFR vs. VEGF). Combined with a blocking gap on TFDA safety/warning data and an unconfirmed original MOA, there is insufficient basis to advance either indication past initial screening.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (resolve DG001, currently blocking)
- Confirmed original mechanism of action and approved indication for panitumumab (resolve DG002)
- Preclinical or mechanistic studies specifically examining EGFR's role in bone metabolism (for the osteoporosis candidate) before further investment
- Given the target mismatch, deprioritize the diabetic retinopathy candidate unless new mechanistic evidence emerges
- Ongoing monitoring for new trials/publications on either indication, given the pure model-driven origin of both signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

