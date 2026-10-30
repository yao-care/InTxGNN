---
layout: default
title: Naratriptan
parent: Model Prediction Only (L5)
nav_order: 580
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
monitor_inn: "Naratriptan"
predicted_indications: ["atrophoderma vermiculata", "ulerythema ophryogenesis"]
description: "Naratriptan: predicted new indication Atrophoderma vermiculata (evidence level L5). Approved use: Not recorded in the local data"
---

# Naratriptan
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

## Naratriptan: Atrophoderma vermiculata
{: .text-alpha }

## One-Sentence Summary

Naratriptan is a triptan originally used to treat acute migraine.
However, there are **no registered clinical trials** and the **20 publications** identified are mostly general migraine or triptan studies, so the prediction is supported mainly by similarity to the approved indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Atrophoderma vermiculata |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Naratriptan is a selective 5-HT1B/1D receptor agonist approved for acute migraine. Currently, detailed mechanism of action data is not available in the data compiled for this report, but the class pharmacology of triptans is well established. It is believed to act on trigeminovascular activation, CGRP release and cranial vasodilation.

Migraine with brainstem aura is a subtype of migraine, so the underlying pathophysiology overlaps with the approved indication. This gives a plausible mechanistic link.

There are two caveats. First, none of the supplied literature studies brainstem aura specifically. Second, triptans have historically been used cautiously in this subtype (formerly called basilar-type migraine) because of theoretical vasoconstriction concerns. The high TxGNN score largely reflects similarity to the approved migraine indication, not independent evidence.

Two other predictions were also reviewed (atrophoderma vermiculata, 0.9974, and ulerythema ophryogenesis, 0.9947). Both have no clinical trials or literature and no plausible mechanistic link to 5-HT1B/1D agonism, so they are held at the model-prediction-only level (L5).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The publications below are general migraine or naratriptan studies. None addresses brainstem aura directly.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10972634](https://pubmed.ncbi.nlm.nih.gov/10972634/) | 2000 | RCT | Clinical Therapeutics | Randomized, double-blind crossover comparison of naratriptan and sumatriptan for headache recurrence in recurrence-prone migraine patients |
| [10961768](https://pubmed.ncbi.nlm.nih.gov/10961768/) | 2000 | RCT | Cephalalgia | Naratriptan given during the prodrome to test prevention of migraine headache |
| [11264684](https://pubmed.ncbi.nlm.nih.gov/11264684/) | 2001 | RCT (placebo-controlled) | Headache | Naratriptan 1 mg and 2.5 mg twice daily vs placebo as short-term prophylaxis of menstrually associated migraine |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort | Neurology | Sumatriptan was less effective in migraine with aura than without aura |
| [14511276](https://pubmed.ncbi.nlm.nih.gov/14511276/) | 2003 | Review | Headache | Managing intractable migraine with naratriptan |
| [21028917](https://pubmed.ncbi.nlm.nih.gov/21028917/) | 2010 | Review | Paediatric Drugs | Use of triptans for pediatric migraine |
| [15926020](https://pubmed.ncbi.nlm.nih.gov/15926020/) | 2005 | Open-label pilot study | Neurological Sciences | Naratriptan as short-term prophylaxis of pure menstrual migraine |
| [16268666](https://pubmed.ncbi.nlm.nih.gov/16268666/) | 2005 | Review | CNS Drugs | Triptans in the management of menstrual migraine |
| [23877022](https://pubmed.ncbi.nlm.nih.gov/23877022/) | 2014 | Case report | Brain & Development | Naratriptan improved intractable migraine-like headaches in a patient with Sturge-Weber syndrome and prior cerebral infarction |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 152736 | Naratrex 2.5 Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 2 tablets (oral) | Not stated in the data compiled |

## Safety Considerations

- **Contraindications (from knowledge-graph drug-disease links, not label text):** hypertension, liver failure, diabetes mellitus and diabetic ketoacidosis, coronary artery disease, myocardial infarction and myocardial ischemia, Prinzmetal angina, stroke and cerebrovascular disorders, cerebral infarction, transient ischemic attack, vertebrobasilar insufficiency, peripheral vascular and arterial disease, obesity, hemoglobinopathy, and familial or sporadic hemiplegic migraine.
- **Relevance to the predicted indication:** vertebrobasilar insufficiency and hemiplegic migraine appear on the list. They are closely related to brainstem aura, so safety in this subtype needs explicit evaluation.
- **Drug Interactions:** 39 interactions were identified. Major-level interactions include:
  - Serotonergic and related agents: lorcaserin, fenfluramine, dexfenfluramine, sibutramine, methylene blue
  - 5-HT3 antagonists: ondansetron, granisetron, dolasetron, palonosetron

  Moderate-level interactions include morphine (including liposomal). Several others, such as omeprazole, pantoprazole, lansoprazole, clarithromycin, bupropion and prednisone, are of unknown severity.

Please also refer to the package insert, as label warnings were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible because brainstem aura is a migraine subtype. However, there are no clinical trials, no literature specific to brainstem aura, and a theoretical vascular safety concern in this very subtype. The high model score mainly reflects similarity to the approved indication. The evidence supports treating this as a research question rather than a development decision.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian label (a blocking gap for safety screening)
- Detailed mechanism of action data
- Subtype-specific evidence, such as case series, registries or controlled studies of triptans in brainstem aura
- A formal cerebrovascular and cardiovascular safety assessment for this population
- The approved indication text for the Indian registration, to confirm the original-indication baseline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

