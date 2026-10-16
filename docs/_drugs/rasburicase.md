---
layout: default
title: Rasburicase
parent: Model Prediction Only (L5)
nav_order: 729
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Rasburicase: predicted new indication Hypouricemia, renal (evidence level L5). Approved use: Hyperuricemia"
---

# Rasburicase
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

# Rasburicase: From Hyperuricemia to Renal Hypouricemia

## One-Sentence Summary

Rasburicase is a recombinant urate oxidase originally used to lower uric acid in hyperuricemia.
The TxGNN model predicts it may be effective for **renal hypouricemia**, but **no clinical trials and no publications** currently support this prediction.
The mechanism also argues against it, so the prediction appears to be a knowledge-graph artifact rather than a real therapeutic opportunity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperuricemia (obsolete disease term in the knowledge graph); no approved indication text is available for the Indian licenses |
| Predicted New Indication | Hypouricemia, renal |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, rasburicase is a recombinant urate oxidase. It converts uric acid to allantoin, which is more soluble, and so lowers serum uric acid. Its efficacy in hyperuricemia follows directly from this action.

Renal hypouricemia, however, is already a state of low serum uric acid, typically caused by loss-of-function in urate transporters such as URAT1 or GLUT9. Depleting urate further is mechanistically counterproductive and could add risk. The high TxGNN score most likely comes from the shared urate-metabolism node in the graph, not from a rational therapeutic link.

Other predictions in the top 10 are also weak. Partial HPRT deficiency has some biological plausibility for acute urate lowering. Rasburicase does not correct the enzyme defect, though, and it is a parenteral, immunogenic protein unsuited to chronic use, while oral xanthine oxidase inhibitors are already established. Hepatic porphyria, hepatopulmonary syndrome, portal vein disorders, copper-associated cirrhosis, renal tubular acidosis and phenylalanine metabolism disorders show no identifiable mechanistic link. They appear to reflect graph proximity only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 187418 | Rasby Injection (Intas Pharmaceuticals Ltd) | Vial of 1 injection | Not stated |
| 186904 | Rascas 1.5mg Injection (Sayre Therapeutics Pvt Ltd) | Vial of 1 injection | Not stated |
| 186229 | Rasburnat Injection (Natco Pharma Ltd) | Vial of 1 injection | Not stated |
| 188807 | Rasbelon Injection (Celon Laboratories Ltd) | Vial of 1 injection | Not stated |
| 189498 | Rasuric 1.5mg Injection (Aureate Healthcare Pvt Ltd) | Vial of 1 injection | Not stated |

## Safety Considerations

- **Drug Interactions**: 13 interactions were identified. Two are rated Major and the rest Moderate.
  - **Major**: prilocaine and nitrous acid.
  - **Moderate**: local anaesthetics (topical or ophthalmic tetracaine, lidocaine, benzocaine, cocaine, proparacaine, oxybuprocaine and cinchocaine) and idelalisib.

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5), with no trials or literature. The mechanism runs against it, because further uric acid lowering in a condition of already low uric acid could cause harm. The other top-ranked predictions have no plausible mechanistic basis either.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator's sources. These are currently missing and block safety screening.
- Detailed mechanism of action data from DrugBank
- Preclinical or clinical evidence that urate depletion is beneficial in any of the predicted conditions
- If any prediction is pursued, a review of partial HPRT deficiency first, since it has the most biological plausibility. Rasburicase would need to show a clear advantage over xanthine oxidase inhibitors, and immunogenicity and the parenteral route would need to be addressed.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

