---
layout: default
title: Nevirapine
parent: 僅模型預測 (L5)
nav_order: 455
evidence_level: L5
indication_count: 3
---

# Nevirapine
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

# Nevirapine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Nevirapine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) widely used for HIV-1 infection in humans.
The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome**,
with **0 clinical trials** and **1 publication** currently supporting this direction.
The evidence base remains at preclinical level only, and the indication is veterinary rather than human medicine.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 Infection |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Nevirapine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) that binds directly and non-competitively to HIV-1 reverse transcriptase (RT), blocking both RNA-dependent and DNA-dependent DNA polymerase activity. Unlike nucleoside analogues, it does not require intracellular phosphorylation. Its efficacy against HIV-1 infection is well established in human medicine.

Feline Immunodeficiency Virus (FIV) belongs to the same Lentivirus genus as HIV-1 and causes an acquired immunodeficiency-like syndrome in cats. The theoretical mechanistic basis is that FIV RT shares structural homology with HIV-1 RT, suggesting NNRTIs could potentially bind the FIV RT hydrophobic pocket. However, key residues at the NNRTI binding site of FIV RT — corresponding to critical positions Y181, Y188, and K103 in HIV-1 — differ significantly, resulting in substantially reduced activity for most first-generation NNRTIs including nevirapine.

The TxGNN model's high score most likely reflects the network connectivity between FIV ↔ HIV-1 ↔ NNRTI nodes in the underlying knowledge graph, rather than direct biological activity. Two additional barriers make this a weak candidate: (1) this is a veterinary indication, governed by a completely separate regulatory and clinical pathway; (2) the single supporting publication is an in vitro structural comparison, not a therapeutic efficacy study.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | In vitro Structural Study | Journal of Veterinary Science | Biochemical and structural comparison of NNRTIs (nevirapine, efavirenz, rilpivirine) against FIV RT vs. HIV RT; investigated the structural basis for differential inhibitor activity between feline and human lentiviral reverse transcriptases |

---

## Safety Considerations

**Drug Interactions**: Nevirapine has **207 known drug interactions** (source: DDInter). The following moderate-level interactions are representative:

| Interacting Drug | Level | Clinical Relevance |
|----------------|-------|-------------------|
| Clarithromycin | Moderate | CYP3A4 interaction; may alter nevirapine plasma levels |
| Dexamethasone | Moderate | CYP3A4 induction; may reduce nevirapine exposure |
| Betamethasone | Moderate | CYP3A4 interaction |
| Budesonide | Moderate | CYP3A4 interaction |
| Triamcinolone | Moderate | CYP3A4 interaction |
| Prednisolone | Moderate | CYP3A4 interaction |
| Bupropion | Moderate | CYP2B6 substrate; nevirapine is a CYP2B6 inducer |
| Ondansetron | Moderate | CYP3A4 interaction |
| Granisetron | Moderate | CYP3A4 interaction |
| Aprepitant | Moderate | CYP3A4 interaction |
| Saxagliptin | Moderate | CYP3A4/5 substrate |
| Linagliptin | Moderate | CYP3A4 interaction |
| Naltrexone | Moderate | CYP3A4 interaction |
| Naloxegol | Moderate | CYP3A4 substrate |
| Naldemedine | Moderate | CYP3A4 substrate |
| Cisapride | Moderate | CYP3A4 substrate |
| Eliglustat | Moderate | CYP2D6/CYP3A4 substrate |
| Orlistat | Moderate | May reduce oral bioavailability |
| Nitisinone | Moderate | CYP-mediated interaction |
| Rabeprazole | Moderate | CYP2C19 interaction |

Please refer to the package insert for key warnings and contraindications (data not available in this evidence pack).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction connects Nevirapine to feline acquired immunodeficiency syndrome via knowledge graph network paths, but the evidence base is limited to a single in vitro structural study with no clinical trial data; furthermore, the target indication is veterinary medicine, which lies outside the standard human drug repurposing pathway.

**To proceed, the following is needed:**

- In vitro antiviral activity data specifically confirming nevirapine efficacy against wild-type FIV reverse transcriptase (not just structural modelling)
- Clarification of development intent: veterinary medicine vs. human medicine repurposing
- MOA data from DrugBank to complete the mechanistic analysis (DG002)
- Key warnings and contraindications from the package insert (DG001) before any safety evaluation
- If veterinary development is intended: regulatory pathway assessment under applicable veterinary drug approval frameworks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

