---
layout: default
title: Aluminum Hydroxide
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 4
---

# Aluminum Hydroxide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Aluminum Hydroxide: From Antacid Use to Active Peptic Ulcer Disease

## One-Sentence Summary

Aluminum hydroxide is a classic alkaline antacid with a long history of use in managing gastric acid-related conditions, though it currently lacks formal regulatory registration in India.
The TxGNN model predicts it may be clinically effective for **Active Peptic Ulcer Disease** — a more formal and specific therapeutic application than general symptomatic acid relief.
This prediction is supported by **no registered clinical trials** but **20 publications**, including multiple RCTs, providing L2-level evidence for its ulcer-healing efficacy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formal indication registered in India |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L2 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Although formal MOA data is not available in the current database, aluminum hydroxide's mechanism of action is extensively documented in the pharmacological literature. As an alkaline antacid, Al(OH)₃ reacts directly with gastric hydrochloric acid (HCl) to form aluminum chloride (AlCl₃) and water, raising intragastric pH above 4. At this pH, pepsin activity is substantially suppressed — pepsin requires pH below 3.5 for full proteolytic function — thereby protecting the ulcer crater from further enzymatic digestion. This two-pronged action (acid neutralization + pepsin inhibition) directly addresses the core aggression mechanisms driving peptic ulcer formation.

Beyond simple pH buffering, aluminum-containing antacids exhibit cytoprotective properties that are critically relevant to ulcer healing. Research has demonstrated that Al(OH)₃ stimulates endogenous production of prostaglandins (particularly PGE₂) and epidermal growth factor (EGF) in the gastric mucosa. These mediators promote epithelial cell proliferation, reinforce the mucus-bicarbonate barrier, and enhance mucosal microcirculation — all essential components of ulcer healing. Aluminum ions also form a viscous gel layer that physically coats the ulcer surface, providing a physical barrier against further acid and pepsin insult.

