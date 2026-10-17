---
layout: default
title: Camphor
parent: Model Prediction Only (L5)
nav_order: 135
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Camphor: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the approval records compiled for this report (marketed…"
monitor_inn: "Camphor"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "erectile dysfunction (disease)", "pulmonary hypertension", "migraine with or without aura, susceptibility to", "kyphoscoliotic heart disease", "ulerythema ophryogenesis", "Raynaud disease", "atrophoderma vermiculata", "Tourette syndrome"]
---

# Camphor
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

# Camphor: From Topical Ophthalmic/Counter-Irritant Use to Migraine Disorder

## One-Sentence Summary

Camphor is a long-established topical agent, marketed in India mainly as an ingredient in eye drops and in a liniment.
The TxGNN model predicts it may be effective for **migraine disorder**, but the support is thin: **no registered clinical trials** and only **3 indirect publications** (two case reports or series and one historical review) were found.
This is best regarded as a research question rather than an established repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the approval records compiled for this report (marketed mainly as eye drops and a liniment) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 for the prediction as retrieved (model prediction with no human efficacy studies); a related migraine-susceptibility prediction has an L4 preclinical study |
| India Market Status | ✓ Marketed |
| Number of Registrations | 19 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available in the data compiled for this report. Based on general pharmacology, camphor is known to modulate TRP channels (TRPV1, TRPA1, TRPM8) and acts as a topical counter-irritant and analgesic. These channels are plausibly involved in trigeminovascular pain pathways, which are central to migraine. This is the main basis for a mechanistic link.

The relationship between the original use and migraine is indirect. Camphor's marketed products are topical or ophthalmic, and its pain-relieving effect is local. Migraine is a central neurovascular disorder, so it is unclear whether a local counter-irritant effect would translate into migraine benefit.

The retrieved literature does not strengthen the case. The two cluster headache reports describe headaches **temporally related to** toothpastes containing camphor and eucalyptus essential oils, which is a potential harm signal rather than a benefit. The third article is a historical review of paediatric neuropsychopharmacotherapy of unclear relevance. The high TxGNN score is a computational prediction only.

A 2026 animal study (PMID 42849823), found under the related prediction "migraine with or without aura, susceptibility to", reported that natural (+)-camphor alleviated reserpine-induced migraine with local cerebral vasospasm, via the p38β MAPK/ATF2 pathway. This is the most direct supportive signal in the dataset, but it is preclinical only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35856604](https://pubmed.ncbi.nlm.nih.gov/35856604/) | 2022 | Case series | Headache | Five cases of cluster headache linked to toothpastes containing pro-convulsant essential oils; a potential harm signal, not evidence of benefit |
| [34373243](https://pubmed.ncbi.nlm.nih.gov/34373243/) | 2021 | Case report | BMJ Case Reports | Two cases of cluster headache temporally related to toothpastes containing camphor and eucalyptus oils |
| [27058833](https://pubmed.ncbi.nlm.nih.gov/27058833/) | 2016 | Review | Z Kinder Jugendpsychiatr Psychother | Historical analysis of paediatric neuropsychopharmacotherapy in the 1940s and 1950s; relevance to camphor in migraine is unclear |
| [42849823](https://pubmed.ncbi.nlm.nih.gov/42849823/) | 2026 | Preclinical animal study | J Ethnopharmacol | Natural (+)-camphor alleviated reserpine-induced migraine with cerebral vasospasm in an animal model via p38β MAPK/ATF2 (found under the related migraine-susceptibility prediction) |

---

## India Market Information

Camphor has 19 valid single-ingredient registrations and none are cancelled or combination products. The approval records do not include indication text. The main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 124746 | Lacricool Eye Drop | Eye drop, 10 ml bottle | Not specified |
| 59558 | Doil-MR Liniment | Liniment, 30 ml bottle | Not specified |
| 74550 | Eyce Eye Drop | Eye drop, 10 ml bottle | Not specified |
| 35072 | Cooleye Eye Drop | Eye drop, 10 ml bottle | Not specified |
| 187998 | Relax Plus Eye Drop | Eye drop, 10 ml packet | Not specified |

The remaining registrations are almost all eye drops or ophthalmic solutions. Only the liniment is a non-ophthalmic product.

---

## Safety Considerations

- **Neurotoxicity signal:** The case reports link camphor and essential-oil products to cluster headache. Essential oils with pro-convulsant properties are known to cause seizures and may worsen migraine. The data compiled for this report also notes camphor's seizure risk on ingestion.
- **Preclinical toxicity:** A rat study of edible camphor (a product that may not be pure camphor) reported oxidative stress and tissue histopathology changes after oral dosing, relevant to any systemic use.

No drug interaction data were found. Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score with no registered trials and no controlled human data. The only direct support is a single animal study, while the human reports suggest possible harm (headache triggering) and camphor carries a recognised seizure risk. The migraine prediction should be treated as a hypothesis-generating research question.

**To proceed, the following is needed:**
- Mechanism-of-action data from DrugBank to evaluate the TRP-channel hypothesis properly
- Package insert warnings and contraindications for the marketed products
- Replication of the preclinical migraine findings and a dose-exposure assessment
- A route and formulation strategy, since current marketed forms are topical or ophthalmic
- A safety assessment of seizure and headache-trigger risk before any human study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

