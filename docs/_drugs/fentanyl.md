---
layout: default
title: Fentanyl
parent: Model Prediction Only (L5)
nav_order: 345
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Fentanyl: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not stated in the available India licence records"
monitor_inn: "Fentanyl"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome"]
---

# Fentanyl
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Fentanyl: From Opioid Analgesia to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Fentanyl is a potent mu-opioid receptor agonist marketed in India as transdermal patches and injections. The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but **no clinical trials and no publications** support this prediction. It rests on a computational score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available India licence records |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9946 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 15 of 15) |
| Number of Registrations | 15 (valid: 15) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Fentanyl is known to be a mu-opioid receptor agonist, and the original indication text is missing from the licence records.

NSIAD is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2). These mutations cause water retention in the kidney independent of vasopressin. Opioids can influence vasopressin release through central pathways. However, NSIAD is driven by constitutive receptor activation in the kidney, so a central opioid effect would not be expected to correct it. Opioids are also more often associated with SIADH-like effects (increased antidiuretic hormone activity), which suggests possible harm rather than benefit.

**The prediction is therefore not mechanistically supported.** The high score of 0.9946 is a computational output only.

A second predicted indication, **Tourette syndrome** (score 0.9905, also L5, Hold), has a weak and speculative link. Opioid-modulating agents such as buprenorphine and naltrexone have been explored in small tic-suppression studies. Fentanyl is a short-acting, high-abuse-liability opioid with respiratory depression risk. It is poorly suited to a chronic neuropsychiatric condition normally managed with alpha-2 agonists, antipsychotics, or behavioural therapy (CBIT). No trials or publications support this prediction either.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

All 15 registrations are valid single-ingredient products, and none has been cancelled. The main authorisations are listed below. The licence records contain no approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 59004 | Durogesic 25mcg Patch (Janssen Pharmaceuticals) | Packet of 3 transdermal patches | Not stated |
| 59860 | Durogesic 50mcg Patch (Janssen Pharmaceuticals) | Packet of 3 transdermal patches | Not stated |
| 85177 | Fendrop 25mcg Patch (Sun Pharmaceutical Industries) | Packet of 1 transdermal patch | Not stated |
| 164595 | Opifent 500 Injection (Varenyam Healthcare) | Ampoule of 10 ml injection | Not stated |
| 84345 | Fent 50mcg Injection (Neon Laboratories) | Vial of 2 ml injection | Not stated |

Available forms are transdermal patches and injectables.

---

## Safety Considerations

- **Contraindication signals (knowledge graph, not label text):** The TxGNN knowledge graph links fentanyl to contraindications in several disease groups:
  - Cardiovascular: hypotensive disorder, orthostatic hypotension, hypertension, long QT syndrome, torsades de pointes
  - Respiratory: COPD, asthma (including allergic and intrinsic forms)
  - Hepatic and renal: liver failure, liver disease, kidney disease
  - Gastrointestinal: pancreatitis, gallbladder disease, inflammatory bowel disease
  - Neurological and psychiatric: multiple system atrophy, basal ganglia disease, focal hand dystonia, blepharospasm, anxiety disorder, substance abuse/dependence
  - Other: benign prostatic hyperplasia, potassium deficiency disease
- **Drug interactions:** 327 interactions were recorded. Examples of **Major** interactions include alvimopan, aprepitant, bupropion, clarithromycin, clotrimazole, dexamethasone, dolasetron, fenfluramine, dexfenfluramine, granisetron and lorcaserin. **Moderate** interactions include atropine, cimetidine, clidinium, dicyclomine, dronabinol, eluxadoline, glycopyrronium and hyoscyamine.

Please refer to the package insert for label warnings and contraindications. These were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical or literature support (L5). The mechanistic reasoning suggests the drug is unlikely to correct NSIAD and may worsen it. Fentanyl also carries serious safety risks, including respiratory depression and abuse liability.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator's website, which block safety screening
- Confirmed mechanism of action data from DrugBank
- Preclinical or mechanistic evidence that fentanyl affects AVPR2-driven water retention
- Original approved indication text for the India licences
- A review of the NSIAD safety concern, since opioids may increase antidiuretic hormone activity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

