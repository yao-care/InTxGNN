---
layout: default
title: Metoclopramide
parent: Model Prediction Only (L5)
nav_order: 542
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "Metoclopramide"
predicted_indications: ["gastroduodenitis", "peptic ulcer perforation"]
description: "Metoclopramide: predicted new indication Gastroduodenitis (evidence level L5). In India: at least 20 listed products"
---

# Metoclopramide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Metoclopramide: Gastroduodenitis
{: .text-alpha }

## One-Sentence Summary

Metoclopramide is a prokinetic and antiemetic drug, originally used for gastroesophageal reflux disease and reflux esophagitis.
The TxGNN model predicts it may be useful for **gastric ulcer**, but the support is weak: **1 clinical trial** (a procedural use, not ulcer treatment) and **19 publications**, mostly general reviews.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Metoclopramide is a dopamine D2 antagonist and 5-HT4 agonist. It speeds gastric emptying and improves upper gastrointestinal motility. According to the Mechanism of Action section of the US FDA-approved prescribing information for metoclopramide: "Metoclopramide stimulates motility of the upper gastrointestinal tract without stimulating gastric, biliary, or pancreatic secretions. The exact mechanism of action of metoclopramide in the treatment of gastroesophageal reflux and acute and recurrent diabetic gastroparesis has not been fully established." ([DailyMed: Reglan (metoclopramide hydrochloride) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de55c133-eb08-4a35-91a2-5dc093027397), label version 2026-02-09; accessed 2026-11-19.)

Its approved use in reflux disease relies on this prokinetic effect. In gastric ulcer, the same effect may ease symptoms that often accompany the disease, such as delayed gastric emptying, reflux and nausea. However, metoclopramide does not reduce acid secretion, eradicate *H. pylori* or promote mucosal healing, which are the core ways ulcers are treated. The link to ulcer treatment is therefore symptomatic and adjunctive, not disease-modifying.

One small animal study (PMID 2730234) reported an ulcer-protective effect in rats, but this has not been confirmed in humans.

Other predicted indications are even less well supported:
- Available papers are mostly motility physiology studies and dyspepsia reviews.
- **Gastrojejunal ulcer (0.9978)**: no evidence that it prevents or heals anastomotic ulcers.
- **Peptic ulcer perforation (0.9978)**: no plausible therapeutic role. Perforation is a surgical emergency, and prokinetics may be inappropriate with GI perforation or obstruction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | Unknown | 60 | Metoclopramide premedication in upper GI bleeding, to improve endoscopic visualization and reduce repeat endoscopy. This is a procedural use, not ulcer treatment. |

