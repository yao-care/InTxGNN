---
layout: default
title: Regorafenib
parent: Model Prediction Only (L5)
nav_order: 732
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Regorafenib: predicted new indication Liposarcoma (evidence level L5). Approved use: Metastatic colorectal cancer, hepatocellular carcinoma (liver cancer)…"
monitor_inn: "Regorafenib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "clear cell renal carcinoma", "renal cell carcinoma associated with neuroblastoma", "unclassified renal cell carcinoma", "renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions", "childhood kidney cell carcinoma", "vulva sarcoma", "spindle cell liposarcoma", "renal cell carcinoma (disease)"]
---

# Regorafenib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Regorafenib: From Metastatic Colorectal Cancer / Hepatocellular Carcinoma / GIST to Liposarcoma

## One-Sentence Summary

Regorafenib is an oral multi-kinase inhibitor originally used for metastatic colorectal cancer, hepatocellular carcinoma and gastrointestinal stromal tumour (GIST).
The TxGNN model predicts it may be effective for **liposarcoma**, with **1 clinical trial** and **9 publications** compiled for this direction.
The strongest data are randomized and placebo-controlled, but they **do not support routine use in liposarcoma**: the liposarcoma-specific cohort showed no benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic colorectal cancer, hepatocellular carcinoma (liver cancer), gastrointestinal stromal tumour. No approved indication text was recorded in the India licence entries, so this comes from the knowledge graph's indication list. |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L1 (see note below) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold (the data-based grade is Proceed with Guardrails, but the liposarcoma-specific results are negative; see Conclusion) |

> **Note on evidence level:** The L1 grade rests on randomized, placebo-controlled Phase 2 trials in soft tissue sarcoma. Strictly under the grading rules (≥2 completed Phase 3 RCTs), no Phase 3 trial exists for this indication, so the level is better read as L2-equivalent. More importantly, the randomized data are **negative for liposarcoma specifically**.

---

## Why is This Prediction Reasonable?

Regorafenib is a multi-kinase inhibitor that targets angiogenic kinases (VEGFR1-3, TIE2), stromal kinases (PDGFR, FGFR) and oncogenic kinases (KIT, RET, RAF). These pathways drive blood-vessel growth and tumour proliferation in many solid tumours, including soft tissue sarcomas. Detailed mechanism-of-action data were not available in the data compiled for this report; the targets above come from the literature.

Its original indications (colorectal cancer, hepatocellular carcinoma and GIST) are all solid tumours that respond to kinase and angiogenesis inhibition. GIST is itself a sarcoma, which links the drug's established use to the sarcoma family. This explains the high TxGNN score.

However, the clinical data show that this mechanistic link does not hold equally across sarcoma subtypes. The REGOSARC randomized trial showed benefit in non-adipocytic sarcomas (leiomyosarcoma, synovial sarcoma and others), but **not in liposarcoma**. The SARC024 liposarcoma cohort confirmed this, and its authors concluded the results "do not support the routine use of regorafenib" in this population.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024: blanket protocol of oral regorafenib in selected sarcoma subtypes, including liposarcoma; the liposarcoma cohort was randomized, double-blind and placebo-controlled |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | RCT | The Oncologist | SARC024 liposarcoma cohort: results do not support routine use of regorafenib in treatment-refractory liposarcoma |
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT | The Lancet Oncology | REGOSARC: placebo-controlled Phase 2 trial of regorafenib in anthracycline-pretreated advanced soft tissue sarcoma |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | RCT (updated analysis) | European Journal of Cancer | Efficacy in leiomyosarcoma, synovial sarcoma and other non-adipocytic sarcomas, but not in liposarcoma; includes post-cross-over activity |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Review | Targeted Oncology | Review of the growing role of regorafenib in sarcoma |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Review | Critical Reviews in Oncology/Hematology | Maintenance therapy after first-line treatment for advanced soft tissue sarcoma |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | Post hoc analysis of RCT | Cancer | REGOSARC quality-adjusted time without symptoms of progression or toxicity (Q-TWiST) analysis |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Study protocol | BMC Cancer | Design of the REGOSARC randomized Phase 2 trial |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 152519 | Nublexa Tablet (Bayer Zydus Pharma Pvt Ltd) | Strip of 28 tablets | Not recorded |
| 185007 | Regonat Tablet (Natco Pharma Ltd) | Bottle of 28 tablets | Not recorded |

Both licences are valid single-ingredient oral products.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (oral multi-kinase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function (hepatic toxicity is a known class concern for anti-angiogenic TKIs), blood pressure, urine protein, skin (hand-foot skin reaction), CBC |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions:** 213 interactions were identified in the interaction database. Examples of the **Major** level include:
  - Acetylsalicylic acid
  - Deferasirox
  - Apixaban
  - Alteplase
  - Abciximab
  - Antithrombin III human
  - Ibritumomab tiuxetan
  - Tositumomab

  Several of these are antithrombotic or thrombolytic agents. **Moderate** examples include dexamethasone, clarithromycin, rosuvastatin, naltrexone and cobicistat.

- **Class-related toxicities (from the retrieved literature):** hand-foot skin reaction, hypertension, diarrhoea, asthenia, hepatic toxicity and proteinuria are reported with regorafenib and related anti-angiogenic kinase inhibitors.

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN score is very high and randomized trials exist, the liposarcoma cohort of SARC024 and the REGOSARC trial both showed no benefit in liposarcoma, and the SARC024 authors explicitly advise against routine use. The positive sarcoma signal is confined to non-adipocytic subtypes. Any move forward would need a rationale beyond monotherapy in unselected liposarcoma. The framework-based recommendation of "Proceed with Guardrails" should therefore be tempered by these negative subtype-specific results.

**To proceed, the following is needed:**
- Evidence of benefit in a defined liposarcoma subset (for example, by histological subtype) or in combination regimens, as the SARC024 authors suggest exploring
- Package insert warnings and contraindications for the India-marketed products
- Mechanism-of-action data and the approved indication text for the India licences
- A safety monitoring plan, including attention to bleeding risk with the major-level antithrombotic interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

