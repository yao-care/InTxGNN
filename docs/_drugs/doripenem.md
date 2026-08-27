---
layout: default
title: Doripenem
parent: 僅模型預測 (L5)
nav_order: 259
evidence_level: L5
indication_count: 10
---

# Doripenem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Doripenem: From Serious Bacterial Infections to Idiopathic Copper-Associated Cirrhosis

## One-Sentence Summary

Doripenem is a carbapenem-class broad-spectrum antibiotic, clinically used for the treatment of serious bacterial infections including hospital-acquired pneumonia, complicated urinary tract infections, and complicated intra-abdominal infections.
The TxGNN model predicts it may be effective for **Idiopathic Copper-Associated Cirrhosis**, however, with **0 clinical trials** and **0 publications** currently supporting this direction, the evidence base is entirely absent.
All 10 predicted indications share this same evidence gap, and the mechanistic rationale for repurposing is assessed as biologically implausible across the board.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious bacterial infections (hospital-acquired pneumonia, complicated UTI, complicated intra-abdominal infections) |
| Predicted New Indication | Idiopathic Copper-Associated Cirrhosis |
| TxGNN Prediction Score | 99.00% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacological knowledge, Doripenem is a carbapenem β-lactam antibiotic that acts by inhibiting bacterial cell wall synthesis — specifically by binding to penicillin-binding proteins (PBPs), thereby disrupting the cross-linking of peptidoglycan and causing cell lysis. It is active against a broad spectrum of Gram-positive, Gram-negative, and anaerobic bacteria, with particular strength against resistant organisms such as *Pseudomonas aeruginosa*.

Idiopathic copper-associated cirrhosis is a condition driven by copper accumulation toxicity or genetic defects in copper metabolism, leading to progressive hepatic fibrosis. There is no known overlap between Doripenem's mechanism and the pathophysiology of copper-mediated liver disease: Doripenem has no copper chelation activity, no hepatic fibrosis inhibition pathway, and no interaction with the known disease-relevant metabolic routes (e.g., ATP7B transporter function, ceruloplasmin regulation).

The TxGNN model's high-score prediction (99.00%) for this indication therefore appears to reflect a graph topology artifact rather than a genuine mechanistic link. The model's output for all 10 top-ranked indications consistently points to rare liver, vascular, and genetic disorders — none of which share a plausible biological mechanism with a carbapenem antibiotic. This pattern suggests the prediction warrants no further clinical development pursuit at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Doripenem currently has **no registered products** in India. The drug is not marketed under any authorization, and no license records are available in the regulatory database.

For reference, Doripenem (brand names including Doribax) is approved in the United States (FDA), European Union (EMA), and Japan (PMDA) for the treatment of complicated intra-abdominal infections, complicated urinary tract infections, and hospital-acquired/ventilator-associated pneumonia.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Full safety data (including CDSCO-sourced warnings, contraindications, and drug interaction records) was not available in this Evidence Pack. The DDI database query also returned an error due to a missing local data file. Before any clinical consideration of Doripenem, the following safety profile from international labelling should be reviewed:
>
> - **CNS toxicity risk**: Carbapenems, particularly imipenem, are associated with seizure risk; Doripenem carries a lower but non-negligible risk — especially relevant given that one predicted indication (neonatal epileptic encephalopathy) involves seizure disorders.
> - **Porphyria caution**: β-lactam antibiotics may trigger acute porphyria attacks; Doripenem's safety in hepatic porphyria (rank 6 predicted indication) has not been established.
> - **Renal dosing**: Dose adjustment required for renal impairment (CrCl < 50 mL/min).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Doripenem are rare hepatic, vascular, or genetic disorders for which the drug has no established or plausible mechanistic rationale. The prediction scores are high (98.5–99.0%), but this appears to reflect knowledge graph structural patterns rather than true biological plausibility. Zero supporting clinical trials or literature exist for any of the predicted indications, placing every candidate firmly at evidence level L5.

**To proceed, the following would be needed:**

- **Mechanistic re-evaluation**: Before any repurposing effort could be justified, a formal MOA gap analysis should be conducted to identify whether any off-target activity of Doripenem (e.g., metalloprotease inhibition given its β-lactam ring) could theoretically intersect with hepatic disease pathways.
- **Safety data retrieval**: Retrieve the full CDSCO/TFDA package insert, including all warnings and contraindications, before any indication expansion work begins.
- **DDI database repair**: Fix the missing DDI data file (`ddinter_code_A.csv`) to enable drug interaction screening.
- **India regulatory pathway assessment**: If any future indication were to be pursued, a regulatory strategy for India (CDSCO New Drug Application) would need to be developed from scratch given zero existing market presence.
- **Re-ranking review**: Consider applying a biological plausibility filter as a post-processing step to TxGNN outputs for antibiotic drug classes, as the current top-10 predictions for Doripenem show a systematic disconnect between the drug's known pharmacology and the predicted disease targets.

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application. Data cutoff: 2026-04-04.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

