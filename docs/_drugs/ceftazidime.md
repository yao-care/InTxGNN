---
layout: default
title: Ceftazidime
parent: Model Prediction Only (L5)
nav_order: 159
evidence_level: L5
indication_count: 9
monitor_inn: "Ceftazidime"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "epiglottitis", "Ureaplasma urethritis", "gonococcal urethritis", "blood group incompatibility", "infectious otitis media", "Peptostreptococcus infectious disease"]
last_modified_at: 2026-11-03
description: "Ceftazidime: predicted new indication hyperamylasemia (evidence level L5). In India: at least 20 listed products"
---

# Ceftazidime
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

## Ceftazidime: Third-generation cephalosporin (beta-lactam antibiotic) → hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Ceftazidime is a third-generation cephalosporin antibiotic that works by blocking bacterial cell wall synthesis.
The TxGNN model predicts it may be associated with **hyperamylasemia**, but **no clinical trials and no publications** support this prediction.
It rests on the model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | hyperamylasemia |
| TxGNN Prediction Score | 0.9951 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for ceftazidime: "Ceftazidime is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Ceftazidime has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: ceftazidime prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=112c5457-8d71-49f5-b531-9761d7d38c93), label version 2026-08-03; accessed 2026-11-19.) Ceftazidime is a beta-lactam antibiotic, and the usual understanding is that it inhibits bacterial cell wall synthesis.

Hyperamylasemia is a laboratory finding (raised amylase in the blood), not an infectious disease. An antibacterial has no clear target in this condition, so there is no plausible mechanistic link between the drug's action and this predicted indication. The high model score therefore cannot be explained by pharmacology and should be treated as a computational signal only, not as a therapeutic rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Ceftazidime is marketed in India. At least 20 single-ingredient injection licences are valid, and the list may be partial. None of the records carries approved-indication text, so the table leaves that column out. Main products:

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| 33120 | Bbcef S 1000mg/500mg Injection | Vial, powder for injection |
| 209865 | Spectrazid 250mg Injection | Vial, injection |
| 165495 | Orzid 2gm Injection | Vial, injection |
| 33512 | Bioceft 1000mg Injection | Vial, injection |
| 85994 | Fortum ES 2gm Injection | Vial, injection |

## Safety Considerations

- **Drug Interactions**: 114 interactions were identified in total. The main ones rated Moderate are:
  - Amphotericin B (including the cholesteryl sulfate, lipid complex and liposomal forms)
  - Aminoglycosides: kanamycin, neomycin, streptomycin
  - Picosulfuric acid

  Further interactions with unknown severity are listed for drugs such as vancomycin, metformin, omeprazole and morphine.

Please refer to the package insert for warnings and contraindications, as no label-based data are available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. No trial or publication addresses hyperamylasemia, and there is no plausible mechanism by which an antibacterial would treat a laboratory finding.

**To proceed, the following is needed:**
- Any clinical or preclinical study directly examining ceftazidime in hyperamylasemia
- Mechanism of action data and a clear biological hypothesis
- Package insert safety information (warnings and contraindications)
- Clarification of whether the signal reflects a drug effect on amylase rather than a treatment benefit

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: ceftazidime prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=112c5457-8d71-49f5-b531-9761d7d38c93) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

