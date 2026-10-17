---
layout: default
title: Mexiletine
parent: Model Prediction Only (L5)
nav_order: 546
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Mexiletine: predicted new indication Hypertrichosis (evidence level L5). Approved use: Not available"
monitor_inn: "Mexiletine"
predicted_indications: ["hypertrichosis (disease)", "nephrogenic syndrome of inappropriate antidiuresis", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "migraine disorder", "isolated genetic hair shaft abnormality", "pulmonary hypertension", "migraine with brainstem aura", "headache disorder"]
---

# Mexiletine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Mexiletine: From Ventricular Arrhythmia to Hypertrichosis (Top Prediction), with Headache Disorder as the Best-Supported Candidate

## One-Sentence Summary

Mexiletine is a class IB sodium channel blocker (antiarrhythmic) marketed in India. The approved indication text is not available in the data compiled for this report.
The TxGNN model's top-ranked prediction is **hypertrichosis**, which has no clinical or literature support. Among the top 10 predictions, **headache disorder** and **migraine disorder** have the most supporting evidence, consisting of small, uncontrolled studies and case series (no registered clinical trials).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (approved indication text is empty in all registrations) |
| Predicted New Indication | Hypertrichosis (rank 1); best-supported alternatives: headache disorder, migraine disorder |
| TxGNN Prediction Score | 99.78% (hypertrichosis); 99.48% (headache disorder); 99.66% (migraine disorder) |
| Evidence Level | L5 for hypertrichosis; L3 for headache disorder and migraine disorder |
| India Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold (hypertrichosis); headache disorder may proceed as a research question only |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Mexiletine is known as a class IB antiarrhythmic that blocks voltage-gated sodium channels, which is the basis for the mechanistic reasoning below.

**Hypertrichosis (top prediction):** No clinical trials or literature were found, and no plausible mechanistic link from sodium channel blockade to hypertrichosis is evident. The high score is a model output only and should be treated with caution. The same applies to the other top-ranked predictions with no evidence (nephrogenic syndrome of inappropriate antidiuresis, Ambras-type hypertrichosis, Dandy-Walker-related syndromes, hair shaft abnormality, and migraine with brainstem aura).

**Headache disorders (best supported):** Sodium channel blockade may dampen abnormal neuronal firing and trigeminal-autonomic pathway activity. This is plausible for refractory headaches, and similar drugs (lidocaine, mexiletine) are already used for neuropathic pain and myotonia. The supporting data are limited to small, mostly uncontrolled studies.

**Pulmonary hypertension:** The only relevant item is a 2026 preclinical study on lidocaine, a related drug, acting on the TMEM16A chloride channel. This is indirect, class-analog support and does not involve mexiletine.

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the top 10 predicted indications.

## Literature Evidence

Evidence below is for headache-related and pulmonary hypertension predictions; the other predictions have no literature.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33361408](https://pubmed.ncbi.nlm.nih.gov/33361408/) | 2021 | Prospective open-label study with single-arm meta-analysis | J Neurol Neurosurg Psychiatry | Medical treatment of SUNCT and SUNA, related headache disorders where treatment evidence is scarce |
| [20425204](https://pubmed.ncbi.nlm.nih.gov/20425204/) | 2010 | Clinical report / case series | Curr Pain Headache Rep | IV lidocaine and mexiletine (class IB sodium channel blockers) in trigeminal autonomic cephalalgias |
| [18793209](https://pubmed.ncbi.nlm.nih.gov/18793209/) | 2008 | Case series (9 patients) | Headache | Mexiletine used in refractory chronic daily headache |
| [6938859](https://pubmed.ncbi.nlm.nih.gov/6938859/) | 1981 | Early clinical report | N Z Med J | Mexiletine in vascular headaches |
| [40197813](https://pubmed.ncbi.nlm.nih.gov/40197813/) | 2025 | Review (Cochrane) | Cochrane Database Syst Rev | Drug treatment for myotonia; not headache-specific |
| [41518899](https://pubmed.ncbi.nlm.nih.gov/41518899/) | 2026 | Preclinical | J Pharmacol Exp Ther | Lidocaine as a TMEM16A chloride channel blocker for pulmonary arterial hypertension (indirect, does not involve mexiletine) |
| [1724233](https://pubmed.ncbi.nlm.nih.gov/1724233/) | 1991 | Clinical study | Int J Cardiol | Disopyramide and mexiletine in ventricular arrhythmias; not relevant to pulmonary hypertension |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 114117 | Jollimex 150 Capsule | Strip of 10 capsules | Not available |
| 114260 | Jollimex 50 Capsule | Strip of 10 capsules | Not available |
| 241508 | Welhart 150mg Capsule | Strip of 10 capsules | Not available |
| 133843 | Mexohar 150mg Capsule | Strip of 30 capsules | Not available |
| 134396 | Mexohar 50mg Capsule | Strip of 30 capsules | Not available |

A sixth registration (241652, Welhart 50mg Capsule, strip of 10 capsules) is also valid. All six registrations are single-ingredient oral capsules.

## Safety Considerations

- **Contraindications (from a knowledge graph of drug-disease relationships, not label text):** epilepsy, liver disease, gallbladder disease, hypotensive disorder, myocardial infarction, coronary thrombosis, hemoglobinopathy, atrioventricular block, sick sinus syndrome, familial sick sinus syndrome.
- **Drug Interactions:** 106 interactions are recorded. Notable examples include **Bupropion (Major)**, and Moderate interactions with alosetron, morphine, lorcaserin, potassium citrate, eliglustat, obeticholic acid, rolapitant, and several bowel-preparation agents (picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes).
- **Other considerations:** As a class IB antiarrhythmic, proarrhythmic risk needs evaluation before any new use. Package insert warnings are not available in the data compiled for this report; please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, hypertrichosis, and all other predictions without evidence). Headache disorder and migraine disorder may be pursued as **research questions** only.

**Rationale:**
The top predictions rest on model scores alone, with no trials, literature, or plausible mechanism. Headache-related indications have limited L3 evidence (case series and an open-label study) with no RCTs, which is not enough for a Go decision. Safety data gaps (missing package insert warnings) also block safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India registrations, including approved indications
- Mechanism of action data
- For headache indications: a controlled study design (RCT) or a more systematic evidence review, focused on trigeminal autonomic cephalalgias and refractory chronic daily headache
- Cardiac safety assessment (proarrhythmic risk, conduction disorders) and a plan for managing the 106 known drug interactions, especially with bupropion
- Route and dosage compatibility assessment for the new indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

