---
layout: default
title: Lamivudine
parent: 僅模型預測 (L5)
nav_order: 367
evidence_level: L5
indication_count: 5
---

# Lamivudine
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

# Lamivudine: From HIV/Hepatitis B to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Lamivudine (3TC) is a nucleoside reverse transcriptase inhibitor (NRTI) with internationally established efficacy against HIV-1 and chronic Hepatitis B virus (HBV), though it is currently not registered or marketed in India.
The TxGNN model predicts **Simian Immunodeficiency Virus (SIV) Infection** as its top new indication with a score of **99.93%**, supported by **0 clinical trials** and **20 publications**; however, the literature exclusively describes non-human primate animal model research and does not constitute a conventional human repurposing indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in India; internationally approved for HIV-1 infection and Chronic Hepatitis B |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 (Preclinical / Animal Model Research) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on well-established pharmacology, Lamivudine (3TC) is a synthetic cytidine nucleoside analogue NRTI. Its active intracellular triphosphate form (3TC-TP) competes with natural deoxycytidine triphosphate (dCTP) for incorporation into the viral DNA chain by reverse transcriptase (RT). Once incorporated, 3TC-TP lacks the 3'-hydroxyl group required for further chain elongation, thereby terminating reverse transcription — the critical step by which retroviruses convert their RNA genome into proviral DNA. This mechanism is active against both HIV-1 reverse transcriptase and the HBV DNA polymerase.

SIV belongs to the same *Lentivirus* genus as HIV, and the two viruses share highly conserved reverse transcriptase tertiary structures — including the polymerase active site and the dNTP-binding pocket targeted by Lamivudine. This mechanistic conservation explains why Lamivudine demonstrates measurable anti-SIV activity in vitro and in non-human primate models. Notably, the M184V resistance mutation (methionine-to-valine substitution at codon 184 of RT) — which is the hallmark of Lamivudine resistance in HIV-1 — has been reproducibly demonstrated to emerge in SIVmac251-infected macaques treated with 3TC, providing direct molecular evidence that Lamivudine acts on the same RT active site in SIV as in HIV.

