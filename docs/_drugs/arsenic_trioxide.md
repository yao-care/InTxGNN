---
layout: default
title: Arsenic Trioxide
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 10
---

# Arsenic Trioxide
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

# Arsenic Trioxide: From Acute Promyelocytic Leukemia to Myelodysplastic Syndrome

## One-Sentence Summary

Arsenic trioxide (ATO, brand name Trisenox) is an internationally established treatment for Acute Promyelocytic Leukemia (APL), achieving molecular remission in over 80% of cases.
The TxGNN model predicts it may be effective for **Myelodysplastic Syndrome (MDS)**, with **24 clinical trials** and **20 publications** currently supporting this direction.
Among the top 10 predicted indications, MDS carries the highest evidence level (L2) and the strongest actionable recommendation ("Proceed with Guardrails").

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Promyelocytic Leukemia (APL) |
| Predicted New Indication | Myelodysplastic Syndrome (MDS) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Arsenic trioxide (As₂O₃) acts through several converging anti-cancer mechanisms. At the molecular level, ATO binds to cysteine thiol groups and inhibits thioredoxin reductase, activating the mitochondrial apoptotic cascade (cytochrome c release → caspase activation). It simultaneously suppresses NF-κB survival signaling, downregulates anti-apoptotic BCL-2 family proteins (BCL-2, BCL-XL, MCL-1), and degrades the GLI2 transcription factor in the Hedgehog/GLI pathway. ATO also exerts immune-modulatory effects by restoring the Treg/Th17/Th1 balance and has documented anti-angiogenic properties.

MDS and APL share a common origin in clonal hematopoietic stem cell dysfunction. In MDS, pathological myeloid progenitors overexpress BCL-2 and rely on constitutive NF-κB signaling to resist programmed cell death — the same targets ATO addresses in APL. This mechanistic overlap forms a direct biological rationale for repurposing. Furthermore, ATO demonstrates synergy with DNA hypomethylating agents (decitabine, azacitidine): ATO dismantles pro-survival signaling while hypomethylating agents reverse epigenetic silencing of tumor suppressor genes. This complementary dual-pathway effect has been validated in both MDS cell lines (MUTZ-1, SKM-1) and Phase I/II clinical trials.

Translational evidence has been partially established: a 2023 systematic review with network meta-analysis confirmed ATO activity (as monotherapy and in combination) in MDS patients, and an oral formulation (Arsenol®) is now being evaluated in active Phase 2 trials specifically designed for MDS and TP53-mutated myeloid malignancies (recruitment ongoing as of 2025). The critical remaining gap is the absence of a completed, adequately powered Phase 3 randomized controlled trial in MDS — the definitive hurdle before formal regulatory approval in this indication.

---

## Clinical Trial Evidence

