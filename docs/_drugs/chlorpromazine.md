---
layout: default
title: Chlorpromazine
parent: Model Prediction Only (L5)
nav_order: 176
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Chlorpromazine: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Schizophrenia and related psychotic disorders (manic bipolar affect…"
monitor_inn: "Chlorpromazine"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "congenital disorder of glycosylation with defective fucosylation", "myopia X-linked", "syndromic myopia", "hydranencephaly (disease)", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "myopia 26, X-linked, female-limited", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "atypical glycine encephalopathy"]
---

# Chlorpromazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Chlorpromazine: From Schizophrenia and Other Psychotic Disorders to Retinal dystrophy with or without extraocular anomalies
{: .text-alpha }

## One-Sentence Summary

Chlorpromazine is a long-established antipsychotic, originally used for schizophrenia and related psychotic and manic disorders.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but there are **0 clinical trials** and only **1 publication** (a 1967 case report describing drug-induced phototoxic reactions, which is a safety signal rather than a benefit).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia and related psychotic disorders (manic bipolar affective disorder, schizoaffective disorder, schizophreniform disorder, and others) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for chlorpromazine: "The precise mechanism whereby the therapeutic effects of chlorpromazine are produced is not known. The principal pharmacological actions are psychotropic. It also exerts sedative and antiemetic activity. Chlorpromazine has actions at all levels of the central nervous system –primarily at subcortical levels – as well as on multiple organ systems." ([DailyMed: chlorpromazine prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bd02d051-2a34-4cd3-a137-b965c0381267), label version 2026-11-10; accessed 2026-11-19.) Chlorpromazine is a phenothiazine antipsychotic, generally understood to act mainly through dopamine D2 receptor antagonism. Its efficacy in psychotic disorders is well established.

The prediction is **not well supported**. The only supporting record is a 1967 report of phototoxic reactions induced by high doses of chlorpromazine and thioridazine. That report documents drug-induced ocular toxicity, a safety concern, and not a therapeutic effect. No plausible mechanism has been identified by which chlorpromazine would treat inherited retinal degeneration. The high TxGNN score therefore appears to be a model artefact, and the available literature points to potential harm in retinal disease.

Other top-ranked predictions show the same pattern. None of the eight highest-ranked predictions (retinal dystrophy, congenital disorder of glycosylation with defective fucosylation, three myopia entries, hydranencephaly, a polymicrogyria syndrome, Charcot-Marie-Tooth type 1G, atypical glycine encephalopathy) has any clinical trial or literature support, apart from the retinal dystrophy case report above. For the myopia entries, dopamine antagonism would be expected to be unhelpful or counterproductive. The rank-10 prediction, early-onset schizophrenia, is largely an on-label extension and not true repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5336672](https://pubmed.ncbi.nlm.nih.gov/5336672/) | 1967 | Case report / toxicology observation | JAMA | Phototoxic reactions induced by high doses of chlorpromazine and thioridazine. This is a safety signal, not evidence of therapeutic benefit. No abstract available. |

## India Market Information

Approved indication text is not available for these registrations.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 35727 | Chlorpromazine Hydrochloride Tablet | Strip of 10 tablets | Valid |
| 44630 | Chlorotame 50mg Tablet | Strip of 10 tablets | Valid |
| 48561 | Clozine 200mg Tablet | Strip of 10 tablets | Valid |
| 56604 | Chlorectil Plus 200mg/2mg Tablet | Strip of 10 tablets | Valid |
| 74602 | Emetil 100mg Tablet | Strip of 10 tablets | Valid |
| 75742 | Elicalm SF Tablet | Strip of 10 tablets | Valid |
| 157636 | Normacalm Forte 50 mg/2 mg/5 mg Tablet | Strip of 10 tablets | Valid |
| 168832 | Ostil 5mg Tablet | Strip of 10 tablets | Valid |
| 171799 | Ostil Plus 100mg/2mg Tablet | Strip of 10 tablets | Valid |
| 186848 | Relitil 25mg Tablet | Strip of 10 tablets | Valid |
| 188795 | Relitil 50mg Tablet | Strip of 10 tablets | Valid |
| 201920 | Sun Prazin 100mg Tablet | Strip of 10 tablets | Valid |
| 211853 | Selocalm Forte Tablet | Strip of 10 tablets | Valid |
| 215281 | Trinicalm Forte Tablet | Strip of 15 tablets | Valid |
| 218175 | Teem H Forte 25mg/2mg/5mg Tablet | Strip of 10 tablets | Valid |
| 220112 | Tranchlor 25mg Tablet | Strip of 10 tablets | Valid |
| 221236 | Talentil 100mg Tablet | Strip of 10 tablets | Valid |
| 222806 | Trinex C 50 mg Tablet | Strip of 10 tablets | Valid |
| 225063 | Talentil Plus 100 mg/2 mg Tablet | Strip of 10 tablets | Valid |
| 225579 | Trytil 50mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All 20 registrations are valid oral tablet products, with none cancelled. Several are fixed-dose combination brands with other ingredients (e.g., Chlorectil Plus, Ostil Plus, Normacalm Forte).

## Cytotoxicity

Not applicable. Chlorpromazine is not an antineoplastic drug.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for label-based safety information.

- **Contraindication signals (from a knowledge graph, not label text)**: The following disease associations were flagged:
  - **Cardiac**: long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease, myocardial infarction and coronary thrombosis.
  - **Blood**: neutropenia, agranulocytosis, leukopenia, thrombocytopenia, anemia (including macrocytic anemia), hemoglobinopathy.
  - **Neurological**: epilepsy, basal ganglia disease, focal hand dystonia, blepharospasm, multiple system atrophy.
  - **Blood pressure and autonomic**: orthostatic hypotension, postural orthostatic tachycardia syndrome.
  - **Liver and gallbladder**: liver disease, gallbladder disease.
  - **Metabolic**: hyperglycemia, obesity disorder, monogenic obesity.
  - **Other**: benign prostatic hyperplasia, substance abuse/dependence, female breast carcinoma.
- **Drug Interactions**: 315 interactions were recorded, and the 20 listed in the data include two **Major** ones:
  - **Bupropion**
  - **Morphine**

  Moderate interactions include:
  - Antidiabetic agents (metformin, pioglitazone, alogliptin, canagliflozin, acarbose, albiglutide, chlorpropamide)
  - Anticholinergics (atropine, hyoscyamine, glycopyrronium)
  - Others (epinephrine, hydrocortisone, famotidine, amphotericin B, loperamide, lorcaserin, bisacodyl)
- **Ocular signal**: The only literature on the predicted indication reports phototoxic and ocular adverse effects at high doses.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score alone, and the single supporting publication describes drug-induced toxicity and not benefit. There are no clinical trials, no plausible mechanism, and a potential harm signal in the retina.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India-marketed products (a blocking gap for safety screening)
- Detailed mechanism of action data, and a mechanistic rationale connecting chlorpromazine to retinal dystrophy pathology
- Preclinical evidence (e.g., retinal degeneration models) showing benefit and not toxicity
- A review of ocular and phototoxicity risk, since retinal toxicity is a known concern

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: chlorpromazine prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bd02d051-2a34-4cd3-a137-b965c0381267) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

