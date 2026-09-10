---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 414
evidence_level: L5
indication_count: 7
---

# Ibuprofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Ibuprofen: From Pain/Inflammation to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ibuprofen is a widely used NSAID; detailed original-indication and mechanism-of-action data were not available in this evidence pack. The TxGNN model's top prediction is **Acromesomelic Dysplasia, Hunter-Thompson Type**, an ultra-rare genetic skeletal disorder, but this is currently supported by **0 clinical trials** and **0 publications** — the prediction rests entirely on knowledge-graph statistics.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in source data (Ibuprofen is a well-known NSAID generally indicated for pain, fever, and inflammation) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for Ibuprofen is not available in this evidence pack (`original_moa: [Data Gap]`), and no original indications were recorded. Based on general pharmacological knowledge, Ibuprofen is a propionic-acid-derivative NSAID that inhibits COX-1/COX-2, reducing prostaglandin synthesis to relieve pain, fever, and inflammation.

Acromesomelic Dysplasia, Hunter-Thompson Type is caused by mutations in the GDF5/CDMP1 gene affecting cartilage morphogenesis signaling — it is a structural/developmental disorder, not a primary inflammatory disease. The only plausible mechanistic bridge is symptomatic: NSAIDs could theoretically relieve secondary joint pain or early-onset osteoarthritis that may accompany this and related skeletal dysplasias, but this would not modify the underlying disease process.

Notably, all seven TxGNN-predicted indications in this evidence pack are rare skeletal/developmental syndromes (brachyolmia variants, pseudoachondroplasia, brachydactyly-syndactyly syndrome, myosclerosis, colobomatous microphthalmia-rhizomelic dysplasia syndrome) clustered at similarly high scores (99.6–99.7%) with identical L5/Hold status and zero trials or literature for any of them. This pattern suggests the model is picking up a broad embedding-space association between NSAIDs and skeletal-disease nodes rather than a disease-specific signal, and none of the seven should be treated as differentiated leads without further mechanistic or clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

- **Drug Interactions**: DDI database records 687 total interactions for Ibuprofen. Representative interactions from this evidence pack:
  - **Major**: Acetylsalicylic acid (Aspirin)
  - **Moderate**: Acetohexamide, Aprepitant, Balsalazide, Betamethasone, Budesonide, Chlorpropamide, Dexamethasone, Dexfenfluramine, Exenatide, Fenfluramine, Glimepiride, Glipizide, Glyburide, Hydrocortisone, Kanamycin, Levofloxacin
  - **Minor**: Famotidine, Ranitidine, Cimetidine

Detailed prescribing warnings and contraindications are not yet available in this evidence pack; please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All seven candidate indications, including the top-ranked Acromesomelic Dysplasia, Hunter-Thompson Type, are L5 (model-prediction-only) with zero supporting trials or literature and a weak-to-absent mechanistic rationale. Combined with a blocking data gap on TFDA label warnings/contraindications and the drug's unmarketed status in Taiwan (0 registrations), this candidate cannot proceed to safety evaluation.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a blocking data gap (DG001)
- Confirmed DrugBank mechanism-of-action data (DG002)
- Preclinical or case-level evidence directly linking Ibuprofen to any of the seven predicted rare skeletal disorders
- Clarification of Taiwan market/import status given the drug is currently not marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

