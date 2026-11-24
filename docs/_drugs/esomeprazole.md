---
layout: default
title: Esomeprazole
parent: Model Prediction Only (L5)
nav_order: 323
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "Esomeprazole"
predicted_indications: ["duodenal obstruction"]
description: "Esomeprazole: predicted new indication Duodenal obstruction (evidence level L5). In India: at least 20 listed products"
---

# Esomeprazole
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

## Esomeprazole: Duodenal obstruction
{: .text-alpha }

## One-Sentence Summary

Esomeprazole is a proton pump inhibitor originally used for acid-related conditions such as peptic ulcer disease, gastroesophageal reflux disease (GERD), and Zollinger-Ellison syndrome.
However, there are **0 clinical trials** and only **1 general review article** for this specific indication, so the prediction rests mainly on the model score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Duodenal obstruction |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Esomeprazole suppresses gastric acid secretion by irreversibly inhibiting the H+/K+ ATPase (proton pump) in gastric parietal cells. This description reflects the well-established class pharmacology of proton pump inhibitors. According to the Mechanism of Action section of the US FDA-approved prescribing information for esomeprazole: "Esomeprazole belongs to a class of antisecretory compounds, the substituted benzimidazoles, that suppress gastric acid secretion by specific inhibition of the H+/K+ ATPase enzyme system at the secretory surface of the gastric parietal cell. Esomeprazole is protonated and converted in the acidic compartment of the parietal cell forming the active inhibitor, the achiral sulphenamide." ([DailyMed: Nexium (esomeprazole magnesium) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f4853677-1622-4037-688b-fdf533a11d96), label version 2025-12-19; accessed 2026-11-20.)

Duodenogastric reflux and the drug's original indications are both upper gastrointestinal disorders. The link is plausible but not direct. The main injurious agents in bile reflux are bile and pancreatic secretions, not acid. Acid suppression may therefore relieve symptoms or mucosal injury only indirectly.

It is not disease-specific evidence. The score should be read as a hypothesis, not as confirmation of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | Eur J Clin Pharmacol | General update on proton pump inhibitor use and pharmacokinetics. It covers peptic ulcer, H. pylori infection, GERD, NSAID-related lesions, and Zollinger-Ellison syndrome, but does not address duodenogastric reflux directly. |

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 73350 | Esiloc 20 Tablet | Strip of 10 tablets | Valid |
| 73979 | Esokem 20mg Tablet | Strip of 15 tablets | Valid |
| 74291 | Esmoleaf 40 Tablet | Strip of 10 tablets | Valid |
| 75579 | Esmodity 40mg Tablet | Strip of 10 tablets | Valid |
| 75833 | Esopen 20mg Tablet | Strip of 10 tablets | Valid |
| 75838 | Esolib 40mg Tablet | Strip of 15 tablets | Valid |
| 76756 | Eztop 40mg Tablet | Strip of 10 tablets | Valid |
| 78836 | Esmoden 40 Tablet | Strip of 10 tablets | Valid |
| 79460 | Esoloc 40mg Tablet | Strip of 10 tablets | Valid |
| 80061 | Eslis IT 40mg/150mg Tablet | Strip of 10 tablets | Valid |
| 80357 | Eszomed 40 Injection | Vial of 1 Injection | Valid |
| 80975 | Esomo 40mg Injection | Vial of 1 Injection | Valid |
| 82856 | Esoriv 20mg Tablet | Strip of 10 tablets | Valid |
| 83177 | Esodoc 40mg Tablet | Strip of 10 tablets | Valid |
| 83633 | Esuzole 40 Injection | Vial of 1 Injection | Valid |
| 83656 | Esvelo 40mg Tablet | Strip of 10 tablets | Valid |
| 141782 | Mezon 40mg Injection | Vial of 1 Injection | Valid |
| 163852 | Opec 20mg Tablet | Strip of 10 tablets | Valid |
| 188640 | Raciper 40mg Tablet | Strip of 10 tablets | Valid |
| 252052 | Zpl Injection | Vial of 1 Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All 20 registrations are valid products, available as oral tablets and injectable vials. Only the first 5 are listed here, and approved-indication text was not available for them.

<!-- review:begin in-lic-20261124-esomeprazole-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All 20 registrations are valid single-ingredient products, available as oral tablets and injectable vials." Removed: it described the products as single-ingredient (or as having no combination products), which does not match the Indian medicine data (the Indian Medicine Dataset): some of the recorded products are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124-esomeprazole-1 -->

## Safety Considerations

- **Contraindications / disease associations (from a knowledge graph, not label text):** liver failure, osteoporosis, postmenopausal osteoporosis, bone fracture, chronic atrophic gastritis.
- **Drug Interactions:** 168 known interactions were identified. Examples from the compiled list:
  - **Major:** acalabrutinib, atazanavir.
  - **Moderate:** hydrochlorothiazide, amphotericin B, amikacin, amphetamine, fenofibrate, apalutamide, armodafinil, atorvastatin, bendamustine, bosutinib, bumetanide.
  - **Minor:** acetylsalicylic acid, axitinib, bortezomib, brivaracetam, cyanocobalamin.

Please refer to the package insert for label warnings and full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score and one general review that does not address this condition. There are no clinical trials. Because bile reflux is not acid-driven, esomeprazole's mechanism offers only an indirect rationale.

Note that the same dataset shows far stronger support for a different predicted indication, **duodenal ulcer**. That indication has 30 registered trials, including multiple completed Phase 3 studies, and RCT literature on esomeprazole-based therapy. Duodenal ulcer is closely related to esomeprazole's existing peptic ulcer indication, so it is better viewed as confirmation of an existing use than as true repurposing.

**To proceed, the following is needed:**
- Disease-specific clinical or observational studies of esomeprazole in duodenogastric (bile) reflux.
- Comparison against bile-targeted approaches, to show a benefit beyond acid suppression.
- Package insert warnings and contraindications for the Indian-marketed products.
- Detailed mechanism of action data.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Indian medicine data (the Indian Medicine Dataset used by this site). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-20 | "Detailed mechanism data were not included in the data compiled for this report, so this description reflects the well-established class pharmacology of proton pump inhibitors" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt (revised 2026-11-20; earlier version kept in the record) | [DailyMed: Nexium (esomeprazole magnesium) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f4853677-1622-4037-688b-fdf533a11d96) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

