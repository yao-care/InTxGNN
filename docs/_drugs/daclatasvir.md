---
layout: default
title: Daclatasvir
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 10
---

# Daclatasvir
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

# Daclatasvir: From Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Daclatasvir is a potent, pangenotypic NS5A replication complex inhibitor originally approved internationally for the treatment of chronic hepatitis C virus (HCV) infection, with no current registration in India.
The TxGNN model predicts it may be effective for **Hepatitis B Virus (HBV) Infection**, with **1 directly relevant completed Phase 2/3 clinical trial** and **19 publications** currently supporting investigation into this direction.
However, the mechanistic link between an NS5A inhibitor and HBV — a DNA virus with no NS5A homologue — is fundamentally weak, and existing clinical evidence primarily reflects HBV reactivation monitoring during HCV treatment rather than direct anti-HBV therapeutic activity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic hepatitis C virus (HCV) infection (international approval; no India registration) |
| Predicted New Indication | Hepatitis B Virus (HBV) Infection |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known published information, daclatasvir is an HCV NS5A replication complex inhibitor. NS5A is a multifunctional phosphoprotein essential for HCV RNA replication, virion assembly, and release. By disrupting NS5A, daclatasvir has demonstrated exceptionally high sustained virologic response (SVR) rates in HCV infection — including genotypes 1 through 6 — when used in combination with sofosbuvir or other direct-acting antivirals.

Both HCV and HBV are hepatotropic viruses sharing a common clinical trajectory: chronic infection → liver fibrosis → cirrhosis → hepatocellular carcinoma (HCC). This phenotypic and epidemiological overlap creates a strong topological connection in the TxGNN knowledge graph, likely explaining the high prediction score. Furthermore, HCV/HBV co-infection is clinically common — particularly in Egypt, Southeast Asia, and sub-Saharan Africa — meaning daclatasvir-containing regimens have been studied in many patients who simultaneously carry HBV, contributing real-world exposure data.

