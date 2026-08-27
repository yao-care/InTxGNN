---
layout: default
title: Ketamine
parent: 僅模型預測 (L5)
nav_order: 359
evidence_level: L5
indication_count: 1
---

# Ketamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Ketamine: From Dissociative Anaesthesia to Headache Disorder

## One-Sentence Summary

Ketamine is a dissociative anaesthetic and analgesic broadly used for anaesthesia induction, procedural sedation, and acute pain management.
The TxGNN model predicts it may be effective for **Headache Disorder** (encompassing migraine, tension-type headache, and cluster headache),
with **at least 9 directly relevant clinical trials** and **4 headache-focused publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Dissociative anaesthesia / acute analgesia (no India regulatory data on file) |
| Predicted New Indication | Headache Disorder |
| TxGNN Prediction Score | 99.33% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, ketamine is an NMDA (N-methyl-D-aspartate) receptor antagonist that blocks glutamate-mediated neurotransmission in the central nervous system. By antagonising NMDA receptors, ketamine disrupts **central sensitisation** — a key pathophysiological mechanism underlying chronic and refractory pain states. This mechanism is well-characterised in the broader literature even though the formal MOA field is marked as a data gap in the current evidence package.

The pathophysiology of headache disorders — particularly migraine, chronic daily headache, and cluster headache — critically involves NMDA-mediated glutamate signalling within the **trigeminovascular system**, together with sustained sensitisation of the spinal trigeminal nucleus (trigeminal nucleus caudalis). Intravenous ketamine infusion can interrupt this sensitisation circuit, providing a direct mechanistic rationale for use in refractory headache. Importantly, sub-dissociative (low) doses that preserve consciousness while producing analgesia are already being evaluated in Emergency Department headache protocols, suggesting a clinically tractable dosing window.

