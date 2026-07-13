---
layout: default
title: Ketorolac
parent: 僅模型預測 (L5)
nav_order: 336
evidence_level: L5
indication_count: 3
---

# Ketorolac
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Ketorolac: From Acute Pain Management to Headache Disorder

## One-Sentence Summary

Ketorolac is a well-established non-steroidal anti-inflammatory drug (NSAID) widely used globally for acute pain management, including postoperative and musculoskeletal pain.
The TxGNN model predicts it may be effective for **Headache Disorder** (including migraine and tension-type headache),
with **36 clinical trials** and **19 publications** currently supporting this direction — many of which test ketorolac as the primary or reference intervention.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute pain management (not currently registered in India) |
| Predicted New Indication | Headache Disorder (migraine, tension-type headache) |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on well-established pharmacological knowledge, Ketorolac is a potent NSAID belonging to the pyrrolizine carboxylic acid class. It exerts its analgesic and anti-inflammatory effects primarily through non-selective inhibition of cyclooxygenase enzymes (COX-1 and COX-2), which reduces the biosynthesis of prostaglandins, thromboxanes, and prostacyclins. This mechanism underlies its efficacy across a broad range of pain conditions.

The connection to headache disorder is mechanistically sound. Prostaglandins — particularly PGE2 — play a well-documented role in sensitising trigeminal pain pathways, promoting neurogenic inflammation, and triggering vasodilation, all of which contribute to migraine attacks and tension-type headaches. By suppressing prostaglandin synthesis at the site of inflammation, Ketorolac can interrupt these pain cascades without acting on opioid receptors, making it an attractive non-opioid analgesic option in emergency and clinical headache management.

