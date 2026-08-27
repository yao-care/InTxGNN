---
layout: default
title: Dapoxetine
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 3
---

# Dapoxetine
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

# Dapoxetine: From Premature Ejaculation to Migraine Disorder

## One-Sentence Summary

Dapoxetine is a short-acting selective serotonin reuptake inhibitor (SSRI), currently approved in multiple countries (but not India) for the treatment of premature ejaculation.
The TxGNN model predicts it may be effective for **Migraine Disorder**,
with **0 clinical trials** and **2 publications** (indirect evidence only) currently supporting this direction — primarily through the shared serotonergic mechanism. However, a fundamental pharmacokinetic limitation — Dapoxetine's ultra-short half-life (~1.5 h) — raises serious doubts about its clinical feasibility for migraine prevention.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Premature ejaculation |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 (mechanism/preclinical only) |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the standard data source. Based on pharmacological data retrieved from drug interaction databases, Dapoxetine is a **short-acting SSRI** that selectively inhibits the serotonin reuptake transporter (SERT, encoded by *SLC6A4*). Unlike conventional antidepressant SSRIs, it has an exceptionally short half-life (~1.5 hours), which is why it was specifically developed for on-demand use in premature ejaculation rather than as a daily therapeutic agent.

Serotonin (5-HT) plays a central role in migraine pathophysiology. The trigeminal vascular system expresses 5-HT₁B/1D receptors — the very targets exploited by triptans, the current standard-of-care for acute migraine. SSRIs increase synaptic 5-HT concentrations and theoretically could modulate cortical spreading depression (CSD) and trigeminal sensitisation, providing a plausible rationale for preventive use. Indeed, longer-acting SSRIs such as fluoxetine and venlafaxine have some evidence for migraine prophylaxis.

However, **Dapoxetine's pharmacokinetics present a fundamental barrier** to this repurposing hypothesis. Sustained 5-HT elevation over days to weeks — necessary for meaningful neuroplastic adaptation and stable migraine threshold modulation — cannot be achieved with a drug that is cleared within hours. This distinguishes Dapoxetine sharply from other SSRIs that have been explored in migraine prevention, and is a critical mechanistic mismatch the TxGNN model (which focuses on target-pathway relationships) cannot fully capture.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33998993](https://pubmed.ncbi.nlm.nih.gov/33998993/) | 2022 | Narrative Review | Current Neuropharmacology | Reviews the full landscape of off-label SSRI uses; includes migraine among conditions where SSRIs have been explored — no specific Dapoxetine migraine data |
| [23504864](https://pubmed.ncbi.nlm.nih.gov/23504864/) | 2013 | Observational / Compliance Study | Urologia | Evaluates patient adherence to Dapoxetine for premature ejaculation; confirms SSRI mechanism and tolerability profile — no migraine-related findings |

> **Note:** Neither publication provides direct evidence for Dapoxetine in migraine. PMID 33998993 discusses SSRIs as a class; PMID 23504864 addresses the approved indication. These represent indirect, class-level evidence only.

---

## India Market Information

Dapoxetine currently has **no registered products** in India. The drug is approved in several other markets (including Germany, Austria, Italy, Portugal, Finland, New Zealand, Argentina, Mexico, and the UK under the brand name **Priligy**), but has not received approval from the US FDA. A completed Phase 3 US trial ([NCT00211094](https://clinicaltrials.gov/ct2/results?term=NCT00211094)) did not lead to FDA approval.

---

## Safety Considerations

Package insert safety data (warnings and contraindications) for the Indian market is unavailable, as the drug is not registered locally. Based on available pharmacological data:

- **Mechanism-Based Interaction**: Dapoxetine inhibits SERT and therefore carries a risk of **serotonin syndrome** when combined with other serotonergic agents (other SSRIs, SNRIs, MAOIs, triptans, tramadol). This interaction is particularly relevant in the context of migraine treatment, where triptans — also serotonergic — are commonly used.
- **Class Effect**: As an SSRI, Dapoxetine shares class-level risks including nausea, dizziness, and syncope (especially orthostatic), which have been documented in its approved indication.

Please refer to the approved country-of-origin package insert (e.g., Priligy SmPC) for complete warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model correctly identifies the serotonergic mechanistic link between Dapoxetine and migraine, but a critical pharmacokinetic barrier — Dapoxetine's ultra-short half-life (~1.5 h) — makes it fundamentally unsuitable for the sustained 5-HT modulation required for migraine prevention. Furthermore, the drug is not marketed in India, there are zero supporting clinical trials, and the two retrieved publications provide only indirect, class-level evidence. The evidence base is insufficient and the mechanistic rationale is weak relative to longer-acting SSRIs already explored for migraine prophylaxis.

**To proceed (if reconsidered), the following would be needed:**

- **Pharmacokinetic feasibility assessment**: Modelling or in vitro data demonstrating whether any modified-release formulation of Dapoxetine could achieve sustained SERT occupancy relevant to migraine prevention
- **Mechanistic MOA data**: Full DrugBank / literature review of Dapoxetine's receptor binding profile beyond SERT (e.g., any 5-HT₁B/1D activity)
- **Comparative literature review**: Systematic comparison of Dapoxetine vs. long-acting SSRIs in serotonin-mediated migraine mechanisms
- **Safety interaction profiling**: Formal assessment of Dapoxetine + triptan co-administration risk (serotonin syndrome), given migraine patients often use triptans acutely
- **Regulatory pathway review**: If further evidence emerges, an analysis of the registration pathway in India (CDSCO) would be required
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

