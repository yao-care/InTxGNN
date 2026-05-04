---
layout: default
title: Dexketoprofen
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
---

# Dexketoprofen
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

# Dexketoprofen: From Acute Pain to Migraine Disorder

## One-Sentence Summary

Dexketoprofen is a potent NSAID (the S-enantiomer of ketoprofen) used globally for acute pain management, though it currently holds **no market authorization in India**.
This multi-indication TxGNN analysis identifies **migraine disorder** as the best-evidenced new indication, supported by **8 clinical trials** and **20 publications** — reaching **L1 evidence level**.
The highest TxGNN model score belongs to **tendinitis** (99.90%), where COX inhibition is mechanistically well-justified, though direct clinical evidence for dexketoprofen in that specific indication remains limited.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No India registration; globally used for acute pain (musculoskeletal, dental, dysmenorrhea) |
| Top TxGNN Predicted Indication | Tendinitis (TxGNN score: 99.90%, Rank #2446) |
| Best-Evidenced Predicted Indication | Migraine Disorder (8 clinical trials, 20 publications, L1) |
| TxGNN Prediction Score (Tendinitis) | 99.90% |
| Evidence Level | Migraine Disorder: **L1** / Tendinitis: L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Migraine Disorder: **Proceed with Guardrails** / Tendinitis: Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Dexketoprofen is the S-enantiomer of ketoprofen, belonging to the propionic acid class of NSAIDs. It works by inhibiting cyclooxygenase (COX-1 and COX-2) enzymes, blocking the conversion of arachidonic acid to prostaglandins (PGs) and thromboxanes — the key lipid mediators of pain and inflammation.

For **tendinitis** (top TxGNN rank), the mechanistic connection is highly plausible: tendinopathic tissue shows elevated PGE2, and COX inhibition directly reduces local prostaglandin concentrations, alleviating inflammatory pain and swelling. NSAIDs are already recognized as first-line agents for tendinitis. The gap here is not mechanistic plausibility, but specific clinical trial evidence for dexketoprofen in this exact indication — the available RCT covers non-traumatic musculoskeletal pain broadly, with tendinitis as one sub-cause.

For **migraine disorder** (best-evidenced prediction), the mechanistic rationale is well-established: prostaglandins — especially PGE2 — participate in the neuroinflammation and intracranial vasodilation that drive migraine attacks. COX inhibition → decreased PG synthesis → reduced sensitization of the trigeminovascular system → headache relief. This pathway is not theoretical: multiple completed RCTs conducted specifically in emergency departments have directly confirmed intravenous dexketoprofen's efficacy in aborting acute migraine attacks.

---

## Clinical Trial Evidence

### Migraine Disorder (Best-Evidenced Indication)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02159547](https://clinicaltrials.gov/study/NCT02159547) | Phase 4 | Completed | 224 | Double-blind placebo-controlled RCT: IV dexketoprofen vs. placebo for migraine attack in ED — primary superiority evidence |
| [NCT01730326](https://clinicaltrials.gov/study/NCT01730326) | Phase 4 | Completed | 200 | Head-to-head RCT: IV dexketoprofen vs. IV paracetamol for acute migraine attack in emergency service |
| [NCT04533568](https://clinicaltrials.gov/study/NCT04533568) | Phase 4 | Completed | 160 | RCT: IV dexketoprofen vs. IV ibuprofen for migraine-related headache in ED |
| [NCT04252521](https://clinicaltrials.gov/study/NCT04252521) | N/A | Completed | 150 | Double-blind RCT: IV metoclopramide vs. dexketoprofen vs. combination therapy for acute migraine in ED |
| [NCT04372264](https://clinicaltrials.gov/study/NCT04372264) | Phase 4 | Unknown | 210 | Three-arm RCT: IV dexketoprofen vs. ibuprofen vs. paracetamol — VAS reduction in acute migraine in ED |
| [NCT04519346](https://clinicaltrials.gov/study/NCT04519346) | N/A | Completed | 150 | RCT: intradermal mesotherapy vs. systemic therapy (including dexketoprofen) for migraine without aura |
| [NCT05780671](https://clinicaltrials.gov/study/NCT05780671) | N/A | Completed | 160 | RCT: supplemental oxygen vs. standard migraine therapy (50 mg dexketoprofen IV + metoclopramide) in ED |
| [NCT06061588](https://clinicaltrials.gov/study/NCT06061588) | N/A | Completed | 140 | VR technology for migraine headaches; dexketoprofen serves as standard background treatment in control arm |

### Tendinitis (Top TxGNN Score Indication)

Currently no registered clinical trials for Dexketoprofen specifically in tendinitis.

---

## Literature Evidence

### Migraine Disorder (Best-Evidenced Indication — Top 10 Publications)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Clinical Practice Guideline | Headache | 2025 AHS guideline update on parenteral pharmacotherapies for acute migraine in the ED — establishes clinical standards including NSAIDs |
| [31725614](https://pubmed.ncbi.nlm.nih.gov/31725614/) | 2019 | Meta-analysis of RCTs | Medicine | Meta-analysis: dexketoprofen significantly better than placebo for pain control in migraine attacks |
| [37291500](https://pubmed.ncbi.nlm.nih.gov/37291500/) | 2023 | Systematic Review / Meta-analysis | BMC Neurology | Network meta-analysis comparing metoclopramide and other anti-migraine drugs including dexketoprofen |
| [25944813](https://pubmed.ncbi.nlm.nih.gov/25944813/) | 2016 | RCT | Cephalalgia | Randomized placebo-controlled trial: IV dexketoprofen for aborting migraine attack in ED |
| [32359776](https://pubmed.ncbi.nlm.nih.gov/32359776/) | 2020 | RCT | Am J Emerg Med | Double-blind RCT: IV metoclopramide vs. dexketoprofen trometamol vs. combination for acute migraine in ED |
| [24394884](https://pubmed.ncbi.nlm.nih.gov/24394884/) | 2014 | RCT | Emerg Med J | RCT: IV paracetamol vs. dexketoprofen for acute migraine attack in ED — dexketoprofen compared favorably |
| [25056381](https://pubmed.ncbi.nlm.nih.gov/25056381/) | 2014 | RCT | Expert Rev Neurother | Efficacy and tolerability of frovatriptan and dexketoprofen as monotherapies for acute migraine |
| [24412801](https://pubmed.ncbi.nlm.nih.gov/24412801/) | 2014 | Phase II RCT | J Pain | Phase II crossover dose-optimization RCT: dexketoprofen trometamol 25 mg vs. 50 mg vs. placebo — primary endpoint pain-free at 2 h |
| [34085549](https://pubmed.ncbi.nlm.nih.gov/34085549/) | 2021 | RCT | Ann Saudi Med | RCT: intradermal mesotherapy vs. IV dexketoprofen for migraine headache without aura in ED |
| [24363238](https://pubmed.ncbi.nlm.nih.gov/24363238/) | 2014 | RCT | Cephalalgia | RCT: frovatriptan + dexketoprofen (25 or 37.5 mg) vs. frovatriptan alone for migraine with or without aura |

### Tendinitis (Available Literature)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30744914](https://pubmed.ncbi.nlm.nih.gov/30744914/) | 2019 | RCT | Am J Emerg Med | IV dexketoprofen vs. paracetamol in non-traumatic musculoskeletal pain in ED — covers tendinitis, muscle spasm, and joint injuries as a combined endpoint |

---

## India Market Information

Dexketoprofen currently has **no registered products in India**. No authorization records are available.

For reference, dexketoprofen trometamol is marketed in Europe (e.g., as **Keral®**, **Enantyum®**) and several other markets for acute pain management. A full CDSCO registration process would be required before any clinical deployment in India.

---

## Summary of All Predicted Indications

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation |
|------|-----------|------------|---------------|---------------|
| 1 | Tendinitis | 99.90% | L4 | Research Question |
| 2 | Fibromyalgia | 99.88% | L5 | Hold |
| 3 | Idiopathic Granulomatous Myositis | 99.88% | L5 | Hold |
| 4 | Myositis Fibrosa | 99.88% | L5 | Hold |
| 5 | Rheumatoid Arthritis | 99.88% | L5 | Hold |
| 6 | **Migraine Disorder** | 99.87% | **L1** | **Proceed with Guardrails** |
| 7 | **Headache Disorder** | 99.86% | **L1** | **Proceed with Guardrails** |
| 8 | Migraine with Brainstem Aura | 99.86% | L3 | Research Question |
| 9 | Exostosis | 99.85% | L5 | Hold |
| 10 | Congenital Hypotrichosis Milia | 99.83% | L5 | Hold |

**Notes on Hold indications:**
- **Fibromyalgia**: Central sensitization dominates; prostaglandins play a limited role; NSAIDs not recommended in current guidelines.
- **Idiopathic granulomatous myositis / Myositis fibrosa**: Rare inflammatory myopathies driven by T-cell granulomatous or fibrotic mechanisms; COX inhibition has no meaningful therapeutic impact.
- **Rheumatoid arthritis**: COX inhibition can reduce symptomatic pain and swelling (PGE2 is elevated in synovial fluid), but RA is an autoimmune disease requiring DMARDs/bDMARDs as backbone therapy; no direct dexketoprofen-specific clinical evidence.
- **Exostosis / Congenital hypotrichosis milia**: Knowledge graph artifacts — structural bone overgrowth and genetic skin disorders with no plausible COX-dependent mechanism.

---

## Safety Considerations

Please refer to the package insert for safety information. Full warnings and contraindications data are not available in this evidence pack.

As a general NSAID class note, the following should be reviewed before clinical use:
- **Gastrointestinal risk**: Risk of GI bleeding and ulceration, especially with prolonged use or in high-risk populations
- **Renal impairment**: NSAIDs can reduce renal prostaglandin synthesis; use with caution in patients with pre-existing renal dysfunction
- **Cardiovascular risk**: Standard NSAID cardiovascular precautions apply
- **Hypersensitivity**: Cross-reactivity risk in patients with aspirin/NSAID hypersensitivity or asthma

Drug-drug interaction data was not found in this evidence pack query.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (Migraine Disorder / Headache Disorder)**

**Rationale:**
Multiple completed Phase 4 RCTs — including a placebo-controlled trial (n=224) and a meta-analysis of RCTs — confirm IV dexketoprofen's efficacy in aborting acute migraine attacks in the emergency department. The COX inhibition → prostaglandin reduction → trigeminovascular desensitization mechanism is well-supported by both basic science and clinical data. Both migraine disorder and the broader headache disorder indication reach L1 evidence level.

**To proceed, the following is needed:**
- **Regulatory pathway**: Initiate CDSCO registration for dexketoprofen trometamol in India (currently no market authorization — a prerequisite for clinical use)
- **Safety documentation**: Retrieve full warnings and contraindications from the package insert (Blocking data gap DG001)
- **MOA verification**: Obtain detailed mechanism of action data from DrugBank (High severity data gap DG002)
- **DDI profile**: Clarify drug-drug interaction profile, especially for co-medications common in migraine management (antiemetics, triptans)
- **Formulation strategy**: IV route has the most evidence (emergency setting); evaluate oral formulation data for outpatient/self-management scenarios
- **Tendinitis pathway**: As the top TxGNN prediction, consider a focused literature review on dexketoprofen in musculoskeletal pain subtypes and assess feasibility of a clinical study specifically in tendinitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

