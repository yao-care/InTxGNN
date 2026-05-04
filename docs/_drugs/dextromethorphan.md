---
layout: default
title: Dextromethorphan
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 6
---

# Dextromethorphan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Dextromethorphan: From Cough Suppression to Nasal Cavity Disease

## One-Sentence Summary

Dextromethorphan (DXM) is a well-established over-the-counter central antitussive agent, widely used globally for cough suppression via sigma-1 receptor agonism and NMDA receptor antagonism.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease**,
with **1 Phase 3 clinical trial** currently supporting this direction (no published literature specific to this indication identified).

> ⚠️ **Note:** The drug is currently **not marketed in India** under CDSCO, and detailed mechanism of action (MOA) data and package insert warnings were not available in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cough suppression (central antitussive) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 (1 Phase 3 trial, recruiting) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Dextromethorphan is a centrally acting antitussive that works primarily through **sigma-1 receptor agonism** and **NMDA receptor antagonism** to suppress the cough reflex center in the medulla oblongata (nucleus tractus solitarius, NTS). It is also a weak serotonin reuptake inhibitor and has activity at several other CNS receptors.

Nasal cavity disease encompasses a broad spectrum of upper respiratory conditions — including allergic rhinitis, sinusitis, and viral rhinitis — many of which present with **concomitant dry or irritative cough** arising from post-nasal drip and mucosal irritation. DXM directly addresses this cough component by suppressing the central reflex arc triggered by nasopharyngeal and laryngeal stimulation.

The mechanistic bridge becomes even more compelling in the context of **combination formulations**: DXM combined with antihistamines (e.g., Bilastine or Chlorphenamine) and nasal decongestants (e.g., Phenylephrine) provides simultaneous coverage of nasal congestion, allergic inflammation, and reflex cough — addressing the complete symptom cluster of nasal cavity disease. This combination approach is already reflected in existing OTC multi-symptom cold and allergy products globally, and a Phase 3 trial of DXM in such a combination has been conducted (see below).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT06958692](https://clinicaltrials.gov/study/NCT06958692) | Phase 3 | Recruiting | 388 | Multicenter RCT evaluating DXM + Bupropion sustained-release tablets in Chinese adult patients with Major Depressive Disorder; trial is ongoing (completion expected Dec 2026). ⚠️ *Note: This trial's brief summary describes a depression indication, though the relevance grading in this evidence pack associates it with DXM combination use in upper respiratory disease. The indication mismatch should be verified before drawing conclusions.* |

> ⚠️ **Data Quality Note:** The single identified trial (NCT06958692) appears to address **Major Depressive Disorder** (DXM + Bupropion), not nasal cavity disease. The evidence pack's internal relevance reasoning references a separate Bilastine + DXM + Phenylephrine combination trial (PMID 39822435) for upper respiratory/nasal symptoms, but this trial is not listed in the structured evidence. The evidence level of L1 assigned in this pack should be **treated with caution** pending verification of the correct trial mapping.

---

## Literature Evidence

Currently no related literature specific to Dextromethorphan for nasal cavity disease is available in this evidence pack.

> The evidence pack references PMID 39822435 in the relevance reasoning for the clinical trial, which reportedly describes Phase 3 results for a Bilastine + DXM + Phenylephrine combination in upper respiratory disease. This publication should be retrieved and reviewed as a priority step.

---

## India Market Information

Dextromethorphan is **not currently registered** under CDSCO in India based on the data available in this evidence pack (0 license records returned).

> Note: DXM is available in many countries as an OTC antitussive ingredient in combination cold and cough products. India's current regulatory status should be independently verified via the CDSCO online database, as single-ingredient and combination registrations may exist under different brand names not captured in this dataset.

---

## Safety Considerations

**Drug-Drug Interactions (DDI):** A total of **306 interactions** were identified (DDInter database). Key interactions to note:

*Major-level interactions (highest risk):*

| Interacting Drug | Interaction Level | Clinical Concern |
|-----------------|-------------------|-----------------|
| Dexfenfluramine | Major | Serotonin syndrome risk |
| Fenfluramine | Major | Serotonin syndrome risk |
| Lorcaserin | Major | Serotonin syndrome risk |
| Sibutramine | Major | Serotonin syndrome risk |
| Ondansetron | Major | Serotonin syndrome / QT prolongation |
| Granisetron | Major | Serotonin syndrome risk |
| Dolasetron | Major | Serotonin syndrome / QT risk |
| Palonosetron | Major | Serotonin syndrome risk |

*Moderate-level interactions (selected):*

| Interacting Drug | Interaction Level | Clinical Concern |
|-----------------|-------------------|-----------------|
| Bupropion | Moderate | CYP2D6 inhibition → elevated DXM levels; also combined in some formulations |
| Morphine / Opium | Moderate | CNS depression additive effect |
| Metoclopramide | Moderate | CNS effects |
| Eliglustat | Moderate | CYP2D6 substrate interaction |
| Cimetidine | Moderate | CYP2D6 inhibition |

> **Key warnings and contraindications** from the official package insert are not available in this evidence pack (Data Gap: DG001). Given DXM's serotonergic activity, **concurrent use with MAOIs is a well-known absolute contraindication** and should be prominently flagged. Full safety review of the CDSCO/TFDA prescribing information is required before any clinical use assessment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
DXM has a pharmacologically coherent mechanistic link to nasal cavity disease through its antitussive action on the cough reflex arc triggered by upper airway mucosal irritation, and multi-symptom combination formulations incorporating DXM alongside antihistamines and decongestants are already in widespread OTC use globally. However, the single identified Phase 3 trial maps to a different indication (MDD), creating an evidence traceability gap that must be resolved before this evaluation can be finalized.

**To proceed, the following is needed:**

- **[Priority: Blocking]** Retrieve and parse the CDSCO/TFDA package insert for DXM to populate key warnings and contraindications (Data Gap DG001)
- **[Priority: High]** Verify and correct the clinical trial mapping — confirm whether NCT06958692 is truly relevant to nasal cavity disease, and retrieve the Bilastine + DXM + Phenylephrine Phase 3 trial data referenced in PMID 39822435
- **[Priority: High]** Retrieve DrugBank MOA data for DXM (Data Gap DG002) to enable formal mechanistic link scoring
- Conduct a targeted PubMed search for DXM in combination cold/allergy formulations for nasal cavity disease to fill the literature evidence gap
- Verify current CDSCO registration status for DXM-containing combination products in India
- Evaluate CYP2D6 pharmacogenomic considerations, as DXM metabolism is highly variable across populations — relevant for any Indian patient population study design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

