---
layout: default
title: Sucralfate
parent: 僅模型預測 (L5)
nav_order: 787
evidence_level: L5
indication_count: 2
---

# Sucralfate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Sucralfate: From Duodenal Ulcer to Duodenogastric Reflux

## One-Sentence Summary

> Sucralfate is a mucosal protectant traditionally used to treat and heal duodenal (peptic) ulcers.
> The TxGNN model predicts it may also be effective for **Duodenogastric Reflux** (bile/alkaline reflux gastritis),
> with **0 registered clinical trials** but **14 supporting publications**, including several older randomized controlled trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Duodenal ulcer (peptic ulcer disease) — based on established clinical use; formal local approval text unavailable (see Data Gap DG001/DG002) |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L3 (multiple completed randomized trials on closely related alkaline/bile reflux gastritis, but no phase-labeled or currently registered trials) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Sucralfate is a **mucosal protectant / cytoprotective agent** that forms a viscous, adherent barrier over damaged gastrointestinal mucosa, binds bile acids and pepsin, and reduces further mucosal injury. Its efficacy in **duodenal ulcer** healing is well established and is the basis of its original approval.

Duodenal ulcer and duodenogastric reflux (bile reflux gastritis) share overlapping pathophysiology: both involve breakdown of the gastroduodenal mucosal barrier, and in duodenogastric reflux, retrograde flow of alkaline bile and pancreatic contents into the stomach causes mucosal injury analogous to peptic ulceration. Because sucralfate's cytoprotective and bile-acid-binding properties directly target this shared injury mechanism, it is mechanistically plausible that a drug effective for ulcer healing would also mitigate mucosal damage from bile reflux.

This plausibility is reinforced by the literature evidence below: multiple small randomized controlled trials from the 1980s–2000s directly tested sucralfate in alkaline/duodenogastric reflux gastritis (including post-gastrectomy and post-cholecystectomy settings), lending independent clinical support to the TxGNN model's prediction even though a modern, phase-labeled trial program does not exist for this specific indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3839973](https://pubmed.ncbi.nlm.nih.gov/3839973/) | 1985 | RCT | Am J Med | Randomized, double-blind trial (n=23) of sucralfate 6g/day vs placebo in alkaline reflux gastritis after Billroth I/II or vagotomy+pyloroplasty; assessed symptoms, endoscopy, and histology |
| [12923369](https://pubmed.ncbi.nlm.nih.gov/12923369/) | 2003 | RCT | Eur J Gastroenterol Hepatol | Randomized trial comparing sucralfate vs rabeprazole vs no treatment for post-cholecystectomy alkaline reactive gastritis; evaluated dyspeptic symptoms and endoscopic/histologic signs |
| [3475771](https://pubmed.ncbi.nlm.nih.gov/3475771/) | 1987 | RCT | Scand J Gastroenterol Suppl | Prospective randomized trial of sucralfate vs placebo over 6 months in patients with symptomatic/macroscopic gastritis, distinguishing gastroesophageal from duodenogastric reflux |
| [1391144](https://pubmed.ncbi.nlm.nih.gov/1391144/) | 1992 | Comparative clinical trial | Minerva Gastroenterol Dietol | Compared cisapride (prokinetic) vs sucralfate (cytoprotective) in 18 patients with dyspepsia from duodenogastric reflux gastritis |
| [17285081](https://pubmed.ncbi.nlm.nih.gov/17285081/) | 2006 | Review | Journal de chirurgie | Comprehensive review of duodenogastric and gastroesophageal bile reflux: pathophysiology, diagnosis (24h bile monitoring), and medical/surgical management |
| [14723838](https://pubmed.ncbi.nlm.nih.gov/14723838/) | 2004 | Review | Curr Treat Options Gastroenterol | Reviews duodenogastric reflux-induced (alkaline) esophagitis and discusses medical treatment options including PPIs and mucosal protectants |
| [6372664](https://pubmed.ncbi.nlm.nih.gov/6372664/) | 1984 | Review | Annu Rev Med | Describes alkaline reflux (bile) gastritis and esophagitis, its pathophysiology after gastric surgery, and diagnostic features |
| [3838414](https://pubmed.ncbi.nlm.nih.gov/3838414/) | 1985 | Review | Am J Gastroenterol | ACG committee review of sucralfate's nonulcer uses, noting cytoprotective effects beyond antipepsin/antacid action, including gastritis and esophagitis |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Case series | Eur J Pediatr | Describes primary duodenogastric reflux in 6 pediatric/adolescent patients confirmed by 24h gastric bilimetry, unresponsive to classical antacid therapy |
| [3616071](https://pubmed.ncbi.nlm.nih.gov/3616071/) | 1987 | Case series | Rev Esp Enferm Apar Dig | Evaluation of 50 cases of postsurgical biliary reflux gastritis treated with sucralfate |

---

## India Market Information

Sucralfate is currently **not marketed** in this jurisdiction — the regulatory dataset shows **0 registered licenses**, so no product registration, dosage form, or approved indication text is available for extraction.

---

## Safety Considerations

- **Drug Interactions**: 413 total interactions on record. Notable examples include:
  - **Major**: Dolutegravir, Bictegravir (co-administration may significantly reduce absorption/efficacy of these antiretrovirals — separation of dosing times is typically required)
  - **Moderate**: Acarbose, Doxycycline, Tetracycline, Albiglutide, Alendronic acid, Allopurinol, Alogliptin, Pioglitazone, Ascorbic acid, Risedronic acid, Baloxavir marboxil, Ibandronate, Calcifediol
  - **Minor**: Acebutolol, Anagrelide, Atenolol, Betaxolol, Bisoprolol

Detailed key warnings and contraindications are not available in the current dataset (Data Gap DG001 — Blocking).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN prediction score is high (99.37%) and multiple older randomized trials support sucralfate's efficacy in alkaline/duodenogastric reflux gastritis, a **Blocking** data gap (missing local package-insert warnings/contraindications, DG001) prevents entry into S1 safety pre-assessment. The drug is also currently **not marketed** in this jurisdiction (0 licenses), limiting immediate actionability.

**To proceed, the following is needed:**
- Local product labeling (warnings & contraindications) — download and parse official package insert (DG001 remediation)
- Detailed mechanism of action data via DrugBank API (DG002 remediation)
- Confirmation of local market entry/registration pathway, given current "not marketed" status
- Assessment of major DDI risk (e.g., Dolutegravir, Bictegravir) for any target patient population, including dosing-separation guidance
- Consideration of a systematic review to consolidate the fragmented, decades-old RCT evidence into a formal evidence synthesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

