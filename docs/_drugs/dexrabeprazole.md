---
layout: default
title: Dexrabeprazole
parent: 僅模型預測 (L5)
nav_order: 232
evidence_level: L5
indication_count: 6
---

# Dexrabeprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Dexrabeprazole: From Acid Peptic Disorders to Active Peptic Ulcer Disease

## One-Sentence Summary

Dexrabeprazole is the R(+) enantiomer of Rabeprazole, a proton pump inhibitor developed for the treatment of acid peptic disorders — commercially available in India since at least 2009 based on published surveillance data, though currently absent from the CDSCO registration database.
The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**,
with **0 registered clinical trials** and **19 publications** currently supporting this direction — including one large-scale direct observational study of Dexrabeprazole itself (4,931 patients in India) and multiple Phase 3 RCTs for its parent compound Rabeprazole.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acid peptic disorders (based on published evidence; no formal CDSCO registration data available) |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L3 |
| India Market Status | Not registered (CDSCO) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Dexrabeprazole is the R(+) enantiomer — the pharmacologically active optical isomer — of Rabeprazole, a second-generation proton pump inhibitor. While formal DrugBank MOA documentation is unavailable for Dexrabeprazole as a standalone entity, published literature establishes that it shares the same mechanism as its parent compound: irreversible inhibition of the H+/K+-ATPase enzyme (the gastric "proton pump") at the secretory surface of parietal cells, leading to potent and sustained suppression of both basal and stimulated gastric acid secretion. A key pharmacokinetic advantage over racemic Rabeprazole is that Dexrabeprazole achieves equivalent or superior acid suppression at half the dose — because the S(−) enantiomer contributes negligible therapeutic activity while adding to systemic exposure and hepatic metabolic burden.

Active peptic ulcer disease is directly driven by an imbalance between acid-mediated mucosal injury (compounded by *H. pylori* infection or NSAID use) and the stomach's protective mechanisms. Because acid suppression is the mechanistic cornerstone of peptic ulcer treatment, the applicability of a potent, enantioselective PPI like Dexrabeprazole to this indication is conceptually direct rather than speculative — this is a "mechanism-first" prediction with a high prior probability of success.

