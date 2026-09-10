---
layout: default
title: Cyclophosphamide
parent: 僅模型預測 (L5)
nav_order: 216
evidence_level: L5
indication_count: 5
---

# Cyclophosphamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Cyclophosphamide: From Broad-Spectrum Alkylating Chemotherapy to Myeloid Leukemia (AML) Transplant Conditioning / GVHD Prophylaxis

## One-Sentence Summary

Cyclophosphamide is a nitrogen mustard alkylating agent long used across a wide range of hematologic and solid malignancies, though this evidence pack does not include a specific original-indication label.
The TxGNN model predicts strong applicability to **myeloid leukemia**, and this direction is already substantiated by **50 clinical trials** and **20 publications**, most describing cyclophosphamide as a core component of allogeneic stem cell transplant conditioning and post-transplant GVHD prophylaxis regimens.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no license/label data supplied) |
| Predicted New Indication | Myeloid Leukemia (AML) |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L1 |
| India Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Cyclophosphamide is a nitrogen mustard alkylating agent that has been a chemotherapy backbone for decades; its cytotoxic and immunosuppressive efficacy across hematologic malignancies and autoimmune conditions is well established, and mechanistically this activity extends naturally to myeloid leukemia treatment settings.

Specifically, the evidence assembled here shows Cyclophosphamide functioning in two closely related roles for AML: (1) as part of myeloablative **conditioning regimens** (e.g., Busulfan/Cyclophosphamide, "Bu/Cy") prior to allogeneic hematopoietic stem cell transplantation, and (2) as **post-transplant cyclophosphamide (PTCy)**, a now-standard strategy for graft-versus-host disease (GVHD) prophylaxis that works by selectively depleting alloreactive T-cells after transplantation. Both applications rely on the same core alkylating/immunomodulatory mechanism.

