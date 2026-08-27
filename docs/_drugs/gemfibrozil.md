---
layout: default
title: Gemfibrozil
parent: 僅模型預測 (L5)
nav_order: 308
evidence_level: L5
indication_count: 10
---

# Gemfibrozil
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

# Gemfibrozil: From Dyslipidemia to Rheumatoid Arthritis

## One-Sentence Summary

> Gemfibrozil is a fibrate-class PPARα agonist originally used to treat dyslipidemia (elevated triglycerides, low HDL-C).
> The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**,
> but this direction is currently supported only by **0 clinical trials** and **4 publications**, mostly preclinical or indirectly related.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dyslipidemia (hypertriglyceridemia / low HDL-C) — inferred from known fibrate pharmacology; no India regulatory filing text is available since the drug is not marketed locally |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap pending DrugBank API lookup). Based on known information, Gemfibrozil is a member of the fibrate class of PPARα agonists, and its efficacy in dyslipidemia (raising HDL-C, lowering triglycerides via LPL activation and ApoC-III suppression) is well established.

PPARα agonists also have recognized anti-inflammatory properties — they can inhibit the NF-κB pathway and reduce expression of pro-inflammatory cytokines (TNF-α, IL-6), which theoretically could provide a modulatory effect on the chronic inflammation seen in rheumatoid arthritis (RA). This is the mechanistic basis for the TxGNN prediction.

However, the supporting literature is weak and largely indirect: it is dominated by animal-model studies of a related but distinct drug (bezafibrate), a case report describing palmar erythema as a gemfibrozil side effect (not an RA study), and a mechanistic Treg/nitric-oxide study conducted in an EAE model (a different autoimmune disease from RA). There is no controlled clinical evidence of gemfibrozil itself being used to treat RA patients, so the mechanistic rationale remains hypothesis-generating rather than clinically validated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | Review/Case Report | American Journal of Clinical Dermatology | Review of palmar erythema etiologies; not an RA study — gemfibrozil is discussed only as one possible drug associated with this dermatologic finding |
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | Preclinical (Animal) | Modern Rheumatology | In a rat adjuvant-induced arthritis (AIA) model, gemfibrozil combined with a reduced steroid dose produced disease control comparable to a full-dose steroid regimen, suggesting a possible steroid-sparing effect |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | Preclinical (Animal) | International Immunopharmacology | Bezafibrate (a pan-PPAR agonist, not gemfibrozil) attenuated experimental RA via PPAR-dependent, especially PPARγ-mediated, anti-inflammatory pathways — supports the fibrate class mechanistically but does not directly test gemfibrozil |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | Preclinical (Animal) | Journal of Immunology | Mechanistic study of nitric oxide and Foxp3/Treg regulation in an EAE (experimental autoimmune encephalomyelitis) model — a different autoimmune disease from RA; relevance to RA is indirect |

---

## Safety Considerations

**Drug Interactions**: DrugBank/DDInter records 129 total interactions for gemfibrozil. Notable **Major**-severity interactions include:
- Eluxadoline
- Loperamide
- Pioglitazone
- Repaglinide
- Rosuvastatin
- Simvastatin

Notable **Moderate**-severity interactions include multiple insulin formulations (aspart, degludec, detemir, glargine, glulisine, human isophane/regular), sulfonylureas (chlorpropamide, tolazamide), other glitazones/glinides (rosiglitazone, nateglinide), rifaximin, and chenodeoxycholic acid.

Key warnings and contraindications from the local product label are not currently available (blocking data gap — pending retrieval and parsing of the official package insert). This must be resolved before any safety evaluation (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Rheumatoid Arthritis signal rests entirely on preclinical/mechanistic and indirect literature (evidence level L4) — no clinical trials, and most supporting studies involve a related drug (bezafibrate) or unrelated disease models (EAE) rather than gemfibrozil in RA patients directly. This is insufficient to advance past S0.

**To proceed, the following is needed:**
- Official India product label (warnings/contraindications) — currently a **Blocking** data gap (DG001)
- Confirmed mechanism of action data from DrugBank — currently a **High**-severity data gap (DG002)
- A dedicated preclinical or clinical study evaluating gemfibrozil (not bezafibrate) specifically in RA models or patients
- Re-evaluation of India market entry plans, since the drug currently has zero local registrations

**Note:** Among the other candidates in this evidence pack, *hypoalphalipoproteinemia* (rank 4) shows materially stronger evidence (Evidence Level L2, decision stage S3, "Proceed with Guardrails") — but this reflects gemfibrozil's already-established fibrate pharmacology rather than a genuinely novel repurposing opportunity, and may warrant a separate evaluation report if needed.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