Empirically, the parent compound Rabeprazole has multiple Phase 3 RCTs demonstrating efficacy in active duodenal ulcer, gastric ulcer, and *H. pylori* eradication (PMIDs 9590413, 12694089, 10763941). More directly, a large-scale Indian postmarketing surveillance study (PMID 19585824, n=4,931) specifically evaluated Dexrabeprazole in acid peptic disorders and confirmed safety, faster healing kinetics, and superior pharmacokinetics relative to racemic Rabeprazole — making this one of the rare TxGNN drug repurposing predictions backed by direct compound-level evidence in the target market.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for Dexrabeprazole in active peptic ulcer disease (ClinicalTrials.gov and ICTRP queried on 2026-03-26, 0 results).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [19585824](https://pubmed.ncbi.nlm.nih.gov/19585824/) | 2009 | Postmarketing Surveillance | Journal of the Indian Medical Association | **Direct Dexrabeprazole study**: 4,931 patients with acid peptic disorders in India; confirmed superior pharmacokinetics, faster and greater healing activity vs. Rabeprazole at half the dose; safety reconfirmed |
| [9590413](https://pubmed.ncbi.nlm.nih.gov/9590413/) | 1998 | RCT (Placebo-controlled) | Digestive Diseases and Sciences | Three placebo-controlled trials of Rabeprazole in duodenal ulcer, gastric ulcer, and GERD; Rabeprazole 20 mg and 40 mg both significantly superior to placebo for ulcer healing |
| [12694089](https://pubmed.ncbi.nlm.nih.gov/12694089/) | 2003 | RCT | Alimentary Pharmacology & Therapeutics | Double-blind RCT: Rabeprazole-based vs. omeprazole-based 7-day triple therapy for *H. pylori* eradication in documented peptic ulcer disease; regimens therapeutically equivalent |
| [22526273](https://pubmed.ncbi.nlm.nih.gov/22526273/) | 2012 | RCT | Journal of Gastroenterology | Rabeprazole significantly reduces recurrence of peptic ulcers in cardiovascular/cerebrovascular patients on low-dose aspirin; prospective randomized active-controlled trial |
| [10763941](https://pubmed.ncbi.nlm.nih.gov/10763941/) | 2000 | RCT | The American Journal of Gastroenterology | Rabeprazole superior to ranitidine for healing active duodenal ulcer disease in a double-blind North American study |
| [16911680](https://pubmed.ncbi.nlm.nih.gov/16911680/) | 2006 | RCT | Journal of Gastroenterology and Hepatology | Low-dose Rabeprazole 10 mg shown equivalent to Omeprazole 20 mg for active peptic ulcer healing rapidity; CYP2C19 genotype effects on healing also investigated |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic Review & Network Meta-analysis | The American Journal of Gastroenterology | P-CAB vs. PPI comparison for severe esophagitis; establishes current context for acid suppressant class comparisons relevant to Dexrabeprazole positioning |
| [10491723](https://pubmed.ncbi.nlm.nih.gov/10491723/) | 1999 | Review | Alimentary Pharmacology & Therapeutics | Pharmacology review of Rabeprazole: more potent H+/K+-ATPase inhibitor than omeprazole; faster activation in parietal cell canaliculus; once-daily dosing adequate |
| [41809210](https://pubmed.ncbi.nlm.nih.gov/41809210/) | 2026 | Expert Consensus | World Journal of Gastrointestinal Pharmacology and Therapeutics | Indian expert consensus on comprehensive management of acid peptic disorders; addresses PPI role and risks of unsupervised acid suppressant use in Indian population |
| [9506245](https://pubmed.ncbi.nlm.nih.gov/9506245/) | 1998 | Review | Drugs | Foundational review of Rabeprazole pharmacology: 2–10× greater antisecretory activity than omeprazole in vitro; clinically superior to placebo and famotidine across acid-peptic conditions |

---

## India Market Information

No CDSCO-registered products were found for Dexrabeprazole. The current regulatory database shows zero active licenses (queried 2026-04-04).

> **Important note**: Published Indian literature (PMID 19585824, 2009) documents that Dexrabeprazole was commercially launched in India for acid peptic diseases, with a postmarketing surveillance program enrolling 4,931 patients across multiple centers. The absence from the current CDSCO database likely reflects a data gap in the evidence pack rather than true non-availability. A direct search of the CDSCO online drug database and review of historical approval records is strongly recommended before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data are currently available for Dexrabeprazole in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dexrabeprazole's prediction for active peptic ulcer disease is mechanistically direct (proton pump inhibition is the established treatment pathway), supported by a large Indian postmarketing observational study specifically for this compound (n=4,931; PMID 19585824), and further anchored by robust Phase 3 RCT evidence for the parent compound Rabeprazole. The L3 evidence level reflects the lack of Dexrabeprazole-specific RCTs — a gap that is addressable rather than a fundamental scientific uncertainty.

**To proceed, the following is needed:**

- **Regulatory verification**: Confirm current CDSCO registration status through a direct database search; retrieve historical approval records and the Indian package insert to clarify the drug's formal regulatory standing
- **Safety dossier**: Extract and document contraindications, boxed warnings, and drug interactions from the Indian prescribing information or the parent compound's regulatory filings
- **Pharmacogenomics plan**: Develop a CYP2C19 genotyping strategy, as PPI-class drugs show clinically significant metabolic variability — though Dexrabeprazole's enantiomeric purity may reduce (but not eliminate) this variability
- **Dose-ranging evidence**: Formalize the therapeutic dose for the Indian indication; published evidence suggests half the racemic Rabeprazole dose, but a prospective dose-confirmation study would be required for regulatory submission
- **Enantiomer-specific RCT**: To upgrade from L3 to L2/L1, at least one Phase 2/3 RCT specifically comparing Dexrabeprazole against standard-of-care PPI therapy in active peptic ulcer disease is needed — this would also close the gap between postmarketing surveillance data and regulatory-grade evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

