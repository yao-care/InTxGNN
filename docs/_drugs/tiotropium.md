---
layout: default
title: Tiotropium
parent: High Evidence (L1-L2)
nav_order: 832
evidence_level: L1
indication_count: 10
---

# Tiotropium
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

Using the specified v5 report template to synthesize this Evidence Pack into the required Markdown report.

---

# Tiotropium: From Bronchodilator (Not Locally Marketed) to Obstructive Lung Disease

## One-Sentence Summary

> Tiotropium is a long-acting muscarinic antagonist (LAMA) bronchodilator with no formally recorded local approval history in this dataset (0 registrations, market status "Not Marketed").
> The TxGNN model's top-ranked candidate is **Obstructive Lung Disease**, which corresponds to tiotropium's internationally established use as a COPD/asthma maintenance bronchodilator.
> This is supported by an unusually large evidence base: **60+ clinical trials** and **20 publications**, including several landmark Phase 3 RCTs.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not locally approved / no registration on file (drug not marketed); internationally established as a long-acting bronchodilator for COPD/asthma |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action (MOA) record for tiotropium is a flagged data gap in this pack (DG002 — High severity, remediation: query DrugBank API). However, the evidence pack's own repurposing rationale supplies the pharmacological basis: **tiotropium is a long-acting muscarinic receptor antagonist (LAMA)** that blocks M1 and M3 receptors, inhibiting acetylcholine-mediated bronchoconstriction. This is the standard mechanistic pathway underlying treatment of obstructive airway diseases such as COPD and severe persistent asthma.

