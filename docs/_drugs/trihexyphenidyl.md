---
layout: default
title: Trihexyphenidyl
parent: Model Prediction Only (L5)
nav_order: 865
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Trihexyphenidyl: predicted new indication Attention deficit-hyperactivity disorder (evidence level L5). Approved use: Parkinson disease (and related parkinsonian disorders, dystonia…"
monitor_inn: "Trihexyphenidyl"
predicted_indications: ["attention deficit-hyperactivity disorder", "faciodigitogenital syndrome", "attention deficit hyperactivity disorder, inattentive type", "Rasmussen subacute encephalitis", "PLA2G6-associated neurodegeneration", "congenital disorder of glycosylation with defective fucosylation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "retinal dystrophy with or without extraocular anomalies", "myelitis", "Charcot-Marie-Tooth disease, demyelinating, type 1G"]
---

# Trihexyphenidyl
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

## Trihexyphenidyl: From Parkinson Disease to Attention Deficit-Hyperactivity Disorder
{: .text-alpha }

## One-Sentence Summary

Trihexyphenidyl is a central anticholinergic drug originally used to treat Parkinson disease and related movement disorders such as parkinsonism and dystonia.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**, but there are currently **no registered clinical trials** and only **1 loosely related publication** (a case series on tic disorder with dystonia), so the prediction rests almost entirely on computation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease (and related parkinsonian disorders, dystonia, blepharospasm) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for trihexyphenidyl: "Trihexyphenidyl Hydrochloride is the substituted piperidine salt, 3-(1-piperidyl)- 1-phenylcyclohexyl-1-propanol hydrochloride, which exerts a direct inhibitory effect upon the parasympathetic nervous system. It also has a relaxing effect on smooth musculature; exerted both directly upon the muscle tissue itself and indirectly through an inhibitory effect upon the parasympathetic nervous system." ([DailyMed: trihexyphenidyl hydrochloride prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b60ef86c-b8b6-4530-baaf-d4671ce961af), label version 2026-07-23; accessed 2026-11-19.) Based on known pharmacology, trihexyphenidyl is a central muscarinic antagonist with preference for the M1 receptor. It modulates the balance between cholinergic and dopaminergic signalling in the striatum, which is the basis of its benefit in parkinsonism and dystonia.

ADHD involves dysregulation of dopaminergic and noradrenergic pathways. This gives an indirect, plausible link: a drug that adjusts striatal cholinergic-dopaminergic balance could, in theory, influence the circuits involved. However, this link is speculative. The only retrieved paper describes primary tic disorder associated with dystonia, a related movement/neuropsychiatric setting, and is not a study of ADHD treatment.

There is also a notable concern. Anticholinergic drugs can cause cognitive and attention-related adverse effects, which runs against what would be desired in ADHD. The very high TxGNN score is therefore a computational signal without direct clinical support.

Other predicted indications in the model output (for example, the ADHD inattentive subtype, PLA2G6-associated neurodegeneration, Rasmussen encephalitis, and myelitis) are also supported mainly by computation. Among these, PLA2G6-associated neurodegeneration has the most plausible symptomatic overlap (dystonia-parkinsonism), though any benefit would be symptomatic only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21506147](https://pubmed.ncbi.nlm.nih.gov/21506147/) | 2011 | Case series | Movement Disorders | Large clinical series and literature review of primary tic disorder co-occurring with dystonia; describes the syndrome's prevalence and features. It does not test trihexyphenidyl in ADHD. |

---

## India Market Information

Twenty valid single-ingredient registrations are listed; the approved indication text is not available for any of them.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 54391 | Cerhexy 2mg Tablet | Strip of 20 tablets | Valid |
| 65495 | D Park 2mg Tablet | Strip of 10 tablets | Valid |
| 73957 | Eps 2 Tablet | Strip of 10 tablets | Valid |
| 89607 | Flyper 5mg Tablet | Strip of 30 tablets | Valid |
| 104970 | Hexymelt 2mg Tablet MD | Strip of 10 tablet md | Valid |
| 105078 | Hexinal 2mg Tablet | Strip of 10 tablets | Valid |
| 105867 | Hexyriv 2mg Tablet | Strip of 10 tablets | Valid |
| 138008 | Movahexy 5 Tablet | Strip of 10 tablets | Valid |
| 139118 | Multizine H 2 mg/25 mg/5 mg Tablet | Strip of 10 tablets | Valid |
| 143652 | Manohexy 2mg Tablet | Strip of 10 tablets | Valid |
| 174426 | Parkinta 2mg Tablet | Strip of 10 tablets | Valid |
| 175048 | Parkin Tablet | Strip of 15 tablets | Valid |
| 190325 | Rini 5mg Tablet | Strip of 10 tablets | Valid |
| 217654 | Tris Tablet | Strip of 10 tablets | Valid |
| 217677 | Try Tablet | Strip of 10 tablets | Valid |
| 218176 | Tri EX 2mg Tablet | Strip of 10 tablets | Valid |
| 221815 | Tryhp 5 Tablet | Strip of 10 tablets | Valid |
| 223117 | Trixytin 5mg Tablet | Strip of 10 tablets | Valid |
| 238881 | Vacitane 5mg Tablet | Strip of 10 tablets | Valid |
| 239880 | Vihexy 2mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All products are oral tablets.

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** these include angle-closure and open-angle glaucoma, benign prostatic hyperplasia, myasthenia gravis, paralytic ileus, achalasia, ulcerative colitis and inflammatory bowel disease, coronary artery disease, heart conduction disease, hypertensive and hypotensive disorders, chronic obstructive pulmonary disease, and liver, kidney and gallbladder disease.
- **Drug Interactions:** 107 interactions were identified. The **major** ones in the listed records are with **potassium chloride** and **potassium citrate**. Many **moderate** interactions involve other anticholinergic or gut-motility-affecting drugs, such as atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, trospium, propantheline, loperamide, morphine, metoclopramide, and dronabinol.
- **Population-specific concern:** anticholinergic effects on attention and cognition are a particular worry in ADHD. Ocular risks (mydriasis, angle-closure glaucoma) and a possible lowering of the seizure threshold also apply to some of the other predicted indications.

Package insert warnings and contraindications were not available for this report; please refer to the package insert for label-based safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The ADHD prediction has a very high model score but no clinical trials and no directly relevant literature, and the drug's anticholinergic cognitive effects work against the intended use. The evidence is insufficient to justify moving forward.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA), for example from DrugBank
- Package insert warnings and contraindications from the Indian regulator, which are required before any safety screening
- Preclinical or clinical studies directly testing trihexyphenidyl in ADHD, including its effects on attention and cognition
- If a lower-risk lead is wanted, a closer look at PLA2G6-associated dystonia-parkinsonism as a symptomatic-use research question

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: trihexyphenidyl hydrochloride prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b60ef86c-b8b6-4530-baaf-d4671ce961af) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

