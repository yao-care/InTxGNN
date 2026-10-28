---
layout: default
title: Tetracycline
parent: Model Prediction Only (L5)
nav_order: 827
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
monitor_inn: "Tetracycline"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "chronic ethmoidal sinusitis", "chronic rhinosinusitis", "paranasal sinus neoplasm (disease)"]
description: "Tetracycline: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Tetracycline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Tetracycline: Punctate epithelial keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Tetracycline is a broad-spectrum antibiotic originally used for bacterial infections such as urinary tract infection, bronchitis, acne, pneumonia and conjunctivitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but there are **no registered clinical trials** and only **1 publication** (a 1992 case report), so this prediction rests mainly on the model itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tetracycline is a member of the tetracycline antibiotic class, its efficacy in bacterial infections including conjunctivitis is established, and mechanistically it may be applicable to punctate epithelial keratoconjunctivitis.

Tetracycline is an established treatment for chlamydial (trachoma/inclusion) conjunctivitis, and persistent superficial punctate keratitis can follow chlamydial infection. Its antibacterial activity against *Chlamydia*, together with the anti-inflammatory and MMP-inhibiting effects of tetracyclines on the ocular surface, gives a plausible link.

However, the only supporting paper is a 1992 report of post-chlamydial keratitis. It is indirect and does not test tetracycline for this indication. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as the approved conjunctivitis indications, not biological evidence.

Other predictions for this drug are weaker or different in kind. Chronic rhinosinusitis (including its ethmoidal subtype) has class-level evidence, mostly on doxycycline. Paranasal sinus neoplasm has no supporting data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case report | Cornea | Two patients with chlamydial follicular conjunctivitis were treated with oral tetracycline or doxycycline, and the follicles resolved. Both then developed recurrent bilateral punctate epithelial keratitis. The report does not test tetracycline as a treatment for the keratitis. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 216002 | Tetralab 250mg Capsule | Strip of 10 capsules | Not stated |
| 20540 | Arcycline 250mg Capsule | Strip of 10 capsules | Not stated |
| 192020 | Rancycline 250mg Capsule (Sun Pharmaceutical) | Strip of 10 capsules | Not stated |
| 217158 | Tetra A 250mg Tablet | Strip of 10 tablets | Not stated |
| 153483 | Nicocycline 500mg Capsule (Abbott) | Strip of 10 capsules | Not stated |

There are 20 valid single-ingredient registrations in total. All are oral capsules or tablets. No ophthalmic formulation appears in the data compiled for this report.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not label text): liver failure, liver disease, kidney disease, kidney failure, uremia, glomerulonephritis, neutropenia, agranulocytosis, G6PD deficiency, epilepsy, diabetes mellitus, diabetic ketoacidosis, gout, peripheral neuropathy, blood coagulation disease, *Clostridium difficile* colitis, respiratory failure, atrial fibrillation, atrioventricular block, and others.
- **Drug Interactions**: 308 interactions were identified. Major ones include:
  - Isotretinoin
  - Acitretin
  - Aminolevulinic acid
- **Moderate interactions** include:
  - Ethinylestradiol
  - Amoxicillin
  - Ampicillin
  - Aluminium hydroxide
  - Aminophylline
  - Atracurium
  - Bismuth subcitrate potassium

Package insert warnings and contraindications could not be obtained for this report. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the only supporting evidence is a single 1992 case report that does not test tetracycline for this condition. No clinical trials exist, and the available India formulations are oral only. The evidence is insufficient to support a repurposing effort at present.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India product labels, which are required for safety screening
- Detailed mechanism of action data
- Clinical evidence testing tetracycline in punctate epithelial keratoconjunctivitis, and an assessment of whether an ophthalmic formulation is available or needed
- Separately, the chronic rhinosinusitis prediction (L3, class-level evidence from doxycycline) could be framed as a research question. It should not be treated as support for tetracycline itself.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

