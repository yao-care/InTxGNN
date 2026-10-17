---
layout: default
title: Alfuzosin
parent: Model Prediction Only (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Alfuzosin: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
monitor_inn: "Alfuzosin"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "allergic urticaria", "persistent fetal circulation syndrome", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
---

# Alfuzosin
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

# Alfuzosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Alfuzosin is an alpha-1 adrenergic receptor blocker originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, alfuzosin is a selective alpha-1 adrenergic receptor antagonist. It relaxes smooth muscle in the prostate and bladder neck, which is why it works in BPH.

A plausible mechanistic link to the predicted indication has not been established. Ambras syndrome is a rare genetic form of hypertrichosis, associated with structural rearrangements on chromosome 8q that affect regulation of the TRPS1 gene. Blocking alpha-1 receptors has no known effect on this pathway. The very high score most likely reflects proximity in the knowledge graph rather than a real therapeutic signal.

The other top-ranked predictions point the same way. They are mostly hair-related genetic conditions (hypertrichosis, trichomegaly, hair shaft abnormalities, hypotrichosis), plus a few developmental malformation syndromes. The same drug is predicted for opposing hair phenotypes (too much hair and too little hair). This suggests the model is picking up generic hair-phenotype associations. For hypertrichosis, the direction of effect is also unclear. Some vasoactive drugs, such as minoxidil, cause hypertrichosis rather than treat it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

All 20 registrations are valid single-ingredient licences. The data compiled for this report does not include approved-indication text. The table lists 5 of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 7778 | Alfuin 10mg Tablet | Strip of 10 tablets | Elio Biocare Lifesciences Pvt Ltd |
| 232426 | Urofuz 10mg Tablet | Strip of 10 tablets | Curis Lifecare |
| 4920 | Alfunex 10mg Tablet | Strip of 10 tablets | Nexkem Pharmaceuticals Pvt Ltd |
| 7592 | Alfuzin 10mg Tablet ER | Strip of 10 extended-release tablets | Astonea Labs Private Limited |
| 233503 | Velfu Tablet PR | Strip of 7 prolonged-release tablets | Intas Pharmaceuticals Ltd |

All products are oral tablets. Several are fixed-dose combinations with dutasteride (e.g., Sterdu L, Alfunol D, Emzosin D).

## Safety Considerations

- **Contraindications and risk conditions (from the knowledge graph, not label text)**: multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, hypotensive disorder, long QT syndrome (including familial), torsades de pointes, liver failure, liver disease, gallbladder disease, and intraoperative floppy iris syndrome.
- **Drug Interactions**: 198 interactions were identified in total. The main ones are:
  - **Major**: cisapride, clarithromycin, dolasetron. These are likely related to QT prolongation or CYP3A4 inhibition.
  - **Moderate**: examples include famotidine, aprepitant, bupropion, levofloxacin, granisetron, and the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin).
  - **Minor**: cimetidine.

Package insert warnings were not available, so please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5). There are no clinical trials or publications, and no plausible mechanism links alpha-1 blockade to Ambras-type hypertrichosis. The treatment direction is also uncertain, and the opposing hair phenotypes among the top predictions suggest a non-specific signal. None of the other nine ranked predictions is better supported.

**To proceed, the following is needed:**
- Mechanism of action data for alfuzosin, plus a biological rationale linking it to TRPS1 or hair follicle regulation
- Preclinical evidence (e.g., hair follicle models) showing a therapeutic rather than inducing effect
- Package insert warnings and contraindications from the India market, for a safety screening
- A review of whether the knowledge-graph prediction reflects real biology or only graph proximity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

