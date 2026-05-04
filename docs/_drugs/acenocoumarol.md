---
layout: default
title: Acenocoumarol
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 3
---

# Acenocoumarol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Acenocoumarol: From Thromboembolic Disease to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Acenocoumarol is a vitamin K antagonist (VKA) anticoagulant, widely used in Europe and parts of Asia for prevention and treatment of thromboembolic disorders such as deep vein thrombosis, pulmonary embolism, and stroke in atrial fibrillation.
The TxGNN model predicts it may be effective for **Heparin Cofactor 2 Deficiency**, a rare inherited coagulation disorder characterized by impaired thrombin clearance.
Currently **no clinical trials** and **no publications** directly support this specific repurposing direction — the prediction is based entirely on model inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Thromboembolic disease prevention and treatment (anticoagulation) |
| Predicted New Indication | Heparin Cofactor 2 Deficiency |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Acenocoumarol is a coumarin-class vitamin K antagonist that inhibits VKORC1, thereby reducing hepatic synthesis of vitamin K-dependent coagulation factors (Factors II, VII, IX, and X) and the natural anticoagulant proteins C and S. Its established clinical use is in preventing and treating thromboembolic conditions.

Heparin Cofactor II (HCII) is a serine protease inhibitor that suppresses thrombin activity in the presence of heparin or dermatan sulfate. In HCII deficiency, the body's capacity to neutralize circulating thrombin is reduced, theoretically raising thrombotic risk. Acenocoumarol's potential rationale in this setting is to compensate for impaired thrombin **clearance** by reducing thrombin **generation** — specifically by suppressing prothrombin (Factor II) activation through VKORC1 inhibition. This upstream intervention to offset a downstream deficit represents a biologically coherent mechanistic logic.

However, two important caveats apply. First, the causal relationship between HCII deficiency and clinical thrombotic risk itself remains debated in the literature — several cohort studies have failed to demonstrate a statistically significant association with thrombotic events. Second, there is currently no direct clinical trial, case series, or case report evidence specifically linking Acenocoumarol use to outcomes in HCII-deficient patients. The prediction therefore rests entirely on mechanistic inference and model scoring.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Acenocoumarol currently has no registered products in India (0 authorizations on record). The drug is therefore not commercially available through regulated domestic channels.

---

## Safety Considerations

**Drug Interactions**: A total of 117 drug interactions have been identified for Acenocoumarol (source: DDInter). Severity levels are largely unclassified in the current dataset. Representative interactions are listed below — clinical significance for each should be verified against current prescribing references:

| Interacting Drug | Level | Clinical Note |
|-----------------|-------|--------------|
| Acetylsalicylic acid | Unknown | Combined antiplatelet + anticoagulant effect; elevated bleeding risk |
| Metronidazole | Unknown | CYP2C9 inhibitor; may potentiate anticoagulant effect and raise INR |
| Simvastatin | Unknown | Statins may elevate INR in some patients |
| Rosuvastatin | Unknown | Statins may elevate INR in some patients |
| Dexamethasone | Unknown | Corticosteroids have complex, variable effects on coagulation |
| Prednisone / Prednisolone | Unknown | Monitor INR closely with concurrent corticosteroid use |
| Morphine | Unknown | Monitor coagulation parameters during co-administration |
| Omeprazole / Lansoprazole / Pantoprazole | Unknown | PPIs may affect CYP2C19 pathways relevant to VKA metabolism |
| Vancomycin | Unknown | Antibiotic-related gut flora changes may alter VKA response |
| Metformin | Unknown | Potential pharmacodynamic interaction; monitor |

For complete warnings and contraindications, please refer to the originating country's package insert (e.g., European SmPC), as India-specific labeling data is not currently available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score for heparin cofactor 2 deficiency is high (99.84%) and the mechanistic hypothesis — upstream reduction of thrombin generation to compensate for impaired HCII-mediated thrombin clearance — is biologically plausible. However, evidence level is L5 (model prediction only), the clinical relevance of HCII deficiency as a thrombotic risk factor remains scientifically contested, and there is no supporting trial or published clinical data whatsoever for this specific repurposing candidate. Proceeding without further validation would carry unacceptable clinical uncertainty.

**To proceed, the following is needed:**

- Obtain full mechanism of action data from DrugBank (DB01418) to confirm VKORC1-mediated pathway details
- Retrieve India or international package insert (warnings, contraindications) to complete safety assessment
- Conduct a systematic literature review on the association between HCII deficiency and thrombotic outcomes, to assess whether the target disease itself has established clinical significance
- Search for case reports or registry data in which VKA-class drugs (warfarin, phenprocoumon) were used in HCII-deficient patients, which would provide indirect class-level evidence
- Assess disease prevalence and unmet medical need for HCII deficiency in the target population
- If mechanistic and epidemiological evidence is supportive, design a formal research protocol (case series or registry study) as the first clinical step before any interventional trial
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

