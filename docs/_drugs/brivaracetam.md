---
layout: default
title: Brivaracetam
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 10
---

# Brivaracetam
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

# Brivaracetam: From Focal Onset Seizures to Visual Epilepsy

## One-Sentence Summary

Brivaracetam (BRV) is a third-generation antiseizure medication internationally approved for focal onset seizures, acting as a high-affinity synaptic vesicle protein 2A (SV2A) ligand with significantly greater potency than its predecessor levetiracetam.
The TxGNN model predicts it may be effective for **Visual Epilepsy** (a subtype of reflex epilepsy triggered by visual stimuli),
with **0 registered clinical trials** and **19 publications** currently supporting this direction — including a Phase 2 RCT directly validating BRV in the photoparoxysmal response (PPR) model.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Focal onset seizures (international approval; not registered in India) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not available in the current dataset. However, based on extensive published literature, Brivaracetam is a propyl analogue of levetiracetam, engineered specifically to bind synaptic vesicle glycoprotein 2A (SV2A) with 15–30 times greater affinity and markedly faster blood-brain barrier penetration than levetiracetam. SV2A modulates synaptic vesicle exocytosis at inhibitory and excitatory synapses throughout the brain, and BRV's high-affinity binding is thought to dampen pathological hypersynchronous neuronal firing without significantly disrupting normal synaptic activity.

Visual epilepsy — most prominently manifested as photosensitive epilepsy with photoparoxysmal EEG response (PPR) — represents a reflex epilepsy subtype where visual cortex hyperexcitability is triggered by flickering or patterned visual stimuli. The occipital and parieto-occipital cortices, which are heavily involved in PPR propagation, are rich in SV2A-expressing synapses, providing a direct mechanistic substrate for BRV's predicted efficacy. Critically, a Phase 2 randomized, double-blind, crossover RCT (PMID 32949370) demonstrated that BRV suppresses PPR significantly faster and more completely than levetiracetam in photosensitive epilepsy patients, directly bridging the mechanistic hypothesis to clinical proof-of-concept.

