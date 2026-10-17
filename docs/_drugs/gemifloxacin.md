---
layout: default
title: Gemifloxacin
parent: Model Prediction Only (L5)
nav_order: 390
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Gemifloxacin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Bacterial pneumonia (streptococcal, Klebsiella…"
monitor_inn: "Gemifloxacin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder", "endomyometritis"]
---

# Gemifloxacin
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

# Gemifloxacin: From Bacterial Pneumonia to Hyperamylasemia

## One-Sentence Summary

Gemifloxacin is a fluoroquinolone antibacterial, originally used to treat bacterial pneumonia, including streptococcal, Klebsiella, Mycoplasma and chlamydial pneumonia.
The TxGNN model predicts it may be effective for **Hyperamylasemia**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.
The high score is most likely an artifact of the knowledge graph rather than a biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial pneumonia (streptococcal, Klebsiella, Mycoplasma pneumoniae and chlamydial pneumonia) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

*Note: The approved indication text is not available in the India registration records compiled for this report. The original indications above come from the TxGNN knowledge graph.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general knowledge, gemifloxacin is a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV. Its efficacy in respiratory bacterial infections is the basis of its original use.

For hyperamylasemia, **no mechanistic link was identified**. Hyperamylasemia is a laboratory finding with varied causes (pancreatic, salivary, renal), not a bacterial disease. An antibacterial DNA gyrase inhibitor has no known effect on it. The high TxGNN score is likely a knowledge-graph artifact.

The other top predictions show the same pattern. Most are haematological or immunological conditions (polyclonal hyperviscosity syndrome, congenital analbuminemia, monoclonal gammopathy, blood group incompatibility) with no plausible mechanism. These predictions appear to be semantically clustered in the graph. Two lower-ranked predictions have an indirect antibacterial rationale and are worth noting as research questions:

- **Septicemic plague (score 99.67%, L4):** *Yersinia pestis* is susceptible to fluoroquinolones such as ciprofloxacin, levofloxacin and moxifloxacin. Gemifloxacin shares the same mechanism and may be active in vitro, but this rests on class-effect inference only.
- **Endomyometritis (score 99.30%, L4):** This is a polymicrobial pelvic infection usually needing anaerobic coverage, which gemifloxacin covers only to a limited extent. Fluoroquinolone use in pregnancy and the postpartum period is also a safety concern.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Showing 5 of 20 valid registrations (all single-ingredient products).

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 31898 | Biogem 200mg Injection (United Biotech Pvt Ltd) | Vial of 1 injection | Not stated |
| 32541 | Biogem 1000mg Injection (United Biotech Pvt Ltd) | Vial of 1 injection | Not stated |
| 94597 | G-Cin Tablet (Lupin Ltd) | Strip of 5 tablets | Not stated |
| 29736 | Biogem 320mg Tablet (Biochem Pharmaceutical Industries) | Strip of 5 tablets | Not stated |
| 183792 | Quinhext 320mg Tablet (Sanofi India Ltd) | Strip of 5 tablets | Not stated |

The remaining registrations are mostly 320 mg tablets from various manufacturers.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (not label text): long QT syndrome (including familial), torsades de pointes, epilepsy, myasthenia gravis and other neuromuscular junction diseases, peripheral neuropathy and other peripheral nervous system diseases, tendinitis and related tendon/joint disorders, impaired renal function, potassium deficiency, *Clostridium difficile* colitis, and anxiety and related psychiatric disorders.
- **Drug interactions:** 273 interactions were identified. Examples at **Major** level include hydrocortisone, betamethasone, chlorpropamide and dolasetron. **Moderate** examples include clarithromycin, metformin, acarbose, famotidine, aspirin, calcium acetate and several SGLT2 inhibitors, DPP-4 inhibitors and GLP-1 agonists. Interactions with corticosteroids, QT-prolonging drugs and antidiabetic agents deserve particular attention.
- **Class-related concern:** Fluoroquinolones carry a boxed warning for peripheral neuropathy and can cause immune haemolytic anaemia. This runs contrary to the predicted benefit in the haematological and neuropathy-related predictions.

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for hyperamylasemia has no clinical trials, no literature and no plausible mechanism, so it is best treated as a knowledge-graph artifact. Among all the predictions, only septicemic plague and endomyometritis have a credible antibacterial rationale, and both remain research questions at L4.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India registrations (currently a blocking gap for safety screening)
- Mechanism of action data
- For septicemic plague: in vitro susceptibility data for gemifloxacin against *Yersinia pestis* and any animal-model data
- For endomyometritis: evidence on spectrum of activity, including anaerobic coverage, and a pregnancy/postpartum safety assessment
- Confirmation of route compatibility (oral tablets and injectable forms are registered in India)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

