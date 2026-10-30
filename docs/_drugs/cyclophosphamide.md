---
layout: default
title: Cyclophosphamide
parent: Model Prediction Only (L5)
nav_order: 218
evidence_level: L5
indication_count: 4
monitor_inn: "Cyclophosphamide"
predicted_indications: ["myeloid leukemia", "vertebral anomalies and variable endocrine and T-cell dysfunction", "retroperitoneal neoplasm", "lymph node cancer"]
last_modified_at: 2026-10-30
description: "Cyclophosphamide: predicted new indication myeloid leukemia (evidence level L5). Approved use: Not recorded in the local data"
---

# Cyclophosphamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Cyclophosphamide: Alkylating cytotoxic agent → myeloid leukemia
{: .text-alpha }

## One-Sentence Summary

Cyclophosphamide is an alkylating chemotherapy agent that cross-links DNA in rapidly dividing cells.
The TxGNN model predicts it may be useful for **myeloid leukemia**, with **35 listed clinical trials** and **20 publications** pointing in this direction.
Most of this evidence reflects its use inside transplant conditioning, post-transplant GVHD prophylaxis and combination regimens, not as a single tested agent, and no cited study tests cyclophosphamide alone against myeloid leukemia.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | myeloid leukemia |
| TxGNN Prediction Score | 0.9947 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Cyclophosphamide is an alkylating agent. Its active metabolite, phosphoramide mustard, cross-links DNA and induces apoptosis in rapidly dividing cells. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description rests on general pharmacology.

In myeloid leukemia, cyclophosphamide appears in three settings: myeloablative conditioning before stem cell transplantation (for example busulfan plus cyclophosphamide), combination chemotherapy (for example clofarabine, etoposide and cyclophosphamide), and post-transplant cyclophosphamide (PTCy) for GVHD prophylaxis. PTCy selectively depletes alloreactive T cells while sparing regulatory T cells and hematopoietic stem cells.

These uses make the prediction plausible. However, cyclophosphamide is almost always one component of a multi-drug or transplant regimen, so the studies cannot isolate its own contribution. Under the evidence rules for this report, the level is therefore L5 (model prediction, with only indirect support), even though the volume of related clinical use is large.

## Clinical Trial Evidence

