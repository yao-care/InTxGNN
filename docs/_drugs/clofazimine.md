---
layout: default
title: Clofazimine
parent: Model Prediction Only (L5)
nav_order: 200
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-20
description: "Clofazimine: predicted new indication Pneumocystosis (evidence level L5). Approved use: Pyoderma gangrenosum, leprosy, multibacillary leprosy"
monitor_inn: "Clofazimine"
predicted_indications: ["pneumocystosis", "malaria", "gastrin secretion abnormality"]
---

# Clofazimine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Clofazimine: From Pyoderma Gangrenosum and Leprosy to Pneumocystosis
{: .text-alpha }

## One-Sentence Summary

Clofazimine is an anti-leprosy drug, originally used for leprosy (including multibacillary leprosy) and pyoderma gangrenosum.
The TxGNN model predicts it may be effective for **Pneumocystosis**, but **no clinical trials** and only **3 publications** are available, none of which show clofazimine acting against Pneumocystis.
This prediction rests on the model alone and should be treated as a hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pyoderma gangrenosum, leprosy, multibacillary leprosy (approved indication text is not listed in the Indian licence records) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (11 of 11) – CDSCO approval status is not included in this data |
| Number of Listed Products | 11 (valid: 11) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for clofazimine: "LAMPRENE is an anti-mycobacterial drug. […] Clofazimine exerts a slow bactericidal effect on Mycobacterium leprae (Hansen’s bacillus). Clofazimine inhibits mycobacterial growth and binds preferentially to mycobacterial DNA. Clofazimine also exerts anti-inflammatory properties in treating erythema nodosum leprosum reactions." ([DailyMed: Lamprene (clofazimine) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2e07448f-f888-4747-80ab-570c1b621250), label version 2026-08-17; accessed 2026-11-19.) Based on known information, clofazimine is a long-established antimycobacterial agent used in multidrug leprosy therapy, and its efficacy in leprosy is established.

No credible mechanistic link to Pneumocystis has been established. The three papers retrieved concern opportunistic infections in AIDS in general, clofazimine as prophylaxis against *Mycobacterium avium* complex (MAC), and a case report of *M. kansasii* infection that was complicated by *Pneumocystis* pneumonia. In these papers, Pneumocystis is a co-occurring condition in people with AIDS, not a target of clofazimine.

The high score (0.9990) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as AIDS-related opportunistic infections, not biological evidence of antifungal activity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8501340](https://pubmed.ncbi.nlm.nih.gov/8501340/) | 1993 | Randomised open-label trial (MAC prophylaxis, not Pneumocystis-specific) | J Infect Dis | Clofazimine 50 mg tested as prophylaxis against disseminated MAC in 110 HIV patients, who had a prior Pneumocystis pneumonia episode or CD4 ≤100/mm³. The target was MAC, not Pneumocystis. |
| [2714863](https://pubmed.ncbi.nlm.nih.gov/2714863/) | 1989 | Case report | Infection | AIDS patient with *M. kansasii* lung disease complicated by Pneumocystis pneumonia. Recovered on a regimen including clofazimine; Pneumocystis was treated with trimethoprim-sulfamethoxazole. |
| [11363899](https://pubmed.ncbi.nlm.nih.gov/11363899/) | 1996 | Review | PI Perspective | General update on opportunistic infections. No Pneumocystis-specific efficacy for clofazimine. |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 123980 | Lepromine 50mg Capsule | Strip of 10 capsules | Not listed |
| 88207 | Fazim 50mg Capsule | Strip of 10 capsules | Not listed |
| 40009 | Clofros 50mg Capsule | Strip of 10 capsules | Not listed |
| 86739 | Feza 50 Capsule | Strip of 10 capsules | Not listed |
| 40922 | Clofozine 50mg Capsule | Box of 100 capsules | Not listed |

There are 11 valid single-ingredient registrations in total, all oral capsules. The five shown are the main ones.

---

## Safety Considerations

- **Contraindications (not label text)**: liver disease, gallbladder disease, diarrheal disease, active peptic ulcer disease, digestive system disease, intestinal disease, splenic infarction, splenic disease, hypersplenism.
- **Drug Interactions**: 111 interactions were found in total. Notable ones:
  - **Major**: cisapride, dolasetron
  - **Moderate**: famotidine, loperamide, bisacodyl, clarithromycin, levofloxacin, ondansetron, granisetron, palonosetron, and several laxatives (e.g. lactulose, magnesium hydroxide, polyethylene glycol)
  - **Minor**: metronidazole

Package insert warnings and contraindications were not available for this report; please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials and no literature showing clofazimine activity against Pneumocystis. The evidence is model-only (L5), and the literature mentions Pneumocystis only as a co-occurring condition.

**To proceed, the following is needed:**
- Mechanism of action data for clofazimine
- In vitro evidence of activity against *Pneumocystis* species
- Package insert warnings and contraindications from the Indian regulator
- A safety review of the gastrointestinal and splenic associations, and of the major interactions (cisapride, dolasetron)

---

### Other Predicted Indications (for reference)

- **Malaria (score 0.9960, Evidence Level L4, Research Question):** Only indirect preclinical support exists, such as in vitro antiplasmodial activity of clofazimine analogues (PMID 29026393). The other retrieved papers concern tuberculosis regimens or unrelated compounds. No malaria trials are registered.
- **Gastrin secretion abnormality (score 0.9960, Evidence Level L5, Hold):** No trials or literature are available, so the prediction is entirely unsupported.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Lamprene (clofazimine) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2e07448f-f888-4747-80ab-570c1b621250) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