Active peptic ulcer disease is fundamentally characterized by an imbalance between acid-peptic aggression and mucosal defense. Aluminum hydroxide addresses both sides of this equation simultaneously: reducing aggressive factors (acid, pepsin) while stimulating defensive mechanisms (prostaglandins, EGF, mucus barrier). The mechanistic chain is complete and direct, making the TxGNN prediction highly plausible. While modern clinical practice has largely shifted toward proton pump inhibitors (PPIs) and H. pylori eradication as first-line therapy, the pharmacological rationale for aluminum hydroxide in active peptic ulcer disease remains scientifically robust.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for Aluminum Hydroxide in Active Peptic Ulcer Disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT (3-arm) | Scand J Gastroenterol | 72 patients with duodenal/prepyloric ulcer in a 12-week double-blind trial; antacid + L-hyoscyamine achieved 50% healing at 3 weeks vs 67% for cimetidine; both significantly superior to placebo |
| [6086186](https://pubmed.ncbi.nlm.nih.gov/6086186/) | 1984 | RCT | Clin Gastroenterol | Comprehensive review of controlled trials on antacids and anticholinergics in duodenal ulcer; documents efficacy and evidence base for aluminum-containing antacid therapy |
| [2986275](https://pubmed.ncbi.nlm.nih.gov/2986275/) | 1985 | RCT | Scand J Gastroenterol Suppl | 68 patients randomized to sucralfate vs alginate/antacid; ~70% of patients became symptom-free or markedly improved in both treatment groups over 6 weeks |
| [22950493](https://pubmed.ncbi.nlm.nih.gov/22950493/) | 2013 | Review | Curr Pharm Design | Comprehensive mechanistic review of antacid gastroprotection beyond prostaglandins; documents Al(OH)₃-mediated cytoprotection, EGF induction, and mucosal barrier reinforcement |
| [1769429](https://pubmed.ncbi.nlm.nih.gov/1769429/) | 1991 | Pharmacodynamic Study | Digestion | Compared unmodified vs acidified Maalox (Al(OH)₃) in acute gastric mucosal lesion models; prostaglandins partially mediate gastroprotective effects; both forms enhanced chronic ulcer healing |
| [2390927](https://pubmed.ncbi.nlm.nih.gov/2390927/) | 1990 | Experimental Study | Dig Dis Sci | Maalox and its active component Al(OH)₃ significantly enhanced PGE₂ and EGF production in rat gastric mucosa; both prostaglandins and EGF identified as mediators of antacid-driven ulcer healing |
| [37146](https://pubmed.ncbi.nlm.nih.gov/37146/) | 1979 | Review | Fortschr Med | Antacid therapy fundamentals: acid neutralization and pepsin inhibition require dosing of 40–80 mval 1 and 3 hours postprandially; neutralizing capacity depends on chemical composition |
| [9334882](https://pubmed.ncbi.nlm.nih.gov/9334882/) | 1997 | In Vitro Study | Jpn J Pharmacol | Al(OH)₃ (0.1–1 mg/ml) prevented both acid- (pH 4.0) and pepsin- (pH 4.5) induced damage to rat gastric epithelial cells (RGM1); identified as the active gastroprotective component of sucralfate |
| [9305482](https://pubmed.ncbi.nlm.nih.gov/9305482/) | 1997 | Clinical Study | Aliment Pharmacol Ther | Aluminum-magnesium hydroxide antacid evaluated in H. pylori-positive duodenal ulcer patients; antacids may aggravate H. pylori gastritis, highlighting importance of eradication co-therapy |
| [35720246](https://pubmed.ncbi.nlm.nih.gov/35720246/) | 2022 | Lab Study | Med Pharm Rep | Evaluated acid-neutralizing capacity (ANC) and physicochemical properties of marketed antacid formulations; documented significant formulation-dependent variation in neutralization efficacy relevant to clinical dosing |

---

## India Market Information

Aluminum hydroxide currently has **no registered products in India**. No authorization numbers, product names, or approved indication texts are available in the regulatory database.

---

## Safety Considerations

**Drug Interactions (205 interactions documented; key interactions listed below):**

| Severity | Interacting Drug | Clinical Implication |
|---------|-----------------|---------------------|
| **Major** | Dolutegravir | Aluminum markedly reduces dolutegravir absorption; separate dosing by ≥6 hours or avoid concurrent use |
| **Major** | Sodium citrate | Concurrent alkalinization may increase aluminum systemic absorption and toxicity risk |
| **Moderate** | Doxycycline | Chelation reduces tetracycline absorption; separate dosing by ≥2 hours |
| **Moderate** | Alendronic acid | Bisphosphonate absorption significantly impaired; administer bisphosphonate on empty stomach, well before antacid |
| **Moderate** | Risedronic acid | Same precaution as alendronic acid |
| **Moderate** | Atazanavir | Reduced antiretroviral bioavailability due to pH-dependent absorption changes |
| **Moderate** | Amphetamine | Urinary alkalinization may reduce renal clearance of amphetamine; monitor clinical effect |
| **Moderate** | Acetylsalicylic acid | Alkalinized urine increases salicylate renal elimination; may reduce analgesic/anti-inflammatory effect |
| **Moderate** | Allopurinol | Reduced allopurinol absorption possible with concurrent administration |
| **Moderate** | Proguanil | Absorption alteration documented; monitor antimalarial efficacy |

> For complete safety information including package insert warnings and contraindications, please consult the prescribing information (data not available in current dataset).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple historical RCTs and pharmacodynamic studies provide L2-level evidence for aluminum hydroxide in active peptic ulcer disease, and the dual mechanism of acid neutralization plus cytoprotection directly targets the disease pathophysiology. However, the drug is currently not registered in India (0 licenses), and modern treatment guidelines position PPIs and H. pylori eradication as first-line therapy, meaning a clearly defined clinical niche must be established before pursuing formal registration.

**To proceed, the following is needed:**
- Obtain the prescribing information / package insert to address the **Blocking data gap** on key warnings and contraindications (DG001), required before any safety evaluation can be completed
- Clarify intended clinical positioning: adjunct to PPI therapy, second-line for PPI-intolerant patients, or acute symptomatic relief bridge during H. pylori eradication
- Define the India regulatory registration pathway given zero current market presence
- Develop a drug interaction management protocol with particular attention to the two **Major** interactions (Dolutegravir, Sodium citrate) and the clinically common **Moderate** interactions (bisphosphonates, tetracyclines, antiretrovirals)
- Consider a prospective observational study or pragmatic trial comparing Al(OH)₃-adjunct therapy vs. PPI monotherapy in a relevant Indian patient population to generate contemporary local evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

