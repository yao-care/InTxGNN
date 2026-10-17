---
layout: default
title: Nilotinib
parent: Model Prediction Only (L5)
nav_order: 595
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Nilotinib: predicted new indication Dermatofibrosarcoma protuberans (evidence level L5). Approved use: Chronic myelogenous leukemia, BCR-ABL1 positive"
monitor_inn: "Nilotinib"
predicted_indications: ["dermatofibrosarcoma protuberans"]
---

# Nilotinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Nilotinib: From BCR-ABL1-Positive Chronic Myelogenous Leukemia to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Nilotinib is a tyrosine kinase inhibitor originally used to treat BCR-ABL1-positive chronic myelogenous leukemia.
The TxGNN model predicts it may be effective for **Dermatofibrosarcoma Protuberans (DFSP)**, but currently only **1 review article** supports this direction and **no registered clinical trials** were found.
The prediction is mechanistically plausible but remains at the research-question stage.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myelogenous leukemia, BCR-ABL1 positive |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 (the data compiled for this report rates it L4; only a general review exists, with no nilotinib-specific study, so model prediction is effectively the main support) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for nilotinib is not available in the data compiled for this report. Based on general knowledge, nilotinib is a tyrosine kinase inhibitor that blocks BCR-ABL1, and it also inhibits PDGFR, KIT and DDR kinases.

DFSP is typically driven by the COL1A1-PDGFB fusion, which causes constitutive autocrine activation of PDGFRB. Because nilotinib can inhibit PDGFR, there is a plausible mechanistic link between its activity in leukemia (kinase inhibition) and the growth signal that drives DFSP. The very high TxGNN score (0.993) is consistent with this biology.

An important caveat: the single supporting publication is a 2018 review of small-molecule PDGFR inhibitors in neoplastic disorders. It appears to centre on imatinib, the established PDGFR inhibitor for this disease, and is not nilotinib-specific clinical evidence. The mechanism described here is inferred from the drug class, not from the data provided.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Review of small-molecule PDGFR inhibitors in neoplastic disorders, covering the PDGF family and PDGFR signalling; likely focused on imatinib rather than nilotinib |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 216456 | Tasigna 150mg Capsule | Strip of 4 capsules | Not specified in available data |
| 215851 | Tasigna 200mg Capsule | Strip of 4 capsules | Not specified in available data |

Both licences are held by Novartis India Ltd and are currently valid. Both are oral single-ingredient products.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (the knowledge graph lists neutropenia, thrombocytopenia and anemia as contraindicated conditions, suggesting haematological risk) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC, liver function, electrolytes (potassium, magnesium), blood glucose, ECG for QT interval |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Contraindicated or high-caution conditions (from the knowledge graph, not label text)**:
  - Cardiovascular: long QT syndrome (including familial), torsades de pointes, hypertension
  - Liver, biliary and pancreatic: liver disease, gallbladder disease, hyperbilirubinemia (including Gilbert syndrome), pancreatitis
  - Blood: thrombocytopenia, neutropenia, agranulocytosis, anemia
  - Metabolic: hyperglycemia, diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hypophosphatemia, hypercalcemia, nephrocalcinosis, phosphorus metabolism disorders
- **Drug Interactions**: 637 interactions were identified in total. Major-level examples include:
  - Dexamethasone
  - Clarithromycin
  - Picosulfuric acid
  - Polyethylene glycol (3350 with electrolytes)

  Moderate-level examples include acid-suppressing drugs (famotidine, ranitidine, rabeprazole, omeprazole, cimetidine), corticosteroids (hydrocortisone, triamcinolone, betamethasone, budesonide), pioglitazone, loperamide, bupropion, aprepitant, bisacodyl and saxagliptin.

Package insert warnings and contraindications were not available. Please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The PDGFR-driven biology of DFSP gives a plausible mechanistic link and the TxGNN score is high. However, there are no registered clinical trials and no nilotinib-specific literature; the only supporting item is a general review that appears to focus on imatinib. The established PDGFR inhibitor for this disease already exists, and nilotinib's safety profile includes significant QT, metabolic and haematological concerns.

**To proceed, the following is needed:**
- Nilotinib-specific evidence in DFSP (case series, phase 2 data, or preclinical studies in COL1A1-PDGFB models)
- Comparative rationale against imatinib, including imatinib-resistant or intolerant patients
- Mechanism of action data (MOA) confirmed from a primary source
- Package insert warnings and contraindications for the India-marketed Tasigna products, plus their approved indication text
- A safety plan covering QT monitoring, and review of the major drug interactions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

