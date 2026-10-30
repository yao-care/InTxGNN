---
layout: default
title: Ivabradine
parent: Model Prediction Only (L5)
nav_order: 458
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-30
description: "Ivabradine: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not stated in the India license data compiled for this report"
monitor_inn: "Ivabradine"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ivabradine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Ivabradine: From Cardiovascular Use (Heart Failure / Heart-Rate Control) to hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Ivabradine is a heart-rate-lowering drug that blocks HCN channels (the If current) in the sinoatrial node, and it is widely marketed in India. The TxGNN model predicts it may be effective for **hypertrichosis**, but **no clinical trials and no publications** currently support this direction. The prediction is a network-based computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India license data compiled for this report (the licensed product names, e.g. "Beat HF", suggest heart failure use) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 0.9979 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ivabradine is not available in the data compiled for this report. Based on known pharmacology, ivabradine inhibits HCN channels (the If current) in the sinoatrial node, which lowers heart rate. Its established use is cardiovascular.

Mechanistically, the link to hypertrichosis is weak. There is no established connection between HCN channel inhibition and hair follicle biology or hair growth regulation. HCN channel expression in hair follicles is not an established pathway. Hypertrichosis is a known adverse effect of some drugs (for example minoxidil), but that is unrelated to HCN inhibition.

The high score (0.9979) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or a true mechanistic relationship. The other top predictions follow the same pattern. They are mostly congenital or genetic conditions that a heart-rate-lowering ion channel blocker is unlikely to correct:

| Rank | Predicted Disease | Score | Assessment |
|---|---|---|---|
| 2 | Ambras type hypertrichosis universalis congenita | 0.9972 | Genetic rearrangement near TRPS1 (chromosome 8q22); no plausible link to HCN blockade |
| 3 | Malformation syndrome with odontal and/or periodontal component | 0.9972 | Broad developmental category; no known role of ivabradine in tooth or periodontal development |
| 4 | Syndrome with a Dandy-Walker malformation as major feature | 0.9970 | Structural brain malformation; not a plausible pharmacological target |
| 5 | Isolated genetic hair shaft abnormality | 0.9969 | Structural keratin or protein defects; no link to HCN channels |
| 6 | Nephrogenic syndrome of inappropriate antidiuresis | 0.9908 | Caused by gain-of-function AVPR2 mutations; ivabradine does not act on this pathway |

## India Market Information

Twenty valid single-ingredient registrations were found. The approved indication text was empty for all of them. The first five are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 206226 | StayHappi Ivabradine 5mg Tablet (Sarvagunaushdhi Pvt Ltd) | Strip of 10 tablets | Not specified |
| 25936 | Beat HF 5 Tablet (Emcure Pharmaceuticals Ltd) | Strip of 10 tablets | Not specified |
| 108150 | Ivabratco 5 Tablet (Natco Pharma Ltd) | Strip of 10 tablets | Not specified |
| 108523 | Ivaniche 15mg Tablet (Alniche Life Sciences Pvt Ltd) | Strip of 10 tablets | Not specified |
| 108395 | Ivabid OD 15mg Tablet (Abbott) | Strip of 10 tablets | Not specified |

All products are oral tablets.

## Safety Considerations

- **Drug Interactions**: 138 interactions were recorded. The listing includes several Major-level interactions, for example:
  - Aprepitant
  - Clarithromycin
  - Cisapride
  - Clotrimazole
  - Cobicistat
  - Dolasetron
  - Granisetron
  - Levofloxacin
  - Ondansetron
  - Palonosetron
  - Papaverine
  
  Moderate-level interactions include famotidine, ranitidine, cimetidine, nizatidine, dexamethasone, miconazole, metreleptin and troglitazone.

Please refer to the package insert for warnings and contraindications, as this information was not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, and the mechanistic link between HCN channel inhibition and hypertrichosis, or any of the other top-ranked conditions, is not plausible. The drug's established safety profile does not justify pursuing a new indication without supporting evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator, which are required for safety screening
- Detailed mechanism-of-action data
- Preclinical evidence of HCN channel involvement in hair follicle biology
- Evidence of route compatibility and similarity to the original indication
- An approved-indication statement for the India licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

