---
layout: default
title: Indacaterol
parent: Model Prediction Only (L5)
nav_order: 430
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "Indacaterol"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "headache disorder", "trigeminal autonomic cephalalgia", "paratenonitis", "calcific tendinitis", "hypertrichosis (disease)", "bronchial disease", "myositis", "anaphylaxis", "Ambras type hypertrichosis universalis congenita"]
description: "Indacaterol: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not recorded in the local data"
---

# Indacaterol
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

## Indacaterol: Nephrogenic syndrome of inappropriate antidiuresis
{: .text-alpha }

## One-Sentence Summary

Indacaterol is an ultra-long-acting beta2-agonist bronchodilator, marketed in India for obstructive airway disease. The TxGNN model predicts it may be effective for **Bronchial Disease**, with **22 clinical trials** and **20 publications** currently supporting this direction. This largely reflects the drug's existing respiratory use (asthma and COPD) rather than a true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9954 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 9 of 9) |
| Number of Registrations | 9 (valid: 9) |
| Recommended Decision | Proceed with Guardrails |

Note: The data compiled for this report predicted 10 candidate indications. Bronchial disease is the only one with clinical trial and literature support. The other nine (for example nephrogenic syndrome of inappropriate antidiuresis, headache disorder, anaphylaxis and myositis) have no trials or publications and remain at Hold. Bronchial disease is therefore the focus of this report.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. From known pharmacology, indacaterol is an ultra-long-acting beta2-adrenergic agonist. It relaxes airway smooth muscle through cAMP-mediated signalling, which produces sustained bronchodilation with once-daily dosing.

Bronchial disease is a broad category that includes obstructive airway conditions such as asthma and COPD. Bronchodilation is a direct mechanistic fit for these conditions, so the prediction is biologically plausible. Phase 3 trials of indacaterol-containing combinations (indacaterol/mometasone, and indacaterol/glycopyrronium/mometasone) in asthma, together with Phase 2 dose-finding studies, support the link.

Two caveats apply. First, this is essentially the drug's established respiratory use, not a new therapeutic area. Second, much of the Phase 3 evidence comes from fixed-dose combinations, so those results cannot be attributed to indacaterol alone.

---

## Clinical Trial Evidence

