---
layout: default
title: Temozolomide
parent: 僅模型預測 (L5)
nav_order: 806
evidence_level: L5
indication_count: 2
---

# Temozolomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Temozolomide: From Malignant Glioma to Adult Astrocytic Tumour (India Market Entry Candidate)

## One-Sentence Summary

> Temozolomide is a globally established oral alkylating agent used as the standard-of-care chemotherapy for malignant glioma (glioblastoma/anaplastic astrocytoma), but it currently has **zero registrations in India**.
> The TxGNN model flags **adult astrocytic tumour** as its top-scoring indication (99.36%),
> and this is backed by **2 clinical trials** and **20 publications**, including several landmark Phase 3 RCTs that already define global treatment guidelines.
> Note: this is less a "novel repurposing" signal and more a **market-entry validation** — the model is confirming a well-known indication for a drug not yet marketed locally.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malignant glioma / glioblastoma multiforme (established global indication; no India license record exists because the drug is not marketed) |
| Predicted New Indication | Adult Astrocytic Tumour |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data from the evidence pack is not available (flagged as a High-severity data gap). Based on well-established public pharmacology, temozolomide is an oral imidazotetrazine alkylating agent that spontaneously converts to the active metabolite MTIC, which methylates DNA (primarily at the O6 position of guanine), triggering cytotoxic DNA damage and apoptosis in rapidly dividing tumour cells.

The predicted indication, "adult astrocytic tumour," is not a mechanistically distant target — it is the same disease family (WHO grade III/IV astrocytic tumours, including anaplastic astrocytoma and glioblastoma) for which temozolomide is already the internationally recognized standard of care (the "Stupp protocol": concomitant radiotherapy plus temozolomide, followed by maintenance temozolomide). This explains the very high TxGNN score and the depth of Phase 3 RCT support.

Because temozolomide is not currently registered in India, this evidence pack should be read as a **market-access opportunity assessment** rather than a speculative repurposing hypothesis — the scientific/clinical evidence is mature and long-standing; what is missing is local regulatory documentation (label warnings, contraindications) needed to complete a safety review.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | Completed | 500 | Randomized trial comparing temozolomide monotherapy vs. PCV (procarbazine/lomustine/vincristine) in recurrent WHO Grade III/IV astrocytic tumours |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | Completed | 26 | Dose-finding study of XL184 (cabozantinib) combined with temozolomide + radiotherapy in newly diagnosed glioblastoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT | N Engl J Med | Landmark EORTC-NCIC trial establishing radiotherapy + concomitant/adjuvant temozolomide as standard of care for newly diagnosed glioblastoma |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | RCT (follow-up) | Lancet Oncol | 5-year follow-up confirming durable survival benefit of temozolomide + radiotherapy over radiotherapy alone |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | RCT | Lancet Oncol | NOA-08 trial: temozolomide monotherapy vs. radiotherapy alone in elderly patients with malignant astrocytoma |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | RCT | Lancet | CeTeG/NOA-09: lomustine-temozolomide combination superior to temozolomide alone in MGMT-methylated glioblastoma |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT | JAMA | EF-14 trial: Tumor-Treating Fields + temozolomide vs. temozolomide alone improves survival in glioblastoma |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT | N Engl J Med | Randomized trial of bevacizumab added to standard temozolomide/radiotherapy in newly diagnosed glioblastoma |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | RCT (Phase II/III) | J Clin Oncol | NRG-BN007: dual immune checkpoint blockade with temozolomide-based regimen in MGMT-unmethylated glioblastoma |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Review | JAMA | Comprehensive review of glioblastoma and primary brain malignancies, confirming temozolomide's role as standard therapy |
| [10914698](https://pubmed.ncbi.nlm.nih.gov/10914698/) | 2000 | Review | Clin Cancer Res | Early review establishing temozolomide's efficacy profile in malignant glioma |
| [29075865](https://pubmed.ncbi.nlm.nih.gov/29075865/) | 2017 | Review | Curr Oncol Rep | Review of glioblastoma treatment in older adults, including temozolomide dosing considerations |

---

## India Market Information

No CDSCO registration currently on record. According to the evidence pack, temozolomide has **0 licenses** in India (`market_status: 未上市` / Not Marketed) — there is no product currently authorized for sale.

---

## Cytotoxicity

Temozolomide is a conventional cytotoxic chemotherapy agent (oral alkylating agent, imidazotetrazine class), used for a malignant CNS tumour indication.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Alkylating agent — imidazotetrazine class) |
| Myelosuppression Risk | Moderate–High — thrombocytopenia and neutropenia are the dose-limiting toxicities of this drug class; nadir typically occurs mid- to late-cycle |
| Emetogenicity Classification | Moderate (standard oral dosing) |
| Monitoring Items | CBC with differential (baseline, weekly during cycle 1, then prior to each cycle), liver function tests, renal function |
| Handling Protection | Requires standard cytotoxic drug handling precautions (PPE, avoid capsule opening/crushing due to mutagenic/teratogenic potential) |

*Note: This classification is based on the drug's known pharmacological class; the evidence pack itself contains no India-specific toxicity/label data (see Safety Considerations below).*

---

## Safety Considerations

- **Drug Interactions**: A total of 320 potential interactions were identified via DDInter. Among the sampled interactions, most severity levels are unclassified ("Unknown") in the source database; two carry an assigned severity: **Naltrexone (Moderate)** and **Levofloxacin (Minor)**. Given the large interaction count, a full DDI screen against a patient's concurrent medication list is recommended before use.

No formal key warnings or contraindications could be extracted — please refer to an authoritative package insert (e.g., FDA/EMA label) for full safety information, as India-specific labeling does not yet exist for this unregistered product.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The clinical evidence for temozolomide in astrocytic tumours/glioblastoma is exceptionally strong (Evidence Level L1, multiple completed Phase 3 RCTs spanning two decades) and this is already the accepted global standard of care. However, a **Blocking**-severity data gap exists: the absence of TFDA/CDSCO label warnings and contraindications means the safety pre-assessment (S1 stage) cannot be completed, and the drug has zero current India registrations.

**To proceed, the following is needed:**
- Official India (or reference-market) package insert data — warnings, contraindications, and precautions — to complete the S1 safety review
- Confirmation of a regulatory registration pathway (new drug application / import license) in India, since this is a market-entry decision rather than an off-label repurposing decision
- DDI severity reconciliation for the ~318 "Unknown"-level interactions, prioritizing agents commonly co-prescribed in oncology settings (antiemetics, corticosteroids, PPIs)

*Secondary signal noted but out of scope for this report: the evidence pack also flags "cauda equina neoplasm" (rank 2, Evidence Level L4, based on a single case report) — evidence is currently insufficient and the pack itself already recommends Hold for this indication.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