Only one trial is registered, and its status is unknown. It is peripheral to the predicted indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38059896](https://pubmed.ncbi.nlm.nih.gov/38059896/) | 2024 | RCT | Am J Gastroenterol | Double-blind RCT of IV metoclopramide for gastric visualization in active upper GI bleeding (procedural use) |
| [42259699](https://pubmed.ncbi.nlm.nih.gov/42259699/) | 2026 | RCT | Rev Gastroenterol Mex | Triple-blind RCT of high-dose metoclopramide (20 mg IV) versus placebo for visualization in acute upper GI bleeding; usefulness described as controversial |
| [42127996](https://pubmed.ncbi.nlm.nih.gov/42127996/) | 2026 | Guideline | Endoscopy | ESGE update on endoscopic management of peptic ulcer bleeding; not evidence of metoclopramide efficacy as ulcer therapy |
| [19445547](https://pubmed.ncbi.nlm.nih.gov/19445547/) | 2009 | Systematic review | Paediatr Drugs | Evidence-based review of drug treatment of reflux in children |
| [2568015](https://pubmed.ncbi.nlm.nih.gov/2568015/) | 1989 | Meta-analysis/Review | Scand J Gastroenterol Suppl | Analysis of randomized trials of H2-blockers, antacids and prokinetics in reflux esophagitis; evidence for prokinetics described as weak |
| [786607](https://pubmed.ncbi.nlm.nih.gov/786607/) | 1976 | Review | Drugs | Pharmacology and clinical use of metoclopramide, including easing emergency endoscopy in upper GI haemorrhage |
| [6336644](https://pubmed.ncbi.nlm.nih.gov/6336644/) | 1983 | Review | Ann Intern Med | Pharmacology of metoclopramide: dopamine antagonism, antiemetic and GI motility effects |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | Animal study | Arch Int Pharmacodyn Ther | Ulcer-protective and antisecretory effects of metoclopramide in rat aspirin-induced and pylorus-ligated ulcer models |
| [7886398](https://pubmed.ncbi.nlm.nih.gov/7886398/) | 1994 | Mechanistic study | Scand J Gastroenterol | Effect of cisapride and metoclopramide on human antroduodenal motility |
| [1551349](https://pubmed.ncbi.nlm.nih.gov/1551349/) | 1992 | RCT | Dig Dis Sci | In 20 patients with reflux esophagitis, metoclopramide and domperidone raised lower esophageal sphincter pressure but did not improve esophageal peristalsis or acid clearance |

Most of the retrieved literature consists of general reviews of gastric motility, dyspepsia and gastroparesis. No study directly shows that metoclopramide heals gastric ulcers in humans.

---

## India Market Information

Metoclopramide is currently marketed in India with 20 valid single-ingredient registrations. The approved-indication text was not available for these products.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 3350 | Almet 10mg Tablet | Strip of 10 tablets | Valid |
| 37753 | Copar 5mg/500mg Tablet | Strip of 10 tablets | Valid |
| 38843 | Clopram 25mg Tablet | Strip of 10 tablets | Valid |
| 45042 | Cepar 5mg/500mg Tablet | Strip of 10 tablets | Valid |
| 135132 | Maxeron 10mg Tablet | Strip of 10 tablets | Valid |
| 135370 | Metaclopramide Injection | Vial of 2 ml Injection | Valid |
| 137031 | Metopar Suspension | Bottle of 60 ml Suspension | Valid |
| 138500 | Maxeron Mps 5 mg/125 mg Tablet | Strip of 10 tablets | Valid |
| 139849 | Maxeron 5mg Syrup | Bottle of 30 ml Syrup | Valid |
| 139888 | Metaclop 5mg Injection | Vial of 2 ml Injection | Valid |
| 141262 | Molmet 5mg/500mg Tablet | Strip of 10 tablets | Valid |
| 144318 | Megatech Syrup | Bottle of 200 ml Syrup | Valid |
| 144531 | Metocan P 5mg/500mg Tablet | Strip of 10 tablets | Valid |
| 144698 | Migrosh 5mg/500mg Tablet | Strip of 10 tablets | Valid |
| 152137 | Nutec Plus Tablet | Strip of 10 tablets | Valid |
| 153142 | Norper Tablet | Strip of 10 tablets | Valid |
| 173690 | Paramet Tablet | Strip of 10 tablets | Valid |
| 184313 | Reglan Injection | Ampoule of 2 ml Injection | Valid |
| 189931 | Reg MPS Tablet | Strip of 10 tablets | Valid |
| 233434 | Vominorm 10mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Available forms include tablets, injections, syrups and a suspension. Several registrations are fixed-dose products, such as 5 mg/500 mg tablets; the Indian Medicine Dataset lists a second active ingredient for these products.

<!-- review:begin in-lic-20261124b-metoclopramide-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Several registrations are fixed-dose products, such as 5 mg/500 mg tablets, though the compiled data classify all as single-ingredient." Revised: the sentence said the data classify these products as single-ingredient, but the Indian Medicine Dataset lists a second active ingredient for several of them (they are fixed-dose combinations). Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124b-metoclopramide-1 -->

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not taken from label text): hypertension, epilepsy, pheochromocytoma and paraganglioma, Parkinson disease and parkinsonian disorders, tardive dyskinesia, torsion dystonia, neuroleptic malignant syndrome, active peptic ulcer disease, porphyria, cirrhosis of liver, impaired renal function, anxiety and neurotic disorders, and certain rare metabolic conditions (e.g., pyruvate dehydrogenase E3 deficiency, methemoglobin reductase deficiency).
  - Of note, the graph lists **active peptic ulcer disease** as a contraindication. This directly conflicts with the proposed ulcer indication and needs clarification.
- **Drug interactions**: 670 interactions were recorded. Examples include:
  - **Major**: tramadol, amisulpride
  - **Moderate**: opioids (fentanyl, codeine, dihydrocodeine, alfentanil), alprazolam, amitriptyline, amantadine, cetirizine, chlorpheniramine, ethanol, abiraterone
  - **Minor**: acetaminophen

Please refer to the package insert for label warnings, as these were not available in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model similarity rather than clinical evidence (evidence level L4). The only trial concerns endoscopic visualization during GI bleeding, not ulcer treatment. Metoclopramide has no acid-suppressing, anti-*H. pylori* or mucosal-healing action, and the knowledge graph flags active peptic ulcer disease as a contraindication.

**To proceed, the following is needed:**
- A clear clinical rationale for ulcer-related use, either symptomatic or procedural, with a defined target population (e.g., gastroparesis or delayed emptying alongside ulcer disease)
- Controlled human studies showing a benefit in ulcer outcomes or symptoms
- Resolution of the active peptic ulcer disease contraindication signal
- Package insert warnings and contraindications from the India label (the approved-indication text for the 20 registrations is also missing)
- Detailed mechanism-of-action data
- A safety plan covering neurological risks (tardive dyskinesia, extrapyramidal effects) and the major interactions with tramadol and amisulpride
- Reframing or dropping the lowest-support predictions (peptic ulcer perforation, gastrojejunal ulcer)

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "(Detailed mechanism-of-action data were not available in the data compiled for this report; this description comes from the mechanistic analysis of the predicted indication.)" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Reglan (metoclopramide hydrochloride) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de55c133-eb08-4a35-91a2-5dc093027397) |
| 2026-11-24 | Revised: the single-ingredient classification | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

