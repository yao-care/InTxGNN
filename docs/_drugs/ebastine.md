---
layout: default
title: Ebastine
parent: 僅模型預測 (L5)
nav_order: 258
evidence_level: L5
indication_count: 10
---

# Ebastine
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

# Ebastine: From Allergic Rhinitis to Coronary Artery Disease

## One-Sentence Summary

Ebastine is a second-generation, selective H1-receptor antagonist primarily used for allergic rhinitis and chronic urticaria.
The TxGNN model predicts it may be effective for **Coronary Artery Disease**,
with **0 clinical trials** and **1 computational study** currently available — making this an early-stage research hypothesis requiring substantial further investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis / Chronic urticaria (H1 antihistamine) |
| Predicted New Indication | Coronary Artery Disease |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ebastine is a selective, second-generation H1 histamine receptor antagonist. Unlike first-generation antihistamines, it does not cross the blood-brain barrier readily, resulting in a non-sedating profile. It is metabolized in the liver — notably, it is a known substrate of the cytochrome P450 enzyme **CYP2J2**, which is the mechanistic hook underlying this TxGNN prediction.

CYP2J2 plays a role in the epoxidation of arachidonic acid to produce **epoxyeicosatrienoic acids (EETs)**, compounds with documented cardioprotective properties including vasodilation, anti-inflammatory effects, and reduction of ischemia/reperfusion injury. Because Ebastine competes for CYP2J2 binding, it could theoretically modulate EET production pathways and, by extension, influence coronary vascular biology. Additionally, H1 receptor blockade may reduce mast cell-mediated inflammation in coronary vasculature, providing a second indirect mechanistic rationale.

However, this chain of reasoning is highly speculative. The link from "CYP2J2 substrate" to "coronary artery disease treatment" involves multiple unverified steps, and there is currently **no direct clinical or preclinical evidence** connecting Ebastine to cardiovascular benefit. The TxGNN model has likely captured a graph-level association between Ebastine's metabolic enzyme (CYP2J2) and cardiovascular disease nodes in the knowledge graph — not a validated therapeutic relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18004755](https://pubmed.ncbi.nlm.nih.gov/18004755/) | 2008 | Computational / In silico | *Proteins* | Homology modeling and molecular dynamics simulation of CYP2J2's active site; finds CYP2J2 catalyzes arachidonic acid epoxidation linked to coronary artery disease and hypertension — Ebastine identified as a ligand candidate for this enzyme |

> **Note:** This study does not test Ebastine therapeutically. It models the CYP2J2 binding site and notes the enzyme's association with CAD. The inclusion of Ebastine as a CYP2J2 substrate in this context is the sole indirect literary connection to coronary artery disease.

---

## India Market Information

Ebastine is **not currently registered or marketed in India**. No license records are available.

---

## Safety Considerations

Detailed safety data (package insert warnings, contraindications, and drug-drug interactions) were not retrieved in this evidence pack. Please refer to the published prescribing information for Ebastine for complete safety details.

Based on the known drug class profile:
- Ebastine is a **second-generation H1 antihistamine** with a generally favorable safety profile compared to first-generation agents
- QTc prolongation has been reported with some second-generation antihistamines; cardiac monitoring considerations may be relevant given the cardiovascular indication being explored
- CYP2J2 substrate status means co-administration with other CYP2J2 inhibitors/inducers may alter pharmacokinetics

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score of 99.18% reflects a model-level signal — likely driven by Ebastine's known CYP2J2 substrate relationship rather than direct pharmacological evidence for coronary artery disease. With zero clinical trials, zero preclinical studies, and only one indirect computational paper, this prediction sits firmly at **Evidence Level L5** and cannot support advancement without foundational research.

**To proceed, the following is needed:**

- **Mechanism validation**: Confirm whether Ebastine's CYP2J2 interaction meaningfully alters EET production in cardiac tissue — in vitro enzyme assay data required
- **Preclinical cardiovascular studies**: Animal models of coronary artery disease to test whether Ebastine has any measurable effect on vascular inflammation, plaque formation, or ischemic endpoints
- **Safety profile clarification**: Retrieve full package insert to assess QTc and cardiac safety signals before any cardiovascular indication is explored
- **MOA documentation**: Obtain DrugBank and primary literature data on Ebastine's complete pharmacology (DG002 remediation)
- **India regulatory filing**: If evidence matures, a new drug application process would be required given no current India market presence

> ⚠️ *This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