The TxGNN knowledge graph model captured this biological overlap and ranked headache disorder at score 99.33%, consistent with a growing body of clinical literature exploring ketamine infusion as a treatment for migraine, tension-type headache, and cluster headache, particularly in refractory or acute-care settings.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | Unknown | 60 | RCT: sub-dissociative IV ketamine vs ketorolac for acute generalised tension-type headache in the ED; primary endpoint pain relief by NRS — most directly relevant Grade A evidence |
| [NCT02657031](https://clinicaltrials.gov/study/NCT02657031) | Phase 4 | Completed | 54 | CHECK Trial: multi-centre double-blind RCT comparing low-dose IV ketamine vs prochlorperazine (Compazine) for headache in the ED |
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Phase 3 | Completed | 80 | THINK Trial: single-blind RCT of sub-dissociative intranasal ketamine vs standard care for primary headache syndromes (migraine, tension-type) presenting to the ED |
| [NCT05306899](https://clinicaltrials.gov/study/NCT05306899) | Phase 3 | Recruiting | 56 | KetHead Study: multicentre placebo-controlled RCT of high-dose IV ketamine (1 mg/kg/h × 6 hours) vs placebo for chronic daily headache; completion expected June 2026 |
| [NCT04814381](https://clinicaltrials.gov/study/NCT04814381) | Phase 4 | Recruiting | 90 | RCT of single IV ketamine infusion combined with magnesium sulphate for drug-resistant chronic cluster headache; completion expected December 2026 |
| [NCT04179266](https://clinicaltrials.gov/study/NCT04179266) | Phase 1/2 | Completed | 23 | Proof-of-concept study of intranasal ketamine aqueous spray (100 µL/nostril) for treatment of refractory chronic cluster headache |
| [NCT06608277](https://clinicaltrials.gov/study/NCT06608277) | Phase 2 | Recruiting | 175 | Multi-centre double-blind RCT comparing IV ketamine, stellate ganglion block, and their combination vs sham for TBI-associated headache and PTSD |
| [NCT02697071](https://clinicaltrials.gov/study/NCT02697071) | N/A | Completed | 34 | Double-blind placebo-controlled RCT of sub-dissociative IV ketamine for acute migraine-type headache in the ED; assessed pain score reduction and 24-hour recurrence |
| [NCT04860713](https://clinicaltrials.gov/study/NCT04860713) | Phase 4 | Completed | 5 | Pilot open-label RCT comparing oral ketamine + aspirin vs rimegepant (CGRP antagonist) for acute headache in the ED; very small sample, exploratory grade only |
| [NCT06428838](https://clinicaltrials.gov/study/NCT06428838) | Phase 3 | Not Yet Recruiting | 102 | Eptinezumab as adjunct to standard care for acute migraine in the ED; no direct ketamine involvement, but provides contemporary comparative benchmark for novel ED headache treatments |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35356451](https://pubmed.ncbi.nlm.nih.gov/35356451/) | 2022 | Retrospective Cohort | Frontiers in Neurology | Retrospective cohort study of combined IV lidocaine and ketamine infusions for inpatient headache disorders; assessed efficacy, duration of response, and safety profile — most directly relevant publication |
| [34919214](https://pubmed.ncbi.nlm.nih.gov/34919214/) | 2022 | Review | Drugs | Comprehensive review of drug treatment for cluster headache, covering acute (oxygen, sumatriptan) and prophylactic therapies, with discussion of NMDA-targeting adjuvants for refractory cases |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Review of Neurotherapeutics | Update on pharmacotherapy for trigeminal neuralgia; identifies ketamine alongside CGRP blockers as a promising adjuvant or monotherapy option when first-line anticonvulsants (carbamazepine, oxcarbazepine) are insufficient |
| [37421541](https://pubmed.ncbi.nlm.nih.gov/37421541/) | 2023 | Review | Current Pain and Headache Reports | Evidence-based review of complex regional pain syndrome covering NMDA-receptor-mediated central sensitisation mechanisms that are mechanistically shared with refractory headache pathophysiology |
| [36260324](https://pubmed.ncbi.nlm.nih.gov/36260324/) | 2022 | Systematic Review & Meta-analysis | JAMA Psychiatry | Systematic review comparing ketamine vs ECT for major depressive episodes; provides cross-indication safety profiling relevant to broader ketamine use |
| [35416105](https://pubmed.ncbi.nlm.nih.gov/35416105/) | 2022 | Review | Expert Opinion on Drug Safety | Long-term safety review of racemic ketamine and esketamine across psychiatric indications, including abuse potential, cognitive effects, and urological toxicity — important for risk-benefit evaluation when extending to headache indications |

---

## India Market Information

No regulatory authorisations are currently registered in India for Ketamine (DB01221). The India market status is **Not Marketed** with **0** active licences on record. Any development programme targeting this indication would require a new regulatory submission.

---

## Safety Considerations

**Drug Interactions** (111 total interactions identified; selected clinically relevant examples shown below):

| Interacting Drug | Severity | Clinical Concern |
|------|------|------|
| Morphine | Moderate | Additive CNS and respiratory depression; common co-administration in acute pain settings requires monitoring |
| Morphine (liposomal) | Moderate | Same mechanism as morphine |
| Opium | Moderate | Additive CNS and respiratory depression |
| Diphenoxylate | Moderate | Opioid-containing antidiarrhoeal; additive CNS depression risk |
| Dronabinol | Moderate | Cannabinoid; additive CNS and psychomimetic effects |
| Nabilone | Moderate | Cannabinoid; additive psychomimetic and sedative effects |
| Ephedrine | Moderate | Sympathomimetic; risk of haemodynamic instability (hypertension, tachycardia) |
| Sibutramine | Moderate | Serotonergic component; potential for serotonin-related adverse effects |
| Phentermine | Moderate | Sympathomimetic; cardiovascular interaction risk |
| Metoclopramide | Moderate | Increased risk of CNS adverse effects with concurrent administration |

> Formal key warnings and contraindications were not available in this Evidence Pack. Please refer to the package insert and current prescribing information before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 3/4 clinical trials directly targeting headache disorders — including the completed THINK Trial (n=80, Phase 3) and CHECK Trial (n=54, Phase 4) alongside the actively recruiting KetHead Phase 3 study — demonstrate that IV and intranasal ketamine is a scientifically credible candidate for headache disorder treatment. The NMDA antagonism mechanism provides a coherent and published biological link to headache pathophysiology. However, Ketamine is not currently marketed in India, critical safety data (package insert warnings and contraindications) is absent from this Evidence Pack, and formal MOA confirmation is still pending.

**To proceed, the following is needed:**
- Retrieve and parse the full prescribing information (package insert PDF) from CDSCO or the originator to complete the safety screening (key warnings, contraindications)
- Confirm MOA details via DrugBank API query for DB01221
- Extract and summarise primary efficacy endpoint results from the completed THINK Trial (NCT03081416, n=80) and CHECK Trial (NCT02657031, n=54)
- Monitor KetHead Study (NCT05306899) Phase 3 results (expected June 2026) — successful completion would upgrade the evidence level to L2 or L1
- Assess regulatory pathway for India market entry and evaluate whether an import/clinical trial licence application is feasible
- Define route-of-administration strategy (IV infusion vs intranasal spray) appropriate for the target headache indication and clinical setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

