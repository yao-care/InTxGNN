---
layout: default
title: Bempedoic Acid
parent: Model Prediction Only (L5)
nav_order: 94
evidence_level: L5
indication_count: 9
monitor_inn: "Bempedoic acid"
predicted_indications: ["hyperthyroidism", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "malignant catarrh", "infectious bovine rhinotracheitis", "cytomegalovirus infection", "hyperthyroxinemia", "drug-induced osteoporosis", "multiple endocrine neoplasia", "pregnancy associated osteoporosis"]
last_modified_at: 2026-11-20
description: "Bempedoic Acid: predicted new indication hyperthyroidism (evidence level L5). In India: 7 listed products (7 not discontinued)"
---

# Bempedoic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Bempedoic acid: ATP-citrate lyase inhibitor (lipid-lowering agent) → hyperthyroidism
{: .text-alpha }

## One-Sentence Summary

Bempedoic acid is an oral lipid-lowering drug that inhibits ATP-citrate lyase (ACLY) and is marketed in India.
The TxGNN model predicts it may be relevant to **hyperthyroidism**, but **no clinical trials and no publications** were found to support this direction.
This is a model-only prediction and should be treated as a hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | hyperthyroidism |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (7 of 7) – CDSCO approval status is not included in this data |
| Number of Listed Products | 7 (valid: 7) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bempedoic acid inhibits ATP-citrate lyase (ACLY) and is associated with AMPK-related pathways, which lowers LDL cholesterol. This description is based on general pharmacological knowledge. According to the Mechanism of Action section of the US FDA-approved prescribing information for bempedoic acid: "Bempedoic acid is an adenosine triphosphate-citrate lyase (ACL) inhibitor that lowers LDL-C by inhibition of cholesterol synthesis in the liver. ACL is an enzyme upstream of 3-hydroxy-3-methyl-glutaryl-coenzyme A (HMG-CoA) reductase in the cholesterol biosynthesis pathway." ([DailyMed: Nexletol (bempedoic acid) prescribing information, Esperion Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=88d06d89-a3da-40b4-b273-8f4f7d56c4c9), label version 2026-06-25; accessed 2026-11-19.)

No established mechanistic link connects this action to hyperthyroidism. Lipid metabolism and thyroid function are related in general, since thyroid hormones strongly influence cholesterol levels. However, that relationship does not show that an ACLY inhibitor would treat excess thyroid hormone production.

The high score is most likely an artifact of network propagation in the model rather than a biological signal. The prediction should be regarded as unsupported until independent evidence appears.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 25911 | Bemdac 180mg Tablet | Strip of 10 tablets | Not recorded |
| 25897 | Brillo 180mg Tablet | Strip of 10 tablets | Not recorded |
| 59914 | Dapcea Tablet | Strip of 10 tablets | Not recorded |
| 26507 | Belmore Tablet | Strip of 10 tablets | Not recorded |
| 25839 | Bempesta Tablet | Strip of 10 tablets | Not recorded |

---

## Safety Considerations

- **Drug Interactions**: 23 interactions were recorded in total. The main ones are:
  - **Major**: corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone, deflazacort, fludrocortisone), levofloxacin and simvastatin.
  - **Moderate**: empagliflozin, glyburide, repaglinide, rifaximin, rosuvastatin, selexipag, fexofenadine and revefenacin.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications, and no plausible mechanistic link to hyperthyroidism. The score alone is not enough to justify moving forward.

**To proceed, the following is needed:**
- Mechanistic evidence connecting ACLY inhibition or AMPK-related pathways to thyroid hormone regulation
- Preclinical or clinical studies that directly address hyperthyroidism
- Package insert warnings and contraindications from the India Pharma source
- Detailed mechanism-of-action data
- A safety review of the major interactions listed above, particularly with corticosteroids

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-20 | "Detailed mechanism-of-action data were not available in the data compiled for this report, so this description is based on general pharmacological knowledge" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt (revised 2026-11-20; earlier version kept in the record) | [DailyMed: Nexletol (bempedoic acid) prescribing information, Esperion Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=88d06d89-a3da-40b4-b273-8f4f7d56c4c9) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

