---
layout: default
title: Vincristine
parent: 僅模型預測 (L5)
nav_order: 882
evidence_level: L5
indication_count: 3
---

# Vincristine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Vincristine: From Established Oncology Indications to Ganglioneuroblastoma

## One-Sentence Summary

> Vincristine is a vinca-alkaloid chemotherapeutic agent widely used in combination regimens for pediatric and hematologic malignancies (specific original-indication text and MOA are not present in this evidence pack).
> The TxGNN model predicts it may be effective for **Ganglioneuroblastoma**,
> with **4 clinical trials** and **6 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no India regulatory license records are on file for this drug in the evidence pack |
| Predicted New Indication | Ganglioneuroblastoma |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on general pharmacological knowledge, vincristine is a vinca-alkaloid that binds tubulin and inhibits microtubule assembly, arresting cell division in mitosis. It is a long-standing component of combination chemotherapy regimens (e.g., VAC, CYVADIC, VCR-based induction) for a range of pediatric and hematologic malignancies.

Ganglioneuroblastoma is a neuroblastic tumor closely related biologically to neuroblastoma, and the evidence pack itself demonstrates that vincristine is already routinely used within multi-agent chemotherapy regimens for this tumor family. One literature entry (PMID 8255850) directly documents a spinal ganglioneuroblastoma achieving complete remission with a vincristine-containing regimen, and the Phase 3 trial NCT03126916 explicitly enrolls "high-risk neuroblastoma or ganglioneuroblastoma." This existing real-world use pattern, rather than a novel biological hypothesis, is the primary support for the TxGNN prediction's plausibility.

Because no original-indication text or DrugBank MOA data were retrievable in this pack, a formal mechanistic-similarity comparison between the original and predicted indications cannot yet be completed — this should be closed out with DrugBank/label data before final sign-off.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01798004](https://clinicaltrials.gov/study/NCT01798004) | Phase 1 | Completed | 150 | Busulfan/melphalan myeloablative consolidation after induction chemotherapy in newly diagnosed high-risk neuroblastoma |
| [NCT06172296](https://clinicaltrials.gov/study/NCT06172296) | Phase 3 | Recruiting | 478 | Dinutuximab added to intensive multimodal therapy (induction chemo, surgery, radiation, transplant, immunotherapy) in newly diagnosed high-risk neuroblastoma |
| [NCT03126916](https://clinicaltrials.gov/study/NCT03126916) | Phase 3 | Recruiting | 750 | 131I-MIBG or ALK inhibitor (lorlatinib) added to standard therapy in newly diagnosed high-risk neuroblastoma **or ganglioneuroblastoma** |
| [NCT03786783](https://clinicaltrials.gov/study/NCT03786783) | Phase 2 | Active, not recruiting | 42 | Pilot induction regimen with dinutuximab + sargramostim combined with chemotherapy in newly diagnosed high-risk neuroblastoma |

*Note: these trials primarily target the broader "high-risk neuroblastoma" spectrum; only NCT03126916 explicitly names ganglioneuroblastoma as an eligible diagnosis.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8255850](https://pubmed.ncbi.nlm.nih.gov/8255850/) | 1993 | Case report | Postgraduate Medical Journal | Unresectable spinal ganglioneuroblastoma achieved histologically confirmed complete remission with vincristine-containing combination chemotherapy (doxorubicin, cyclophosphamide, etoposide, ifosfamide, cisplatin) alone, without surgery or radiotherapy |
| [7421294](https://pubmed.ncbi.nlm.nih.gov/7421294/) | 1980 | Case series | J Thorac Cardiovasc Surg | 31 patients with intrathoracic ganglioneuroblastoma treated with resection, radiation, and/or chemotherapy; long-term follow-up up to 25 years |
| [31342649](https://pubmed.ncbi.nlm.nih.gov/31342649/) | 2019 | Prospective clinical trial | Pediatric Blood & Cancer | Image-defined risk factors used to guide timing of surgical resection in low-risk neuroblastoma, reducing treatment-related complications |
| [15701990](https://pubmed.ncbi.nlm.nih.gov/15701990/) | 2005 | Case report | J Pediatr Hematol Oncol | Ganglioneuroblastoma presenting with obstructive jaundice, a rare initial feature of neuroblastic tumors |
| [8888754](https://pubmed.ncbi.nlm.nih.gov/8888754/) | 1996 | Case report | J Pediatr Hematol Oncol | Stage 4 multifocal ganglioneuroblastoma with rare gastric involvement in an infant |
| [3071124](https://pubmed.ncbi.nlm.nih.gov/3071124/) | 1988 | Case report | Hinyokika Kiyo | Multimodality treatment of adrenal ganglioneuroblastoma with giant regional lymph node metastasis |

---

## India Market Information

Vincristine is currently **not marketed** in India according to the regulatory data in this evidence pack — no license or registration entries are on file (`total_licenses: 0`). No product-level table can be generated until India regulatory records are obtained.

---

## Cytotoxicity

Vincristine is a conventional cytotoxic chemotherapy agent (vinca alkaloid class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Vinca alkaloid, microtubule/mitotic inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Must follow standard cytotoxic/hazardous drug handling regulations |

---

## Safety Considerations

**Drug Interactions**: DDI screening identified **505 total interactions**. Notable examples include:
- **Major**: Clarithromycin
- **Moderate**: Aprepitant, Dexamethasone, Metronidazole, Eliglustat, Naltrexone, Glycerol phenylbutyrate, Miconazole, Rolapitant, Rosuvastatin, Simvastatin, Tinidazole, Troglitazone
- **Minor**: Levofloxacin
- **Unknown severity** (requires further review): Calcitriol, Pantoprazole, Clotrimazole, Morphine, Metformin, Omeprazole

Package-insert-level warnings and contraindications are not yet available in this evidence pack (flagged as a blocking data gap — see below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap exists — India/local product-label warnings and contraindications are not yet available, which prevents this candidate from entering the S1 safety pre-assessment stage. While the TxGNN score is high (99.31%) and existing literature/trials show vincristine is already used within combination regimens for neuroblastoma-spectrum tumors including ganglioneuroblastoma, no completed Phase 2/3 RCT specifically evaluates vincristine for ganglioneuroblastoma, and original indication/MOA data are also missing.

**To proceed, the following is needed:**
- India product label / TFDA-equivalent warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action from DrugBank API (DG002, High)
- Confirmed original indication list for the drug
- Route compatibility assessment (currently pending, not yet evaluated)
- Clarification of whether trial results for "high-risk neuroblastoma" (broad) can be reasonably extrapolated to ganglioneuroblastoma specifically, or whether ganglioneuroblastoma-specific outcome data is required
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

