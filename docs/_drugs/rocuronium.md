---
layout: default
title: Rocuronium
parent: Model Prediction Only (L5)
nav_order: 750
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
description: "Rocuronium: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the Indian licence records compiled for this report"
monitor_inn: "Rocuronium"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "cauda equina syndrome", "atrophoderma vermiculata", "ulerythema ophryogenesis", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "sciatic neuropathy", "headache disorder"]
---

# Rocuronium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Rocuronium: From Neuromuscular Blockade in Anaesthesia to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Rocuronium is a non-depolarizing neuromuscular blocking agent marketed in India as an injection. The TxGNN model predicts it may be effective for **migraine disorder**, but the prediction rests on **1 clinical trial that is not relevant to efficacy** and **no supporting publications**. The prediction appears to be a TxGNN model (deep learning) artifact rather than a real therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Indian licence records compiled for this report |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (11 of 11) – CDSCO approval status is not included in this data |
| Number of Registrations | 11 (valid: 11) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From general pharmacology, rocuronium is a non-depolarizing neuromuscular blocker. It competitively antagonizes nicotinic acetylcholine receptors at the neuromuscular junction and is used as an anaesthetic adjunct for muscle relaxation.

This mechanism has no established link to migraine pathophysiology, such as CGRP signalling, trigeminovascular activation or cortical spreading depression. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top predictions point the same way. They include migraine with brainstem aura, cauda equina syndrome, atrophoderma vermiculata and irritable bowel syndrome, and none has a plausible mechanistic rationale. Several are clustered around migraine-related terms, which suggests ontology proximity drives the results. Rocuronium also requires intravenous administration with ventilatory support, which makes use in a chronic condition like migraine impractical.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3520 | Pharmacokinetic study of understudied drugs given to children as standard of care. It does not test migraine efficacy, and the match appears incidental (relevance grade C). |

---

## Literature Evidence

Currently no related literature is available for migraine disorder.

For the related prediction **headache disorder** (score 0.9909), two publications were found. Neither shows that rocuronium treats headache.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23812022](https://pubmed.ncbi.nlm.nih.gov/23812022/) | 2014 | Clinical study | J ECT | Compared succinylcholine with rocuronium-sugammadex for myalgia and headache after electroconvulsive therapy. This is a perioperative side-effect outcome, not headache treatment. |
| [24196089](https://pubmed.ncbi.nlm.nih.gov/24196089/) | 2013 | Case report | Pediatr Emerg Care | Rapid sequence intubation in a child with elevated intracranial pressure. Rocuronium is mentioned only as an anaesthetic adjunct. |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 117347 | Kabiroc 10mg Injection (Fresenius Kabi India) | Vial of 5 ml injection | Not stated |
| 189625 | Rocsur 50mg Injection (Gland Pharma) | Vial of 5 ml injection | Not stated |
| 78509 | Esmeron 100mg Injection (Organon India) | Vial of 10 ml injection | Not stated |
| 185921 | Rocunium 50mg Injection (Neon Laboratories) | Vial of 5 ml injection | Not stated |
| 194149 | Rocutroy 10mg Injection (Troikaa Pharmaceuticals) | Vial of 5 ml injection | Not stated |

There are 11 valid single-ingredient registrations in total, all injectable.

---

## Safety Considerations

**Drug Interactions:** 73 interactions were identified. Among the entries reviewed, the main ones are:
- **Major:** paromomycin, kanamycin, neomycin (aminoglycosides, which may potentiate neuromuscular blockade)
- **Moderate:** doxycycline, tetracycline, minocycline, vancomycin, magnesium sulfate, magnesium chloride, amphotericin B, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, prednisone), mannitol, metoclopramide
- **Minor:** ranitidine

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by model output. The single linked trial is an unrelated pediatric pharmacokinetic study, and no literature supports a migraine benefit. No plausible mechanism connects neuromuscular blockade to migraine, and the intravenous, ventilator-dependent use of rocuronium makes a migraine indication impractical.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator
- Confirmed approved indications and mechanism of action data
- Any mechanistic or preclinical evidence linking rocuronium to migraine pathophysiology
- A reassessment of whether other candidates are more biologically plausible, since the predictions for this drug look like TxGNN model (deep learning) artifacts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

