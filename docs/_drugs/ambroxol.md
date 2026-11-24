---
layout: default
title: Ambroxol
parent: Model Prediction Only (L5)
nav_order: 46
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
description: "Ambroxol: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Pharyngitis"
monitor_inn: "Ambroxol"
predicted_indications: ["nasal cavity disease", "vulvovaginal candidiasis", "faucial diphtheria", "cervical disc degenerative disorder"]
---

# Ambroxol
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

## Ambroxol: From Pharyngitis to Nasal Cavity Disease
{: .text-alpha }

## One-Sentence Summary

Ambroxol is a mucolytic/secretolytic (expectorant) agent, originally used to treat pharyngitis.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but the supporting evidence is thin: **0 clinical trials** and **1 publication** (a 2015 narrative article on acute cough that does not directly address the nasal cavity).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharyngitis |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ambroxol is a mucolytic/secretolytic agent that increases airway mucus clearance. It has also been reported to have local anaesthetic-like (sodium channel blocking) and anti-inflammatory effects.

Pharyngitis and nasal cavity disease both involve the upper airway mucosa. Mucus clearance and anti-inflammatory effects could plausibly relieve upper airway mucosal symptoms, which is consistent with ambroxol's existing use in pharyngitis.

The caveat is that the only linked article concerns acute cough, a lower respiratory tract problem, and does not directly address nasal cavity disease. The very high TxGNN score is a computational prediction only and is not backed by clinical data for this indication.

Other predictions in the list show how weak the evidence is across the board. Vulvovaginal candidiasis, faucial diphtheria and cervical disc degenerative disorder have no clear mechanistic link and no evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26525480](https://pubmed.ncbi.nlm.nih.gov/26525480/) | 2015 | Review / narrative article | Vestnik otorinolaringologii | Discusses treatment of acute cough associated with influenza and acute respiratory viral infection. Covers productive and non-productive cough. Concerns the lower airway and does not directly address nasal cavity disease. |

## India Market Information

A total of 20 valid registrations were found. Approved indication text was not available for any of them.

<!-- review:begin in-lic-20261124c-ambroxol-1 -->

> **Review correction (2026-11-24)**: Originally stated: "A total of 20 valid single-ingredient registrations were found." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-ambroxol-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 3034 | Abituss-LS Syrup | Bottle of 100 ml Syrup | Valid |
| 4370 | Abmont AL 75mg/5mg/10mg Tablet | Strip of 10 tablets | Valid |
| 9464 | Ambrodex AM Syrup Sugar Free | Bottle of 100 ml Syrup | Valid |
| 18883 | Aerodyn-CX Syrup Sugar Free | Bottle of 100 ml Syrup | Valid |
| 20792 | Alciz AM 75mg/5mg/10mg Tablet SR | Strip of 10 tablet sr | Valid |
| 27519 | Brocofil-DR Syrup Sugar Free | Bottle of 100 ml Syrup | Valid |
| 30370 | Brex Syrup | Bottle of 100 ml Syrup | Valid |
| 41805 | Cofodd LS Syrup | Bottle of 60 ml Syrup | Valid |
| 79288 | Eddycold Tablet | Strip of 10 tablets | Valid |
| 101147 | Genkoff XL Syrup | Bottle of 100 ml Syrup | Valid |
| 120129 | Kopkuf AM Syrup | Bottle of 100 ml Syrup | Valid |
| 127913 | Luzicough XP Syrup | Bottle of 100 ml Syrup | Valid |
| 131291 | Levcof AM Expectorant | Bottle of 60 ml Syrup | Valid |
| 149041 | M Roxt Syrup | Bottle of 100 ml Syrup | Valid |
| 154905 | New Ventakof Expectorant | Bottle of 100 ml Expectorant | Valid |
| 158797 | Notus AT Expectorant | Bottle of 100 ml Expectorant | Valid |
| 200985 | Sukuff Total Tablet | Strip of 15 tablets | Valid |
| 208293 | Sucroff D Kid Syrup | Bottle of 60 ml Syrup | Valid |
| 244291 | X Par A Tablet | Strip of 10 tablets | Valid |
| 245347 | Xeroc LS Syrup | Bottle of 60 ml Syrup | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: One pharmacological interaction was recorded, with glucosylceramidase beta (GBA1). Ambroxol acts as a chaperone for this enzyme. In acellular fluid at neutral pH it inhibits enzyme activity, while inside cells and acidic lysosomes it increases enzyme activity by raising the amount of enzyme reaching the lysosome. This is a target-level pharmacology finding, not a drug-drug interaction with a defined clinical severity level.

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests almost entirely on the TxGNN score. There are no registered clinical trials, and the single linked article concerns acute cough rather than nasal cavity disease. The evidence is at the L4 level, which is not enough to support moving forward.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian-marketed products (currently missing and blocking safety screening)
- Mechanism of action data (for example from DrugBank) to support the link to nasal cavity disease
- Literature and trials that directly address ambroxol in nasal or upper airway disease
- Approved indication text for the registered products, to confirm how the original indication is labelled in India
- Consideration of acute laryngopharyngitis as a closer-to-label alternative, although it also currently has no direct evidence

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

