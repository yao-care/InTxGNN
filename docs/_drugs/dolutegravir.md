---
layout: default
title: Dolutegravir
parent: 僅模型預測 (L5)
nav_order: 256
evidence_level: L5
indication_count: 3
---

# Dolutegravir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Dolutegravir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Dolutegravir is a second-generation integrase strand transfer inhibitor (INSTI) used globally for HIV-1 infection treatment in adults and children.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**,
with **1 clinical trial** and **15 publications** currently supporting this research direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 Infection (globally approved; not yet registered in India) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Dolutegravir belongs to the integrase strand transfer inhibitor (INSTI) class of antiretrovirals. It exerts its antiviral effect by blocking the HIV integrase enzyme, which is essential for inserting viral DNA into the host cell genome — a step required for productive viral replication. Second-generation INSTIs such as Dolutegravir are distinguished by their slow dissociation kinetics from the integrase-DNA complex, conferring a high genetic barrier to resistance.

SIV and HIV both belong to the *Lentivirus* genus within *Retroviridae* and share a high degree of integrase complex structural homology. This mechanistic overlap directly supports the biological rationale for Dolutegravir's activity against SIV. Multiple published studies have demonstrated that Dolutegravir exerts measurable selective pressure on SIV integrase in vivo, generating resistance mutation profiles (e.g., E92Q, G118R) closely analogous to those observed in HIV-1 — directly confirming drug-target engagement in the SIV system and validating SIV non-human primate (NHP) models as reliable pharmacological surrogates for HIV drug development.

It should be noted that this predicted indication represents a veterinary and animal model application rather than a conventional human clinical repurposing target. The primary scientific value lies in two areas: (1) validating SIV-NHP models for HIV resistance and eradication research, and (2) providing antiretroviral treatment for SIV-infected captive primates (e.g., chimpanzees, macaques) for animal welfare purposes. The 2017 case report of successful SIVcpz treatment in a captive chimpanzee illustrates this real-world veterinary application.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Vedolizumab combined with ART (including INSTI) in HIV-infected subjects seeking virological remission off-ART; indirectly supports INSTI-based ART use in lentiviral infection management, but study likely did not complete enrollment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30381490](https://pubmed.ncbi.nlm.nih.gov/30381490/) | 2019 | Animal In Vivo Study | J Virology | DTG monotherapy in SIV-infected macaques selected E92Q/G118R resistance mutations with variable virological outcomes, directly confirming DTG-SIV integrase interaction in vivo |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Animal Comparative Study | AIDS Res Hum Retroviruses | Injectable cART including DTG (FTC+TDF+DTG) suppressed SIVmac239 replication in rhesus macaques to clinically relevant levels, establishing NHP cART model |
| [36365101](https://pubmed.ncbi.nlm.nih.gov/36365101/) | 2022 | Animal Long-term Pharmacological Study | Pharmaceutics | Pharmacological validation of long-term TDF+FTC+DTG in SIVmac251-infected NHPs; confirmed appropriate PK profiles and sustained virological suppression |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | In Vitro / Animal Study | J Virology | Comprehensive INSTI resistance profiling in SIVmac239; same drug resistance mutations produce similar phenotypes in SIV and HIV, validating SIV as a resistance model |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Animal Translational Study | mBio | Despite effective cART including DTG, lentiviral reservoirs persist in brain microglia and macrophages; SIV-NHP model parallels CNS reservoir dynamics in humans with HIV |
| [32166319](https://pubmed.ncbi.nlm.nih.gov/32166319/) | 2020 | In Vitro / Animal Safety Study | Clin Infect Dis | DTG and Raltegravir promote pro-adipogenic and profibrotic effects and induce insulin resistance in human and simian adipose tissue; key metabolic safety signal for long-term INSTI use |
| [31619550](https://pubmed.ncbi.nlm.nih.gov/31619550/) | 2019 | In Vitro Mechanistic Study | J Virology | Wnt/β-Catenin pathway modulation reduces long-lived memory CD4+ T cell proliferation in ART-suppressed SIV-infected macaques; mechanistic insight into viral reservoir maintenance |
| [28576126](https://pubmed.ncbi.nlm.nih.gov/28576126/) | 2017 | Veterinary Case Report | Retrovirology | Successful antiretroviral treatment of SIVcpz-induced immunodeficiency in a captive chimpanzee; direct demonstration of INSTI-based regimen feasibility in NHP veterinary care |
| [40093003](https://pubmed.ncbi.nlm.nih.gov/40093003/) | 2025 | Animal Study | Front Immunol | FTC+TDF+DTG cART in rhesus macaques modulated CNS extracellular free water and white matter tract deficits associated with SIV infection; neuroimaging evidence of treatment benefit |
| [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/) | 2021 | Structural Biology / Review | FEBS Journal | X-ray crystal structures of HIV/SIV intasome complexes elucidate the molecular basis of second-generation INSTI (DTG, bictegravir) binding and their high genetic barrier to resistance |

---

## Safety Considerations

**Drug Interactions:** A total of 62 drug-drug interactions have been identified (source: DDInter). Key concerns are summarised below.

**Major Interactions — Polyvalent Cation Chelation:**
Dolutegravir absorption is significantly reduced by polyvalent cation-containing products. The following agents all carry **Major** interaction ratings and must be carefully timed relative to Dolutegravir administration:

| Category | Agents |
|----------|--------|
| Antacids / Buffers | Aluminum hydroxide, Magaldrate, Magnesium carbonate, Magnesium chloride, Magnesium citrate, Magnesium phosphate |
| Calcium supplements | Calcium acetate, Calcium carbonate, Calcium citrate, Calcium glubionate, Calcium gluconate, Calcium lactate, Calcium phosphate |
| Adsorbents | Attapulgite, Kaolin |
| Iron supplements | Iron (all oral forms) |

> ⚠️ **Clinical implication:** Dolutegravir should be administered at least 2 hours before or 6 hours after these agents. If separation is not possible, Dolutegravir may be taken simultaneously with food when combined with calcium or iron supplements.

**Minor Interactions:** Aprepitant, Cimetidine, Clarithromycin, Clotrimazole, Dexamethasone — monitor for modest pharmacokinetic interactions; dose adjustment typically not required.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dolutegravir's mechanism of HIV integrase inhibition is directly applicable to SIV given the high structural and sequence homology between HIV and SIV integrase complexes. Multiple peer-reviewed animal studies confirm drug-target engagement, characterised resistance mutation patterns, and measurable virological suppression in NHP models. However, this application is primarily veterinary and scientific (NHP research model and captive primate welfare) rather than a conventional human clinical drug repurposing pathway, which limits its immediate translational impact.

**To proceed, the following is needed:**
- Species-specific pharmacokinetic studies to establish appropriate dosing regimens across target NHP species (rhesus macaques, chimpanzees)
- Formal EC₅₀ characterisation of Dolutegravir against purified SIV integrase and against FIV integrase (for feline indication), compared directly to HIV integrase
- Detailed MOA data retrieval from DrugBank (DB08930) to complete mechanistic documentation
- Long-term safety monitoring plan addressing INSTI-class metabolic effects (weight gain, insulin resistance, adipose tissue changes) in the NHP context
- Regulatory pathway assessment: veterinary drug approval versus compassionate/off-label use in captive primate programmes
- TFDA/CDSCO package insert review to fill the current Blocking data gap on approved warnings and contraindications before any clinical translation is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

