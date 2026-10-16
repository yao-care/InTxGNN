---
layout: default
title: Dipyridamole
parent: Model Prediction Only (L5)
nav_order: 276
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dipyridamole: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Atrial fibrillation"
---

# Dipyridamole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Dipyridamole: From Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Dipyridamole is an antiplatelet and vasodilating drug, listed in the knowledge graph under atrial fibrillation as its source indication.
The TxGNN model's top-ranked prediction is **Prinzmetal angina**, but this one is supported only by diagnostic and observational literature (**0 clinical trials**, **10 publications**).
The best-supported prediction is **stroke disorder** (rank 2), backed by **8 clinical trials** and **19 publications**, including the large ESPRIT trial. This is an established use rather than a novel repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation (from the knowledge graph; no approved indication text is available from the India licences) |
| Predicted New Indication | Prinzmetal angina (rank 1); stroke disorder (rank 2) is the best-supported alternative |
| TxGNN Prediction Score | 99.99% (Prinzmetal angina); 99.95% (stroke disorder) |
| Evidence Level | L4 for Prinzmetal angina; L1 for stroke disorder |
| India Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold for Prinzmetal angina; Proceed with Guardrails for stroke disorder |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the literature, dipyridamole inhibits adenosine reuptake and phosphodiesterase (PDE) activity. This raises cAMP and cGMP in platelets and vascular smooth muscle, which reduces platelet aggregation and causes vasodilation.

**Prinzmetal angina (rank 1).** The mechanistic link is weak. In the retrieved literature, dipyridamole appears mainly as a pharmacologic stress-test agent. One report describes aminophylline reversal after dipyridamole stress triggering coronary vasospasm in variant angina. That is diagnostic and pathophysiological context, not evidence of therapeutic benefit. Adenosine-mediated coronary steal could even worsen vasospasm in susceptible patients.

**Stroke disorder (rank 2) and transient ischemic attack (rank 5).** The mechanism fits well. Platelet inhibition is the basis for aspirin plus extended-release dipyridamole in secondary stroke prevention. Randomized trials, meta-analyses and Cochrane reviews support this use. The prediction is therefore reasonable, but it confirms an already-known indication.

**Other predictions.** "Thrombotic disease" is biologically consistent but too broad, and its literature is largely general or off-topic. The remaining predictions (sick sinus syndrome 2, sarcoglycanopathy, Wildervanck syndrome, a macrocephaly syndrome, and cavernous and lateral sinus thrombosis) have no trials or literature and no evident mechanistic link. They are model signals only.

---

## Clinical Trial Evidence