Because these uses are supported by multiple completed Phase 2/3 randomized and large cohort studies, the TxGNN prediction is best understood as confirming an already-established clinical practice pattern rather than proposing a wholly novel use — which strengthens rather than weakens the credibility of the model's output.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02744742](https://clinicaltrials.gov/study/NCT02744742) | Phase 2/3 | Completed | 202 | RCT comparing G-CSF+Decitabine+Busulfan+Cyclophosphamide vs Busulfan+Cyclophosphamide conditioning for RAEB-1/2 and AML secondary to MDS undergoing allo-HSCT. |
| [NCT00723099](https://clinicaltrials.gov/study/NCT00723099) | Phase 2 | Completed | 73 | Umbilical cord blood transplant with reduced-intensity cyclophosphamide/fludarabine/TBI preparative regimen for hematologic malignancies. |
| [NCT03959241](https://clinicaltrials.gov/study/NCT03959241) | Phase 3 | Completed | 431 | BMT CTN 1703 — randomized comparison of Tacrolimus/Methotrexate vs PTCy/Tacrolimus/Mycophenolate for GVHD prophylaxis after reduced-intensity allo-PBSCT. |
| [NCT02999854](https://clinicaltrials.gov/study/NCT02999854) | Phase 3 | Terminated | 63 | Randomized comparison of ATIR101 (T-cell depleted) vs haploidentical HSCT with post-transplant high-dose Cyclophosphamide (PTCy) for hematologic malignancy. |
| [NCT00186823](https://clinicaltrials.gov/study/NCT00186823) | Phase 3 | Completed | 57 | Haploidentical transplant using purified CD34+ cells for high-risk hematologic malignancies. |
| [NCT02665065](https://clinicaltrials.gov/study/NCT02665065) | Phase 3 | Active, not recruiting | 153 | Pivotal study of Iomab-B plus reduced-intensity conditioning vs conventional care in older patients with active/relapsed/refractory AML. |
| [NCT01010217](https://clinicaltrials.gov/study/NCT01010217) | Phase 2 | Completed | 176 | Three-arm trial (haploidentical, mismatched related/unrelated, matched unrelated donor) using T-cell replete allograft with high-dose post-transplant Cyclophosphamide. |
| [NCT00134017](https://clinicaltrials.gov/study/NCT00134017) | Phase 2 | Completed | 142 | HLA-matched related/unrelated BMT using Busulfan/Cyclophosphamide conditioning plus post-transplant Cyclophosphamide for hematologic malignancies. |
| [NCT00342316](https://clinicaltrials.gov/study/NCT00342316) | N/A | Completed | 340 | Prospective controlled study of reduced-intensity allo-SCT vs best standard chemotherapy care for AML in first complete remission. |
| [NCT07249346](https://clinicaltrials.gov/study/NCT07249346) | Phase 2 | Recruiting | 124 | Dose-expansion study of low-dose post-transplant Cyclophosphamide/Tacrolimus/Ruxolitinib for GVHD prophylaxis in myeloablative allogeneic PBSCT. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | Review | Int J Mol Sci | Reviews post-transplant Cyclophosphamide (PTCy) as GVHD prophylaxis in matched sibling/unrelated donor HSCT for pediatric AML. |
| [39939431](https://pubmed.ncbi.nlm.nih.gov/39939431/) | 2025 | Registry Cohort | Bone Marrow Transplant | EBMT registry study (n=1823) analyzing cytogenetic/molecular risk-driven conditioning intensity in AML patients receiving PTCy. |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | Cohort | Future Oncol | Compares Busulfan-Cyclophosphamide vs Fludarabine-Busulfan conditioning for allogeneic transplant in AML. |
| [32857869](https://pubmed.ncbi.nlm.nih.gov/32857869/) | 2020 | Cohort | Am J Hematol | Examines NK cell alloreactivity in AML in the post-transplant Cyclophosphamide era. |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | Cohort | Cytotherapy | Identifies prognostic factors in haploidentical transplantation with PTCy for AML. |
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | Cohort | Haematologica | Analyzes genetic risk classification (n=217) in AML patients treated with HCT and PTCy-based GVHD prophylaxis. |
| [40437709](https://pubmed.ncbi.nlm.nih.gov/40437709/) | 2025 | Cohort | Eur J Haematol | Evaluates conditioning intensity impact on survival in AML patients receiving ATG + PTCy-based GVHD prophylaxis. |
| [38499049](https://pubmed.ncbi.nlm.nih.gov/38499049/) | 2024 | Cohort | Transplant Immunol | Assesses Cladribine combined with Busulfan+Cyclophosphamide as intensive conditioning for relapsed/refractory AML. |
| [25345651](https://pubmed.ncbi.nlm.nih.gov/25345651/) | 2015 | Cohort | Am J Hematol | Compares survival outcomes of myeloablative vs Cyclophosphamide/Fludarabine nonmyeloablative allotransplant for AML (n=165). |
| [31449699](https://pubmed.ncbi.nlm.nih.gov/31449699/) | 2019 | Cohort | Eur J Haematol | Evaluates reduced-intensity conditioning with ATG and PTCy for GVHD prophylaxis in AML. |

## India Market Information

Cyclophosphamide currently has **no market authorization records** in this evidence pack (market status: Not Marketed; 0 registrations). No license or product data is available to summarize.

## Cytotoxicity

Cyclophosphamide is classified as antineoplastic based on its established role as a nitrogen mustard alkylating chemotherapy agent used across hematologic malignancies and transplant conditioning regimens.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Nitrogen mustard alkylating agent) |
| Myelosuppression Risk | High — dose-dependent neutropenia, thrombocytopenia, and anemia are well documented, particularly at myeloablative conditioning and high-dose PTCy doses |
| Emetogenicity Classification | High at high-dose/conditioning regimens; Moderate at standard chemotherapy doses |
| Monitoring Items | CBC with differential, renal and hepatic function, urinalysis (hemorrhagic cystitis risk), cardiac monitoring at high doses |
| Handling Protection | Yes — cytotoxic drug handling precautions required per standard hazardous-drug protocols; please refer to the package insert for full warnings and precautions |

## Safety Considerations

**Drug Interactions**: 481 total interactions on record. Notable Moderate-level interactions include Amphotericin B (all formulations), Bupropion, Aprepitant, Metronidazole, Nitisinone, and multiple sulfonylureas (Chlorpropamide, Acetohexamide, Glimepiride, Glipizide, Glyburide, Nateglinide, Repaglinide, Tolazamide, Tolbutamide, Troglitazone). Minor-level interactions include Levofloxacin and Ondansetron.

No key warnings or contraindications data is available in this evidence pack — please refer to the package insert for this information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2/3 trials and registry cohorts (L1 evidence) establish Cyclophosphamide-based conditioning (Bu/Cy) and post-transplant Cyclophosphamide (PTCy) as standard practice for AML transplant management, giving strong confidence in the mechanistic and clinical basis of this prediction — though it should be understood as confirming established practice rather than a novel indication.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data from DrugBank to support formal safety linkage
- TFDA/local label warnings and contraindications (currently unavailable — flagged as Blocking data gap)
- Clinical review of the 481 catalogued drug interactions for relevance to conditioning/PTCy dosing regimens
- Local market authorization and formulation/route data, since the drug is currently unmarketed in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

