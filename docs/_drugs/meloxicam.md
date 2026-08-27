---
layout: default
title: Meloxicam
parent: 僅模型預測 (L5)
nav_order: 413
evidence_level: L5
indication_count: 10
---

# Meloxicam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Meloxicam: From Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Meloxicam is a preferential COX-2 inhibitor NSAID, clinically established for osteoarthritis, rheumatoid arthritis, and inflammatory musculoskeletal conditions.
The TxGNN model's top-ranked prediction is **Acromesomelic Dysplasia, Hunter-Thompson Type** (score 99.92%), a rare skeletal dysplasia with no mechanistic link to COX-2 inflammation pathways; among all 10 predicted indications, the most clinically coherent candidates are **Spondyloarthropathy** (Rank 6) and **RF-positive Polyarticular Juvenile Idiopathic Arthritis** (Rank 8), both reaching L3 evidence level.
Currently, the top-ranked indication is supported by **0 clinical trials** and **0 publications**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoarthritis, Rheumatoid Arthritis, Inflammatory Pain |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Meloxicam is a preferential COX-2 inhibitor of the oxicam class, selectively suppressing cyclooxygenase-2 to reduce prostaglandin E2 (PGE2) synthesis. This translates to anti-inflammatory, analgesic, and antipyretic effects that underpin its established use in chronic inflammatory joint diseases such as osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis.

Acromesomelic Dysplasia, Hunter-Thompson Type is a rare autosomal recessive skeletal dysplasia arising from loss-of-function mutations in the *GDF5* gene (Growth Differentiation Factor 5). GDF5 is a bone morphogenetic protein critical for limb chondrogenesis; its deficiency causes disproportionate shortening of the middle and distal limb segments through a developmental — not inflammatory — mechanism. This pathway has no established intersection with the COX-2/PGE2 axis that Meloxicam modulates.

The high TxGNN score most likely reflects topological proximity in the knowledge graph between skeletal dysplasia disease nodes that share structural annotation features with inflammatory joint diseases (e.g., shared "musculoskeletal system" ontology branches), rather than genuine pharmacological plausibility. This is a recognised limitation of graph neural network repurposing models: high scores can emerge from structural graph similarity rather than mechanistic relevance. No clinical or preclinical evidence exists to support this prediction, and it should be treated as a model artefact requiring manual expert triage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Meloxicam currently has **no registered products** in the Indian market. No authorizations are on record in the regulatory dataset.

> Note: Meloxicam is approved in multiple major markets globally (FDA, EMA, Japan PMDA) for osteoarthritis and rheumatoid arthritis. Its absence from the India regulatory dataset warrants verification against the current CDSCO database, as registration status may have changed after the data cutoff of 2026-04-04.

---

## Safety Considerations

**Drug Interactions (273 interactions identified; selected clinically significant moderate-level interactions shown):**

| Interacting Drug | Level | Clinical Concern |
|-----------------|-------|-----------------|
| Hydrocortisone | Moderate | NSAID + systemic corticosteroid: additive GI mucosal injury and bleeding risk |
| Dexamethasone | Moderate | NSAID + corticosteroid: additive GI mucosal injury and bleeding risk |
| Betamethasone | Moderate | NSAID + corticosteroid: additive GI mucosal injury and bleeding risk |
| Triamcinolone | Moderate | NSAID + corticosteroid: additive GI mucosal injury and bleeding risk |
| Budesonide | Moderate | NSAID + corticosteroid: additive GI mucosal injury and bleeding risk |
| Acetylsalicylic acid | Moderate | Dual antiplatelet/NSAID exposure: substantially elevated GI and cardiovascular bleeding risk |
| Metformin | Moderate | NSAIDs may reduce renal clearance of metformin; monitor for lactic acidosis risk |
| Glimepiride | Moderate | NSAIDs may potentiate sulfonylurea hypoglycaemic effect; monitor blood glucose |
| Vancomycin | Moderate | Additive nephrotoxicity; renal function monitoring required |
| Kanamycin | Moderate | Additive nephrotoxicity; renal function monitoring required |

A total of **273 drug-drug interactions** were identified in the DDInter database. Key warnings and contraindications data are not available in this Evidence Pack (Data Gap DG001). Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction — Acromesomelic Dysplasia, Hunter-Thompson Type — has no mechanistic plausibility, no clinical trial support, and no published literature (L5), making it unsuitable for drug repurposing development at this time. The high model score is attributable to knowledge graph topology artefacts rather than pharmacological signal. Of note, two lower-ranked predictions — **Spondyloarthropathy (Rank 6, L3, "Proceed with Guardrails")** and **RF-positive Polyarticular JIA (Rank 8, L3, "Proceed with Guardrails")** — have substantially stronger mechanistic rationale consistent with Meloxicam's known COX-2 mechanism, and should be prioritised for dedicated separate evaluation.

**To proceed, the following is needed:**
- **Resolve DG001 (Blocking):** Retrieve and parse the package insert from CDSCO/TFDA to obtain warnings and contraindications — required before any safety assessment can be completed
- **Resolve DG002 (High):** Query DrugBank API for full MOA data to enable mechanistic linkage analysis
- **Re-prioritise candidate indications:** Commission dedicated evidence reviews for Spondyloarthropathy (Rank 6) and RF-positive Polyarticular JIA (Rank 8), which have established NSAID mechanistic rationale and existing observational evidence
- **Verify India registration status:** Cross-check current CDSCO database directly, as Meloxicam is globally approved and the "Not Marketed" status may reflect a data gap rather than true market absence
- **Assess India-specific unmet need:** Evaluate epidemiology of SpA and JIA in India to determine clinical and market rationale before committing to regulatory strategy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