However, the mechanistic connection is weak at its core. HBV belongs to the Hepadnaviridae family and is a partially double-stranded DNA virus that replicates via an RNA intermediate through reverse transcription. It has no NS5A protein or functional homologue. Critically, multiple case reports document HBV *reactivation* — not improvement — during DAA-based HCV therapy (PMID 27329484, 26297529), because successful HCV clearance removes HCV's immunological suppression of HBV replication. This is a safety warning rather than a therapeutic signal. The TxGNN score of 99.80% very likely reflects graph-level proximity of "viral hepatitis" nodes rather than a direct pharmacological rationale.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | The most directly relevant trial: a prospective study of DAA therapy specifically in HCV/HBV co-infected patients, assessing incidence, morbidity, mortality and risk factors for HBV reactivation during HCV treatment — however, HBV reactivation monitoring, not HBV cure, was the primary endpoint |
| [NCT01016912](https://clinicaltrials.gov/study/NCT01016912) | Phase 2 | Completed | 51 | Daclatasvir + PegIFN-alfa-2b + ribavirin in Japanese HCV genotype 1 patients; HBV evaluated as a comorbidity screening item during patient selection, not treated as a primary endpoint |
| [NCT02304159](https://clinicaltrials.gov/study/NCT02304159) | Phase 4 | Completed | 39 | Randomized study comparing 16 vs. 24 weeks of DCV + SOF + RBV in cirrhotic HCV genotype 3 patients; HBV management noted as a secondary safety consideration |
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Phase 3 | Completed | 506 | Head-to-head comparison of ABT-493/ABT-530 versus SOF + daclatasvir in HCV genotype 3; no direct HBV treatment objective |
| [NCT03226717](https://clinicaltrials.gov/study/NCT03226717) | N/A | Unknown | 100 | Study of DAA effects on HCV-related arthropathy in Egypt; HBV not a treatment target |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | Real-world Cohort | Trans R Soc Trop Med Hyg | SOF/DCV-based therapy in Egyptian patients with chronic HCV and HCV/HBV co-infection; demonstrated high SVR rates for HCV; HBV viral load monitored but was not a primary treatment target |
| [29194858](https://pubmed.ncbi.nlm.nih.gov/29194858/) | 2018 | Cohort | J Viral Hepat | Low incidence of HBV reactivation during interferon-free DAA therapy across 790 patients; among those receiving asunaprevir + daclatasvir, reactivation rates were modest and manageable with prophylaxis |
| [28555436](https://pubmed.ncbi.nlm.nih.gov/28555436/) | 2017 | Cohort | Indian J Gastroenterol | HBV infection associated with 43% HCC recurrence rate in HCV patients who achieved HCV SVR via DAA therapy; HBV as a co-risk factor, not a DAA treatment target |
| [27329484](https://pubmed.ncbi.nlm.nih.gov/27329484/) | 2016 | Case Report | Clin J Gastroenterol | Acute hepatitis B in an HCV-infected patient following daclatasvir + asunaprevir therapy; HBV reactivation documented as an adverse safety event, not a therapeutic benefit |
| [26297529](https://pubmed.ncbi.nlm.nih.gov/26297529/) | 2016 | Case Report | Hepatol Res | HBV reactivation in an HBV/HCV co-infected patient during interferon-free DCV + asunaprevir DAA therapy; underscores the critical need for HBV monitoring when using HCV DAAs in co-infected patients |
| [36838792](https://pubmed.ncbi.nlm.nih.gov/36838792/) | 2023 | Computational | Molecules | Virtual screening of HBV pre-genomic RNA (pgRNA) ε stem-loop as a novel antiviral target; provides in silico rationale for exploring new chemical scaffolds against HBV replication — indirect mechanistic support for exploring HBV-specific drug development |
| [30369001](https://pubmed.ncbi.nlm.nih.gov/30369001/) | 2019 | Cohort | Transplant Infect Dis | Efficacy and safety of SOF + DCV in kidney transplant recipients with chronic HCV; HBV co-infection managed as a comorbidity requiring separate treatment |
| [26904396](https://pubmed.ncbi.nlm.nih.gov/26904396/) | 2016 | Review | Acta Pharm Sin B | Comprehensive review of direct anti-HCV agents; explicitly notes that HCV — unlike HBV and HIV — is a curable disease, underscoring the fundamental mechanistic gap between NS5A inhibitors and HBV therapies |
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | Cohort | Lancet Gastroenterol Hepatol | SOF-VEL-VOX re-treatment in Rwanda for HCV patients with prior DAA failure; contextualises HBV/HCV co-infection burden in low-income settings where daclatasvir is most accessible |
| [40578045](https://pubmed.ncbi.nlm.nih.gov/40578045/) | 2025 | Observational | Int J Drug Policy | Decentralized point-of-service model integrating HBV, HCV, and HIV prevention in people who inject drugs in South Africa; illustrates the real-world epidemiological overlap requiring coordinated management of these co-infections |

---

## India Market Information

Daclatasvir (DrugBank ID: DB09102) currently has **no registered products in India**. It has not received CDSCO approval and is not commercially available through domestic market channels. The drug is approved in other jurisdictions — including as Daklinza® in the EU, USA, and Japan — exclusively for the treatment of chronic HCV infection, typically in combination with sofosbuvir.

---

## Safety Considerations

**Drug Interactions** (89 interactions documented; key interactions shown below):

| Interacting Drug | Severity | Category |
|----------------|----------|---------|
| Dexamethasone | **Major** | Corticosteroid; CYP3A4 inducer — may significantly reduce daclatasvir exposure |
| Clarithromycin | **Major** | Strong CYP3A4 inhibitor — may substantially increase daclatasvir plasma levels |
| Eluxadoline | **Major** | Gastrointestinal agent; co-administration not recommended |
| Cobicistat | **Major** | CYP3A4 inhibitor used in HIV regimens — requires daclatasvir dose reduction to 30 mg QD |
| Rosuvastatin | Moderate | Statin; increased plasma exposure risk — monitor for myopathy |
| Simvastatin | Moderate | Statin; elevated exposure risk — consider dose reduction |
| Metformin | Moderate | Antidiabetic; potential interaction via organic cation transporter (OCT) pathways |
| Apixaban | Moderate | Direct oral anticoagulant — monitor anticoagulation parameters |
| Rifaximin | Moderate | Non-absorbed antibiotic; potential PK interaction |
| Aprepitant | Moderate | NK1 antagonist / CYP3A4 modulator — may alter daclatasvir exposure |

> Detailed prescribing warnings and contraindications specific to Indian regulatory labelling are not currently available. Please refer to the EMA or FDA-approved package insert for comprehensive safety guidance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Daclatasvir's NS5A inhibition mechanism has no known direct pharmacological activity against HBV — a DNA virus with fundamentally different replication machinery — and the only clinically relevant trial in HCV/HBV co-infection (NCT02555943, n=23) was designed to detect HBV reactivation risk, not to treat HBV. Published case reports document HBV reactivation as a safety concern during daclatasvir therapy, making a therapeutic benefit claim unjustifiable without dedicated in vitro and in vivo anti-HBV efficacy data.

**To proceed, the following is needed:**

- **MOA clarification (DG002):** Obtain full DrugBank pharmacology data confirming whether any known off-target activity could plausibly affect HBV replication
- **Regulatory safety data (DG001):** Download and parse the CDSCO/FDA prescribing information to complete the S1 safety screening gate
- **In vitro HBV activity data:** Commission a cell-based HBV replication assay (e.g., HepAD38 or HepG2.2.15) to determine whether daclatasvir has any measurable anti-HBV effect at clinically achievable concentrations
- **Mechanistic hypothesis revision:** If pursuing the co-infection angle, reframe the hypothesis around optimised HCV/HBV co-infection management protocols rather than direct HBV antiviral activity
- **Dedicated Phase 2 RCT design:** If in vitro data proves positive, design a small proof-of-concept trial in HCV/HBV co-infected patients with explicit dual HBV and HCV virological endpoints
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

