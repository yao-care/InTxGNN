---
layout: default
title: Ifosfamide
parent: 僅模型預測 (L5)
nav_order: 295
evidence_level: L5
indication_count: 10
---

# Ifosfamide
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

# Ifosfamide: From Soft Tissue Sarcoma to Female Breast Carcinoma

## One-Sentence Summary

Ifosfamide is a nitrogen mustard oxazaphosphorine alkylating agent with established efficacy in soft tissue sarcomas, testicular carcinoma, and rhabdomyosarcoma, but currently holds no marketing authorization in India.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with **8 clinical trials** and **20 publications** currently supporting this direction.
Evidence stems primarily from Phase 2 combination regimens in anthracycline-resistant metastatic settings; a Phase 3 trial exists but its result status is unknown, limiting the overall grade to L2.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Soft tissue sarcoma, testicular carcinoma (established international clinical use; no India regulatory approval recorded) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on published pharmacology, ifosfamide is a prodrug that requires bioactivation by cytochrome P450 enzymes — primarily CYP3A4, CYP2B6, and CYP2C9 — to generate 4-hydroxy-ifosfamide (4-OH-IF) and ultimately the active alkylating species ifosforamide mustard. This mustard derivative forms DNA interstrand crosslinks that halt replication in rapidly dividing tumour cells.

What is particularly compelling for breast carcinoma is that breast tumour tissue itself expresses CYP3A4, CYP2B6, and CYP2C9, enabling local intratumoral bioactivation of ifosfamide independent of systemic hepatic metabolism (PMID 14970873). DNA adduct formation has been directly quantified in breast cancer tissue from patients receiving ifosfamide (PMID 11138456), providing pharmacodynamic proof-of-concept for on-target cytotoxic activity within the tumour microenvironment — not merely systemic exposure.

