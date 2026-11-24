---
layout: default
title: Lidocaine
parent: Model Prediction Only (L5)
nav_order: 491
evidence_level: L5
indication_count: 10
monitor_inn: "Lidocaine"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "papillary conjunctivitis", "rosacea conjunctivitis", "exposure keratitis", "atopic conjunctivitis", "conjunctival disorder", "nephrotic syndrome", "non-human animal disease", "tinea corporis", "sporadic idiopathic steroid-resistant nephrotic syndrome"]
last_modified_at: 2026-11-24
description: "Lidocaine: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Relations recorded in the knowledge graph (not label-confirmed approv…"
---

# Lidocaine
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

## Lidocaine: From Local Anaesthesia and Neuralgia to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Lidocaine is a sodium channel–blocking local anaesthetic.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **no clinical trials and no publications** directly study this disease, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relations recorded in the knowledge graph (not label-confirmed approvals): dermatitis, neuralgia, haemorrhoids, postherpetic neuralgia, scabies and others. The licence records compiled for this report contain no approved indication text. |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Number of Approvals | At least 20 licences (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for lidocaine: "Lidocaine hydrochloride exerts an antiarrhythmic effect by increasing the electrical stimulation threshold of the ventricle during diastole. In usual therapeutic doses, lidocaine hydrochloride produces no change in myocardial contractility, in systemic arterial pressure, or in absolute refractory period." ([DailyMed: Lidocaine Hydrochloride And Dextrose (lidocaine hydrochloride) prescribing information, Baxter Healthcare Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f21512ea-c7c3-4766-b976-b2c0b5616bf0), label version 2026-02-20; accessed 2026-11-19.) Based on general knowledge, lidocaine blocks voltage-gated sodium channels and is used as a local anaesthetic, including on the ocular surface.

The link to the predicted disease is weak. A topical anaesthetic could in theory relieve surface pain, but it would not treat the underlying keratoconjunctivitis. Topical anaesthetics can also impair corneal epithelial healing, which is a safety concern for this kind of condition. The high model score therefore should not be read as support for therapeutic benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered for punctate epithelial keratoconjunctivitis.

For context, the model's other eye-related predictions have some registered trials, but none address the predicted disease here. For example, for the lower-ranked "conjunctival disorder" prediction, the trials concern anaesthesia during eye surgery (for example, [NCT05978687](https://clinicaltrials.gov/study/NCT05978687), a completed Phase 4 trial of lidocaine gel versus subconjunctival injection in pterygium excision, n=41). These test anaesthetic technique, not treatment of the disease.

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

## India Market Information

At least 20 lidocaine licences are valid in India. None of the records include approved indication text.

<!-- review:begin in-lic-20261124c-lidocaine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "At least 20 single-ingredient lidocaine licences are valid in India." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-lidocaine-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 8623 | Avicaine Oral Topical Solution | Bottle of 100 ml Solution | Valid |
| 28932 | Biocaine 2% Injection | Vial of 30 ml Injection | Valid |
| 109472 | Ilidotrans Transdermal Patch | Box of 2 transdermal patches | Valid |
| 121665 | Lignox 2% Gel | Tube of 30 gm Gel | Valid |
| 121721 | Lignox 2 % A Injection | Vial of 30 ml Injection | Valid |
| 122515 | Lignox 2% Injection | Vial of 30 ml Injection | Valid |
| 122746 | Lignox+adrenline Injection | Vial of 30 ml Injection | Valid |
| 125383 | Lidofix 2% Injection | Vial of 30 ml Injection | Valid |
| 126646 | Lignotross Injection | Vial of 1 Injection | Valid |
| 127832 | Lignocip 2% Injection | Vial of 30 ml Injection | Valid |
| 129868 | Lcaine Injection | Vial of 30 ml Injection | Valid |
| 131281 | Leecaine 2% Injection | Vial of 30 ml Injection | Valid |
| 131323 | Lignorain 2% Injection | Vial of 30 ml Injection | Valid |
| 162965 | Oculan 1% Injection | Vial of 1 ml Injection | Valid |
| 163480 | Oculan 1% Injection | Ampoule of 2 ml Injection | Valid |
| 203383 | Skore Not Out Lidocaine Topical Spray | Bottle of 12 gm Spray | Valid |
| 218772 | Themicaine AD 2%/0.005mg Injection | Vial of 30 ml Injection | Valid |
| 244086 | Xylo 2% Injection | Vial of 30 ml Injection | Valid |
| 244166 | Xylocaine 5% Injection | Vial of 2 ml Injection | Valid |
| 249369 | Zylo Injection | Vial of 30 ml Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Available forms include injections, gel, spray, oral topical solution and transdermal patch.

## Safety Considerations

- **Contraindications (knowledge-graph relations, not label text):** the knowledge graph records contraindication relations with conditions including hypertension, liver failure, liver disease, cirrhosis, kidney disease, epilepsy, open-angle glaucoma, herpes simplex virus keratitis, adrenocortical insufficiency, hypothyroidism, atopic dermatitis, osteoporosis, psychotic disorders, fungal infections and gastritis.
- **Drug Interactions:** 100 interactions were found. The main ones include:
  - **Major:** bupropion.
  - **Moderate:** aprepitant, cimetidine, liposomal morphine, obeticholic acid, polyethylene glycol (3350 with electrolytes), picosulfuric acid, sodium sulfate.
  - **Minor:** dexamethasone, kanamycin, neomycin, omeprazole, streptomycin, troglitazone.
- **Eye-specific concern:** misuse of topical anaesthetics is known to cause corneal damage, and the model's predicted use is on the ocular surface.
- Other literature in the compiled data documents neuropsychiatric adverse effects of lidocaine, a case of methemoglobinemia when combined with other topical agents, and seizures in animals at low doses given in a combination preparation.

Please also refer to the package insert, as label warnings were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but no trial or publication directly studies lidocaine for punctate epithelial keratoconjunctivitis, so the evidence level is L5. The plausible mechanism (surface anaesthesia) would only relieve symptoms, and topical anaesthetics may harm corneal healing.

**To proceed, the following is needed:**
- Direct preclinical or clinical evidence in punctate epithelial keratoconjunctivitis
- Corneal safety assessment for repeated ocular-surface use
- Package insert warnings and contraindications from India licence documents
- Mechanism of action data from DrugBank

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Lidocaine Hydrochloride And Dextrose (lidocaine hydrochloride) prescribing information, Baxter Healthcare Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f21512ea-c7c3-4766-b976-b2c0b5616bf0) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

