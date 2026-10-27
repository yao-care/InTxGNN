---
layout: default
title: Cefditoren
parent: Model Prediction Only (L5)
nav_order: 153
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cefditoren: predicted new indication Osteoarthritis susceptibility (evidence level L5). Approved use: Not stated in the licence data compiled for this report (cefditoren i…"
monitor_inn: "Cefditoren"
predicted_indications: ["osteoarthritis susceptibility", "rheumatoid arthritis", "osteoarthritis", "hemoglobinopathy", "brachyolmia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "partial deletion of the short arm of chromosome 16"]
---

# Cefditoren
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

## Cefditoren: From Bacterial Infection to Osteoarthritis Susceptibility
{: .text-alpha }

## One-Sentence Summary

Cefditoren is a third-generation oral cephalosporin antibiotic that is marketed in India. The TxGNN model predicts it may be related to **osteoarthritis susceptibility**, but **no clinical trials and no publications** currently support this prediction. It is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data compiled for this report (cefditoren is a third-generation oral cephalosporin antibacterial) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, cefditoren is a third-generation oral cephalosporin that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins. Its established role is in treating bacterial infections.

Osteoarthritis susceptibility is a genetic-risk phenotype, not an infectious condition. No plausible mechanistic link between a beta-lactam antibacterial and this phenotype has been identified. The high TxGNN score (0.992) most likely reflects network-based associations in the knowledge graph rather than biological rationale.

Other top-ranked predictions show the same pattern. They include rheumatoid arthritis, osteoarthritis, hemoglobinopathy and several rare skeletal dysplasias (such as brachyolmia and acromesomelic dysplasia, Hunter-Thompson type). None has trial or literature support, and none has a credible mechanism. The scores appear to be driven by shared skeletal and joint disease neighbours in the graph.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 246583 | Zostum O 100mg Dry Syrup | Bottle of 30 ml dry syrup | Not stated |
| 38267 | Cefdicare 200mg Tablet | Strip of 10 tablets | Not stated |
| 37725 | Ceftorin 200mg Tablet | Strip of 6 tablets | Not stated |
| 246413 | Zostum-O 200mg Tablet | Strip of 10 tablets | Not stated |
| 247093 | Zostum-O 50mg Tablet DT | Strip of 10 dispersible tablets | Not stated |

All five registrations are valid single-ingredient products. Manufacturers are Zuventus Healthcare Ltd (three products), Meyer Organics Pvt Ltd and Cipla Ltd.

## Safety Considerations

**Drug Interactions**: The interaction screen found 27 interactions, all graded Moderate. The main groups are:
- **Acid-suppressing drugs**: H2 blockers (famotidine, ranitidine, cimetidine, nizatidine) and proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole). These may reduce cefditoren absorption.
- **Antacids**: aluminium hydroxide, calcium carbonate, magaldrate, magnesium carbonate, magnesium hydroxide, magnesium oxide, sodium bicarbonate and sodium citrate.
- **Anticoagulant**: dicoumarol.

Only 20 of the 27 interactions are itemised in the data compiled for this report. For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no clinical trials, no publications and no plausible mechanistic link between a bacterial cell-wall inhibitor and osteoarthritis susceptibility. This is a genetic-risk phenotype, not a treatable condition. The same holds for the other nine top-ranked predictions.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications for the Indian products (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence supporting a link to the predicted condition
- A defined repurposing hypothesis, including route and dosage form compatibility, before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

