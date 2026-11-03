---
layout: default
title: Bleomycin
parent: Model Prediction Only (L5)
nav_order: 113
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-03
monitor_inn: "Bleomycin"
predicted_indications: ["cauda equina neoplasm", "adult astrocytic tumour", "primary pulmonary lymphoma", "pulmonary blastoma", "well-differentiated fetal adenocarcinoma of the lung"]
description: "Bleomycin: predicted new indication Cauda equina neoplasm (evidence level L5). Approved use: Not recorded in the local data"
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

Bleomycin is a cytotoxic agent that works by cutting DNA strands. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description reflects general knowledge of the drug class.

No direct mechanistic link to cauda equina neoplasm has been established. The only retrieved paper looks at radiation therapy for relapsed CNS germinoma after a chemotherapy regimen that included carboplatin, etoposide and bleomycin. That is a different tumour type, so the connection is weak and indirect. Germ cell tumours at other sites are known to be bleomycin-sensitive, but this does not show benefit in cauda equina neoplasm.

The high TxGNN score is a model output and is not backed by clinical evidence for this disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9440744](https://pubmed.ncbi.nlm.nih.gov/9440744/) | 1998 | Cohort (retrospective) | Journal of Clinical Oncology | Radiation therapy as salvage for CNS germinoma that relapsed after primary chemotherapy including carboplatin, etoposide and bleomycin (PEB). It does not study cauda equina neoplasm. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 26306 | Bleomycin Sulphate Injection (Dabur India Ltd) | Vial of 1 ml injection | Not stated |
| 167240 | Oncobleo 15IU Injection (Sun Pharmaceutical Industries Ltd) | Vial of 1 injection | Not stated |
| 32205 | Bledmax 15mg Injection (Max India Ltd) | Vial of 1 powder for injection | Not stated |
| 29038 | Bleotex 15IU Injection (Alkem Laboratories Ltd) | Vial of 1 injection | Not stated |
| 219746 | Tumocin 15IU Injection (Neon Laboratories Ltd) | Vial of 1 ml injection | Not stated |

These are 5 of the 18 valid single-ingredient licences. None of the licence records carries indication text.

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

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

