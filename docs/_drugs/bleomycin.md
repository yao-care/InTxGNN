---
layout: default
title: Bleomycin
parent: Model Prediction Only (L5)
nav_order: 113
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
monitor_inn: "Bleomycin"
predicted_indications: ["cauda equina neoplasm", "adult astrocytic tumour", "primary pulmonary lymphoma", "pulmonary blastoma", "well-differentiated fetal adenocarcinoma of the lung"]
description: "Bleomycin: predicted new indication Cauda equina neoplasm (evidence level L5). In India: 18 listed products (18 not discontinued)"
---

# Bleomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Bleomycin: Cauda equina neoplasm
{: .text-alpha }

## One-Sentence Summary

Bleomycin is a cytotoxic antibiotic that causes DNA strand breaks and is marketed in India as an injectable anticancer drug.
The TxGNN model predicts it may be relevant for **cauda equina neoplasm**, but the data compiled for this report contain **no registered clinical trials** and only **1 publication**, which is an indirect study of CNS germinoma rather than of this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cauda equina neoplasm |
| TxGNN Prediction Score | 0.9930 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (18 of 18) – CDSCO approval status is not included in this data |
| Number of Listed Products | 18 (valid: 18) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Bleomycin is a cytotoxic agent that works by cutting DNA strands. This description reflects general knowledge of the drug class. According to the Mechanism of Action section of the US FDA-approved prescribing information for bleomycin: "Although the exact mechanism of action of bleomycin is unknown, available evidence indicates that the main mode of action is the inhibition of DNA synthesis with some evidence of lesser inhibition of RNA and protein synthesis. Bleomycin is known to cause single, and to a lesser extent, double-stranded breaks in DNA." ([DailyMed: Bleomycin (bleomycin sulfate) prescribing information, Meitheal Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=640602f9-a7df-46f0-a9b1-19c471008bee), label version 2026-04-17; accessed 2026-11-19.)

No direct mechanistic link to cauda equina neoplasm has been established. The only retrieved paper looks at radiation therapy for relapsed CNS germinoma after a chemotherapy regimen that included carboplatin, etoposide and bleomycin. That is a different tumour type, so the connection is weak and indirect. Germ cell tumours at other sites are known to be bleomycin-sensitive, but this does not show benefit in cauda equina neoplasm.

The high TxGNN score is a model output and is not backed by clinical evidence for this disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9440744](https://pubmed.ncbi.nlm.nih.gov/9440744/) | 1998 | Cohort (retrospective) | Journal of Clinical Oncology | Radiation therapy as salvage for CNS germinoma that relapsed after primary chemotherapy including carboplatin, etoposide and bleomycin (PEB). It does not study cauda equina neoplasm. |

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 26306 | Bleomycin Sulphate Injection | Vial of 1 ml Injection | Valid |
| 26540 | Bleocel 15IU Injection | Vial of 1 ml Injection | Valid |
| 28040 | Bleocin Injection | Vial of 1 Injection | Valid |
| 28066 | Bleochem 15IU Injection | Vial of 1 Injection | Valid |
| 29038 | Bleotex 15IU Injection | Vial of 1 Injection | Valid |
| 30898 | Bleowel 15IU Injection | Vial of 1 Injection | Valid |
| 31004 | Bleocol 15IU Injection | Vial of 1 Injection | Valid |
| 31506 | Bleocare 15mg Injection | Vial of 1 Injection | Valid |
| 31747 | Blomin 15IU Injection | Vial of 1 Injection | Valid |
| 32205 | Bledmax 15mg Injection | Vial of 1 Powder for Injection | Valid |
| 32396 | Bleolem 15mg Injection | Vial of 1 Injection | Valid |
| 32712 | Bleocare 30mg Injection | Vial of 1 Injection | Valid |
| 144283 | Metbleo Injection | Vial of 1 Injection | Valid |
| 155196 | Naprobleo 15IU Injection | Vial of 1 Injection | Valid |
| 167240 | Oncobleo 15IU Injection | Vial of 1 Injection | Valid |
| 169639 | Oil Bleo 30mg Injection | Vial of 1 Injection | Valid |
| 219746 | Tumocin 15IU Injection | Vial of 1 ml Injection | Valid |
| 224367 | Tumocin 30mg Injection | Vial of 1 Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

None of the licence records carries indication text.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA-damaging glycopeptide antibiotic) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Pulmonary function and chest imaging, given the lung injury reported with bleomycin, plus CBC and liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 205 interacting drugs. The entries listed here were mostly of unknown severity, with levofloxacin graded Minor. Examples include pantoprazole, palonosetron, aprepitant, morphine, omeprazole, vancomycin, prednisone and ondansetron.
- **Pulmonary toxicity**: The retrieved literature reports interstitial pneumonitis and dose-related lung injury with bleomycin.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting paper concerns a different CNS tumour (germinoma) and does not directly address cauda equina neoplasm. No trials are registered, so the high model score has no clinical backing and the evidence level is L5.

**To proceed, the following is needed:**
- Studies that directly examine bleomycin in cauda equina or spinal cord region neoplasms
- Mechanism-of-action data for the drug
- Package insert warnings and contraindications from the India licence holders
- A review of bleomycin's pulmonary toxicity and of how well the drug reaches the target tissue

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-20 | "Detailed mechanism-of-action data were not available in the data compiled for this report, so this description reflects general knowledge of the drug class" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt (revised 2026-11-20; earlier version kept in the record) | [DailyMed: Bleomycin (bleomycin sulfate) prescribing information, Meitheal Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=640602f9-a7df-46f0-a9b1-19c471008bee) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

