---
layout: default
title: Acetylsalicylic Acid
parent: Model Prediction Only (L5)
nav_order: 22
evidence_level: L5
indication_count: 7
monitor_inn: "Acetylsalicylic acid"
predicted_indications: ["atrophoderma vermiculata", "ulerythema ophryogenesis", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "trigeminal autonomic cephalalgia", "thrombophilia"]
last_modified_at: 2026-11-24
description: "Acetylsalicylic Acid: predicted new indication atrophoderma vermiculata (evidence level L5). In India: at least 20 listed products"
---

# Acetylsalicylic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Acetylsalicylic acid: Cyclooxygenase-inhibiting antiplatelet and anti-inflammatory agent → atrophoderma vermiculata
{: .text-alpha }

## One-Sentence Summary

Acetylsalicylic acid (aspirin) is a long-established oral drug that inhibits cyclooxygenase. The TxGNN model predicts it may be relevant to **atrophoderma vermiculata**, a rare skin disorder, with a prediction score of 0.9959. No clinical trials or publications were found for this prediction, so it rests on computation alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | atrophoderma vermiculata |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for aspirin and extended - release dipyridamole (a combination product containing acetylsalicylic acid): "Aspirin Aspirin inhibits platelet aggregation by irreversible inhibition of platelet cyclooxygenase and thus inhibits the generation of thromboxane A 2, a powerful inducer of platelet aggregation and vasoconstriction." ([DailyMed: Aspirin And Extended - Release Dipyridamole Capsules, 25 Mg / 200 Mg (aspirin and extended - release dipyridamole) prescribing information, Major Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a6e652e1-b2e4-47ba-bed2-c5e902f8b8f1), label version 2026-08-19; accessed 2026-11-19.) Aspirin is generally known to block cyclooxygenase enzymes, which reduces prostaglandin and thromboxane production and gives it antiplatelet, analgesic and anti-inflammatory effects.

The data compiled for this report did not identify any mechanistic rationale linking these actions to atrophoderma vermiculata. This condition is a rare follicular and atrophic skin disorder. The high score is a computational output only. It is not supported by any trial, case series or publication retrieved for this report, and the similarity to the drug's established uses has not been assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 6589 | Atorec Gold 75mg/10mg/75mg Tablet | Strip of 10 tablets | Valid |
| 8775 | Atromend-Gold-Forte Capsule | Strip of 10 capsules | Valid |
| 41882 | Cardiplet A Tablet | Strip of 10 tablets | Valid |
| 51093 | Clopivib A 75mg/75mg Tablet | Strip of 10 tablets | Valid |
| 62232 | Dilfit Gold 75mg/10mg/75mg Capsule | Strip of 10 capsules | Valid |
| 72413 | Ecosprin Gold 40 Capsule | Strip of 15 capsules | Valid |
| 100082 | Gatro AC 75mg/10mg/75mg Capsule | Strip of 10 capsules | Valid |
| 121162 | Lipirose-Gold 10 Capsule | Strip of 10 capsules | Valid |
| 150398 | Novastat Gold Tablet | Strip of 10 tablets | Valid |
| 164127 | Opvast Gold 75mg/10mg/75mg Tablet | Strip of 15 tablets | Valid |
| 165958 | Opvast Gold 75mg/20mg/75mg Tablet | Strip of 15 tablets | Valid |
| 184829 | Rosave-Gold 20mg Capsule | Strip of 10 capsules | Valid |
| 185142 | Roslaren AC 20 Capsule | Strip of 10 capsules | Valid |
| 186413 | Rosucrest-Gold 10 Capsule | Strip of 10 capsules | Valid |
| 187690 | Roztek Asp 75mg/20mg/75mg Capsule | Strip of 10 capsules | Valid |
| 187704 | Rosuvotin Gold 75mg/10mg/75mg Capsule | Strip of 10 capsules | Valid |
| 192252 | Rosuq Gold 75mg/10mg/75mg Capsule | Strip of 10 capsules | Valid |
| 195217 | Rosuper Gold 75mg/20mg/75mg Tablet | Strip of 10 tablets | Valid |
| 195249 | Rosuline Gold 150mg/10mg/75mg Capsule | Strip of 15 capsules | Valid |
| 216432 | Triopar 10 Capsule | Strip of 10 capsules | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Aspirin-containing products are currently marketed in India, and all licences in the local data are valid. These are oral products (capsules and tablets). The local records contain no approved-indication text.

---

## Safety Considerations

- **Drug Interactions**: The data compiled for this report contain 657 recorded interactions. Examples rated **Major** include:
  - acalabrutinib
  - acetazolamide
  - ketorolac
  - ibuprofen
  - fondaparinux
  - trastuzumab emtansine
  
  Examples rated **Moderate** include:
  - abciximab
  - nifedipine
  - hydrocortisone
  - ethanol
  - alendronic acid
  - fluvoxamine
  
  Bleeding risk with other antithrombotic or anti-inflammatory agents is the main theme.

Package insert warnings and contraindications were not retrieved. Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction has a high model score but no supporting trials, literature or mechanistic rationale, so it stays at evidence level L5.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological link to atrophoderma vermiculata
- Any case reports, preclinical work or other studies that directly address this condition
- Package insert warnings and contraindications for the marketed products
- An assessment of whether an oral antiplatelet or anti-inflammatory drug is a suitable route for a skin condition, with a bleeding-risk review

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for this drug were not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Aspirin And Extended - Release Dipyridamole Capsules, 25 Mg / 200 Mg (aspirin and extended - release dipyridamole) prescribing information, Major Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a6e652e1-b2e4-47ba-bed2-c5e902f8b8f1) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

