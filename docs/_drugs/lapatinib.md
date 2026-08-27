---
layout: default
title: Lapatinib
parent: 僅模型預測 (L5)
nav_order: 370
evidence_level: L5
indication_count: 1
---

# Lapatinib
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

# Lapatinib: From HER2-Positive Breast Cancer to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Lapatinib (Tykerb) is a dual tyrosine kinase inhibitor targeting EGFR and HER2, approved globally for HER2-positive advanced or metastatic breast cancer.
The TxGNN model predicts it may be effective for **Dermatofibrosarcoma Protuberans (DFSP)**,
however, **no clinical trials** and **no publications** currently support this direction — placing this prediction at the lowest evidence level (L5).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive advanced/metastatic breast cancer |
| Predicted New Indication | Dermatofibrosarcoma Protuberans (DFSP) |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Lapatinib is a targeted kinase inhibitor in the anti-cancer drug class. Its efficacy in HER2-positive breast cancer has been established through multiple clinical trials, and its mechanism centers on reversible inhibition of the EGFR (ErbB1) and HER2 (ErbB2) receptor tyrosine kinases, thereby suppressing downstream proliferative signaling.

However, this prediction faces a meaningful mechanistic challenge: DFSP is primarily driven by the COL1A1-PDGFB chromosomal translocation, which constitutively activates the PDGFRβ signaling pathway — a pathway entirely distinct from the EGFR/HER2 axes that Lapatinib targets. While EGFR expression has been reported anecdotally in certain soft-tissue sarcomas, DFSP does not rely on EGFR or HER2 as a primary oncogenic driver, and there is no established biological rationale connecting the two.

The high TxGNN score (99.30%) most likely reflects phenotypic proximity in the knowledge graph — both conditions are skin-associated tumors with kinase-driven biology — rather than direct mechanistic support. Established first-line targeted therapies for DFSP (Imatinib, Avapritinib) already address the PDGFRβ pathway with clinical evidence, and Lapatinib offers no clear differentiated mechanism in this setting.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Dual EGFR/HER2 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Low — as a targeted agent, significant myelosuppression is uncommon; however, grade 1–2 neutropenia has been reported in combination regimens |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (hepatotoxicity; ALT/AST monitoring required), cardiac function (LVEF assessment for QT prolongation risk), CBC, renal function, electrolytes |
| Handling Protection | Follow institutional cytotoxic drug handling and disposal regulations |

---

## Safety Considerations

**Drug Interactions**: Lapatinib has 549 documented drug interactions. The following are the most clinically significant:

*Major interactions:*
- **Loperamide** — Risk of serious cardiac arrhythmia via QT prolongation; combination should be avoided or used with close cardiac monitoring
- **Clarithromycin** — Strong CYP3A4 inhibitor; significantly increases Lapatinib plasma concentrations and toxicity risk

*Moderate interactions (selected):*
- **Proton pump inhibitors** (Omeprazole, Rabeprazole, Dexlansoprazole): Elevated gastric pH reduces Lapatinib solubility and bioavailability; staggered dosing or avoidance recommended
- **H2 receptor antagonists** (Famotidine, Ranitidine, Cimetidine): Similar bioavailability reduction via pH effect
- **Corticosteroids** (Dexamethasone, Hydrocortisone, Betamethasone, Budesonide, Triamcinolone): CYP3A4 induction may reduce Lapatinib exposure and efficacy
- **Aprepitant**: Mixed CYP3A4 inhibition/induction; may alter Lapatinib plasma levels unpredictably
- **Saxagliptin, Pioglitazone**: Moderate metabolic interactions via CYP and transporter pathways

Please refer to the full drug interaction database and package insert for comprehensive safety information, including warnings and contraindications not captured in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.30%), there is zero supporting clinical or published evidence, and the mechanistic link between Lapatinib's EGFR/HER2 inhibition and DFSP's PDGFRβ-driven biology is weak. Effective PDGFR-targeted therapies already exist for this indication, making a Lapatinib-based approach difficult to justify without new preclinical or biomarker data.

**To proceed, the following is needed:**
- Preclinical data (in vitro or in vivo) demonstrating Lapatinib activity in DFSP cell lines or patient-derived xenograft models
- Tumor biomarker evidence of EGFR/HER2 co-expression or activation in DFSP specimens, identifying a potential patient subgroup
- Mechanistic rationale explaining why EGFR/HER2 inhibition would provide clinical benefit over established PDGFRβ-targeting agents (Imatinib, Avapritinib)
- Full MOA data from DrugBank to complete the mechanistic analysis and identify potential off-target effects relevant to DFSP
- Package insert (CDSCO/TFDA or equivalent) to complete safety evaluation for warnings and contraindications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

