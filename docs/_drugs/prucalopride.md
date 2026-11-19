---
layout: default
title: Prucalopride
parent: Model Prediction Only (L5)
nav_order: 710
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
description: "Prucalopride: predicted new indication Hypoalphalipoproteinemia (evidence level L5). Approved use: Constipation disorder"
monitor_inn: "Prucalopride"
predicted_indications: ["hypoalphalipoproteinemia", "homozygous familial hypercholesterolemia", "duodenal ulcer (disease)", "oral candidiasis", "obsolete familial combined hyperlipidemia", "amyloidosis (disease)", "strongyloidiasis", "HIV infectious disease", "primary amyloidosis", "acquired amyloid peripheral neuropathy"]
---

# Prucalopride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Prucalopride: From Constipation Disorder to Hypoalphalipoproteinemia
{: .text-alpha }

## One-Sentence Summary

Prucalopride is a selective 5-HT4 receptor agonist originally used to treat constipation disorder.
The TxGNN model predicts it may be effective for **hypoalphalipoproteinemia** (low HDL cholesterol), but this is a TxGNN model (deep learning) prediction only,
with **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constipation disorder |
| Predicted New Indication | Hypoalphalipoproteinemia |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for prucalopride: "Prucalopride, a selective serotonin type 4 (5-HT 4 ) receptor agonist, is a gastrointestinal (GI) prokinetic agent that stimulates colonic peristalsis (high-amplitude propagating contractions [HAPCs]), which increases bowel motility. Prucalopride was devoid of effects mediated via 5-HT 2A, 5-HT 2B, 5-HT 3, motilin or CCK-A receptors in vitro at concentrations exceeding 5-HT 4 receptor affinity by 150-fold or greater." ([DailyMed: Motegrity (prucalopride) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bca1e4c6-4b2b-4876-8ab3-654629c4ff1b), label version 2025-07-17; accessed 2026-11-19.) Based on known information, prucalopride is a selective 5-HT4 receptor agonist that enhances gut motility, and its efficacy in constipation disorder is established.

For hypoalphalipoproteinemia, however, no mechanistic link can be identified. No established pathway connects 5-HT4 agonism to HDL metabolism. The very high TxGNN score (0.9982) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological or clinical evidence, and should be treated as a hypothesis-generating signal only.

Other top-ranked predictions show the same pattern. Most lipid disorders (homozygous familial hypercholesterolemia, familial combined hyperlipidemia), infections (oral candidiasis, strongyloidiasis, HIV) and duodenal ulcer have no plausible mechanistic basis. The only partially plausible direction is amyloidosis-related gut dysmotility (amyloidosis, primary amyloidosis), where a prokinetic might give symptomatic relief of intestinal pseudo-obstruction without treating the underlying disease. These have only indirect literature support (a case report and a motility-diagnosis study, neither testing prucalopride).

## India Market Information

Prucalopride has 20 valid single-ingredient registrations in India, all oral tablets. Approved indication text is not available for these registrations. Main examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 174899 | Prudac 1 Tablet (Zydus Cadila) | Strip of 10 tablets | Not specified |
| 174283 | Prusent 1mg Tablet (Lupin Ltd) | Strip of 10 tablets | Not specified |
| 39195 | Convio 2mg Tablet (Wellvio Healthcare Pvt Ltd) | Strip of 10 tablets | Not specified |
| 174810 | Prucapla 1mg Tablet (Cipla Ltd) | Strip of 10 tablets | Not specified |
| 176052 | Prucalor 2mg Tablet (Ajanta Pharma Ltd) | Strip of 10 tablets | Not specified |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not label text): ulcerative colitis, inflammatory bowel disease, intestinal perforation.
- **Drug Interactions**: 98 interactions are recorded. Examples include:
  - Moderate: aclidinium, levonorgestrel, norethisterone, ethinylestradiol, and anticholinergics such as hyoscyamine, atropine, benztropine, biperiden, glycopyrronium and clidinium.
  - Minor: nifedipine, afatinib, alpelisib, amiodarone, cobicistat, captopril, diltiazem, spironolactone, carvedilol and conivaptan.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication hypoalphalipoproteinemia has no clinical trials, no literature and no plausible mechanistic link to 5-HT4 agonism, so the high TxGNN score is not backed by evidence (Evidence Level L5).

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian market, which are needed for safety screening
- Detailed mechanism of action data
- A credible biological rationale linking 5-HT4 agonism to HDL metabolism, supported by preclinical data
- Consideration of the amyloidosis-related gut dysmotility direction (the only partially plausible candidate, ranked as a research question) in place of the top-ranked lipid prediction, along with controlled studies of prucalopride in that setting

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Motegrity (prucalopride) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bca1e4c6-4b2b-4876-8ab3-654629c4ff1b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

