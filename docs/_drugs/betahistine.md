---
layout: default
title: Betahistine
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 10
---

# Betahistine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Betahistine: From Vestibular Vertigo to Restless Legs Syndrome

## One-Sentence Summary

Betahistine (DB06698) is a histamine analogue internationally established for Ménière's disease and vestibular vertigo, but currently has no registered products in India.
The TxGNN model ranks **Restless Legs Syndrome** as its highest-scoring predicted new indication (98.51%), though this prediction is currently unsupported by any clinical or preclinical evidence (L5).
More clinically actionable are the co-predicted vestibular indications—particularly **Active Vestibular Menière Disease** supported by **19 publications** and multiple Cochrane reviews at evidence level **L1**, and **Peripheral Vertigo** with **4 clinical trials** and **20 publications** at evidence level **L2**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in India; internationally used for Ménière's disease and vestibular vertigo (Serc®/Betaserc®) |
| TxGNN #1 Predicted Indication | Restless Legs Syndrome |
| TxGNN Prediction Score | 98.51% |
| Evidence Level (RLS — TxGNN #1) | L5 — model prediction only, no supporting data |
| Highest-Evidence Co-Prediction | Active Vestibular Menière Disease (L1) |
| India Market Status | ✗ Not Marketed |
| Number of India Registrations | 0 |
| Recommended Decision | Hold (RLS) / Proceed with Guardrails (Menière Disease, Peripheral Vertigo) |

---

## All Predicted Indications at a Glance

This is a multi-indication Evidence Pack (TW-DB06698-multi). All ten TxGNN predictions are summarised below.

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|----------------|----------------|
| 1 | Restless Legs Syndrome | 98.51% | L5 | Hold |
| 2 | Active Cochlear Menière Disease | 98.34% | L4 | Research Question |
| **3** | **Active Vestibular Menière Disease** | **98.34%** | **L1** | **Proceed with Guardrails** |
| 4 | Active Cochleovestibular Menière Disease | 98.34% | L4 | Research Question |
| 5 | Otosclerosis | 98.19% | L4 | Research Question |
| **6** | **Peripheral Vertigo** | **98.07%** | **L2** | **Proceed with Guardrails** |
| 7 | Age-Related Hearing Impairment | 97.93% | L5 | Hold |
| 8 | BPPV (Benign Paroxysmal Positional Vertigo) | 97.78% | L2 | Research Question |
| 9 | Autosomal Recessive Hyperinsulinism (Kir6.2) | 97.77% | L5 | Hold |
| 10 | Familial Hyperinsulinemic Hypoglycemia | 97.32% | L5 | Hold |

---

## Why is This Prediction Reasonable?

### Restless Legs Syndrome (TxGNN #1 Prediction)

Currently, detailed mechanism of action data is not available (DrugBank MOA data gap). Based on known pharmacology, betahistine is a weak histamine H1 receptor agonist and potent H3 receptor antagonist acting primarily on the vestibular and inner-ear histaminergic systems. The speculative mechanistic link to RLS runs as follows: H3 receptor antagonism in subcortical circuits may indirectly modulate dopaminergic tone in the basal ganglia—the core pathological axis in RLS (dopaminergic hypofunction in nigrostriatal pathways). However, this pathway is highly indirect and entirely unverified. The TxGNN model's high score most likely reflects indirect node-connectivity between RLS, dopamine, and histamine in the knowledge graph, rather than a direct pharmacological relationship. No clinical trial registrations or published literature support this prediction.

### Active Vestibular Menière Disease and Peripheral Vertigo (Highest-Evidence Predictions)

Betahistine's dual mechanism provides a well-grounded biological rationale for vestibular indications. H3 receptor antagonism increases endogenous histamine release at vestibular nuclei, suppressing pathological hyperexcitability and actively accelerating vestibular compensation after damage. Simultaneously, H1 receptor agonism improves endolymphatic sac perfusion and reduces endolymphatic hydrops—the structural lesion underlying Ménière's disease. Together, these actions address both episodic vertigo attacks and the longer-term compensatory recovery process.

Ménière's disease and peripheral vertigo (encompassing BPPV, vestibular neuronitis, and Ménière's disease) share the common feature of disrupted vestibular signalling, meaning betahistine's mechanisms are applicable across this clinical spectrum. More than 20 controlled clinical studies spanning four decades—including the landmark Phase 3 BEMED trial (BMJ, 2016), two Cochrane systematic reviews, a 12-study meta-analysis, and the European Academy of Otology and Neurotology's 2018 Position Statement—confirm betahistine's efficacy in reducing vertigo attack frequency, severity, and duration. Because betahistine has no current registration in India, all of these internationally validated vestibular indications represent genuine first-entry opportunities in a market where treatment options for these prevalent conditions are limited.

