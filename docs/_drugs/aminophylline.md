---
layout: default
title: Aminophylline
parent: Moderate Evidence (L3-L4)
nav_order: 51
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-30
description: "Aminophylline: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated on the Indian licences in the data compiled for this report"
monitor_inn: "Aminophylline"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "ulerythema ophryogenesis", "Prinzmetal angina", "pulmonary hypertension", "sciatic neuropathy", "hyperthyroidism", "kyphoscoliotic heart disease"]
---

# Aminophylline
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **9** 
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

## Aminophylline: From Respiratory Airway Disease (Indication Not Stated on Licences) to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Aminophylline is a methylxanthine drug (a theophylline salt) that is marketed in India, mainly as an injection, and the approved indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **no registered clinical trials** and only **4 publications**, mostly narrative, case-level or mechanistic.
This is an early-stage research question, not a validated repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated on the Indian licences in the data compiled for this report |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L4 (mechanistic and narrative literature only; no clinical trials) |
| India Market Status | Listed in a compiled Indian medicine price dataset (7 of 7) – CDSCO approval status is not included in this data |
| Number of Listed Products | 7 (valid: 7) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Aminophylline is a non-selective adenosine receptor antagonist and phosphodiesterase inhibitor. Adenosine signalling has been linked to migraine through activation of the trigeminovascular system and cerebral vasodilation. A 2023 review proposes that migraine may involve impaired brain energy metabolism with abnormally high adenosine levels, and that aminophylline has given pain relief, particularly in post-dural headache.

A case report also describes a hemiplegic migraine episode triggered by regadenoson, an adenosine A2A receptor agonist. This supports the idea that adenosine-pathway activation can provoke migraine, so blocking it could plausibly help.

Detailed mechanism of action data was not available in the compiled data, so the reasoning above is drawn from the literature rather than a curated mechanism record. The link remains hypothesis-level: no trial has tested aminophylline in migraine.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine disorder.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38059379](https://pubmed.ncbi.nlm.nih.gov/38059379/) | 2023 | Review | Pain Management | Proposes that migraine involves high adenosine and impaired brain energy metabolism. Discusses aminophylline, an adenosine antagonist, as giving therapeutic relief in pain, especially post-dural headache, and cites an observational case series in migraine. |
| [34308528](https://pubmed.ncbi.nlm.nih.gov/34308528/) | 2022 | Case report | J Nucl Cardiol | Hemiplegic migraine triggered by regadenoson (an adenosine A2A agonist). Supports a role for adenosine signalling in migraine. |
| [7728647](https://pubmed.ncbi.nlm.nih.gov/7728647/) | 1995 | Case report | Can J Cardiol | Patient with syndrome X attributed to excessive adenosine effect ("myocardial migraine"). Indirect link to adenosine excess. |
| [14168418](https://pubmed.ncbi.nlm.nih.gov/14168418/) | 1964 | Review | Aggiornamenti Clinicoterapeutici | Historical review of medical headaches. No abstract available. |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 7456 | Aminophyllin 250mg Injection | Vial of 10 ml injection | Not stated |
| 221782 | Theoresp A Tablet | Strip of 10 tablets | Not stated |
| 3018 | Aminophylin Injection | Vial of 1 ml injection | Not stated |
| 27594 | Biofylin 250mg Injection | Vial of 1 injection | Not stated |
| 185377 | Renophyllline Injection | Ampoule of 10 ml injection | Not stated |

Seven valid single-ingredient licences are registered in total; the five above are shown. Six are injectable products and one is an oral tablet.

---

## Safety Considerations

- **Drug Interactions**: 279 interactions were identified in the data compiled for this report. Selected examples:
  - **Major**: Bupropion
  - **Moderate**: Famotidine, ranitidine, cimetidine, nizatidine, doxycycline, tetracycline, minocycline, clarithromycin, and the corticosteroids hydrocortisone, dexamethasone, betamethasone, triamcinolone and budesonide
  - **Minor**: Lansoprazole

Other safety signals from the literature on related predicted indications (not migraine) point to caution:
- Aminophylline withdrawal after dipyridamole stress has been reported to trigger coronary vasospasm in variant angina.
- Methylxanthines may worsen tremor and tachycardia in hyperthyroidism.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the only support for migraine is one narrative review, case reports and a mechanistic hypothesis. There are no registered trials, and the safety profile and licensed indication text could not be confirmed from the data compiled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator or manufacturers (currently blocking any safety screening)
- Approved indication text for the Indian licences
- Curated mechanism of action data
- Critical appraisal of the observational case series cited in the 2023 review, followed by a small controlled study (for example, a pilot RCT in post-dural puncture headache or migraine) if the signal holds
- A narrow therapeutic window assessment (theophylline level monitoring, cardiac and seizure risk) for the migraine population
- Merging of the related migraine entities (migraine with brainstem aura, and migraine with or without aura susceptibility) into a single migraine assessment, since neither has independent evidence

**Other predicted indications (for context):**
- **Pulmonary hypertension** has the most developed evidence (L3): one Phase 1 safety and pharmacokinetic trial (NCT01530464, n=18) and mostly older, small hemodynamic and preclinical studies. It remains a research question.
- **Prinzmetal angina** and **hyperthyroidism**: the literature points to safety concerns rather than benefit.
- **Atrophoderma vermiculata**, **ulerythema ophryogenesis**, **sciatic neuropathy** and **kyphoscoliotic heart disease** have no meaningful support and are probably TxGNN model (deep learning) artifacts.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

