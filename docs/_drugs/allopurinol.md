---
layout: default
title: Allopurinol
parent: Model Prediction Only (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
monitor_inn: "Allopurinol"
predicted_indications: ["hepatic porphyria", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "primitive portal vein thrombosis", "hepatoportal sclerosis", "idiopathic copper-associated cirrhosis", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "idiopathic eosinophilic myositis"]
last_modified_at: 2026-11-24
description: "Allopurinol: predicted new indication hepatic porphyria (evidence level L5). In India: at least 20 listed products"
---

# Allopurinol
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

## Allopurinol: xanthine oxidase inhibitor → hepatic porphyria
{: .text-alpha }

## One-Sentence Summary

Allopurinol is a xanthine oxidase inhibitor that is marketed in India as single-ingredient tablets and capsules.
The TxGNN model predicts it may be effective for **hepatic porphyria**, but this rests on a high model score alone, with **0 clinical trials** and **2 indirect publications** (a hypothesis paper and a rat study) supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | hepatic porphyria |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for allopurinol: "Allopurinol is a structural analogue of the natural purine base, hypoxanthine. Allopurinol and its oxypurinol metabolite inhibitor xanthine oxidase, the enzyme responsible for the conversion of hypoxanthine to xanthine and of xanthine to uric acid, the end product of purine metabolism in humans." ([DailyMed: Aloprim (allopurinol) prescribing information, Mylan Institutional LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=10cc918f-aa44-415b-932d-2404695ac449), label version 2022-02-18; accessed 2026-11-19.) Allopurinol is generally known as a xanthine oxidase inhibitor that lowers uric acid production, but the data compiled for this report do not describe its mechanism, so its link to hepatic porphyria cannot be established from them.

The support for this prediction is indirect. A 2019 hypothesis paper proposes metabolic targeting of 5-aminolevulinate synthase (ALAS1), the rate-limiting enzyme of haem synthesis, as a way to treat acute hepatic porphyrias. A 1992 rat study examined how carbamazepine affects haem metabolism in the liver in relation to porphyria exacerbation. Neither paper studies allopurinol as a treatment for hepatic porphyria in patients.

Porphyria patients are also sensitive to many drugs that induce ALAS1, so any use would need a careful review of whether the drug can provoke porphyric attacks. The very high model score is a computational signal only, not evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis/Review | Medical Hypotheses | Proposes lowering the demand on the liver haem pool, via tryptophan or inhibition of tryptophan 2,3-dioxygenase, to reduce ALAS1 induction in acute hepatic porphyrias; allopurinol is not shown to be tested |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Animal study (rat) | Biochemical Pharmacology | Very low-dose carbamazepine altered haem metabolism in rat liver, relevant to how drugs worsen hepatic porphyrias |

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 3556 | Allopurizol 300 Tablet | Strip of 10 tablets | Valid |
| 13090 | Alur 100mg Tablet | Strip of 10 tablets | Valid |
| 16043 | Ausric 300 Tablet | Strip of 10 tablets | Valid |
| 20861 | Allric 100mg Tablet | Strip of 10 tablets | Valid |
| 21521 | Aluzit 100 Tablet | Strip of 10 tablets | Valid |
| 35830 | Ciploric 300 Tablet | Strip of 10 tablets | Valid |
| 118335 | Kayloric 100mg Tablet | Strip of 10 tablets | Valid |
| 122102 | Logout 100mg Tablet | Strip of 10 tablets | Valid |
| 126377 | Lodiric-SR 250mg Capsule | Strip of 10 capsule sr | Valid |
| 146100 | Mecnol 300mg Tablet | Strip of 10 tablets | Valid |
| 157821 | Niloric 100mg Tablet | Strip of 10 tablets | Valid |
| 160532 | Neoall 300mg Tablet | Strip of 10 tablets | Valid |
| 188437 | Rapinol 300mg Tablet | Strip of 10 tablets | Valid |
| 192549 | Ricdol 300mg Tablet SR | Strip of 10 tablet sr | Valid |
| 232953 | Urokret 100mg Tablet | Strip of 10 tablets | Valid |
| 235796 | Vriloric 100mg Tablet | Strip of 10 tablets | Valid |
| 246755 | Zyrik 300 Tablet | Strip of 10 tablets | Valid |
| 250406 | Zylotis 100 Tablet | Strip of 10 tablets | Valid |
| 250865 | Zyronic 100mg Tablet | Strip of 10 tablets | Valid |
| 251175 | Zyrinol 100mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

The list shows 5 of the records compiled for this report and may be partial. All 20 records are valid single-ingredient licences, and none of them carries indication text.

## Safety Considerations

- **Drug Interactions**: 217 interacting drugs were identified in the interaction query. Moderate-level interactions include aluminum hydroxide, attapulgite, kaolin, magaldrate and sucralfate. Minor-level interactions include amoxicillin and chlorpropamide. Many others, such as metformin, omeprazole, glimepiride and morphine, have an unclassified level.
- **Porphyria-specific concern**: Patients with hepatic porphyria are sensitive to drugs that induce haem-pathway enzymes, so the porphyrinogenic potential of allopurinol would need dedicated review before any use.

Please refer to the package insert for further safety information, since label warnings and contraindications were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials and no study that tests allopurinol in hepatic porphyria. The two publications are a hypothesis paper and a rat study with only an indirect link, so the evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data linking allopurinol to haem biosynthesis or ALAS1 regulation
- A porphyrinogenicity review, including preclinical haem-pathway testing
- Package insert warnings and contraindications from the India label
- Any human case or clinical data on allopurinol use in hepatic porphyria

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Aloprim (allopurinol) prescribing information, Mylan Institutional LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=10cc918f-aa44-415b-932d-2404695ac449) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

