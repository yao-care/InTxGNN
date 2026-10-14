---
layout: default
title: Benzoic Acid
parent: Model Prediction Only (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Benzoic Acid
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

# Benzoic Acid: From Fibrosing Skin and Connective Tissue Conditions to Bronchitis

## One-Sentence Summary

Benzoic acid is a small organic acid, in India marketed as a single-ingredient topical ointment. The data compiled for this report link it to fibrosing and autoimmune skin conditions such as Peyronie disease, scleroderma and pemphigus.
The TxGNN model predicts it may be effective for **bronchitis**, but **no clinical trials** and **no relevant publications** support this prediction, so it rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pemphigus, Peyronie disease, penile fibromatosis, balanitis xerotica obliterans, scleroderma, localized scleroderma, systemic sclerosis, dermatomyositis (from the knowledge graph; the Indian licence records contain no indication text) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Benzoic acid is known as a preservative and a metabolic intermediate, and the data compiled for this report do not establish how it would act in the original indications or in bronchitis.

The prediction comes from the TxGNN knowledge-graph model, which scores drug-disease pairs by network proximity. The score is very high (99.98%), but it is a graph-based inference only. The two publications retrieved for bronchitis, a repaglinide review in type 2 diabetes and a soluble epoxide hydrolase inhibitor study in smoke-induced COPD, do not study benzoic acid. They therefore provide no direct support, and no credible mechanistic link between benzoic acid and bronchitis can be drawn from the available data.

By contrast, other predictions on the list are more coherent with the original indications. Palmar fibromatosis, Ledderhose disease and infantile digital fibromatosis share a fibrotic phenotype with Peyronie disease and scleroderma. These are the more biologically plausible directions, though they too have no trial or literature support and are only research questions at this stage.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publication retrieved studies benzoic acid in bronchitis. The two papers below are tangential only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11577798](https://pubmed.ncbi.nlm.nih.gov/11577798/) | 2001 | Review | Drugs | Review of repaglinide, a benzoic acid derivative, in type 2 diabetes. It does not study benzoic acid or bronchitis. |
| [22180869](https://pubmed.ncbi.nlm.nih.gov/22180869/) | 2012 | Preclinical | Am J Respir Cell Mol Biol | Soluble epoxide hydrolase inhibitor in smoke-induced COPD. It does not involve benzoic acid. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 60907 | Dersol BH Ointment | Tube of 30 gm ointment | Not stated |
| 115674 | Keralin Ointment | Tube of 15 gm ointment | Not stated |
| 72830 | Exsora Ointment | Tube of 15 gm ointment | Not stated |

All three are valid single-ingredient topical products. Topical ointments are not a plausible route for treating bronchitis, so route compatibility with the predicted indication is also unresolved.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** The knowledge graph links benzoic acid to contraindication-type associations with many conditions. The main groups are:
  - Liver and kidney disease, including liver failure
  - Cardiovascular conditions: hypertension, coronary artery disease, heart conduction disease and sudden cardiac arrest
  - Diabetes and diabetic ketoacidosis
  - Bleeding disorders such as hemophilia
  - G6PD deficiency, anemia, and metabolic disorders such as galactosemia and cystinuria
  - Myasthenia gravis and other neuromuscular junction disease
  - Gastritis and gallbladder disease
- **Dry eye note:** Benzoate-type preservatives are used in ophthalmic products and raise an ocular-surface toxicity concern, which argues against the dry eye prediction.

These associations come from the graph, not from product labelling, and should be verified against the package inserts. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction is supported only by a high model score, with no trials and no literature that study benzoic acid. The mechanism is undefined, and the available topical ointments do not match a respiratory indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the three Indian products (currently a blocking gap for safety screening)
- Mechanism of action data for benzoic acid (for example from DrugBank)
- Direct preclinical or clinical evidence in bronchitis, or a re-prioritisation toward the fibrosis-related predictions (palmar fibromatosis, Ledderhose disease), which fit the original indications better
- An assessment of route and formulation compatibility with any proposed new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

