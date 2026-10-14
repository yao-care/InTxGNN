---
layout: default
title: Memantine
parent: Model Prediction Only (L5)
nav_order: 523
evidence_level: L5
indication_count: 4
---

# Memantine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Memantine: From Dementia to Pulmonary Hypertension

## One-Sentence Summary

Memantine is an NMDA receptor antagonist marketed in India as oral tablets. The registration text compiled for this report does not state its approved indication.
The TxGNN model's top-ranked prediction is **pulmonary hypertension** (score 99.5%), but this rests on model prediction alone, with **0 clinical trials** and **2 publications**, neither of which supports the indication.
The data compiled for this report show that the better-supported direction is **migraine disorder**, with **1 Phase 3 trial** and **19 publications** (see the notes below).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India registration data compiled for this report |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 (model prediction only) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

**Other predicted indications in the data:**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 2 | Migraine disorder | 99.52% | L1 (nominal) | Research question, worth pursuing |
| 3 | Kyphoscoliotic heart disease | 99.43% | L5 | Hold |
| 4 | Migraine with brainstem aura | 99.41% | L4 | Research question |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Memantine is generally known as a non-competitive NMDA receptor antagonist, which is the basis for the discussion below. This is general pharmacological knowledge, not drawn from the compiled data.

**Pulmonary hypertension (rank 1).** The mechanistic link is weak. One retrieved paper (PMID 33500723) is a preclinical study of NMDA receptor activation in insulin sensitivity and lipid metabolism. It mentions the glutamate/NMDAR axis in pulmonary arterial hypertension only in passing. The other paper (PMID 41739394) is a Phase 1 study of MN-08, a nitrate derivative of memantine, which is a different compound. Neither shows that memantine itself is effective. The high score should be treated as a model signal that needs independent validation.

**Migraine disorder (rank 2).** This link is more plausible. Glutamate/NMDA signalling is implicated in cortical spreading depression, central sensitisation and trigeminovascular activation. Reviews (PMID 36869904, 29508147) support this mechanism. However, an editorial titled "Memantine for migraine: big promise but little evidence" (PMID 34510445) cautions that the evidence base is thin.

**Migraine with brainstem aura (rank 4).** The link is indirect. It is extrapolated from general migraine and aura biology. The only RCT-type paper studied migraine without aura.

**Kyphoscoliotic heart disease (rank 3).** No mechanistic rationale, trials or literature were found.

## Clinical Trial Evidence

