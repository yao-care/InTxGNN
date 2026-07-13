---
layout: default
title: Mercaptopurine
parent: 僅模型預測 (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
---

# Mercaptopurine
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

# Mercaptopurine: From Acute Lymphoblastic Leukemia to Myeloid Leukemia

## One-Sentence Summary

Mercaptopurine (6-MP) is a purine antimetabolite classically established as the backbone of maintenance therapy for acute lymphoblastic leukemia (ALL), with decades of clinical validation across global multi-centre trials.
The TxGNN model predicts it may be effective for **Myeloid Leukemia** — a mechanistically adjacent indication with historical precedent — supported by **29 clinical trials** and **20 publications** currently available.
Evidence quality reaches **L2**, reflecting completed Phase 3/4 trials in APL maintenance and emerging Phase 1 data directly testing 6-MP in relapsed/refractory AML.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute lymphoblastic leukemia (established global clinical use; no India regulatory authorisation on record) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Mercaptopurine belongs to the thiopurine class of antimetabolites. Once absorbed, it is converted by hypoxanthine-guanine phosphoribosyltransferase (HPRT) into 6-thioinosine monophosphate (TIMP) and subsequently into cytotoxic thioguanine nucleotides (TGNs). These TGNs are incorporated into both DNA and RNA, causing strand termination and triggering apoptosis in rapidly dividing cells. A secondary metabolic branch generates 6-methylmercaptopurine ribonucleotides (MMPRs), which inhibit phosphoribosyl pyrophosphate amidotransferase — the rate-limiting enzyme in de novo purine biosynthesis. This dual mechanism creates a broad-spectrum cytotoxic effect against any malignancy with high purine turnover, regardless of haematological lineage.

The mechanistic link between ALL and myeloid leukemia is direct: both diseases involve uncontrolled proliferation of leukemic blasts originating from haematopoietic progenitors, and both depend heavily on sustained nucleotide synthesis for DNA replication. Historically, 6-MP was a core component of AML induction regimens — most notably the Japanese BHAC-DM protocol (behenoyl cytarabine + daunorubicin + 6-MP), for which nationwide Phase 3 RCTs demonstrated complete remission rates exceeding 60%. In acute promyelocytic leukemia (APL), a biologically distinct AML subtype, 6-MP + methotrexate oral maintenance remains embedded in international standards (AIDA, PETHEMA LPA 2005, AIDA2000) as the two-year post-consolidation backbone.

More recently, the drug is regaining attention as a partner for novel agents: a Phase 1 trial (NCT05506332) is actively recruiting relapsed/refractory AML patients to test 6-MP + venetoclax, and a Phase 1/2 trial (NCT06199557) is investigating 6-MP + valproic acid for AML and high-risk MDS patients unfit for intensive chemotherapy. Together, these strands of evidence — historical RCT data, established APL maintenance protocols, and active early-phase trials — provide a coherent mechanistic and clinical rationale for TxGNN's high-confidence prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Phase 1 | Recruiting | 10 | ApoAML Trial: venetoclax + 6-MP combination in R/R AML; directly tests 6-MP efficacy in myeloid leukemia with a modern BCL-2 inhibitor backbone |
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Phase 1/2 | Recruiting | 48 | 6-MP + valproic acid vs hydroxyurea + valproic acid for newly diagnosed AML or HR-MDS ineligible for standard therapy; targets a clinically urgent unmet need |
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Phase 3 | Completed | 420 | Untreated APL: randomised ATRA + anthracycline ± arsenic trioxide consolidation, followed by maintenance with tretinoin ± mercaptopurine + methotrexate; directly evaluated 6-MP's maintenance contribution |
| [NCT00408278](https://clinicaltrials.gov/study/NCT00408278) | Phase 4 | Completed | 300 | PETHEMA LPA 2005: risk-adapted ATRA + idarubicin induction; 6-MP + methotrexate oral maintenance for 2 years; confirmed tolerability and efficacy in a large, prospective APL cohort |
| [NCT01064557](https://clinicaltrials.gov/study/NCT01064557) | N/A | Unknown | 1,068 | AIDA guideline study (1993–2020) for APL ages >12 months; maintenance arm randomised between ATRA, methotrexate + 6-MP, or both in PCR-negative patients after consolidation |
| [NCT00465933](https://clinicaltrials.gov/study/NCT00465933) | Phase 4 | Completed | N/A | APL AIDA with risk-stratified consolidation; ATRA + 6-MP + methotrexate maintenance; special evaluation of dose reduction in elderly patients (>70 years) |
| [NCT00180128](https://clinicaltrials.gov/study/NCT00180128) | Phase 4 | Unknown | 80 | AIDA2000: APL risk-adapted therapy by age and WBC count; 2-year maintenance with 6-MP + methotrexate + ATRA as standard post-remission care |
| [NCT00492856](https://clinicaltrials.gov/study/NCT00492856) | Phase 3 | Completed | 105 | S0521: Low/intermediate-risk APL — maintenance therapy versus observation; assessed the clinical necessity of sustained post-consolidation treatment |
| [NCT00700544](https://clinicaltrials.gov/study/NCT00700544) | Phase 3 | Completed | 330 | GOELAMS SA-2002: elderly AML patients; ICL induction, then maintenance ± androgens; provided framing evidence for AML post-remission maintenance strategies in older adults |
| [NCT02845232](https://clinicaltrials.gov/study/NCT02845232) | N/A | Completed | 214 | Observational economic analysis of blood product transfusion requirements across AML treatment intensity levels; supports the case for low-toxicity maintenance options |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10497848](https://pubmed.ncbi.nlm.nih.gov/10497848/) | 1999 | RCT | Int J Hematol | JALSG-AML92: daunorubicin + behenoyl cytarabine + 6-MP ± etoposide; no survival advantage from adding etoposide, confirming 6-MP's role as a core component of Japanese AML induction |
| [8174198](https://pubmed.ncbi.nlm.nih.gov/8174198/) | 1994 | RCT | Cancer Chemother Pharmacol | Nationwide Japan RCT (360 evaluable): BH-AC + daunorubicin + 6-MP vs BH-AC + aclarubicin + 6-MP; CR rates 63.7% vs 53.9%; established 6-MP as an AML combination-regimen standard |
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | Clinical Study | J Korean Med Sci | Oral 6-MP + weekly methotrexate for 2 years in transplant-ineligible AML patients after first CR; reported improved leukemia-free and overall survival versus no maintenance |
| [9095207](https://pubmed.ncbi.nlm.nih.gov/9095207/) | 1997 | Phase 2 | Cancer Invest | High-dose continuous IV 6-MP followed by intermediate-dose cytarabine during AML first remission in children; demonstrated feasibility of 6-MP intensification as consolidation component |
| [1793832](https://pubmed.ncbi.nlm.nih.gov/1793832/) | 1991 | Clinical Study | Int J Hematol | 41 adult AML patients: intensive behenoyl cytarabine + daunorubicin + 6-MP induction achieved 71% CR; multi-drug intensive regimen with 6-MP as purine backbone |
| [24492035](https://pubmed.ncbi.nlm.nih.gov/24492035/) | 2014 | Review | Rinsho Ketsueki | Comprehensive review of AML and APL current therapy in Japan; contextualises the evolution of 6-MP-containing regimens and its residual role in APL maintenance |
| [28835099](https://pubmed.ncbi.nlm.nih.gov/28835099/) | 2017 | Translational | Biomacromolecules | CD44-targeted glutathione-sensitive hyaluronic acid–6-MP prodrug (HA-GS-MP) for AML; enhanced intracellular delivery and superior cytotoxicity vs free 6-MP in AML cell lines |
| [265178](https://pubmed.ncbi.nlm.nih.gov/265178/) | 1977 | Clinical Study | Blood | Juvenile chronic myeloid leukemia: sequential subcutaneous cytarabine + oral 6-MP cycles achieved clinical and haematologic response in a disease previously considered unresponsive to chemotherapy |
| [8383541](https://pubmed.ncbi.nlm.nih.gov/8383541/) | 1993 | Case Series | Ann Hematol | AML-M0 (minimally differentiated AML): review of 5 institutional cases and 63 published cases; 6-MP-containing combination regimens among the approaches evaluated |
| [5220682](https://pubmed.ncbi.nlm.nih.gov/5220682/) | 1966 | Historical Study | Minnesota Med | One of the earliest reports of 6-MP + cyclophosphamide for AML; historical anchor establishing 6-MP's multi-decade involvement in myeloid malignancy management |

---

## India Market Information

Mercaptopurine currently has **no registered product authorisations in India**. The drug is not marketed domestically. Any clinical use would rely on import or compounding under compassionate/investigational frameworks.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Antimetabolite (Thiopurine / Purine analog class) |
| Myelosuppression Risk | **High** — leucopenia, neutropenia, thrombocytopenia, and anaemia are expected, dose-limiting toxicities; severity is sharply amplified in patients with TPMT deficiency or NUDT15 R139C variant (especially relevant for Asian populations where NUDT15 R139C allele frequency is ~10%) |
| Emetogenicity Classification | Low |
| Monitoring Items | Complete blood count with differential (weekly during initiation; biweekly to monthly during stable maintenance), liver function tests (ALT, AST, bilirubin — 6-MP hepatotoxicity via MMPN accumulation), renal function; **pre-treatment TPMT and NUDT15 genotyping is a clinical necessity** — dose must be reduced by 50–90% in intermediate/poor metabolisers |
| Handling Protection | Must be handled under cytotoxic drug handling regulations; do not crush or split tablets without appropriate PPE; pregnant healthcare workers should not handle the drug |

---

## Safety Considerations

**Drug Interactions** (296 total interactions identified; key interactions listed below):

| Interacting Drug | Level | Clinical Note |
|-----------------|-------|--------------|
| Mesalazine | Moderate | Aminosalicylates inhibit TPMT activity, raising TGN levels and myelotoxicity risk; dose reduction of 6-MP required if co-administered |
| Sulfasalazine | Moderate | Same TPMT-inhibition mechanism as mesalazine; frequent co-medication in IBD patients also treated with thiopurines |
| Balsalazide | Moderate | Same class; caution warranted in overlap IBD/haematology patients |
| Olsalazine | Moderate | Same class |
| Naltrexone | Moderate | Low-dose naltrexone may interact via immunomodulatory pathways; mechanism not fully characterised |

Please refer to the package insert for complete warnings, contraindications, and the full interaction list.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
6-MP is already embedded as a standard post-remission maintenance agent in APL (an AML subtype), validated by multiple completed Phase 3/4 international trials and longstanding inclusion in AIDA-based protocols. A 2015 prospective study further demonstrated survival benefit for 6-MP oral maintenance in non-APL AML patients ineligible for transplantation. Two currently active early-phase trials (NCT05506332, NCT06199557) are directly testing 6-MP in broader AML settings, confirming sustained clinical interest. The TxGNN score of 99.94% and L2 evidence rating align with this substantial but largely AML-subtype-specific track record.

**To proceed, the following is needed:**
- **Pharmacogenomic screening**: Pre-treatment TPMT and NUDT15 genotyping for all patients; establish a local dosing adjustment protocol adapted to Indian population allele frequencies
- **Regulatory pathway**: Initiate CDSCO import/marketing authorisation process — no approved India formulation currently exists
- **Indication-specific protocol design**: Distinguish APL maintenance context (low-intensity, long-term 6-MP + MTX) from broader AML contexts (higher-intensity or novel-combination settings); tailor dosing and monitoring accordingly
- **Mechanistic data gap (DG002)**: Retrieve full DrugBank MOA and pharmacodynamics data to complete the mechanistic dossier
- **Safety data gap (DG001)**: Obtain TFDA/reference label package insert to formalise contraindication and warning documentation for the Indian regulatory submission
- **Prospective registry or Phase 2 study**: Consider an India-specific study of 6-MP oral maintenance in transplant-ineligible AML patients, given the unmet need and preliminary supportive evidence

> **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

