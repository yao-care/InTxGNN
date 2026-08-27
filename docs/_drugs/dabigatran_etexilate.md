---
layout: default
title: Dabigatran Etexilate
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 5
---

# Dabigatran Etexilate
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

# Dabigatran Etexilate: From Atrial Fibrillation/VTE to Sclerosing Cholangitis

## One-Sentence Summary

Dabigatran etexilate (Pradaxa) is a direct thrombin inhibitor originally approved for stroke prevention in non-valvular atrial fibrillation and treatment/prevention of venous thromboembolism.
The TxGNN model predicts it may be effective for **Sclerosing Cholangitis** with a score of **99.82%**, yet **0 clinical trials** and **0 publications** currently exist to directly support this repurposing direction.
This prediction remains at the lowest evidence level (L5) — model-generated only — and requires substantial preclinical and clinical investigation before any application can be considered.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Stroke prevention in non-valvular atrial fibrillation; treatment and prophylaxis of venous thromboembolism (DVT/PE) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established pharmacology, Dabigatran etexilate is a prodrug that is converted in vivo to dabigatran — a potent, competitive, and reversible direct inhibitor of thrombin. Thrombin is the central serine protease of the coagulation cascade responsible for converting fibrinogen to fibrin, activating platelets, and amplifying pro-inflammatory signaling. Its clinical efficacy in thrombotic conditions (atrial fibrillation, DVT/PE) is well validated across major trials such as RE-LY and RE-COVER.

The theoretical rationale for sclerosing cholangitis involves the protease-activated receptor (PAR) pathway. Thrombin activates hepatic stellate cells (HSCs) via PAR-1 and PAR-2 receptors, promoting pro-fibrotic cytokine release (e.g., TGF-β1) and collagen deposition in the biliary tree — key pathological drivers of both primary sclerosing cholangitis (PSC) and secondary sclerosing cholangitis (SSC). By blocking thrombin, dabigatran could theoretically disrupt this pro-fibrotic amplification loop and slow the progression of biliary fibrosis.

However, this mechanistic link must be characterized as **highly speculative**. No preclinical animal model data directly testing dabigatran in PSC or SSC currently exist. The TxGNN high score most likely reflects knowledge graph co-occurrence patterns between coagulation network nodes and biliary disease nodes, rather than validated pharmacological evidence. Independent experimental confirmation is required before this hypothesis can advance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for sclerosing cholangitis.

---

## Literature Evidence

Currently no related literature available for sclerosing cholangitis.

---

## India Market Information

Dabigatran etexilate currently has **no approved registrations in India**. No license data is available in the regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug-drug interaction data were not retrievable in this Evidence Pack (identified as Data Gap DG001). Safety assessment must be completed before any clinical decision can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is based solely on TxGNN model output (L5 evidence) with no supporting clinical trials, published literature, or preclinical studies for sclerosing cholangitis. The thrombin–PAR–hepatic stellate cell mechanistic link is biologically plausible in principle, but remains entirely unvalidated for this indication, and the drug has no approved registrations in India.

**To proceed, the following is needed:**

- **Retrieve package insert data**: Obtain TFDA/EMA/CDSCO prescribing information to complete safety screening (key warnings, contraindications) — this is a blocking requirement before Stage 1 evaluation
- **Retrieve MOA data**: Query DrugBank API for full mechanism-of-action description to formalize the mechanistic rationale
- **Preclinical validation**: Commission or identify in vitro and/or animal studies examining dabigatran's effect on hepatic stellate cell activation, biliary fibrosis markers (TGF-β1, collagen I/III), and cholestatic injury models (e.g., MDR2-knockout mouse, bile duct ligation)
- **Drug-drug interaction profile**: Complete DDI assessment for co-medications common in PSC patients (e.g., immunosuppressants, ursodeoxycholic acid, antibiotics for cholangitis)
- **India regulatory pathway analysis**: Assess import/new drug application requirements given zero current registrations
- **Exploratory literature scan expansion**: Broaden search to include thrombin inhibitors as a drug class (not dabigatran specifically) in liver fibrosis and cholestatic disease models to calibrate the class-level evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

