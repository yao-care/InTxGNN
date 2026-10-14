---
layout: default
title: Dexketoprofen
parent: Model Prediction Only (L5)
nav_order: 252
evidence_level: L5
indication_count: 10
---

# Dexketoprofen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Dexketoprofen: From Pain Relief to Migraine

## One-Sentence Summary

Dexketoprofen is a non-steroidal anti-inflammatory drug (NSAID) that is marketed in India as tablets, injections and a topical gel.
The TxGNN model predicts it may be effective for **migraine disorder** (the top-ranked prediction, tendinitis, has only indirect evidence), with **5 clinical trials** and **more than 20 publications** supporting this direction, including placebo-controlled randomized trials and a meta-analysis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the data compiled for this report (the approved indication text of the India licences is blank) |
| Predicted New Indication | Migraine disorder (the strongest-evidence prediction; the first-ranked prediction by TxGNN is tendinitis) |
| TxGNN Prediction Score | 99.87% (migraine disorder); 99.90% (tendinitis) |
| Evidence Level | L1 (with caveats: the trials are Phase 4 or N/A rather than Phase 3, and are mostly emergency department studies) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Proceed with Guardrails |

Note: The top-ranked prediction, tendinitis (score 99.90%), has only one indirect study (L4, Hold). This report focuses on migraine disorder, the prediction with the strongest supporting evidence.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, dexketoprofen is an NSAID that inhibits cyclo-oxygenase (COX-1 and COX-2), thereby reducing prostaglandin production, inflammation and pain. Its analgesic efficacy is well established, and mechanistically it may be applicable to migraine.

Prostaglandin-mediated neurogenic inflammation and sensitization of pain pathways contribute to migraine attacks, so COX inhibition is biologically plausible. Dexketoprofen has been tested directly in acute migraine, including placebo-controlled trials, a meta-analysis, and combination studies with the triptan frovatriptan.

The same trial set also supports a broader "headache disorder" prediction, but the evidence is strongest for migraine specifically. Migraine with brainstem aura (a migraine subtype) is supported only by extrapolation from general migraine studies.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02159547](https://clinicaltrials.gov/study/NCT02159547) | Phase 4 | Completed | 224 | IV dexketoprofen vs placebo in migraine attack in the emergency department |
| [NCT04252521](https://clinicaltrials.gov/study/NCT04252521) | N/A | Completed | 150 | IV metoclopramide vs dexketoprofen trometamol vs combination in acute migraine; randomized, double-blind |
| [NCT04533568](https://clinicaltrials.gov/study/NCT04533568) | Phase 4 | Completed | 160 | IV ibuprofen vs IV dexketoprofen for migraine headache in the emergency department |
| [NCT01730326](https://clinicaltrials.gov/study/NCT01730326) | Phase 4 | Completed | 200 | IV dexketoprofen vs paracetamol for headache in acute migraine attack |
| [NCT04372264](https://clinicaltrials.gov/study/NCT04372264) | Phase 4 | Unknown | 210 | IV paracetamol vs dexketoprofen vs ibuprofen on pain score (VAS) in acute migraine; double-blind |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31725614](https://pubmed.ncbi.nlm.nih.gov/31725614/) | 2019 | Meta-analysis | Medicine | Meta-analysis of randomized studies of dexketoprofen vs placebo for pain control in migraine attack |
| [25944813](https://pubmed.ncbi.nlm.nih.gov/25944813/) | 2016 | RCT | Cephalalgia | IV dexketoprofen vs placebo for aborting migraine in the emergency department |
| [24412801](https://pubmed.ncbi.nlm.nih.gov/24412801/) | 2014 | RCT (Phase II) | The Journal of Pain | Dexketoprofen trometamol 25 mg and 50 mg vs placebo in 93 patients; crossover dose-optimization study |
| [32359776](https://pubmed.ncbi.nlm.nih.gov/32359776/) | 2020 | RCT | Am J Emerg Med | IV metoclopramide vs dexketoprofen vs combination in acute migraine |
| [24394884](https://pubmed.ncbi.nlm.nih.gov/24394884/) | 2014 | RCT | Emerg Med J | IV paracetamol vs dexketoprofen in acute migraine in the emergency department |
| [24363238](https://pubmed.ncbi.nlm.nih.gov/24363238/) | 2014 | RCT | Cephalalgia | Frovatriptan plus dexketoprofen vs frovatriptan alone in migraine with or without aura |
| [25056381](https://pubmed.ncbi.nlm.nih.gov/25056381/) | 2014 | RCT | Expert Rev Neurother | Efficacy and tolerability of frovatriptan and dexketoprofen in acute migraine |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline | Headache | American Headache Society 2025 update on parenteral treatments for migraine in the emergency department |
| [37291500](https://pubmed.ncbi.nlm.nih.gov/37291500/) | 2023 | Meta-analysis | BMC Neurology | Network meta-analysis of metoclopramide vs other anti-migraine drugs |
| [30744914](https://pubmed.ncbi.nlm.nih.gov/30744914/) | 2019 | RCT | Am J Emerg Med | IV dexketoprofen vs paracetamol in non-traumatic musculoskeletal pain (indirect evidence for the tendinitis prediction) |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 66672 | Deket-P 25mg/325mg Tablet | Strip of 10 tablets | Not stated |
| 180872 | Puron 50mg Injection | Vial of 2 ml injection | Not stated |
| 108262 | Infen 25 Tablet | Strip of 10 tablets | Not stated |
| 109815 | Infen 50mg Injection | Vial of 2 ml injection | Not stated |
| 107911 | Infen P Tablet | Strip of 10 tablets | Not stated |

A sixth licence (108166, Infen Gel, 30 g tube, topical) is also valid. All 6 registrations are single-ingredient products and currently valid.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several randomized trials, including placebo-controlled studies, and a meta-analysis support dexketoprofen in acute migraine, and the drug is already marketed in India in oral and injectable forms. However, the trials are Phase 4 or N/A rather than Phase 3, and are mostly emergency department studies, so the L1 level should be read with caution. Other predictions (tendinitis, fibromyalgia, rheumatoid arthritis, and others) have little or no direct evidence and should remain on Hold.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India licences (currently missing, and blocking safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the regulatory status and approved indication text for migraine in India
- Safety precautions for NSAIDs (gastrointestinal, renal and cardiovascular risks) and limits on use frequency to avoid medication-overuse headache
- Evidence in outpatient settings and for oral formulations, since most trials used the IV route in emergency departments
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

