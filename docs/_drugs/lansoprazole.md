---
layout: default
title: Lansoprazole
parent: Model Prediction Only (L5)
nav_order: 471
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "Lansoprazole"
predicted_indications: ["duodenal obstruction"]
description: "Lansoprazole: predicted new indication Duodenal obstruction (evidence level L5). In India: at least 20 listed products"
---

# Lansoprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Lansoprazole: Duodenal obstruction
{: .text-alpha }

## One-Sentence Summary

Lansoprazole is a proton pump inhibitor originally used to treat gastric and duodenal ulcers, gastroesophageal reflux disease, esophagitis, and Zollinger-Ellison syndrome.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Duodenal obstruction |
| TxGNN Prediction Score | 0.9968 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for lansoprazole: "Lansoprazole belongs to a class of antisecretory compounds, the substituted benzimidazoles, that suppress gastric acid secretion by specific inhibition of the (H +, K + )-ATPase enzyme system at the secretory surface of the gastric parietal cell. Because this enzyme system is regarded as the acid (proton) pump within the parietal cell, lansoprazole has been characterized as a gastric acid-pump inhibitor, in that it blocks the final step of acid production." ([DailyMed: Prevacid (lansoprazole) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=71ba78cb-7e46-43eb-9425-fa130f537f84), label version 2025-07-08; accessed 2026-11-19.) Based on general knowledge, lansoprazole is a proton pump inhibitor that suppresses gastric acid secretion, and its efficacy in acid-related upper gastrointestinal disease is well established.

Duodenogastric (bile) reflux is the backflow of duodenal contents, including bile and pancreatic fluid, into the stomach. Acid suppression may reduce mucosal injury and symptoms when acid and bile act together. However, lansoprazole does not stop the reflux itself and does not neutralize bile acids, so the mechanistic link is indirect and symptomatic at best.

The high TxGNN score likely reflects the close pathophysiological and network proximity of this condition to lansoprazole's existing indications (GERD, esophagitis, peptic ulcer), not independent clinical evidence.

A second prediction, duodenal obstruction (score 0.9968), was also generated. It has no identified mechanistic rationale, no trials, and no literature. Obstruction is mainly a mechanical or structural problem, and lansoprazole would at most be an adjunct for associated peptic disease. This prediction is not pursued further here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | European Journal of Clinical Pharmacology | General update on PPI clinical use and pharmacokinetics (peptic ulcer, H. pylori, GERD, NSAID-related lesions, Zollinger-Ellison syndrome). Not specific to duodenogastric reflux. |

## India Market Information

Twenty valid single-ingredient licences are registered and none are cancelled. The approved indication text is not available for any of them.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 25600 | Aumanso 30mg Capsule | Strip of 10 capsules | Valid |
| 65397 | Dazdom Junior 15mg Tablet | Strip of 10 tablets | Valid |
| 113876 | Junior Lanzol 30mg Tablet DT | Strip of 10 tablet dt | Valid |
| 124137 | Lanzomed 15mg Tablet DT | Strip of 10 tablet dt | Valid |
| 124450 | Lansopress Kid 15mg Tablet DT | Strip of 10 tablet dt | Valid |
| 125632 | L Pro 15mg Tablet | Strip of 10 tablets | Valid |
| 127064 | Lonido 30mg Capsule | Strip of 10 capsules | Valid |
| 127067 | Lansoz 30mg Capsule | Strip of 10 capsules | Valid |
| 129207 | L Cid Junior 30mg Tablet | Strip of 10 tablets | Valid |
| 129378 | Lanzorun 15mg Tablet DT | Strip of 10 tablet dt | Valid |
| 130303 | Lantic 30mg Tablet | Strip of 10 tablets | Valid |
| 130379 | Lancron 30mg Capsule | Strip of 10 capsules | Valid |
| 130532 | Lansotaj 30mg Injection | Vial of 1 Powder for Injection | Valid |
| 130682 | Lansoford 30mg Tablet | Strip of 10 tablets | Valid |
| 130722 | Lanzosten 15mg Tablet DT | Strip of 10 tablet dt | Valid |
| 133126 | Lanprosh 30mg Capsule | Strip of 10 capsules | Valid |
| 175609 | Pep 30mg Capsule | Strip of 10 capsules | Valid |
| 178856 | Prozer 30mg Tablet | Strip of 10 tablets | Valid |
| 241729 | Waypra-Kid Tablet MD | Strip of 10 tablet md | Valid |
| 250590 | Zopra 30mg Capsule | Strip of 10 capsules | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Available forms include oral tablets, dispersible tablets, capsules and an injectable powder.

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** These are graph-derived associations and not confirmed label contraindications. They include long QT syndrome, torsades de pointes, liver failure and liver disease, kidney disease, porphyria, congestive heart failure, myocardial infarction, stroke and cerebrovascular disorders, osteoporosis, blood coagulation disease, anaemia, *Clostridium difficile* colitis, and myasthenia gravis.
- **Drug Interactions:** 618 interactions were recorded. Examples:
  - **Major:** acalabrutinib, atazanavir.
  - **Moderate:** hydrochlorothiazide, amphotericin B, amikacin, amphetamine, fenofibrate, apalutamide, aprepitant, atorvastatin, bosutinib, brigatinib, bromocriptine.
  - **Minor:** acetylsalicylic acid, axitinib, brivaracetam, cyanocobalamin.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on model score and proximity to existing indications. There are no trials, the single review is not condition-specific, and the mechanism is indirect and symptomatic. Package insert safety data is also missing.

**To proceed, the following is needed:**
- Condition-specific clinical studies of PPIs (including lansoprazole) in duodenogastric or bile reflux
- Mechanism of action data from DrugBank
- Package insert warnings and contraindications for the Indian products, to allow safety screening
- Approved indication text for the Indian licences
- Review of the knowledge-graph contraindication signals against label information

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Prevacid (lansoprazole) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=71ba78cb-7e46-43eb-9425-fa130f537f84) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

