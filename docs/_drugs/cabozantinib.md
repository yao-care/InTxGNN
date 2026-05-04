---
layout: default
title: Cabozantinib
parent: 僅模型預測 (L5)
nav_order: 129
evidence_level: L5
indication_count: 10
---

# Cabozantinib
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

# Cabozantinib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Cabozantinib is a multi-target tyrosine kinase inhibitor (TKI) approved internationally for renal cell carcinoma, medullary thyroid cancer, and hepatocellular carcinoma, acting primarily through simultaneous inhibition of VEGFR2, MET, and AXL signaling pathways.
The TxGNN model predicts it may be effective for **Liposarcoma**, with **1 clinical trial** and **1 publication** currently supporting this direction.
Evidence remains early-stage and is drawn from broad soft tissue sarcoma populations rather than liposarcoma-specific cohorts.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Renal cell carcinoma (global approval; no registration in India) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L3 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Cabozantinib is a multi-target tyrosine kinase inhibitor that simultaneously inhibits VEGFR2, MET, and AXL — three kinases deeply involved in tumor angiogenesis, stromal remodeling, and immune evasion. Its efficacy against renal cell carcinoma and medullary thyroid cancer has been established through multiple pivotal Phase 3 trials (METEOR, CheckMate 9ER), confirming that blocking these three axes together provides meaningful clinical benefit in solid tumors driven by vascular and mesenchymal signaling.

Liposarcoma, particularly dedifferentiated and myxoid/round-cell subtypes, is characterized by VEGFR-dependent neovascularization and documented MET overactivation. The dual VEGFR2 + MET blockade by cabozantinib may suppress both angiogenic supply and MET-driven stromal interactions that support liposarcoma survival and metastasis. Although MDM2 amplification — a hallmark genomic driver of well-differentiated and dedifferentiated liposarcoma — is not a direct cabozantinib target, inhibition of AXL may enhance the tumor microenvironment's susceptibility to immune checkpoint therapy, which is precisely the rationale behind the ongoing combination trial with ipilimumab and nivolumab (NCT05836571).

It is important to emphasize that liposarcoma is a heterogeneous disease across four major subtypes, and the mechanistic plausibility of cabozantinib likely varies by subtype. Dedicated liposarcoma-specific efficacy data are currently absent; all available evidence is extrapolated from the broader soft tissue sarcoma population.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | Active, Not Recruiting | 66 | Randomized comparison of cabozantinib + ipilimumab + nivolumab versus ipilimumab + nivolumab alone in advanced soft tissue sarcoma. Liposarcoma is included as a subtype but without dedicated stratification; efficacy results in the liposarcoma subgroup have not yet been published. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 | American Journal of Clinical Oncology | Phase 1 neoadjuvant study evaluating concurrent cabozantinib + radiation therapy in extremity soft tissue sarcoma (including liposarcoma subtypes). Primary objective was safety assessment, specifically addressing concerns about fistula and perforation risk associated with combining cabozantinib with RT. No dedicated liposarcoma efficacy data reported. |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Multi-target tyrosine kinase inhibitor (VEGFR / MET / AXL) |
| Myelosuppression Risk | Low to moderate (thrombocytopenia and neutropenia reported in Phase 3 trials; substantially less severe than conventional cytotoxic agents) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function tests (ALT/AST/bilirubin), renal function (serum creatinine), thyroid function (TSH), blood pressure, urinalysis for proteinuria, wound healing assessment |
| Handling Protection | Standard oral targeted therapy precautions apply; dedicated cytotoxic handling protocols are not required — tablets should not be crushed or dissolved, and caregivers should avoid contact with broken tablets |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The current evidence base for cabozantinib in liposarcoma consists of a single ongoing Phase 2 trial in the broader soft tissue sarcoma population (with no liposarcoma-specific subgroup analysis published) and one Phase 1 safety study; this L3 evidence level is insufficient to support clinical adoption or regulatory exploration without dedicated efficacy data in liposarcoma.

**To proceed, the following is needed:**

- Retrieve mechanism of action (MOA) data from DrugBank API or prescribing information (resolves DG002)
- Retrieve CDSCO/regulatory package insert for key warnings and contraindications (resolves DG001 — currently blocking S1 safety evaluation)
- Await published results from NCT05836571, specifically requesting liposarcoma subgroup analysis from investigators
- Identify or initiate a dedicated Phase 2 basket trial in liposarcoma with cabozantinib, stratified by histological subtype (particularly dedifferentiated liposarcoma given MDM2 amplification)
- Review retrospective real-world data from sarcoma centers for any off-label cabozantinib use in liposarcoma
- Consider CDSCO import/named-patient use pathway if a specific patient case warrants compassionate use, given the drug is not currently registered in India
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

