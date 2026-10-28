---
layout: default
title: Alpelisib
parent: Model Prediction Only (L5)
nav_order: 38
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Alpelisib: predicted new indication Pulmonary hypertension (evidence level L4). Approved use: Not recorded in the India license data (the clinical program is HR+/H…"
monitor_inn: "Alpelisib"
predicted_indications: ["pulmonary hypertension"]
---

# Alpelisib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Alpelisib: From Oncology Use (PIK3CA-Mutated Breast Cancer) to Pulmonary Hypertension
{: .text-alpha }

## One-Sentence Summary

Alpelisib is a PI3K-alpha inhibitor marketed in India as Pivikto 200 mg tablets. The approved indication text is not recorded in the data compiled for this report, but the drug's clinical program is in PIK3CA-mutated breast cancer.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but there are **no clinical trials** and only **1 publication** for this indication. That publication is a case report of alpelisib-induced interstitial lung disease, which is a safety signal and not support for benefit.
Evidence for this prediction is essentially model-derived.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the India license data (the clinical program is HR+/HER2-, PIK3CA-mutated advanced breast cancer) |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 0.9903 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Alpelisib is known to be a PI3K-alpha isoform inhibitor, and its clinical development has been in oncology, particularly PIK3CA-mutated breast cancer.

The biological rationale is that PI3K/AKT signaling contributes to proliferation and remodeling of pulmonary vascular smooth muscle, which is a feature of pulmonary hypertension. Inhibiting PI3K-alpha is therefore biologically plausible. This is a theoretical link only.

The only retrieved publication is a case report of alpelisib-induced interstitial lung disease in a patient with advanced breast cancer. It describes a pulmonary adverse event and does not support benefit. The high TxGNN score is not backed by clinical evidence, and the pulmonary toxicity signal raises a safety concern for this direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for pulmonary hypertension.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Case report | J Oncol Pharm Pract | Alpelisib-induced interstitial lung disease in a patient with advanced breast cancer. This is an adverse event report, not evidence of benefit. |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 175328 | Pivikto 200mg Tablet (Novartis India Ltd) | Strip of 14 tablets | Not recorded |

---

## Cytotoxicity

Alpelisib is an anticancer drug, but it is a targeted therapy (PI3K-alpha inhibitor) and not a conventional cytotoxic agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Blood glucose is a key monitoring item, because hyperglycemia is a recognized safety issue in the alpelisib clinical program. Other monitoring should follow the package insert. |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified, and the 20 reviewed here were all rated Moderate. Many are glucose-lowering agents, including acarbose, albiglutide, alogliptin, metformin, pioglitazone, acetohexamide, canagliflozin, chlorpropamide, dapagliflozin, empagliflozin, ertugliflozin, exenatide, dulaglutide, glimepiride and glipizide. Other interacting drugs include alosetron, bupropion, dexamethasone, dronabinol and fidaxomicin.
- **Pulmonary toxicity signal**: A published case report describes alpelisib-induced interstitial lung disease, which is relevant when considering use in a pulmonary vascular condition.
- **Hyperglycemia**: Safety data from the alpelisib breast cancer trials indicate hyperglycemia is a key safety issue.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score and a plausible but unproven PI3K-related mechanism. There are no clinical trials in pulmonary hypertension, and the only retrieved publication is a pulmonary adverse event report. This raises a safety concern rather than supporting efficacy.

**To proceed, the following is needed:**
- Preclinical evidence (for example, animal models of pulmonary hypertension) showing a benefit of PI3K-alpha inhibition
- Detailed mechanism of action data
- Package insert warnings and contraindications, particularly for pulmonary toxicity and hyperglycemia
- An assessment of the interstitial lung disease risk and of interactions with the glucose-lowering drugs listed above
- The approved indication text for the India license
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

