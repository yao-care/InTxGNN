---
layout: default
title: Lorlatinib
parent: 僅模型預測 (L5)
nav_order: 299
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

# Lorlatinib: From ALK-Positive Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Lorlatinib is a third-generation, brain-penetrant ALK/ROS1 tyrosine kinase inhibitor (TKI) with established efficacy in ALK-positive non-small cell lung cancer (NSCLC), as demonstrated by the landmark Phase 3 CROWN study.
The TxGNN model predicts it may be effective for **Fibromatosis, Gingival**, with **0 clinical trials** and **0 publications** currently supporting this direction.
The prediction score is high (99.81%), but mechanistic plausibility is low and the overall evidence grade is L5 — model prediction only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive non-small cell lung cancer (NSCLC) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Lorlatinib is a third-generation ALK/ROS1 tyrosine kinase inhibitor with exceptional blood-brain barrier penetrance. Its efficacy in ALK-positive NSCLC has been established by the CROWN Phase 3 trial published in the *New England Journal of Medicine* (2020), demonstrating superior progression-free survival versus crizotinib. It is also active against ROS1-rearranged NSCLC and ALK-driven neuroblastoma.

Gingival fibromatosis is a benign fibrous proliferative lesion of the gums, caused by gain-of-function mutations in *SOS1* (sporadic) or *FAM20A* genes. The pathogenesis is driven entirely by structural protein and signalling scaffold dysfunction — there is no known biological intersection between the ALK/ROS1 kinase axis and fibroblast proliferation in gingival tissue. Lorlatinib's mechanism has no recognised therapeutic rationale for this condition.

The TxGNN model's high prediction score most likely originates from shared knowledge graph nodes between "fibrous proliferation" and "mesenchymal/stromal tumour" entities, creating a spurious cross-indication signal. This is a recognised limitation of graph-based AI prediction when applied to benign, non-kinase-driven hereditary conditions. No preclinical, translational, or clinical evidence supports this repurposing direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Lorlatinib is not currently registered or marketed in India. No regulatory authorisation records are on file (total licences: 0).

---

## Cytotoxicity

Lorlatinib is an antineoplastic targeted therapy for ALK-positive malignancies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — 3rd-generation ALK/ROS1 tyrosine kinase inhibitor |
| Myelosuppression Risk | Low (myelosuppression is not a characteristic toxicity of ALK TKIs; anaemia occasionally reported) |
| Emetogenicity Classification | Low |
| Monitoring Items | Lipid panel (hypercholesterolaemia and hypertriglyceridaemia are common class effects), CBC, liver function tests, renal function, CNS adverse events (mood changes, cognitive effects, hallucinations), body weight, blood glucose |
| Handling Protection | Standard oral antineoplastic handling precautions required; follow institutional cytotoxic drug handling regulations |

---

## Safety Considerations

**Drug Interactions**: Lorlatinib has 461 documented drug interactions. Clinically significant interactions include:

| Severity | Interacting Drug(s) |
|----------|---------------------|
| **Major** | Dexamethasone, Clarithromycin |
| **Moderate** (selected) | Hydrocortisone, Betamethasone, Triamcinolone, Bupropion, Aprepitant, Morphine, Cimetidine, Dapagliflozin, Empagliflozin, Saxagliptin, Linagliptin, Glimepiride, Chlorpropamide, Naloxegol, Naldemedine, Dronabinol, Eliglustat, Alosetron |

> Full package insert warnings and contraindications were not available in this evidence pack. Please refer to the approved prescribing information for complete safety guidance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Gingival fibromatosis is a benign hereditary condition driven by structural gene mutations (*SOS1* / *FAM20A*) that have no known interaction with the ALK/ROS1 signalling axis targeted by lorlatinib. The TxGNN high-score prediction is most likely a knowledge graph artefact rather than a true mechanistic signal, and zero clinical or preclinical evidence supports this repurposing direction.

**To proceed, the following is needed:**
- Preclinical evidence establishing ALK or ROS1 pathway involvement in gingival fibromatosis (prerequisite for any further evaluation)
- Detailed MOA data for lorlatinib (retrieve via DrugBank API — currently a high-severity data gap)
- Official package insert warnings and contraindications (currently a blocking data gap; retrieve from CDSCO / approved prescribing information)
- India regulatory pathway feasibility assessment (drug is currently not marketed; new drug application would be required)

---

> ⚠️ **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All content should be reviewed by qualified medical and regulatory professionals.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

