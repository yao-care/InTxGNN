---
layout: default
title: Vincristine
parent: Model Prediction Only (L5)
nav_order: 891
evidence_level: L5
indication_count: 2
monitor_inn: "Vincristine"
predicted_indications: ["vertebral anomalies and variable endocrine and T-cell dysfunction", "retroperitoneal neoplasm"]
last_modified_at: 2026-11-24
description: "Vincristine: predicted new indication Vertebral anomalies and variable endocrine and T-cell dysfunction (evidence level L5). In India: 16 listed products (16 not discontinued)"
---

# Vincristine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Vincristine: Vertebral anomalies and variable endocrine and T-cell dysfunction
{: .text-alpha }

## One-Sentence Summary

Vincristine is a cytotoxic injectable anticancer drug.
The TxGNN model predicts it may be useful for **vertebral anomalies and variable endocrine and T-cell dysfunction**, a rare syndromic disorder.
The data compiled for this report contain **0 clinical trials** and **0 publications** for this disease, so the prediction is model-based only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Vertebral anomalies and variable endocrine and T-cell dysfunction |
| TxGNN Prediction Score | 0.9924 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (16 of 16) – CDSCO approval status is not included in this data |
| Number of Listed Products | 16 (valid: 16) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for vincristine: "The mechanisms of action of vincristine sulfate remain under investigation. The mechanism of action of vincristine sulfate has been related to the inhibition of microtubule formation in mitotic spindle, resulting in an arrest of dividing cells at the metaphase stage." ([DailyMed: vincristine sulfate prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b22e4c8e-dbe1-4d4b-a026-e1812974071c), label version 2026-02-17; accessed 2026-11-19.) Vincristine is a vinca alkaloid, a class that binds tubulin and blocks microtubule formation. This arrests rapidly dividing cells in mitosis, which explains its use in blood cancers.

The predicted disease is a rare syndrome of vertebral malformation, endocrine abnormalities and T-cell dysfunction. Its core problem is developmental or immune, not uncontrolled cell proliferation. No therapeutic rationale for a cytotoxic, anti-mitotic drug can be established from the supplied data. The very high score from the TxGNN model (deep learning) (0.9924) is not backed by any trial or publication, and it may reflect similarities the model learned between related diseases, not biological evidence. Treat the prediction as a hypothesis only, not as a lead supported by biology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

The records contain no approved-indication text, so no approved use can be stated from them.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 14867 | Alcrist 1mg Injection | Vial of 1 Injection | Valid |
| 30211 | Biocristin 1mg Injection | Vial of 1 Injection | Valid |
| 30933 | B Cristine 1mg Injection | Vial of 1 Injection | Valid |
| 31216 | Biocristin AQ 1mg Injection | Vial of 1 ml Injection | Valid |
| 36318 | Cytocristin 1mg Injection | Vial of 1 ml Injection | Valid |
| 40690 | Cytocristin 2mg Injection | Vial of 2 ml Injection | Valid |
| 111937 | Ivin 1mg Injection | Vial of 1 ml Injection | Valid |
| 163537 | Onvinc 1mg Injection | Vial of 1 Injection | Valid |
| 165312 | Oncocristin AQ 1mg Injection | Vial of 1 ml Injection | Valid |
| 233766 | Vinlon 1mg Injection | Vial of 1 ml Injection | Valid |
| 234694 | Vincreta 1mg Injection | Vial of 1 Injection | Valid |
| 234808 | Vinstin 1mg Injection | Vial of 1 Injection | Valid |
| 237200 | Vriestran 1mg/100mg Injection | Vial of 1 ml Injection | Valid |
| 237360 | Vincryst 1mg Injection | Vial of 1 ml Injection | Valid |
| 237515 | Vinrosa 1mg Injection | Vial of 1 ml Injection | Valid |
| 237878 | Vcad 1mg Injection | Vial of 1 Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (vinca alkaloid, anti-microtubule) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Blood counts (CBC with differential), liver function and neurological status. The knowledge graph links the drug to liver failure, cholestasis, leukopenia and peripheral neuropathy as contraindication relations |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindication relations in the knowledge graph** (not label text): liver failure, cholestasis and other hyperbilirubinaemia conditions (including Gilbert syndrome), leukopenia, peripheral neuropathy and other neuromuscular diseases (including Charcot-Marie-Tooth disease), acute urate nephropathy, and fungal or other infectious disease.
- **Drug interactions**: 505 interactions are recorded. The one listed as major is **clarithromycin**. Moderate interactions include aprepitant, dexamethasone, metronidazole, miconazole, rolapitant, simvastatin, rosuvastatin, naltrexone, eliglustat, tinidazole, troglitazone and glycerol phenylbutyrate.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no trials or publications for this disease, and no plausible link between an anti-mitotic cytotoxic drug and a developmental or immune syndrome. Vincristine's toxicity (nerve, liver and blood-count effects) is also hard to justify without any supporting evidence.

**To proceed, the following is needed:**
- An independent biological rationale, such as disease mechanism, or preclinical or case-level data for this syndrome
- Mechanism-of-action data for the drug
- Package insert warnings and contraindications for the India-licensed products
- A benefit-risk assessment for a rare, likely non-malignant condition

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for vincristine are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: vincristine sulfate prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b22e4c8e-dbe1-4d4b-a026-e1812974071c) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

