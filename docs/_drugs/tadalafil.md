---
layout: default
title: Tadalafil
parent: Model Prediction Only (L5)
nav_order: 803
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
description: "Tadalafil: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Erectile dysfunction, benign prostatic hyperplasia…"
monitor_inn: "Tadalafil"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
---

# Tadalafil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Tadalafil: From Erectile Dysfunction and Pulmonary Hypertension to Ambras Type Hypertrichosis Universalis Congenita
{: .text-alpha }

## One-Sentence Summary

Tadalafil is a PDE5 inhibitor originally used for erectile dysfunction, benign prostatic hyperplasia, and pulmonary hypertension.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but **no clinical trials and no publications** currently support this prediction. It rests on a score from the TxGNN model (deep learning) alone, which may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Erectile dysfunction, benign prostatic hyperplasia, pulmonary hypertension, premature ejaculation, psychologic dyspareunia (approved-indication text is not available in the Indian licence records) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for tadalafil: "Penile erection during sexual stimulation is caused by increased penile blood flow resulting from the relaxation of penile arteries and corpus cavernosal smooth muscle. This response is mediated by the release of nitric oxide (NO) from nerve terminals and endothelial cells, which stimulates the synthesis of cGMP in smooth muscle cells. […] Tadalafil inhibits PDE5." ([DailyMed: Cialis (tadalafil) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bcd8f8ab-81a2-4891-83db-24a0b0e25895), label version 2026-06-03; accessed 2026-11-19.) Based on general knowledge, tadalafil is a PDE5 inhibitor. It raises cGMP and causes vasodilation, which underlies its proven effect in erectile dysfunction and pulmonary hypertension.

On the evidence available, the prediction is **not mechanistically convincing**. Ambras syndrome is a congenital hypertrichosis linked to a chromosomal rearrangement affecting gene regulation near *TRPS1*. No plausible pathway connects PDE5 inhibition to this condition. The high score most likely reflects shared network neighbours among hypertrichosis-related nodes, for example vasodilators such as minoxidil that *cause* hypertrichosis. If so, the association points to an adverse-effect pattern, not a treatment. Even if a link existed, a drug that induces hair growth would not be expected to treat excess hair growth.

The same pattern appears in the other top-ranked predictions: hypertrichosis, isolated genetic hair shaft abnormality, familial isolated trichomegaly, and developmental malformation syndromes (odontal/periodontal and Dandy-Walker). None has supporting evidence in the data compiled for this report.

Two lower-ranked predictions are worth noting:
- **Kyphoscoliotic heart disease** (score 0.9943): this is the only prediction with an indirect, speculative pathway. Tadalafil is approved for pulmonary arterial hypertension, and kyphoscoliosis can lead to cor pulmonale. However, no data support it, and PDE5 inhibitors may worsen ventilation-perfusion matching in chronic hypoxic or restrictive lung disease.
- **Migraine with brainstem aura** (score 0.9908): the only evidence is a case report of tadalafil *associated with* migraine aura, which is a safety signal, not a therapeutic one.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top-ranked prediction (Ambras type hypertrichosis universalis congenita), currently no related literature is available.

The only publication found across the predictions is for migraine with brainstem aura, and it is a safety signal rather than support for efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/) | 2006 | Case report | Cephalalgia | Tadalafil associated with typical migraine aura without headache (abstract not available) |

## India Market Information

Tadalafil is marketed in India with 20 valid single-ingredient registrations and no cancelled ones. The approved-indication text is not recorded for any of them.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 58308 | Duraplus Tablet | Strip of 4 tablets | Valid |
| 60082 | Deta M 2.5mg Tablet | Strip of 10 tablets | Valid |
| 62398 | Dapodafil Tablet | Strip of 4 tablets | Valid |
| 63941 | Durolong 10mg Tablet | Strip of 10 tablets | Valid |
| 72376 | Efil 2.5mg Tablet | Strip of 10 tablets | Valid |
| 72564 | Efil 5mg Tablet | Strip of 10 tablets | Valid |
| 72749 | Edrive-T 2.5 Tablet | Strip of 10 tablets | Valid |
| 75798 | Erectaid T 10mg Tablet | Strip of 10 tablets | Valid |
| 96357 | Getgo 20mg Tablet | Strip of 4 tablets | Valid |
| 108956 | Igtad-MD 5 Tablet | Strip of 10 tablet md | Valid |
| 124527 | Longtid 20 Tablet | Strip of 1 Tablet | Valid |
| 133818 | Mildfil Tablet | Strip of 10 tablets | Valid |
| 139658 | Moodwell Tablet | Strip of 10 tablets | Valid |
| 189329 | Riseup 20mg Tablet | Strip of 4 tablets | Valid |
| 192889 | Redrive 20mg Tablet | Strip of 5 tablets | Valid |
| 215827 | Tadmax 20mg Tablet | Strip of 5 tablets | Valid |
| 217786 | Tadasure 20 Disintegrating Strip | Strip of 1 Disintegrating Strip | Valid |
| 218902 | Tedarose 10 Tablet | Strip of 10 tablets | Valid |
| 219208 | Tadazane 5mg Tablet | Strip of 10 tablets | Valid |
| 220185 | Tadalip 10mg Tablet MD | Strip of 10 tablet md | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

Package insert warnings and contraindications were not available. The following come from the knowledge graph and the drug-interaction database, not from label text.

- **Disease contraindications (knowledge graph)**, grouped:
  - Cardiovascular: aortic stenosis and other aortic valve disease, hypotensive disorder, acute coronary syndrome, myocardial infarction, coronary thrombosis, stroke and cerebrovascular disorders, cerebral infarction, hypertrophic cardiomyopathy (including familial)
  - Haematological: sickle cell anaemia, hemoglobinopathy, hereditary persistence of fetal haemoglobin, blood coagulation disease, plasma cell myeloma, leukaemia
  - Genitourinary: priapism, Peyronie disease, penile fibromatosis, balanitis xerotica obliterans
  - Other: liver failure, epilepsy, hearing loss disorder, visual loss
- **Drug interactions**: 132 interactions were recorded. Moderate-level examples include aprepitant, dexamethasone, clarithromycin, cimetidine, miconazole, clotrimazole, lorcaserin, sapropterin, and the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin). Papaverine is minor.
- **Migraine aura signal**: a published case report associates tadalafil with migraine aura.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a score from the TxGNN model (deep learning), with no clinical trials or publications. The score may reflect similarities the model learned between related diseases, not biological evidence, including similarities with drugs that cause hypertrichosis. There is also no plausible mechanism, and the one available publication is an adverse-event signal.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) and an analysis of whether any PDE5/cGMP effect on hair follicles exists
- Package insert warnings and contraindications from Indian regulatory sources
- Literature review on the direction of effect (induction versus treatment of hypertrichosis)
- If pursuing a different direction, a focused literature review of kyphoscoliotic heart disease with pulmonary hypertension, including the risk of worsened ventilation-perfusion matching

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cialis (tadalafil) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bcd8f8ab-81a2-4891-83db-24a0b0e25895) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