The 10 most relevant of the 22 registered trials are listed below, prioritised by relevance grade and trial phase.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02554786](https://clinicaltrials.gov/study/NCT02554786) | Phase 3 | Completed | 2216 | 52-week study of indacaterol/mometasone (QMF149) versus mometasone alone in poorly controlled asthma |
| [NCT00529529](https://clinicaltrials.gov/study/NCT00529529) | Phase 3 | Completed | 805 | 26-week safety study of indacaterol 300 and 600 µg versus salmeterol in moderate to severe persistent asthma |
| [NCT01079130](https://clinicaltrials.gov/study/NCT01079130) | Phase 3 | Completed | 511 | 14-day bronchodilator efficacy of indacaterol versus placebo and salmeterol in persistent asthma |
| [NCT04259164](https://clinicaltrials.gov/study/NCT04259164) | Phase 3 | Completed | 28 | Glycopyrronium added to indacaterol/mometasone, anti-inflammatory effect on the allergen-induced late asthmatic response |
| [NCT00403637](https://clinicaltrials.gov/study/NCT00403637) | Phase 2/3 | Completed | 45 | Single doses of indacaterol 150, 300 and 600 µg versus placebo and formoterol in persistent asthma |
| [NCT00545272](https://clinicaltrials.gov/study/NCT00545272) | Phase 2 | Completed | 392 | 14-day dose-ranging of four indacaterol doses in adults and adolescents with persistent asthma |
| [NCT01609478](https://clinicaltrials.gov/study/NCT01609478) | Phase 2 | Completed | 335 | 12-week study of indacaterol acetate 75 and 150 µg in persistent asthma, supporting dose selection for QMF149 |
| [NCT01156844](https://clinicaltrials.gov/study/NCT01156844) | Phase 2 | Completed | 191 | Three dosing regimens of indacaterol maleate versus placebo in persistent asthma |
| [NCT02892019](https://clinicaltrials.gov/study/NCT02892019) | Phase 2 | Completed | 79 | Indacaterol acetate 75 and 150 µg in children aged 6 to 11 with asthma |
| [NCT04206761](https://clinicaltrials.gov/study/NCT04206761) | Phase 3 | Withdrawn | 0 | Xenon MRI study of triple therapy (QVM149); withdrawn with no participants enrolled, so it provides no evidence |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32653074](https://pubmed.ncbi.nlm.nih.gov/32653074/) | 2020 | RCT (Phase 3, IRIDIUM) | Lancet Respir Med | Once-daily single-inhaler mometasone-indacaterol-glycopyrronium versus mometasone-indacaterol or fluticasone-salmeterol in inadequately controlled asthma |
| [34783265](https://pubmed.ncbi.nlm.nih.gov/34783265/) | 2022 | RCT-classified review | Expert Rev Respir Med | Inhaled indacaterol/glycopyrronium/mometasone fixed-dose combination in moderate to severe asthma |
| [33871819](https://pubmed.ncbi.nlm.nih.gov/33871819/) | 2021 | Review | Drugs | Review of indacaterol/glycopyrronium/mometasone (Enerzair Breezhaler) in asthma |
| [31425937](https://pubmed.ncbi.nlm.nih.gov/31425937/) | 2019 | Review | Respir Med | Ultra-LABAs in asthma, which are prescribed only alongside an inhaled corticosteroid |
| [22611179](https://pubmed.ncbi.nlm.nih.gov/22611179/) | 2012 | Review | Pharmacol Rev | Pharmacology and therapeutics of bronchodilators in airway disorders |
| [23348973](https://pubmed.ncbi.nlm.nih.gov/23348973/) | 2013 | Review | Am J Respir Crit Care Med | Beta2-agonist therapy in lung disease |
| [19609496](https://pubmed.ncbi.nlm.nih.gov/19609496/) | 2009 | Review | Adv Ther | Indacaterol as a once-daily LABA producing rapid, sustained bronchodilation in COPD and asthma |
| [22499359](https://pubmed.ncbi.nlm.nih.gov/22499359/) | 2012 | Review | Pharmacotherapy | Indacaterol as an ultra-long-acting beta2-agonist for COPD |
| [40887869](https://pubmed.ncbi.nlm.nih.gov/40887869/) | 2025 | Pharmacology study | Pharmacol Res Perspect | Molecular pharmacological comparison of short, long and ultra-long-acting beta2-agonists |
| [25176969](https://pubmed.ncbi.nlm.nih.gov/25176969/) | 2014 | Review | Eur Respir Rev | Long-acting bronchodilators in COPD, including indacaterol and indacaterol/glycopyrronium |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 107811 | Indamet 160 Capsule | Bottle of 15 capsules | Not stated |
| 120933 | Loftair Capsule | Strip of 10 capsules | Not stated |
| 150680 | Nistami Ecopack | Box of 30 capsules | Not stated |
| 164416 | Onbrez 300mcg Breezhaler | Packet of 1 kit | Not stated |
| 163214 | Onbrez 150mcg Breezhaler | Packet of 1 kit | Not stated |

All 9 registrations are valid single-ingredient licences. The remaining four are Loftair-L Capsule with Inhaler, Indamet 80 Capsule, Indamet 320 Capsule and Sequadra Inhaler.

---

## Safety Considerations

- **Disease associations from the knowledge graph (not label text):** The drug-disease contraindication links in the knowledge graph include hypertension, long QT syndrome and other heart conduction disease, sudden cardiac arrest, coronary artery disease, epilepsy, diabetes mellitus and diabetic ketoacidosis, hyperglycaemia, potassium deficiency, and thyrotoxicosis (hyperthyroidism, Graves disease). These are cautions to verify against the label, not confirmed contraindications.
- **Drug Interactions:** The interaction screening found 440 interacting drugs. Examples of moderate interactions include epinephrine, clarithromycin, and the antidiabetic drugs metformin, pioglitazone, alogliptin, saxagliptin, canagliflozin, dapagliflozin and chlorpropamide. Minor interactions include several corticosteroids (hydrocortisone, dexamethasone, budesonide and others) and aprepitant.

Please refer to the package insert for warnings and contraindications, since label text was not available in the compiled data.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2 and Phase 3 trials, plus a Phase 3 RCT publication, support indacaterol-based therapy in airway disease, and the mechanism is a direct fit. However, the evidence largely reflects the drug's existing respiratory use, and the key Phase 3 data come from combination products.

**To proceed, the following is needed:**
- Confirmation of the approved indications on the Indian licences, since the indication text is blank
- Package insert warnings and contraindications for the Indian products
- Detailed mechanism of action data
- Clarification of what "bronchial disease" adds beyond the existing asthma and COPD indications
- Separation of indacaterol monotherapy effects from combination-product data
- A cardiovascular, metabolic and QT safety review, given the knowledge-graph cautions and the large number of interacting drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

