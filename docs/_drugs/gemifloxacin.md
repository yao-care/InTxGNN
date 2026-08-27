---
layout: default
title: Gemifloxacin
parent: 僅模型預測 (L5)
nav_order: 309
evidence_level: L5
indication_count: 10
---

# Gemifloxacin
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

# Gemifloxacin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

> Gemifloxacin is a fluoroquinolone antibacterial agent; per the notes embedded in this evidence pack, it acts by inhibiting bacterial DNA gyrase/topoisomerase IV and its antibacterial spectrum concentrates on respiratory pathogens such as *Streptococcus pneumoniae*.
> The TxGNN model predicts a possible association with **Hyperamylasemia**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack itself notes no known biological pathway connecting the drug's antibacterial mechanism to this outcome.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (fluoroquinolone antibacterial) — no formal India/Taiwan market license record is available to cite a specific approved indication text |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| India Market Status | Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not available for Gemifloxacin in this evidence pack — it is flagged as a **High-severity data gap (DG002)**. Based on information embedded in the repurposing-rationale text of this evidence pack, Gemifloxacin belongs to the fluoroquinolone class of antibacterials, working through inhibition of bacterial DNA gyrase and topoisomerase IV, with an antibacterial spectrum noted to concentrate on respiratory pathogens such as *Streptococcus pneumoniae*.

The relationship between the original indication (bacterial infection) and the top-ranked predicted indication (Hyperamylasemia) is weak. Hyperamylasemia is a metabolic/pancreatic biochemical abnormality; per the evidence pack's own assessment, it has **no known biological pathway connection** to Gemifloxacin's DNA gyrase/topoisomerase IV inhibition mechanism. The very high TxGNN score (99.89%) more likely reflects topological similarity in the knowledge graph's node embeddings (e.g., shared neighbors within the same drug class) rather than a causal pharmacological relationship — a caveat the evidence pack states explicitly.

Across all ten TxGNN-predicted indications in this pack, mechanistic plausibility is generally low to absent (hyperamylasemia, polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility, premalignant hematological disease, monoclonal gammopathy, and congenital hematological disorder are all noted as having no biologically plausible link to an antibacterial mechanism). Two exceptions are only partially plausible: septicemic plague (rank 8) has class-level plausibility because fluoroquinolones are an accepted alternative treatment for *Yersinia pestis*, but no Gemifloxacin-specific evidence exists; endomyometritis (rank 10) has theoretical antibacterial relevance, but Gemifloxacin's spectrum has limited anaerobic coverage and is not a standard choice for this indication. One prediction (rank 7, hematological disease with acquired peripheral neuropathy) is flagged as potentially **conflicting with a known fluoroquinolone class safety signal** (peripheral neuropathy risk) rather than supporting a therapeutic use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

No registration or license records are available for Gemifloxacin in this jurisdiction. Market status is recorded as **Not marketed** with **0 total licenses**.

---

## Safety Considerations

- **Drug Interactions**: 273 total documented interactions were identified (source: DDInter). Among the interactions listed, **Major-level** interactions include Hydrocortisone, Betamethasone, Chlorpropamide, and Dolasetron. **Moderate-level** interactions include Metformin, Pioglitazone, Acarbose, Bisacodyl, Calcium acetate, Clarithromycin, Famotidine, Acetylsalicylic acid, and several glucose-lowering agents (Albiglutide, Alogliptin, Canagliflozin, Dapagliflozin, Dulaglutide, Empagliflozin, Loperamide) — a pattern consistent with the known fluoroquinolone-class risk of glycemic disturbance when combined with antidiabetic agents. **Minor-level**: Cimetidine.
- **Note**: Official label-level safety information (key warnings and contraindications) is not yet available in this evidence pack. This is flagged as a **Blocking-severity data gap (DG001)** and prevents the candidate from entering the S1 safety pre-assessment stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-predicted indications in this pack are rated Evidence Level L5 (model prediction only, zero supporting clinical trials or publications) with decision stage S0, and the evidence pack itself recommends "Hold" for every candidate. The mechanistic rationale for the top-ranked prediction (Hyperamylasemia) is explicitly assessed as lacking a known biological pathway, and the drug currently has no market presence (0 registrations). Combined with a Blocking-severity gap on official label warnings/contraindications (DG001) and a High-severity gap on MOA (DG002), this candidate cannot yet proceed to safety review.

**To proceed, the following is needed:**
- Official label/regulatory safety data (warnings, contraindications) — Blocking gap DG001
- Verified mechanism of action documentation — High-severity gap DG002
- Drug-specific preclinical or clinical evidence connecting Gemifloxacin to Hyperamylasemia (currently zero trials/publications)
- If the septicemic plague signal (rank 8) is pursued instead, dedicated pharmacokinetic/pharmacodynamic data against *Yersinia pestis* are needed, since current support is class-level extrapolation only, not drug-specific evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

