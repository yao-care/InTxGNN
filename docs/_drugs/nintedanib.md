---
layout: default
title: Nintedanib
parent: 僅模型預測 (L5)
nav_order: 490
evidence_level: L5
indication_count: 10
---

# Nintedanib
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

# Nintedanib: From Idiopathic Pulmonary Fibrosis to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Nintedanib is a triple angiokinase inhibitor (VEGFR / PDGFR / FGFR) approved for idiopathic pulmonary fibrosis (IPF) and related fibrosing interstitial lung diseases.
The TxGNN model predicts it may be effective for **Dermatofibrosarcoma Protuberans (DFSP)**,
with **0 clinical trials** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Idiopathic Pulmonary Fibrosis (IPF); systemic sclerosis-associated ILD |
| Predicted New Indication | Dermatofibrosarcoma Protuberans (DFSP) |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L4 — Mechanistic / preclinical studies only |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory file. Based on known pharmacological information, Nintedanib (brand name Ofev®) is a triple angiokinase inhibitor that simultaneously blocks VEGFR (1/2/3), PDGFRα/β, and FGFR (1/2/3), along with additional kinases such as FLT3 and Src. These overlapping targets suppress both pro-fibrotic and pro-angiogenic signalling, which explains its efficacy in IPF, systemic sclerosis-associated ILD, and — in certain markets — non-small cell lung cancer (NSCLC) adenocarcinoma.

The mechanistic link to DFSP is biologically compelling. DFSP is driven by a t(17;22) chromosomal translocation that creates a COL1A1-PDGFB fusion protein, which constitutively activates PDGFRβ. Nintedanib's PDGFRα/β inhibition places it in the same mechanistic class as imatinib — the only FDA-approved systemic therapy for DFSP — establishing a clear class-effect rationale. Additionally, nintedanib's concurrent VEGFR and FGFR inhibition may provide complementary anti-tumour activity in the tumour microenvironment beyond what imatinib alone offers.

However, this mechanistic logic has not been validated clinically for DFSP. The entire body of direct evidence for this drug-disease pair consists of a single broad narrative review of PDGFR inhibitors, with no case reports, basket trials, or prospective studies involving nintedanib specifically in DFSP. The prediction is hypothesis-driven and requires prospective experimental confirmation before any clinical exploration can be justified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Nintedanib in Dermatofibrosarcoma Protuberans.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Narrative Review | Pharmacological Research | Comprehensive review of small-molecule PDGFR inhibitors (including nintedanib) across neoplastic disorders; establishes PDGFRβ as a validated oncology target and discusses the mechanistic basis for PDGFR-targeted therapy in PDGFR-driven tumours |

---

## India Market Information

Nintedanib is currently **not marketed in India**. No product registrations are on file with CDSCO (0 licences recorded).

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Triple angiokinase inhibitor (VEGFR / PDGFR / FGFR class) |
| Myelosuppression Risk | Low to moderate (haematological toxicity is less prominent than conventional cytotoxics; neutropenia has been reported in combination regimens for NSCLC) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (ALT / AST — hepatotoxicity is a key signal), CBC, renal function, blood pressure, signs of haemorrhage or GI perforation |
| Handling Protection | Standard oral targeted therapy precautions; institutional cytotoxic handling policy recommended given antineoplastic classification |

---

## Safety Considerations

Nintedanib's full safety profile is not available in the current Evidence Pack. Based on its approved use in IPF and ILD, the following signals are known from the prescribing information (Ofev® SmPC):

- **Hepatotoxicity**: Elevations in ALT/AST are common; dose reduction or interruption may be required
- **Gastrointestinal effects**: Diarrhoea (very common), nausea, vomiting, abdominal pain
- **Haemorrhagic events**: Increased bleeding risk, particularly relevant when combined with anticoagulants
- **Embryo-foetal toxicity**: Contraindicated in pregnancy; effective contraception required

Please refer to the full package insert for contraindications, drug interactions, and population-specific warnings (hepatic impairment, cardiovascular disease).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The PDGFRβ inhibition mechanism offers a credible biological basis for exploring nintedanib in DFSP — particularly in imatinib-resistant or imatinib-intolerant patients — but the entire current evidence base consists of a single mechanistic review with no direct clinical, case-report, or preclinical data for this specific drug-disease pair (Evidence Level L4). With no India market authorisation and critical data gaps in MOA documentation and safety profiling, the evidence threshold for advancement has not been met.

**To proceed, the following is needed:**

- Retrieve full MOA and pharmacological profile from DrugBank API (DB09079) to complete the mechanistic rationale
- Conduct systematic literature search for nintedanib in soft-tissue sarcomas broadly (not limited to DFSP) to detect any indirect evidence
- Identify preclinical (in vitro / in vivo) studies of PDGFR inhibition in DFSP cell lines or PDX models
- Obtain CDSCO regulatory approval status and download the Ofev® package insert for India-specific safety and contraindication data
- Assess feasibility of a basket trial entry for nintedanib in PDGFRβ-activated sarcomas (including imatinib-refractory DFSP)
- Clarify DDI data gap (DDInter database file missing) before any polypharmacy evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

