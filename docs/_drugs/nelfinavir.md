---
layout: default
title: Nelfinavir
parent: 僅模型預測 (L5)
nav_order: 477
evidence_level: L5
indication_count: 4
---

# Nelfinavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Nelfinavir: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Nelfinavir is an HIV protease inhibitor, globally approved for treatment of HIV-1 infection as part of combination antiretroviral therapy, though it carries no current registration in India.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**,
supported by **0 clinical trials** and **4 preclinical/in vitro publications**.
Critically, SIV infection is a non-human primate research model rather than a human clinical indication, which fundamentally limits the translational and clinical development value of this prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (combination antiretroviral therapy; no India registration on record) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Nelfinavir is a competitive inhibitor of the HIV-1 aspartyl protease — an enzyme that cleaves the gag-pol polyprotein precursor into functional structural and replicative proteins. Inhibiting this step produces immature, non-infectious viral particles, effectively halting viral maturation. This mechanism of action is well-established in the HIV literature, though detailed MOA data was not available in the current Evidence Pack (Data Gap DG002).

SIV (Simian Immunodeficiency Virus) and HIV share the same genus *Lentivirus* within the primate lentivirus group. Their protease enzymes share conserved catalytic residues (the Asp-Thr-Gly triad) and nearly identical three-dimensional architecture, providing a credible theoretical basis for cross-species inhibitory activity. PMID 15040537 directly evaluated 16 approved antiretroviral drugs — spanning multiple drug classes including protease inhibitors — against HIV-2, SIV mac251/B670, and SHIV strains in vitro, making it the most directly relevant piece of evidence in this set.

However, the clinical translation value of this prediction is fundamentally constrained: SIV infection exists exclusively as a non-human primate experimental model for studying HIV pathogenesis and evaluating therapies. It is not an independent human disease indication. Any repurposing signal here is confined to basic science validation and pre-clinical utility, not a novel therapeutic opportunity for human patients. The high TxGNN score (0.9994) likely reflects the close ontological proximity of HIV ↔ SIV nodes in the knowledge graph rather than an independent pharmacological prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro susceptibility study | Antiviral Therapy | Evaluated 16 approved antiretroviral drugs (including protease inhibitor class) against HIV-2, SIV mac251/B670, and SHIV in cell culture; most directly relevant to cross-species activity of nelfinavir |
| [11507214](https://pubmed.ncbi.nlm.nih.gov/11507214/) | 2001 | Cohort / immunology study | Journal of Virology | Antiretroviral therapy (including protease inhibitors) restored Mycobacterium-specific T-cell immunity in SIV/BCG-coinfected macaques; demonstrates in vivo proof-of-concept in SIV animal model |
| [12234864](https://pubmed.ncbi.nlm.nih.gov/12234864/) | 2002 | In vitro mechanistic study | Antimicrobial Agents and Chemotherapy | Diketo derivative integrase inhibitors tested against HIV-1, HIV-2, and SIV mac251; nelfinavir used as a comparator in subsynergistic combinations — indirect relevance |
| [12176326](https://pubmed.ncbi.nlm.nih.gov/12176326/) | 2002 | In vitro mechanistic study | Current Biology | Novel HIV integrase inhibitor class assessed in cell culture; nelfinavir mentioned tangentially as combination partner — minimal direct relevance to SIV activity |

---

## India Market Information

Nelfinavir currently has no registered products in India. No authorization records are available in the regulatory database.

---

## Safety Considerations

**Drug Interactions**: Nelfinavir has **254** documented drug interactions. Representative examples from the current dataset:

- **Major interactions**: Rabeprazole, Omeprazole, Budesonide, Triamcinolone, Loperamide
- **Moderate interactions**: Acarbose, Metformin, Alogliptin, Canagliflozin, Chlorpropamide, Hydrocortisone, Dexamethasone, Betamethasone, Aprepitant, Alosetron, Albiglutide (and others — total moderate count is substantial)
- **Minor interactions**: Famotidine, Ranitidine

The high volume of interactions (254 total) is consistent with nelfinavir's known role as a CYP3A4 inhibitor and substrate, which broadly affects co-administered drugs metabolized through the same pathway. Particularly notable are interactions with corticosteroids (major level for Budesonide and Triamcinolone) and proton pump inhibitors (major level for Omeprazole and Rabeprazole), which are commonly co-prescribed in complex patient populations.

> For complete warnings and contraindications, please refer to the package insert. Formal warning and contraindication data were not available in this Evidence Pack (Data Gap DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction is mechanistically coherent — conserved lentiviral protease structure does support a plausible cross-species inhibitory effect — but SIV infection is not a human clinical indication. It is a pre-clinical research model, and "repurposing" Nelfinavir for SIV has no actionable clinical development pathway. With zero clinical trials, only 4 low-tier publications, no India market registration, and missing MOA and safety data, there is no basis to advance this candidate toward any clinical application.

**To proceed, the following is needed:**

- **Clarify research intent**: If the goal is SIV-model pre-clinical validation of nelfinavir's mechanism, this remains a basic science question — not a repurposing candidate. If the intended target is human HIV infection (the established indication), that should be evaluated separately as a regulatory reactivation or market-entry question for India.
- **Resolve Data Gap DG001**: Obtain India package insert (or international equivalent) to complete safety profiling before any clinical consideration.
- **Resolve Data Gap DG002**: Retrieve full MOA data from DrugBank (DB00220) to enable proper mechanistic linkage analysis for any downstream indication.
- **Consider de-prioritization of ranks 2–4**: Feline AIDS (rank 2), the rare neurodevelopmental disorder (rank 3), and the obsolete hyperlipidemia term (rank 4) all present either KG topology artifacts or mechanistic contradictions, and none have any supporting evidence. These should be formally flagged as false positives in the candidate list.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

