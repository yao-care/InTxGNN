---
layout: default
title: Conjugated Estrogens
parent: Model Prediction Only (L5)
nav_order: 212
evidence_level: L5
indication_count: 9
monitor_inn: "Conjugated estrogens"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis", "rheumatoid arthritis", "heparin cofactor 2 deficiency", "Prinzmetal angina", "hemoglobinopathy", "thrombophilia"]
last_modified_at: 2026-11-20
description: "Conjugated Estrogens: predicted new indication migraine disorder (evidence level L5). In India: 8 listed products (8 not discontinued)"
---

# Conjugated Estrogens
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Conjugated Estrogens: Estrogen receptor agonist → migraine disorder
{: .text-alpha }

## One-Sentence Summary

Conjugated estrogens are a mixed estrogen preparation, marketed in India as oral tablets and a vaginal cream.
The TxGNN model predicts they may be relevant to **migraine disorder**, with a score of **0.9977**.
There are **no registered clinical trials** for this disease, and the data compiled for this report include **5 publications** that touch on hormones and migraine, so the direction of effect remains uncertain.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | migraine disorder |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (8 of 8) – CDSCO approval status is not included in this data |
| Number of Listed Products | 8 (valid: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for conjugated estrogens: "Endogenous estrogens are largely responsible for the development and maintenance of the female reproductive system and secondary sexual characteristics. Although circulating estrogens exist in a dynamic equilibrium of metabolic interconversions, estradiol is the principal intracellular human estrogen and is substantially more potent than its metabolites, estrone and estriol, at the receptor level. […] Thus, estrone and the sulfate-conjugated form, estrone sulfate, are the most abundant circulating estrogens in postmenopausal women." ([DailyMed: Premarin Vaginal (conjugated estrogens) prescribing information, Wyeth Pharmaceuticals LLC, a subsidiary of Pfizer Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=96609623-528e-4aba-cabe-7254aed816d5), label version 2025-05-30; accessed 2026-11-19.) Based on known information, conjugated estrogens act on estrogen receptors and change circulating estrogen levels.

Migraine is strongly linked to estrogen fluctuation, especially the drop in estrogen around menstruation and during the menopausal transition. In theory, exogenous estrogen could stabilise hormone levels and so reduce hormone-triggered attacks.

The clinical literature, however, shows mixed results. Depending on dose, route and regimen, hormone therapy has worsened migraine in some women and improved it in others. Oral conjugated estrogens produce fluctuating blood levels, which may be less favourable than stable transdermal delivery. Migraine with aura also carries an added risk of ischaemic stroke with estrogen. The high score is plausible, but the direction of effect is unclear.

Because none of the cited papers is a trial testing conjugated estrogens as a treatment for migraine, the evidence level is capped at L5 (model prediction with no direct study of the disease as a treatment target).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29521155](https://pubmed.ncbi.nlm.nih.gov/29521155/) | 2018 | Review | Climacteric | Hormonal fluctuations, especially large estradiol swings in the perimenopause, are an important migraine trigger; different migraine types respond differently |
| [11306204](https://pubmed.ncbi.nlm.nih.gov/11306204/) | 2001 | Cohort | Maturitas | Evaluated how hormone replacement therapy influences the course of primary headaches in postmenopausal women |
| [12390622](https://pubmed.ncbi.nlm.nih.gov/12390622/) | 2002 | Cohort | Headache | Compared three oral HRT schemes on migraine course in postmenopausal women; effects differed by scheme |
| [8309263](https://pubmed.ncbi.nlm.nih.gov/8309263/) | 1994 | Review | Mayo Clinic Proceedings | Compared transdermal and oral estrogen therapy across groups of women |
| [14195735](https://pubmed.ncbi.nlm.nih.gov/14195735/) | 1964 | Case series | Medizinische Klinik | Early report on conjugated estrogens for climacteric disorders (no abstract available) |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 173733 | Premarin Vaginal Cream | tube of 14 gm Vaginal Cream | Not recorded in the local data |
| 173715 | Premarin Tablet | strip of 28 tablets | Not recorded in the local data |
| 40919 | Conjya 0.625mg Tablet | strip of 28 tablets | Not recorded in the local data |
| 40355 | Cornil Tablet | strip of 21 tablets | Not recorded in the local data |
| 36260 | Conjugase Tablet | strip of 28 tablets | Not recorded in the local data |

## Safety Considerations

- **Stroke risk in migraine with aura**: the evidence compiled for this report notes an added ischaemic stroke risk with estrogen exposure in people with aura.
- **Thrombotic risk**: estrogens are prothrombotic, which is a concern in people with thrombophilia.
- **Drug Interactions**: 100 interactions were found. Most listed ones are Moderate, including:
  - Acarbose, alogliptin, albiglutide, canagliflozin, dapagliflozin, dulaglutide, empagliflozin, acetohexamide and chlorpropamide (antidiabetic agents)
  - Hydrocortisone, dexamethasone, betamethasone, budesonide and triamcinolone (corticosteroids)
  - Aprepitant, clarithromycin, clotrimazole, chenodeoxycholic acid and topical calcitriol
  - Cimetidine is rated Minor.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but no trial studies conjugated estrogens for migraine, and the literature shows both worsening and improvement. The stroke risk in migraine with aura adds a safety concern.

**To proceed, the following is needed:**
- Controlled trials of conjugated estrogens in migraine, separating menstrual and menopausal migraine and aura status
- Comparison of oral and transdermal delivery for hormone stability
- Mechanism-of-action data and package insert warnings and contraindications
- A cardiovascular and thrombosis risk assessment for migraine patients

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Premarin Vaginal (conjugated estrogens) prescribing information, Wyeth Pharmaceuticals LLC, a subsidiary of Pfizer Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=96609623-528e-4aba-cabe-7254aed816d5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

