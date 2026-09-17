---
layout: default
title: Streptokinase
parent: High Evidence (L1-L2)
nav_order: 784
evidence_level: L1
indication_count: 10
---

# Streptokinase
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Streptokinase: From Thrombolytic Therapy to Myocardial Infarction

## One-Sentence Summary

Streptokinase is a bacterial fibrinolytic enzyme historically used to dissolve blood clots in acute thromboembolic disease. The TxGNN model's top prediction is **Myocardial Infarction** — but this is actually streptokinase's classic, already-established indication rather than a novel repurposing target, and it is supported by **34 clinical trials** and **20 publications**, including multiple landmark Phase 3 RCTs from the 1970s–1990s.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not documented in this evidence pack (data gap); globally, streptokinase is classically used as a thrombolytic for acute MI, deep vein thrombosis, pulmonary embolism, and arterial/graft occlusion |
| Predicted New Indication | Myocardial Infarction — **Note: this is the drug's long-established core indication, confirmed rather than newly discovered by the model (see rationale below)** |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L1 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the structured record (flagged as a High-severity data gap, DG002). Based on well-established pharmacology, streptokinase is a bacterial-derived plasminogen activator: it forms a 1:1 complex with plasminogen, converting it to plasmin, which then degrades fibrin and dissolves intravascular thrombi. This is the same mechanism underlying its decades-long use as a fibrinolytic agent in acute coronary thrombosis.

Critically, the model's top-ranked "new" indication — myocardial infarction — is **not actually a novel repurposing candidate**. As the evidence pack's own rationale states, this is "the most classic and clinically established mechanism of thrombolytic agents... not a strict repurposing case but the original core indication." Streptokinase was one of the first agents ever proven, in large RCTs (ISIS/European Working Party, GISSI-era trials, TIMI, GUSTO), to reduce mortality when given early in acute MI. TxGNN essentially re-derived a well-known clinical fact from the knowledge graph rather than surfacing new therapeutic territory.

