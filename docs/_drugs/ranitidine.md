---
layout: default
title: Ranitidine
parent: Model Prediction Only (L5)
nav_order: 726
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "Ranitidine"
predicted_indications: ["peptic ulcer perforation", "duodenal obstruction", "gastroduodenitis", "Smouldering systemic mastocytosis", "abnormality of glucagon secretion", "lymphoadenopathic mastocytosis with eosinophilia"]
description: "Ranitidine: predicted new indication Peptic ulcer perforation (evidence level L5). In India: at least 20 listed products"
---

# Ranitidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Ranitidine: Peptic ulcer perforation
{: .text-alpha }

## One-Sentence Summary

Ranitidine is a histamine H2-receptor antagonist that reduces gastric acid secretion and is marketed in India as a single-ingredient product.
The TxGNN model predicts it may be useful for **peptic ulcer perforation**, but no clinical trial is registered and none of the supplied publications tests ranitidine as a treatment for this condition, so the evidence level is **L5** (model prediction only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Peptic ulcer perforation |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for ranitidine: "Ranitidine Tablets are a competitive, reversible inhibitor of the action of histamine at the histamine H 2 -receptors, including receptors on the gastric cells. Ranitidine Tablets do not lower serum Ca ++ in hypercalcemic states." ([DailyMed: ranitidine prescribing information, Atland Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fcf27c99-8bd4-41fb-bff8-38fed9de76d9), label version 2026-09-24; accessed 2026-11-19.) Ranitidine belongs to the H2-receptor antagonist class, whose general effect is to lower gastric acid output. Acid suppression is established as helpful for ulcer healing and for preventing ulcer recurrence. Long-term H2-antagonist therapy has been reviewed as reducing relapse and, in one review, the risk of complications (PMIDs 8364140 and 8103373).

The link to perforation is weak, however. Perforation is an acute surgical complication, and acid suppression does not treat it. At most, ranitidine could play an adjunct or secondary-prevention role, for example in protecting high-risk patients or supporting healing after repair. The supplied studies do not show such a benefit directly. The one randomized trial on perforated ulcer (PMID 2927479) compared nonoperative management with emergency surgery and did not test ranitidine specifically. The prediction therefore rests mainly on the model score and a plausible but indirect mechanistic argument.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2927479](https://pubmed.ncbi.nlm.nih.gov/2927479/) | 1989 | RCT | N Engl J Med | 83 patients with suspected perforated peptic ulcer were randomized to nonoperative treatment or emergency surgery. Not ranitidine-specific. |
| [7861219](https://pubmed.ncbi.nlm.nih.gov/7861219/) | 1995 | RCT | J Neurosurg | 101 high-risk neurosurgical patients received ranitidine 50 mg every 6 hours or placebo to prevent postoperative gastroduodenal bleeding and/or perforation. This tested prevention in a different setting, not treatment of perforated ulcer. |
| [11488789](https://pubmed.ncbi.nlm.nih.gov/11488789/) | 2001 | Retrospective and randomized studies | Br J Surg | Examined the effect of H. pylori eradication on ulcer recurrence after simple closure of perforated duodenal ulcer. Not ranitidine-specific. |
| [8364140](https://pubmed.ncbi.nlm.nih.gov/8364140/) | 1993 | Review of controlled trials | Aliment Pharmacol Ther | Continuous H2-antagonist therapy reduces ulcer recurrence. Relapse rates vary with study design. |
| [8103373](https://pubmed.ncbi.nlm.nih.gov/8103373/) | 1993 | Review | Aliment Pharmacol Ther | Long-term H2-antagonist treatment aims to prevent painful recurrence and to reduce the risk of complications such as haemorrhage and perforation. |
| [8346951](https://pubmed.ncbi.nlm.nih.gov/8346951/) | 1993 | Clinical study | Arch Dis Child | Intravenous ranitidine at different doses was assessed for its effect on intragastric pH in 10 preterm infants on dexamethasone, who are at risk of gastric perforation. |
| [11871831](https://pubmed.ncbi.nlm.nih.gov/11871831/) | 2002 | Clinical study | Indian J Gastroenterol | Studied H. pylori infection in patients operated on for perforated duodenal ulcer and its effect on ulcer healing. |
| [1679675](https://pubmed.ncbi.nlm.nih.gov/1679675/) | 1991 | Review | Aliment Pharmacol Ther | Therapeutic recommendations for NSAID-induced gastroduodenal injury, a cause of bleeding and perforation. |
| [9260785](https://pubmed.ncbi.nlm.nih.gov/9260785/) | 1997 | Review | Am J Gastroenterol | H. pylori and NSAIDs cause almost all gastric and duodenal ulcers. Therapy is moving from acid suppression alone toward addressing causes. |
| [8781800](https://pubmed.ncbi.nlm.nih.gov/8781800/) | 1996 | Case report | Endoscopy | A very rare case of a gastric ulcer penetrating the pericardium and heart. |

## India Market Information

Ranitidine is currently marketed in India. The data compiled for this report show valid licences (one of them, Magnet 150mg/200mg Tablet, combines ranitidine with magaldrate) and no cancelled ones. The records may be partial; approved indication text is not recorded in the local data.

<!-- review:begin in-lic-20261124b-ranitidine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The data compiled for this report show 20 valid single-ingredient licences and no cancelled ones. The records may be partial. The table lists five main authorizations; approved indication text is not recorded in the local data." Revised: the sentence referred to the earlier table on this page, which showed only some of the products, and described other products as additional, further, remaining or not shown. The product table under India Market Information now lists every product held in the data, so that relative wording and the hard-coded counts were dropped; current figures are in the Quick Overview and that table. The sentence also described the products as single-ingredient, but the Indian Medicine Dataset lists a second active ingredient for some of them. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124b-ranitidine-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 18467 | Ancid 150mg Syrup | Bottle of 170 ml Syrup | Valid |
| 96621 | Glentac 300mg Tablet | Strip of 30 tablets | Valid |
| 110584 | Intac 150mg Tablet | Strip of 10 tablets | Valid |
| 135008 | Magnet 150mg/200mg Tablet | Strip of 10 tablets | Valid |
| 184342 | Rantidine 150mg Tablet | Strip of 10 tablets | Valid |
| 185026 | Rantid 150mg Tablet | Strip of 10 tablets | Valid |
| 185119 | Ranitin 300 Tablet | Strip of 10 tablets | Valid |
| 185430 | R-Loc 50mg Injection 2ml | Packet of 14 injections | Valid |
| 185680 | Ranitac 150mg Tablet | Strip of 10 tablets | Valid |
| 185702 | Ranitin 50mg Injection | Vial of 2 ml Injection | Valid |
| 185893 | Ranial 150mg Tablet | Strip of 10 tablets | Valid |
| 187093 | Raniday Tablet | Strip of 10 tablets | Valid |
| 188440 | Ranitin 300 Tablet | Strip of 20 tablets | Valid |
| 188604 | Ranicool 150mg Tablet | Strip of 10 tablets | Valid |
| 192532 | Rantime 25mg Injection | Vial of 2 ml Injection | Valid |
| 193730 | Reltac 300mg Tablet | Strip of 10 tablets | Valid |
| 197034 | Ranisac 150mg Tablet | Strip of 10 tablets | Valid |
| 197336 | Raninett 25mg Injection | Vial of 2 ml Injection | Valid |
| 198948 | Ranimac 25mg Injection | Vial of 30 ml Injection | Valid |
| 221308 | Tinadin 150mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: The interaction query found 585 recorded interactions. Examples in the supplied list include:
  - **Major**: atazanavir.
  - **Moderate**: acalabrutinib, acetohexamide, aminophylline, bosutinib, brigatinib, ceritinib, chlorpropamide, and several cephalosporins (cefditoren, cefpodoxime, cefuroxime).
  - **Minor**: acetaminophen, alendronic acid, aluminum hydroxide, calcium carbonate, cisapride.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The evidence level is L5. No registered trial and no supplied study tests ranitidine as a treatment for peptic ulcer perforation. The randomized trial of ranitidine (PMID 7861219) looked at prevention of postoperative gastroduodenal bleeding in neurosurgical patients. Perforation is an acute surgical event that acid suppression does not treat, so the mechanistic link is indirect.

**To proceed, the following is needed:**
- Mechanism of action data for ranitidine.
- Clinical studies that define a specific role, such as adjunct therapy after perforation repair or prevention in high-risk patients, and test ranitidine directly in that role.
- Package insert warnings and contraindications for safety screening.
- Review of the interaction profile, especially the major interaction with atazanavir, if a study is planned.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: ranitidine prescribing information, Atland Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fcf27c99-8bd4-41fb-bff8-38fed9de76d9) |
| 2026-11-24 | Revised: wording about the earlier partial table and the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