Because `original_indications` and `taiwan_regulatory.licenses` are both empty, this jurisdiction has no on-file record of tiotropium ever being formally indicated or registered locally — the drug shows as "Not Marketed" with zero registrations. The TxGNN model's top prediction, "obstructive lung disease," is therefore not a novel mechanistic leap; it converges with tiotropium's globally recognized primary use, as explicitly noted in the rank-5 rationale for "chronic obstructive pulmonary disease" in the same pack ("此為Tiotropium國際公認之主要適應症，本資料集market_status標示Not marketed可能僅反映該轄區尚未核准" — this is tiotropium's internationally recognized primary indication; the "not marketed" status here likely just reflects that this jurisdiction has not yet approved it).

In other words, the mechanistic applicability is high because the "new" indication and the drug's known pharmacology are the same disease class — the gap is regulatory/administrative (no local license on record), not scientific.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00144339](https://clinicaltrials.gov/study/NCT00144339) | Phase 3 | Completed | 5,993 | UPLIFT trial — evaluated whether daily tiotropium reduces the rate of lung function (FEV1) decline over time in COPD |
| [NCT00277264](https://clinicaltrials.gov/study/NCT00277264) | Phase 3 | Completed | 914 | SAFE study — 1-year RCT on trough FEV1 change with tiotropium 18 µg vs. placebo; Grade A relevance |
| [NCT00776984](https://clinicaltrials.gov/study/NCT00776984) | Phase 3 | Completed | 453 | 48-week RCT of tiotropium Respimat 5 µg as add-on therapy in severe persistent asthma; Grade A relevance |
| [NCT01012765](https://clinicaltrials.gov/study/NCT01012765) | Phase 3 | Completed | 173 | Crossover study using open-label tiotropium 18 µg as active bronchodilator comparator in moderate COPD; Grade A relevance |
| [NCT01316913](https://clinicaltrials.gov/study/NCT01316913) | Phase 3 | Completed | 872 | 24-week RCT comparing GSK573719/GW642444 combination vs. tiotropium in COPD; Grade B relevance |
| [NCT01911364](https://clinicaltrials.gov/study/NCT01911364) | Phase 3 | Completed | 3,686 | 52-week trial of triple therapy (beclometasone+formoterol+glycopyrrolate) vs. tiotropium in severe COPD |
| [NCT02006732](https://clinicaltrials.gov/study/NCT02006732) | Phase 3 | Completed | 809 | TONADO-type study assessing tiotropium+olodaterol fixed-dose combination vs. tiotropium and placebo in moderate-severe COPD |
| [NCT02173769](https://clinicaltrials.gov/study/NCT02173769) | N/A | Completed | 1,845 | AKTIV — large real-world study on physical functioning changes with tiotropium ± olodaterol combination therapy |
| [NCT00463567](https://clinicaltrials.gov/study/NCT00463567) | Phase 2/3 | Completed | 2,059 | Seamless adaptive dose-finding study using open-label tiotropium as active control in COPD |
| [NCT00274014](https://clinicaltrials.gov/study/NCT00274014) | Phase 3 | Completed | 1,000 | 1-year RCT evaluating tiotropium's effect on airflow obstruction severity and exacerbation incidence/severity in moderate-severe COPD |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28877027](https://pubmed.ncbi.nlm.nih.gov/28877027/) | 2017 | RCT | N Engl J Med | Long-term tiotropium improves lung function and slows decline in mild/moderate, early-stage COPD |
| [25046211](https://pubmed.ncbi.nlm.nih.gov/25046211/) | 2014 | Review/Meta-analysis (Cochrane) | Cochrane Database Syst Rev | Systematic review confirming tiotropium efficacy vs. placebo across multiple COPD trials |
| [29605624](https://pubmed.ncbi.nlm.nih.gov/29605624/) | 2018 | RCT (DYNAGITO) | Lancet Respir Med | Tiotropium+olodaterol vs. tiotropium alone for prevention of COPD exacerbations |
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Review (Cochrane) | Cochrane Database Syst Rev | Comparative review of tiotropium vs. ipratropium bromide in stable COPD |
| [32727455](https://pubmed.ncbi.nlm.nih.gov/32727455/) | 2020 | Review | Respiratory Research | Overview of tiotropium's clinical development program as LAMA monotherapy across GOLD groups B/C/D |
| [35510163](https://pubmed.ncbi.nlm.nih.gov/35510163/) | 2022 | Cohort (real-world) | Int J Chron Obstruct Pulmon Dis | Multicenter Taiwan-based comparison of tiotropium/olodaterol vs. other LABA/LAMA combinations in COPD |
| [19402836](https://pubmed.ncbi.nlm.nih.gov/19402836/) | 2009 | Meta-analysis | Respirology | Efficacy and safety of tiotropium in Chinese patients with stable COPD |
| [12010082](https://pubmed.ncbi.nlm.nih.gov/12010082/) | 2002 | Review | Drugs | Pharmacological profile and clinical efficacy summary of tiotropium bromide in COPD |
| [10069510](https://pubmed.ncbi.nlm.nih.gov/10069510/) | 1999 | Review | Life Sciences | Original mechanistic characterization of tiotropium as a slow-dissociating M1/M3-selective antimuscarinic |
| [16030078](https://pubmed.ncbi.nlm.nih.gov/16030078/) | 2005 | Review | Ann Pharmacother | Review of tiotropium efficacy and tolerability as a COPD bronchodilator |

---

## India Market Information

Tiotropium is currently **not marketed** in this jurisdiction — `total_licenses = 0`, and no authorization records are present in the evidence pack (`licenses: []`). There is no local product name, dosage form, or approved-indication text on file to report.

---

## Safety Considerations

- **Drug Interactions**: The evidence pack's DDI query returned **430 total interactions**. The most clinically notable pattern is **additive anticholinergic burden** with other antimuscarinic/anticholinergic agents — flagged as *Moderate* severity for: Hyoscyamine, Atropine, Glycopyrronium (systemic and topical), Clidinium, Dicyclomine, Eluxadoline, Trospium, Mepenzolate, Methscopolamine, Propantheline, and Scopolamine. Co-administration may increase risk of dry mouth, urinary retention, constipation, and blurred vision. A *Minor* interaction was noted with Cimetidine. Several additional interactions (e.g., Calcitriol, Pantoprazole, Glimepiride, Mesalazine, Doxycycline) are recorded at "Unknown" severity and warrant individual review before use.

*(Key warnings and contraindications were not available in this pack — flagged as Blocking data gap DG001, requiring TFDA/CDSCO label retrieval before safety sign-off.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The obstructive-lung-disease indication is backed by L1-level evidence — multiple large, completed Phase 3 RCTs (including the 5,993-patient UPLIFT trial and the 914-patient SAFE study) plus Cochrane-level systematic reviews confirm bronchodilator efficacy. However, this jurisdiction currently has **zero registrations** for the product, and two Blocking/High-severity data gaps (local label warnings/contraindications, and a structured MOA record) must be closed before any regulatory or clinical-use decision.

**To proceed, the following is needed:**
- Retrieve and parse the official product label (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirm structured MOA via DrugBank API — currently a High-severity gap (DG002)
- Local market-authorization dossier assessment, since the drug has no current registration despite strong global evidence
- Formal review of anticholinergic DDI risk in target patient populations (esp. concomitant antimuscarinic use)

**Note on other predicted candidates in this pack:** Predictions ranked #2 (respiratory malformation), #3 (Rienhoff syndrome), #6–#10 (interstitial emphysema, hyperlucent lung, compensatory emphysema, tracheal stenosis, CD8α-related immunodeficiency) were all scored L5/Hold — these reflect structural, congenital, or immunologic conditions with no plausible mechanistic link to LAMA pharmacology and no supporting trials or literature; they should be treated as knowledge-graph noise rather than actionable candidates. Rank #4 ("COPD, severe early onset") and rank #5 ("chronic obstructive pulmonary disease" itself) are consistent with and reinforce the rank #1 conclusion above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

