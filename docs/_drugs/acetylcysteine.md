---
layout: default
title: Acetylcysteine
parent: High Evidence (L1-L2)
nav_order: 21
evidence_level: L2
indication_count: 10
monitor_inn: "Acetylcysteine"
predicted_indications: ["thrombotic disease", "closed-angle glaucoma", "nasal cavity disease", "dry eye syndrome", "pharyngitis", "acute laryngopharyngitis", "tracheal disease", "transient ischemic attack (disease)", "laryngotracheitis", "angle-closure glaucoma"]
last_modified_at: 2026-11-24
description: "Acetylcysteine: predicted new indication Thrombotic disease (evidence level L2). In India: at least 20 listed products"
---

# Acetylcysteine
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

## Acetylcysteine: Thrombotic disease
{: .text-alpha }

## One-Sentence Summary

Acetylcysteine is a mucolytic and antioxidant thiol drug that is widely marketed in India.
The TxGNN model predicts it may be effective for **thrombotic disease**, with **7 clinical trials** and **20 publications** compiled for this direction.
The strongest support is in thrombotic microangiopathy (TA-TMA) and thrombotic thrombocytopenic purpura (TTP), not thrombosis in general.

<!-- review:begin in-lic-20261124c-acetylcysteine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Acetylcysteine is a mucolytic and antioxidant thiol drug that is widely marketed in India as single-ingredient products." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-acetylcysteine-1 -->

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L2 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for acetylcysteine: "Acetylcysteine has been shown to reduce the extent of liver injury following acetaminophen overdose. Acetaminophen doses of 150 mg/kg or greater have been associated with hepatotoxicity. Acetylcysteine probably protects the liver by maintaining or restoring the glutathione levels, or by acting as an alternate substrate for conjugation with, and thus detoxification of, the reactive metabolite of acetaminophen." ([DailyMed: Acetadote (acetylcysteine) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=472f158a-5ab9-4308-8e49-1116e6ea3d39), label version 2025-04-30; accessed 2026-11-19.) Based on the repurposing analysis, acetylcysteine is a thiol-based reducing agent. It can break disulfide bonds in von Willebrand factor (VWF), reducing multimer size and platelet-binding activity.

This is plausible for VWF-driven microvascular thrombosis such as TTP and transplant-associated thrombotic microangiopathy (TA-TMA). Its antioxidant activity may also reduce oxidative endothelial injury and platelet activation. Preclinical mouse and baboon TTP models support this mechanism (PMID 28011677).

