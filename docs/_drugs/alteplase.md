---
layout: default
title: Alteplase
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 9
---

# Alteplase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Alteplase: From Acute Thromboembolic Conditions to Posteroinferior Myocardial Infarction

## One-Sentence Summary

Alteplase is a recombinant tissue plasminogen activator (rt-PA) used globally as a thrombolytic agent for acute ischemic stroke, pulmonary embolism, and ST-elevation myocardial infarction; however, it is not currently registered in India.
The TxGNN model predicts it may be effective for the specific STEMI subtype of **Posteroinferior Myocardial Infarction**, caused by RCA or LCx occlusion,
with **0 clinical trials** and **1 publication** currently supporting this specific indication direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from India regulatory data (Alteplase is a known thrombolytic for STEMI/ischaemic stroke/PE globally) |
| Predicted New Indication | Posteroinferior Myocardial Infarction |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this evidence pack. Based on known pharmacological information, Alteplase is a recombinant human tissue-type plasminogen activator that binds selectively to fibrin within a thrombus and converts plasminogen to plasmin, initiating localised fibrinolysis. Its efficacy in achieving coronary artery reperfusion in STEMI has been established through landmark trials including the GUSTO and TAMI series.

Posteroinferior myocardial infarction is a STEMI subtype arising from occlusion of the right coronary artery (RCA) or left circumflex artery (LCx). Because Alteplase's fibrinolytic mechanism acts on thrombus regardless of the coronary artery involved, the mechanistic rationale for applying it to this anatomical subtype is pharmacologically sound and mechanistically continuous with established use. Landmark STEMI trials have historically enrolled patients with both anterior and inferior/posterior wall involvement, providing indirect subgroup evidence.

A critical clinical nuance specific to this subtype is the elevated risk of reperfusion-related complications following RCA recanalization — including bradyarrhythmia and the Bezold-Jarisch reflex — which require heightened post-thrombolysis monitoring protocols not typically addressed in anterior STEMI trial designs. This anatomical specificity is what drives the "repurposing" framing: existing evidence does not systematically characterise efficacy and safety in this precise subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [16294818](https://pubmed.ncbi.nlm.nih.gov/16294818/) | 2005 | Retrospective Observational | Archivos de cardiologia de Mexico | Short-term clinical and angiographic outcomes of rescue percutaneous transluminal coronary angioplasty (RPTCA) after failed thrombolysis in acute MI; describes the role of thrombolytic failure as a trigger for rescue intervention |

---

## India Market Information

Alteplase is not currently registered or marketed in India. No regulatory authorisation records are available.

---

## Safety Considerations

**Drug Interactions**: Alteplase has 140 documented interactions. The following major interactions are of particular clinical concern when considering thrombolysis:

| Interacting Drug | Level | Clinical Concern |
|-----------------|-------|----------------|
| Abciximab | Major | GPIIb/IIIa inhibitor — compounded haemorrhagic risk with concurrent thrombolysis |
| Apixaban | Major | DOAC — significantly elevated bleeding risk |
| Fondaparinux | Major | Anticoagulant — compounded bleeding risk |
| Anisindione | Major | Anticoagulant — compounded bleeding risk |
| Acalabrutinib | Major | BTK inhibitor — increased intracranial/systemic haemorrhage risk |
| Deferasirox | Major | Iron chelator — potential haemorrhagic interaction |
| Ibritumomab tiuxetan | Major | Radioimmunotherapy — significant haemorrhagic risk |
| Tositumomab / Tositumomab (I-131) | Major | Radioimmunotherapy — significant haemorrhagic risk |
| Acetylsalicylic acid (Aspirin) | Moderate | Antiplatelet — additive bleeding risk (commonly co-administered in STEMI protocols, requires careful management) |
| Ibuprofen / Ketorolac | Moderate | NSAIDs — additive bleeding risk, should be avoided peri-thrombolysis |

For complete warnings and contraindications, please refer to the originator package insert (Activase® / Actilyse®).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although Alteplase's thrombolytic mechanism is directly applicable to coronary artery thrombosis, the evidence base specific to the posteroinferior MI subtype consists of a single retrospective observational study that does not directly evaluate Alteplase dosing, efficacy, or safety endpoints in this anatomical context. Alteplase is not registered in India, further limiting immediate clinical translation.

**To proceed, the following is needed:**
- Subgroup extraction from major STEMI trials (GUSTO, TAMI-1) specifically isolating posteroinferior/inferior wall MI patients treated with Alteplase — to evaluate patency rates, mortality, and reperfusion arrhythmia incidence
- Mechanistic data (MOA) from DrugBank or published pharmacology literature to formally document the fibrin-binding thrombolysis pathway
- Review of originator package insert (Actilyse® / Activase®) to document official contraindications, warnings, and dose recommendations for STEMI subtypes
- Assessment of regulatory pathway for Alteplase registration in India (no current license)
- Protocol development addressing Bezold-Jarisch reflex management specific to RCA thrombolysis in posteroinferior MI
- Safety monitoring plan covering bleeding risk stratification given 140 documented drug interactions, especially with anticoagulants and antiplatelets commonly used in acute MI management
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

