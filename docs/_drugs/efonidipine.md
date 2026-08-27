---
layout: default
title: Efonidipine
parent: 僅模型預測 (L5)
nav_order: 275
evidence_level: L5
indication_count: 4
---

# Efonidipine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Efonidipine: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Efonidipine is a dual L/T-type calcium channel blocker (CCB), authorised for clinical use in Japan and India for its anti-hypertensive effects.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism (Group 5 PH)**,
with **no clinical trials** and **no direct literature** currently supporting this specific repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (anti-hypertensive) |
| Predicted New Indication | Pulmonary Hypertension with Unclear Multifactorial Mechanism |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available from DrugBank. However, pharmacological data confirms that efonidipine binds to **Cav3.2** — a T-type calcium channel encoded by the *CACNA1H* gene — distinguishing it from conventional dihydropyridine CCBs that block only L-type channels. Efonidipine's dual L/T-type blocking profile is the pharmacological foundation for this TxGNN prediction.

T-type calcium channels (Cav3.x) are widely expressed in pulmonary arterial smooth muscle cells. The mechanistic hypothesis holds that dual L/T-type blockade could suppress pulmonary arterial vasoconstriction and reduce pulmonary vascular resistance to a greater degree than L-type-only CCBs. This makes efonidipine theoretically interesting in the context of pulmonary hypertension driven by abnormal vascular tone.

However, Group 5 pulmonary hypertension — classified as "unclear multifactorial mechanism" — is a heterogeneous category encompassing conditions such as haematologic disorders, systemic inflammatory disease, and metabolic disorders, where aberrant vascular tone is only one of many pathological drivers. Vasodilator therapy with CCBs is established only in a small, carefully selected subset of Group 1 PAH patients who respond to acute vasoreactivity testing. The applicability of efonidipine's dual-channel mechanism to Group 5 PH remains entirely theoretical, with no preclinical or clinical data to substantiate the prediction at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no literature directly studying efonidipine in pulmonary hypertension with unclear multifactorial mechanism is available.

> **Note:** A PubMed search for the adjacent indication (Group 3 PH — pulmonary hypertension owing to lung disease and/or hypoxia) returned 20 publications, but none address efonidipine specifically. The retrieved articles cover general hypoxia biology (neurodegeneration, cancer metabolism, HIF signalling) and are not relevant to the drug-disease repurposing hypothesis.

---

## India Market Information

Efonidipine is **not currently registered in the local regulatory database**. No drug authorization licenses are on record.

> **Cross-reference:** Pharmacology source data (Guide to Pharmacology) notes that efonidipine has been authorised for clinical use in **Japan** and **India** for its anti-hypertensive effects. Regulatory confirmation from CDSCO should be sought directly to clarify current market status.

---

## Safety Considerations

Full safety information (package insert warnings and contraindications) is not available in this Evidence Pack and represents a **blocking data gap** preventing formal safety evaluation.

**Pharmacological Target Interaction:**
- Efonidipine binds to **Cav3.2** (T-type calcium channel; gene: *CACNA1H*; Entrez ID: 8912; Ensembl: ENSG00000196557). This is a confirmed pharmacological target interaction, not a drug-drug interaction in the clinical sense.

Please refer to the official package insert for comprehensive safety information before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is at the lowest tier (L5 — model prediction only), with no clinical trials, no direct literature, and no preclinical data supporting efonidipine's use in Group 5 pulmonary hypertension. A critical data gap in formal MOA and safety documentation further blocks entry into the evaluation pipeline.

**To proceed, the following is needed:**

- **Resolve blocking data gap (DG001):** Obtain and parse the official package insert (PMDA or CDSCO) to retrieve key warnings and contraindications
- **Resolve high-priority data gap (DG002):** Confirm full MOA from DrugBank API, particularly the L/T dual-channel blocking evidence
- **Preclinical feasibility check:** Search for in vitro or animal model data on efonidipine's effect on pulmonary vascular resistance
- **Class-effect literature review:** Evaluate existing evidence for other dual L/T-type CCBs (e.g., mibefradil) in pulmonary hypertension models as a proxy for mechanistic plausibility
- **Group 5 PH aetiology review:** Determine which Group 5 PH subtypes (if any) have a vascular tone component amenable to CCB therapy
- **Vasoreactivity testing rationale:** Assess whether a vasoreactivity-testing design would be appropriate before any clinical hypothesis is formalised
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

