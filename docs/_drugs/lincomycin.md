---
layout: default
title: Lincomycin
parent: Model Prediction Only (L5)
nav_order: 492
evidence_level: L5
indication_count: 3
monitor_inn: "Lincomycin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia"]
last_modified_at: 2026-11-24
description: "Lincomycin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Pneumococcal, staphylococcal and streptococcal infections"
---

# Lincomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Lincomycin: From Pneumococcal, Staphylococcal and Streptococcal Infections to Polyclonal Hyperviscosity Syndrome
{: .text-alpha }

## One-Sentence Summary

Lincomycin is a lincosamide antibiotic. The TxGNN model (deep learning) predicts it may be effective for **polyclonal hyperviscosity syndrome**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pneumococcal, staphylococcal and streptococcal infections (relations recorded in the knowledge graph; the local licence records contain no approved indication text) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 0.9914 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for lincomycin: "Lincomycin inhibits bacterial protein synthesis by binding to the 23S RNA of the 50S subunit of the bacterial ribosome. Lincomycin is predominantly bacteriostatic in vitro." ([DailyMed: Lincocin (lincomycin hydrochloride) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c01906fa-2c73-4c13-9765-2fd06628d263), label version 2025-03-10; accessed 2026-11-19.) Lincomycin is known as a lincosamide antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit.

Polyclonal hyperviscosity syndrome arises from elevated serum immunoglobulins or other proteins, for example in autoimmune disease or chronic infection. It is not a bacterial-driven process that an antibiotic would directly treat. No credible mechanistic link was identified between lincomycin and this condition.

The high TxGNN score (0.9914) is a computational prediction only. It comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Two other top-ranked predictions, hyperamylasemia (0.9914) and congenital analbuminemia (0.9906), show the same pattern: high scores, no supporting studies, and no plausible mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

At least 20 licences exist. The licence records contain no approved indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 123274 | Lincocin 600mg Injection | Vial of 2 ml Injection | Valid |
| 125442 | Licomine Syrup | Bottle of 60 ml Syrup | Valid |
| 125534 | Liod 300mg Injection | Vial of 2 ml Injection | Valid |
| 126429 | Lycin 125mg Syrup | Bottle of 60 ml Syrup | Valid |
| 127489 | Lincozin 500mg Capsule | Strip of 10 capsules | Valid |
| 128095 | Lycin Injection | Vial of 2 ml Injection | Valid |
| 128244 | Linoson 600mg Injection | Vial of 2 ml Injection | Valid |
| 128955 | Lines 250mg Capsule | Strip of 10 capsules | Valid |
| 129176 | Lincozin 250mg Capsule | Strip of 10 capsules | Valid |
| 129187 | Linkosol 300mg Injection | Vial of 2 ml Injection | Valid |
| 130092 | Linocin 250mg Capsule | Strip of 10 capsules | Valid |
| 130190 | Lincom 500mg Capsule | Strip of 10 capsules | Valid |
| 130314 | Lincobiotic Injection | Vial of 2 ml Injection | Valid |
| 130868 | Lincowin 600mg Injection | Vial of 2 ml Injection | Valid |
| 131567 | Linka 300mg Injection | Vial of 1 ml Injection | Valid |
| 132033 | Lincoriv 300mg Injection | Vial of 2 ml Injection | Valid |
| 132659 | Lincop 600mg Injection | Vial of 2 ml Injection | Valid |
| 207651 | Shelinc 600mg Injection | Vial of 2 ml Injection | Valid |
| 209770 | Semilinc Syrup | Bottle of 30 ml Syrup | Valid |
| 211453 | Splinc 500mg Capsule | Strip of 10 capsules | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Available forms across the listed licences include injections, capsules and syrups.

---

## Safety Considerations

**Contraindication relations in the knowledge graph** (not label text): liver failure, Clostridium difficile colitis, perinatal necrotizing enterocolitis, colitis, digestive system disease and intestinal disease.

**Drug Interactions:** 21 interactions were found. Those rated Moderate:
- Balsalazide
- Picosulfuric acid
- Attapulgite
- Kaolin
- Erythromycin
- Ethinylestradiol

The remaining interactions have an unknown severity level, including warfarin, metformin, morphine, simvastatin, omeprazole, cimetidine, ranitidine, lidocaine, clotrimazole, lactulose, triamcinolone, cetirizine, montelukast and salmeterol.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. No clinical trials or publications study lincomycin in polyclonal hyperviscosity syndrome, and no plausible mechanism links an antibacterial protein-synthesis inhibitor to this condition. The evidence level is L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator or manufacturers (needed for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical study directly addressing polyclonal hyperviscosity syndrome
- Route compatibility and similarity-to-original-indication assessments, which are still pending
- Review of the gastrointestinal and liver-related contraindication relations before any further evaluation

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Lincocin (lincomycin hydrochloride) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c01906fa-2c73-4c13-9765-2fd06628d263) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

