---
layout: default
title: Ketorolac
parent: High Evidence (L1-L2)
nav_order: 464
evidence_level: L1
indication_count: 3
last_modified_at: 2026-10-30
description: "Ketorolac: predicted new indication Headache disorder (evidence level L1). Approved use: Atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis"
monitor_inn: "Ketorolac"
predicted_indications: ["headache disorder", "rosacea conjunctivitis", "trigeminal autonomic cephalalgia"]
---

# Ketorolac
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **3** 
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

## Ketorolac: From Allergic Conjunctivitis (Atopic, Papillary, Vernal) to Headache Disorder
{: .text-alpha }

## One-Sentence Summary

Ketorolac is a non-steroidal anti-inflammatory drug (NSAID). The original indications in the knowledge base are atopic, papillary and vernal conjunctivitis.
The TxGNN model predicts it may be effective for **headache disorder** (mainly migraine and tension-type headache),
with **17 clinical trials** and **19 publications** currently supporting this direction, including several systematic reviews and meta-analyses.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis (from the knowledge base; no approved indication text is available in the India licence records) |
| Predicted New Indication | Headache disorder |
| TxGNN Prediction Score | 0.9943 |
| Evidence Level | L1 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available in the data compiled for this report. Ketorolac is a non-selective COX-1/COX-2 inhibitor (an NSAID) that reduces prostaglandin synthesis. This is a well-established mechanism for the drug class.

Its original ocular indications are inflammatory conditions of the eye surface, where reducing prostaglandins eases inflammation and discomfort. Prostaglandins also contribute to peripheral and central sensitization and neurogenic inflammation in migraine and tension-type headache. COX inhibition therefore offers a plausible analgesic mechanism for headache, and the same anti-inflammatory action explains why the model links the two conditions.

Clinical practice already reflects this link: injectable ketorolac is widely used in emergency departments for acute migraine, and several trials have tested intravenous and intranasal formulations.

## Clinical Trial Evidence

