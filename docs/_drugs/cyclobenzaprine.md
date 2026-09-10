---
layout: default
title: Cyclobenzaprine
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 3
---

# Cyclobenzaprine
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

# Cyclobenzaprine: From Muscle Spasm to Myofascial Pain Syndrome

## One-Sentence Summary

> Cyclobenzaprine is a centrally-acting skeletal muscle relaxant, best known for treating muscle spasm associated with acute, painful musculoskeletal conditions.
> The TxGNN model predicts it may be effective for **Myofascial Pain Syndrome**,
> with **17 clinical trials** and **5 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Muscle spasm associated with acute, painful musculoskeletal conditions (no formal Taiwan license text on file — see note below) |
| Predicted New Indication | Myofascial Pain Syndrome |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

*Note: `taiwan_regulatory.licenses` is empty (drug not marketed in Taiwan), so the original-indication text above is drawn from context within the evidence pack itself (trial NCT01041495 describes cyclobenzaprine as "approved by the FDA as a muscle relaxant, indicated for the treatment of muscle spasm associated with acute, painful musculoskeletal conditions"), not from a local label.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available from DrugBank for this candidate [Data Gap: DG002]. Based on known pharmacology, cyclobenzaprine is structurally related to the tricyclic antidepressants and acts at the brainstem level to reduce tonic somatic motor activity, thereby dampening excessive muscle activation — the core mechanism underlying its established use for muscle spasm.

Myofascial Pain Syndrome (MPS) is pathophysiologically characterized by localized muscle spasm and hyperexcitable trigger points. This overlaps substantially with the mechanism already validated in cyclobenzaprine's original indication, making the TxGNN prediction a mechanistic extension of existing pharmacology rather than a novel, unrelated hypothesis.