While the broader literature corpus for this prediction consists largely of focal epilepsy management reviews rather than visual epilepsy-specific trials, the convergence of BRV's unique pharmacokinetic profile (rapid CNS penetration), established preclinical anti-convulsant activity across multiple seizure models, and direct Phase 2 PPR validation collectively support the TxGNN prediction as biologically well-founded. The absence of a dedicated Phase 3 trial for visual epilepsy reflects the rarity and diagnostic heterogeneity of the condition rather than a lack of mechanistic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Brivaracetam in visual epilepsy.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|------|
| [32949370](https://pubmed.ncbi.nlm.nih.gov/32949370/) | 2020 | Phase 2 RCT | CNS Drugs | Randomized crossover trial directly comparing BRV vs levetiracetam in photosensitive epilepsy patients; BRV eliminated PPR faster and more completely, providing direct proof-of-concept for visual/photosensitive epilepsy |
| [38576178](https://pubmed.ncbi.nlm.nih.gov/38576178/) | 2024 | Phase 3 RCT | Epilepsia Open | Phase 3 double-blind placebo-controlled trial of adjunctive BRV in adult Asian patients with focal-onset seizures; demonstrated efficacy and tolerability in Asian populations |
| [31195850](https://pubmed.ncbi.nlm.nih.gov/31195850/) | 2019 | Systematic Review / Meta-analysis | Expert Review of Neurotherapeutics | Comprehensive review of BRV efficacy and safety in focal epilepsy; covers racetam class pharmacology, clinical trial data, and post-marketing experience |
| [31937513](https://pubmed.ncbi.nlm.nih.gov/31937513/) | 2020 | Pooled Safety Analysis | Epilepsy & Behavior | In-depth pooled safety analysis of adjunctive BRV across clinical trials for focal seizures; provides comprehensive tolerability profile |
| [38811492](https://pubmed.ncbi.nlm.nih.gov/38811492/) | 2024 | Narrative Review | Advances in Therapy | Reviews BRV preclinical profile and clinical benefits; discusses SV2A mechanism, higher affinity vs levetiracetam, and broad epilepsy clinical evidence |
| [40568060](https://pubmed.ncbi.nlm.nih.gov/40568060/) | 2025 | Narrative Review | Journal of Epilepsy Research | Synthesizes clinical trial and real-world data on BRV pharmacology, efficacy, safety, and tolerability; emphasizes rapid brain penetration and SV2A selectivity |
| [38970892](https://pubmed.ncbi.nlm.nih.gov/38970892/) | 2024 | Prospective Observational | Epilepsy & Behavior | EXPERIENCE pooled analysis assessing BRV effectiveness and tolerability in older vs younger adults across Australia, Europe, and the US |
| [39664134](https://pubmed.ncbi.nlm.nih.gov/39664134/) | 2024 | Systematic Review | Cureus | Systematic review of BRV efficacy, safety, and reasons for switching from prior AEDs in adults and children with epilepsy |
| [37483441](https://pubmed.ncbi.nlm.nih.gov/37483441/) | 2023 | Systematic Review & Meta-analysis | Frontiers in Neurology | Systematic review and meta-analysis of BRV safety and efficacy specifically in childhood epilepsy |
| [32120063](https://pubmed.ncbi.nlm.nih.gov/32120063/) | 2020 | Mechanistic Review | Neuropharmacology | Comprehensive review of antiseizure drug mechanisms including SV2A pathway; contextualizes BRV's mechanism within the broader pharmacology of seizure suppression |

---

## India Market Information

Brivaracetam currently has **no registered products** in India. There are 0 approved licenses on record.

For reference, BRV has been approved internationally under the brand name **Briviact®** by the US FDA (2016) and EMA (2016) for adjunctive treatment of focal onset seizures in adults and adolescents aged ≥16 years. Intravenous formulation is also available internationally.

---

## Safety Considerations

**Drug Interactions** (69 total interactions identified; key interactions listed below):

| Interacting Drug | Severity | Clinical Note |
|------|------|------|
| Morphine | Moderate | CNS depressant combination; increased sedation risk |
| Morphine (liposomal) | Moderate | Same as morphine — enhanced CNS depression |
| Opium | Moderate | CNS depressant combination |
| Difenoxin | Moderate | CNS depressant combination |
| Diphenoxylate | Moderate | CNS depressant combination |
| Promethazine | Moderate | CNS depressant combination; additive sedation |
| Metoclopramide | Moderate | Potential pharmacodynamic interaction |
| Dronabinol | Moderate | CNS depressant combination |
| Nabilone | Moderate | CNS depressant combination |
| Sibutramine | Moderate | Serotonergic/CNS interaction risk |
| Clopidogrel | Moderate | Potential pharmacokinetic interaction |
| Ethanol | Moderate | Additive CNS depression; patients should be advised to avoid alcohol |

> Please refer to the package insert for complete warnings and contraindications. Key warning and contraindication data were not available in the current evidence pack and require retrieval from the prescribing information.

---

## All Predicted Indications — Summary Dashboard

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|----------------|----------------|
| 1 | Visual Epilepsy | 99.51% | L3 | Proceed with Guardrails |
| 2 | Status Epilepticus | 99.40% | L2 | Proceed with Guardrails |
| 3 | Thinking Seizures | 99.19% | L4 | Research Question |
| 4 | Micturation-induced Seizures | 99.19% | L4 | Research Question |
| 5 | Audiogenic Seizures | 99.19% | L3 | Research Question |
| 6 | Eating Seizures | 99.19% | L5 | Hold |
| 7 | Orgasm-induced Seizures | 99.19% | L5 | Hold |
| 8 | Startle Epilepsy | 99.19% | L5 | Research Question |
| 9 | Beta-ketothiolase Deficiency | 99.14% | L5 | Hold |
| 10 | ADPEAF (Auditory Features) | 99.10% | L5 | Research Question |

**Notable:** Rank 2 (Status Epilepticus) has the strongest clinical trial evidence — a completed head-to-head IV BRV vs IV levetiracetam trial in pediatric SE (NCT07163572, n=152). This may warrant a separate dedicated report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for visual epilepsy is mechanistically well-supported — BRV's high-affinity SV2A binding and rapid CNS penetration provide a compelling theoretical basis, and a Phase 2 RCT (PMID 32949370) has directly demonstrated BRV's superiority over levetiracetam in suppressing photoparoxysmal response in photosensitive epilepsy patients. However, the absence of a dedicated Phase 3 trial for visual epilepsy specifically (as opposed to broader focal epilepsy) limits the current evidence to L3.

**To proceed, the following is needed:**

- **MOA documentation**: Retrieve full mechanism of action from DrugBank API (Data Gap DG002) to support regulatory submission narrative
- **Safety package**: Download and parse prescribing information (package insert) to obtain key warnings and contraindications (Data Gap DG001 — currently Blocking for S1 safety screening)
- **India regulatory pathway**: Assess whether BRV's existing FDA/EMA approvals can support an abbreviated new drug application (ANDA) or import registration pathway in India, given zero current market presence
- **Phase 2/3 trial design**: If pursuing visual epilepsy as a new indication, consider a proof-of-concept study using the validated PPR model as a surrogate endpoint, following the precedent set by NCT (PPR suppression studies)
- **Status Epilepticus parallel track**: NCT07163572 results (IV BRV vs IV LEV in pediatric SE, n=152, completed) should be obtained and reviewed separately — this indication has L2 evidence and may offer a faster regulatory pathway given the unmet need and available IV formulation

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