Clinically, the primary use case for ifosfamide in breast cancer is as a salvage strategy following anthracycline failure. Multiple Phase 2 trials from the 1990s through 2024 report objective response rates with combinations such as paclitaxel + ifosfamide, epirubicin + ifosfamide (IMEpi, ~50% overall response rate), and the ICE regimen (ifosfamide + carboplatin + etoposide). A recent 2024 case series also reports ifosfamide-based chemotherapy in the first-line setting for metaplastic breast cancer — an aggressive subtype with poor response to standard anthracycline/taxane therapy (PMID 39306877).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00954174](https://clinicaltrials.gov/study/NCT00954174) | Phase 3 | Unknown | 637 | Paclitaxel + carboplatin vs ifosfamide + paclitaxel in newly diagnosed/recurrent uterine or fallopian tube carcinosarcoma; largest gynaecological malignancy trial with ifosfamide; result status unknown, limiting confidence |
| [NCT00026078](https://clinicaltrials.gov/study/NCT00026078) | Phase 2 | Unknown | 42 | Docetaxel + ifosfamide as first-line chemotherapy for metastatic breast cancer; direct indication test in 42 patients |
| [NCT00012311](https://clinicaltrials.gov/study/NCT00012311) | Phase 2 | Unknown | N/A | Randomised comparison of multi-cycle high-dose chemotherapy vs optimised conventional-dose regimens in metastatic breast cancer; ifosfamide-containing arm |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | N/A | TIME regimen (topotecan + ifosfamide/mesna + etoposide) followed by autologous stem cell rescue in metastatic breast cancer; terminated due to insufficient enrolment |
| [NCT00002854](https://clinicaltrials.gov/study/NCT00002854) | Phase 1 | Completed | 33 | Sequential high-dose cisplatin, cyclophosphamide, etoposide, then ifosfamide/carboplatin/paclitaxel with autologous stem cell support in advanced cancers including breast; safety and feasibility |
| [NCT00003086](https://clinicaltrials.gov/study/NCT00003086) | Phase 1/2 | Terminated | 12 | Samarium-153 combined with double autologous bone marrow transplant for Stage IV breast cancer; ifosfamide as conditioning agent; very small sample, terminated |
| [NCT00020722](https://clinicaltrials.gov/study/NCT00020722) | Phase 2 | Terminated | 7 | Chemotherapy + peripheral stem cell transplant + activated T-cell immunotherapy in Stage IV breast cancer; ifosfamide in conditioning; 7 patients, terminated |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | Unknown | 35 | Organoid-guided chemotherapy selection in refractory solid tumours including breast cancer; ifosfamide as one candidate agent in the personalised selection pool |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [11932893](https://pubmed.ncbi.nlm.nih.gov/11932893/) | 2002 | Phase 2 | *Cancer* | Paclitaxel (24-hr infusion) + ifosfamide in anthracycline-resistant metastatic breast carcinoma; direct efficacy and tolerability data |
| [8711499](https://pubmed.ncbi.nlm.nih.gov/8711499/) | 1996 | Phase 2 RCT | *Semin Oncol* | Randomised Phase 2: epirubicin/ifosfamide continued vs treatment interruption in advanced metastatic breast cancer (n=357); 8% CR, 37% PR overall |
| [2347053](https://pubmed.ncbi.nlm.nih.gov/2347053/) | 1990 | Phase 2 | *Cancer Chemother Pharmacol* | Epirubicin + ifosfamide in refractory breast cancer (n=23) plus other solid tumours; notable activity in heavily pretreated patients |
| [8873839](https://pubmed.ncbi.nlm.nih.gov/8873839/) | 1996 | Phase 2 | *J Chemother* | IMEpi (ifosfamide + mesna + epirubicin) as second-line in 16 patients with advanced metastatic breast carcinoma; 50% overall response rate, 9.6-month median remission |
| [9226029](https://pubmed.ncbi.nlm.nih.gov/9226029/) | 1997 | Phase 2 | *Tumori* | Ifosfamide + etoposide in previously treated advanced breast cancer; response and toxicity profile |
| [8918497](https://pubmed.ncbi.nlm.nih.gov/8918497/) | 1996 | Phase 2 | *J Clin Oncol* | Ifosfamide + vinorelbine as first-line chemotherapy for metastatic breast cancer; efficacy and tolerability |
| [10602907](https://pubmed.ncbi.nlm.nih.gov/10602907/) | 1999 | Phase 2 | *Cancer Chemother Pharmacol* | ICE (ifosfamide + carboplatin + etoposide) in metastatic and refractory breast cancer (n=25) after multiple prior regimens |
| [9708645](https://pubmed.ncbi.nlm.nih.gov/9708645/) | 1998 | Phase 2 | *Am J Clin Oncol* | Single-agent ifosfamide + mesna in 29 previously treated metastatic breast cancer patients; establishes single-agent activity baseline |
| [39306877](https://pubmed.ncbi.nlm.nih.gov/39306877/) | 2024 | Case series | *Curr Probl Cancer* | Ifosfamide-based chemotherapy in first-line setting for metaplastic breast cancer (rare aggressive triple-negative variant); fills a gap in standard anthracycline/taxane-resistant subtype |
| [14970873](https://pubmed.ncbi.nlm.nih.gov/14970873/) | 2004 | In vitro/ex vivo | *Br J Cancer* | CYP3A4, CYP2C9, CYP2B6 expression and ifosfamide turnover quantified in breast cancer tissue microsomes; establishes mechanistic basis for intratumoral bioactivation |

---

## Cytotoxicity

Ifosfamide is a conventional cytotoxic alkylating agent (oxazaphosphorine/nitrogen mustard class) with antineoplastic indications. This section is required.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Oxazaphosphorine alkylating agent (nitrogen mustard class) |
| Myelosuppression Risk | High — neutropenia and thrombocytopenia are dose-limiting; G-CSF support is typically required at standard oncological doses |
| Emetogenicity Classification | Moderate to High — prophylactic antiemetics (5-HT3 antagonist ± dexamethasone) required before each infusion |
| Monitoring Items | CBC with differential (before each cycle and at nadir), serum creatinine and urinalysis (nephrotoxicity and haemorrhagic cystitis), liver function tests, serum electrolytes (Fanconi syndrome risk), neurological status assessment (encephalopathy risk) |
| Handling Protection | Must follow cytotoxic drug handling regulations; closed-system transfer devices (CSTDs) required during preparation and administration; personnel protective equipment mandatory |

---

## Safety Considerations

**Drug Interactions**: 471 drug-drug interactions have been identified. Key clinically significant moderate interactions include:

- **Amphotericin B / Amphotericin B lipid complex**: Additive nephrotoxicity — avoid concurrent use or monitor renal function intensively
- **Aprepitant**: CYP3A4 modulation may alter ifosfamide bioactivation; monitor for altered toxicity or efficacy
- **Sulfonylureas** (chlorpropamide, glimepiride, glipizide, glyburide, nateglinide, repaglinide, tolazamide, acetohexamide): Ifosfamide may potentiate hypoglycaemic effect; blood glucose monitoring required
- **Aminoglycosides** (kanamycin, neomycin): Additive nephrotoxicity risk
- **Bupropion**: Increased seizure risk; avoid combination or use with extreme caution
- **Dronabinol / Nabilone**: Additive CNS depression; enhanced encephalopathy risk
- **Scopolamine**: Additive anticholinergic and CNS effects
- **Metoclopramide / Morphine**: CNS interaction; monitor for encephalopathy in patients on concurrent opioids or prokinetics

Please refer to the international package insert for complete safety information, including specific warnings, contraindications, and mandatory mesna uroprotection protocols.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 2 trials with direct breast cancer relevance demonstrate objective response rates with ifosfamide-containing salvage regimens, supported by a biologically plausible intratumoral bioactivation mechanism unique to breast tumour tissue. A Phase 3 trial (NCT00954174, n=637) in a closely related gynaecological malignancy exists, though its unknown result status prevents elevation to L1. The evidence base justifies further evaluation — specifically in anthracycline-resistant and taxane-pretreated metastatic breast cancer, and in aggressive subtypes such as metaplastic breast cancer — but not broad first-line adoption.

**To proceed, the following is needed:**

- **Regulatory pathway assessment**: Ifosfamide is not registered in India; clarify whether clinical use requires an investigational new drug (IND) application, compassionate access approval, or import licensing from CDSCO before any patient exposure
- **Complete safety documentation**: Obtain and review the full international package insert (FDA/EMA) to address the current gaps in formal warnings and contraindications data
- **Mesna uroprotection protocol**: Standardised mesna dosing and hydration guidelines must accompany any ifosfamide administration to prevent haemorrhagic cystitis
- **Neurological monitoring plan**: Ifosfamide encephalopathy is a known serious adverse effect; establish pre-treatment neurological baseline assessment and management algorithm
- **Target patient population definition**: Narrow clinical indication to the subgroup most likely to benefit (e.g., triple-negative, anthracycline- and taxane-pretreated metastatic disease; or metaplastic breast cancer as an unmet-need subtype) to maximise benefit-risk ratio
- **Pharmacokinetic/bioactivation confirmation**: Verify intratumoral CYP expression in the target Indian patient population, as CYP genotype variability may affect bioactivation and therapeutic outcome
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

