---
layout: default
title: Diltiazem
parent: 僅模型預測 (L5)
nav_order: 245
evidence_level: L5
indication_count: 1
---

# Diltiazem
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

# Diltiazem: From Hypertension / Angina to Susceptibility to Ischemic Stroke

## One-Sentence Summary

Diltiazem is a well-established L-type calcium channel blocker (CCB) classically used for hypertension, angina pectoris, and rate control in atrial fibrillation.
The TxGNN model predicts it may confer protection against **susceptibility to ischemic stroke**,
however **no supporting clinical trials or published literature** were identified for this specific indication pairing — making this a model-only prediction at present.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, angina pectoris, atrial fibrillation (rate control) |
| Predicted New Indication | Susceptibility to Ischemic Stroke |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 — Model prediction only, no supporting studies identified |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacological knowledge, Diltiazem is a non-dihydropyridine L-type calcium channel blocker (benzothiazepine class). It reduces intracellular calcium influx in vascular smooth muscle and cardiac conduction tissue, thereby producing vasodilation, blood pressure reduction, and heart rate slowing.

Three mechanistic pathways plausibly link Diltiazem to reduced ischemic stroke susceptibility: ① Sustained blood pressure reduction — hypertension is the single most important modifiable risk factor for ischemic stroke; ② Heart rate and rhythm control in atrial fibrillation — AF is a major source of cardioembolic stroke, and rate control with Diltiazem may indirectly reduce thromboembolic events; ③ Preclinical data suggest CCBs may attenuate neuronal calcium overload during ischemia, offering a degree of neuroprotective effect.

However, the predicted indication is framed as "susceptibility" — a preventive rather than acute-treatment context. The existing evidence base for Diltiazem as a primary stroke-prevention agent is limited compared to other antihypertensives (e.g., ACE inhibitors, ARBs) that have stronger stroke outcome data. The ontology label also carries the prefix "obsolete," suggesting this disease term may be deprecated or underspecified in the knowledge graph, which adds further uncertainty to the prediction target.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Diltiazem in ischemic stroke susceptibility.

---

## Literature Evidence

Currently no related literature available for this specific drug–indication pair.

---

## India Market Information

No marketing authorizations for Diltiazem are currently registered in India according to this evidence pack.

---

## Safety Considerations

**Drug Interactions:** Diltiazem has a notably broad interaction profile — **369 interactions** have been identified (source: DDInter). Key interactions include:

| Interacting Drug | Severity | Clinical Note |
|-----------------|----------|---------------|
| Loperamide | **Major** | Risk of serious cardiac arrhythmia; concurrent use requires close monitoring or avoidance |
| Hydrocortisone | Moderate | Corticosteroids may attenuate antihypertensive effect |
| Dexamethasone | Moderate | As above; CYP3A4 interaction may alter Diltiazem plasma levels |
| Budesonide | Moderate | CYP3A4-mediated increase in budesonide exposure |
| Pioglitazone | Moderate | Diltiazem may increase pioglitazone levels via CYP2C8 inhibition |
| Canagliflozin | Moderate | Pharmacodynamic interaction; monitor blood pressure and renal function |
| Morphine | Moderate | Additive hypotension and CNS depression risk |
| Acetylsalicylic acid | Moderate | Potential pharmacodynamic interaction; monitor bleeding and cardiac effects |
| Aprepitant | Moderate | CYP3A4 substrate interaction; monitor for increased Diltiazem effect |
| Calcium salts (multiple) | Moderate | Calcium supplementation may antagonise CCB effect |

> **Note:** Detailed prescriber warnings and contraindications were not available in this evidence pack. Please refer to the approved package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high confidence score (99.08%), and the mechanistic hypothesis linking Diltiazem's antihypertensive and rate-control properties to reduced ischemic stroke susceptibility is biologically plausible. However, zero clinical trials and zero publications were found to support this specific repurposing direction; the disease term itself is flagged as "obsolete" in the ontology, introducing ambiguity about the precise clinical target. A Hold decision is appropriate until the evidence base and indication definition are clarified.

**To proceed, the following is needed:**

- **Clarify the indication target:** The ontology term "obsolete susceptibility to ischemic stroke" should be mapped to a current, active disease ontology term (e.g., MONDO or ICD-10) to ensure the prediction target is clinically actionable
- **Mechanism of action (MOA) data:** Retrieve full DrugBank MOA record for Diltiazem to support a formal mechanistic rationale document
- **Regulatory safety data:** Download and parse the approved prescribing information (package insert) to obtain complete warnings, contraindications, and special population guidance before any clinical evaluation is initiated
- **Targeted literature review:** Conduct a broader PubMed search using related terms (e.g., "calcium channel blocker stroke prevention," "Diltiazem cerebrovascular") to determine if evidence exists under adjacent search terms not captured by the current query
- **Comparative positioning:** Evaluate how Diltiazem compares to other antihypertensives (amlodipine, lisinopril, losartan) that have established stroke-reduction outcome data, to assess whether a repurposing claim adds clinical value
- **India regulatory pathway assessment:** Confirm whether Diltiazem can be licensed or imported for investigational use under CDSCO regulations before planning any prospective study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

