---
layout: default
title: Entecavir
parent: 僅模型預測 (L5)
nav_order: 271
evidence_level: L5
indication_count: 10
---

# Entecavir
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

# Entecavir: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir is a potent guanosine nucleoside analogue globally approved since 2005 as a first-line treatment for chronic hepatitis B virus (HBV) infection.
The TxGNN model predicts it may be effective for **Chronic Hepatitis C Virus Infection** with a score of **99.98%**;
however, the retrieved evidence — spanning **35+ clinical trials** and **20 publications** — consistently reflects HBV/HCV co-infection management contexts rather than direct anti-HCV efficacy, supporting a **Hold** decision at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic hepatitis B virus (HBV) infection (FDA-approved 2005; not registered in India per available data) |
| Predicted New Indication | Chronic Hepatitis C Virus Infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on published pharmacological literature, Entecavir acts as a selective inhibitor of HBV DNA polymerase/reverse transcriptase. Once intracellularly phosphorylated to its active triphosphate form (ETV-TP), it blocks three critical steps of HBV replication: priming of the viral polymerase, DNA-dependent DNA synthesis, and RNase H-mediated degradation of pregenomic RNA. Its potency (IC₅₀) against HBV polymerase far exceeds that of older nucleoside analogues such as lamivudine, and its high genetic barrier to resistance has made it a cornerstone of chronic HBV therapy.

The TxGNN prediction of activity against chronic HCV likely originates from the knowledge graph's recognition that HBV and HCV share overlapping disease nodes — both cause chronic viral hepatitis, liver cirrhosis, and hepatocellular carcinoma risk — and that nucleoside/nucleotide analogues as a drug class have demonstrated broad antiviral activity across related viral families. The model may also have learned from the frequent co-occurrence of HBV and HCV in clinical trial populations and literature, reinforcing a spurious mechanistic linkage.

However, the mechanistic basis for genuine ETV activity against HCV is critically weak. HCV is a positive-sense, single-stranded RNA virus that replicates exclusively through its NS5B RNA-dependent RNA polymerase (RdRp) — a structurally and functionally distinct enzyme from HBV's DNA-dependent DNA polymerase/reverse transcriptase. ETV-TP has no known inhibitory activity against HCV NS5B. Every co-infection trial in the data set uses ETV strictly to manage the HBV component while approved direct-acting antivirals (DAAs) address HCV. There are no human data supporting independent anti-HCV efficacy for Entecavir.

---

## Clinical Trial Evidence

