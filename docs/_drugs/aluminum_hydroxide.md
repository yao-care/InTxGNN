---
layout: default
title: Aluminum Hydroxide
parent: Model Prediction Only (L5)
nav_order: 43
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Aluminum Hydroxide: predicted new indication Active peptic ulcer disease (evidence level L5). Approved use: Gastric ulcer, peptic ulcer disease, gastroesophageal reflux disease…"
monitor_inn: "Aluminum hydroxide"
predicted_indications: ["gastroduodenitis"]
---

# Aluminum Hydroxide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Aluminum Hydroxide: From Peptic Ulcer Disease to Active Peptic Ulcer Disease

## One-Sentence Summary

Aluminum hydroxide is an antacid originally used for gastric ulcer, peptic ulcer disease, gastroesophageal reflux disease, esophagitis, dyspepsia and duodenal ulcer.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, but this is essentially an existing indication rather than a true new use.
There are **0 registered clinical trials** and **9 publications**, mostly historical or indirect, supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric ulcer, peptic ulcer disease, gastroesophageal reflux disease, esophagitis, dyspepsia, duodenal ulcer (from the knowledge graph; no approved indication text is available in the India licence records) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, aluminum hydroxide is an antacid that neutralizes gastric acid and reduces peptic activity. The supplied literature supports this: antacids containing aluminum hydroxide raise intragastric pH and adsorb pepsin, and they protect the gastric mucosa against damage from agents such as aspirin and ethanol.

Active peptic ulcer disease is closely related to the drug's original indications of gastric ulcer, duodenal ulcer and peptic ulcer disease. The high TxGNN score most likely reflects this existing overlap rather than a new discovery. For this reason, the prediction is better described as a confirmation of an established use than as true repurposing.

Much of the supplied literature concerns sucralfate (an aluminum-containing mucosal protectant), antacid acid-neutralizing capacity, and a nizatidine trial. None of it provides direct modern clinical evidence of aluminum hydroxide for this disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3018068](https://pubmed.ncbi.nlm.nih.gov/3018068/) | 1986 | Clinical physiology study | J Clin Gastroenterol | Compared sodium bicarbonate with aluminum-magnesium hydroxide on postprandial gastric acid in duodenal ulcer patients |
| [3104655](https://pubmed.ncbi.nlm.nih.gov/3104655/) | 1986 | Review | Klin Wochenschr | Aluminum hydroxide antacids prevent gross mucosal necrosis and haemorrhage from aspirin or ethanol, mainly in deeper gastric mucosa |
| [3929601](https://pubmed.ncbi.nlm.nih.gov/3929601/) | 1985 | Mechanistic study (sucralfate) | Am J Med | Aluminum hydroxide moieties inhibit peptic activity by raising pH and adsorbing pepsin |
| [9334882](https://pubmed.ncbi.nlm.nih.gov/9334882/) | 1997 | Animal/in vitro (sucralfate) | Jpn J Pharmacol | Aluminum hydroxide prevented acid- and pepsin-induced damage to rat gastric epithelial cells |
| [35720246](https://pubmed.ncbi.nlm.nih.gov/35720246/) | 2022 | In vitro/product characterization | Med Pharm Rep | Evaluated acid-neutralizing capacity of antacids marketed in Morocco |
| [6798099](https://pubmed.ncbi.nlm.nih.gov/6798099/) | 1981 | Review (sucralfate) | J Clin Gastroenterol | Development of sucralfate, an aluminum salt designed to counteract acid and pepsin |
| [7190055](https://pubmed.ncbi.nlm.nih.gov/7190055/) | 1980 | Review | Brain Res Bull | Restraint-induced ulcers respond to known therapies, including aluminum hydroxide |
| [1526089](https://pubmed.ncbi.nlm.nih.gov/1526089/) | 1992 | RCT (nizatidine vs placebo, not aluminum hydroxide) | Clin Pharmacol Ther | Nizatidine in benign gastric ulcer; does not test aluminum hydroxide |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 212944 | Silicool Oral Suspension Mint Sugar Free | 170 ml bottle, oral suspension | Not stated |
| 195702 | Radocid Oral Suspension | 170 ml bottle, oral suspension | Not stated |
| 22523 | Alzimin Oral Gel | 170 ml bottle, oral gel | Not stated |
| 153745 | Neutral Oral Gel Sugar Free | 170 ml bottle, oral gel | Not stated |
| 4923 | Alumcid MPS Oral Suspension | 170 ml bottle, oral suspension | Not stated |

All 20 registrations are valid single-ingredient products, in oral suspension, gel, syrup, liquid and tablet forms.

## Safety Considerations

- **Drug Interactions**: 205 interactions were recorded. The main ones are:
  - Major: dolutegravir, sodium citrate
  - Moderate: acalabrutinib, doxycycline, alendronic acid, risedronic acid, allopurinol, amphetamine, ascorbic acid, acetylsalicylic acid, atazanavir, proguanil
  - Minor: famotidine, ranitidine, and others
- **Other points from the literature**: Long-term or high-dose use may cause phosphate depletion and bone demineralization or osteomalacia, and acid rebound has been discussed for antacids in general.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Active peptic ulcer disease is effectively an existing indication, so this is not a true repurposing candidate. The high TxGNN score likely reflects the labeled use, and there are no registered trials and no direct modern clinical evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed Indian products
- Detailed mechanism of action data
- Confirmation of the approved indication text for the Indian licences
- Direct controlled clinical evidence, if a formal claim for this indication is intended

**Other predicted indications (for reference):**

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Gastroduodenitis | 99.59% | L4 | Hold; only historical (1949–1962) reports, indirect |
| Gastrojejunal ulcer | 99.54% | L4 | Research question; mechanistically coherent but evidence is indirect and largely old |
| Peptic ulcer perforation | 99.54% | L5 | Hold; no literature, and an antacid has no plausible role in this surgical complication |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

