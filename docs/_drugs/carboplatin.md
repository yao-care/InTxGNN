---
layout: default
title: Carboplatin
parent: Model Prediction Only (L5)
nav_order: 147
evidence_level: L5
indication_count: 9
monitor_inn: "Carboplatin"
predicted_indications: ["rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "adult germ cell tumor", "cervical mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "endometrial mucinous adenocarcinoma", "villoglandular endometrial endometrioid adenocarcinoma", "endometrial mixed adenocarcinoma", "extrahepatic bile duct mucinous adenocarcinoma"]
last_modified_at: 2026-10-30
description: "Carboplatin: predicted new indication rectum mucinous adenocarcinoma (evidence level L5). In India: at least 20 listed products"
---

# Carboplatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Carboplatin: platinum-based DNA-crosslinking chemotherapy → rectum mucinous adenocarcinoma
{: .text-alpha }

## One-Sentence Summary

Carboplatin is a platinum-based cytotoxic chemotherapy agent.
The TxGNN model predicts it may be relevant to **rectum mucinous adenocarcinoma**, but the data compiled for this report contain **0 clinical trials** and **0 publications** for this disease, so the prediction is not yet supported by any direct study.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | rectum mucinous adenocarcinoma |
| TxGNN Prediction Score | 0.9928 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for carboplatin: "Carboplatin is a platinum-based drug that binds to DNA and forms DNA cross-links. These crosslinks inhibit DNA replication and transcription and trigger cytotoxic processes that lead to cell death." ([DailyMed: Kyxata (carboplatin) prescribing information, AVYXA Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f91c48da-68d1-4aa7-89b8-d84a3e8b629b), label version 2026-11-09; accessed 2026-11-19.) Carboplatin belongs to the platinum class of cytotoxic drugs. As a class, platinum agents form DNA crosslinks that block cell division and trigger cell death. This could, in principle, apply to many adenocarcinomas.

The model's score most likely reflects shared mucinous adenocarcinoma histology with tumours that carboplatin already addresses. It does not reflect a validated mechanism in rectal tissue. Platinum agents are generally considered to offer limited benefit in colorectal cancers, and mucinous histology tends to be less chemosensitive. No retrieved study evaluates carboplatin in rectal mucinous adenocarcinoma.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Carboplatin is marketed in India. All 20 licences found are valid single-ingredient injectable or infusion products, and none are cancelled. The licence records carry no approved-indication text, so the approved indication is not recorded in the local data. Because the record set may be partial, the table lists five examples.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 41122 | Carbokem Novo 150mg Injection | Vial, injection | Alkem Laboratories Ltd |
| 18001 | Acoticyt 150mg Injection | Vial, injection | Accord Pharmaceuticals |
| 42624 | Celcarb 450mg Injection | Vial, injection | Celon Laboratories Ltd |
| 39455 | Carboplan 150mg Injection | Vial, injection | Natco Pharma Ltd |
| 118834 | Karplat 450mg Infusion | Bottle of 50 ml, infusion | Cadila Pharmaceuticals Ltd |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (platinum class) |
| Myelosuppression Risk | High; thrombocytopenia and neutropenia are the main dose-limiting effects |
| Emetogenicity Classification | Moderate (higher at high doses) |
| Monitoring Items | CBC with differential and platelets, renal and liver function, electrolytes, and neurological and hearing assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 488 recorded interacting drugs. Most of the listed ones are rated Moderate. They include:
  - proton pump inhibitors (omeprazole, esomeprazole, pantoprazole, lansoprazole, rabeprazole, dexlansoprazole)
  - aminoglycosides (kanamycin, neomycin, streptomycin)
  - vancomycin
  - metronidazole and tinidazole
  - statins (simvastatin, rosuvastatin)

  Levofloxacin is rated Minor.
- **Conditions flagged for caution in the compiled data**: kidney disease, liver disease, gallbladder disease, thrombocytopenia, neutropenia, leukopenia, anaemia, blood coagulation disorders, peripheral neuropathy and hearing disorders. These are not taken from label text and should be confirmed against the package insert.

Please refer to the package insert for key warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9928), but there is no clinical trial or publication on rectum mucinous adenocarcinoma. The evidence level is therefore L5. Platinum agents are generally of limited benefit in colorectal cancers, so the score alone does not justify advancing.

**To proceed, the following is needed:**
- Disease-specific preclinical or clinical data on carboplatin in rectal mucinous adenocarcinoma
- Mechanism-of-action data and a mechanistic rationale for this histology
- Package insert warnings and contraindications from the India licence holders
- A comparison against standard-of-care regimens for this disease

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not currently available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Kyxata (carboplatin) prescribing information, AVYXA Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f91c48da-68d1-4aa7-89b8-d84a3e8b629b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

