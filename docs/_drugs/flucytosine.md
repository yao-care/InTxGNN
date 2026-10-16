---
layout: default
title: Flucytosine
parent: Model Prediction Only (L5)
nav_order: 359
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Flucytosine: predicted new indication Bone Paget disease (evidence level L5). Approved use: Not available"
---

# Flucytosine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Flucytosine: From Antifungal Therapy to Bone Paget Disease

## One-Sentence Summary

Flucytosine is an antifungal prodrug marketed in India as 500 mg tablets. The TxGNN model predicts it may be effective for **bone Paget disease**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the approved indication text in the India licences is blank; flucytosine is known as an antifungal) |
| Predicted New Indication | Bone Paget disease |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled record. Based on general pharmacology, flucytosine is an antifungal prodrug. Fungal cytosine deaminase converts it to 5-fluorouracil (5-FU), which inhibits thymidylate synthase and disrupts RNA and DNA synthesis. Mammalian cells have little cytosine deaminase activity, so systemic conversion is minimal, although gut flora can convert some.

No established biological link to Paget disease of bone was identified. That disease involves dysregulated osteoclast activity (for example SQSTM1/p62 mutations and RANKL/NF-κB signalling) and is treated mainly with bisphosphonates. The very high TxGNN score is a knowledge-graph prediction and does not reflect an identified mechanism.

One speculative possibility is that 5-FU-derived antimetabolite effects could affect the proliferation of osteoclast precursors. There is no supporting evidence for this. Flucytosine's toxicities (bone marrow suppression, hepatotoxicity, accumulation when kidney function is impaired) and its many known drug interactions make repurposing for a chronic disease that already has effective treatment unfavourable.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 40974 | Cytoflu 500mg Tablet (Jolly Healthcare) | Bottle of 50 tablets | Not stated |
| 36269 | Cytorx 500mg Tablet (Cipla Ltd) | Strip of 10 tablets | Not stated |
| 36184 | Cytoflu 500mg Tablet (Jolly Healthcare) | Bottle of 100 tablets | Not stated |
| 36263 | Cytoflu 500mg Tablet (Jolly Healthcare) | Strip of 10 tablets | Not stated |

## Safety Considerations

- **Disease-level contraindication signals (from the TxGNN knowledge graph, not from label text):**
  - Kidney disease, pyoureter, liver disease, gallbladder disease and potassium deficiency.
  - Blood disorders, including thrombocytopenia, leukopenia, agranulocytosis, neutropenia (including several congenital forms), cyclic hematopoiesis, and acquired aplastic anaemia and aplastic anaemia.
- **Drug Interactions:** 85 interactions are recorded. The major one listed is **deferiprone**. Moderate interactions include:
  - amphotericin B (including lipid, liposomal and cholesteryl sulfate forms);
  - aminoglycosides and other antibiotics (kanamycin, neomycin, streptomycin, vancomycin, polymyxin B, bacitracin);
  - aminosalicylates (mesalazine, balsalazide, olsalazine, sulfasalazine);
  - deferasirox, pentamidine, ibuprofen, iobenguane (I-131) and strontium-89 chloride.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score, with no clinical trials, no literature and no identified mechanism linking flucytosine to Paget disease. Bisphosphonates already treat the disease effectively, and flucytosine's bone marrow, liver and kidney toxicity profile is unfavourable for chronic use.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India licences (currently a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- Preclinical evidence of any effect on osteoclast biology or Paget disease models
- Confirmation of the approved indication text for the India licences
- Route and formulation compatibility assessment for the new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

