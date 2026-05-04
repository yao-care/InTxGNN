---
layout: default
title: Dalteparin
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 5
---

# Dalteparin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Dalteparin: From Venous Thromboembolism Prevention to Thrombophilia due to Protein C Deficiency (Autosomal Recessive)

## One-Sentence Summary

Dalteparin (brand name: Fragmin) is a low molecular weight heparin (LMWH) with established clinical use in the prevention and treatment of venous thromboembolism (VTE), including deep vein thrombosis (DVT) and pulmonary embolism.
The TxGNN model predicts it may be effective for **Thrombophilia due to Protein C Deficiency (Autosomal Recessive)**, with a prediction score of 99.88% (TxGNN rank 2,816).
Currently, **no registered clinical trials** and **no publications** directly supporting this specific indication subtype were identified.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Venous thromboembolism prevention and treatment (Dalteparin not registered in India; based on international clinical knowledge) |
| Predicted New Indication | Thrombophilia due to Protein C Deficiency, Autosomal Recessive |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L4 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dalteparin is a low molecular weight heparin (LMWH) whose primary mechanism of action involves binding to antithrombin III (AT-III), thereby potentiating its inhibition of Factor Xa and, to a lesser extent, thrombin. This shifts the coagulation cascade toward an anticoagulated state, reducing pathological clot formation. Although detailed MOA data is not available in the current Evidence Pack, the drug's pharmacological class and clinical behaviour are well characterised in the global literature.

Protein C deficiency (autosomal recessive form) represents one of the most severe inherited thrombophilias. Under normal physiology, activated Protein C inhibits the procoagulant cofactors Factor Va and Factor VIIIa, acting as a natural brake on clot propagation. In autosomal recessive protein C deficiency, this brake is entirely absent, leading to neonatal purpura fulminans or severe recurrent thrombosis. Dalteparin's antithrombin-mediated Factor Xa inhibition provides an alternative, complementary anticoagulant pathway that does not depend on the Protein C/S system — effectively bypassing the defective pathway. This mechanistic rationale is strong: LMWH is already recommended in clinical guidelines for acute thrombotic management in protein C deficiency.

The TxGNN network-based prediction reflects this biological plausibility through shared disease graph topology between venous thromboembolism and protein C deficiency pathways. However, evidence specific to the autosomal recessive subtype — which is rarer and more severe than the heterozygous form — is entirely absent from the current search results, limiting confidence and preventing advancement beyond a research hypothesis at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for thrombophilia due to protein C deficiency (autosomal recessive).

> **Reviewer's Note:** Among all five predicted indications in this Evidence Pack, **Neuropathy, Painful** (ranked 5th by TxGNN score) carries the strongest clinical evidence: three registered trials including [NCT00662831](https://clinicaltrials.gov/study/NCT00662831), a completed double-blind placebo-controlled Phase 2/3 RCT (n=276) evaluating Dalteparin in diabetic neuroischaemic foot ulcers. That indication is rated L2 ("Proceed with Guardrails") and may represent a more immediately actionable repurposing opportunity.

---

## Literature Evidence

Currently no related literature available for thrombophilia due to protein C deficiency (autosomal recessive) in combination with Dalteparin.

---

## India Market Information

Dalteparin is currently **not registered** in India. No marketing authorizations were identified in the regulatory data submitted to this Evidence Pack. Clinicians wishing to access Dalteparin in India would need to explore import licenses or compassionate/special access pathways under applicable Indian pharmaceutical regulations (e.g., Schedule H1 controlled import or New Drug provisions under the Drugs and Cosmetics Act).

---

## Safety Considerations

**Drug Interactions (174 total interactions identified; major interactions listed below):**

| Interacting Drug | Severity | Clinical Concern |
|-----------------|----------|-----------------|
| Acetylsalicylic acid (Aspirin) | **Major** | Additive bleeding risk via dual antiplatelet and anticoagulant effect |
| Fondaparinux | **Major** | Additive anticoagulant effect; significantly elevated haemorrhage risk |
| Ibuprofen | **Major** | NSAID-related additive bleeding risk |
| Ketorolac | **Major** | High-potency NSAID; major haemorrhage risk |
| Abciximab | **Major** | GPIIb/IIIa inhibitor; compounding antiplatelet and anticoagulant effect |
| Acalabrutinib | **Major** | BTK inhibitor with antiplatelet properties; additive bleeding risk |
| Trastuzumab emtansine (T-DM1) | **Major** | Additive bleeding risk in oncology settings |
| Ibritumomab tiuxetan | **Major** | Radioimmunotherapy; additive haemorrhagic risk |
| Tositumomab / Tositumomab (I-131) | **Major** | Radioimmunotherapy; additive haemorrhagic risk |
| Deferasirox | **Major** | Iron chelator; gastrointestinal bleeding risk |
| Sugammadex | Moderate | May affect anticoagulant binding dynamics |
| Fluvoxamine | Moderate | SSRI; modest additive bleeding risk |
| Fosinopril | Moderate | ACE inhibitor; potential hyperkalaemia and bleeding interaction |

> Please refer to the full package insert for complete warnings and contraindications, which were not available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the mechanistic link between Dalteparin and autosomal recessive protein C deficiency is biologically well-grounded, the complete absence of clinical trial data or peer-reviewed literature for this specific disease subtype — combined with zero regulatory registrations in India — means the evidence base is insufficient to support advancement at this time.

**To proceed, the following is needed:**

- **Literature review:** Conduct a targeted systematic review for LMWH use in autosomal recessive protein C deficiency (case reports, paediatric case series, inherited thrombophilia registries, international clinical guidelines)
- **Safety documentation:** Obtain and review the full Dalteparin package insert to resolve the blocking data gap for warnings and contraindications (DG001)
- **MOA data:** Retrieve mechanism-of-action details from DrugBank API to complete DG002 and enable full mechanistic analysis
- **Regulatory pathway:** Assess feasibility of Dalteparin importation or registration in India (currently not marketed)
- **Alternative focus:** Consider prioritising the **Neuropathy, Painful** indication (Evidence Level L2; three clinical trials including a completed Phase 2/3 RCT with n=276), which represents a more evidence-supported repurposing candidate within this same Evidence Pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

