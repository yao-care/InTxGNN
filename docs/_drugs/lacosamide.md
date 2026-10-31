---
layout: default
title: Lacosamide
parent: Model Prediction Only (L5)
nav_order: 467
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
monitor_inn: "Lacosamide"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "trichotillomania", "nephrogenic syndrome of inappropriate antidiuresis", "migraine disorder", "insomnia (disease)", "migraine with brainstem aura", "myofascial pain syndrome", "obsessive-compulsive disorder", "papillary conjunctivitis"]
description: "Lacosamide: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Lacosamide
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

## Lacosamide: Manic bipolar affective disorder
{: .text-alpha }

## One-Sentence Summary

Lacosamide is a sodium-channel-modulating antiseizure medicine that is widely marketed in India.
The TxGNN model predicts it may be effective for **migraine disorder**,
with **4 clinical trials** (including 3 Phase 3 trials) and **19 publications** currently supporting this direction, including one published randomized double-blind trial against propranolol.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the literature, lacosamide enhances slow inactivation of voltage-gated sodium channels and may also interact with collapsin response mediator protein 2 (CRMP2). Preclinical work suggests that CRMP2 modulation can reduce release of calcitonin gene-related peptide (CGRP) in the trigeminal system, a key driver of migraine pain.

Several antiseizure medicines (such as topiramate) are already used for migraine prevention, so a link between seizure control and migraine prevention is established. In mice, lacosamide reduced cortical spreading depolarization, the wave of cortical activity thought to underlie migraine aura. This supports biological plausibility.

Clinical support is real but limited. Published human results come mainly from one randomized trial against propranolol, and most trials compare against active drugs rather than placebo. This limits conclusions about absolute efficacy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05851781](https://clinicaltrials.gov/study/NCT05851781) | Phase 3 | Completed | 600 | Lacosamide vs propranolol in migraine; outcomes are reduction in monthly headache days and ≥50% responder rate |
| [NCT06243692](https://clinicaltrials.gov/study/NCT06243692) | Phase 3 | Unknown | 600 | Lacosamide vs topiramate in migraine; no results available, reliability uncertain |
| [NCT05632133](https://clinicaltrials.gov/study/NCT05632133) | Phase 3 (labelled; described as a pilot) | Completed | 200 | Effect on serum CGRP in episodic migraine, with lacosamide 50 mg twice daily plus ibuprofen vs ibuprofen alone; biomarker-oriented |
| [NCT00440518](https://clinicaltrials.gov/study/NCT00440518) | Phase 2 | Completed | 218 | Double-blind, placebo-controlled trial of 100 mg/day and 300 mg/day lacosamide; the registry title is truncated, so the indication could not be confirmed from the available data |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41863672](https://pubmed.ncbi.nlm.nih.gov/41863672/) | 2026 | RCT | Molecular Neurobiology | Double-blind trial of lacosamide vs propranolol for episodic migraine prevention, aimed especially at patients who cannot tolerate propranolol |
| [38502425](https://pubmed.ncbi.nlm.nih.gov/38502425/) | 2024 | RCT | Acta Neurologica Belgica | Effect of lacosamide on serum CGRP levels in episodic migraine patients |
| [22779776](https://pubmed.ncbi.nlm.nih.gov/22779776/) | 2013 | Systematic review/meta-analysis | Epilepsia | Adverse event profile of lacosamide across randomized controlled trials |
| [40670944](https://pubmed.ncbi.nlm.nih.gov/40670944/) | 2025 | Preclinical | J Headache Pain | Lacosamide effect on cortical spreading depolarization in mice |
| [27917413](https://pubmed.ncbi.nlm.nih.gov/27917413/) | 2016 | Preclinical | Pain Reports | (S)-Lacosamide in preclinical models of cephalic pain, targeting CRMP2 to inhibit CGRP release |
| [22862686](https://pubmed.ncbi.nlm.nih.gov/22862686/) | 2012 | Review | Expert Opin Emerg Drugs | Emerging treatments for chronic and refractory chronic migraine |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | Pharmacotherapy update for trigeminal neuralgia; mentions third-generation anticonvulsants as possible options (indirect) |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 126251 | Lacove 150mg Tablet | Strip of 10 tablets | Not stated |
| 250388 | Zolaco 200mg Tablet | Strip of 10 tablets | Not stated |
| 121572 | Lacoxa 100mg Tablet | Strip of 10 tablets | Not stated |
| 123738 | Laconext 10mg Injection | Vial of 20 ml injection | Not stated |
| 208370 | Seizgard 150mg Tablet | Strip of 10 tablets | Not stated |

Twenty valid single-ingredient registrations are on record, in oral tablet and injectable forms.

## Safety Considerations

- **Disease associations flagged in the knowledge graph** (drug-disease contraindication links, not label text): liver disease, gallbladder disease, cardiac conduction and rhythm disorders (atrioventricular block, sick sinus syndrome, atrial fibrillation, atrial flutter), coronary artery disease, myocardial ischemia, and orthostatic hypotension and related autonomic disorders (multiple system atrophy, postural orthostatic tachycardia syndrome). Cardiac conduction problems deserve particular attention when screening migraine patients.
- **Drug Interactions**: 25 interactions were recorded. Major-level interactions are with dolasetron, ceritinib and siponimod. Moderate-level interactions include clarithromycin, ethanol, cobicistat, chloroquine, hydroxychloroquine, mefloquine, lidocaine, ketoconazole, pasireotide, alectinib, brigatinib, crizotinib, fingolimod, idelalisib, imatinib, ozanimod and sunitinib. Many of these are drugs that affect cardiac conduction.
- **Case report safety signal**: neutropenia was reported with lacosamide in a patient with bipolar disorder and epilepsy.

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Migraine is the best-supported prediction among the candidates. It has three Phase 3 trials, one Phase 2 placebo-controlled trial and one published randomized double-blind trial, plus plausible sodium channel and CGRP-related mechanisms. However, published results come from essentially one trial and the active-comparator designs limit conclusions about absolute efficacy.

**To proceed, the following is needed:**
- Results from the completed trials (NCT05851781, NCT00440518) and confirmation of what NCT00440518 studied
- Independent replication, ideally a placebo-controlled trial, to confirm effect sizes
- Package insert warnings and contraindications from the India registrations, plus the approved indication text
- Confirmed mechanism of action data
- A cardiac safety plan (ECG screening and attention to conduction-affecting co-medications)

**Other predicted indications (for reference):** Manic bipolar affective disorder (L3) and myofascial pain syndrome (L2) are research questions only. Bipolar disorder rests on small observational data and a neutropenia case report. Myofascial pain has only a Phase 2 trial in fibromyalgia, with no results provided. Tourette syndrome, trichotillomania, nephrogenic syndrome of inappropriate antidiuresis, insomnia, migraine with brainstem aura, obsessive-compulsive disorder and papillary conjunctivitis are on hold, since they have no meaningful supporting evidence. For Tourette syndrome, the literature even suggests antiepileptic drugs can induce tics.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

