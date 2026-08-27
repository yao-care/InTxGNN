---
layout: default
title: Lenalidomide
parent: 僅模型預測 (L5)
nav_order: 375
evidence_level: L5
indication_count: 6
---

# Lenalidomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Lenalidomide: From Multiple Myeloma / MDS to Myeloid Leukemia

## One-Sentence Summary

Lenalidomide (Revlimid®) is an oral immunomodulatory drug (IMiD) approved globally for multiple myeloma and myelodysplastic syndromes (MDS) with del(5q) cytogenetic abnormality.
The TxGNN model predicts it may be effective for **Myeloid Leukemia** (including AML and high-risk MDS),
with **50 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple myeloma; MDS with del(5q)-associated transfusion-dependent anemia (based on global approvals) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Lenalidomide is a member of the immunomodulatory drugs (IMiDs) class, derived from thalidomide. It exerts its anticancer effects primarily through binding to cereblon (CRBN), an E3 ubiquitin ligase substrate receptor. This interaction recruits and promotes the degradation of key transcription factors — IKZF1 (Ikaros) and IKZF3 (Aiolos) — that are critical survival factors in malignant hematopoietic cells. Beyond this targeted mechanism, lenalidomide also activates T cells and natural killer (NK) cells, inhibits angiogenesis, and promotes apoptosis in abnormal clones.

Myeloid leukemia (including AML) and MDS share a common origin in hematopoietic stem cell dysregulation. MDS is a recognized pre-leukemic state — approximately one-third of patients progress to AML. Lenalidomide's established activity in del(5q) MDS reflects its ability to suppress clonal hematopoiesis by selectively eliminating del(5q) clones via CDC20B-CK1α-mediated degradation, while restoring normal erythropoiesis. The same molecular vulnerabilities — chromosome 5 deletions, aberrant epigenetic regulation, impaired NK-cell immune surveillance, and dysregulated IKZF1 activity — are present across the myeloid leukemia disease continuum.