No clinical trials were registered for the top-ranked indication, pulmonary hypertension. The only trial in the compiled data is for migraine disorder (rank 2):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04698525](https://clinicaltrials.gov/study/NCT04698525) | Phase 3 | Completed | 33 | Memantine vs sodium valproate for prophylaxis of episodic migraine. Active-comparator design, not placebo-controlled. The small sample limits statistical power, and no results were available in the data. |

## Literature Evidence

**Pulmonary hypertension (rank 1)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33500723](https://pubmed.ncbi.nlm.nih.gov/33500723/) | 2021 | Preclinical/Mechanistic | Theranostics | NMDA receptor activation regulates insulin sensitivity and lipid metabolism. Pulmonary hypertension is mentioned only as background. |
| [41739394](https://pubmed.ncbi.nlm.nih.gov/41739394/) | 2026 | Phase 1 PK/Safety | Clin Drug Investig | Safety and pharmacokinetics of MN-08, a nitrate derivative of memantine, in healthy volunteers. Not memantine itself. |

**Migraine disorder (rank 2), selected publications**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33961371](https://pubmed.ncbi.nlm.nih.gov/33961371/) | 2021 | Meta-analysis of RCTs | Clin Neuropharmacol | Memantine vs placebo in migraine. The abstract notes that efficacy remains controversial. |
| [34352118](https://pubmed.ncbi.nlm.nih.gov/34352118/) | 2021 | Systematic review | Headache | Efficacy and safety of memantine for prophylaxis of episodic migraine. |
| [40978493](https://pubmed.ncbi.nlm.nih.gov/40978493/) | 2025 | Network meta-analysis | Front Pharmacol | Comparative efficacy and safety of oral preventive medications for migraine in adults. |
| [39467289](https://pubmed.ncbi.nlm.nih.gov/39467289/) | 2024 | Clinical practice guideline | Ann Intern Med | 2023 VA/DoD guideline on the treatment and prevention of migraine and tension-type headache. |
| [36869904](https://pubmed.ncbi.nlm.nih.gov/36869904/) | 2023 | Review | Naunyn Schmiedebergs Arch Pharmacol | Memantine and ketamine as potential anti-migraine agents. |
| [25159002](https://pubmed.ncbi.nlm.nih.gov/25159002/) | 2014 | Review | Ann Pharmacother | Efficacy and safety of memantine for prevention of primary headache disorders. |
| [29508147](https://pubmed.ncbi.nlm.nih.gov/29508147/) | 2018 | Review | Neurotherapeutics | Glutamate and its receptors as therapeutic targets in migraine. |
| [34510445](https://pubmed.ncbi.nlm.nih.gov/34510445/) | 2021 | Editorial | Headache | "Big promise but little evidence" for memantine in migraine. |
| [17901918](https://pubmed.ncbi.nlm.nih.gov/17901918/) | 2007 | Retrospective study | J Headache Pain | Retrospective study of 60 patients who received memantine as migraine prevention. |

**Migraine with brainstem aura (rank 4)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26638119](https://pubmed.ncbi.nlm.nih.gov/26638119/) | 2016 | RCT (indirect) | Headache | Randomised, double-blind, placebo-controlled study of memantine for prophylaxis of migraine without aura. Indirect evidence for this subtype. |
| [36983158](https://pubmed.ncbi.nlm.nih.gov/36983158/) | 2023 | Review/Mechanistic | J Clin Med | Targeting peripheral NMDA receptors as a novel migraine strategy. |

## India Market Information

Memantine has 20 valid single-ingredient registrations in India, all oral tablets. The approved indication text is not stated in the registration data. The main registrations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 121855 | Larentine 5 Tablet (La Renon Healthcare) | Strip of 10 tablets | Not stated |
| 140383 | Mentagen 10mg Tablet (Cellgen Biopharma) | Strip of 10 tablets | Not stated |
| 138971 | Memantal 5mg Tablet (East West Pharma) | Strip of 10 tablets | Not stated |
| 63272 | Demenzil 10mg Tablet (Alkem Laboratories) | Strip of 10 tablets | Not stated |
| 66929 | Dmentin 5mg Tablet MD (Micro Labs) | Strip of 10 tablets (MD) | Not stated |

## Safety Considerations

- **Disease contraindications from the knowledge graph:** Liver disease, gallbladder disease and impaired renal function. These come from drug-disease contraindication edges in the TxGNN knowledge graph, not from label text.
- **Drug interactions:** 100 interactions were found in total. The notable ones are:
  - **Moderate:** anticholinergic and antispasmodic agents, including hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, methscopolamine, propantheline, scopolamine, trospium and mepenzolate.
  - **Minor:** ranitidine, metformin, cimetidine and potassium citrate.
  - **Unknown severity:** glimepiride, doxycycline, lansoprazole, loperamide, famotidine and acetylsalicylic acid.

Please also refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold** for the top-ranked indication, pulmonary hypertension.

**Rationale:**
- The TxGNN score is very high (99.5%), but there are no clinical trials and the two retrieved papers do not support memantine in this condition. One concerns a different compound, MN-08.
- Migraine disorder (rank 2) is the more promising direction and is best treated as a research question. Its L1 label comes from a single small Phase 3 trial (n=33) with no available results, and the literature describes the evidence as limited.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indication text for the India registrations
- Detailed mechanism of action data
- For migraine: the results of NCT04698525 and replication in larger placebo-controlled trials
- For pulmonary hypertension: preclinical or clinical data on memantine itself, not on the derivative MN-08
- For kyphoscoliotic heart disease and migraine with brainstem aura: any supporting evidence for these subtypes before further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

