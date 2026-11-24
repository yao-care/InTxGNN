---
layout: default
title: Cyclopentolate
parent: Model Prediction Only (L5)
nav_order: 217
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Cyclopentolate: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Cycloplegia"
monitor_inn: "Cyclopentolate"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome"]
---

# Cyclopentolate
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

## Cyclopentolate: From Cycloplegia to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Cyclopentolate is a topical anticholinergic eye drop originally used to produce cycloplegia (paralysis of eye focusing muscles) and pupil dilation.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cycloplegia |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9954 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for cyclopentolate: "This anticholinergic preparation blocks the responses of the sphincter muscle of the iris and the accommodative muscle of the ciliary body to cholinergic stimulation, producing pupillary dilation (mydriasis) and paralysis of accommodation (cycloplegia). It acts rapidly, but has a shorter duration than atropine." ([DailyMed: Cyclogyl (cyclopentolate hydrochloride) prescribing information, Alcon Laboratories, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1d008c76-7210-4ace-90fa-7cd22762e12e), label version 2024-06-25; accessed 2026-11-19.) Based on known pharmacology, cyclopentolate is a muscarinic antagonist (anticholinergic). It is used in the eye to relax the focusing muscle and dilate the pupil, and its efficacy for cycloplegia is established.

The only conceivable link to cauda equina syndrome is through reduced bladder detrusor activity, since anticholinergics can calm bladder overactivity. However, this link is weak. Cauda equina syndrome is a structural neurological emergency that usually requires surgical decompression. Its typical bladder presentation is urinary retention, which anticholinergics could worsen. In addition, cyclopentolate is marketed only as an ophthalmic solution, with no systemic dosing established.

The high TxGNN score is a computational prediction only and should not be read as clinical support.

### Other Predicted Indications (for context)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Neurogenic bladder (obsolete ontology term) | 0.9940 | L5 | Systemic antimuscarinics are established for neurogenic detrusor overactivity, so the mechanism is plausible in principle. Cyclopentolate has no systemic dosing, has CNS toxicity concerns (confusion, seizures, especially in children), and the disease term is obsolete. Better-validated alternatives exist. |
| 3 | Irritable bowel syndrome | 0.9927 | L5 | Class-level rationale only (antispasmodics such as dicyclomine and hyoscyamine). No studies of cyclopentolate and no oral formulation. |

## India Market Information

Cyclopentolate is marketed in India with 20 valid registrations, all ophthalmic (eye drops or ophthalmic solutions). Approved indication text was not available for these products.

<!-- review:begin in-lic-20261124c-cyclopentolate-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Cyclopentolate is marketed in India with 20 valid single-ingredient registrations, all ophthalmic (eye drops or ophthalmic solutions)." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-cyclopentolate-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 7497 | Auropent Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 35169 | Cyclomid Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 36779 | Cyclofez Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 37043 | C Pent Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 39143 | Cyclate Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 39227 | Cyclopen Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 42776 | Cyclopen D Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 42886 | Cyclodex Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 43187 | Cepenta Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 43571 | Cylate Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 44839 | Cp Dilate 1% Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 46714 | Cyclin 1% Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 47758 | Cyclopent DM Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 48457 | Cycloray 1% Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 50227 | Cyclate Drop | Bottle of 5 ml Eye Drop | Valid |
| 52131 | Cycleen 1% Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 76372 | Eslate Eye Drops | Bottle of 5 ml Ophthalmic Solution | Valid |
| 163305 | Open Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 174841 | Pentol Eye Drop | Bottle of 3 ml Eye Drop | Valid |
| 178507 | Pentocyl Eye Drop | Packet of 5 ml Ophthalmic Solution | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Knowledge-graph-listed contraindicated conditions** (from the TxGNN knowledge graph, not label text): angle-closure glaucoma, hypertension, heart disease (including coronary artery disease, sudden cardiac arrest and heart conduction disease), arteriosclerosis and atherosclerosis, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, hyperthyroidism (Graves disease, thyrotoxicosis), brain injury or brain disease, and Down syndrome.
- **Systemic anticholinergic concerns** (from the prediction rationale): CNS effects such as confusion and seizures, especially in children. Relevant to any systemic use, which is not an established route for this drug.

Please refer to the package insert for label warnings and drug interaction information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for cauda equina syndrome has no clinical trial or literature support (Evidence Level L5). The mechanistic link is weak and potentially counterproductive, since anticholinergics may worsen urinary retention. The only available formulation is topical ophthalmic, which is unsuited to systemic use. The other predicted indications (neurogenic bladder, IBS) are likewise unsupported and already served by better-validated drugs.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India-marketed products (a blocking gap for safety screening)
- Detailed mechanism of action data
- Any preclinical or clinical evidence for the predicted indication
- A feasibility assessment of a systemic formulation and route, including systemic anticholinergic safety, particularly CNS effects

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cyclogyl (cyclopentolate hydrochloride) prescribing information, Alcon Laboratories, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1d008c76-7210-4ace-90fa-7cd22762e12e) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

