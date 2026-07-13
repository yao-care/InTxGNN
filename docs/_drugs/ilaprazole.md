---
layout: default
title: Ilaprazole
parent: 僅模型預測 (L5)
nav_order: 296
evidence_level: L5
indication_count: 5
---

# Ilaprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Ilaprazole: From Acid-Related Disease Treatment to Active Peptic Ulcer Disease

## One-Sentence Summary

Ilaprazole is a next-generation proton pump inhibitor (PPI) marketed in South Korea, China, Mexico, and India for acid-related conditions including dyspepsia, gastroesophageal reflux disease (GERD), and peptic ulcer disease.
The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease** — with **5 clinical trials** and **6 publications** providing direct support for this indication.
Although no CDSCO registration exists in India, robust multinational Phase 3 trial data creates a clear regulatory pathway for local approval.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No CDSCO approval on record; internationally approved for GERD, peptic ulcer disease, and dyspepsia |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L1 |
| India Market Status | Not marketed (CDSCO) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

From pharmacology data and early mechanism studies (PMID 11304936), ilaprazole (IY-81149) irreversibly inhibits the H⁺/K⁺-ATPase enzyme on gastric parietal cells — the proton pump that drives all gastric acid secretion. In vitro studies show ilaprazole inhibits this pump with an IC₅₀ of 6.0 × 10⁻⁶ mol/L, approximately 17-fold more potent than omeprazole at physiological pH. By permanently blocking the final step of acid production, ilaprazole elevates intragastric pH and removes the primary chemical driver of ulcer formation.

Peptic ulcer disease is the most direct therapeutic application of this mechanism. Elevated intragastric pH improves platelet aggregation at bleeding ulcer sites, inactivates pepsin (which would otherwise digest the vulnerable ulcer bed), and creates a permissive environment for mucosal regeneration. In H. pylori-positive ulcers — the most common aetiology — the elevated pH also stabilises co-administered antibiotics, improving eradication rates. This mechanistic chain (pump inhibition → acid suppression → ulcer healing) is the most complete and evidence-supported link available for any PPI.

Ilaprazole is already approved for peptic ulcer disease in South Korea and China. Multinational Phase 3 trials confirm non-inferiority or superiority compared to established PPIs including omeprazole, rabeprazole, and pantoprazole. The TxGNN prediction therefore validates established global clinical practice rather than proposing a speculative novel use — making this principally a market-introduction opportunity for India rather than a discovery-stage repurposing exercise.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00952978](https://clinicaltrials.gov/study/NCT00952978) | Phase 3 | Completed | 496 | Ilaprazole 10 mg/day vs Omeprazole 20 mg/day in active duodenal ulcer; primary endpoint: ulcer healing rate at week 4; positive-controlled, multicenter RCT in China |
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Ilaprazole vs Pantoprazole-based triple therapy for H. pylori eradication in gastric and/or duodenal ulcer patients; 7-day treatment, randomised, double-blind, multicenter design |
| [NCT02847455](https://clinicaltrials.gov/study/NCT02847455) | Phase 2/3 | Completed | 408 | Ilaprazole (5 mg or 10 mg/day) vs Rabeprazole 10 mg/day in active duodenal ulcer; dose-ranging across 4 weeks; provides non-inferiority data versus a second-generation PPI |
| [NCT00953381](https://clinicaltrials.gov/study/NCT00953381) | Phase 2 | Completed | 235 | Ilaprazole at 5, 10, and 20 mg/day vs Omeprazole 20 mg/day in active duodenal ulcer; established 10 mg/day as the optimal therapeutic dose |
| [NCT06284876](https://clinicaltrials.gov/study/NCT06284876) | Phase 3 | Recruiting | 416 | Ilaprazole 10 mg vs active control for prevention of NSAIDs-associated peptic ulcer; non-inferiority design with 24-week follow-up (expected completion: February 2027) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22070512](https://pubmed.ncbi.nlm.nih.gov/22070512/) | 2012 | Phase 3 RCT | Current Medical Research and Opinion | Confirmed ilaprazole 10 mg/day compared with omeprazole 20 mg/day in duodenal ulcer healing; characterised CYP2C19 metabolism and its impact on pharmacokinetic variability |
| [19434360](https://pubmed.ncbi.nlm.nih.gov/19434360/) | 2009 | Phase 3 RCT | Journal of Gastroenterology | First multinational human RCT comparing ilaprazole vs omeprazole across both gastric and duodenal ulcers; established clinical proof-of-concept |
| [30789856](https://pubmed.ncbi.nlm.nih.gov/30789856/) | 2019 | Phase 3 RCT | Journal of Clinical Gastroenterology | Ilaprazole vs Rabeprazole in duodenal ulcer treatment across multiple doses; explored dose-effect relationship and confirmed therapeutic equivalence |
| [27605258](https://pubmed.ncbi.nlm.nih.gov/27605258/) | 2016 | RCT | Clinical Drug Investigation | Randomised, double-blind, active-controlled multicenter study of ilaprazole in reflux esophagitis; PPI class safety and acid-suppression efficacy confirmed across related indications |
| [20679904](https://pubmed.ncbi.nlm.nih.gov/20679904/) | 2011 | RCT | Journal of Clinical Gastroenterology | Investigated efficacy and safety of ilaprazole vs omeprazole in duodenal ulcers; provided dose-response characterisation supporting the 10 mg/day dose selection |
| [24801687](https://pubmed.ncbi.nlm.nih.gov/24801687/) | 2014 | Animal Study | Digestive Diseases and Sciences | Intravenous ilaprazole showed superior gastroprotective potency over oral formulation in rat models; supports rationale for IV formulation development in surgical/hospitalised ulcer patients |

---

## India Market Information

No CDSCO regulatory approvals are currently on record for Ilaprazole in India. The drug has 0 registered products and holds no approved indications under the Indian regulatory authority. Note: pharmacological reference data indicates ilaprazole may be commercially available in India through separate channels, but this is not reflected in the CDSCO registration database reviewed for this report.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Formal TFDA/CDSCO package insert warnings and contraindications were not available in the current Evidence Pack. Prior to proceeding with any clinical or regulatory application, a complete safety review — including contraindications, warnings, and drug-drug interaction profile — should be sourced from the marketing authorisation holder or the published SmPC (South Korea/China approvals).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs conducted across China and South Korea demonstrate consistent efficacy and tolerability of ilaprazole 10 mg/day for active peptic ulcer disease, including confirmed non-inferiority or superiority versus omeprazole, rabeprazole, and pantoprazole. The H⁺/K⁺-ATPase inhibition mechanism is well-characterised, directly aligned with the predicted indication, and shares the same pharmacological basis as the globally established PPI drug class.

**To proceed, the following is needed:**
- CDSCO registration application package leveraging existing Phase 3 multinational data (a bridging pharmacokinetic study in the Indian population may be required, particularly given CYP2C19 polymorphism variability)
- India-specific package insert with complete warnings, contraindications, and special population guidance (currently a data gap)
- Formal drug-drug interaction profile beyond the known H⁺/K⁺-ATPase pharmacology interaction
- CYP2C19 pharmacogenomics assessment specific to the Indian population, as metaboliser status significantly affects PPI plasma exposure
- Clarification of current India commercial availability status (discrepancy between pharmacology reference data and CDSCO registration records)
- Confirmed local supply chain, formulation availability, and pricing strategy for the Indian market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

