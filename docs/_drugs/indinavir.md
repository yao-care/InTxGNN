---
layout: default
title: Indinavir
parent: 僅模型預測 (L5)
nav_order: 330
evidence_level: L5
indication_count: 7
---

# Indinavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Indinavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Indinavir (Crixivan) is an HIV-1 protease inhibitor originally developed for treating HIV-1 infection as part of combination antiretroviral therapy (HAART).
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**, with **0 clinical trials** and **12 publications** currently supporting this direction — all derived exclusively from non-human primate animal models.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (combination antiretroviral therapy) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Indinavir is a competitive inhibitor of the HIV-1 aspartyl protease. It binds the enzyme's active site and prevents cleavage of Gag-Pol polyprotein precursors into functional structural proteins, thereby blocking the maturation of infectious viral particles.

SIV (Simian Immunodeficiency Virus) is a lentivirus closely related to HIV-1, and its protease shares significant structural homology with the HIV-1 enzyme. This is the mechanistic foundation for the TxGNN prediction. In vitro data (PMID 12709355) directly confirmed that Indinavir inhibits SIVmac239 with an EC₅₀ of 39 ± 8 nM — comparable to its activity against HIV-1 (EC₅₀ 66 ± 4 nM). PMID 15040537 further demonstrated measurable activity against additional SIV strains (SIVmac251, SIVb670). Primate HAART studies (PMID 20868521, 19240457) showed that Indinavir-containing regimens reduce tissue viral load and prevent vaginal SIV transmission in macaques.

A critical limitation must be noted: SIV infection is an animal disease affecting non-human primates and does not occur in humans. The clinical relevance of this prediction is therefore confined to veterinary or preclinical research contexts, not human drug repurposing. All 12 supporting publications use macaque models exclusively, and no human clinical trials exist for this indication.

## Clinical Trial Evidence

Currently no related clinical trials registered for Indinavir in simian immunodeficiency virus infection.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro / Animal | Antimicrobial Agents and Chemotherapy | Direct susceptibility comparison of SIV and HIV-1 to protease inhibitors; Indinavir inhibited SIVmac239 at EC₅₀ 39 nM vs 66 nM for HIV-1 |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro | Antiviral Therapy | Evaluated 16 approved antiretrovirals against HIV-2, SIV, and SHIV; Indinavir showed activity against SIVmac251 and SIVb670 strains |
| [19240457](https://pubmed.ncbi.nlm.nih.gov/19240457/) | 2009 | Animal Study | AIDS | Post-exposure prophylaxis with ZDV + 3TC + Indinavir prevented vaginal SIV transmission in macaques |
| [20868521](https://pubmed.ncbi.nlm.nih.gov/20868521/) | 2010 | Animal Study | Retrovirology | Short-term HAART including Indinavir reduced SIV tissue viral load in macaques; efficacy was dependent on timing of initiation after infection |
| [11507214](https://pubmed.ncbi.nlm.nih.gov/11507214/) | 2001 | Animal Study | Journal of Virology | Indinavir-containing HAART restored Mycobacterium-specific T-cell immunity and controlled fatal TB-like disease in SIV/BCG co-infected macaques |
| [15378436](https://pubmed.ncbi.nlm.nih.gov/15378436/) | 2004 | Animal Study | Journal of Infectious Diseases | Tenofovir + Indinavir treatment in SIV-infected macaques enabled recovery of Vγ2Vδ2+ T cell responses during active mycobacterial co-infection |
| [12804006](https://pubmed.ncbi.nlm.nih.gov/12804006/) | 2003 | Mechanistic Study | AIDS Research and Human Retroviruses | HAART (ZDV + 3TC + Indinavir) modulated P-glycoprotein and cellular kinase expression at the transcriptional level in SIV-infected macaques |
| [11689641](https://pubmed.ncbi.nlm.nih.gov/11689641/) | 2001 | Animal Study | Journal of Virology | Bone marrow hematopoiesis defects in SHIV-infected macaques persisted despite HAART reducing viremia, suggesting early and persistent immune damage |
| [14610172](https://pubmed.ncbi.nlm.nih.gov/14610172/) | 2003 | Animal Study | Journal of Virology | Short-term post-exposure HAART (AZT + 3TC + Indinavir) modulated lymphocyte proliferation kinetics during primary SIVmac251 infection |
| [22615988](https://pubmed.ncbi.nlm.nih.gov/22615988/) | 2012 | Animal Study | PLoS One | HAART including Indinavir, initiated during chronic SIV stage or shortly post-exposure, reduced viral load in male genital organs |

## India Market Information

Indinavir is not currently marketed in India. No regulatory licenses or approved products are on record with CDSCO.

## Safety Considerations

**Drug Interactions**: Indinavir has **229 documented drug interactions** (source: DDInter). Key interactions include:

- **Major interactions** (require contraindication or close monitoring): Loperamide, Triamcinolone, Budesonide
- **Moderate interactions** (monitor carefully): Omeprazole, Rabeprazole, Dexamethasone, Hydrocortisone, Betamethasone, Budesonide (nasal), Metformin, Canagliflozin, Alogliptin, Acarbose, Alogliptin, Aprepitant, Chlorpropamide, Alosetron

The exceptionally broad DDI profile (229 interactions) — particularly with corticosteroids, proton pump inhibitors, and antidiabetic agents — represents a major clinical management challenge and demands thorough medication reconciliation in any treatment setting.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction is mechanistically plausible — Indinavir inhibits SIV protease in vitro with potency comparable to HIV-1 — but SIV is an animal disease with no human clinical application. This indication is a research model, not a viable human repurposing target. Furthermore, Indinavir is not marketed in India (0 registrations), and all available evidence is preclinical (L4), making it unsuitable for clinical advancement in this direction.

**To proceed, the following is needed:**
- Redirect evaluation to clinically actionable human HIV-spectrum indications: **Congenital HIV** (rank 5, L1 evidence, 9 clinical trials including Phase IV) and **AIDS Related Complex** (rank 6, L2 evidence, 6 trials + 11 publications) are substantially stronger repurposing candidates
- Obtain mechanism of action data from DrugBank (Data Gap DG002) to support mechanistic narrative for human HIV indications
- Retrieve full prescribing information and package insert warnings (Data Gap DG001) to assess the safety profile against the 229 DDIs
- If SIV research use is the intent (non-human primate model), no further regulatory approval is needed — proceed with the existing animal study evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

