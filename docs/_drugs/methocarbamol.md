---
layout: default
title: Methocarbamol
parent: Model Prediction Only (L5)
nav_order: 534
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Methocarbamol: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not stated in the India license data (methocarbamol is generally used…"
monitor_inn: "Methocarbamol"
predicted_indications: ["cauda equina syndrome", "irritable bowel syndrome", "panuveitis (disease)", "anaphylaxis", "iris disease", "uveitis", "ventricular tachycardia", "food-dependent exercise-induced anaphylaxis", "conjunctivitis", "obsolete bundle branch block"]
---

# Methocarbamol
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

## Methocarbamol: From Muscle Spasm (Musculoskeletal Conditions) to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Methocarbamol is a centrally acting skeletal muscle relaxant that is marketed in India as tablets and an injection.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, but **no clinical trials and no publications** support this prediction.
It is a computational prediction only, so the evidence is very weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India license data (methocarbamol is generally used as a muscle relaxant for painful muscle spasm) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (3 of 3) – CDSCO approval status is not included in this data |
| Number of Registrations | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, methocarbamol is a centrally acting skeletal muscle relaxant. A plausible link would be symptomatic relief of muscle spasm or pain associated with the condition.

Cauda equina syndrome is caused by compression of the nerve roots at the base of the spinal cord, and it is a surgical emergency. Methocarbamol would not treat the underlying compression. At most, it could play a supportive, symptomatic role. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other top-ranked predictions are also unsupported by the data compiled for this report. These are irritable bowel syndrome, panuveitis, anaphylaxis, iris disease, uveitis, ventricular tachycardia, food-dependent exercise-induced anaphylaxis, conjunctivitis and obsolete bundle branch block. For these, no plausible mechanistic link could be drawn. The only literature retrieved was for anaphylaxis and ventricular tachycardia, and it does not show efficacy (see below).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for cauda equina syndrome.

For the lower-ranked predictions, the following papers were retrieved. They do not show therapeutic benefit:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20086833](https://pubmed.ncbi.nlm.nih.gov/20086833/) | 1998 | Review | The Physician and Sportsmedicine | General review of arthropod bites and stings. Methocarbamol is mentioned only as an option for symptoms after widow spider bites. It is not an anaphylaxis treatment (anaphylaxis prediction, rank 4). |
| [42543011](https://pubmed.ncbi.nlm.nih.gov/42543011/) | 2026 | Review | Orvosi Hetilap | Compares side-effect profiles of centrally acting muscle relaxants. It concerns safety, not benefit, and notes anaphylactic reactions with tolperisone (anaphylaxis prediction, rank 4). |
| [30050852](https://pubmed.ncbi.nlm.nih.gov/30050852/) | 2017 | Case report (veterinary) | Veterinary Medicine (Auckland) | Severe lamotrigine toxicosis in a dog. It is not about methocarbamol efficacy and gives no evidence for ventricular tachycardia (rank 7). |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 136699 | Mecotha Tablet | Strip of 10 tablets | Not stated |
| 184792 | Robinax 100mg Injection | Vial of 10 ml injection | Not stated |
| 184528 | Robinax 500mg Tablet | Strip of 10 tablets | Not stated |

All three licenses are valid single-ingredient products. There are no combination products and no cancelled licenses.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** The TxGNN knowledge graph links methocarbamol with contraindications in these conditions: epilepsy, kidney disease, liver disease, gallbladder disease, thrombocytopenia and thrombocytopenic purpura, peptic ulcer disease (including active disease) and gastritis, gout, substance abuse/dependence, anaemia (including macrocytic anaemia), bleeding disorders (haemophilia, von Willebrand disease, congenital prothrombin deficiency, vitamin K deficiency haemorrhagic disease), Reye syndrome, Alzheimer disease, Pick disease, cerebellar degeneration, nasal cavity polyp and pyoureter. These should be verified against the official package insert.
- **Drug Interactions:** 126 interactions were recorded. The main ones are:
  - **Major:** morphine and liposomal morphine (additive central nervous system and respiratory depression is the expected concern).
  - **Moderate:** dronabinol, nabilone, metoclopramide, opium and sibutramine.
  - Further interactions with unknown severity were recorded, including metformin, glimepiride, omeprazole, pantoprazole and doxycycline.

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN computational score, with no clinical trials or supporting literature. Methocarbamol cannot treat the underlying nerve compression in cauda equina syndrome, and the best case is symptomatic relief.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications from the India license documents
- Mechanism of action data (for example from DrugBank)
- Clinical or observational evidence for the predicted indication, or a reasoned choice of a more plausible candidate indication
- Review of the knowledge graph contraindication signals, especially for hepatic, renal and haematological conditions
- A route-of-administration compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