---

## Clinical Trial Evidence

> **Note:** The top TxGNN prediction (Restless Legs Syndrome) has no registered clinical trials. The following trials are drawn from the highest-evidence co-predictions (peripheral vertigo and BPPV).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03908567](https://clinicaltrials.gov/study/NCT03908567) | Phase 2 | Completed | 124 | TRAVERS trial: AM-125 (betahistine dihydrochloride nasal spray) vs placebo for acute peripheral vertigo after neurosurgery (vestibular schwannoma labyrinthectomy / vestibular neurectomy); proof-of-concept confirming betahistine safety and preliminary efficacy in acute vestibular loss |
| [NCT07075289](https://clinicaltrials.gov/study/NCT07075289) | Phase 4 | Completed | 44 | Direct head-to-head comparison of betahistine mesylate vs lumbrokinase DLBS1033 in BPPV; primary endpoints include IL-1β inflammatory marker reduction, quality of life, and symptom resolution |
| [NCT01759251](https://clinicaltrials.gov/study/NCT01759251) | Post-marketing (N/A) | Completed | 309 | International post-marketing observational study of Betaserc® (betahistine dihydrochloride) for vestibular vertigo in real-world clinical practice across Russia and Ukraine; assesses effectiveness and disease course after treatment discontinuation |
| [NCT05127694](https://clinicaltrials.gov/study/NCT05127694) | N/A | Completed | 30 | Comparison of pharmacological treatment (including betahistine) vs vestibular rehabilitation in acute BPPV; examines the role of betahistine within standard care pathway for BPPV management |

---

## Literature Evidence

> **Note:** The top TxGNN prediction (Restless Legs Syndrome) has no published literature. The following publications are from the best-evidenced co-predictions (active vestibular Menière disease and peripheral vertigo). Priority order: RCT / Meta-analysis > Systematic Review > Clinical Guideline > Review.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [26797774](https://pubmed.ncbi.nlm.nih.gov/26797774/) | 2016 | Phase 3 RCT (BEMED) | BMJ | Long-term multicentre double-blind RCT of betahistine dihydrochloride vs placebo in Menière's disease; primary endpoint on vertigo attack incidence; landmark Phase 3 trial for this drug class |
| [23778722](https://pubmed.ncbi.nlm.nih.gov/23778722/) | 2014 | Meta-analysis | Eur Arch Otorhinolaryngol | Meta-analysis of 12 double-blind, randomised, placebo-controlled trials (published and unpublished data) of betahistine in Ménière's disease and vestibular vertigo; odds ratio for favourable treatment outcome significantly favours betahistine |
| [40070497](https://pubmed.ncbi.nlm.nih.gov/40070497/) | 2025 | Systematic Review / Meta-analysis | World J Otorhinolaryngol Head Neck Surg | Betahistine as add-on to Epley manoeuvre for BPPV; PRISMA-compliant meta-analysis evaluating reduction of residual dizziness after successful canalith repositioning |
| [36827524](https://pubmed.ncbi.nlm.nih.gov/36827524/) | 2023 | Cochrane Systematic Review | Cochrane Database Syst Rev | Comprehensive systematic review of systemic pharmacological interventions for Ménière's disease including betahistine, diuretics, antiviral agents, and corticosteroids; current best-evidence synthesis |
| [27327415](https://pubmed.ncbi.nlm.nih.gov/27327415/) | 2016 | Cochrane Systematic Review | Cochrane Database Syst Rev | Betahistine for vertigo symptoms across multiple aetiologies; examines whether betahistine is superior to placebo in improving inner-ear blood flow and reducing vertigo |
| [30256205](https://pubmed.ncbi.nlm.nih.gov/30256205/) | 2018 | Clinical Guideline | J Int Adv Otology | European Academy of Otology and Neurotology Position Statement on Diagnosis and Treatment of Menière's Disease; betahistine recognised as standard first-line pharmacological management |
| [22365373](https://pubmed.ncbi.nlm.nih.gov/22365373/) | 2012 | RCT | J Laryngol Otol | Randomised placebo-controlled double-blind trial of Meniett low-pressure device in unilateral Menière's disease unresponsive to betahistine; validates betahistine as established first-line standard before escalation to procedural therapy |
| [26245698](https://pubmed.ncbi.nlm.nih.gov/26245698/) | 2015 | Clinical Review | Acta Otolaryngol | Review and meta-analyses demonstrating betahistine is effective and safe for Ménière's disease, BPPV, vestibular neuronitis, and other peripheral vertigo types |
| [16116833](https://pubmed.ncbi.nlm.nih.gov/16116833/) | 2005 | RCT | Acta Otorhinolaryngol Ital | Prospective RCT in 103 BPPV patients comparing liberatory manoeuvre and gradual otolith dispersion technique with and without adjunct betahistine; evaluates whether betahistine adds benefit to repositioning manoeuvres |
| [7113814](https://pubmed.ncbi.nlm.nih.gov/7113814/) | 1982 | Long-term Clinical Trial | Adv Otorhinolaryngol | 12–14 year continuous treatment evaluation with betahistine HCl in Ménière's disease; >80% success rate with no habituation observed over the extended treatment period |

---

## India Market Information

Betahistine currently has **no registered pharmaceutical products in India**. No CDSCO authorisation numbers are on record, and the drug is not available on the Indian market.

---

## Safety Considerations

Complete India-specific safety data (package insert warnings, contraindications, drug interaction profile) are not available in this Evidence Pack.

Based on international clinical studies referenced above:
- The BEMED Phase 3 RCT and multiple large post-marketing studies (including N=309 real-world cohort) reported a generally favourable safety profile with no serious safety signals
- The 12–14 year long-term treatment study demonstrated no significant long-term adverse effects and no therapeutic habituation
- Internationally recognised precautions include: caution in patients with bronchial asthma or history of peptic ulcer disease (due to H1 agonist activity); contraindicated in pheochromocytoma

Please refer to the international package inserts (Serc®/Betaserc®, Solvay Pharmaceuticals) and consult CDSCO requirements for India registration safety documentation.

---

## Conclusion and Next Steps

**Decision: Stratified by Indication**

---

### Active Vestibular Menière Disease and Peripheral Vertigo — ✅ Proceed with Guardrails

**Rationale:**
Betahistine holds one of the strongest evidence profiles among vestibular pharmacotherapies: L1 evidence for vestibular Menière's disease (Cochrane reviews, Phase 3 RCT, European clinical guideline) and L2 evidence for peripheral vertigo (Phase 2 and Phase 4 RCTs, 12-study meta-analysis). This is an internationally established standard-of-care drug without any India registration, representing a clear and actionable unmet need.

**To proceed, the following is needed:**
- CDSCO New Drug Application (NDA) filing with reference to international registrations (EU, Japan, South Korea, etc.)
- India-specific package insert with locally validated warnings and contraindications (currently a blocking data gap)
- Full MOA data retrieval from DrugBank API (currently [Data Gap] — affects mechanistic dossier completeness)
- Dedicated drug interaction database query (DDI returned no results and requires a targeted search)
- India post-marketing surveillance plan and pharmacovigilance protocol

---

### Restless Legs Syndrome (TxGNN #1) — ⏸ Hold

**Rationale:**
Despite being the highest TxGNN-scoring prediction, RLS has zero supporting clinical or preclinical evidence. The mechanistic link depends on highly speculative indirect histamine-dopamine pathway interactions. This indication should not be actively pursued until basic mechanistic data is generated.

**To proceed, the following is needed:**
- Preclinical in vitro/in vivo studies examining betahistine's effect on nigrostriatal dopaminergic tone
- Retrospective chart review for RLS symptom occurrence in patients receiving betahistine for vestibular indications
- Mechanistic studies on H3 receptor antagonism effects on dopamine release in basal ganglia circuits

---

### Cochlear Menière Disease, Cochleovestibular Menière Disease, and Otosclerosis (L4) — 🔬 Research Question

**Rationale:**
These inner-ear conditions share the same pathological substrate as vestibular Menière's disease (endolymphatic dysfunction, cochlear microvascular insufficiency), making betahistine mechanistically plausible. Current evidence, however, is limited to two mechanistic/preclinical publications. These can most efficiently be addressed as secondary endpoints in Menière's disease registration studies.

**To proceed, the following is needed:**
- Clinical trial design incorporating cochlear Menière's and cochleovestibular Menière's as pre-specified subgroups alongside audiological outcome measures
- Dedicated search in cochlear Menière's-specific trial registries (ICTRP, EU CTR)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

