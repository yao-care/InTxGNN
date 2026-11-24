---
layout: default
title: Homatropine
parent: Model Prediction Only (L5)
nav_order: 409
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "Homatropine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "gastroduodenitis", "overactive bladder (disease)"]
description: "Homatropine: predicted new indication Cauda equina syndrome (evidence level L5). In India: 12 listed products (12 not discontinued)"
---

# Homatropine
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

## Homatropine: Cauda equina syndrome
{: .text-alpha }

## One-Sentence Summary

Homatropine is an antimuscarinic (anticholinergic) agent, originally used for conditions such as peptic ulcer disease, uveitis and cycloplegia (pupil dilation and paralysis of eye focusing).
The TxGNN model predicts it may be effective for **cauda equina syndrome**,
but **no clinical trials and no publications** currently support this prediction, so it rests on computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (12 of 12) – CDSCO approval status is not included in this data |
| Number of Listed Products | 12 (valid: 12) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, homatropine belongs to the antimuscarinic class. It blocks muscarinic receptors, which explains its use in the eye (pupil dilation, cycloplegia) and in the gut (reduced secretion and motility).

Cauda equina syndrome is caused by compression of the nerve roots at the base of the spine. It can lead to neurogenic bladder dysfunction. Antimuscarinics reduce detrusor (bladder muscle) contractility, so they could in theory ease bladder symptoms. This would be symptom relief only. The underlying cause needs surgical decompression, which no drug replaces.

The other predictions follow the same class-level logic:

- **Obsolete neurogenic bladder:** Antimuscarinics are an established class for neurogenic detrusor overactivity. However, there is no homatropine-specific evidence, and the disease term is flagged as obsolete in the ontology, which may affect mapping accuracy.
- **Gastroduodenitis:** This overlaps with the existing peptic ulcer indication, so it is not a clearly novel use. Antimuscarinics are not first-line here.
- **Overactive bladder:** Oxybutynin and tolterodine are standard therapy, giving strong class-level plausibility. Homatropine is non-selective with systemic anticholinergic effects, and better-studied alternatives exist.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

All 12 valid licences are single-ingredient eye drops. The records contain no approved indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 8681 | Aurohom Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 103703 | Homide Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 103975 | Homatropine Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 104002 | HA2 Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 104066 | Homacid Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 104217 | Homatropine Eye Drop | Packet of 10 ml Eye Drop | Valid |
| 104627 | Homarin Forte Eye Drop | Packet of 3 ml Eye Drop | Valid |
| 105593 | Homarin Forte Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 105688 | Homatropine Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 105693 | Homatrapar 2% Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 106959 | Homatrapar 1% Eye Drop | Bottle of 5 ml Eye Drop | Valid |
| 135062 | Mydryn Eye Drop | Packet of 5 ml Eye Drop | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

---

## Safety Considerations

**Contraindications flagged in the knowledge graph** (drug-disease links, not label text):
- Cardiovascular: hypertension, hypotension, coronary artery disease
- Liver and kidney: liver failure, liver disease, hepatic coma and encephalopathy, kidney disease, gallbladder disease
- Neurological and psychiatric: epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder, substance abuse/dependence
- Gastrointestinal and urological: gastric ulcer, inflammatory bowel disease, benign prostatic hyperplasia, pyoureter
- Blood and metabolic: porphyria (including inherited forms), thrombocytopenia, neutropenia, agranulocytosis, hypothyroidism, myxedema, congenital hypothyroidism
- Sleep: obstructive sleep apnea and sleep apnea syndrome

**Drug Interactions:** 17 interactions were identified.
- **Major:** potassium chloride and potassium citrate
- **Moderate:** other anticholinergics (dicyclomine, glycopyrronium, hyoscyamine, mepenzolate, methscopolamine, propantheline, ipratropium), opium, hydrocodone, edrophonium, physostigmine, cyclizine, phenindamine, phenylephrine and thiethylperazine

The marketed products are eye drops. Systemic use for the predicted indications would involve a different exposure profile, and no dosage form or route suitable for that use has been confirmed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 0.9989 TxGNN score is a computational prediction only, with no clinical trials or publications behind it. Marketed homatropine products in India are ophthalmic only. Better-studied antimuscarinics already exist for the bladder-related predictions, and surgery is the definitive treatment for cauda equina syndrome.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed products, which are currently missing and block safety screening
- Mechanism of action data (for example from DrugBank)
- A literature and trial search specific to homatropine in bladder dysfunction
- An assessment of whether a systemic or suitable route and formulation exists, since only eye drops are marketed
- A comparison against established antimuscarinics for overactive bladder and neurogenic bladder, to judge whether homatropine adds any value
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

