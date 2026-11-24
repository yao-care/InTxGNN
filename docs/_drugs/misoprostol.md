---
layout: default
title: Misoprostol
parent: Model Prediction Only (L5)
nav_order: 560
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Misoprostol: predicted new indication Amenorrhea (disease) (evidence level L5). Approved use: Not stated in the available India registration records"
monitor_inn: "Misoprostol"
predicted_indications: ["amenorrhea (disease)", "atypical coarctation of aorta"]
---

# Misoprostol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Misoprostol: From Obstetric/Gastric Use to Amenorrhea (Predicted)
{: .text-alpha }

## One-Sentence Summary

Misoprostol is a prostaglandin E1 analog marketed in India as 20 single-ingredient tablet registrations. The TxGNN model predicts it may be relevant to **amenorrhea**, but there are **0 registered clinical trials** and only **7 publications**, which mostly describe pregnancy termination rather than treatment of amenorrhea. The prediction is a computational hypothesis with weak direct support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available India registration records |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 0.9964 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for diclofenac sodium and misoprostol (a combination product containing misoprostol): "Misoprostol Misoprostol is a synthetic PGE1 analog with gastric antisecretory and mucosal protective properties. Misoprostol can increase bicarbonate and mucus production, but it has been shown at doses 200 mcg and above that are also antisecretory." ([DailyMed: diclofenac sodium and misoprostol prescribing information, Mylan Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a7701e8c-4e16-4165-8b83-de2c08d5ded3), label version 2026-08-31; accessed 2026-11-19.) Based on known information, misoprostol is a prostaglandin E1 analog that induces uterine contraction and cervical ripening. Its established uses are in pregnancy termination, missed abortion and uterine evacuation.

The retrieved literature concerns misoprostol, usually combined with mifepristone, for early medical abortion and prevention of unintended pregnancy. In those studies "amenorrhea" is only an inclusion criterion (gestation of ≤35 days of amenorrhea), and the outcome is restored menses or termination of pregnancy. None of it shows that misoprostol treats amenorrhea as a disease.

The high TxGNN score most likely reflects network proximity to reproductive and menstrual disorders, not direct therapeutic evidence. A plausible link exists only in narrow contexts, such as retained products of conception or intrauterine pathology. No evidence supports a general amenorrhea indication.

A second prediction, atypical coarctation of aorta (score 0.9930), has no trials or literature at all. Prostaglandin E1 analogs such as alprostadil keep the ductus arteriosus open, which is a conceptual link. However, misoprostol is an oral, uterine-acting drug with no established role there, and it carries teratogenic risk. This is a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reprod Sci | 744 women with amenorrhea ≤35 days compared hospital vs self-administered misoprostol after low-dose mifepristone for ultra-early medical abortion |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT (dose-ranging) | Reprod Sci | 2,500 women with ultra-early pregnancy received mifepristone 50–150 mg plus misoprostol 200 µg; the endpoint was complete abortion |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Cohort | Hum Reprod | Low-dose mifepristone plus misoprostol before expected menstruation to prevent unintended pregnancy |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Study on self-administered regimen | J Obstet Gynaecol Res | Safety and efficacy of self-administered misoprostol with low-dose mifepristone for early pregnancy termination |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Review | BMJ | Medical management of missed abortion and anembryonic pregnancy |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Review | J Obstet Gynaecol Can | Endometrial ablation for abnormal uterine bleeding (not specific to misoprostol) |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case report | Cureus | Acute fatty liver of pregnancy; amenorrhea appeared only as a presenting symptom |

## India Market Information

There are 20 valid single-ingredient registrations, with no cancelled ones. All are oral tablets. The available records do not include approved indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 35475 | Cytolog 600 Tablet | Strip of 1 Tablet | Valid |
| 45601 | Contrapill Duo Tablet | Strip of 10 tablets | Valid |
| 116713 | Kontrac 200mcg Tablet | Strip of 2 tablets | Valid |
| 122640 | L Pill 200mcg Tablet | Strip of 4 tablets | Valid |
| 133961 | Misoprost 25 Tablet | Strip of 4 tablets | Valid |
| 134439 | Mistol 200mcg Tablet | Strip of 4 tablets | Valid |
| 134673 | Miso-Gyn 200 Tablet | Strip of 4 tablets | Valid |
| 134794 | Misoclear 200mcg Tablet | Strip of 4 tablets | Valid |
| 135470 | M Prost 200mcg Tablet | Strip of 4 tablets | Valid |
| 139394 | Misogen 200mcg Tablet | Strip of 4 tablets | Valid |
| 139440 | Miso-Gyn 25mcg Tablet | Strip of 4 tablets | Valid |
| 140131 | Miso-Gyn 50mcg Tablet | Strip of 4 tablets | Valid |
| 140918 | Misogest 200mcg Tablet | Strip of 4 tablets | Valid |
| 141398 | Misopost 200mcg Tablet | Strip of 4 tablets | Valid |
| 143003 | Mizolast Tablet | Strip of 10 tablets | Valid |
| 148601 | Misobort 100mcg Tablet | Strip of 4 tablets | Valid |
| 179523 | Pregclear 200mcg Tablet | Strip of 4 tablets | Valid |
| 186575 | Rpitant 200mcg Tablet | Strip of 4 tablets | Valid |
| 216775 | Trust Miso Tablet | Strip of 4 tablets | Valid |
| 230560 | Uniprest Tablet | Strip of 4 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions:** 196 interactions were recorded. The main ones are:
  - **Major:** dinoprostone (topical).
  - **Moderate:** magnesium-containing antacids (magnesium oxide, magnesium carbonate, magnesium hydroxide, magaldrate) and quinapril.
  - **Minor:** sodium citrate, aluminum hydroxide, calcium carbonate, sodium bicarbonate and naproxen.
- **Knowledge-graph contraindication signals** (from a computational knowledge graph, not label text):
  - cardiovascular and cerebrovascular disease, including hypertension, heart failure, myocardial infarction and stroke
  - liver disease and liver failure
  - inflammatory bowel disease
  - asthma
  - blood coagulation disorders
  - anemia
  - active peptic ulcer disease
- **Pregnancy:** misoprostol is contraindicated in pregnancy because of teratogenic risk, including vascular disruption defects. This matters for any reproductive-age indication such as amenorrhea.

Please also refer to the package insert for authoritative warnings and contraindications, as label text was not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials exist, and the literature describes pregnancy termination, not treatment of amenorrhea. The TxGNN score is high, but evidence remains at the model-prediction and mechanism level (L4). Pregnancy-related risks make a speculative indication in women with amenorrhea unsafe to pursue without stronger data.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India registrations (currently missing, and blocking for safety screening)
- Approved indication text for the registered products
- Detailed mechanism of action data
- Targeted literature on misoprostol for a specific amenorrhea setting (for example, intrauterine adhesions or retained tissue), with controlled clinical data
- A pregnancy-exclusion and safety plan before any clinical use in women of reproductive age

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: diclofenac sodium and misoprostol prescribing information, Mylan Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a7701e8c-4e16-4165-8b83-de2c08d5ded3) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

