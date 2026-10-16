---
layout: default
title: Cefpodoxime
parent: Model Prediction Only (L5)
nav_order: 157
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Cefpodoxime: predicted new indication Osteoarthritis susceptibility (evidence level L5). Approved use: Not recorded in the India license data (cefpodoxime is a cephalospori…"
monitor_inn: "cefpodoxime"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis"]
---

# Cefpodoxime
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Cefpodoxime: From Bacterial Infection (Original Indication Not Recorded) to Osteoarthritis Susceptibility

## One-Sentence Summary

Cefpodoxime is a third-generation cephalosporin antibiotic that is marketed in India in several oral forms (tablets, dispersible tablets and dry syrups).
The TxGNN model predicts it may be effective for **osteoarthritis susceptibility**, but the prediction has **0 clinical trials** and **0 publications** behind it.
This is a computational prediction only, and the evidence is currently very weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the India license data (cefpodoxime is a cephalosporin antibiotic) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, cefpodoxime is a third-generation cephalosporin that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins. Its established use is against bacterial infections.

The data compiled for this report does not support a mechanistic link between this action and osteoarthritis. No anti-inflammatory, chondroprotective or analgesic activity is documented. "Susceptibility" is also a genetic-risk phenotype rather than a treatable disease state, so the prediction is of doubtful therapeutic relevance. The high TxGNN score (0.993) reflects a knowledge-graph pattern and should not be read as evidence of efficacy.

Two other predictions are similar in nature: **osteoarthritis** (99.25%) and **rheumatoid arthritis** (99.24%). Both are also unsupported by trials or literature. For rheumatoid arthritis, long-term antibiotic exposure would raise concerns about resistance and microbiome disruption.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Cefpodoxime has 20 valid single-ingredient registrations, with none cancelled. The approved indication text is not available for any of them. Five main authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 247914 | Zerapod 50mg Dry Syrup | Bottle of 30 ml dry syrup | Not available |
| 119398 | Kepdox 200mg Tablet | Strip of 10 tablets | Not available |
| 202512 | Safepodox Dry Syrup | Bottle of 30 ml dry syrup | Not available |
| 212104 | Safydox 100mg Tablet DT | Strip of 10 dispersible tablets | Not available |
| 229113 | Topod CV 200mg/125mg Tablet | Strip of 6 tablets | Not available |

---

## Safety Considerations

- **Drug Interactions**: 78 interactions were recorded, and the 20 listed are all of Moderate severity. They fall into these groups:
  - Acid-suppressing agents: famotidine, ranitidine, cimetidine, nizatidine, and the proton pump inhibitors omeprazole, esomeprazole, lansoprazole, dexlansoprazole, rabeprazole and pantoprazole
  - Antacids: aluminum hydroxide, calcium carbonate, magaldrate, and magnesium carbonate, hydroxide and oxide
  - Aminoglycosides: kanamycin and neomycin
  - Others: balsalazide

Please refer to the package insert for warnings and contraindications, as this information is not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or publications, no plausible mechanism, and the "susceptibility" phenotype is not a treatable condition. The evidence level is L5, and safety screening cannot proceed without the package insert data.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indication text for the India licenses
- Mechanism of action data (e.g., from DrugBank)
- A literature and trial search for any link between cephalosporins and osteoarthritis or rheumatoid arthritis
- A defined therapeutic target, because "susceptibility" is not a treatable disease state
- A review of the 78 recorded drug interactions for a chronic, polypharmacy population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

