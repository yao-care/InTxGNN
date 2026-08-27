---
layout: default
title: Glycine
parent: 僅模型預測 (L5)
nav_order: 317
evidence_level: L5
indication_count: 2
---

# Glycine
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

# Glycine: From No Approved Indication in Taiwan to Nasal Cavity Disease

## One-Sentence Summary

Glycine (DrugBank DB00145) currently holds **no approved indication or marketing authorization in Taiwan** (0 licenses on file). The TxGNN model predicts a possible association with **Nasal Cavity Disease**, with a prediction score of **99.85%**, but this is currently supported by only **1 clinical trial** and **2 publications**, none of which directly evaluate Glycine for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on record (drug not marketed in Taiwan) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Glycine is not available in DrugBank (flagged as a High-severity data gap). Based on the information available in this evidence pack, Glycine is described as an inhibitory neurotransmitter and immunomodulatory amino acid, and the repurposing rationale suggests it could theoretically exert an anti-inflammatory effect on mucosal tissue — which is the proposed link to nasal cavity disease. However, this link is described in the evidence pack itself as a **knowledge-graph-derived association**, not a drug-specific mechanistic finding.

Glycine has no recorded original indication in this dataset (empty `original_indications`, and the drug is not marketed in Taiwan), so no meaningful comparison can be made between an established use and the newly predicted indication. Without an anchoring original indication, the biological plausibility of the prediction rests entirely on the TxGNN knowledge graph's associative scoring rather than on demonstrated pharmacology.

The single clinical trial and two literature records retrieved do not evaluate Glycine itself: the trial is a PET imaging biomarker study unrelated to Glycine (relevance graded "C" — low), and the two publications are basic-science/preclinical papers on unrelated topics (bovine nasal mucosa histochemistry; mucosal vaccine adjuvants) that happen to mention the nasal cavity. As such, mechanistic applicability to nasal cavity disease cannot currently be substantiated beyond the model's associative prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Phase 1/2 | Completed | 25 | Evaluated the PET radiopharmaceutical 18F-FPPRGD2 for imaging αvβ3 integrin expression (angiogenesis biomarker) in glioblastoma, gynecological cancer, and renal cell carcinoma patients. **Not a Glycine trial** — relevance to nasal cavity disease graded "C" (low); the association appears incidental (imaging agent/anatomic region), not therapeutic. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | Preclinical/Experimental | Chemical & Pharmaceutical Bulletin | Investigated oligoarginine-conjugated polymers as nasal mucosal vaccine adjuvants for inducing systemic IgG/mucosal IgA in mice. No evaluation of Glycine. |
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | Basic Science (Histochemistry) | Veterinary Pathology | Lectin histochemistry study of glycoconjugate composition in normal vs. herpesvirus-infected bovine nasal mucosa. No evaluation of Glycine. |

---

## India Market Information

Glycine is **not currently marketed** in Taiwan, and no product registrations are on file (0 licenses). No authorization, product name, dosage form, or approved-indication data exists in the regulatory record to report.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available for this candidate; a Taiwan FDA label review is flagged as a **Blocking** data gap and would be required before any safety pre-assessment.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 — this indication association is derived solely from the TxGNN model, without any clinical trial or literature evidence that directly studies Glycine in nasal cavity disease. The one available trial and two publications are tangential (different drug/agent, unrelated study focus) and do not establish mechanistic or clinical plausibility.

**To proceed, the following is needed:**
- Taiwan FDA package insert data (warnings/contraindications) — currently a **Blocking** gap preventing any safety pre-assessment
- Confirmed mechanism of action (MOA) data from DrugBank — currently a **High**-severity gap affecting mechanistic-relevance analysis
- Drug-specific clinical or preclinical studies evaluating Glycine (or a defined dose/route) in nasal cavity disease or related mucosal conditions
- Clarification of Glycine's regulatory/marketing status, since it currently has no approved indication or license record to serve as a baseline for repurposing comparison
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

