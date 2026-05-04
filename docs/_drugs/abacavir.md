---
layout: default
title: Abacavir
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 3
---

# Abacavir
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

# Abacavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Abacavir is a nucleoside reverse transcriptase inhibitor (NRTI) with well-established use in antiretroviral therapy for HIV-1 infection.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**,
with **0 clinical trials** and **1 publication** currently supporting this direction.
The mechanistic basis is strong in principle, but clinical applicability is largely limited to non-human primate models and occupational exposure scenarios.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (antiretroviral combination therapy) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on the clinical context across the available evidence, Abacavir is an NRTI whose active metabolite — carbovir triphosphate — competitively inhibits the viral reverse transcriptase enzyme and terminates proviral DNA chain elongation. This mechanism is the cornerstone of its established efficacy in HIV-1 infection.

SIV (Simian Immunodeficiency Virus) and HIV-1 are both members of the *Lentivirus* genus and share high sequence homology in their reverse transcriptase domains. Because Abacavir's active metabolite directly targets the RT active site — a structurally conserved region across lentiviruses — its inhibitory activity is expected to extend to SIV RT via the same chain-termination mechanism. This cross-species extrapolation is mechanistically sound and not merely speculative.

However, the practical clinical context is significantly limited. SIV primarily infects non-human primates; it is not a human pathogen under ordinary circumstances. Therapeutic relevance for Abacavir in this setting is therefore confined to: (1) animal model research for HIV pathogenesis and drug development, and (2) post-exposure prophylaxis in occupational accidents involving SIV-infected primates. These are niche scientific rather than mainstream clinical applications.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Abacavir in simian immunodeficiency virus infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro comparative study | Antiviral Therapy | Evaluated 16 approved antiretroviral drugs against HIV-2, SIV (mac251, B670), and SHIV strains; demonstrated that multiple NRTI-class drugs retain activity against SIV reverse transcriptase, providing direct in vitro evidence for cross-species antiviral susceptibility relevant to treatment and post-exposure prophylaxis guidance |

---

## India Market Information

Abacavir is currently **not registered or marketed in India**. No authorisation records are available.

---

## Safety Considerations

**Drug Interactions:** A total of 93 drug interactions have been identified via DDInter. Key interactions include:

| Interacting Drug | Interaction Level |
|-----------------|------------------|
| Naltrexone | Moderate |
| Orlistat | Moderate |
| Morphine | Unknown |
| Metformin | Unknown |
| Prednisone | Unknown |
| Amphotericin B | Unknown |
| Sulfasalazine | Unknown |
| Vancomycin | Unknown |

The majority of interactions are classified as "Unknown" severity, indicating limited characterisation data. The two moderate-level interactions (Naltrexone, Orlistat) warrant clinical attention when co-administered.

For complete warnings, contraindications, and precautions, please refer to the approved package insert (e.g., Ziagen® prescribing information), as this data was not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between Abacavir and SIV is biologically coherent given the shared lentiviral RT structure, but clinical evidence is limited to a single in vitro comparative study with no registered clinical trials. Furthermore, SIV infection is not a human disease — the clinical use case is restricted to animal model research or rare occupational post-exposure scenarios, which substantially limits the drug repurposing value from a public health or commercial development perspective.

**To proceed, the following is needed:**

- **MOA data**: Retrieve full DrugBank mechanism-of-action entry for Abacavir to complete the mechanistic rationale analysis
- **Safety data**: Download and parse the approved package insert (e.g., from FDA or EMA) to obtain formal warnings, contraindications, and black-box alerts — currently a blocking data gap (DG001)
- **Preclinical activity data**: Identify published in vivo studies confirming Abacavir activity against SIV in non-human primate models to upgrade evidence from L4 toward L3
- **Clinical context clarification**: Define the specific use case (animal model support vs. occupational PEP) before proceeding with any further regulatory or development planning
- **India registration strategy**: If clinical application is pursued (e.g., PEP guidelines), assess regulatory pathway under CDSCO for new indication filing, given that Abacavir is currently entirely unregistered in India
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

