---
layout: default
title: Eribulin
parent: Model Prediction Only (L5)
nav_order: 319
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Eribulin: predicted new indication Autosomal recessive familial Mediterranean fever (evidence level L5). Approved use: Liposarcoma"
monitor_inn: "Eribulin"
predicted_indications: ["autosomal recessive familial Mediterranean fever", "dermatofibrosarcoma protuberans", "pleural mesothelioma", "malignant peritoneal mesothelioma", "ovarian myxoid liposarcoma", "pleural adenomatoid tumor", "pleural biphasic mesothelioma", "fibroblastic neoplasm", "pleural epithelioid mesothelioma", "heart fibrosarcoma"]
---

# Eribulin
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

## Eribulin: From Liposarcoma to Autosomal Recessive Familial Mediterranean Fever
{: .text-alpha }

## One-Sentence Summary

Eribulin is a microtubule-targeting cytotoxic chemotherapy, originally used for liposarcoma.
The TxGNN model predicts it may be effective for **autosomal recessive familial Mediterranean fever**, but **no clinical trials and no publications** currently support this prediction, which is likely an artifact of the knowledge-graph structure.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Liposarcoma |
| Predicted New Indication | Autosomal recessive familial Mediterranean fever |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Eribulin is a synthetic analog of halichondrin B that inhibits microtubule dynamics. It is used in cytotoxic oncology. Detailed mechanism-of-action data were not available in the data compiled for this report, so the mechanistic description relies on its known drug class.

Familial Mediterranean fever is an autoinflammatory disease driven by dysregulation of the pyrin inflammasome. The standard therapy, colchicine, is also a microtubule-targeting agent. This shared target class may explain the high model score. However, eribulin binds tubulin differently from colchicine. Its cytotoxic profile is also unsuitable for a chronic, non-malignant condition. The score is therefore most likely a knowledge-graph artifact rather than a true mechanistic signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Eribulin is marketed in India as an injectable. Eight valid single-ingredient registrations are on file. The approved indication text was not available for these registrations, so it is not shown. The table lists the first five.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| Registration No. 75829 | Ebunat 0.5mg Injection (Natco Pharma Ltd) | Vial of 1 Injection |
| Registration No. 75269 | Eribilin Injection (Emcure Pharmaceuticals Ltd) | Vial of 2 ml Solution for Injection |
| Registration No. 77600 | Epbriv 0.44mg Injection (Hetero Healthcare Limited) | Vial of 2 ml Injection |
| Registration No. 104185 | Halaven 1mg Injection (Eisai Pharmaceuticals India Pvt Ltd) | Vial of 2 ml Injection |
| Registration No. 75256 | Embremma Injection (Emcure Pharmaceuticals Ltd) | Vial of 2 ml Injection |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (microtubule dynamics inhibitor) |
| Myelosuppression Risk | High. Neutropenia and thrombocytopenia appear among the knowledge-graph contraindication-related conditions |
| Emetogenicity Classification | Low to moderate (general drug-class knowledge) |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes (including potassium), ECG/QT, and peripheral neuropathy assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text)**: long QT syndrome (including familial), thrombocytopenia, neutropenia, agranulocytosis, potassium deficiency, peripheral neuropathy and other peripheral nervous system disease, and constipation disorder.
- **Drug Interactions**: 375 interactions were identified.
  - **Major**: dolasetron and cisapride, both QT-prolonging agents.
  - **Moderate**: ondansetron, palonosetron, clarithromycin, levofloxacin, metronidazole, tinidazole, famotidine, loperamide, rosuvastatin and simvastatin. Several laxatives and bowel-preparation agents also appear, such as bisacodyl, lactulose, lactitol, castor oil, sodium sulfate and polyethylene glycol.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5), with no trials or publications. The mechanistic link is weak, and a cytotoxic agent with significant myelosuppression and QT-related risks is a poor fit for a chronic autoinflammatory disease. Established therapies such as colchicine already exist.

**To proceed, the following is needed:**
- Any mechanistic or preclinical evidence linking eribulin to pyrin inflammasome regulation
- Detailed mechanism-of-action data
- Package insert warnings and contraindications from the India regulatory source
- A risk-benefit assessment for a non-malignant chronic indication

**Note on other predictions:** Among the other model predictions, **fibroblastic neoplasm** (rank 8, score 99.36%) has the strongest support. It has a completed Phase 2 trial of eribulin in advanced solitary fibrous tumor (ERASING, [NCT03840772](https://clinicaltrials.gov/study/NCT03840772), n=16) and supportive preclinical literature. Its results were not available, so efficacy is unconfirmed. If this evaluation is redirected toward oncology, that indication is the more promising candidate for follow-up.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

