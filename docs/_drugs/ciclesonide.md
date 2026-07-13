---
layout: default
title: Ciclesonide
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 6
---

# Ciclesonide
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

# Ciclesonide: From Asthma / Allergic Rhinitis to Atopic Eczema

## One-Sentence Summary

Ciclesonide is a second-generation inhaled corticosteroid (ICS) clinically established for asthma and allergic rhinitis, acting via its active metabolite des-ciclesonide to suppress glucocorticoid receptor-mediated airway inflammation.
The TxGNN model predicts it may be effective for **Atopic Eczema** (score 99.96%), yet there are currently **no registered clinical trials** and **no direct supporting publications** for this specific application.
While the mechanistic rationale is scientifically plausible, the absence of a topical skin formulation represents a critical route-compatibility gap that must be addressed before clinical development can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (not marketed in India; standard global use: asthma, allergic rhinitis) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ciclesonide is a prodrug that is converted by airway esterases into its pharmacologically active form, **des-ciclesonide**, following inhalation. Des-ciclesonide binds with high affinity to glucocorticoid receptors (GR), triggering suppression of pro-inflammatory gene transcription. This specifically downregulates **IL-4, IL-13, and TSLP** — the core cytokines driving Th2-polarised immune activation.

Atopic eczema (atopic dermatitis) is fundamentally a **Th2-skewed inflammatory disease**: its pathophysiology is driven by exactly the same IL-4/IL-13/TSLP axis that des-ciclesonide suppresses. This mechanistic alignment is not incidental — it is the reason why **topical corticosteroids (TCS) are the established first-line therapy** for atopic dermatitis worldwide, lending strong biological plausibility to the TxGNN prediction.

However, the current gap is practical rather than mechanistic: ciclesonide exists only as an **inhaled aerosol and intranasal spray**, with no approved dermatological formulation. Realising this prediction would require either a purpose-built topical reformulation of ciclesonide, or evaluation of an alternative systemic route — both of which demand dedicated pharmacokinetic, safety, and efficacy studies before any clinical trial could proceed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ciclesonide in Atopic Eczema.

---

## Literature Evidence

Currently no related literature available for Ciclesonide in Atopic Eczema.

---

## India Market Information

Ciclesonide is **not currently marketed in India** and holds no product registrations with the Indian regulatory authority (CDSCO). No authorization records are available.

---

## Safety Considerations

**Drug Interactions** — 63 interactions identified (DDInter database):

| Interacting Drug | Severity |
|-----------------|----------|
| Cladribine | **Major** |
| Clarithromycin | Moderate |
| Cobicistat | Moderate |
| Atazanavir | Moderate |
| Fosamprenavir | Moderate |
| Amprenavir | Moderate |
| Boceprevir | Moderate |
| Ceritinib | Moderate |
| Conivaptan | Moderate |
| Fostamatinib | Moderate |
| Miconazole | Moderate |
| Insulin human (inhalation, rapid acting) | Moderate |
| Abametapir (topical) | Moderate |
| Formoterol | Minor |
| Salbutamol | Minor |
| Arformoterol | Minor |

> The most significant interaction is with **Cladribine (Major)**, likely reflecting immunosuppression compounding. Multiple **CYP3A4 inhibitors** (clarithromycin, cobicistat, HIV protease inhibitors) are flagged at moderate severity, consistent with ciclesonide's known CYP3A4-dependent metabolism.

> Key warnings and contraindications data are not available in the current evidence pack. Please refer to the official package insert (EMA/US FDA SmPC) for complete safety and contraindication information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN's prediction is mechanistically coherent — the Th2/GR pathway alignment between ciclesonide's pharmacology and atopic eczema's pathophysiology is genuine — there is **zero clinical or published evidence** specifically supporting this use, and ciclesonide's existing formulations are incompatible with dermatological application. The route-compatibility gap is a blocking prerequisite, not a minor detail.

**To proceed, the following is needed:**
- **Formulation feasibility**: Determine whether ciclesonide can be reformulated as a topical skin preparation (cream/ointment), or whether an oral/systemic route could be justified for moderate-to-severe atopic dermatitis
- **Preclinical data**: Commission skin penetration studies and in vitro/in vivo atopic dermatitis model testing with reformulated ciclesonide
- **MOA documentation**: Retrieve complete mechanism of action data from DrugBank (DB01410) to formalise the mechanistic dossier
- **Regulatory safety review**: Download and parse the EMA/FDA package insert to extract key warnings, contraindications, and special population restrictions
- **Competitive context analysis**: Evaluate differentiation opportunity against widely available generic topical corticosteroids (e.g., hydrocortisone, betamethasone) and newer biologics (dupilumab) in the atopic dermatitis market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