The evidence is strongest for the TMA/TTP subset. It should not be extrapolated to venous or arterial thrombosis in general.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Phase 3 | Completed | 170 | Safety and efficacy of N-acetylcysteine in transplant-associated thrombotic microangiopathy; results should be verified |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Phase 2/3 | Active, not recruiting | 44 | Single-arm trial of N-acetylcysteine for TA-TMA; results not yet available |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Phase 2 | Completed | 40 | Randomized, double-blind, placebo-controlled cross-over trial (RENACTIF) on the thrombotic phenotype in renal insufficiency |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Early Phase 1 | Completed | 3 | Pilot of intravenous N-acetylcysteine in suspected TTP; too small for efficacy conclusions |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Phase 2 | Unknown | 44 | Dexamethasone plus acetylcysteine in newly diagnosed immune thrombocytopenia; indirect, combination design |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Phase 1/2 | Unknown | 200 | Atorvastatin, acetylcysteine and danazol in steroid-resistant or relapsed immune thrombocytopenia; indirect, combination |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Early Phase 1 | Completed | 15 | Atorvastatin plus N-acetylcysteine on platelet count in immune thrombocytopenia; indirect, combination |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35940529](https://pubmed.ncbi.nlm.nih.gov/35940529/) | 2022 | Randomized trial | Transplantation and Cellular Therapy | N-acetylcysteine as prophylaxis for TA-TMA in a placebo-controlled study |
| [41977015](https://pubmed.ncbi.nlm.nih.gov/41977015/) | 2026 | Systematic review | Journal of Clinical Medicine | Systematic review and critical appraisal of N-acetylcysteine in TTP |
| [42338865](https://pubmed.ncbi.nlm.nih.gov/42338865/) | 2026 | Systematic review | Cureus | Systematic review of N-acetylcysteine as adjunctive therapy in TTP |
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | Cohort study | Annals of Hematology | Retrospective study of N-acetylcysteine and in-hospital mortality in acquired TTP |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | Preclinical | Blood | N-acetylcysteine in mouse and baboon TTP models |
| [32243196](https://pubmed.ncbi.nlm.nih.gov/32243196/) | 2020 | Review | Expert Review of Hematology | Repurposed drugs for TTP, including N-acetylcysteine |
| [28416507](https://pubmed.ncbi.nlm.nih.gov/28416507/) | 2017 | Review | Blood | Overview of TTP pathophysiology and management |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Review | Journal of Clinical Medicine | TTP pathophysiology, diagnosis and management |
| [36410267](https://pubmed.ncbi.nlm.nih.gov/36410267/) | 2022 | Review | Journal of Infection and Public Health | N-acetylcysteine in COVID-19, which involves a prothrombotic state |

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 7554 | Acybronk Tablet | Strip of 10 tablets | Valid |
| 41444 | Coenac 400 Solution | Ampoule of 2 ml Injection | Valid |
| 73522 | Efetil Tablet | Strip of 10 tablets | Valid |
| 84091 | Fluimucil 600mg Tablet | Strip of 10 tablets | Valid |
| 87042 | Fluimucil Eff 600mg Tablet | Strip of 6 tablets | Valid |
| 133862 | Mucomelt A Tablet | Strip of 10 tablets | Valid |
| 134237 | Mucyst Injection | Vial of 2 ml Injection | Valid |
| 134850 | Mucyst 600mg Tablet | Strip of 10 tablets | Valid |
| 134951 | Manotab 600mg Tablet | Strip of 10 tablets | Valid |
| 138607 | Mucolix 600mg Tablet | Strip of 10 tablets | Valid |
| 140255 | Mucosys 1000mg Injection | Vial of 5 ml Injection | Valid |
| 141361 | Mucomeg AM 300mg/60mg Tablet | Strip of 10 tablets | Valid |
| 142381 | Mucoscan Injection | Ampoule of 2 ml Injection | Valid |
| 151932 | Nacomac 600mg Effervescent Tablet | Strip of 10 Effervescent Tablet | Valid |
| 153350 | Nacniva Tablet | Strip of 10 tablets | Valid |
| 153551 | Nacel 1000mg Injection | Vial of 5 ml Injection | Valid |
| 156069 | Nacyres Injection | Vial of 5 ml Injection | Valid |
| 162138 | Ovanac Tablet | Strip of 10 tablets | Valid |
| 162443 | Oxitres Tablet | Strip of 10 tablets | Valid |
| 234623 | Vexanac 600 Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

The data lists 20 valid licences, and the records may be partial. Dosage forms are oral tablets and injectables.

<!-- review:begin in-lic-20261124c-acetylcysteine-2 -->

> **Review correction (2026-11-24)**: Originally stated: "The data lists 20 valid single-ingredient licences, and the records may be partial." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-acetylcysteine-2 -->

## Safety Considerations

Detailed package insert warnings and contraindications are not available in the data compiled for this report; please refer to the package insert.

- **Drug Interactions**: 247 interactions were found in the interaction databases. Listed examples include activated charcoal (minor) and inhaled rapid-acting human insulin (moderate). Many others, such as bupropion, metformin, morphine, omeprazole, prednisone and vancomycin, have an unclassified severity.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level is L2. One completed Phase 3 trial (NCT03252925) and a completed randomized placebo-controlled cross-over trial (NCT03636932) tested acetylcysteine in thrombotic conditions. A randomized TA-TMA prophylaxis trial and systematic reviews in TTP add support. However, there are not multiple completed Phase 3 trials, and the evidence is concentrated in thrombotic microangiopathy rather than thrombosis broadly.

**To proceed, the following is needed:**
- Published results from NCT03252925 and the ongoing NCT07279610
- Restrict the claim to TA-TMA/TTP unless broader thrombotic evidence emerges
- Package insert warnings and contraindications for safety screening
- Mechanism of action data
- A review of interactions with anticoagulant and antiplatelet therapy in the target population

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data for the drug is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Acetadote (acetylcysteine) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=472f158a-5ab9-4308-8e49-1116e6ea3d39) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

