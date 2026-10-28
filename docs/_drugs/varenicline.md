---
layout: default
title: Varenicline
parent: Model Prediction Only (L5)
nav_order: 883
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Varenicline: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Varenicline"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "diffuse alopecia areata", "alopecia", "open-angle glaucoma", "primary hereditary glaucoma", "headache disorder", "pulmonary hypertension"]
---

# Varenicline
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

## Varenicline: From Smoking Cessation to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Varenicline is a nicotinic acetylcholine receptor partial agonist, marketed in India as Nocrav 1mg Tablet. The TxGNN model predicts it may be effective for **migraine disorder**, but this is a model prediction only. There are **no clinical trials** and **no publications** showing efficacy for this indication. The single retrieved publication is a case report of cardiac arrest, which is a safety signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the India licence has no approved indication text) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally available in the data compiled for this report. From general pharmacology, varenicline is a partial agonist of α4β2 nicotinic acetylcholine receptors and a full agonist at α7 receptors. Nicotinic cholinergic signalling and cortical spreading depression are loosely implicated in migraine, which is the only theoretical bridge to this prediction.

No direct mechanistic or clinical link between varenicline and migraine has been shown. The very high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Other high-ranking predictions (for example migraine with brainstem aura, which is a subtype of migraine) appear to reflect the same learned similarity to migraine.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19585710](https://pubmed.ncbi.nlm.nih.gov/19585710/) | 2009 | Case report | Therapie | Cardiac arrest in a patient taking varenicline. This is a safety report and not evidence of efficacy in migraine. |

Related headache searches also returned smoking-cessation studies. None evaluates headache or migraine as a treatment target, and headache appears in them as an adverse event of varenicline. One case report (PMID 23175211) describes bath-related headache induced by varenicline.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 150993 | Nocrav 1mg Tablet (Lyf Healthcare) | Strip of 10 tablets | Not stated |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not label text): anxiety disorder, neurotic disorder, dysthymic disorder, bipolar disorder, major affective disorder, substance abuse/dependence, schizophrenia, acute coronary syndrome, peripheral vascular disease, intermittent vascular claudication, and peripheral arterial disease.
- **Drug Interactions**: 104 interactions were recorded. Only cimetidine is classified (Minor); the rest are unclassified. Examples include phentermine, metformin, glimepiride, rosiglitazone, omeprazole, pantoprazole, lansoprazole, morphine, prednisone, simvastatin, and epinephrine.
- **Case-report safety signals**: cardiac arrest and varenicline-induced headache have been reported.

Please refer to the package insert for label warnings and contraindications, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the TxGNN model score (evidence level L5). There are no trials and no supporting literature, and headache is a known adverse effect of varenicline, which argues against a therapeutic role. The knowledge graph also flags several psychiatric and cardiovascular contraindications.

**To proceed, the following is needed:**
- The India package insert warnings and contraindications (a blocking gap for safety screening)
- Formal mechanism of action data from DrugBank
- Preclinical or mechanistic evidence linking nicotinic receptor modulation to migraine
- Any clinical signal for migraine, such as exploratory trials or observational data
- A review of the headache adverse-event signal and the cardiovascular safety profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

