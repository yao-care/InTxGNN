---
layout: default
title: Enalaprilat
parent: 僅模型預測 (L5)
nav_order: 280
evidence_level: L5
indication_count: 1
---

# Enalaprilat
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

# Enalaprilat: From Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Enalaprilat is the active metabolite of enalapril, an ACE inhibitor originally used to treat hypertension by blocking the conversion of angiotensin I to angiotensin II.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**,
however, this prediction is currently supported by **0 clinical trials** and **0 publications**, making it a model-only hypothesis at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (via enalapril prodrug) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank directly. Based on pharmacological data from the drug interaction record, Enalaprilat is the active diacid form of enalapril, acting as an **ACE (Angiotensin-Converting Enzyme) inhibitor**. It blocks the renin-angiotensin system (RAS) by preventing the conversion of angiotensin I to the vasoconstrictive angiotensin II, which is its established role in hypertension management.

The mechanistic rationale linking Enalaprilat to primary hereditary glaucoma rests on the hypothesis that a local RAS exists within the eye. Local RAS components have been identified in ocular tissues, and ACE inhibition may theoretically influence intraocular pressure (IOP) by modulating aqueous humor production and drainage dynamics. This provides a biological basis for TxGNN's prediction.

However, the scientific link is tenuous for this specific indication. Primary hereditary glaucoma is fundamentally a structural disorder — caused by developmental defects in the trabecular meshwork (associated with mutations in genes such as *CYP1B1* and *LTBP2*) — rather than a disorder of vascular tone dysregulation. ACE inhibition addresses functional hemodynamics and is not known to correct or compensate for congenital trabecular network malformations. The biological plausibility of this repurposing therefore faces a fundamental mechanistic challenge, even if a local ocular RAS connection exists.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Enalaprilat has no registered products or marketing authorizations in India. The drug has zero active licenses on record.

---

## Safety Considerations

**Drug Interactions:**

| Interacting Target | Type | Clinical Relevance |
|---|---|---|
| Angiotensin-Converting Enzyme (ACE) | Pharmacological (enzyme inhibition) | Enalaprilat is the direct inhibitor of ACE (gene: *ACE*, Entrez: 1636). Concomitant use with other RAS-modulating agents (e.g., ARBs, direct renin inhibitors) may result in additive hypotension, hyperkalemia, or renal impairment. |

> For complete warnings, contraindications, and drug interaction data, please refer to the enalapril/enalaprilat package insert, as label-level safety data was not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high score (99.09%) to this pairing, but the prediction is entirely unsupported by clinical or preclinical evidence (L5). More critically, the mechanistic rationale faces a fundamental challenge: primary hereditary glaucoma is a developmental structural disorder driven by gene mutations, and ACE inhibition is not known to address its underlying pathophysiology.

**To proceed, the following is needed:**

- **Preclinical validation**: Animal or in vitro studies demonstrating that ACE inhibition or RAS modulation has measurable effects on IOP or trabecular meshwork function in genetic glaucoma models (e.g., *Cyp1b1*-knockout mice)
- **MOA documentation**: Retrieve full DrugBank MOA profile for Enalaprilat to clarify any direct ocular targets
- **Safety dossier**: Download and parse the enalapril/enalaprilat package insert from the originator label (FDA or EMA) to complete the S1 safety pre-screening — currently a blocking data gap (DG001)
- **Literature survey**: Conduct a broader PubMed search for ACE inhibitors + glaucoma (not restricted to primary hereditary glaucoma) to determine if any class-level signal exists before narrowing to this indication
- **Indication re-scope**: Consider whether a more common glaucoma subtype (e.g., primary open-angle glaucoma with vascular dysregulation component) might present a stronger mechanistic and evidentiary fit for this drug class
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

