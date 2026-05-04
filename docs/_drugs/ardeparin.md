---
layout: default
title: Ardeparin
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 6
---

# Ardeparin
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

# Ardeparin: From DVT Prevention to Thrombophilia due to Protein C Deficiency

## One-Sentence Summary

Ardeparin is a low molecular weight heparin (LMWH), originally developed as an anticoagulant for the prevention and treatment of deep vein thrombosis (DVT). The TxGNN model predicts it may be effective for **thrombophilia due to protein C deficiency, autosomal recessive**, a hereditary hypercoagulable disorder with mechanistic overlap with LMWH's known anti-Xa activity. Currently, **no clinical trials and no publications** directly support this specific repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Deep vein thrombosis (DVT) prevention / anticoagulation |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Ardeparin. Based on known information, Ardeparin belongs to the low molecular weight heparin (LMWH) class, which exerts its anticoagulant effect primarily through anti-Factor Xa (anti-Xa) activity — inhibiting the coagulation cascade and reducing thrombus formation. Other LMWHs in the same class (e.g., Enoxaparin, Dalteparin) have well-established clinical use in thrombotic conditions.

Protein C deficiency (autosomal recessive) results in a severe hereditary hypercoagulable state. Protein C normally functions as a natural anticoagulant by inactivating Factors Va and VIIIa; when deficient, the coagulation cascade becomes dysregulated, greatly increasing the risk of life-threatening thrombosis. This mechanistic logic — using an anti-Xa anticoagulant to compensate for impaired endogenous anticoagulation — makes the TxGNN prediction biologically plausible.

However, the key limitation is that Ardeparin itself has been withdrawn from the market (Normiflo, discontinued), and no Ardeparin-specific trials exist for this indication. The mechanistic link is extrapolated from the broader LMWH class rather than from direct evidence for Ardeparin. Class-level plausibility exists, but drug-level evidence does not.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Ardeparin has no approved drug registrations in India. The drug (originally marketed as Normiflo) has been withdrawn from the market and is currently unavailable commercially.

---

## Safety Considerations

**Drug Interactions (76 interactions identified; selected major interactions below):**

| Interacting Drug | Severity | Clinical Concern |
|-----------------|----------|-----------------|
| Acetylsalicylic acid (Aspirin) | **Major** | Combined antiplatelet + anticoagulant use significantly increases bleeding risk |
| Abciximab | **Major** | GPIIb/IIIa inhibitor + LMWH increases haemorrhagic risk |
| Alteplase | **Major** | Thrombolytic + anticoagulant: high risk of serious bleeding |
| Apixaban | **Major** | Dual anticoagulation; additive bleeding risk |
| Bivalirudin | **Major** | Direct thrombin inhibitor combination; major haemorrhage risk |
| Clopidogrel | **Major** | Antiplatelet + anticoagulant; significant bleeding risk |
| Cangrelor | **Major** | IV antiplatelet; additive haemorrhagic risk |
| Antithrombin III human | **Major** | Potentiates heparin effect; risk of over-anticoagulation |
| Ibritumomab tiuxetan | **Major** | Radiolabelled antibody; risk of haemorrhagic complications |
| Deferasirox | **Major** | Iron chelator; GI bleeding risk may be amplified |
| Dipyridamole | **Major** | Antiplatelet agent; additive bleeding risk |
| Betrixaban | **Major** | Oral FXa inhibitor; additive anticoagulant effect |
| Caplacizumab | **Major** | Anti-vWF nanobody used in TTP; combined haemorrhage risk |
| Cilostazol | **Major** | Antiplatelet/vasodilator; increased bleeding tendency |

> **Note:** A total of 76 drug interactions are on record. Major interactions are predominantly with other anticoagulants, antiplatelets, and thrombolytics. Please refer to the complete DDI database before any clinical use.

> Key warnings and contraindications data are not currently available. Please refer to the original package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Ardeparin's predicted use in protein C deficiency thrombophilia carries biological plausibility at the LMWH class level, but the evidence level is L5 (model prediction only) — there are zero clinical trials and zero publications specifically for this drug-disease pair. Compounding this, Ardeparin has been withdrawn from the market globally, making clinical development highly impractical without substantial justification.

**To proceed, the following is needed:**

- Confirm whether class-level LMWH evidence (e.g., Enoxaparin trials in protein C deficiency) can serve as a sufficient surrogate for Ardeparin
- Obtain complete MOA data from DrugBank API (currently missing)
- Retrieve and review full prescribing information and package insert warnings/contraindications (DG001: Blocking data gap)
- Conduct a feasibility assessment given Ardeparin's withdrawn market status — evaluate whether redevelopment or substitution with an active LMWH is more appropriate
- If development proceeds, design a Phase 1/2 proof-of-concept trial in patients with confirmed autosomal recessive protein C deficiency
- Assess anti-Xa monitoring protocols and dosing strategy, given the severity of bleeding risk interactions identified (76 DDIs, predominantly Major)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

