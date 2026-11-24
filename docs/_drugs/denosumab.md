---
layout: default
title: Denosumab
parent: Model Prediction Only (L5)
nav_order: 242
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Denosumab: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Osteoporosis (including postmenopausal and drug-induced osteoporosis)"
monitor_inn: "Denosumab"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Denosumab
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

## Denosumab: From Osteoporosis to Severe Nonproliferative Diabetic Retinopathy
{: .text-alpha }

## One-Sentence Summary

Denosumab is a RANKL inhibitor originally used to treat osteoporosis, including postmenopausal and drug-induced osteoporosis.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but the support is **model prediction only**, with **no clinical trials** and **no directly relevant publications** for this specific indication.
A related prediction, diabetic retinopathy, has 2 publications, but neither addresses retinopathy outcomes directly.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis (including postmenopausal and drug-induced osteoporosis) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (10 of 10) – CDSCO approval status is not included in this data |
| Number of Listed Products | 10 (valid: 10) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for denosumab: "Denosumab products bind to RANKL, a transmembrane or soluble protein essential for the formation, function, and survival of osteoclasts, the cells responsible for bone resorption. Denosumab products prevent RANKL from activating its receptor, RANK, on the surface of osteoclasts and their precursors." ([DailyMed: Conexxence (denosumab) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=39a0a789-778f-4695-b3a9-61643e6396cd), label version 2026-11-04; accessed 2026-11-19.) Denosumab is known as a RANKL inhibitor, and its efficacy in osteoporosis is established. Mechanistically, RANKL/RANK signalling has been proposed to play a role in inflammation, vascular calcification and metabolic regulation.

A link to retinal microvascular disease or diabetes-related inflammation is therefore conceivable, but it is speculative. The only support in the data is the very high TxGNN score. No ocular efficacy or ocular safety data are available, and the mechanism cannot be cross-checked against a recorded mechanism of action.

For the broader prediction of **diabetic retinopathy** (score 0.9923), one 2024 cohort analysis suggests denosumab may reduce the incidence of type 2 diabetes and related complications compared with bisphosphonates. This is an indirect, metabolic signal and not evidence of benefit in the retina.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for severe nonproliferative diabetic retinopathy. The following two publications were retrieved for the related prediction of diabetic retinopathy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | Cohort / observational (inferred from title) | Diabetes, Obesity & Metabolism | Real-world cohort analysis with systematic review and meta-analysis. Denosumab was associated with lower incidence of type 2 diabetes, less foot ulceration and lower all-cause mortality than bisphosphonates. Microvascular outcomes, including retinopathy, were examined, but retinopathy-specific results cannot be confirmed from the available abstract. |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | Observational / cross-sectional (inferred from title) | Cureus | Use of the FRAX fracture risk tool in adults with type 2 diabetes. Not relevant to denosumab efficacy in retinopathy. |

## India Market Information

Approved indication text was not recorded for these registrations. Five of the 10 valid registrations are listed.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 58562 | Denu Injection | Prefilled syringe of 1 ml Injection | Valid |
| 59166 | Denosurel 120mg Injection | Vial of 1 Injection | Valid |
| 60203 | Denolite Injection | Prefilled syringe of 1 ml Injection | Valid |
| 60751 | Denaxa Injection | Prefilled syringe of 1 Injection | Valid |
| 61547 | Denorange Injection | Prefilled syringe of 1 ml Injection | Valid |
| 73057 | Esentra 60mg Injection | Vial of 1 Injection | Valid |
| 161730 | Olimab 60mg Injection | Prefilled syringe of 1 Injection | Valid |
| 173788 | Prolia Solution for Injection | Prefilled syringe of 1 Solution for Injection | Valid |
| 184573 | Rozel Injection | Prefilled syringe of 1 ml Injection | Valid |
| 243842 | Xgeva Solution for Injection | Vial of 1 Solution for Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 193 interactions were recorded. The ones listed here are all moderate. They include corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone), immunosuppressants and related agents (tacrolimus, mercaptopurine, dupilumab, levamisole, trimetrexate), radiopharmaceuticals (ibritumomab tiuxetan, iobenguane I-131, tositumomab), and corticotropin and tetracosactide.

Please refer to the package insert for warnings and contraindications. No ocular safety data are available for denosumab.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score alone (L5), with no clinical trials and no direct literature on retinopathy. The mechanistic link between RANKL inhibition and retinal microvascular disease is hypothetical.

**To proceed, the following is needed:**
- Full-text review of PMID 38899553 to check whether it contains retinopathy-specific outcomes, which could support an upgrade to L4
- Detailed mechanism of action data and preclinical evidence linking RANKL/RANK signalling to diabetic retinopathy
- Package insert warnings and contraindications for the registered Indian products
- Ocular safety and efficacy data, including whether systemic administration is suitable for a retinal indication

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Conexxence (denosumab) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=39a0a789-778f-4695-b3a9-61643e6396cd) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

