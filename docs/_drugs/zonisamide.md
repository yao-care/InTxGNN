---
layout: default
title: Zonisamide
parent: Model Prediction Only (L5)
nav_order: 912
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Zonisamide: predicted new indication Tourette syndrome (evidence level L5). Approved use: Not stated in the Indian license records compiled for this report (zo…"
---

# Zonisamide
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

# Zonisamide: From Epilepsy to Tourette Syndrome

## One-Sentence Summary

Zonisamide is an anticonvulsant (antiseizure) drug that is marketed in India in capsule and tablet forms.
The TxGNN model predicts it may be effective for **Tourette syndrome**, but this is a model prediction only, with **no clinical trials** and **no publications** currently supporting it.
Among the other top-ranked predictions, **absence epilepsy** has the most supporting literature, although it is closer to an extension of the existing epilepsy use than a true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Indian license records compiled for this report (zonisamide is a known antiseizure medication) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 13 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, zonisamide is an antiseizure drug that is thought to block voltage-gated sodium channels and T-type calcium channels and to modulate dopaminergic and serotonergic transmission. Its efficacy in epilepsy is established, and these effects could plausibly relate to the circuits involved in tics.

The prediction should be read with caution. A pragmatic review (PMID 36005856) reports that antiseizure medications can induce obsessive-compulsive and tic disorders, which points to a possible safety concern rather than support for benefit in Tourette syndrome. The TxGNN score is high, but no trial or publication directly supports this indication.

Other predictions in the top 10 differ in strength:
- **Absence epilepsy (score 99.24%, Evidence Level L3):** The most credible of the group. T-type calcium channel blockade is the same mechanism that underlies absence seizures and the action of ethosuximide. Evidence consists of small uncontrolled or retrospective studies. Because zonisamide is already used in epilepsy, this is a niche or adjunctive use rather than new repurposing.
- **Manic bipolar affective disorder (score 99.35%, Evidence Level L4):** The evidence is mixed. An open-label-type report exists in bipolar depression, but there is also a report of zonisamide-induced mania.
- **Fibromyalgia (score 99.20%, Evidence Level L5):** The only trial was withdrawn with zero enrollment.
- **Trichotillomania, Prinzmetal angina, conjunctivitis:** Prediction only, with speculative or implausible mechanistic links.
- **Methemoglobinemia (including alpha type) and methemoglobin reductase deficiency:** No plausible mechanism. These scores probably reflect shared graph neighbours, and sulfonamides are more often linked to hematologic risk than benefit.

## Clinical Trial Evidence

Currently no related clinical trials are registered for Tourette syndrome.

For reference, the only trial found among the top 10 predictions concerns fibromyalgia:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00259636](https://clinicaltrials.gov/study/NCT00259636) | Phase 4 | Withdrawn | 0 | Zonisamide vs placebo in patients with fibromyalgia and migraine; withdrawn with no participants, so no efficacy or safety data |

## Literature Evidence

Currently no related literature is available for Tourette syndrome.

The most relevant publications found for related predictions are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36005856](https://pubmed.ncbi.nlm.nih.gov/36005856/) | 2022 | Review | Expert Rev Neurother | Antiseizure medication-induced obsessive-compulsive and tic disorders; a possible safety concern for the Tourette prediction |
| [35363878](https://pubmed.ncbi.nlm.nih.gov/35363878/) | 2022 | Network meta-analysis | Cochrane Database Syst Rev | Antiepileptic drug monotherapy for epilepsy (general, not zonisamide-specific) |
| [23350722](https://pubmed.ncbi.nlm.nih.gov/23350722/) | 2013 | Evidence review (ILAE) | Epilepsia | Efficacy of antiepileptic drugs as initial monotherapy for epileptic seizures and syndromes |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Practice guideline | Neurology | AAN/AES guideline update on new antiepileptic drugs in new-onset epilepsy |
| [15847848](https://pubmed.ncbi.nlm.nih.gov/15847848/) | 2005 | Chart review | Epilepsy Res | In 45 patients aged 18 or under with absence seizures, 51.1% became seizure-free on zonisamide |
| [24907183](https://pubmed.ncbi.nlm.nih.gov/24907183/) | 2014 | Case series | Epilepsy Res | Zonisamide in drug-resistant juvenile absence epilepsy |
| [15634623](https://pubmed.ncbi.nlm.nih.gov/15634623/) | 2004 | Retrospective study | Epileptic Disord | Efficacy and tolerability of zonisamide in 15 patients with juvenile myoclonic epilepsy |
| [17163811](https://pubmed.ncbi.nlm.nih.gov/17163811/) | 2007 | Clinical study (open-label pilot) | Expert Opin Pharmacother | Zonisamide for bipolar depression, evaluating effectiveness, tolerability and switch to mania |
| [2109869](https://pubmed.ncbi.nlm.nih.gov/2109869/) | 1990 | Case report | Psychosomatics | Zonisamide-induced mania |
| [22575611](https://pubmed.ncbi.nlm.nih.gov/22575611/) | 2013 | Systematic review | Int J Neuropsychopharmacol | Anticonvulsants in acute bipolar depression (RCT-based review) |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 10380 | Asmide 100mg Capsule (Asterisk Laboratories) | Strip of 10 capsules | Not stated in the records |
| 248467 | Zonit 100mg Capsule (Torrent) | Strip of 10 capsules | Not stated in the records |
| 246646 | Zonegran Tablet (Eisai) | Strip of 10 tablets | Not stated in the records |
| 246678 | Zonisep 100 Capsule (Sun Pharma) | Strip of 10 capsules | Not stated in the records |
| 247095 | Zonimid 100 Capsule (Intas) | Strip of 10 capsules | Not stated in the records |

There are 13 valid single-ingredient registrations in total, in oral capsule and tablet forms.

## Safety Considerations

- **Contraindications flagged in the drug-disease knowledge graph (not label text):** The graph links zonisamide to a number of conditions, including:
  - Psychiatric: anxiety disorder, psychotic disorder, schizoaffective disorder, dysthymic disorder
  - Kidney and liver: kidney disease, nephrolithiasis, liver disease, gallbladder disease
  - Metabolic: metabolic acidosis
  - Hematologic: agranulocytosis and neutropenia (including several congenital forms)
- **Psychiatric and neurological signals in the literature:** A report of zonisamide-induced mania (PMID 2109869) and a review of antiseizure medication-induced obsessive-compulsive and tic disorders (PMID 36005856).
- **Sulfonamide class:** Zonisamide is a sulfonamide, which is generally associated with hematologic and oxidative risk. This is relevant to the methemoglobinemia predictions.
- **Drug Interactions:** 154 interactions were recorded. Major-level interactions include:
  - Anticholinergics: atropine, scopolamine, hyoscyamine, methscopolamine, glycopyrronium, dicyclomine, clidinium, trospium, mepenzolate, propantheline
  - Metformin
  
  Moderate-level interactions include aprepitant, morphine, dexamethasone, cimetidine, clarithromycin, dronabinol, nabilone, metoclopramide and miconazole.

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Tourette syndrome prediction rests on the model score alone, with no trials or publications, and the only related literature raises a possible tic-inducing concern. Zonisamide's safety profile also includes psychiatric and hematologic signals that need careful assessment before any new use is pursued.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator or manufacturers
- Detailed mechanism of action data (for example, from DrugBank)
- Approved indication text for the Indian licenses, to confirm the original indication
- Preclinical or clinical evidence specific to Tourette syndrome, with a focus on tic-related safety
- If a more evidence-supported direction is wanted, a separate assessment of **absence epilepsy** (Evidence Level L3), recognizing that it is largely an extension of the existing epilepsy use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

