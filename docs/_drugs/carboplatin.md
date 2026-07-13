---
layout: default
title: Carboplatin
parent: 僅模型預測 (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
---

# Carboplatin
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

# Carboplatin: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Carboplatin is a second-generation platinum-based chemotherapy agent, established as a standard treatment for ovarian cancer, non-small cell lung cancer, and multiple other solid tumors globally.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma** with a high confidence score of 99.86%,
backed by **multiple Phase 2/3 clinical trials** (including 2 completed Phase 3 RCTs with over 3,000 patients enrolled) and **20 publications** supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ovarian cancer; other solid tumors (global pharmacological use; no India CDSCO registration on record) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Carboplatin is a platinum-containing compound that forms DNA intrastrand and interstrand crosslinks, primarily at GG and AG dinucleotide sequences. This structural damage prevents DNA replication and transcription, triggering programmed cell death in rapidly proliferating tumor cells. While detailed mechanism of action data was not retrieved from DrugBank in this evidence pack, Carboplatin's platinum-based cytotoxic mechanism is one of the best-characterised in oncology and is mechanistically distinct from antimetabolites or topoisomerase inhibitors.

The connection to female breast carcinoma is particularly compelling at the molecular level. Triple-negative breast cancer (TNBC) has a high prevalence of BRCA1/2 mutations and homologous recombination deficiency (HRD) — precisely the cellular context in which platinum-induced DNA crosslinks cannot be repaired, leading to cell death. This principle, known as "BRCAness," predicts platinum sensitivity and is well-validated across multiple TNBC clinical trials including GeparSixto, NACATRINE, and BROCADE3. For HER2-positive breast cancer, Carboplatin paired with Docetaxel and Trastuzumab forms the TCH regimen, which the landmark BCIRG 006 Phase 3 trial (n=3,222) established as non-inferior in disease-free survival to anthracycline-containing regimens while carrying significantly lower cardiac risk.

The TxGNN model's 99.86% prediction score reflects both the strong mechanistic overlap between Carboplatin's known mechanism and breast cancer vulnerability pathways, and the dense clinical evidence network linking platinum compounds to breast cancer outcomes. This represents one of the most evidence-rich drug repurposing predictions in this analysis — the model is identifying a biologically grounded, clinically validated connection rather than a speculative extrapolation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Phase 3 | Completed | 3,222 | BCIRG 006: Adjuvant TCH (Docetaxel+Carboplatin+Trastuzumab) vs AC-TH vs AC-T in HER2+ operable BC; TCH demonstrated non-inferior DFS with significantly lower cardiotoxicity — established TCH as a global standard of care |
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Phase 3 | Completed | 263 | Docetaxel+Carboplatin+Trastuzumab vs Docetaxel+Trastuzumab as first-line in HER2-amplified advanced BC; directly evaluated the added value of Carboplatin in HER2-targeted regimens |
| [NCT02978495](https://clinicaltrials.gov/study/NCT02978495) | Phase 2 | Completed | 154 | NACATRINE: Neoadjuvant Carboplatin in TNBC (Brazil); prospective Phase 2 RCT assessing pCR rate with platinum-based neoadjuvant therapy in triple-negative subtype |
| [NCT00005963](https://clinicaltrials.gov/study/NCT00005963) | Phase 2 | Completed | 53 | Docetaxel+Carboplatin as first-line therapy for metastatic BC; directly demonstrated combination activity in advanced disease |
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Phase 1 | Completed | 103 | Olaparib (AZD2281, PARP inhibitor)+Carboplatin in BRCA1/2 mutation carriers and sporadic TNBC; established safety and explored platinum-PARP inhibitor synergy |
| [NCT01237067](https://clinicaltrials.gov/study/NCT01237067) | Phase 1 | Completed | 77 | Olaparib+Carboplatin PK/PD study in refractory/recurrent women's cancers (BC and OC); characterised pharmacokinetic interaction and optimised combination dosing |
| [NCT06351332](https://clinicaltrials.gov/study/NCT06351332) | Phase 1/2 | Active, not recruiting | 78 | ZAP-IT: Azenosertib (WEE1 inhibitor)+Carboplatin+Pembrolizumab in metastatic TNBC; novel triplet targeting cell cycle checkpoint, DNA damage, and immune suppression simultaneously |
| [NCT00479674](https://clinicaltrials.gov/study/NCT00479674) | Phase 2 | Completed | 41 | Abraxane (nab-Paclitaxel)+Carboplatin+Bevacizumab in triple-negative metastatic BC; evaluated multi-modal combination addressing angiogenesis and DNA damage |
| [NCT00616967](https://clinicaltrials.gov/study/NCT00616967) | Phase 2 | Active, not recruiting | 68 | Double-blind Phase II: Carboplatin+Nab-Paclitaxel ± Vorinostat (HDAC inhibitor) as preoperative chemo in HER2-negative BC; assessed epigenetic sensitisation alongside platinum |
| [NCT07103447](https://clinicaltrials.gov/study/NCT07103447) | Phase 2 | Not yet recruiting | 54 | AK112 (PD-1/VEGF bispecific antibody)+nab-Paclitaxel+Carboplatin as neoadjuvant in TNBC; evaluating pCR, ORR, breast conservation rate, and iDFS |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38309017](https://pubmed.ncbi.nlm.nih.gov/38309017/) | 2024 | Phase 3 RCT (final OS) | Eur J Cancer | BROCADE3 final OS: Veliparib+Carboplatin+Paclitaxel significantly improved PFS vs placebo+Carbo/Pac in BRCA1/2-mutated HER2-negative advanced BC; OS trend favoured the veliparib arm |
| [24794243](https://pubmed.ncbi.nlm.nih.gov/24794243/) | 2014 | Phase 2 RCT | Lancet Oncol | GeparSixto (GBG 66): Addition of Carboplatin to neoadjuvant therapy significantly improved pCR in TNBC (53.2% vs 36.9%) and HER2+ BC; landmark trial establishing neoadjuvant Carboplatin role |
| [39671272](https://pubmed.ncbi.nlm.nih.gov/39671272/) | 2025 | RCT | JAMA | CamRelief: Camrelizumab (anti-PD-1)+Carboplatin-containing neoadjuvant chemo vs placebo+chemo in early/locally advanced TNBC; demonstrated improved pCR rates with immunotherapy-platinum combination |
| [33208340](https://pubmed.ncbi.nlm.nih.gov/33208340/) | 2021 | Phase 2 RCT | Clin Cancer Res | NeoSTOP: Anthracycline-free neoadjuvant Carboplatin+Taxane vs anthracycline-containing regimen in Stage I-III TNBC; comparable pCR rates support Carboplatin as anthracycline-sparing backbone |
| [40593759](https://pubmed.ncbi.nlm.nih.gov/40593759/) | 2025 | Phase 2b RCT | Nat Commun | MUKDEN 06: ARX788+Pyrotinib vs standard TCbHP (Docetaxel+Carboplatin+Trastuzumab+Pertuzumab) neoadjuvant in HER2+ BC; Carboplatin-based TCbHP arm serves as the active control |
| [25247558](https://pubmed.ncbi.nlm.nih.gov/25247558/) | 2014 | Meta-analysis | PLoS One | Meta-analysis confirming Carboplatin and Bevacizumab independently and significantly improve pCR rate in neoadjuvant treatment of TNBC; quantified magnitude of benefit across trials |
| [40817986](https://pubmed.ncbi.nlm.nih.gov/40817986/) | 2025 | Phase 2 RCT | Breast Cancer Res Treat | Randomised Phase II: Carboplatin alone vs Carboplatin+Everolimus (mTOR inhibitor) in advanced TNBC; explored PTEN-loss driven mTOR activation as a carboplatin resistance mechanism |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Review | Med Oncol | Comprehensive review of Paclitaxel+Carboplatin combination in advanced BC: synergy evidence, preclinical mechanism of potentiation, and clinical safety profile |
| [33256829](https://pubmed.ncbi.nlm.nih.gov/33256829/) | 2020 | Phase 2 | Breast Cancer Res | Carboplatin+Bevacizumab in BC brain metastases; demonstrated clinically meaningful activity in this difficult-to-treat population facing blood-brain barrier challenges |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Phase 1 | Breast Cancer Res Treat | Carboplatin+Gemcitabine+Mifepristone (GR antagonist) in advanced BC and recurrent OC; GR antagonism hypothesised to block chemotherapy-induced apoptosis suppression and enhance Carboplatin cytotoxicity |

---

## India Market Information

Carboplatin currently has **no registered products** in the Indian CDSCO regulatory database according to this evidence pack (market status: Not Marketed; 0 registered licenses). This likely reflects a coverage gap in the regulatory data source rather than actual clinical unavailability, as Carboplatin is a widely available generic chemotherapy agent used globally. Formal CDSCO registration verification through official channels is strongly recommended before pursuing any clinical or commercial pathway in India.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Platinum compound (second-generation, DNA crosslinking agent; ATC code L01XA02) |
| Myelosuppression Risk | **High** — Thrombocytopenia is the primary dose-limiting toxicity (platelet nadir typically at Day 21); neutropenia and anaemia are also common; Grade 3/4 thrombocytopenia reported in 25–33% of patients at standard AUC 5–6 dosing |
| Emetogenicity Classification | **Moderate** (lower than cisplatin); 5-HT3 antagonist antiemetics ± dexamethasone prophylaxis is standard; emetogenicity increases at higher AUC doses |
| Monitoring Items | Complete blood count with platelet count (pre-cycle and nadir), serum creatinine and creatinine clearance (Calvert formula required for AUC-based dosing), electrolytes (Mg²⁺, Ca²⁺, K⁺), audiometry (especially in high-dose regimens or paediatric patients), liver function tests, neurological assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations — closed-system drug transfer devices (CSTDs), double gloving, and eye protection during preparation; disposal as hazardous pharmaceutical waste; healthcare workers should avoid skin or mucous membrane contact |

---

## Safety Considerations

**Drug Interactions** (488 total interactions identified in this dataset; key interactions listed below):

| Interacting Drug | Severity | Notes |
|------|------|------|
| Proton Pump Inhibitors (Omeprazole, Esomeprazole, Lansoprazole, Rabeprazole, Pantoprazole, Dexlansoprazole) | Moderate | Six PPI agents each carry a moderate interaction flag with Carboplatin; clinical monitoring recommended when co-administered |
| Aminoglycosides (Kanamycin, Neomycin, Streptomycin) | Moderate | Potential additive nephrotoxicity and ototoxicity; Carboplatin's intrinsic renal and cochlear toxicity is amplified by concurrent aminoglycoside use |
| Vancomycin | Moderate | Additive nephrotoxicity risk; close renal function monitoring required with concomitant use |
| Metronidazole / Tinidazole | Moderate | Moderate interaction noted; clinical monitoring advised |
| Rosuvastatin / Simvastatin | Moderate | Potential pharmacokinetic interaction; monitor for statin toxicity or altered Carboplatin exposure |
| Levofloxacin | Minor | Lower clinical significance; standard monitoring applies |

Please refer to the package insert for complete safety information including boxed warnings and contraindications — CDSCO-approved prescribing information was not available in this evidence pack and should be retrieved before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Carboplatin has an extensive, mature clinical evidence base for female breast carcinoma at the highest evidence level (L1), anchored by at least two completed Phase 3 RCTs — including the landmark BCIRG 006 trial (n=3,222) establishing the TCH regimen as standard of care in HER2-positive BC — plus multiple Phase 2 trials across TNBC and metastatic breast cancer subtypes. The mechanistic rationale is strong and mechanistically coherent (BRCA/HRD-driven platinum sensitivity), and the TxGNN prediction score of 99.86% is consistent with this deep evidence network.

**To proceed, the following is needed:**
- Retrieve complete mechanism of action data from DrugBank (currently a data gap — DG002)
- Obtain CDSCO-approved prescribing information (boxed warnings, contraindications) to complete the safety profile (currently a data gap — DG001)
- Confirm India market availability and CDSCO registration status through official channels; 0 registered licenses were found in this dataset
- Define patient selection biomarkers: BRCA1/2 mutation testing and HRD scoring should be incorporated into any clinical pathway to identify patients most likely to benefit from platinum-based therapy
- Develop renal function-based dosing protocol using the Calvert formula (GFR-based AUC targeting), with consideration for Indian patient population renal function characteristics
- Establish myelosuppression management guidelines including G-CSF prophylaxis thresholds, platelet monitoring schedule, and transfusion triggers appropriate for the target setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

