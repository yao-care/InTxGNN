---
layout: default
title: Desvenlafaxine
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# Desvenlafaxine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Desvenlafaxine: From Major Depressive Disorder to Obsessive-Compulsive Disorder

## One-Sentence Summary

Desvenlafaxine is a serotonin-norepinephrine reuptake inhibitor (SNRI) with international approval (FDA) for the treatment of Major Depressive Disorder (MDD), though it is not currently marketed in India.
The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**, with **2 registered clinical trials** (indirect relevance) and **4 publications** — most notably an RCT demonstrating efficacy of its parent compound Venlafaxine in OCD — currently supporting this direction.
Direct clinical evidence for Desvenlafaxine as a primary OCD treatment is absent, placing this prediction at an early mechanistic stage requiring dedicated investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major Depressive Disorder (FDA-approved internationally; not marketed in India) |
| Predicted New Indication | Obsessive-Compulsive Disorder |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Desvenlafaxine is the primary active metabolite of Venlafaxine, belonging to the SNRI drug class. Its pharmacological mechanism centres on dual inhibition of the serotonin (5-HT) and norepinephrine (NE) reuptake transporters, with relatively greater potency at the serotonin transporter. This mechanism overlaps substantially with the established first-line pharmacotherapy for OCD — selective serotonin reuptake inhibitors (SSRIs) and the tricyclic agent clomipramine — both of which rely on enhanced serotonergic neurotransmission to reduce obsessive and compulsive symptom burden.

The strongest mechanistic bridge comes from Venlafaxine, Desvenlafaxine's parent compound. A double-blind RCT (PMID 14624187) directly compared Venlafaxine with Paroxetine (an SSRI) in 150 primary OCD patients, and a subsequent 2014 review (PMID 24766145) confirmed that serotonergic antidepressants — including SNRIs — demonstrate clinically meaningful effects in OCD. Since Desvenlafaxine is the pharmacologically active moiety responsible for the majority of Venlafaxine's CNS effects, class-level mechanistic extrapolation is scientifically reasonable.

Currently, detailed mechanism of action data for Desvenlafaxine is not formally available in this evidence pack. However, based on its established SNRI classification and its role as Venlafaxine's active metabolite, its serotonergic efficacy in MDD has been demonstrated in multiple Phase 3 RCTs, and mechanistically this property is directly relevant to OCD. The key limitation is the complete absence of a dedicated Desvenlafaxine-in-OCD clinical trial — the drug appears in the OCD trial landscape only as a prior treatment from which patients had an inadequate response (NCT03299166), not as an investigational agent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03299166](https://clinicaltrials.gov/study/NCT03299166) | Phase 2/3 | Completed | 426 | Evaluates adjunctive troriluzole vs. placebo in OCD patients with prior inadequate response to SSRIs, clomipramine, venlafaxine, or **desvenlafaxine**. Desvenlafaxine is listed as an eligible background treatment, not the investigational drug — confirms its use in OCD populations but does not assess its efficacy |
| [NCT01527786](https://clinicaltrials.gov/study/NCT01527786) | Phase 3 | Completed | 25 | Open-label pilot of Desvenlafaxine monotherapy for postpartum depression assessing functional recovery and mood outcomes. Indication does not match OCD; included for context as a Desvenlafaxine-specific trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [14624187](https://pubmed.ncbi.nlm.nih.gov/14624187/) | 2003 | RCT | Journal of Clinical Psychopharmacology | First randomised double-blind comparison of an SNRI (Venlafaxine) vs. Paroxetine in 150 primary OCD patients — directly supports the relevance of SNRI-class serotonergic activity for OCD; most critical mechanistic evidence for Desvenlafaxine extrapolation |
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Review | Expert Opinion on Pharmacotherapy | Updated review of double-blind studies testing 5-HT antidepressants in OCD; confirms the centrality of the serotonergic system to OCD pathophysiology and reviews SNRI data |
| [40224942](https://pubmed.ncbi.nlm.nih.gov/40224942/) | 2025 | Case Series | Psychiatry and Clinical Psychopharmacology | Risperidone augmentation in antidepressant-resistant somatic symptom disorder; references OCD as a relevant comorbidity — tangential relevance only |
| [36686097](https://pubmed.ncbi.nlm.nih.gov/36686097/) | 2022 | Review | Cureus | Comprehensive review of postpartum depression noting that untreated PPD can lead to later onset of OCD and anxiety disorders — provides indirect epidemiological association, not mechanistic evidence |

---

## India Market Information

Desvenlafaxine is **not currently approved or marketed in India**. No regulatory licenses are registered with CDSCO. The drug is internationally approved under the brand name **Pristiq** (Pfizer) for Major Depressive Disorder in adults, with approval held in the USA (FDA), EU, Canada, and several other markets. Any clinical development or compassionate use in India would require new regulatory filings from the ground up.

---

## Safety Considerations

**Drug Interactions:** Desvenlafaxine has a broad drug interaction profile with **184 documented interactions** recorded in the DDinter database. The following interactions warrant particular clinical attention:

| Severity | Interacting Drug | Clinical Concern |
|----------|-----------------|-----------------|
| Major | Bupropion | Elevated risk of seizures and serotonergic toxicity with combined use |
| Major | Lorcaserin | Serotonin syndrome risk due to 5-HT2C agonism combined with SNRI |
| Major | Fenfluramine / Dexfenfluramine | Serotonin syndrome risk via combined serotonergic activity |
| Major | Dolasetron / Granisetron | QT prolongation and serotonin syndrome risk |
| Major | Diethylpropion / Mazindol | CNS stimulant interaction; cardiovascular and CNS toxicity risk |
| Moderate | Epinephrine / Ephedrine (including topical/nasal/ophthalmic) | Potentiation of adrenergic cardiovascular effects |
| Moderate | Morphine | CNS and respiratory depression potentiation |
| Moderate | Acetylsalicylic acid | Increased risk of bleeding via platelet serotonin depletion |
| Moderate | Dronabinol | CNS depression and possible serotonergic interaction |
| Minor | Cimetidine | Possible modest increase in desvenlafaxine plasma exposure |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the SNRI mechanism of Desvenlafaxine provides a theoretically coherent basis for OCD treatment — substantiated by Venlafaxine RCT data (PMID 14624187) — no clinical trial has directly investigated Desvenlafaxine as a primary agent for OCD. The L4 evidence level reflects mechanistic plausibility rather than clinical proof, and the drug's absence from the Indian market adds a further regulatory barrier before any development pathway can begin.

**To proceed, the following is needed:**
- A dedicated Phase 2 proof-of-concept RCT of Desvenlafaxine in OCD (Y-BOCS as primary endpoint)
- Head-to-head or add-on comparison with established OCD treatments (fluvoxamine, sertraline, clomipramine)
- Full mechanism of action documentation, including receptor binding selectivity profile and 5-HT transporter occupancy data
- India regulatory strategy: CDSCO new drug application or import licence pathway assessment, as Desvenlafaxine is entirely absent from the Indian market
- Dose-ranging study for OCD — optimal dose may differ from the FDA-approved MDD dose (50–100 mg/day)
- Review of contraindications and TFDA/CDSCO-level safety warnings, which are currently unavailable (Data Gap DG001)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

