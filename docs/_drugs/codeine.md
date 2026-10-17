---
layout: default
title: Codeine
parent: Model Prediction Only (L5)
nav_order: 207
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Codeine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "Codeine"
predicted_indications: ["acute laryngopharyngitis", "trigeminal autonomic cephalalgia", "allergic urticaria"]
---

# Codeine
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

# Codeine: From Allergic Rhinitis and Common Cold Symptoms to Nasal Cavity Disease

## One-Sentence Summary

Codeine is an opioid medicine originally used for symptom relief in upper respiratory conditions (allergic rhinitis, pharyngitis, common cold) and headache disorders.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but this rests on a very high model score alone: **0 clinical trials** and **1 publication** (a case report describing an adverse event, not a benefit) are available.
The evidence does not currently support a therapeutic repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis, headache disorder |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

*Note: The original indications come from the TxGNN knowledge graph, because the approved indication text in the India licence records is blank.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, codeine is an opioid used mainly for cough suppression and mild pain relief. Its use in upper respiratory symptoms is well established, and mechanistically it acts through mu-opioid receptors in the central nervous system.

The high prediction score most likely reflects the closeness of nasal cavity disease to the approved indications (rhinitis, nasopharyngitis) in the knowledge graph. This is anatomical and symptomatic adjacency, not proof of benefit. Codeine's central antitussive and analgesic actions do not address nasal pathology, and no plausible mechanism for treating nasal cavity disease is supported.

The only publication is a case report of a rhinolith (nasal stone) that formed around a hardened codeine and opium foreign body. This is an incidental or adverse event, not a therapeutic effect.

Other predictions in the ranked list show the same pattern:
- **Acute laryngopharyngitis** (score 99.92%): no trials or literature; adjacent to the approved pharyngitis and cold indications. Codeine use in children with upper respiratory conditions is restricted because of ultra-rapid CYP2D6 metabolism risk.
- **Trigeminal autonomic cephalalgia** (score 99.43%): opioids are not recommended for cluster headache, and the retrieved papers show no codeine benefit. Opioids also carry a risk of medication-overuse headache and dependence.
- **Allergic urticaria** (score 99.37%): the literature points in the opposite direction. Codeine directly triggers mast-cell histamine release and is used as a positive control in skin tests, so it can provoke urticaria rather than treat it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case report | Ear, Nose & Throat Journal | A 21-year-old man had a rhinolith formed around a hardened codeine and opium foreign body ("opioma"). It was an unusual cause of nasal obstruction, not a treatment benefit. |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 52843 | Codybex Syrup | Syrup, 100 ml bottle | Not stated in the licence record |
| 43548 | Codifem Syrup | Syrup, 100 ml bottle | Not stated in the licence record |
| 129888 | Lecof-C Syrup | Syrup, 100 ml bottle | Not stated in the licence record |
| 36031 | Codine Sulphate 15mg Tablet | Tablet, strip of 10 | Not stated in the licence record |
| 34726 | Codeine Phosphate Linctus | Linctus, 60 ml bottle | Not stated in the licence record |

Twenty single-ingredient licences are currently valid (none cancelled). Most are syrups, with a few tablet and linctus products.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (not label text): hypertension, liver failure and liver disease, kidney disease, epilepsy, insomnia, chronic obstructive pulmonary disease, anxiety and other mental disorders (including psychotic disorders), porphyria, pancreatitis, gallbladder disease, thrombocytopenia, hypothyroidism, peptic ulcer disease, inflammatory bowel disease, gastritis, and dermatitis herpetiformis.
- **Drug interactions**: 449 interactions are recorded. The major ones listed are **alvimopan** and **bupropion**. Moderate ones include atropine, cimetidine, dexamethasone, dicyclomine, glycopyrronium, hyoscyamine, loperamide, granisetron, dolasetron and fenfluramine.
- **Paediatric use**: Ultra-rapid CYP2D6 metabolism makes codeine risky in children with upper respiratory conditions.
- **Urticaria**: Codeine can directly provoke mast-cell degranulation and urticaria, which is relevant for patients with urticaria or asthma.
- **Headache**: Opioid use carries a risk of medication-overuse headache and dependence.

Package insert warnings and contraindications were not available, so please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but the evidence is model prediction only (L5), with no clinical trials and a single case report that describes an adverse event. There is no plausible mechanism for benefit in nasal cavity disease, and codeine has meaningful safety concerns.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator, which are required before any safety screening
- Mechanism of action data (for example, from DrugBank)
- Any controlled clinical evidence showing therapeutic benefit in nasal cavity disease, which does not currently exist
- A review of the paediatric and respiratory risks, and the mast-cell and urticaria signal, if the project continues
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

