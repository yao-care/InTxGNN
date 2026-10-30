---
layout: default
title: Niclosamide
parent: Moderate Evidence (L3-L4)
nav_order: 592
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-30
description: "Niclosamide: predicted new indication Heart disease (evidence level L5). Approved use: Not stated in the India license data (the drug is generally known as…"
monitor_inn: "Niclosamide"
predicted_indications: ["heart disease", "Laubry-Pezzi syndrome", "Pierre Robin syndrome associated with a chromosomal anomaly", "genetic syndromic Pierre Robin syndrome", "partial deletion of the long arm of chromosome 7", "orofacial clefting syndrome", "pulmonary valve disease", "interventricular septum aneurysm", "Jeune syndrome situs inversus", "disorder of fucoglycosan synthesis"]
---

# Niclosamide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

## Niclosamide: From Anthelmintic Use to Heart Disease
{: .text-alpha }

## One-Sentence Summary

Niclosamide is an oral anthelmintic (anti-worm) drug that is marketed in India, but the data compiled for this report do not state its approved indication text.
The TxGNN model predicts it may be effective for **heart disease**, but **no clinical trials** are registered and the supporting literature is almost entirely preclinical or indirect.
This is a model-generated hypothesis with limited biological support, not a clinically validated direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India license data (the drug is generally known as an anthelmintic) |
| Predicted New Indication | Heart disease |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L4 (preclinical and mechanistic studies only) |
| India Market Status | Listed in a compiled Indian medicine price dataset (2 of 2) – CDSCO approval status is not included in this data |
| Number of Listed Products | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Niclosamide is known as an anthelmintic and is on the WHO List of Essential Medicines. The literature describes it as suppressing mitochondrial oxidative phosphorylation (mitochondrial uncoupling) and modulating several signalling pathways, such as AMPK/mTOR.

Several preclinical findings point to plausible cardiac relevance:
- In mice with pressure-overload heart failure, niclosamide improved outcomes. The authors link this to enhanced mitochondrial respiration and ATP production in cardiomyocytes (PMID 34736968).
- In human valvular interstitial cells, niclosamide reduced calcification by inhibiting the AMPK/mTOR pathway, which may be relevant to calcific aortic valve disease (PMID 39515588).

There are important caveats:
- Niclosamide potentiates the TMEM16A channel and induces vasoconstriction (PMID 38814250, PMID 40491382), which is a possible cardiovascular safety concern.
- Oral niclosamide has poor systemic bioavailability, which limits translation to heart tissue.
- "Heart disease" is a very broad category. Any further work should narrow it to specific conditions, such as heart failure or calcific aortic valve disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Most of the retrieved papers are mechanistic, preclinical, or only tangentially related. The table lists the most relevant ones.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34736968](https://pubmed.ncbi.nlm.nih.gov/34736968/) | 2021 | Animal study (mouse) | Eur J Pharmacol | Niclosamide attenuated pressure-overload heart failure in mice, linked to enhanced mitochondrial function |
| [39515588](https://pubmed.ncbi.nlm.nih.gov/39515588/) | 2024 | In vitro (human cells) | Biochem Pharmacol | Reduced calcification in human valvular interstitial cells through AMPK/mTOR inhibition |
| [38814250](https://pubmed.ncbi.nlm.nih.gov/38814250/) | 2024 | Mechanistic/pharmacology | J Gen Physiol | Niclosamide potentiates TMEM16A and induces vasoconstriction (safety signal) |
| [40491382](https://pubmed.ncbi.nlm.nih.gov/40491382/) | 2025 | Pharmacology | Br J Pharmacol | Clinically relevant concentrations modulate TMEM16A and CaV1.2 channels, affecting artery tone and capillary diameter |
| [38288981](https://pubmed.ncbi.nlm.nih.gov/38288981/) | 2024 | Animal study (mouse) | ACS Appl Mater Interfaces | ROS-suppressing nanoplatform for preventing myocardial infarction in mice, reportedly using a niclosamide-based formulation |
| [36684586](https://pubmed.ncbi.nlm.nih.gov/36684586/) | 2022 | Mechanistic (indirect) | Front Cardiovasc Med | Niclosamide identified as a TMEM16F inhibitor in the context of SARS-CoV-2 spike-driven platelet procoagulant activity |
| [29736201](https://pubmed.ncbi.nlm.nih.gov/29736201/) | 2018 | Animal study (indirect) | Am J Transl Res | Niclosamide ethanolamine improved diabetes and diabetic kidney disease in mice |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 153896 | Niclesone 1000mg Tablet | Strip of 10 tablets | Not stated in license data |
| 151214 | Niclosan 500mg Tablet | Strip of 4 tablets | Not stated in license data |

Both products are single-ingredient oral tablets with valid status.

---

## Safety Considerations

- **Drug Interactions** (7 records in the data compiled for this report):
  - **Major:** Tizanidine
  - **Moderate:** Alosetron, Bendamustine, Duloxetine, Ropinirole, Ramelteon
  - **Pharmacological target:** Niclosamide acts on the KNa1.1 (KCNT1) potassium channel.
- **Cardiovascular signal:** Preclinical studies show that niclosamide potentiates TMEM16A and causes vasoconstriction. This needs careful evaluation before any cardiac use.

Package insert warnings and contraindications were not available. Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is a model prediction only. There are no clinical trials, and the supporting evidence is limited to animal and in vitro studies. Poor oral bioavailability and a vasoconstriction signal further weaken the case. The other nine predicted indications (for example, Laubry-Pezzi syndrome and Pierre Robin syndrome) have no supporting literature or trials and are not mechanistically plausible.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from India
- Detailed mechanism of action data (MOA)
- Narrowing "heart disease" to specific conditions (such as heart failure or calcific aortic valve disease) and confirming the preclinical findings in those models
- Pharmacokinetic and formulation work to achieve adequate systemic exposure
- A dedicated cardiovascular safety assessment, focused on TMEM16A-mediated vasoconstriction and the Tizanidine interaction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