The clinical evidence further validates this prediction. Multiple Phase 3 and Phase 4 randomised controlled trials have specifically tested Ketorolac as a first-line or comparator treatment for acute migraine and tension-type headache in emergency department settings — across both adult and paediatric populations. Systematic reviews by major headache societies (American Headache Society, Canadian Headache Society) have explicitly included Ketorolac in their evidence-based treatment algorithms, cementing its role as a clinically recognised intervention in headache disorders.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01267864](https://clinicaltrials.gov/study/NCT01267864) | Phase 4 | Completed | 330 | Three-arm RCT comparing IV valproate, IV metoclopramide, and IV ketorolac for acute migraine in the ED |
| [NCT01011673](https://clinicaltrials.gov/study/NCT01011673) | Phase 4 | Completed | 123 | Ketorolac vs metoclopramide/diphenhydramine for acute tension-type headache in the ED |
| [NCT05641363](https://clinicaltrials.gov/study/NCT05641363) | Phase 3 | Completed | 171 | Dose-comparison RCT of ketorolac in children with acute pain (including headache) |
| [NCT02358681](https://clinicaltrials.gov/study/NCT02358681) | Phase 3 | Completed | 59 | Intranasal vs intravenous ketorolac for migraine in paediatric patients; non-inferiority design |
| [NCT00483717](https://clinicaltrials.gov/study/NCT00483717) | Phase 2 | Completed | 173 | Double-blind, placebo-controlled trial of intranasal ketorolac for acute migraine treatment |
| [NCT01807234](https://clinicaltrials.gov/study/NCT01807234) | Phase 4 | Completed | 72 | Ketorolac nasal spray vs sumatriptan nasal spray vs placebo for acute migraine abortive therapy |
| [NCT01596166](https://clinicaltrials.gov/study/NCT01596166) | Phase 4 | Completed | 56 | Combination IV ketorolac + metoclopramide for paediatric migraine in the ED |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | Unknown | 60 | Sub-dissociative ketamine vs ketorolac for acute tension-type headache in the ED |
| [NCT02664116](https://clinicaltrials.gov/study/NCT02664116) | Phase 4 | Unknown | 40 | IM ketorolac vs oral diclofenac potassium powder for severe migraine |
| [NCT06083571](https://clinicaltrials.gov/study/NCT06083571) | Phase 2 | Terminated | 41 | Intranasal ketorolac + oral adjuncts vs IV ketorolac for paediatric migraine; non-inferiority design |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [35138658](https://pubmed.ncbi.nlm.nih.gov/35138658/) | 2022 | Systematic Review & Meta-analysis | Academic Emergency Medicine | Evaluated efficacy of parenteral ketorolac specifically for acute migraine; pooled analysis of RCTs |
| [39674934](https://pubmed.ncbi.nlm.nih.gov/39674934/) | 2025 | Systematic Review & Bayesian Network Meta-analysis | Annals of Emergency Medicine | Compared pharmacological therapies for migraine in the ED; assessed relative efficacy and safety including ketorolac |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Clinical Guideline | Headache | 2025 AHS guideline update on parenteral pharmacotherapies for acute migraine management in the ED |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Evidence Assessment (Review) | Headache | American Headache Society updated evidence assessment of acute migraine pharmacotherapies |
| [24875925](https://pubmed.ncbi.nlm.nih.gov/24875925/) | 2015 | Systematic Review | Cephalalgia | Canadian Headache Society systematic review and recommendations for migraine pain treatment in emergency settings |
| [35670115](https://pubmed.ncbi.nlm.nih.gov/35670115/) | 2022 | RCT | Headache | RCT comparing IV metoclopramide alone vs metoclopramide + ketorolac in paediatric ED migraine; assessed efficacy and safety |
| [30783794](https://pubmed.ncbi.nlm.nih.gov/30783794/) | 2019 | RCT | Neurological Sciences | Prospective double-blind RCT comparing dexamethasone, metoclopramide, ketorolac, and chlorpromazine for migraine pain and recurrence |
| [37849443](https://pubmed.ncbi.nlm.nih.gov/37849443/) | 2024 | Systematic Review & Meta-analysis | Advances in Clinical and Experimental Medicine | Updated meta-analysis comparing IV ketorolac vs metoclopramide in adult migraine; synthesised recent trial data |
| [9484382](https://pubmed.ncbi.nlm.nih.gov/9484382/) | 1998 | RCT | Neurology | Three-arm controlled trial of IM ketorolac vs meperidine/promethazine vs placebo for acute tension-type headache |
| [1514724](https://pubmed.ncbi.nlm.nih.gov/1514724/) | 1992 | RCT | Annals of Emergency Medicine | Early RCT comparing IM ketorolac vs meperidine/hydroxyzine for acute migraine headache in the ED |

---

## India Market Information

Ketorolac currently has **no registered products in India**. No licence data is available for display.

---

## Safety Considerations

**Drug Interactions (222 interactions identified; key interactions listed below):**

| Severity | Interacting Drug(s) | Clinical Note |
|----------|---------------------|---------------|
| **Major** | Acetylsalicylic acid (Aspirin) | Concurrent use significantly increases risk of gastrointestinal bleeding and renal toxicity; combination generally contraindicated |
| **Moderate** | Corticosteroids (Betamethasone, Budesonide, Dexamethasone, Hydrocortisone) | Combined NSAID + steroid use increases GI ulceration and bleeding risk |
| **Moderate** | Sulfonylureas (Glimepiride, Glipizide, Glyburide, Chlorpropamide, Acetohexamide) | NSAIDs may enhance hypoglycaemic effect; blood glucose monitoring advised |
| **Moderate** | Levofloxacin | May increase risk of CNS adverse effects and seizures |
| **Moderate** | Kanamycin | Potential for additive nephrotoxicity |
| **Moderate** | Exenatide, Fenfluramine, Dexfenfluramine | Metabolic and pharmacodynamic interactions warranting monitoring |
| **Minor** | Famotidine, Ranitidine, Cimetidine | H2 blockers may alter ketorolac absorption or gastric protection context; clinically minor |

> **Note:** Detailed warnings and contraindications from Indian regulatory labelling (package insert) are not currently available. Please refer to the internationally approved prescribing information (e.g., FDA or EMA label) for full safety guidance pending local data acquisition.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence supporting Ketorolac for headache disorder is exceptionally strong — multiple completed Phase 3 and Phase 4 RCTs have directly tested its efficacy for acute migraine and tension-type headache, and it is explicitly endorsed in major international headache society guidelines (American and Canadian). The TxGNN prediction aligns with established clinical practice globally. However, Ketorolac is not currently marketed in India, and no local regulatory safety data (package insert, CDSCO approval status) has been retrieved, which creates a significant gap for market entry assessment.

**To proceed, the following is needed:**

- **Regulatory pathway in India:** Initiate CDSCO registration process or investigate whether Ketorolac can be imported under existing frameworks
- **Local safety labelling:** Obtain and review the full package insert from a reference agency (FDA/EMA) for warnings, contraindications, and special population data
- **Mechanism of action data:** Query DrugBank API (DB00465) to formally document COX-1/COX-2 inhibition profile for the regulatory dossier
- **Indication specificity:** Clarify the target indication (migraine vs tension-type vs post-dural puncture headache) to align with the most robust Phase 3 evidence for the regulatory submission
- **Formulation strategy:** Determine preferred route of administration (IV, IM, or intranasal) given India's clinical setting; intranasal formulation has Phase 3 non-inferiority data vs IV and may ease administration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

