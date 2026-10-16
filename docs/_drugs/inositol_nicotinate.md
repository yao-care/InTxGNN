---
layout: default
title: Inositol Nicotinate
parent: Model Prediction Only (L5)
nav_order: 433
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Inositol Nicotinate: predicted new indication Vitamin deficiency disorder (evidence level L5). Approved use: Pellagra, beriberi"
monitor_inn: "Inositol nicotinate"
predicted_indications: ["vitamin deficiency disorder", "biotin metabolic disease", "non-syndromic esophageal malformation", "iron deficiency anemia", "acute urate nephropathy", "esophageal disease", "early-onset familial noncirrhotic portal hypertension", "idiopathic copper-associated cirrhosis", "hepatoportal sclerosis", "hepatopulmonary syndrome"]
---

# Inositol Nicotinate
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

# Inositol Nicotinate: From Pellagra and Beriberi to Vitamin Deficiency Disorder

## One-Sentence Summary

Inositol nicotinate is a hexanicotinate ester of inositol that releases nicotinic acid (niacin, vitamin B3) in the body. It was originally associated with the treatment of pellagra and beriberi.
The TxGNN model predicts it may be effective for **vitamin deficiency disorder**, but the data compiled for this report contain **no clinical trials and no publications** supporting this prediction. It is essentially a model-based extension of the original indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pellagra, beriberi (from the knowledge-graph indication edges; the Indian licence records contain no indication text) |
| Predicted New Indication | Vitamin deficiency disorder |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only; no trials or literature supplied) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, inositol nicotinate is hydrolysed in the body to release nicotinic acid (vitamin B3), and niacin deficiency is the cause of pellagra, so it is mechanistically plausible for correcting vitamin deficiency states.

The predicted indication, vitamin deficiency disorder, is a broad category that already contains the original indication (pellagra). The prediction is therefore biologically plausible, but it is better viewed as an extension of the existing use than as a true repurposing. Niacin does not replace other vitamins, so any benefit would be limited to niacin-related deficiency.

Other predictions generated for this drug are weaker. The data compiled for this report show that they lack supporting evidence and are likely to reflect knowledge-graph artifacts:
- **Biotin metabolic disease**: Niacin and biotin are both B-complex vitamins, but niacin does not correct biotin metabolism defects.
- **Iron deficiency anaemia**: Only a speculative link exists. Iron replacement is the standard treatment.
- **Acute urate nephropathy**: Nicotinic acid can raise serum uric acid, so it may worsen rather than benefit this condition.
- **Oesophageal and liver-related conditions** (non-syndromic oesophageal malformation, oesophageal disease, early-onset familial noncirrhotic portal hypertension, idiopathic copper-associated cirrhosis, hepatoportal sclerosis, hepatopulmonary syndrome): No plausible mechanism was identified. Niacin derivatives also carry a hepatotoxicity concern.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 76336 | Ergovas Tablet | Strip of 10 tablets | Not stated in the records |
| 104663 | Hexolip 500 Tablet | Strip of 10 tablets | Not stated in the records |
| 104701 | Hexolip 1000 Tablet | Strip of 10 tablets | Not stated in the records |
| 150521 | Niacin NF Tablet | Strip of 10 tablets | Not stated in the records |

All four registrations are valid single-ingredient oral products. None has been cancelled.

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (drug-disease contraindication edges, not package insert text):
  - Liver and gallbladder: liver disease, gallbladder disease
  - Metabolic: hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, gout, hypophosphataemia
  - Bleeding and blood: thrombocytopenia, blood coagulation disease, haemoglobinopathy
  - Cardiovascular and cerebrovascular: acute coronary syndrome, coronary artery disease, myocardial infarction, coronary thrombosis, stroke disorder, cerebrovascular disorder, cerebral infarction, cerebral artery occlusion, brain stem infarction, hypotensive disorder
  - Other: peptic ulcer disease, substance abuse/dependence
- **Specific cautions linked to the predictions**: Nicotinic acid may raise uric acid levels (relevant to gout and urate nephropathy), and high-dose niacin is associated with hepatotoxicity (relevant to liver disease). Its vasodilatory effect may also be a concern in conditions involving vascular dilation.

No drug interaction records were found. For label-based warnings, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has a high model score but no supporting clinical trials or literature, and it largely overlaps with the drug's original use in niacin deficiency. The remaining predictions have no plausible mechanism, and some carry safety concerns. The knowledge graph also lists many contraindicated conditions.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed Indian products (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for the Indian registrations
- A literature and clinical trial search for inositol nicotinate or niacin in the specific vitamin deficiency states of interest
- Clarification of whether vitamin deficiency disorder represents a meaningfully new use beyond pellagra
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

