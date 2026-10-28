---
layout: default
title: Carbimazole
parent: Model Prediction Only (L5)
nav_order: 145
evidence_level: L5
indication_count: 2
monitor_inn: "Carbimazole"
predicted_indications: ["resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "hyperthyroxinemia"]
last_modified_at: 2026-10-27
description: "Carbimazole: predicted new indication resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta (evidence level L5). Approved use: Not recorded in the local data"
---

# Carbimazole
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

## Carbimazole: Antithyroid thionamide prodrug (methimazole) → resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta
{: .text-alpha }

## One-Sentence Summary

Carbimazole is an antithyroid drug that is converted in the body to methimazole and lowers thyroid hormone production.
The TxGNN model predicts it may be useful for **resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta**, but there are **no clinical trials** and only **1 case report** on this disease, so the evidence is model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 19 of 19) |
| Number of Registrations | 19 (valid: 19) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Carbimazole is known as a prodrug of methimazole, which inhibits thyroid peroxidase and reduces thyroid hormone synthesis.

In resistance to thyroid hormone caused by THRB mutations, tissues respond poorly to T3. Circulating T4 and T3 are high while TSH is not suppressed. The model likely scored this disease highly because its biochemistry (high free T4) resembles hyperthyroid states.

The mechanistic link is weak, and the approach could be counterproductive. Lowering hormone levels with an antithyroid drug would tend to raise TSH further, promote thyroid enlargement, and could worsen hypothyroidism in the already resistant tissues. The high score should therefore be read as network proximity, not as a therapeutic rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/) | 2013 | Case report / differential diagnosis | BMJ Case Reports | A young man had been labelled hyperthyroid for 10 years, with persistently high free T4 and non-suppressed TSH, and was treated intermittently with carbimazole. The report discusses how to distinguish this pattern from true hyperthyroidism. It does not show that carbimazole benefits resistance to thyroid hormone. |

## India Market Information

Carbimazole is marketed in India under multiple single-ingredient tablet licences (for example Neo-Mercazole, Anti-Thyrox, Thyrodip, Carkozom). The local records do not carry approved-indication text.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials and no study showing benefit in this disease. The mechanism suggests antithyroid treatment could raise TSH and worsen tissue hypothyroidism.

**To proceed, the following is needed:**
- Mechanism of action data and a clear mechanistic argument for why lowering hormone synthesis would help in THRB-mutation resistance
- Studies directly addressing this disease, including safety with respect to TSH rise and goitre
- Package insert warnings and contraindications for safety screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

