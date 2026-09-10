---
layout: default
title: Famotidine
parent: 僅模型預測 (L5)
nav_order: 335
evidence_level: L5
indication_count: 10
---

# Famotidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Famotidine: From Peptic Ulcer Disease to Duodenogastric Reflux

## One-Sentence Summary

Famotidine is a histamine H2-receptor antagonist historically used to treat peptic ulcer disease and acid-related gastrointestinal conditions.
The TxGNN model predicts it may also be effective for **Duodenogastric Reflux**, with a prediction score of **99.99%**,
though currently only **2 publications** and **no registered clinical trials** directly support this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic Ulcer Disease / Acid-related GI disorders (based on known drug class; no TFDA/India label text available — see Data Gap DG001) |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (source data labels this "Research Question" stage — S1) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on known information, Famotidine belongs to the histamine H2-receptor antagonist class, and its efficacy in acid-related peptic ulcer disease is well established through decades of clinical use.

Duodenogastric reflux (bile/duodenal content refluxing into the stomach) is mechanistically distinct from simple gastric acid hypersecretion, so the applicability of an H2-antagonist is less direct than in classic acid-peptic disease. Per the model's own rationale: acid suppression may reduce symptoms associated with concurrent acidic reflux, but the mechanistic link to bile/duodenogastric reflux itself is indirect, since neutralizing bile-mediated mucosal injury is not the primary pathway of H2-receptor blockade.

Given this indirect mechanistic link, and the fact that only observational/small non-RCT literature exists for this specific indication, the prediction should be treated as a research hypothesis rather than a near-term repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12532466](https://pubmed.ncbi.nlm.nih.gov/12532466/) | 2003 | Cohort (ICU patients) | World Journal of Gastroenterology | Investigated famotidine's effect on gastroesophageal reflux (GER) and duodeno-gastro-esophageal reflux (DGER) in critically ill patients, exploring possible mechanisms and relevant risk factors. |
| [16259441](https://pubmed.ncbi.nlm.nih.gov/16259441/) | 2004 | Review / small non-English study | Eksperimental'naia i klinicheskaia gastroenterologiia | Evaluated famotidine 20 mg BID at early stages of gastroduodenal reflux disease (Savary-Miller grade 0–1) via clinical and endoscopic assessment. |

---

## India Market Information

Famotidine is currently not registered or marketed in India (0 registrations on file).

---

## Safety Considerations

**Drug Interactions**: 639 documented interactions on record (source: DDInter). Representative Moderate-level interactions include Abiraterone, Acalabrutinib, Tramadol, Abarelix, Acetohexamide, Adenosine, Salbutamol, Aminophylline, Amiodarone, Amisulpride, Amitriptyline, Amoxapine, Anagrelide, Apalutamide, Apomorphine, Arformoterol, and Aripiprazole. Minor-level interactions include Alendronic acid and Aluminum hydroxide.

(Key warnings and contraindications are not yet available — see Data Gap DG001 below.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but for duodenogastric reflux specifically the evidence base is limited to two older, non-RCT publications with no registered clinical trials, and the mechanistic link (H2-blockade vs. bile-mediated reflux injury) is indirect. This does not yet meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/India regulatory package insert (warnings, contraindications) — currently blocking (Data Gap DG001)
- Confirmed mechanism of action data from DrugBank — currently high-impact gap (Data Gap DG002)
- Prospective or controlled trials evaluating famotidine specifically in duodenogastric/duodeno-gastro-esophageal reflux populations
- Note: within this same evidence pack, other predicted indications for famotidine — **peptic ulcer disease** (L1, multiple completed Phase 3/4 RCTs), **active peptic ulcer disease** (L1), and **gastrojejunal/marginal ulcer** (L2, direct Phase 4 RCT evidence) — show substantially stronger, more actionable evidence and may warrant prioritization over duodenogastric reflux.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