> The trials retrieved are predominantly HBV-specific studies or HBV/HCV co-infection trials where ETV serves as the HBV management agent. No trial directly evaluates Entecavir as a treatment for hepatitis C virus infection. The most contextually relevant trials are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | N/A | Unknown | 60 | Randomized, three-arm, active-controlled study investigating whether prophylactic nucleoside analogue (including ETV) started at initiation of DAA therapy prevents clinical HBV reactivation in HCV/HBV co-infected patients receiving DAA for chronic hepatitis C. ETV role is HBV prophylaxis, not anti-HCV treatment. |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study of DAA agents for HCV/HBV co-infection; determines incidence, morbidity, and predisposing factors for HBV reactivation during direct anti-HCV treatment. ETV is used to manage the HBV component and is not evaluated for anti-HCV activity. |
| [NCT03272009](https://clinicaltrials.gov/study/NCT03272009) | Phase 1 | Completed | 73 | Randomized, double-blind, placebo-controlled study of FXR-agonist EYP001a (a bile-acid receptor modulator) in chronically HBV-infected subjects. Safety/tolerability/PK/PD focus; not an HCV efficacy evaluation. |
| [NCT01037166](https://clinicaltrials.gov/study/NCT01037166) | Phase 2 | Completed | 84 | Japanese Phase 2 study assessing ETV safety and antiviral activity in CHB patients with incomplete response to lamivudine. Entirely HBV-specific; no HCV component. |
| [NCT04157257](https://clinicaltrials.gov/study/NCT04157257) | Phase 2 | Unknown | 60 | Open-label multicenter study of QL-007 tablets combined with ETV or tenofovir in CHB patients previously on nucleoside therapy. ETV serves as a HBV-protective backbone; HCV activity is not assessed. |
| [NCT01925820](https://clinicaltrials.gov/study/NCT01925820) | Phase 4 | Unknown | 540 | Three-arm comparison: Pegasys + ETV vs ETV alone vs Pegasys alone in HBeAg-negative CHB. A pure HBV outcomes trial. |
| [NCT01022801](https://clinicaltrials.gov/study/NCT01022801) | Phase 2 | Completed | 120 | Japanese Phase 2 dose-response study of ETV vs lamivudine in CHB patients, measured by HBV DNA at Week 22. HBV head-to-head; no HCV relevance. |
| [NCT06566248](https://clinicaltrials.gov/study/NCT06566248) | Phase 2a | Recruiting | 90 | Double-blind, placebo-controlled Phase IIa trial of TQA3810 tablets combined or uncombined with nucleoside analogues in CHB patients. HBV-focused based on study context. |
| [NCT01018381](https://clinicaltrials.gov/study/NCT01018381) | N/A | Completed | 130 | Randomized clinical study of arabinoxylan rice bran (MGN-3/Biobran) for HCC, HBV, and HCV. Marginal ETV relevance; no direct anti-HCV evaluation of ETV. |
| [NCT03662568](https://clinicaltrials.gov/study/NCT03662568) | Phase 1 | Completed | 56 | Open-label drug-drug interaction study of Morphothiadine Mesilate/Ritonavir combined with ETV or TDF in healthy subjects. Pharmacokinetics focus; no HCV efficacy assessment. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | Evaluated HCV reactivation in 66 anti-HCV antibody-positive CHB patients receiving nucleoside analogue (NUC) therapies including ETV. At baseline, all had detectable HCV RNA. NUC therapy (for HBV) did not eradicate HCV — HCV evolved independently, underscoring mechanistic separation between ETV and HCV. |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opinion on Pharmacotherapy | Comprehensive review of HBV/HCV co-infection treatment advances. Authors recommend ETV or tenofovir for the HBV component and IFN-based or DAA regimens for HCV. No overlap in drug activity is described. |
| [28487602](https://pubmed.ncbi.nlm.nih.gov/28487602/) | 2017 | Review | World Journal of Gastroenterology | Review of HBV infection and alcohol consumption in the context of HCC. Notes that DAA era has largely resolved HCV-driven HCC; HBV (managed with ETV/TDF) remains the leading unmet need. |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wiener Medizinische Wochenschrift | Treatment overview of chronic HBV and HCV. PegIFN/NUC for HBV; IFN + ribavirin for HCV. Drug class separation explicitly stated. |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterologica e Dietologica | Antiviral medications for HBV and HCV and their effects on kidney function. ETV classified as HBV-specific; HCV agents (boceprevir, telaprevir era) classified separately. |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Review | Clinics and Research in Hepatology and Gastroenterology | Management of viral hepatitis B and C in children. Distinct therapeutic approaches confirmed: NUC analogues for HBV; DAAs under evaluation for paediatric HCV. |
| [21497740](https://pubmed.ncbi.nlm.nih.gov/21497740/) | 2011 | Review | Best Practice & Research Clinical Gastroenterology | Fibrosis in chronic viral hepatitis. ETV/NUC therapy shown to reduce HBV-driven fibrosis; IFN-based regimens for HCV fibrosis. No shared mechanism described. |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | Review | World Journal of Hepatology | Management of HBV and HCV before and after liver/kidney transplantation. ETV/tenofovir for HBV recurrence prevention; distinct DAA protocols for HCV. Highlights renal dose adjustment requirements for ETV. |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Review | Clinics and Research in Hepatology and Gastroenterology | HBV/HCV co-infection as a therapeutic challenge; includes a case report of a co-infected patient requiring dual antiviral strategies — HBV and HCV treated with separate drug classes. |
| [39351520](https://pubmed.ncbi.nlm.nih.gov/39351520/) | 2024 | Review | World Journal of Hepatology | Metabolomics in liver disease. Provides background context on chronic viral hepatitis; does not contribute direct evidence for ETV anti-HCV activity. |

---

## India Market Information

Entecavir is **not currently registered** in India based on the data in this Evidence Pack (`market_status: "未上市"`, `total_licenses: 0`). No license authorization records are available to display.

> **Note**: Entecavir (brand name Baraclude®, Bristol-Myers Squibb) holds regulatory approvals in multiple major markets including the United States (FDA, 2005), the European Union (EMA), Japan (PMDA), and China (NMPA) for chronic HBV infection. Independent verification with the **Central Drugs Standard Control Organisation (CDSCO)** of India is strongly recommended to confirm current registration status, as market data gaps may reflect a data retrieval limitation rather than a definitive regulatory absence.

---

## Safety Considerations

**Drug Interactions**: Entecavir has **44 documented drug interactions**, all classified as **Moderate severity**, identified via the DDInter database. Key interaction categories include:

- **H2 receptor antagonists** (Famotidine, Ranitidine, Cimetidine, Ranitidine bismuth citrate): May compete with ETV for renal tubular secretion via organic cation transporters, potentially increasing ETV plasma concentrations.
- **Nephrotoxic antibiotics** (Vancomycin, Kanamycin, Neomycin, Polymyxin B, Levofloxacin, Amoxicillin): Shared renal elimination pathways may compound tubular secretion burden or nephrotoxicity risk.
- **Antifungals** (Amphotericin B — standard, lipid complex, liposomal, and cholesteryl sulfate formulations): Concurrent nephrotoxic potential; caution warranted in patients with pre-existing renal impairment.
- **5-ASA derivatives** (Mesalazine, Balsalazide, Olsalazine, Sulfasalazine): Moderate interactions likely via renal organic anion/cation transport competition.
- **Metformin**: Competing renal organic cation transporter (OCT2/MATE) substrates; co-administration may alter plasma levels of either drug.
- **Orlistat**: Moderate interaction; mechanism and clinical significance require monitoring.

> Key warnings and contraindications were not available in the current Evidence Pack (classified as Blocking data gap DG001). Please refer to the Entecavir package insert (Baraclude® SmPC or FDA label) for complete prescribing information, including warnings regarding lactic acidosis risk in patients with severe hepatic decompensation and renal dose adjustment requirements.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Entecavir's mechanism of action — selective inhibition of HBV DNA polymerase/reverse transcriptase — is fundamentally incompatible with the HCV replication machinery (NS5B RNA-dependent RNA polymerase). Every piece of clinical evidence in this data set places ETV in the role of HBV management within HBV/HCV co-infection contexts; no human data support independent anti-HCV efficacy. The high TxGNN prediction score (99.98%) most likely reflects knowledge graph topology proximity between hepatitis disease nodes rather than genuine pharmacological activity against HCV.

**To proceed, the following would be required:**

- Independent **in vitro virology studies** demonstrating ETV or ETV-TP inhibition of HCV NS5B RdRp at clinically achievable concentrations
- A plausible **mechanistic explanation** for how a DNA polymerase inhibitor could suppress an RNA virus replicase
- Resolution of **data gaps**: retrieval of MOA documentation (DG002), package insert warnings and contraindications (DG001), and CDSCO registration status for India
- If any preclinical anti-HCV signal is identified, a **dedicated Phase 1/2 clinical trial** in HCV mono-infected patients would be required before further development — HBV/HCV co-infection trials cannot substitute as efficacy evidence for this indication

> **Disclosure**: This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

