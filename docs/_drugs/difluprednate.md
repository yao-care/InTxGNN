---
layout: default
title: Difluprednate
parent: Model Prediction Only (L5)
nav_order: 267
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Difluprednate: predicted new indication Familial adrenal hypoplasia with absent pituitary luteinizing hormone (evidence level L5). Approved use: Postoperative ocular inflammation and pain, and anteri…"
monitor_inn: "Difluprednate"
predicted_indications: ["familial adrenal hypoplasia with absent pituitary luteinizing hormone", "seborrheic keratosis", "PAGOD syndrome", "vulvar inverted follicular keratosis", "adrenocortical insufficiency", "seborrheic dermatitis", "46,XY disorder of sex development", "necrobiosis lipoidica", "nephrotic syndrome", "iris disease"]
---

# Difluprednate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Difluprednate: From Ocular Inflammation to Familial Adrenal Hypoplasia with Absent Pituitary Luteinizing Hormone
{: .text-alpha }

## One-Sentence Summary

Difluprednate is a topical ophthalmic corticosteroid, used to treat eye inflammation and pain after ocular surgery and anterior uveitis.
The TxGNN model predicts it may be effective for **familial adrenal hypoplasia with absent pituitary luteinizing hormone**, but **no clinical trials and no publications** currently support this prediction.
The prediction is a computational signal only and does not hold up on mechanistic review.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postoperative ocular inflammation and pain, and anterior uveitis (based on pharmacology data; no approved indication text is recorded in the India licence entries) |
| Predicted New Indication | Familial adrenal hypoplasia with absent pituitary luteinizing hormone |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 19 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled dataset. Based on known pharmacology, difluprednate is a synthetic glucocorticoid that acts as an agonist at the glucocorticoid receptor (NR3C1). A receptor binding assay reported a Ki of 0.78 nM. Its efficacy in ocular inflammation is established.

The prediction most likely comes from the link between the glucocorticoid class and adrenal disorders in the knowledge graph. However, this condition is a congenital developmental disorder. Its standard of care is hormone replacement, not anti-inflammatory steroid therapy. Difluprednate is a topical ocular product with no evidence of systemic exposure adequate for replacement. **No plausible mechanism supports a benefit**, so the high score appears to reflect graph proximity rather than a real therapeutic link.

### Other Predicted Indications Reviewed

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Seborrheic keratosis | 99.96% | L5 | Benign growth, not inflammatory; steroids not an established treatment |
| 3 | PAGOD syndrome | 99.93% | L5 | Ultra-rare malformation syndrome; no inflammatory target |
| 4 | Vulvar inverted follicular keratosis | 99.92% | L5 | Benign lesion usually excised; no supporting data |
| 5 | Adrenocortical insufficiency | 99.67% | L5 | Class link plausible, but ocular product gives no adequate systemic exposure; prolonged use may suppress the HPA axis |
| 6 | Seborrheic dermatitis | 99.53% | L5 | Research question: topical steroids are established, but no difluprednate data and the emulsion is not made for skin |
| 7 | 46,XY disorder of sex development | 99.47% | L5 | Genetic/endocrine disorder; glucocorticoid activity not relevant |
| 8 | Necrobiosis lipoidica | 99.24% | L5 | Research question: class-level rationale only; skin atrophy risk |
| 9 | Nephrotic syndrome | 99.21% | L5 | Systemic steroids are the appropriate option; topical ocular use would not reach relevant exposure |
| 10 | Iris disease | 99.16% | L4 | Research question: plausible, but likely overlaps with existing labelled uses (anterior uveitis) |

## Clinical Trial Evidence

Currently no related clinical trials registered for the top predicted indication.

## Literature Evidence

Currently no related literature available for the top predicted indication.

For reference, the only publication found across the top ten predictions relates to iris disease (rank 10):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21182429](https://pubmed.ncbi.nlm.nih.gov/21182429/) | 2011 | Preclinical PK study (rabbit) | J Ocul Pharmacol Ther | Pharmacokinetic and pharmacodynamic features of difluprednate ophthalmic emulsion compared with other ophthalmic agents, using a glucocorticoid receptor-binding bioassay |

## India Market Information

All 19 registrations are valid single-ingredient ophthalmic products. Approved indication text is not recorded for these entries. The main authorizations are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 176619 | Prednate Eye Drop | Bottle of 5 ml Eye Drop | Not recorded |
| 61843 | Diflusap Eye Drop | Bottle of 5 ml Ophthalmic Emulsion | Not recorded |
| 84886 | Flupred 0.05% Eye Drop | Packet of 5 ml Ophthalmic Emulsion | Not recorded |
| 89156 | Flurocart 0.05% Eye Drop | Bottle of 5 ml Eye Drop | Not recorded |
| 231299 | Uvefrost Eye Drop | Packet of 5 ml Eye Drop | Not recorded |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** The TxGNN knowledge graph lists contraindication links with ocular hypertension, herpes simplex virus keratitis, ocular tuberculosis and mycotic corneal ulcer. These should be verified against the official package insert.
- **Drug Interactions:** The only interaction record is a pharmacological one: difluprednate acts on the glucocorticoid receptor (NR3C1) as an agonist. No drug-drug interactions are listed.
- **Systemic effects:** Prolonged topical ocular steroid use can suppress the HPA axis. This is a safety concern for adrenal-related indications, not a benefit.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no clinical or literature support and no plausible mechanism. It is a congenital developmental disorder treated with replacement therapy, and a topical ocular steroid would not provide adequate systemic exposure. The evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator or manufacturer websites
- Detailed mechanism of action data (for example, via DrugBank)
- Approved indication text for the India registrations
- For any future repurposing work, redirect attention to the lower-ranked "Research Question" candidates (seborrheic dermatitis, necrobiosis lipoidica, iris disease). These would need difluprednate-specific data and a suitable formulation and route, since the current products are ophthalmic only.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

