---
layout: default
title: Acetylcysteine
parent: High Evidence (L1-L2)
nav_order: 21
evidence_level: L1
indication_count: 10
---

# Acetylcysteine
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

# Acetylcysteine: From Bronchitis and Paracetamol Poisoning to Thrombotic Disease

## One-Sentence Summary

Acetylcysteine is a mucolytic and antidote, originally used for bronchitis, paracetamol poisoning, cystic fibrosis and bronchiectasis.
The TxGNN model predicts it may be effective for **thrombotic disease** (most plausibly transplant-associated thrombotic microangiopathy and thrombotic thrombocytopenic purpura),
with **7 clinical trials** and **20 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bronchitis, paracetamol poisoning, cystic fibrosis, bronchiectasis (the approved indication text in the India licences is blank, so these come from the knowledge-graph indication list) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 (see note in the Clinical Trial Evidence section) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

No detailed mechanism-of-action data is available in the compiled data. Based on known information, acetylcysteine is a thiol-based reducing agent with antioxidant activity. It is established as a mucolytic and as an antidote for paracetamol poisoning.

Its thiol group can reduce disulfide bonds in von Willebrand factor (VWF), shrinking VWF multimers and reducing their platelet-binding activity. This is plausible for VWF-driven microvascular thrombosis, such as thrombotic thrombocytopenic purpura (TTP) and transplant-associated thrombotic microangiopathy (TA-TMA). Its antioxidant action may also reduce oxidative endothelial injury and platelet activation.

Preclinical mouse and baboon models of TTP support this mechanism. The evidence is strongest for the thrombotic microangiopathy / TTP subset, not for thrombosis in general. The link to the original respiratory and antidote uses is therefore pharmacological (thiol and antioxidant chemistry) rather than a shared disease area.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Phase 3 | Completed | 170 | Safety and efficacy of NAC in transplant-associated thrombotic microangiopathy. Results should be verified. |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Phase 2/3 | Active, not recruiting | 44 | Single-arm trial of NAC for TA-TMA. Results not yet available. |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Phase 2 | Completed | 40 | Randomized, double-blind, placebo-controlled crossover trial (RENACTIF) of NAC on the thrombotic phenotype in renal insufficiency. |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Early Phase 1 | Completed | 3 | Pilot of IV NAC with plasma exchange in suspected TTP. Too small for efficacy conclusions. |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Phase 2 | Unknown | 44 | High-dose dexamethasone plus NAC in newly diagnosed immune thrombocytopenia. Indirect relevance. |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Phase 1/2 | Unknown | 200 | Atorvastatin, NAC and danazol in steroid-resistant or relapsed ITP. Combination, indirect. |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Early Phase 1 | Completed | 15 | Atorvastatin plus NAC on platelet count in ITP. Combination, indirect. |

Note: the only Phase 3 trial is a single study with unverified results, and the 2022 randomized trial below addresses prevention, not treatment. The L1 label comes from the pre-computed scoring, and the evidence is arguably closer to L2.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35940529](https://pubmed.ncbi.nlm.nih.gov/35940529/) | 2022 | RCT | Transplantation and Cellular Therapy | Randomized, placebo-controlled trial of NAC as prophylaxis for TA-TMA after stem cell transplantation |
| [41977015](https://pubmed.ncbi.nlm.nih.gov/41977015/) | 2026 | Systematic review | Journal of Clinical Medicine | Systematic review and critical appraisal of NAC in TTP |
| [42338865](https://pubmed.ncbi.nlm.nih.gov/42338865/) | 2026 | Systematic review | Cureus | Systematic review of NAC as adjunctive therapy in TTP |
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | Cohort | Annals of Hematology | Retrospective cohort examining NAC and in-hospital mortality in acquired TTP |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | Preclinical | Blood | NAC in mouse and baboon TTP models |
| [32243196](https://pubmed.ncbi.nlm.nih.gov/32243196/) | 2020 | Review | Expert Review of Hematology | Repurposed drugs for TTP, including NAC |
| [28416507](https://pubmed.ncbi.nlm.nih.gov/28416507/) | 2017 | Review | Blood | Overview of TTP pathophysiology and management |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Review | Journal of Clinical Medicine | TTP pathophysiology, diagnosis and management |
| [36410267](https://pubmed.ncbi.nlm.nih.gov/36410267/) | 2022 | Review | Journal of Infection and Public Health | NAC in COVID-19, which involves a prothrombotic state |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 234623 | Vexanac 600 Tablet | Strip of 10 tablets | Not stated |
| 134850 | Mucyst 600mg Tablet | Strip of 10 tablets | Not stated |
| 87042 | Fluimucil Eff 600mg Tablet | Strip of 6 tablets | Not stated |
| 151932 | Nacomac 600mg Effervescent Tablet | Strip of 10 effervescent tablets | Not stated |
| 153551 | Nacel 1000mg Injection | Vial of 5 ml injection | Not stated |

There are 20 valid single-ingredient registrations in total, covering oral tablets, effervescent tablets and injectables. The injectable forms are relevant to the intravenous use studied in TTP.

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: peptic ulcer disease, hypotensive disorder, respiratory failure, asthma, bronchial disease, esophageal varices.
- **Drug Interactions**: 247 interactions were recorded. Named examples include activated charcoal (minor) and inhaled rapid-acting human insulin (moderate). Many others, such as mannitol, bupropion, metformin, omeprazole, pantoprazole, morphine and prednisone, have an unclassified severity.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 trial, a randomized prophylaxis trial, systematic reviews, and preclinical models support a plausible mechanism in TA-TMA and TTP. The evidence is narrow in scope and the results are not verified, so the decision applies only to this thrombotic microangiopathy subset, not thrombotic disease broadly.

**To proceed, the following is needed:**
- Verified results for NCT03252925 and the outcome of NCT07279610
- Package insert warnings and contraindications for the Indian products (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Safety review of the knowledge-graph contraindications (asthma, respiratory failure, hypotension, peptic ulcer, esophageal varices) for the intended patients
- Confirmation of the intravenous route and dosing for the target indication
- Approved indication text for the Indian licences

### Other Predicted Indications (for reference)

| Indication | Evidence Level | Decision | Comment |
|------|------|------|------|
| Dry eye syndrome | L1 | Proceed with Guardrails | Randomized trials in Sjögren's dryness and chitosan-NAC drops. Much of the evidence is for the conjugate eye-drop formulation, not plain acetylcysteine, and no topical ophthalmic product appears in the India licences. |
| Tracheal disease | L4 | Research question | Preclinical and in vitro evidence only |
| Nasal cavity disease, pharyngitis, transient ischemic attack | L4 | Hold | Tangential literature, no trials |
| Closed-angle glaucoma, angle-closure glaucoma (duplicates), acute laryngopharyngitis, laryngotracheitis | L5 | Hold | Model prediction only |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

