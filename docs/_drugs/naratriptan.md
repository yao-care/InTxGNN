---
layout: default
title: Naratriptan
parent: 僅模型預測 (L5)
nav_order: 377
evidence_level: L5
indication_count: 3
---

# Naratriptan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Naratriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Naratriptan is a selective serotonin 5-HT1B/1D receptor agonist (triptan class), originally approved for the acute treatment of migraine headache with or without aura.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura (MBA)** — a subtype previously known as basilar-type migraine — with **0 registered clinical trials** but **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute migraine treatment (with or without aura) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Naratriptan is a selective 5-HT1B/1D receptor agonist belonging to the triptan class. It exerts its anti-migraine effect by causing constriction of dilated cranial blood vessels and inhibiting the release of neuropeptides (CGRP, substance P) from trigeminal nerve endings — both of which are core pathophysiological targets in migraine.

Migraine with Brainstem Aura (MBA) is a migraine subtype in which aura symptoms originate from the brainstem rather than the cerebral cortex. The basilar artery and brainstem circuitry are regions where 5-HT1B/1D receptors are expressed, providing a direct mechanistic basis for potential triptan efficacy. Historically, triptans were considered contraindicated in this subtype due to theoretical concerns about vasoconstriction in the posterior circulation; however, Naratriptan's comparatively weaker vasoconstrictive potency and higher 5-HT1D selectivity relative to sumatriptan represent a more favourable safety profile within the triptan class.

Emerging evidence and evolving headache society guidelines increasingly suggest that the risk of posterior circulation ischaemia from triptans in MBA is largely theoretical, and that the trigeminovascular mechanism is shared across migraine subtypes. The TxGNN model's prediction is therefore mechanistically plausible, though prospective safety data specific to this subtype remain an important gap to address before routine clinical adoption.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Naratriptan in migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10972634](https://pubmed.ncbi.nlm.nih.gov/10972634/) | 2000 | RCT (Phase 3) | Clinical Therapeutics | Randomised crossover study comparing naratriptan vs sumatriptan in recurrence-prone migraine patients; naratriptan demonstrated a lower headache recurrence rate |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Systematic Review | Headache | American Headache Society evidence assessment: naratriptan rated as an established effective therapy for acute migraine treatment in adults |
| [11264684](https://pubmed.ncbi.nlm.nih.gov/11264684/) | 2001 | RCT | Headache | Naratriptan 2.5 mg twice daily significantly more effective than placebo for short-term prophylaxis of menstrually associated migraine |
| [10961768](https://pubmed.ncbi.nlm.nih.gov/10961768/) | 2000 | Clinical Trial | Cephalalgia | Naratriptan administered during the prodrome phase showed potential to prevent development of full migraine attacks |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort Study | Neurology | Sumatriptan showed reduced efficacy in migraine with aura vs without aura, highlighting that aura subtype may influence triptan response — relevant to MBA considerations |
| [15926020](https://pubmed.ncbi.nlm.nih.gov/15926020/) | 2005 | Clinical Trial | Neurological Sciences | Open-label pilot study confirming naratriptan efficacy and tolerability as short-term prophylaxis specifically for pure menstrual migraine |
| [17578540](https://pubmed.ncbi.nlm.nih.gov/17578540/) | 2007 | Open-label Study | Headache | Long-term tolerability of intermittent naratriptan for menstrually related migraine prophylaxis confirmed over extended follow-up |
| [14511276](https://pubmed.ncbi.nlm.nih.gov/14511276/) | 2003 | Case Series | Headache | Naratriptan found useful for managing intractable migraine cases refractory to standard therapy |
| [23877022](https://pubmed.ncbi.nlm.nih.gov/23877022/) | 2014 | Case Report | Brain & Development | Naratriptan remarkably improved intractable migraine-like headaches with visual aura (homonymous hemianopsia) in a Sturge-Weber syndrome patient with prior cerebral infarction |
| [27910087](https://pubmed.ncbi.nlm.nih.gov/27910087/) | 2017 | Narrative Review | Headache | Comprehensive review of menstrual migraine treatment options; naratriptan cited as an effective acute and short-term prophylactic agent within the triptan class |

---

## India Market Information

Naratriptan currently has **no registered products in India** (total licenses: 0). The drug is not approved or commercially marketed in the Indian market at this time.

---

## Safety Considerations

**Drug Interactions:** Naratriptan has 39 documented drug interactions. Clinically significant major interactions are summarised below:

| Interacting Drug | Severity | Clinical Concern |
|-----------------|----------|-----------------|
| Lorcaserin | Major | Serotonin syndrome risk (combined serotonergic activity) |
| Fenfluramine / Dexfenfluramine | Major | Serotonin syndrome risk |
| Sibutramine | Major | Serotonin syndrome risk |
| Dolasetron | Major | Serotonin syndrome risk (paradoxical — 5-HT3 antagonism plus downstream serotonergic effects) |
| Palonosetron | Major | Serotonin syndrome risk |
| Granisetron | Major | Serotonin syndrome risk |
| Ondansetron | Major | Serotonin syndrome risk |
| Methylene blue | Major | Serotonin syndrome risk (MAO inhibition mechanism) |
| Morphine / Morphine (liposomal) | Moderate | Potentiated CNS and respiratory depression |

Please refer to the full package insert for complete warnings, contraindications, and additional safety information, as formal prescribing label data were not available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Naratriptan's 5-HT1B/1D receptor mechanism directly targets the trigeminovascular pathophysiology shared by all migraine subtypes including MBA, and its comparatively mild vasoconstrictive profile makes it the most pharmacologically rational triptan candidate for this indication. Multiple publications including Phase 3 RCTs and a systematic review establish its efficacy and tolerability in migraine broadly, warranting further investigation in the brainstem aura subtype rather than an outright hold.

**To proceed, the following is needed:**
- Prospective clinical trial data specifically enrolling patients with confirmed migraine with brainstem aura (IHS ICHD-3 criteria)
- Full prescribing information / package insert (FDA or EMA label) to document contraindications, boxed warnings, and restricted populations
- Detailed MOA documentation retrieved from DrugBank to formalise the mechanistic dossier
- Dedicated posterior circulation safety monitoring protocol (MRI/MRA endpoint, neurological assessment) for any investigational use
- India regulatory pathway assessment — since the drug is not currently marketed in India, a fresh registration or import licence would be required prior to any clinical investigation
- Neurologist and headache specialist review of the risk-benefit balance specifically for the brainstem aura subtype, given evolving but still incomplete guidance from IHS and major headache societies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