The TxGNN prediction is consistent with a large body of translational and clinical evidence. Lenalidomide has been investigated across the full spectrum of myeloid disease: as monotherapy and combined with azacitidine in high-risk MDS and AML, as combination chemotherapy (MEC regimen, idarubicin + cytarabine) in relapsed/refractory AML, and as post-transplant maintenance therapy to prevent relapse. A 2025 mechanistic study (PMID 39881283) confirmed that the histone demethylase KDM5C stabilizes CRBN in AML cells, directly linking lenalidomide's known mechanism to leukemia cell biology.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01029262](https://clinicaltrials.gov/study/NCT01029262) | Phase 3 | Completed | 239 | Lenalidomide vs. placebo in transfusion-dependent, lower-risk MDS without del(5q), refractory to ESA |
| [NCT00843882](https://clinicaltrials.gov/study/NCT00843882) | Phase 3 | Active, Not Recruiting | 247 | Lenalidomide alone vs. with epoetin alfa in low/int-1 risk MDS with symptomatic anemia |
| [NCT01522976](https://clinicaltrials.gov/study/NCT01522976) | Phase 2/3 | Active, Not Recruiting | 282 | Azacitidine ± lenalidomide or vorinostat for higher-risk MDS and CMML |
| [NCT01358734](https://clinicaltrials.gov/study/NCT01358734) | Phase 2 | Completed | 88 | Lenalidomide vs. AZA vs. AZA + lenalidomide for newly diagnosed AML in patients ≥65 years |
| [NCT01743859](https://clinicaltrials.gov/study/NCT01743859) | Phase 2 | Completed | 37 | Sequential azacitidine + lenalidomide for relapsed/refractory AML and high-risk MDS |
| [NCT03118466](https://clinicaltrials.gov/study/NCT03118466) | Phase 2 | Completed | 41 | MEC chemotherapy + lenalidomide for relapsed or refractory AML |
| [NCT00957385](https://clinicaltrials.gov/study/NCT00957385) | Phase 2 | Completed | 24 | Lenalidomide maintenance in AML patients ≥60 years (CR1) or <60 years (CR2+) |
| [NCT00065156](https://clinicaltrials.gov/study/NCT00065156) | Phase 2 | Completed | 148 | Landmark trial: lenalidomide monotherapy in transfusion-dependent MDS with del(5q) |
| [NCT02472691](https://clinicaltrials.gov/study/NCT02472691) | Phase 2 | Completed | 50 | Azacitidine + lenalidomide + donor lymphocyte infusions for MDS/CMML/AML relapse post-allo-SCT |
| [NCT00360672](https://clinicaltrials.gov/study/NCT00360672) | Phase 2 | Completed | 27 | Lenalidomide in relapsed/refractory AML or high-risk MDS with chromosome 5 abnormalities |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [30271212](https://pubmed.ncbi.nlm.nih.gov/30271212/) | 2018 | Meta-analysis | Cancer Manag Res | Systematic review and meta-analysis of lenalidomide efficacy and safety specifically in AML |
| [31221030](https://pubmed.ncbi.nlm.nih.gov/31221030/) | 2019 | Meta-analysis | Hematology | Meta-analysis of azacitidine + lenalidomide for AML, MDS, and CMML — efficacy and adverse events |
| [37288607](https://pubmed.ncbi.nlm.nih.gov/37288607/) | 2023 | Review | Am J Hematol | MDS 2023 update: diagnosis, risk stratification, and management including lenalidomide role |
| [37874917](https://pubmed.ncbi.nlm.nih.gov/37874917/) | 2023 | Review | Blood | Clinical decision-making in MDS; risk-benefit framework for lenalidomide in lower-risk disease |
| [23644421](https://pubmed.ncbi.nlm.nih.gov/23644421/) | 2013 | Review | Leukemia | AZA + lenalidomide combination in MDS and AML — mechanistic rationale and clinical evidence |
| [23316859](https://pubmed.ncbi.nlm.nih.gov/23316859/) | 2013 | Review | Expert Opin Investig Drugs | Lenalidomide as a novel treatment for AML: mechanism, completed trials, and future perspectives |
| [37259567](https://pubmed.ncbi.nlm.nih.gov/37259567/) | 2023 | Prospective study | Haematologica | Azalena-Trial: AZA + lenalidomide + DLI for post-transplant relapse of AML, MDS, and CMML |
| [37435080](https://pubmed.ncbi.nlm.nih.gov/37435080/) | 2023 | Prospective study | Front Immunol | AZA + low-dose lenalidomide as relapse prophylaxis maintenance after allo-HSCT in AML |
| [39881283](https://pubmed.ncbi.nlm.nih.gov/39881283/) | 2025 | Basic science | Cell Mol Biol Lett | KDM5C stabilizes CRBN to enhance lenalidomide sensitivity in AML cells — key mechanistic insight |
| [35512188](https://pubmed.ncbi.nlm.nih.gov/35512188/) | 2022 | Cohort study | Blood | Lenalidomide exposure selectively promotes TP53-mutated therapy-related myeloid neoplasms — safety signal |

---

## India Market Information

Lenalidomide is **not registered or marketed in India**. No product licenses were found in the regulatory database (0 registrations).

> For reference, lenalidomide (Revlimid®) holds approval from the US FDA for multiple myeloma, del(5q) MDS, mantle cell lymphoma, and follicular/marginal zone lymphoma, and from the EMA under comparable indications. Access for Indian patients would require import under specific regulatory pathways, compassionate use programs, or enrollment in clinical trials.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy / Immunomodulatory drug (IMiD) — not conventional cytotoxic; antineoplastic via CRBN-mediated protein degradation |
| Myelosuppression Risk | **High** — neutropenia and thrombocytopenia are very common adverse effects; Black Box Warning for myelosuppression; requires dose modification and growth factor support |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (weekly for first 8 weeks, then monthly); serum creatinine / CrCl (mandatory dose adjustment for renal impairment); thyroid function; DVT/PE signs and symptoms |
| Handling Protection | Oral capsule — standard oral antineoplastic precautions apply; **REMS program enrollment is mandatory** (due to severe teratogenicity risk analogous to thalidomide); strict pregnancy prevention program required for all patients |

---

## Safety Considerations

**Drug Interactions:** 347 total interactions identified in the DDI database. Key interactions include:

- **Major severity:** Rosuvastatin, Simvastatin — risk of increased statin plasma concentrations; consider dose reduction or switch to a less interactive statin
- **Moderate severity:** Eliglustat, Naltrexone — monitor for pharmacodynamic or pharmacokinetic changes
- **Unknown severity (clinical significance to be evaluated):** Metformin, Prednisone, Omeprazole, Lansoprazole, Pantoprazole, Vancomycin, Morphine, Doxycycline, Clotrimazole, Rosiglitazone, and others

> Detailed warnings and contraindications were not available in the current Evidence Pack. Please refer to the US FDA-approved package insert (Revlimid®) for complete safety information. Known Black Box Warnings include: myelosuppression, deep vein thrombosis/pulmonary embolism (especially when combined with dexamethasone), and embryo-fetal toxicity (absolute contraindication in pregnancy).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Lenalidomide has robust clinical evidence in myeloid malignancies — including a completed Phase 3 trial in MDS and multiple completed Phase 2 trials across the AML/MDS spectrum — supported by two meta-analyses confirming measurable efficacy signals. The TxGNN score of 99.49% is biologically justified given the direct mechanistic overlap between MDS (original indication) and myeloid leukemia. However, the drug is not registered in India, safety data gaps remain in this Evidence Pack, and the evidence in AML specifically is less definitive than in MDS.

**To proceed, the following is needed:**

- **Regulatory pathway:** Establish an India access pathway for a currently unregistered drug (import license, compassionate use, or clinical trial IND)
- **Safety documentation:** Retrieve the complete package insert warnings and contraindications (currently data gap); implement a teratogenicity risk management program equivalent to Revlimid REMS®
- **Subgroup stratification:** Clarify the target patient population — del(5q) MDS, non-del(5q) MDS, or AML — as response rates and regulatory status differ substantially by subgroup
- **Myelosuppression management plan:** CBC monitoring protocol (weekly for ≥8 weeks), dose-modification guidelines, and G-CSF/PLT transfusion thresholds
- **DVT/PE prophylaxis protocol:** Risk-stratified anticoagulation or aspirin regimen, especially if combined with dexamethasone or other agents
- **Renal function assessment:** Mandatory CrCl-based dose adjustment protocol for all enrolled patients
- **TP53 mutation screening:** In light of PMID 35512188, pre-screening for existing TP53 clonal hematopoiesis may be advisable to avoid accelerating therapy-related myeloid neoplasms
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