The following 10 most relevant trials are selected from 24 registered trials for MDS:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00803530](https://clinicaltrials.gov/study/NCT00803530) | Phase 2 | Terminated | 55 | Prospective multicenter trial of ATO + ascorbic acid in MDS; terminated early but generated partial efficacy data supporting ATO + vitamin C combination |
| [NCT00251511](https://clinicaltrials.gov/study/NCT00251511) | Phase 2 | Terminated | 60 | ATO + thalidomide in low through high-risk MDS (IPSS-stratified); dual-pathway suppression design exploring immune modulation and apoptosis induction |
| [NCT00454480](https://clinicaltrials.gov/study/NCT00454480) | Phase 2/3 | Completed | 2,000 | Largest completed trial; evaluates multiple regimens including ATO in older patients with AML and high-risk MDS; MDS subgroup data available for analysis |
| [NCT00020969](https://clinicaltrials.gov/study/NCT00020969) | Phase 2 | Terminated | N/A | Early landmark multicenter Phase 2 of ATO monotherapy in MDS; foundational study that established the research direction despite early termination |
| [NCT00274820](https://clinicaltrials.gov/study/NCT00274820) | Phase 2 | Completed | 15 | TADA regimen (Thalidomide + ATO + Dexamethasone + Ascorbic Acid) in MDS/overlap myeloproliferative disorders; provides multi-agent proof-of-concept data |
| [NCT06778187](https://clinicaltrials.gov/study/NCT06778187) | Phase 2 | Recruiting | 30 | Oral ATO (Arsenol®) + ascorbic acid ± low-intensity therapy in previously untreated or relapsed/refractory TP53-mutated MDS/AML; most current study (start: Feb 2025) |
| [NCT02190695](https://clinicaltrials.gov/study/NCT02190695) | Phase 2 | Completed | 92 | Three-arm randomized study: decitabine vs. decitabine + carboplatin vs. decitabine + ATO in relapsed/refractory AML and MDS; provides comparative contribution data for ATO arm |
| [NCT00274781](https://clinicaltrials.gov/study/NCT00274781) | Phase 2 | Completed | 30 | ATO + gemtuzumab ozogamicin in advanced MDS; completed with 30 patients; provides combination safety profile and activity signal in an advanced disease setting |
| [NCT06670222](https://clinicaltrials.gov/study/NCT06670222) | Phase 1 | Recruiting | 24 | Dose-escalation of oral ATO in low-risk MDS failing ESA and luspatercept; start July 2025; establishes safe dose range for oral formulation in treatment-refractory patients |
| [NCT00671697](https://clinicaltrials.gov/study/NCT00671697) | Phase 1 | Completed | 13 | IV decitabine + ATO + ascorbic acid in MDS and AML; completed with 13 patients; characterizes pharmacodynamic interaction of triple combination |

---

## Literature Evidence

The following 10 publications are prioritized by study type and clinical relevance (from 20 publications for MDS):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37908176](https://pubmed.ncbi.nlm.nih.gov/37908176/) | 2023 | Systematic Review / Meta-Analysis | Hematology | Network meta-analysis confirming ATO efficacy in MDS across multiple regimens; identifies ATO + ascorbic acid and ATO + decitabine as optimal combinations |
| [40167011](https://pubmed.ncbi.nlm.nih.gov/40167011/) | 2025 | Retrospective Clinical Study | Hematology | Decitabine + ATO in elderly high-risk MDS; demonstrates efficacy and manageable safety profile in a population with limited treatment options |
| [38816179](https://pubmed.ncbi.nlm.nih.gov/38816179/) | 2024 | Comparative Clinical Analysis | Immunopharmacology and Immunotoxicology | Compares oral (realgar) vs. IV ATO immunological effects in MDS mouse model; details Treg/Th17/Th1 rebalancing and cytokine modulation |
| [20956016](https://pubmed.ncbi.nlm.nih.gov/20956016/) | 2011 | Phase I/II Clinical Trial | Leukemia Research | ATO + low-dose cytarabine in 49 patients with Int-2/high-risk MDS; CR rate 17%, established dosing feasibility and activity signal |
| [17920679](https://pubmed.ncbi.nlm.nih.gov/17920679/) | 2008 | Clinical Study | Leukemia Research | ATO + all-trans retinoic acid + thalidomide in higher-risk MDS; evaluates triple-agent differentiation-plus-apoptosis strategy |
| [18282365](https://pubmed.ncbi.nlm.nih.gov/18282365/) | 2007 | Review | Clinical Lymphoma & Myeloma | Summarizes ATO clinical data in leukemia and MDS; contextualizes APL remission rates with exploratory MDS results and combination approaches |
| [20425329](https://pubmed.ncbi.nlm.nih.gov/20425329/) | 2006 | Review | Current Hematologic Malignancy Reports | Reviews ATO mechanisms (pro-apoptotic, anti-proliferative, anti-angiogenic) in MDS and summarizes early trial outcomes supporting clinical development |
| [30898879](https://pubmed.ncbi.nlm.nih.gov/30898879/) | 2019 | In Vitro / Mechanistic | Journal of Investigative Medicine | Synergistic apoptosis induction by decitabine + ATO in MUTZ-1 and SKM-1 MDS cell lines via endoplasmic reticulum stress; provides mechanistic basis for combination therapy |
| [22964015](https://pubmed.ncbi.nlm.nih.gov/22964015/) | 2012 | Translational / Clinical Sample | Journal of Hematology & Oncology | Ex vivo comparison of BCL2 family gene expression in MDS patient bone marrow before and after ATO treatment; directly demonstrates BCL2/BCL-XL downregulation |
| [16105982](https://pubmed.ncbi.nlm.nih.gov/16105982/) | 2005 | Mechanistic Study | Blood | Characterizes NF-κB activity and FLIP expression in MDS patient samples; demonstrates ATO-induced apoptosis via NF-κB suppression in RAEB subtype |

---

## India Market Information

Arsenic trioxide currently has **no registered products in India** (market status: Not Marketed; total registrations: 0). The drug is internationally approved — notably as Trisenox® (FDA-approved for APL) and in multiple other regulatory jurisdictions — but has not obtained market authorization in India as of the data cutoff (April 5, 2026). Any clinical use in India for MDS would require a special import license, a New Drug Application submission, or a compassionate use / expanded access protocol.

---

## Cytotoxicity

Arsenic trioxide is an antineoplastic agent (approved for the hematologic malignancy APL; original indication involves leukemia). This section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Inorganic cytotoxic (arsenic-based); induces differentiation and apoptosis in malignant hematopoietic cells through a distinct mechanism separate from conventional alkylating agents or antimetabolites |
| Myelosuppression Risk | Moderate — particularly relevant in MDS patients who already have pre-existing cytopenias; initial worsening of blood counts possible before clinical response; CBC monitoring is essential |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (weekly during induction), serum electrolytes (K⁺, Mg²⁺ before each dose), 12-lead ECG / QTc interval (baseline and during treatment), liver function tests (AST/ALT), renal function (creatinine, eGFR) |
| Handling Protection | Must follow cytotoxic drug handling regulations: closed-system drug-transfer device, PPE (gloves, gown, face shield), disposal as hazardous pharmaceutical waste |

---

## Safety Considerations

**Drug Interactions (332 total interactions identified; key interactions listed below):**

| Interacting Drug | Severity | Clinical Concern |
|---------|------|------|
| Amphotericin B (conventional, lipid complex, cholesteryl sulfate, liposomal) | **Major** | All formulations cause hypokalemia and hypomagnesemia, potentiating ATO-induced QT prolongation; correct electrolytes before and during concurrent use |
| Hydrocortisone | **Major** | Corticosteroid-driven electrolyte shifts (hypokalemia) amplify QT risk; monitor QTc closely |
| Cisapride | **Major** | Direct additive QT prolongation; concurrent use is contraindicated |
| Clarithromycin | **Major** | Strong QT prolongation; prefer alternative antibiotics (e.g., amoxicillin-clavulanate) |
| Dolasetron | **Major** | Additive QT prolongation; use alternative antiemetics (e.g., metoclopramide, dexamethasone) |
| Granisetron | **Major** | Additive QT prolongation; minimize 5-HT3 antagonist use or choose ondansetron with careful QTc monitoring |
| Levofloxacin | **Major** | Additive QT prolongation; select non-QT-prolonging antibiotics whenever clinically feasible |
| Famotidine | Moderate | Monitor; H2-receptor blockers may alter gastric pH and drug absorption kinetics |
| Loperamide | Moderate | Moderate QT prolongation risk; use cautiously if antidiarrheal therapy is needed |
| Magnesium citrate / Magnesium hydroxide | Moderate | Electrolyte shifts may transiently affect QTc interval; monitor serum Mg²⁺ |

> The predominant interaction pattern across all 332 DDIs is **QT interval prolongation**. Baseline ECG with QTc measurement, correction of electrolyte abnormalities (K⁺ ≥ 4.0 mEq/L; Mg²⁺ ≥ 0.8 mmol/L), and ongoing cardiac monitoring are essential safety measures throughout ATO treatment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 2 trials have directly evaluated ATO in MDS, a 2023 systematic review with network meta-analysis confirms clinically meaningful activity, and active Phase 2 trials (including an oral ATO formulation, Arsenol®) are currently recruiting as of 2025. The mechanistic rationale — pro-apoptotic, anti-NF-κB, synergy with hypomethylating agents, immune modulation — is supported across preclinical, translational, and early clinical data. However, no completed Phase 3 RCT specifically in MDS exists, ATO is not registered in India, and the full safety profile for the Indian regulatory context requires verification.

**To proceed, the following is needed:**

- **Complete MOA documentation**: Retrieve full DrugBank mechanism-of-action data (DrugBank DB01169) to support mechanistic-link analysis in the regulatory dossier
- **Full safety package**: Download and parse the complete prescribing information / package insert (FDA Trisenox® or equivalent) for comprehensive warnings, contraindications, and special population data
- **QT cardiac safety protocol**: Develop a formal QTc monitoring plan given 332 total drug interactions, the majority of which involve QT prolongation risk
- **Target population definition**: Prioritize a clinically defined MDS subgroup — candidates include TP53-mutated MDS, hypomethylating agent-refractory MDS, or high-risk MDS by IPSS-R — to maximize the benefit-risk ratio
- **Phase 3 trial design**: Design a well-powered randomized controlled trial (e.g., ATO + decitabine vs. decitabine alone in high-risk MDS) building on the Phase 2 data and the 2023 meta-analysis findings
- **India regulatory pathway**: Engage with CDSCO to assess feasibility of a New Drug Application or special import authorization for ATO in the MDS indication; evaluate whether data from international trials can support an abbreviated approval pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

