---
layout: default
title: Chloroquine
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 4
---

# Chloroquine
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

# Chloroquine: From Malaria to Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis

## One-Sentence Summary

Chloroquine is a 4-aminoquinoline antimalarial and antirheumatic agent, classically used to treat malaria, adult rheumatoid arthritis, and systemic lupus erythematosus.
The TxGNN model predicts it may be effective for **Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis (RF+ pJIA)**,
with **0 clinical trials** and **2 publications** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No India registration data available; known uses include malaria, adult RA, and SLE |
| Predicted New Indication | Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Chloroquine is a long-established DMARD (disease-modifying antirheumatic drug). Its immunomodulatory actions — including inhibition of lysosomal phospholipase A2, interference with Toll-like receptor signalling (TLR7/TLR9), suppression of MHC-II antigen presentation, and reduction of pro-inflammatory cytokines (IL-1, IL-6, TNF-α) — form the mechanistic basis for its use in autoimmune conditions.

Rheumatoid factor-positive polyarticular JIA (RF+ pJIA) is the paediatric subtype most closely resembling adult seropositive rheumatoid arthritis, sharing autoantibody-driven synovitis and similar cytokine-mediated joint destruction pathways. Because the inflammatory drivers are mechanistically analogous to adult RA — a condition for which Chloroquine and its analogue hydroxychloroquine are recognised DMARDs — the TxGNN prediction carries biological plausibility.

However, no dedicated clinical trial data exists for Chloroquine specifically in RF+ pJIA. Historical literature in broader juvenile chronic arthritis populations (where Chloroquine was used as a second-line DMARD in the 1970s–1990s) provides only indirect, bridging support. Clinical validation specific to the RF+ polyarticular subtype remains absent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for rheumatoid factor-positive polyarticular juvenile idiopathic arthritis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24334641](https://pubmed.ncbi.nlm.nih.gov/24334641/) | 2014 | Prospective Observational | The Journal of Rheumatology | Long-term real-world experience with leflunomide in JIA; provides DMARD management context but is not specific to Chloroquine |
| [8627446](https://pubmed.ncbi.nlm.nih.gov/8627446/) | 1996 | Case Report | The Journal of Pediatrics | Two RF+ polyarticular JRA patients developed accelerated nodulosis on methotrexate; hydroxychloroquine addition arrested nodule progression in one — indirect evidence of antimalarial benefit in this specific subtype |

---

## India Market Information

Chloroquine is currently **not registered** in India. There are no active drug licenses on record (total registrations: 0).

---

## Safety Considerations

**Drug Interactions (467 total interactions identified; key examples listed below):**

**Major interactions — require clinical review before use:**

| Interacting Drug | Level | Clinical Concern |
|-----------------|-------|-----------------|
| Agalsidase beta | Major | May reduce enzyme replacement therapy efficacy |
| Bupropion | Major | May lower seizure threshold |
| Cisapride | Major | Additive QT interval prolongation risk |
| Clarithromycin | Major | Additive QT interval prolongation risk |
| Dolasetron | Major | Additive QT interval prolongation risk |
| Granisetron | Major | Additive QT interval prolongation risk |

**Notable moderate interactions:**

| Interacting Drug | Level | Clinical Concern |
|-----------------|-------|-----------------|
| Famotidine, Cimetidine | Moderate | May alter Chloroquine absorption or metabolism |
| Aluminum hydroxide, Calcium carbonate, Attapulgite | Moderate | Antacids may reduce Chloroquine gastrointestinal absorption |
| Glimepiride, Glipizide, Glyburide, Chlorpropamide, Acetohexamide, Insulin human | Moderate | Chloroquine may potentiate hypoglycaemic effects |
| Metronidazole, Loperamide, Aprepitant | Moderate | Variable pharmacokinetic or pharmacodynamic interactions |

> Please refer to the package insert for full safety information including key warnings and contraindications (CDSCO label data not yet available in this Evidence Pack).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high prediction score (99.41%) and the biological mechanism is plausible — given RF+ pJIA shares key inflammatory pathways with adult seropositive RA — there are zero dedicated clinical trials and only 2 indirect literature references for this specific indication, yielding an evidence level of L5. This is insufficient to support clinical or regulatory advancement at this stage.

**To proceed, the following is needed:**
- Retrieve formal MOA documentation (DrugBank API query to address DG002)
- Obtain India CDSCO label / package insert to extract key warnings and contraindications (DG001 — currently Blocking severity)
- Conduct a systematic review bridging hydroxychloroquine evidence in JIA subtypes to assess whether hydroxychloroquine data can support a Chloroquine indication
- Evaluate feasibility of a Phase 2 proof-of-concept trial specifically in RF+ pJIA patients
- Clarify regulatory pathway for India market entry if evidence strengthens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

