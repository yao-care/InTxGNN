---
layout: default
title: Carbimazole
parent: Model Prediction Only (L5)
nav_order: 145
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Carbimazole: predicted new indication Resistance to thyroid hormone due to a mutation in thyroid hormone re… (evidence level L5). Approved use: Hyperthyroidism, Graves disease, thyrotoxicosis"
monitor_inn: "Carbimazole"
predicted_indications: ["resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "neonatal thyrotoxicosis", "hyperthyroxinemia"]
---

# Carbimazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Carbimazole: From Hyperthyroidism to Resistance to Thyroid Hormone (THRB Mutation)

## One-Sentence Summary

Carbimazole is an antithyroid drug (a prodrug of methimazole) originally used to treat hyperthyroidism, Graves disease and thyrotoxicosis.
The TxGNN model predicts it may be effective for **resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta**, but there are **0 clinical trials** and only **1 publication** (a case report) for this prediction, and the mechanistic rationale is weak.
The more plausible related candidate is neonatal thyrotoxicosis, which is largely an extension of the existing indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperthyroidism, Graves disease, thyrotoxicosis (the approved-indication text is blank in the registration records, so this comes from the knowledge graph) |
| Predicted New Indication | Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta (RTH-beta) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 19 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, carbimazole is converted to methimazole, which inhibits thyroid peroxidase and reduces thyroid hormone synthesis. Its efficacy in hyperthyroidism is well established.

For RTH-beta, the rationale is weak and may be counterproductive. In this condition, tissues respond poorly to T3 because of THRB mutations. Circulating T4/T3 are elevated and TSH is not suppressed. Lowering hormone levels with an antithyroid drug would tend to raise TSH further, drive thyroid enlargement, and could worsen hypothyroidism in the resistant tissues. The high TxGNN score most likely reflects network proximity to hyperthyroid-like biochemistry (high free T4) rather than a true therapeutic rationale.

The only supporting literature is a case report of a young man whose RTH-like picture (elevated free T4 with non-suppressed TSH) went undiagnosed for 10 years. He was treated with carbimazole intermittently as "hyperthyroidism". It illustrates misdiagnosis, not therapeutic benefit.

### Other predicted indications in the data

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Neonatal thyrotoxicosis | 99.41% | L4 | Mechanistically plausible; antithyroid drugs are already standard care. Largely an extension of the existing indication to a specific population, not a novel repurposing. Evidence is mostly case reports, case series and reviews. |
| 3 | Hyperthyroxinemia | 99.21% | L4 | A laboratory phenotype with heterogeneous causes. Benefit is limited to cases that overlap with true hyperthyroidism. Antithyroid treatment is not indicated in binding-protein abnormalities or TSH-secreting adenoma. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/) | 2013 | Case report / differential diagnosis | BMJ Case Reports | Young man with elevated free T4 and non-suppressed TSH, treated intermittently with carbimazole for 10 years as hyperthyroidism. Highlights the differential diagnosis, not a therapeutic benefit. |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 217092 | Thyrodip 20mg Tablet (Lupin Ltd) | Bottle of 100 tablets | Not stated in the records |
| 150585 | Neo-Mercazole 20 Tablet (Abbott) | Bottle of 120 tablets | Not stated in the records |
| 206718 | Sterzole 20 Tablet (Captab Biotec) | Bottle of 100 tablets | Not stated in the records |
| 217783 | Thyrozole 5mg Tablet (Cadila Pharmaceuticals Ltd) | Strip of 10 tablets | Not stated in the records |
| 1021 | Anti-Thyrox 20 Tablet (Macleods Pharmaceuticals Pvt Ltd) | Bottle of 100 tablets | Not stated in the records |

There are 19 valid single-ingredient registrations in total, all oral tablets, with no cancelled registrations.

---

## Safety Considerations

Please refer to the package insert for safety information.

The literature compiled for the neonatal thyrotoxicosis candidate notes a possible association between fetal carbimazole exposure and choanal atresia (PMID 12124735, case report) and related congenital anomalies. This is relevant to any use in pregnancy. No drug-interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for RTH-beta is very high, but the prediction rests on model prediction alone (L5). There are no trials, the only publication is a misdiagnosis case report, and the pharmacology suggests lowering thyroid hormone could be counterproductive by further raising TSH. The score appears to be a network artefact.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank
- Package insert warnings and contraindications from the India regulatory source, which are currently missing and block safety screening
- Expert endocrinology review of whether any RTH-beta rationale exists at all; if not, deprioritise this candidate
- If pursuing a related direction, review neonatal thyrotoxicosis (L4) as an extension of the existing indication, with a specific pregnancy and neonatal safety assessment (e.g. choanal atresia signal)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

