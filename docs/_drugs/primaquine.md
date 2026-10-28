---
layout: default
title: Primaquine
parent: Model Prediction Only (L5)
nav_order: 699
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
monitor_inn: "Primaquine"
predicted_indications: ["myiasis", "wound myiasis", "furuncular myiasis", "creeping myiasis", "toxoplasmosis", "nocardiosis", "pneumocystosis"]
description: "Primaquine: predicted new indication Myiasis (evidence level L5). Approved use: Not recorded in the local data"
---

# Primaquine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Primaquine: Myiasis
{: .text-alpha }

## One-Sentence Summary

Primaquine is an 8-aminoquinoline antimalarial, originally used for the radical cure of *Plasmodium vivax* malaria.
The TxGNN model predicts it may be effective for **myiasis** (fly-larvae infestation), but **no clinical trials and no publications** support this prediction, and no plausible mechanistic link has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 (model prediction only) |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, primaquine is an 8-aminoquinoline whose efficacy in *P. vivax* malaria is well established. Its activity is generally attributed to redox-active metabolites acting on liver-stage hypnozoites and on gametocytes.

Myiasis is an infestation of tissue by fly larvae, which are multicellular insect parasites. Primaquine is not known to act on insect targets. Standard care is mechanical removal or debridement, plus larvicidal agents such as ivermectin, and primaquine has no known larvicidal activity. The same lack of a mechanistic link applies to the related subtypes (wound, furuncular and creeping myiasis).

The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should be read as a computational result, not as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Primaquine is marketed in India as single-ingredient oral tablets, with 20 valid registrations and none cancelled. Main authorizations:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 178384 | Primaline 15mg Tablet | Strip of 10 tablets | Unicure India Pvt Ltd |
| 219666 | Tpquin P 15mg Tablet | Strip of 10 tablets | Taurus Laboratories Pvt Ltd |
| 179447 | Primacare 7.5mg Tablet | Strip of 10 tablets | Olcare Laboratories |
| 180931 | Prib DS 15mg Tablet | Strip of 10 tablets | Bennet Pharmaceuticals Limited |
| 129012 | Leoprime 7.5mg Tablet | Strip of 14 tablets | Leo Pharmaceuticals |

---

## Safety Considerations

- **Contraindication-related conditions (not taken from label text)**: neutropenia, agranulocytosis, G6PD deficiency, hemolytic anemia, methemoglobinemia due to methemoglobin reductase deficiency, glycogen storage disease, cystinuria, galactosemia, and pyruvate dehydrogenase E3 deficiency.
- **Drug Interactions**: 278 interactions are recorded. One is Major (dolasetron). Most others are Moderate, including famotidine, alosetron, loperamide, clarithromycin, levofloxacin, ondansetron, granisetron, palonosetron, and various laxatives and bowel-preparation agents. Metronidazole is Minor.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The myiasis prediction rests on model output alone (L5). There are no trials or publications, and primaquine has no known activity against fly larvae. Safe, effective alternatives (mechanical removal, ivermectin) already exist, while primaquine carries a significant hemolysis risk in G6PD-deficient patients.

**To proceed, the following is needed:**
- Any preclinical evidence of larvicidal activity (a mechanistic rationale)
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications for India-marketed products
- A comparison of expected benefit against the hemolysis and drug-interaction risks, if any evidence emerges

Other predictions for primaquine have much stronger support. Malaria (an on-label use with Phase 3 trials) and pneumocystosis (clindamycin plus primaquine as a second-line regimen, with a Phase 3 trial) both reach L1. They could be evaluated with G6PD screening as a guardrail.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