Several of the retrieved trials directly test cyclobenzaprine (or its sublingual formulation, TNX-102 SL) in related muscle-pain conditions — fibromyalgia, jaw/myofascial pain, and acute myofascial strain — reinforcing that the predicted indication sits within the drug's known pharmacological territory rather than being a speculative leap.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04704297](https://clinicaltrials.gov/study/NCT04704297) | Phase 4 | Recruiting | 180 | Trigger point injection RCT for low-back myofascial pain syndrome — most directly disease-matched trial, though cyclobenzaprine's role as a comparator/adjunct vs. the injection technique itself is not fully specified |
| [NCT00635037](https://clinicaltrials.gov/study/NCT00635037) | N/A | Completed | 30 | Acupuncture vs. trigger point injection combined with bupivacaine + cyclobenzaprine + dipyrone for myofascial pain relief |
| [NCT01041495](https://clinicaltrials.gov/study/NCT01041495) | Phase 4 | Terminated | 37 | Cyclobenzaprine ER (Amrix) augmentation for fibromyalgia-related fatigue and muscle pain; terminated early, small sample |
| [NCT02015234](https://clinicaltrials.gov/study/NCT02015234) | Phase 3 | Completed | 158 | 12-month open-label extension of TNX-102 SL (sublingual cyclobenzaprine) long-term safety in fibromyalgia |
| [NCT01903265](https://clinicaltrials.gov/study/NCT01903265) | Phase 2/3 | Completed | 205 | Double-blind RCT of TNX-102 SL 2.8 mg for fibromyalgia efficacy and safety |
| [NCT02436096](https://clinicaltrials.gov/study/NCT02436096) | Phase 3 | Completed | 519 | Double-blind, placebo-controlled RCT of TNX-102 SL for fibromyalgia (AtEase program) |
| [NCT05273749](https://clinicaltrials.gov/study/NCT05273749) | Phase 3 | Completed | 457 | Double-blind, placebo-controlled RCT of TNX-102 SL 5.6 mg for fibromyalgia (RELIEF program) |
| [NCT04172831](https://clinicaltrials.gov/study/NCT04172831) | Phase 3 | Completed | 503 | Double-blind, placebo-controlled RCT of TNX-102 SL 5.6 mg for fibromyalgia |
| [NCT01921296](https://clinicaltrials.gov/study/NCT01921296) | Phase 2 | Terminated | 2 | Pilot study of cyclobenzaprine for sleep disturbance/fatigue/musculoskeletal symptoms in aromatase-inhibitor-treated breast cancer patients; terminated at n=2 |
| [NCT01634412](https://clinicaltrials.gov/study/NCT01634412) | Phase 1 | Completed | 24 | PK comparison of sublingual TNX-102, oral, and IV cyclobenzaprine in healthy adults (formulation study, not efficacy) |

*Note: Most Phase 3 trials above are for fibromyalgia (a related but distinct diffuse muscle-pain condition using the TNX-102 SL formulation), not myofascial pain syndrome specifically. Only NCT04704297 and NCT00635037 directly name MPS.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24822235](https://pubmed.ncbi.nlm.nih.gov/24822235/) | 2014 | RCT | Journal of Oral & Facial Pain and Headache | Cyclobenzaprine vs. tizanidine vs. placebo added to self-care for myofascial jaw pain upon awakening |
| [11889661](https://pubmed.ncbi.nlm.nih.gov/11889661/) | 2002 | RCT | Journal of Orofacial Pain | Cyclobenzaprine vs. clonazepam vs. placebo added to self-care for myofascial jaw pain upon awakening |
| [12764337](https://pubmed.ncbi.nlm.nih.gov/12764337/) | 2003 | RCT | Annals of Emergency Medicine | Cyclobenzaprine + ibuprofen vs. ibuprofen alone for acute myofascial strain in the ED |
| [20673246](https://pubmed.ncbi.nlm.nih.gov/20673246/) | 2011 | RCT | Pain Practice | Acupuncture vs. trigger point injection combined with cyclobenzaprine and dipyrone for myofascial trigger point pain |
| [3464212](https://pubmed.ncbi.nlm.nih.gov/3464212/) | 1986 | Review | The American Journal of Medicine | Classic review describing the clinical syndrome of fibrositis (precursor terminology overlapping fibromyalgia/MPS) |

---

## Taiwan Market Information

Cyclobenzaprine currently holds no marketing license in Taiwan (`total_licenses = 0`); no registration records are available for this drug.

---

## Safety Considerations

- **Drug Interactions**: Of 236 total interactions on record, several are classified as **Major**, including **Bupropion**, **Morphine**, **Potassium citrate**, **Dexfenfluramine**, and **Fenfluramine**. Additional **Moderate**-level interactions include anticholinergic-burden agents (Hyoscyamine, Atropine, Glycopyrronium, Dicyclomine, Clidinium, Mepenzolate, Methscopolamine) and opioid/GI agents (Loperamide, Aprepitant, Eluxadoline, Dronabinol).

Key warnings and contraindications from the local label are not yet available [Data Gap: DG001, Blocking severity — required before S1 safety screening can proceed].

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The L2 evidence level (direct RCT support in mechanistically related myofascial/jaw pain and acute myofascial strain, plus a large body of fibromyalgia RCTs for the same drug/formulation) supports moving forward, but the missing local label data (warnings/contraindications) and MOA documentation prevent an unconditional "Go."

**To proceed, the following is needed:**
- TFDA/local label warnings and contraindications (currently blocking — DG001)
- Confirmed DrugBank mechanism-of-action data (DG002)
- Clarification of cyclobenzaprine's specific therapeutic contribution in combination trials (e.g., NCT04704297, NCT00635037) versus the injection/acupuncture comparators
- A dedicated Phase 2/3 trial in myofascial pain syndrome specifically (rather than inferring from fibromyalgia data)
- Review of Major-level DDIs (Bupropion, Morphine, Potassium citrate, Dexfenfluramine, Fenfluramine) against likely co-medications in the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

