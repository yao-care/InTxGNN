---
layout: default
title: Crizotinib
parent: Model Prediction Only (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# Crizotinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Crizotinib: From Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Crizotinib is an ALK/ROS1/MET tyrosine kinase inhibitor originally developed for ALK-positive/ROS1-positive non-small cell lung cancer (NSCLC) — this is documented in the literature within this evidence pack rather than in formal India regulatory records, since the drug is not currently marketed in India. The TxGNN model's top-ranked prediction for this drug is **Gingival Fibromatosis**, but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model prediction with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in India licensing (drug not marketed); per literature in this pack, crizotinib is approved for ALK-positive/ROS1-positive non-small cell lung cancer (NSCLC) |
| Predicted New Indication | Gingival Fibromatosis |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap in DrugBank for this evidence pack. However, literature captured elsewhere in this same evidence pack (PMID 24756793, PMID 30069759) describes crizotinib as an ATP-competitive small-molecule inhibitor of the receptor tyrosine kinases c-Met, ALK, and ROS1, approved for NSCLC harboring EML4-ALK rearrangements and, subsequently, ROS1-rearranged NSCLC.

Gingival fibromatosis is a benign, non-neoplastic overgrowth of gingival connective tissue, typically driven by fibroblast proliferation (often hereditary or drug-induced, e.g., by phenytoin, cyclosporine, or calcium channel blockers). There is no established biological pathway linking ALK, ROS1, or MET signaling to gingival fibroblast overgrowth, and no clinical or preclinical literature in this evidence pack draws that connection.

Consistent with this, the model's own rationale record for this candidate states explicitly that there is no supporting trial or literature evidence and no known mechanistic link — the prediction reflects a TxGNN network-proximity signal only, not a validated pharmacological hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Cytotoxicity

Crizotinib is classified as an antineoplastic agent (targeted small-molecule kinase inhibitor used in oncology), so cytotoxicity considerations are included even though the predicted indication above is non-oncologic.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1/MET tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function (ALT/AST/bilirubin — reports of fulminant hepatotoxicity), cardiac monitoring (ECG/QT interval — reports of bradycardia, QT prolongation, and multiple simultaneous cardiac toxicities), pulmonary symptoms (reports of drug-induced interstitial lung disease/organizing pneumonia) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

**Drug Interactions**: A DDI query returned 566 total interactions. Notable **Major**-level interactions identified include Clarithromycin, Cisapride, Dolasetron, Eliglustat, and Granisetron. Multiple **Moderate**-level interactions were also identified, including Famotidine, Metformin, Loperamide, Bupropion, Aprepitant, and Dexamethasone.

Key warnings and contraindications are not currently available in this evidence pack — please refer to the package insert for that information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Gingival Fibromatosis) has no clinical trial or literature support and no plausible mechanistic link to crizotinib's ALK/ROS1/MET-inhibiting activity — evidence level L5 does not meet the threshold to advance this candidate.

**To proceed, the following is needed:**
- Preclinical or mechanistic data establishing any plausible link between ALK/ROS1/MET signaling and gingival fibroblast proliferation
- Formal MOA and safety documentation (both currently flagged as data gaps, one of them Blocking)
- India-specific regulatory/label data, since the drug is currently not marketed there
- Note: within this same evidence pack, other predicted indications for crizotinib carry materially stronger evidence and may warrant prioritization instead — notably "lung hilum carcinoma" (L3, Proceed with Guardrails) and "lung benign neoplasm" (L2, though its literature appears to reflect malignant ALK+/ROS1+ NSCLC trials rather than benign disease and should be re-verified for disease-label accuracy before use)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

