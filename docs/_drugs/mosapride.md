---
layout: default
title: Mosapride
parent: 僅模型預測 (L5)
nav_order: 436
evidence_level: L5
indication_count: 1
---

# Mosapride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Mosapride: From Gastrointestinal Disorders to Insomnia

## One-Sentence Summary

Mosapride is a selective 5-HT₄ receptor agonist (gastroprokinetic agent) approved in several South American and East Asian countries for the treatment of gastrointestinal disorders, including functional dyspepsia and gastroparesis, by accelerating gastric emptying.
The TxGNN model predicts it may be effective for **Insomnia**, with a prediction score of **99.87%**;
however, **0 clinical trials** and **0 publications** directly support this new indication, making this a model-only prediction at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gastrointestinal disorders (functional dyspepsia, gastroparesis); accelerates gastric emptying |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known pharmacological information from the DDI data, Mosapride is a selective 5-HT₄ receptor agonist in the gastroprokinetic drug class, with its efficacy in gastrointestinal disorders well established across multiple national regulatory approvals (primarily in South America and East Asia).

The theoretical mechanistic link to insomnia rests on two hypotheses. First, 5-HT₄ receptors are distributed not only in the gastrointestinal tract but also in the hippocampus and cerebral cortex, regions potentially involved in sleep regulation. However, Mosapride is actively effluxed by P-glycoprotein at the blood-brain barrier, resulting in extremely low CNS penetration (estimated < 1%), which severely undermines any direct central pharmacodynamic effect on sleep architecture.

Second, the gut-brain axis hypothesis proposes that by alleviating nocturnal gastrointestinal symptoms (e.g., functional dyspepsia or GERD), Mosapride might indirectly reduce sleep disturbances. While plausible, this mechanism is indirect and non-specific—it does not address the core pathophysiology of primary insomnia. The overall mechanistic link is considered **weak** and remains a speculative, indirect inference rather than a direct pharmacological rationale.

---

## Clinical Trial Evidence

> ⚠️ **Note:** 2 trials were retrieved by the evidence system, but both were assessed as **Grade C (not relevant)**. Neither trial tests Mosapride as an investigational drug for insomnia—Mosapride appears only as a background standard-of-care treatment for functional dyspepsia in both studies. These results are likely due to keyword co-occurrence during database retrieval and do not constitute supporting evidence for this repurposing hypothesis.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT07187492](https://clinicaltrials.gov/study/NCT07187492) | Phase 4 | Recruiting | 180 | **Irrelevant (Grade C)** — Investigational drug is *Bacillus coagulans* (probiotic) for anxiety/depression in functional dyspepsia. Mosapride used only as background GI treatment. |
| [NCT07182890](https://clinicaltrials.gov/study/NCT07182890) | Phase 4 | Recruiting | 180 | **Irrelevant (Grade C)** — Investigational drug is *Clostridium butyricum* (probiotic) for anxiety/depression in functional dyspepsia. Parallel design to NCT07187492; Mosapride again used only as background GI treatment. |

**Effective supporting trials for Mosapride + Insomnia: 0**

---

## Literature Evidence

Currently no related literature available for Mosapride in the treatment of insomnia.

---

## India Market Information

Mosapride is currently **not registered or marketed** in the India market. No license records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Known pharmacological note:** Mosapride acts as a selective agonist at the **5-HT₄ receptor** (gene: *HTR4*, Entrez: 3360, Ensembl: ENSG00000164270). This is the drug's primary pharmacological target rather than a drug-drug interaction per se, but co-administration with other serotonergic agents should be evaluated for potential additive serotonergic effects.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.87%), but this is a **purely model-driven signal (L5 evidence)**—there are no direct clinical trials, no published literature, and no regulatory approvals supporting Mosapride for insomnia. The mechanistic rationale is biologically weak: the drug's ultra-low CNS penetration (< 1% due to P-glycoprotein efflux) makes a direct central sleep-modulating effect implausible, and the indirect gut-brain axis pathway does not differentiate Mosapride from other GI agents.

**To proceed, the following is needed:**

- **MOA verification:** Obtain full mechanism of action data from DrugBank API (DG002) to confirm or refute any CNS activity
- **Safety package:** Retrieve TFDA/originator package insert warnings and contraindications (DG001, currently Blocking severity) before any safety assessment can proceed
- **Preclinical evidence:** Conduct a targeted literature search for animal sleep studies or CNS pharmacology studies involving 5-HT₄ agonists and sleep architecture
- **Indirect evidence search:** Investigate whether sleep quality improvement has been reported as a secondary endpoint in existing Mosapride GI trials
- **BBB penetration data:** Obtain quantitative CNS penetration data (Kp,uu,brain) to determine if any therapeutically relevant brain exposure is achievable
- **Regulatory feasibility:** Assess whether India/Taiwan registration is feasible given zero current market presence; a de novo regulatory filing would be required
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