The table covers the best-supported prediction (stroke disorder). No clinical trials are registered for Prinzmetal angina, the rank 1 prediction.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00161070](https://clinicaltrials.gov/study/NCT00161070) | Phase 4 | Completed | 4500 | ESPRIT: aspirin plus dipyridamole or mild anticoagulation versus aspirin alone after cerebral ischemia of arterial origin |
| [NCT00562588](https://clinicaltrials.gov/study/NCT00562588) | Phase 4 | Completed | 551 | EARLY: Aggrenox started within 24 hours of ischaemic stroke versus after 7 days of aspirin (open-label, blinded endpoint) |
| [NCT00238667](https://clinicaltrials.gov/study/NCT00238667) | Phase 3 | Completed | 250 | CADISS: feasibility of anticoagulants versus antiplatelets in cervical artery dissection (dipyridamole not the specific agent) |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | PFO closure or anticoagulation versus antiplatelet therapy to prevent stroke recurrence (indirect evidence) |
| [NCT00738894](https://clinicaltrials.gov/study/NCT00738894) | N/A | Completed | 664 | Gore REDUCE: PFO closure plus antiplatelet management versus antiplatelet management alone (device trial) |
| [NCT02630862](https://clinicaltrials.gov/study/NCT02630862) | N/A | Completed | 240 | Oxidative stress and oxysterol profiling after carotid revascularization, including dipyridamole's antioxidant action (biomarker study) |
| [NCT06053021](https://clinicaltrials.gov/study/NCT06053021) | N/A | Unknown | 1200 | Antiplatelet therapy in acute ischemic stroke with thrombocytopenia |
| [NCT06983795](https://clinicaltrials.gov/study/NCT06983795) | N/A | Not yet recruiting | 1000 | Asia-Pacific registry of patients with PFO and ischemic stroke |

---

## Literature Evidence

**Stroke disorder (best-supported prediction)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15569877](https://pubmed.ncbi.nlm.nih.gov/15569877/) | 2005 | Meta-analysis | Stroke | Individual patient data meta-analysis of dipyridamole for preventing recurrent ischemic stroke |
| [17636684](https://pubmed.ncbi.nlm.nih.gov/17636684/) | 2007 | Cochrane review | Cochrane Database Syst Rev | Dipyridamole for stroke and vascular event prevention; aspirin plus dipyridamole gave a 22% risk reduction versus aspirin in one trial |
| [11786451](https://pubmed.ncbi.nlm.nih.gov/11786451/) | 2002 | Meta-analysis | BMJ | Antiplatelet therapy for preventing death, MI and stroke in high-risk patients |
| [23871093](https://pubmed.ncbi.nlm.nih.gov/23871093/) | 2013 | Meta-analysis | J Neurol Sci | Aspirin plus dipyridamole versus aspirin for secondary prevention after TIA or stroke |
| [31177983](https://pubmed.ncbi.nlm.nih.gov/31177983/) | 2019 | Network meta-analysis | Stroke | Efficacy and safety of antiplatelet agents after noncardioembolic stroke or TIA |
| [34211246](https://pubmed.ncbi.nlm.nih.gov/34211246/) | 2021 | Review | Australian Prescriber | Aspirin, clopidogrel, or aspirin plus dipyridamole are first-line options for secondary prevention without atrial fibrillation |
| [20955428](https://pubmed.ncbi.nlm.nih.gov/20955428/) | 2010 | Review | Ann N Y Acad Sci | Possible neuroprotective and anti-inflammatory effects of dipyridamole in acute stroke |

**Prinzmetal angina (rank 1)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [633593](https://pubmed.ncbi.nlm.nih.gov/633593/) | 1978 | Observational | Jpn Circ J | Response of 26 patients with rest angina, including 13 with variant angina, to several drugs including dipyridamole 50 mg |
| [3421166](https://pubmed.ncbi.nlm.nih.gov/3421166/) | 1988 | Case report/Observational | Am J Cardiol | Aminophylline termination of dipyridamole stress can trigger coronary vasospasm in variant angina |
| [3190956](https://pubmed.ncbi.nlm.nih.gov/3190956/) | 1988 | Observational | Br Heart J | Reproducibility of exercise testing in patients with ST elevation and different dipyridamole test responses |

The Prinzmetal angina literature is diagnostic or observational and does not show therapeutic benefit.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 111097 | Infartin 60 Tablet | Strip of 30 tablets | Not specified |
| 220671 | Thrombonil 75mg Tablet | Strip of 10 tablets | Not specified |
| 176522 | Persantin 100mg Tablet | Strip of 10 tablets | Not specified |
| 41947 | Cardiwell 75mg Tablet | Strip of 10 tablets | Not specified |
| 44912 | Cardiwell 100mg Tablet | Strip of 10 tablets | Not specified |

A sixth valid licence, Dynacard 100mg Tablet (64959, USV Ltd), is also registered. All six are single-ingredient oral tablets, and none has been cancelled.

---

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: The knowledge graph links dipyridamole to a long list of conditions, including kidney disease, liver disease, gallbladder disease, thrombocytopenia, peptic ulcer disease, hypotensive disorder, gout, acute coronary syndrome, myocardial infarction, hemophilia, anemia, gastritis, and Alzheimer disease. These are graph edges and must be checked against the official package insert before use.
- **Drug Interactions**: 321 interactions are recorded. Moderate-level interactions include dexfenfluramine, sibutramine and fenfluramine. Other recorded interactions (level not classified) include acetylsalicylic acid, cimetidine, omeprazole, pantoprazole, lansoprazole, morphine, metformin, glimepiride, rosiglitazone, simvastatin, prednisone, vancomycin, amphotericin B, calcitriol, sucralfate, lactulose and nystatin.
- **Practical guardrails** (from the evidence review): headache and gastrointestinal intolerance, bleeding risk with concomitant antithrombotics, and caution in severe coronary disease.

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold for Prinzmetal angina (rank 1); Proceed with Guardrails for stroke disorder and transient ischemic attack**

**Rationale:**
- Prinzmetal angina has the highest TxGNN score but no trials, and only diagnostic or observational literature. Dipyridamole's adenosine-mediated vasodilation could plausibly worsen vasospasm, so the decision is Hold.
- Stroke disorder and transient ischemic attack are supported by ESPRIT (n=4500) and multiple meta-analyses and Cochrane reviews (Level L1). These are already-established uses, so they confirm the model but are not novel repurposing.
- The other predictions are prediction-only (L5), or too broad to evaluate (thrombotic disease, L4), and should stay on Hold.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications for the India-licensed products (a blocking data gap for safety screening)
- Detailed mechanism of action data
- For thrombotic disease, a narrower and specific thrombotic condition to evaluate
- A review of the knowledge-graph contraindications and the 321 recorded interactions against label text, with a bleeding-risk monitoring plan for co-prescribed antithrombotics
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

