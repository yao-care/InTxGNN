---
layout: default
title: Tadalafil
parent: Model Prediction Only (L5)
nav_order: 803
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Tadalafil: From Erectile Dysfunction and Pulmonary Hypertension to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tadalafil is a PDE5 inhibitor originally used for erectile dysfunction, benign prostatic hyperplasia, and pulmonary hypertension.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but **no clinical trials and no publications** currently support this prediction. It rests on a graph-based computational score alone, and the plausible explanation is a statistical artifact rather than a therapeutic link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Erectile dysfunction, benign prostatic hyperplasia, pulmonary hypertension, premature ejaculation, psychologic dyspareunia (approved-indication text is not available in the Indian licence records) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, tadalafil is a PDE5 inhibitor. It raises cGMP and causes vasodilation, which underlies its proven effect in erectile dysfunction and pulmonary hypertension.

On the evidence available, the prediction is **not mechanistically convincing**. Ambras syndrome is a congenital hypertrichosis linked to a chromosomal rearrangement affecting gene regulation near *TRPS1*. No plausible pathway connects PDE5 inhibition to this condition. The high score most likely reflects shared network neighbours among hypertrichosis-related nodes, for example vasodilators such as minoxidil that *cause* hypertrichosis. If so, the association points to an adverse-effect pattern, not a treatment. Even if a link existed, a drug that induces hair growth would not be expected to treat excess hair growth.

The same pattern appears in the other top-ranked predictions: hypertrichosis, isolated genetic hair shaft abnormality, familial isolated trichomegaly, and developmental malformation syndromes (odontal/periodontal and Dandy-Walker). None has supporting evidence in the data compiled for this report.

Two lower-ranked predictions are worth noting:
- **Kyphoscoliotic heart disease** (score 99.43%): this is the only prediction with an indirect, speculative pathway. Tadalafil is approved for pulmonary arterial hypertension, and kyphoscoliosis can lead to cor pulmonale. However, no data support it, and PDE5 inhibitors may worsen ventilation-perfusion matching in chronic hypoxic or restrictive lung disease.
- **Migraine with brainstem aura** (score 99.08%): the only evidence is a case report of tadalafil *associated with* migraine aura, which is a safety signal, not a therapeutic one.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top-ranked prediction (Ambras type hypertrichosis universalis congenita), currently no related literature is available.

The only publication found across the predictions is for migraine with brainstem aura, and it is a safety signal rather than support for efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/) | 2006 | Case report | Cephalalgia | Tadalafil associated with typical migraine aura without headache (abstract not available) |

## India Market Information

Tadalafil is marketed in India with 20 valid single-ingredient registrations and no cancelled ones. The approved-indication text is not recorded for any of them. The main registrations are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 108956 | Igtad-MD 5 Tablet | Strip of 10 orally disintegrating tablets | Not recorded |
| 215827 | Tadmax 20mg Tablet | Strip of 5 tablets | Not recorded |
| 72376 | Efil 2.5mg Tablet | Strip of 10 tablets | Not recorded |
| 124527 | Longtid 20 Tablet | Strip of 1 tablet | Not recorded |
| 217786 | Tadasure 20 Disintegrating Strip | Strip of 1 disintegrating strip | Not recorded |

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
The prediction rests only on a computational score, with no clinical trials or publications, and the likely explanation is a graph artifact linked to drugs that cause hypertrichosis. There is also no plausible mechanism, and the one available publication is an adverse-event signal.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) and an analysis of whether any PDE5/cGMP effect on hair follicles exists
- Package insert warnings and contraindications from Indian regulatory sources
- Literature review on the direction of effect (induction versus treatment of hypertrichosis)
- If pursuing a different direction, a focused literature review of kyphoscoliotic heart disease with pulmonary hypertension, including the risk of worsened ventilation-perfusion matching
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

