---
layout: default
title: Aprepitant
parent: Model Prediction Only (L5)
nav_order: 65
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Aprepitant: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not available in the compiled data (aprepitant is generally known as…"
monitor_inn: "Aprepitant"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "hypertrichosis (disease)", "pulmonary hypertension", "leprosy", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "kyphoscoliotic heart disease", "syndrome with a Dandy-Walker malformation as major feature", "subarachnoid hemorrhage (disease)", "isolated genetic hair shaft abnormality"]
---

# Aprepitant
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

## Aprepitant: From Chemotherapy-Related Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Aprepitant is an NK1 receptor antagonist marketed in India in several oral and injectable products. The approved indication text was not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis**, but **no clinical trials and no relevant publications** currently support this prediction. It is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (aprepitant is generally known as an antiemetic) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for aprepitant: "Aprepitant is a selective high-affinity antagonist of human substance P/neurokinin 1 (NK 1 ) receptors. Aprepitant has little or no affinity for serotonin (5-HT 3 ), dopamine, and corticosteroid receptors. Aprepitant has been shown in animal models to inhibit emesis induced by cytotoxic chemotherapeutic agents, such as cisplatin, via central actions." ([DailyMed: Cinvanti (aprepitant) prescribing information, Heron Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4c218d3a-a508-4abc-9ed8-a6e8e191d1b4), label version 2026-04-01; accessed 2026-11-19.) Based on known information, aprepitant is an NK1 receptor antagonist, which blocks substance P signaling. Its efficacy in its established antiemetic use is well known, but it is unclear whether this mechanism applies to the new indication.

Substance P/NK1 signaling has been loosely linked to fluid and vasopressin regulation. However, nephrogenic syndrome of inappropriate antidiuresis is caused by gain-of-function mutations in the V2 vasopressin receptor, and no established mechanistic link to NK1 antagonism exists. The high score (0.9997) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should not be read as evidence of efficacy.

Other top-ranked predictions (for example hypertrichosis, pulmonary hypertension, leprosy and subarachnoid hemorrhage) also have no supporting clinical evidence. Subarachnoid hemorrhage has a biologically plausible but unvalidated preclinical hypothesis (substance P/NK1 involvement in blood-brain barrier disruption and cerebral edema).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the predicted indication.

## India Market Information

Twenty valid registrations were found. Approved indication text was not available for any of them.

<!-- review:begin in-lic-20261124c-aprepitant-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Twenty valid single-ingredient registrations were found." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-aprepitant-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 421 | Aprecap 125/80 Capsule | Strip of 3 capsules | Valid |
| 1956 | Aprecap 150mg Injection | Vial of 1 Injection | Valid |
| 2335 | Apretero 125/80 Kit | Packet of 1 Kit | Valid |
| 2429 | Apristar 125 mg/80 mg Capsule | Strip of 3 capsules | Valid |
| 2741 | Apriset Kit | Packet of 3 kit | Valid |
| 4444 | Apriset 150mg Injection | Vial of 10 ml Injection | Valid |
| 5323 | Aprebion Kit | Box of 3 capsules | Valid |
| 6514 | Aprelief Kit | Strip of 1 Kit | Valid |
| 7557 | Aprepit Kit | Packet of 1 Kit | Valid |
| 8227 | Aprifer 125mg/80mg Capsule | Strip of 1 Capsule | Valid |
| 8624 | Amitant Kit | Box of 1 Kit | Valid |
| 12638 | Apricyt Kit | Packet of 3 capsules | Valid |
| 15973 | Aprepep 125mg Capsule | Strip of 3 capsules | Valid |
| 73901 | Emend 125mg/80mg Capsule | Strip of 3 capsules | Valid |
| 74628 | Emvoid 125 mg/80 mg Capsule | Strip of 3 capsules | Valid |
| 75079 | Emvoid Injection | Vial of 1 Injection | Valid |
| 85346 | Fos-Aprepitant 125mg Tablet | Strip of 3 tablets | Valid |
| 89745 | Fosapine 150mg Injection | Vial of 1 Injection | Valid |
| 167245 | Opilo Kit | Packet of 1 Kit | Valid |
| 176590 | Prepit Capsule | Box of 1 Kit | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Other registered products include fosaprepitant injections and tablets, and multiple kit presentations from Alkem, Sun, Intas, Abbott, Lupin, Hetero and others.

## Cytotoxicity

Aprepitant is a supportive-care antiemetic, not an antineoplastic agent, so this section does not apply.

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: The TxGNN knowledge graph lists a contraindication association with **liver failure**.
- **Drug Interactions**: 469 interactions were identified. The examples below come from the compiled sample:
  - **Major**: Fentanyl, Alfentanil, Acalabrutinib
  - **Moderate**: Paclitaxel, Abemaciclib, Nifedipine, Ibuprofen, Levonorgestrel, Hydrocortisone, Rabeprazole, Fluvoxamine, Fosphenytoin, Gefitinib, among others
  - **Minor**: Dolutegravir

Package insert warnings and contraindications were not available. Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or relevant publications, and no plausible link between NK1 antagonism and the V2 receptor gain-of-function mechanism of this disease. The single literature record matched to another prediction (pulmonary hypertension) concerns an unrelated drug and is not evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently blocking safety screening)
- Mechanism of action data (for example from DrugBank)
- Preclinical evidence of NK1/substance P involvement in this disease
- A review of the knowledge-graph liver failure contraindication
- A target-population assessment, since this is an ultra-rare disease, and a review of the interaction burden for likely co-medications

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cinvanti (aprepitant) prescribing information, Heron Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4c218d3a-a508-4abc-9ed8-a6e8e191d1b4) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

