---
layout: default
title: Cefetamet
parent: Model Prediction Only (L5)
nav_order: 154
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cefetamet: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not stated in the data compiled for this report . Based on its drug c…"
monitor_inn: "Cefetamet"
predicted_indications: ["rheumatoid arthritis", "osteoarthritis", "osteoarthritis susceptibility", "gout", "hemoglobinopathy", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia", "beta-thalassemia with other manifestations", "acromesomelic dysplasia, Hunter-Thompson type"]
---

# Cefetamet
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

# Cefetamet: From Bacterial Infection (Antibacterial Use) to Rheumatoid Arthritis

## One-Sentence Summary

Cefetamet is a third-generation oral cephalosporin antibiotic (given as its prodrug, cefetamet pivoxil) and is currently marketed in India as single-ingredient tablets.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but **no clinical trials and no publications** currently support this prediction.
It is a computational signal only and should be treated as a low-confidence hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the approved indication text on all Indian licences is blank). Based on its drug class, it is an antibacterial. |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 97.99% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, cefetamet is a beta-lactam cephalosporin. It acts by inhibiting bacterial cell wall synthesis.

The link to rheumatoid arthritis is weak. Cefetamet has no known anti-inflammatory or immunomodulatory activity relevant to autoimmune arthritis. The high score (0.980) most likely reflects network proximity in the knowledge graph rather than a real pharmacological relationship.

The other top-ranked predictions are osteoarthritis, osteoarthritis susceptibility, gout, hemoglobinopathy, pseudoachondroplasia, colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachyolmia, beta-thalassemia, and Hunter-Thompson acromesomelic dysplasia. None has any trial or literature support, and none has a plausible mechanism. Together they form a cluster of musculoskeletal and hematologic or genetic conditions, which points to a graph artifact rather than a true repurposing signal.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 7368 | Altamet 250mg Tablet (Alembic Pharmaceuticals Ltd) | Strip of 4 tablets | Not stated |
| 190698 | Recocef 500mg Tablet (Zydus Cadila) | Strip of 4 tablets | Not stated |
| 230548 | Ultipime O 500mg Tablet (Cadila Pharmaceuticals Ltd) | Strip of 4 tablets | Not stated |
| 190624 | Recocef 250mg Tablet (Zydus Cadila) | Strip of 10 tablets | Not stated |
| 231376 | Ultipime O 250mg Tablet (Cadila Pharmaceuticals Ltd) | Strip of 4 tablets | Not stated |

A sixth licence (180683, Pryzm 500mg Tablet, Torrent Pharmaceuticals Ltd, strip of 4 tablets) is also valid. All six registrations are single-ingredient oral tablets.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, and no plausible mechanism links a beta-lactam antibacterial to rheumatoid arthritis. The evidence level is L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian products (a blocking gap for safety screening)
- Confirmed mechanism-of-action data from DrugBank
- Any preclinical or clinical signal showing that cefetamet affects inflammatory or autoimmune arthritis pathways
- Confirmation of the approved indications on the Indian licences
- Assessment of route compatibility (currently pending; the available form is oral tablets only)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