The mechanistic rationale is nonetheless sound and directly supports **coronary thrombosis** (rank 4, also L1/Proceed with Guardrails) as the closest true pathophysiological correlate — coronary thrombus is the direct anatomical substrate of MI, and plasminogen activation directly resolves it. Genuinely exploratory candidates with weaker but non-trivial support include peripheral vascular disease (L2) and peripheral arterial disease (L3), reflecting the same fibrinolytic mechanism applied to non-coronary arterial thrombosis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000507](https://clinicaltrials.gov/study/NCT00000507) | Phase 3 | Completed | N/A | Landmark NIH trial testing whether early IV streptokinase limits myocardial damage in acute transmural MI |
| [NCT00000505](https://clinicaltrials.gov/study/NCT00000505) | Phase 3 | Completed | N/A | TIMI I/II: compared streptokinase vs rt-PA thrombolytic activity and side effects in AMI; TIMI II assessed follow-on PTCA strategy |
| [NCT00000503](https://clinicaltrials.gov/study/NCT00000503) | Phase 3 | Completed | N/A | Assessed effect of non-surgical (intracoronary) reperfusion on infarct size in AMI |
| [NCT00245648](https://clinicaltrials.gov/study/NCT00245648) | Phase 3 | Completed | N/A | GUSTO-V: evaluated sex differences in presentation, management, and outcomes of fibrinolytic-treated AMI patients (streptokinase/tPA) |
| [NCT02182011](https://clinicaltrials.gov/study/NCT02182011) | Phase 3 | Completed | 49 | Open-label RCT comparing procoagulant effect (TAT levels) of tenecteplase, alteplase, and streptokinase in AMI |
| [NCT01305226](https://clinicaltrials.gov/study/NCT01305226) | Phase 3 | Completed | 120 | RCT of recombinant staphylokinase (THR-100) vs streptokinase in AMI |
| [NCT00302419](https://clinicaltrials.gov/study/NCT00302419) | Phase 4 | Completed | 95 | Complementary intracoronary streptokinase after primary PCI improved microvascular perfusion and late infarct size |
| [NCT00627809](https://clinicaltrials.gov/study/NCT00627809) | Phase 4 | Completed | 53 | Low-dose intracoronary streptokinase adjunct to primary PCI evaluated for effect on LV infarct size/volumes |
| [NCT00968929](https://clinicaltrials.gov/study/NCT00968929) | Phase 4 | Completed | 83 | RCT comparing recombinant streptokinase vs urokinase for pulmonary embolism in China |
| [NCT00526474](https://clinicaltrials.gov/study/NCT00526474) | Phase 3 | Completed | 26,449 | Large placebo-controlled trial (TRA 2°P-TIMI 50) in atherothrombotic disease, providing broader safety context for thrombolytic/antithrombotic strategies in MI prevention |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8028463](https://pubmed.ncbi.nlm.nih.gov/8028463/) | 1994 | Meta-analysis | Medical Decision Making | Combined meta-analysis/decision analysis on how infarct location and likelihood of AMI affect cost-effectiveness of IV streptokinase |
| [2868343](https://pubmed.ncbi.nlm.nih.gov/2868343/) | 1986 | RCT | Lancet | Landmark trial establishing efficacy of streptokinase in acute myocardial infarction |
| [2888018](https://pubmed.ncbi.nlm.nih.gov/2888018/) | 1987 | RCT | New England Journal of Medicine | Double-blind trial (n=219) of streptokinase vs placebo within 4 hours of MI onset; improved LV function and early survival |
| [4934187](https://pubmed.ncbi.nlm.nih.gov/4934187/) | 1971 | RCT | British Medical Journal | European Working Party controlled multicentre trial (n=730) of streptokinase vs heparin in recent MI |
| [481511](https://pubmed.ncbi.nlm.nih.gov/481511/) | 1979 | RCT | New England Journal of Medicine | 11-center European trial (n=2,338); streptokinase infusion significantly reduced 6-month mortality vs glucose control |
| [8005961](https://pubmed.ncbi.nlm.nih.gov/8005961/) | 1993 | Review | J Assoc Physicians India | Review of streptokinase use in acute myocardial infarction |
| [3312370](https://pubmed.ncbi.nlm.nih.gov/3312370/) | 1987 | Review | J Am Coll Cardiol | Review of randomized trials of intracoronary and IV streptokinase for AMI treatment |
| [21070617](https://pubmed.ncbi.nlm.nih.gov/21070617/) | 2012 | Review | Cardiovascular Therapeutics | Review of thrombolytics for MI; traces streptokinase's discovery through to newer plasminogen activators |
| [3815914](https://pubmed.ncbi.nlm.nih.gov/3815914/) | 1987 | Case Report | Clinical Cardiology | Case of sequential inferolateral and anterior MI occurring during apparently successful streptokinase therapy |
| [3139173](https://pubmed.ncbi.nlm.nih.gov/3139173/) | 1988 | Commentary | BMJ | Editorial reflecting on streptokinase thrombolysis as a milestone in MI treatment |

---

## India Market Information

Streptokinase is currently **Not Marketed** in India per this evidence pack (0 registrations found). No authorization records, product names, or approved indication text are available.

---

## Safety Considerations

**Drug Interactions** (122 total documented; selected major/moderate examples):

- **Major risk (bleeding potentiation)**: Apixaban, Betrixaban, Bivalirudin, Abciximab, Acalabrutinib, Avapritinib, Deferasirox, Ibritumomab tiuxetan, Tositumomab (I-131)
- **Moderate risk (additive bleeding/antiplatelet effect)**: Acetylsalicylic acid, Ibuprofen, Ketorolac (oral and ophthalmic), Celecoxib, Diclofenac (topical), Fenfluramine, Sibutramine, Aminocaproic acid, Omega-3 fatty acids, Ginger

Streptokinase's fibrinolytic mechanism means concurrent use of anticoagulants, antiplatelet agents, GPIIb/IIIa inhibitors, or NSAIDs meaningfully raises hemorrhagic risk and should be managed with close clinical monitoring.

> **Note**: TFDA/India-specific package insert warnings and contraindications are not available in this evidence pack (Blocking data gap, DG001) and must be obtained before any formal safety sign-off.

---

## Additional Candidate Indications (Not Detailed Above)

For completeness, given this evidence pack evaluated 10 candidate indications, a brief summary of the others:

| Rank | Indication | Evidence Level | Decision | Note |
|------|-----------|----------------|----------|------|
| 4 | Coronary thrombosis | L1 | Proceed with Guardrails | Direct anatomical substrate of MI; strongest mechanistic overlap |
| 8 | Peripheral vascular disease | L2 | Research Question | Same fibrinolytic mechanism, weaker/older evidence base (Cochrane review favors newer agents) |
| 9 | Peripheral arterial disease | L3 | Research Question | Shares trial evidence with PVD; no dedicated literature |
| 5 | Septal myocardial infarction | L4 | Hold | Anatomic MI subtype; literature concerns re: hemorrhagic MI association |
| 7 | Posterolateral myocardial infarction | L4 | Hold | Anatomic MI subtype; only indirect/case-level evidence |
| 2 | Prinzmetal angina | L4 | Hold | Pathology is vasospasm, not thrombosis — weak mechanistic fit |
| 6 | Posteroinferior myocardial infarction | L5 | Hold | No supporting trials or literature |
| 3 | Hemoglobinopathy | L5 | Hold | Single 1954 case report on topical enzymatic debridement; not a systemic thrombolytic use case |
| 10 | Chromosome 16p deletion | L5 | Hold | No plausible biological link; likely knowledge-graph noise |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The core MI indication is backed by decades of Level-1 RCT evidence and is pharmacologically well-established, but a Blocking data gap (missing India-specific label warnings/contraindications, DG001) prevents completion of the S1 safety review, and the drug is currently unregistered in India.

**To proceed, the following is needed:**
- TFDA/India package insert PDF retrieval and parsing for warnings and contraindications (DG001, Blocking)
- Formal MOA documentation via DrugBank API query (DG002, High)
- Clarification of intended repurposing target — if the goal is genuine "new use" discovery rather than confirming the known MI indication, prioritize coronary thrombosis, peripheral vascular disease, or peripheral arterial disease for further evaluation
- India-market entry pathway assessment given current "Not Marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

