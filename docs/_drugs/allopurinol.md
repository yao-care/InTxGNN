---
layout: default
title: Allopurinol
parent: Model Prediction Only (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Allopurinol: predicted new indication Hepatic porphyria (evidence level L5). Approved use: Gout"
monitor_inn: "Allopurinol"
predicted_indications: ["hepatic porphyria", "hepatopulmonary syndrome", "idiopathic copper-associated cirrhosis", "primitive portal vein thrombosis", "early-onset familial noncirrhotic portal hypertension", "hepatoportal sclerosis", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "idiopathic eosinophilic myositis"]
---

# Allopurinol
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

# Allopurinol: From Gout to Hepatic Porphyria

## One-Sentence Summary

Allopurinol is a xanthine oxidase inhibitor used for gout, hyperuricemia and acute urate nephropathy.
The TxGNN model predicts it may be effective for **hepatic porphyria**,
but there are currently **0 clinical trials** and only **2 indirect, non-clinical publications** (a hypothesis paper and a rat study), so the prediction rests almost entirely on the model.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout (also hyperuricemia and acute urate nephropathy, per the knowledge graph; no approved-indication text is available in the Indian licence records) |
| Predicted New Indication | Hepatic porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, allopurinol is a long-established urate-lowering agent, its efficacy in gout and hyperuricemia is well recognised, and it may mechanistically touch on purine and oxidative metabolism that could in theory relate to hepatic haem pathways.

The link to hepatic porphyria is weak. The only support is a 2019 hypothesis paper on metabolic targeting of 5-aminolevulinate synthase (ALAS1), the rate-limiting enzyme of haem biosynthesis, and a 1992 rat study on how carbamazepine affects hepatic haem metabolism. Neither tests allopurinol as a treatment in people with porphyria.

Porphyria patients are also sensitive to many drugs that induce ALAS1, so any use would need a careful porphyrinogenicity review. The very high TxGNN score reflects a graph-based signal, not demonstrated efficacy.

Other top-ranked predictions (hepatopulmonary syndrome, idiopathic copper-associated cirrhosis, portal vein and portal hypertension conditions, immune-mediated necrotizing myopathy, antisynthetase syndrome, eosinophilic myositis, and a disorder of phenylalanine metabolism) have no direct clinical evidence either.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis/Review | Medical Hypotheses | Proposes targeting liver ALAS1 via tryptophan or inhibitors of haem utilisation by tryptophan 2,3-dioxygenase as therapy for acute hepatic porphyrias; not specific to allopurinol |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Animal study (rat) | Biochemical Pharmacology | Acute carbamazepine affected hepatic haem metabolism in rats, relevant to how drugs exacerbate hepatic porphyrias |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 246755 | Zyrik 300 Tablet | Strip of 10 tablets | Not specified in available records |
| 235796 | Vriloric 100mg Tablet | Strip of 10 tablets | Not specified in available records |
| 126377 | Lodiric-SR 250mg Capsule | Strip of 10 SR capsules | Not specified in available records |
| 20861 | Allric 100mg Tablet | Strip of 10 tablets | Not specified in available records |
| 16043 | Ausric 300 Tablet | Strip of 10 tablets | Not specified in available records |

A total of 20 valid single-ingredient registrations exist, all oral forms (tablets, SR tablets, SR capsules).

## Safety Considerations

- **Contraindication-related conditions (from knowledge graph, not label text)**: liver disease, gallbladder disease, impaired renal function, hypersensitivity vasculitis, cutaneous leukocytoclastic angiitis, allergic cutaneous vasculitis, anti-glomerular basement membrane disease. Liver disease is notable because the predicted indication is hepatic.
- **Drug Interactions**: 217 interactions are recorded. Moderate-level ones include aluminum hydroxide, attapulgite, kaolin, magaldrate and sucralfate. Minor ones include amoxicillin and chlorpropamide. Many others (e.g., metformin, omeprazole, pantoprazole, glimepiride, morphine, doxycycline) have an unclassified severity level.
- **Other concern**: Allopurinol is a known cause of hypersensitivity reactions with eosinophilia (e.g., DRESS), and porphyria patients are sensitive to drugs that induce ALAS1.

Please refer to the package insert for full warnings, as label-based warnings were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but support is limited to one hypothesis paper and one rat study, with no clinical trials and no human data in porphyria. Safety data from the label is also missing, and liver disease appears among the graph-based contraindications.

**To proceed, the following is needed:**
- Mechanism of action data for allopurinol and a defined hypothesis for its effect on haem biosynthesis
- Preclinical or in vitro studies of allopurinol in porphyria models
- A formal porphyrinogenicity review, since porphyria patients react to many drugs
- Package insert warnings and contraindications from Indian regulatory sources
- Review of the liver-disease contraindication signal in this population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

