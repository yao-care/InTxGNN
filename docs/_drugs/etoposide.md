---
layout: default
title: Etoposide
parent: 僅模型預測 (L5)
nav_order: 328
evidence_level: L5
indication_count: 10
---

# Etoposide
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

# Etoposide: From Cytotoxic Chemotherapy to Well-Differentiated Fetal Adenocarcinoma of the Lung

## One-Sentence Summary

Etoposide is a topoisomerase II inhibitor long used as a cytotoxic chemotherapy backbone across multiple malignancies (e.g., small cell lung cancer, testicular cancer, lymphomas), though its Taiwan-specific approved indication text and detailed MOA data are not available in this evidence pack. The TxGNN model's top-ranked prediction is **Well-Differentiated Fetal Adenocarcinoma of the Lung**, a very rare pulmonary blastoma-spectrum tumor, but this is currently supported by only **0 clinical trials** and **1 case report**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack — no Taiwan license records exist; internationally Etoposide is a well-established chemotherapy agent for multiple cancers (e.g., SCLC, testicular cancer, lymphoma) |
| Predicted New Indication | Well-differentiated fetal adenocarcinoma of the lung |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information, Etoposide is a topoisomerase II inhibitor and conventional cytotoxic chemotherapy agent, part of the epipodophyllotoxin class, with proven efficacy across a range of highly proliferative and embryonal/epithelial malignancies.

Well-differentiated fetal adenocarcinoma of the lung is a rare epithelial component within the pulmonary blastoma spectrum, alongside classic biphasic pulmonary blastoma and pleuropulmonary blastoma. The mechanistic rationale extends from etoposide's cytotoxic activity against other highly proliferative embryonal/sarcomatoid lung tumor components, rather than from direct evidence specific to this exact histology.

The single supporting publication describes a related but distinct entity (classic biphasic pulmonary blastoma) treated with a different regimen (nedaplatin plus paclitaxel, not etoposide), making this an indirect line of evidence rather than a direct demonstration of efficacy for this specific tumor type.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33107372](https://pubmed.ncbi.nlm.nih.gov/33107372/) | 2020 | Case Report | The Journal of international medical research | Case report of classic biphasic pulmonary blastoma (a related entity to well-differentiated fetal adenocarcinoma) in a patient who underwent right upper lobe resection followed by nedaplatin plus paclitaxel adjuvant chemotherapy; does not directly evaluate etoposide in this indication |

---

## Taiwan Market Information

Etoposide is currently not marketed in Taiwan (0 registrations on file); no product license records are available in this evidence pack.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (topoisomerase II inhibitor / epipodophyllotoxin class) |
| Myelosuppression Risk | Not characterized in this evidence pack — please refer to the package insert warnings and precautions. As a general pharmacological reference, epipodophyllotoxin agents are typically associated with significant dose-limiting myelosuppression (neutropenia/thrombocytopenia) |
| Emetogenicity Classification | Not characterized in this evidence pack — please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function, blood pressure during infusion |
| Handling Protection | Cytotoxic drug handling precautions apply per standard oncology practice; institution-specific protocol should be confirmed once TFDA labeling is obtained |

---

## Safety Considerations

**Drug Interactions**: A total of 495 interactions were identified in the DDI query. Notable Moderate-level interactions include:
- Aprepitant
- Metronidazole
- Eliglustat
- Rolapitant
- Rosuvastatin
- Simvastatin
- Tinidazole

A Minor-level interaction was also identified with Levofloxacin. Several additional interactions (e.g., Calcitriol, Vitamin A, Doxycycline, Clotrimazole, Cimetidine, Amphotericin B) are recorded at an Unknown severity level and warrant individual review before combination use.

Key warnings and contraindications are currently unavailable (blocked pending TFDA label acquisition — see Conclusion below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction for Etoposide (well-differentiated fetal adenocarcinoma of the lung) is supported only by a single indirect case report and no registered clinical trials, placing it at evidence level L4/decision stage S1. Combined with the absence of Taiwan market authorization and TFDA labeling data, there is insufficient basis to advance this specific candidate at this time.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a Blocking data gap preventing safety pre-screening (DG001)
- Detailed mechanism of action data from DrugBank (High-severity gap, DG002)
- Dedicated case series, preclinical, or mechanism studies specific to well-differentiated fetal adenocarcinoma/pulmonary blastoma (rather than the related but distinct biphasic pulmonary blastoma entity)
- Taiwan regulatory pathway assessment, since Etoposide is currently unmarketed locally

**Additional note:** This evidence pack contains several other predicted indications for Etoposide with substantially stronger evidentiary support than the top-ranked candidate above — notably **Ewing sarcoma** (L1, Proceed with Guardrails) and **rhabdomyosarcoma** (L1, Proceed with Guardrails), both backed by multiple completed Phase 3 RCTs, and **primary pulmonary lymphoma** (L2, Proceed with Guardrails). If the goal is to identify the most defensible repurposing opportunity for Etoposide rather than strictly the highest TxGNN score, those candidates warrant priority review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

