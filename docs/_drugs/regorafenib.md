---
layout: default
title: Regorafenib
parent: High Evidence (L1-L2)
nav_order: 732
evidence_level: L2
indication_count: 8
last_modified_at: 2026-11-04
monitor_inn: "Regorafenib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "clear cell renal carcinoma", "renal cell carcinoma associated with neuroblastoma", "renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions", "unclassified renal cell carcinoma", "childhood kidney cell carcinoma", "vulva sarcoma"]
description: "Regorafenib: predicted new indication Liposarcoma (evidence level L2). Approved use: Not recorded in the local data"
---

# Regorafenib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **8** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Regorafenib: Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Regorafenib is an oral multi-kinase inhibitor that blocks angiogenic, stromal and oncogenic kinases. The TxGNN model predicts it may be relevant to **liposarcoma**. Support is mixed: **1 completed Phase 2 trial** and **9 publications** are in the data compiled for this report, but the liposarcoma-specific randomized results did not support routine use. Evidence level is **L2**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L2 |
| India Market Status | Listed in a compiled Indian medicine price dataset (2 of 2) – CDSCO approval status is not included in this data |
| Number of Listed Products | 2 (valid: 2) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Regorafenib inhibits VEGFR1-3, TIE2, PDGFR, FGFR, KIT, RET and RAF. These pathways drive angiogenesis and tumor growth in soft tissue sarcomas, including liposarcoma. Formal mechanism-of-action data were not available in the compiled data, so this description comes from the published literature.

The randomized Phase 2 REGOSARC trial showed benefit in non-adipocytic soft tissue sarcomas (leiomyosarcoma, synovial sarcoma and others), which supports the general idea that regorafenib acts on sarcoma biology. However, REGOSARC did not show benefit in liposarcoma, and the liposarcoma-specific SARC024 cohort concluded that the results "do not support the routine use of regorafenib in this patient population." The high model score should therefore be read with caution: the signal is stronger for sarcoma in general than for liposarcoma itself.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024: blanket protocol of oral regorafenib in selected sarcoma subtypes, including liposarcoma; randomized, double-blind, placebo-controlled liposarcoma cohort |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | RCT | The Oncologist | SARC024 liposarcoma cohort: regorafenib vs placebo in treatment-refractory liposarcoma; results do not support routine use |
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT | The Lancet Oncology | REGOSARC: randomized Phase 2 trial in anthracycline-pretreated advanced soft tissue sarcoma |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | RCT | Eur J Cancer | Updated REGOSARC analysis including post-cross-over use; benefit seen in non-adipocytic sarcoma but not in liposarcoma |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Review | Targeted Oncology | Overview of regorafenib's growing role in sarcoma subtypes |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Review | Crit Rev Oncol Hematol | Maintenance therapy after first-line treatment of advanced soft tissue sarcoma |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Study protocol | BMC Cancer | Design of the REGOSARC randomized Phase 2 trial |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | Quality-adjusted analysis of RCT | Cancer | REGOSARC Q-TWiST analysis of clinical benefit versus toxicity |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 152519 | Nublexa Tablet (Bayer Zydus Pharma Pvt Ltd) | Strip of 28 tablets | Not recorded |
| 185007 | Regonat Tablet (Natco Pharma Ltd) | Bottle of 28 tablets | Not recorded |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function, blood pressure, skin reactions (hand-foot skin reaction), proteinuria, CBC |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 213 interactions were recorded. Major-level examples include acetylsalicylic acid, deferasirox, ibritumomab tiuxetan, tositumomab, abciximab, alteplase, antithrombin III human and apixaban (largely antithrombotic or bleeding-risk agents). Moderate-level examples include dexamethasone, clarithromycin, naltrexone, rosuvastatin and cobicistat.
- Published meta-analyses of related anti-angiogenic kinase inhibitors report hand-foot skin reaction, hepatic toxicity and proteinuria as notable adverse events.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The main prediction has a completed randomized Phase 2 program (SARC024 and REGOSARC), but no Phase 3 trial, and the liposarcoma-specific results were negative or not supportive. The model score is high, but clinical data do not currently justify routine use in liposarcoma.

**To proceed, the following is needed:**
- Subtype-focused data (well-differentiated/dedifferentiated vs myxoid/pleomorphic liposarcoma) to find any responsive subgroup
- Evaluation of combination approaches, as suggested by the SARC024 investigators
- Package insert warnings and contraindications from the Indian labels
- Detailed mechanism-of-action data
- A safety monitoring plan covering liver function, blood pressure, skin toxicity and bleeding-risk drug interactions

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

