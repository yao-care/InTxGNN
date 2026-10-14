---
layout: default
title: Dimenhydrinate
parent: Moderate Evidence (L3-L4)
nav_order: 271
evidence_level: L4
indication_count: 2
---

# Dimenhydrinate
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

# Dimenhydrinate: From Motion Sickness and Vertigo to Allergic Urticaria

## One-Sentence Summary

Dimenhydrinate was originally used to treat motion sickness and vertigo of central nervous system origin.
The TxGNN model predicts it may be effective for **allergic urticaria**,
but at present only **1 publication** (a veterinary pharmacokinetic pilot study) and **no clinical trials** support this direction, so the evidence rests mainly on the model prediction and the known pharmacology of its active component.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Central nervous system origin vertigo; motion sickness (the registration records in India do not list approved indication text) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dimenhydrinate is a salt of diphenhydramine and 8-chlorotheophylline. Once absorbed, it releases diphenhydramine, a first-generation H1-receptor antagonist. Its efficacy in motion sickness and vertigo is established, and mechanistically it may be applicable to histamine-mediated conditions.

Urticaria is driven largely by histamine released from mast cells. H1 antagonists are a recognized drug class for this condition, so the prediction is pharmacologically plausible, and the high TxGNN score (0.997) is consistent with it. However, the support is indirect. It comes from the diphenhydramine component, not from dimenhydrinate itself being tested in urticaria. Current practice generally favors second-generation, less sedating antihistamines, so any use of a sedating first-generation agent would need to be justified against that standard.

A second prediction, **cold urticaria** (score 99.24%), has the same theoretical rationale but no clinical trials or literature at all (evidence level L5, decision Hold).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Pharmacokinetic study (pilot, in dogs) | Veterinary Dermatology | Compared diphenhydramine pharmacokinetics after oral and intravenous diphenhydramine and oral dimenhydrinate in healthy dogs, with the effect on histamine-induced wheal formation. Dimenhydrinate has been reported to give better oral absorption of diphenhydramine. |

This is an animal study and does not provide direct clinical evidence in humans.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 222323 | Transmine 50mg Tablet | Strip of 10 tablets | Not specified |
| Registration No. 58841 | Draminate 50mg Tablet | Strip of 10 tablets | Not specified |
| Registration No. 94324 | Gravol Tablet | Strip of 10 tablets | Not specified |
| Registration No. 61798 | Draminate 15.625mg/5ml Syrup | Bottle of 30 ml syrup | Not specified |

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug-disease contraindication links in the TxGNN knowledge graph, not label text): hypertension and hypotension; liver disease; gallbladder disease; thrombocytopenia and blood coagulation disorders; diabetes mellitus, hyperglycemia and diabetic ketoacidosis; peptic ulcer disease and pyloric stenosis; benign prostatic hyperplasia and bladder neck obstruction; angle-closure glaucoma and ocular hypertension; hyperthyroidism (Graves disease, thyrotoxicosis); gout; substance abuse/dependence; acute coronary syndrome, coronary artery disease and myocardial infarction; hemoglobinopathy; hypophosphatemia.
- **Drug Interactions**: 67 interactions were recorded in total. Examples:
  - **Major**: potassium citrate, potassium chloride.
  - **Moderate**: anticholinergics (atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, trospium, propantheline, clidinium, mepenzolate, methscopolamine), opioids and related drugs (morphine, opium, loperamide, eluxadoline), nabilone, metoclopramide and prucalopride.

For package insert warnings and contraindications, please refer to the product label.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link through the diphenhydramine component is plausible and the TxGNN score is high. However, there are no clinical trials, the only publication is a veterinary pharmacokinetic pilot study, and safety screening cannot proceed without label-based warnings. Second-generation antihistamines are the existing standard, and sedating first-generation agents are less attractive.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed Indian products
- Detailed mechanism of action data (MOA)
- Human clinical evidence of dimenhydrinate or diphenhydramine in allergic urticaria, and a comparison against second-generation antihistamines
- Route and dosage compatibility assessment for the new indication
- Review of the knowledge-graph contraindication signals and the interaction profile for the intended population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