Of the 17 trials in the data, the 10 most relevant are listed below. Ketorolac is the direct intervention in some and an active comparator or background therapy in others.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01807234](https://clinicaltrials.gov/study/NCT01807234) | Phase 4 | Completed | 72 | Ketorolac nasal spray vs sumatriptan nasal spray vs placebo for acute migraine |
| [NCT00483717](https://clinicaltrials.gov/study/NCT00483717) | Phase 2 | Completed | 173 | Double-blind, placebo-controlled study of intranasal ketorolac for acute migraine |
| [NCT01596166](https://clinicaltrials.gov/study/NCT01596166) | Phase 4 | Completed | 56 | IV ketorolac plus metoclopramide for pediatric migraine in the emergency department |
| [NCT02358681](https://clinicaltrials.gov/study/NCT02358681) | Phase 3 | Completed | 59 | Intranasal vs intravenous ketorolac for pediatric migraine (non-inferiority) |
| [NCT01267864](https://clinicaltrials.gov/study/NCT01267864) | Phase 4 | Completed | 330 | IV valproate vs IV metoclopramide vs IV ketorolac for acute migraine |
| [NCT01011673](https://clinicaltrials.gov/study/NCT01011673) | Phase 4 | Completed | 123 | Metoclopramide/diphenhydramine vs ketorolac alone for tension-type headache |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | Unknown | 60 | Ketamine vs ketorolac for tension-type headache |
| [NCT06083571](https://clinicaltrials.gov/study/NCT06083571) | Phase 2 | Terminated | 41 | Intranasal ketorolac combination vs IV ketorolac regimen in pediatric migraine |
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Phase 3 | Completed | 80 | Intranasal ketamine vs standard therapy for primary headache in the emergency department |
| [NCT06729047](https://clinicaltrials.gov/study/NCT06729047) | Phase 1/2 | Not yet recruiting | 330 | Neostigmine plus atropine vs ketorolac for post-dural puncture headache |

Several other trials, including withdrawn studies with no enrollment, provide no usable efficacy data and are omitted.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35138658](https://pubmed.ncbi.nlm.nih.gov/35138658/) | 2022 | Systematic review / meta-analysis | Acad Emerg Med | Efficacy of parenteral ketorolac in acute migraine attacks |
| [37849443](https://pubmed.ncbi.nlm.nih.gov/37849443/) | 2024 | Systematic review / meta-analysis | Adv Clin Exp Med | IV ketorolac vs metoclopramide in adult migraine |
| [39674934](https://pubmed.ncbi.nlm.nih.gov/39674934/) | 2025 | Systematic review / network meta-analysis | Ann Emerg Med | Comparative effectiveness and safety of migraine therapies in the emergency department |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline | Headache | American Headache Society update on parenteral drugs for acute migraine in the emergency department |
| [23298250](https://pubmed.ncbi.nlm.nih.gov/23298250/) | 2013 | Systematic review | Headache | Effectiveness of parenteral ketorolac in acute migraine |
| [35670115](https://pubmed.ncbi.nlm.nih.gov/35670115/) | 2022 | RCT | Headache | Adding IV ketorolac to metoclopramide in children with migraine in the emergency department |
| [30783794](https://pubmed.ncbi.nlm.nih.gov/30783794/) | 2019 | RCT | Neurol Sci | IV dexamethasone, metoclopramide, ketorolac and chlorpromazine compared for migraine pain relief and recurrence |
| [24875925](https://pubmed.ncbi.nlm.nih.gov/24875925/) | 2015 | Systematic review / recommendations | Cephalalgia | Canadian Headache Society recommendations for migraine in emergency settings |
| [24433525](https://pubmed.ncbi.nlm.nih.gov/24433525/) | 2014 | Systematic review | Headache | Parenteral treatment of episodic tension-type headache |
| [1514724](https://pubmed.ncbi.nlm.nih.gov/1514724/) | 1992 | RCT | Ann Emerg Med | IM ketorolac vs meperidine plus hydroxyzine for acute migraine |

## India Market Information

Twenty valid single-ingredient registrations are on record, covering oral tablets (mostly dispersible), injections and ophthalmic solutions. No approved indication text is available for any of them. The five main registrations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 117966 | Ketoserve 30mg Injection | Vial of 1 injection | Not stated |
| 118190 | Ketam Injection | Vial of 1 ml injection | Not stated |
| 137470 | Mighty Mox-KT Eye Drop | Bottle of 5 ml ophthalmic solution | Not stated |
| 164392 | Olopine-KT Eye Drop | Bottle of 5 ml eye drop | Not stated |
| 216327 | Torodent-DT Tablet | Strip of 6 dispersible tablets | Not stated |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (not taken from label text): hypertension, peptic ulcer disease (including active disease), liver disease, gallbladder disease, rheumatoid arthritis, inflammatory bowel disease, asthma, diabetes mellitus, diabetic ketoacidosis, blood coagulation disorders, haemophilia, stroke and cerebrovascular disorders, myocardial infarction, anaemia and haemoglobinopathy, impaired renal function, cardiovascular and heart disease, and dry eye syndrome.
- **Drug Interactions**: 222 interactions are recorded. The major interaction listed is acetylsalicylic acid (aspirin). Moderate interactions include corticosteroids (betamethasone, budesonide, dexamethasone, hydrocortisone), sulfonylureas (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide), exenatide, levofloxacin, kanamycin, balsalazide and fenfluramine. Minor interactions include famotidine, ranitidine, cimetidine and linaclotide. A case report also describes lithium toxicity when ketorolac was co-administered.

Package insert warnings and contraindications were not available for this report, so please refer to the package insert for the official safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2 to 4 trials, together with systematic reviews, meta-analyses and an updated guideline, support ketorolac for acute migraine and tension-type headache, and the drug is already widely registered in India. However, the safety profile (gastrointestinal, renal, cardiovascular and bleeding risks) requires strict controls, and the package insert data was not available.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India products, since the missing safety data blocks formal safety screening
- Detailed mechanism of action data from DrugBank
- Confirmation of the approved indications and routes of the registered injectable and nasal/oral products for headache use
- Guardrails: avoid in patients with GI bleeding risk, renal impairment, cardiovascular disease or pregnancy; limit treatment duration; check drug interactions (e.g. lithium); use careful dosing in children
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