**Critical limitation:** SIV is a pathogen exclusive to non-human primates; it does not cause human disease. This "indication" therefore represents animal model research rather than a genuine human clinical repurposing target. The TxGNN knowledge graph prediction likely reflects the deep biological homology between SIV and HIV nodes within the graph, generating a high association score by mechanistic proximity rather than identifying an unmet human medical need. This finding should not be pursued as a human drug repurposing candidate under conventional regulatory frameworks.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Lamivudine in Simian Immunodeficiency Virus infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [19240457](https://pubmed.ncbi.nlm.nih.gov/19240457/) | 2009 | Animal Study | AIDS | ZDV + Lamivudine + Indinavir post-exposure prophylaxis after vaginal SIV exposure in macaques; demonstrated reduction in SIV transmission risk |
| [12021341](https://pubmed.ncbi.nlm.nih.gov/12021341/) | 2002 | Animal / Resistance | J. Virology | M184V resistance mutation emerged within 5 weeks in SIVmac251-infected neonatal macaques treated with Lamivudine, mirroring HIV-1 clinical resistance patterns |
| [12502828](https://pubmed.ncbi.nlm.nih.gov/12502828/) | 2003 | Animal / Resistance | J. Virology | M184V in SIV reverts under Tenofovir pressure even in presence of Lamivudine; demonstrates shared RT active site between SIV and HIV |
| [15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/) | 2005 | Animal Study | J. Virology | Efavirenz + Lamivudine + Tenofovir HAART suppressed RT-SHIV plasma RNA by >2 log₁₀ in all 7 treated macaques |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal Study | J. Virology | Quadruple antiretroviral therapy (including Lamivudine) produced rapid SIVmac251 viral decay in macaques with kinetics comparable to HIV-1 mathematical models |
| [14610172](https://pubmed.ncbi.nlm.nih.gov/14610172/) | 2003 | Animal Study | J. Virology | Short-term HAART (AZT + Lamivudine + Indinavir) initiated 4 hours post-SIVmac251 inoculation suppressed viremia and altered lymphocyte proliferation kinetics |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In Vitro / Animal | Antiviral Therapy | Systematic evaluation of 16 approved antiretrovirals against HIV-2, SIVmac251, SIV-B670, and SHIV; Lamivudine confirmed active against multiple SIV strains |
| [20868521](https://pubmed.ncbi.nlm.nih.gov/20868521/) | 2010 | Animal Study | Retrovirology | Short-term HAART effect on SIV tissue reservoirs in macaques depends on timing of initiation and antiviral tissue diffusion; Lamivudine part of study regimen |
| [22615988](https://pubmed.ncbi.nlm.nih.gov/22615988/) | 2012 | Animal Study | PLoS ONE | HAART (including Lamivudine) reduced SIV replication in male genital organs; persistent low-level shedding from tissue sanctuaries identified |
| [11689641](https://pubmed.ncbi.nlm.nih.gov/11689641/) | 2001 | Animal Study | J. Virology | SHIV-infected macaques receiving HAART (including Lamivudine) showed persistent bone marrow hematopoiesis defects despite efficient viral suppression — paralleling HIV observations |

---

## India Market Information

Lamivudine currently has **no registered products** in India under the CDSCO registry. No product authorization data is available.

> **Note:** Lamivudine (3TC) is widely approved and marketed internationally — including in the United States (FDA: Epivir®), European Union (EMA), and numerous Asia-Pacific markets — for HIV-1 infection and chronic Hepatitis B. The absence of India registration data in this dataset may reflect a data collection gap rather than confirmed market absence. Independent verification through the CDSCO online database is recommended.

---

## Safety Considerations

**Drug Interactions:** Based on DDInter database analysis, Lamivudine has **145 identified interactions** across 145 drug pairs.

*Moderate-severity interactions (monitoring or management required):*

| Interacting Drug | Severity | Clinical Note |
|-----------------|----------|---------------|
| Lactitol | Moderate | Monitor for altered Lamivudine exposure |
| Mannitol | Moderate | Monitor for altered Lamivudine exposure |
| Naltrexone | Moderate | Combination may require clinical monitoring |
| Orlistat | Moderate | Orlistat may reduce oral bioavailability of Lamivudine |
| Sorbitol | Moderate | Sorbitol co-administration reduces Lamivudine absorption |

*Interactions with uncharacterised severity (Unknown level):* Calcitriol, Vitamin A, Glimepiride, Clotrimazole, Cimetidine, Amphotericin B, Pantoprazole, Mesalazine, Morphine, Metformin, Omeprazole, Sucralfate, Rosiglitazone, Lansoprazole, Vancomycin, and 130 additional interactions. Please refer to the complete DDInter report for full details.

Please refer to the official package insert for warnings and contraindications, which could not be retrieved in this data pull (Data Gap DG001 — CDSCO labelling not yet obtained).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
SIV is a non-human primate pathogen with no established human disease burden; it therefore cannot serve as a valid human drug repurposing target under conventional clinical development or regulatory frameworks. While the mechanistic rationale for Lamivudine's anti-SIV activity is scientifically well-founded (conserved lentivirus reverse transcriptase active site), the TxGNN high prediction score reflects graph-level biological similarity between SIV and HIV rather than an actionable human clinical indication gap. No human clinical trials exist for this indication, and none would be ethically or scientifically justified in this context.

**To proceed, the following is needed:**

- **Reframe the repurposing scope:** If the goal is human repurposing, redirect analysis to more clinically relevant TxGNN predictions — particularly **Chronic Hepatitis C** (Rank #5, L3 evidence, though mechanistic caveats apply regarding NS5B vs. RT activity differences) and the **neurodevelopmental interferon disorder** (Rank #3, L5, theoretical basis via NRTI suppression of LINE-1 retroelement activity in cGAS-STING pathway diseases such as Aicardi-Goutières Syndrome)
- **Resolve DG001 (Blocking):** Download and parse CDSCO/India package insert PDF to obtain approved warnings and contraindications before any safety evaluation stage
- **Resolve DG002 (High):** Query DrugBank API for Lamivudine MOA, pharmacodynamics, and toxicity categories to support mechanistic analysis
- **Verify India market status:** Conduct direct CDSCO registry query to confirm whether Lamivudine products (e.g., generic 3TC formulations) are available in India under local brand names not captured in this dataset
- **Exclude obsolete/invalid predictions:** Rank #4 ("obsolete familial combined hyperlipidemia") should be removed from further evaluation due to both the deprecated disease classification and the absence of any mechanistic rationale linking NRTI pharmacology to lipid metabolism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

