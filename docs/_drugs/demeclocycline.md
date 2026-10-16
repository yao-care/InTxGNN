---
layout: default
title: Demeclocycline
parent: Model Prediction Only (L5)
nav_order: 241
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Demeclocycline: predicted new indication Chronic ethmoidal sinusitis (evidence level L5). Approved use: Bacterial infections"
---

# Demeclocycline
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

# Demeclocycline: From Bacterial Infections to Chronic Ethmoidal Sinusitis

## One-Sentence Summary

Demeclocycline is a tetracycline-class antibiotic, originally used to treat bacterial infections such as urinary tract infection, bronchitis, gonorrhea and pharyngitis.
The TxGNN model predicts it may be effective for **chronic ethmoidal sinusitis**,
but at present there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (urinary tract infection, bronchitis, anthrax, staphylococcal infection, gonorrhea, pharyngitis and others; the approved indication text on the Indian licences is blank, so this list comes from the knowledge graph) |
| Predicted New Indication | Chronic ethmoidal sinusitis |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

Other predictions for this drug are chronic rhinosinusitis (99.09%) and paranasal sinus neoplasm (99.05%). Neither has any clinical trials or literature either.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, demeclocycline is a member of the tetracycline class of antibiotics. Its efficacy in bacterial infections of the respiratory tract and other sites is the basis of its original use, and mechanistically it may be applicable to chronic ethmoidal sinusitis.

Plausible links include antibacterial activity against sinus pathogens, and the anti-inflammatory and matrix metalloproteinase-inhibiting properties of the tetracycline class. The original indications include upper airway infections such as bronchitis and pharyngitis, which offer only weak indirect plausibility for sinus disease. None of these links is supported by trial or literature data compiled for this report.

The high TxGNN score is a computational prediction only and is not clinical evidence. The predicted indication is closely related to chronic rhinosinusitis, which was also predicted. The third prediction, paranasal sinus neoplasm, has low biological plausibility for an antibiotic. Its high score likely reflects network proximity to sinus-related diseases rather than a true therapeutic signal.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 124393 | Ledermycin 150mg Tablet (Pfizer Ltd) | Strip of 10 tablets | Not stated in the available data |
| 122118 | Ledermycin 300mg Tablet (Pfizer Ltd) | Strip of 10 tablets | Not stated in the available data |

Both licences are valid single-ingredient oral products.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, and diabetes insipidus (including neurohypophyseal and central forms).
- **Drug Interactions**: 154 interactions were identified. The sample reviewed included mostly Moderate-level interactions:
  - **Major**: Vitamin A.
  - **Moderate**: Amoxicillin, balsalazide, and polyvalent cation products (calcium phosphate, calcium acetate, magnesium oxide, magnesium sulfate, magnesium chloride, zinc sulfate, zinc acetate, potassium citrate). Several insulin products are also listed (aspart, degludec, detemir, glargine, glulisine, human isophane, human regular, human inhalation).
  - **Minor**: Mannitol.

Package insert warnings and contraindications have not been obtained. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting clinical trials or publications (Evidence Level L5). The package insert safety data are also missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian products (a blocking gap)
- Mechanism of action data for demeclocycline
- A literature and trial search on tetracycline-class antibiotics in chronic sinusitis, to establish whether any real-world or preclinical evidence exists
- A review of the approved indications on the Indian licences, which are currently blank
- A safety assessment of the knowledge-graph contraindications (especially kidney disease and *C. difficile* colitis) against the intended sinusitis population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

