---
layout: default
title: Levofloxacin
parent: Model Prediction Only (L5)
nav_order: 487
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Levofloxacin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder"]
description: "Levofloxacin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). In India: at least 20 listed products"
---

# Levofloxacin
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

## Levofloxacin: Punctate epithelial keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Levofloxacin is a broad-spectrum fluoroquinolone antibacterial that is marketed in India as single-ingredient oral tablets.
The TxGNN model predicts it may be useful for **punctate epithelial keratoconjunctivitis**, with a score of 0.9992.
Evidence is very thin: **0 clinical trials** and **1 publication** (an outbreak report that does not test levofloxacin).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for levofloxacin: "Levofloxacin is a member of the fluoroquinolone class of antibacterial agents. […] Levofloxacin is the L-isomer of the racemate, ofloxacin, a quinolone antimicrobial agent. The antibacterial activity of ofloxacin resides primarily in the L-isomer. The mechanism of action of levofloxacin and other fluoroquinolone antimicrobials involves inhibition of bacterial topoisomerase IV and DNA gyrase (both of which are type II topoisomerases), enzymes required for DNA replication, transcription, repair and recombination." ([DailyMed: levofloxacin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=814450ae-439e-4a5d-8c60-9b21b6f14be5), label version 2026-11-05; accessed 2026-11-19.) Based on its drug class, levofloxacin is a fluoroquinolone that kills bacteria by inhibiting bacterial DNA replication enzymes. Because it works against a broad range of bacteria, applying it to infections of the ocular surface is plausible.

The only retrieved paper is a report of a microsporidial keratoconjunctivitis outbreak linked to swimming-pool water in Taiwan. Microsporidia are intracellular, fungi-related organisms that fluoroquinolones do not reliably treat. The paper therefore gives no support for efficacy.

The very high TxGNN score most likely reflects the model's closeness to other eye-surface infection and inflammation conditions, not direct evidence. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Outbreak report | American Journal of Ophthalmology | Microsporidial keratoconjunctivitis outbreak tied to contaminated swimming-pool water in Taiwan. It does not evaluate levofloxacin treatment. |

## India Market Information

The record may be partial.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 11175 | Avulox 500mg Tablet | Strip of 10 tablets | Valid |
| 66405 | Decaflox 500mg Tablet | Strip of 10 tablets | Valid |
| 75606 | Evabit 500mg Tablet | Strip of 10 tablets | Valid |
| 79798 | Elev 250mg Tablet | Strip of 10 tablets | Valid |
| 82302 | Elvox 500mg Tablet | Strip of 5 tablets | Valid |
| 122062 | Lquin 750 Tablet | Strip of 5 tablets | Valid |
| 127653 | L Bakterie 500mg Tablet | Strip of 10 tablets | Valid |
| 128899 | Livopen 250mg Tablet | Strip of 10 tablets | Valid |
| 131798 | Lefloxil 500 Tablet | Strip of 10 tablets | Valid |
| 132195 | Livoxit 500mg Tablet | Strip of 10 tablets | Valid |
| 133310 | Lefoq 250mg Tablet | Strip of 10 tablets | Valid |
| 133341 | Levoase 500mg Tablet | Strip of 10 tablets | Valid |
| 171676 | Ofladea 500mg Tablet | Strip of 10 tablets | Valid |
| 192687 | R-Levo 250 Tablet | Strip of 10 tablets | Valid |
| 197875 | Rinlevo 500mg Tablet | Strip of 10 tablets | Valid |
| 199122 | Ryvlox 500mg Tablet | Strip of 10 tablets | Valid |
| 212618 | Selevo OZ 250mg/500mg Tablet | Strip of 10 tablets | Valid |
| 225191 | Tri Alevo 250mg Tablet | Strip of 10 tablets | Valid |
| 238899 | Volflox 500mg Tablet | Strip of 10 tablets | Valid |
| 241417 | Voxquin OZ 250mg/500mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All listed products are oral tablets. No topical or ophthalmic formulation appears in the local records, which matters for an ocular surface indication.

## Safety Considerations

- **Drug Interactions**: 434 interactions are recorded. Major-level examples include tramadol and hydrocortisone. Moderate-level examples include metformin, pioglitazone, alogliptin, ibuprofen, ketorolac, famotidine, ethinylestradiol, salbutamol, formoterol and adenosine.
- **Conditions flagged for caution** (not taken from label text): long QT syndrome and torsades de pointes, epilepsy, liver disease and drug-induced liver injury, tendinitis, peripheral neuropathy, myasthenia gravis, diabetes (including ketoacidosis), impaired renal function, rhabdomyolysis, *Clostridium difficile* colitis, and several blood-count disorders (thrombocytopenia, leukopenia, anemia, pancytopenia).

Please also refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5. The only paper concerns a microsporidial outbreak, a cause fluoroquinolones are not expected to treat, and no trial tests levofloxacin for this condition. The high score alone does not justify moving forward.

**To proceed, the following is needed:**
- Evidence that links levofloxacin to bacterial causes of punctate epithelial keratoconjunctivitis, such as clinical or microbiological studies
- Detailed mechanism of action data
- A route-compatibility assessment, since only oral tablets are recorded locally and no ocular formulation is listed
- Package insert warnings and contraindications to complete the safety screen

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: levofloxacin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=814450ae-439e-4a5d-8c60-9b21b6f14be5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