The table lists the trials judged most relevant. Many trials are in leukemia-related transplant settings where cyclophosphamide is one part of the regimen.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04473911](https://clinicaltrials.gov/study/NCT04473911) | Phase 1 | Completed | 25 | Reduced-intensity haploidentical transplant with PTCy plus GVHD prevention in AML, ALL, MDS and lymphoma |
| [NCT00315705](https://clinicaltrials.gov/study/NCT00315705) | Phase 1/2 | Completed | 50 | Clofarabine + etoposide + cyclophosphamide in pediatric relapsed/refractory acute leukemias |
| [NCT00939653](https://clinicaltrials.gov/study/NCT00939653) | Phase 2 | Terminated | 6 | Clofarabine + etoposide + cyclophosphamide in relapsed/refractory AML |
| [NCT00003187](https://clinicaltrials.gov/study/NCT00003187) | Phase 2/3 | Completed | 19 | Unrelated donor marrow transplantation; cyclophosphamide likely part of conditioning |
| [NCT00390793](https://clinicaltrials.gov/study/NCT00390793) | Phase 2 | Completed | 107 | Hyper-CVAD plus dasatinib in Ph-positive leukemia; partial relevance to myeloid disease |
| [NCT01350245](https://clinicaltrials.gov/study/NCT01350245) | Phase 2 | Completed | 28 | Two-step haploidentical transplant for hematologic malignancies |
| [NCT02441803](https://clinicaltrials.gov/study/NCT02441803) | Phase 2 | Completed | 11 | Allogeneic transplant as salvage in primary induction-failure AML |
| [NCT04904588](https://clinicaltrials.gov/study/NCT04904588) | Phase 2 | Active, not recruiting | 300 | Mismatched unrelated donor transplant with PTCy for hematologic malignancies |
| [NCT00309842](https://clinicaltrials.gov/study/NCT00309842) | Phase 2 | Completed | 213 | Cord blood transplant after cyclophosphamide/fludarabine/TBI conditioning |
| [NCT05515029](https://clinicaltrials.gov/study/NCT05515029) | Phase 3 | Active, not recruiting | 56 | PTCy with abatacept, vedolizumab and calcineurin inhibitor for GVHD prevention in children and young adults with blood cancers |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | Systematic review / network meta-analysis | Bone Marrow Transplant | Compares myeloablative conditioning regimens, including busulfan-cyclophosphamide, in AML in remission |
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | Cohort | Haematologica | 217 AML patients given PTCy-based GVHD prophylaxis; 2-year overall survival 77% |
| [38758817](https://pubmed.ncbi.nlm.nih.gov/38758817/) | 2024 | Registry study | Cancer | PTCy vs ATG vs combination for GVHD prevention in haploidentical transplant for AML |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | Cohort | Future Oncol | Busulfan-cyclophosphamide vs fludarabine-busulfan conditioning in AML |
| [25345651](https://pubmed.ncbi.nlm.nih.gov/25345651/) | 2015 | Cohort | Am J Hematol | Cyclophosphamide/fludarabine non-myeloablative transplant vs myeloablative transplant in AML |
| [41046309](https://pubmed.ncbi.nlm.nih.gov/41046309/) | 2026 | Cohort | Bone Marrow Transplant | Cord blood vs haploidentical transplant with PTCy in AML in first remission |
| [42373850](https://pubmed.ncbi.nlm.nih.gov/42373850/) | 2026 | Cohort | Bone Marrow Transplant | Haploidentical vs mismatched unrelated transplant with PTCy in secondary AML |
| [36842566](https://pubmed.ncbi.nlm.nih.gov/36842566/) | 2023 | Cohort | Transplant Immunology | PTCy and early mixed chimerism in myeloid malignancies |
| [14662323](https://pubmed.ncbi.nlm.nih.gov/14662323/) | 2003 | Review | Exp Hematol | Busulfan-cyclophosphamide vs TBI-cyclophosphamide conditioning in AML |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | Cohort | Int J Mol Sci | PTCy after matched donor transplant in pediatric AML |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 39643 | Cycloxan 200mg Injection | vial of 1 Injection | Not recorded |
| 47544 | Cyphos 1000mg Injection | vial of 1 Injection | Not recorded |
| 49209 | Cycram 1000mg Injection | vial of 1 Injection | Not recorded |
| 72341 | Endoxan Tablet | strip of 10 tablets | Not recorded |
| 175621 | Phosmid 50mg Tablet | strip of 10 tablets | Not recorded |

The list may be partial. There are 20 valid single-ingredient licences, in injectable and oral tablet forms.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | High; neutropenia is expected, especially at transplant-conditioning doses |
| Emetogenicity Classification | Moderate, dose-dependent |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes, urinalysis for haemorrhagic cystitis |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Drug Interactions**: 481 interactions are recorded. Those listed are mostly moderate, including amphotericin B (several formulations), bupropion, aprepitant, metronidazole, and sulfonylurea and related antidiabetic agents (chlorpropamide, glimepiride, glipizide, glyburide, tolbutamide, repaglinide, nateglinide). Levofloxacin and ondansetron are minor.

Label warnings and contraindications are not available in the data compiled for this report; please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible and cyclophosphamide is widely used in myeloid leukemia transplant and chemotherapy regimens. But no cited study isolates its effect against this disease, so the evidence stays at L5 and the safety data are incomplete.

**To proceed, the following is needed:**
- Studies that isolate cyclophosphamide's contribution in myeloid leukemia (for example randomized comparisons of regimens that differ only in cyclophosphamide)
- Package insert warnings and contraindications for the Indian products
- Mechanism-of-action data from a curated source
- A safety monitoring plan for high-dose and transplant-conditioning use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

