---
layout: default
title: Bromocriptine
parent: Model Prediction Only (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bromocriptine: predicted new indication Congenital disorder of glycosylation with defective fucosylation (evidence level L5). Approved use: Parkinson disease, hyperprolactinaemia, acromegaly"
monitor_inn: "Bromocriptine"
predicted_indications: ["congenital disorder of glycosylation with defective fucosylation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "retinal dystrophy with or without extraocular anomalies", "atypical glycine encephalopathy", "myopia 26, X-linked, female-limited", "hydranencephaly (disease)", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "schizophrenia", "syndromic myopia"]
---

# Bromocriptine
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

# Bromocriptine: From Parkinson Disease to Congenital Disorder of Glycosylation with Defective Fucosylation

## One-Sentence Summary

Bromocriptine is a dopamine D2 receptor agonist, originally used for Parkinson disease, hyperprolactinaemia (including prolactin-producing pituitary tumours) and acromegaly.
The TxGNN model ranks **congenital disorder of glycosylation with defective fucosylation** as its top prediction, but there are **0 clinical trials** and **0 publications** supporting it, so this is a model-only signal.
Among the other top-ten predictions, schizophrenia has the most material (1 clinical trial, which targets metabolic comorbidity rather than psychosis itself) and retinal dystrophy has only preclinical and case-level literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease, hyperprolactinaemia, acromegaly (the licence records contain no approved indication text) |
| Predicted New Indication | Congenital disorder of glycosylation with defective fucosylation |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, bromocriptine is a dopamine D2 receptor agonist. Its efficacy in Parkinson disease, hyperprolactinaemia and acromegaly is established, and it acts mainly through dopaminergic signalling.

For the top-ranked prediction, no mechanistic link to fucosylation pathways is known. The very high score (99.83%) reflects graph-based similarity only and should not be read as biological support. The same applies to the other low-ranked predictions with no data, such as polymicrogyria with cerebellar hypoplasia, atypical glycine encephalopathy and hereditary demyelinating neuropathy.

Two other predictions have some plausibility:
- **Retinal dystrophy:** A 2024 preclinical study (PMID 39009597) tested a combination of tamsulosin, metoprolol and bromocriptine in retinopathy models and reported mutation-agnostic efficacy. A 1991 case report treated Goldmann-Favre syndrome with cyclosporin A plus bromocriptine, where the effect of bromocriptine cannot be separated.
- **Schizophrenia:** The dopamine hypothesis points in a mixed direction, because dopamine agonism could worsen psychosis. A 1993 case report (PMID 8120934) describes bromocriptine-induced schizophrenia. The one registered trial looks at metabolic effects, not antipsychotic efficacy.

---

## Clinical Trial Evidence

For the top-ranked prediction (congenital disorder of glycosylation with defective fucosylation), currently no related clinical trials are registered.

For reference, the only trial among the top-ten predictions is for schizophrenia:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03575000](https://clinicaltrials.gov/study/NCT03575000) | Phase 4 | Not yet recruiting | 15 | Open-label pilot of adjunctive bromocriptine for antipsychotic-associated impaired glucose tolerance/insulin resistance in schizophrenia with prediabetes; focuses on safety and tolerability, no controls, no results |

---

## Literature Evidence

For the top-ranked prediction, currently no related literature is available.

For reference, the most relevant items among the other top-ten predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39009597](https://pubmed.ncbi.nlm.nih.gov/39009597/) | 2024 | Preclinical | Nature Communications | Tamsulosin, metoprolol and bromocriptine combination suppressed cAMP and Ca2+ activity and showed mutation-agnostic efficacy in retinopathy models (retinal dystrophy) |
| [1753674](https://pubmed.ncbi.nlm.nih.gov/1753674/) | 1991 | Case report | Klin Monatsbl Augenheilkd | Goldmann-Favre syndrome treated with cyclosporin A and bromocriptine; bromocriptine effect not separable |
| [6574535](https://pubmed.ncbi.nlm.nih.gov/6574535/) | 1983 | Clinical study (10 patients) | Psychiatry Research | Bromocriptine in chronic schizophrenia, with effects on symptoms, sleep and prolactin response (schizophrenia) |
| [8120934](https://pubmed.ncbi.nlm.nih.gov/8120934/) | 1993 | Case report | J Natl Med Assoc | Schizophrenia developed after starting bromocriptine for a macroprolactinoma and resolved after discontinuation (safety signal) |
| [30805732](https://pubmed.ncbi.nlm.nih.gov/30805732/) | 2019 | Review | J Neural Transm | Overview of classical dopamine agonists including bromocriptine (schizophrenia, background) |
| [39265262](https://pubmed.ncbi.nlm.nih.gov/39265262/) | 2024 | Systematic review | Schizophrenia Research | Insulin resistance as a modifiable pathway to cognitive dysfunction in schizophrenia (background) |

---

## India Market Information

Bromocriptine is marketed in India, with 20 valid single-ingredient registrations. The main ones are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 79840 | Encript 5mg Tablet (Micro Labs Ltd) | Strip of 10 tablets | Not stated in the data |
| 75407 | Encript 2.5mg Tablet (Micro Labs Ltd) | Strip of 10 tablets | Not stated in the data |
| 26231 | Brom 2.5mg Tablet (Inga Laboratories) | Strip of 10 tablets | Not stated in the data |
| 37799 | Criptin 2.5mg Tablet (DD Pharmaceuticals) | Strip of 10 tablets | Not stated in the data |
| 29731 | Brom Syrup (Hi Tech Pharmaceuticals) | Bottle of 100 ml syrup | Not stated in the data |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** hypertensive disorders, hypertension, liver disease, gallbladder disease, coronary artery disease, stroke and cerebrovascular disorders, cerebral infarction, and pre-eclampsia (severe, mild) including HELLP syndrome.
- **Drug Interactions:** 87 interactions were identified. Major-level ones include **isometheptene** and **lorcaserin**. Moderate-level ones include morphine, clarithromycin, dronabinol, lansoprazole, metoclopramide, promethazine, ethanol, deferasirox and fostamatinib.
- **Schizophrenia-specific signal:** a case report links bromocriptine to new-onset psychosis, so psychiatric risk needs attention if the schizophrenia direction is pursued.

Please refer to the package insert for further safety information, since label warnings were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction rests only on a graph-model score, with no trials, no literature and no plausible mechanistic link to fucosylation. The evidence level is L5. The schizophrenia direction (the only one with a registered trial) is a research question with a mixed safety direction, and its single trial concerns metabolic comorbidity.

**To proceed, the following is needed:**
- Detailed mechanism of action data for bromocriptine
- Package insert warnings and contraindications from Indian labelling, which are needed for safety screening
- Biological rationale or preclinical data linking dopamine D2 agonism to glycosylation pathways
- If pursuing a lower-ranked option, confirmation of whether bromocriptine is a component in PMID 39009597 and of the evidence quality for retinal dystrophy, or results from NCT03575000 for schizophrenia-related metabolic use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

