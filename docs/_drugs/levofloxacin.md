---
layout: default
title: Levofloxacin
parent: 僅模型預測 (L5)
nav_order: 358
evidence_level: L5
indication_count: 10
---

# Levofloxacin
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

# Levofloxacin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Levofloxacin is a broad-spectrum fluoroquinolone antibiotic, widely used for the treatment of bacterial infections including respiratory tract, urinary tract, and skin and soft tissue infections.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis (PEK)**,
with **0 clinical trials** and **1 publication** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (respiratory tract, urinary tract, skin and soft tissue) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| India Market Status | Not marketed (0 registrations on record) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on established pharmacological knowledge, Levofloxacin is a third-generation fluoroquinolone antibiotic that inhibits two bacterial enzymes — DNA gyrase (topoisomerase II) and topoisomerase IV — which are essential for DNA replication, transcription, and repair. This mechanism confers broad-spectrum activity against both Gram-positive and Gram-negative bacteria. Notably, ophthalmic formulations of Levofloxacin (Quixin 0.5%, Iquix 1.5%) are already approved for bacterial conjunctivitis and bacterial corneal ulcers, establishing a precedent for ocular surface use.

Punctate epithelial keratoconjunctivitis (PEK) describes a superficial corneal-conjunctival epithelial injury pattern that can arise from multiple etiologies: bacterial infection, viral infection (most commonly adenovirus), toxic or medicamentous exposure, and dry eye disease. For cases with a confirmed bacterial etiology, there is a plausible mechanistic link to Levofloxacin given its high penetration into ocular surface tissues and its established ophthalmic antibacterial activity. The TxGNN model likely captures this indirect relationship based on Levofloxacin's adjacency in the knowledge graph to bacterial ocular surface disease.

However, the majority of PEK cases are non-bacterial in origin — viral, toxic, or dry-eye-driven — for which an antibacterial mechanism offers no direct benefit. The prediction is therefore conditionally reasonable in a narrow subset of PEK cases (bacterially confirmed), but lacks general applicability across the full disease spectrum. This limits the translational value without etiology-specific patient stratification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Outbreak Case Series | American Journal of Ophthalmology | Reports an outbreak of **microsporidial** keratoconjunctivitis linked to contaminated swimming pools in Taiwan; describes clinical presentation consistent with PEK. Note: microsporidial etiology is not a primary indication for fluoroquinolone antibiotics, limiting direct relevance. |

---

## India Market Information

Based on the available regulatory dataset, Levofloxacin currently has **no registered products** in the India market (0 licenses on record). This may represent a data gap rather than a true absence of market presence, and independent verification via CDSCO records is recommended before drawing regulatory conclusions.

---

## Safety Considerations

**Drug Interactions**: The DDI database identifies **434 total interactions** for Levofloxacin. Clinically significant interactions from the reviewed sample include:

- **Major interactions**:
  - *Tramadol* — Increased risk of seizures and CNS toxicity (lowered seizure threshold)
  - *Hydrocortisone* — Elevated risk of tendon rupture and tendinopathy (class effect: fluoroquinolones + corticosteroids)

- **Moderate interactions** (selected clinically relevant examples):
  - *NSAIDs* (Ibuprofen, Ketorolac) — Additive risk of CNS stimulation and seizures
  - *Antidiabetic agents* (Metformin, Pioglitazone, Alogliptin, Acarbose, Albiglutide) — Potential alterations in glycemic control; monitor blood glucose
  - *Beta-agonists* (Formoterol, Salbutamol) — Additive QT prolongation risk
  - *Alfuzosin, Famotidine, Adenosine, Ethinylestradiol, Abiraterone, Amifampridine* — Moderate interactions requiring clinical monitoring

- **Minor interactions**: Paclitaxel, Aldesleukin, Altretamine

Please refer to the full package insert for complete warnings and contraindications, which are not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the TxGNN model assigns a high prediction score (99.92%), this likely reflects Levofloxacin's proximity to bacterial ocular surface diseases in the knowledge graph rather than direct evidence for PEK. Only one indirectly relevant case series was identified, no clinical trials exist, and PEK is predominantly non-bacterial in etiology — making Levofloxacin's antibacterial mechanism applicable only to a narrow, etiology-dependent patient subset.

**To proceed, the following is needed:**

- **Etiology stratification**: Identify the proportion of PEK cases with confirmed bacterial origin in target populations, as this is the only patient group where a mechanistic rationale exists
- **Dedicated clinical evidence**: Prospective studies or retrospective case series specifically evaluating Levofloxacin ophthalmic formulations in bacterially-confirmed PEK
- **Comparative effectiveness data**: Head-to-head comparison with current standard-of-care ophthalmic antibiotics (e.g., moxifloxacin, tobramycin) for bacterial PEK
- **MOA data gap closure**: Retrieve full CDSCO/DrugBank mechanism data (Data Gap DG002) to formalize the mechanistic rationale
- **Regulatory label review**: Obtain and parse CDSCO package insert for key warnings and contraindications (Data Gap DG001, currently Blocking)
- **India market verification**: Cross-check CDSCO database to confirm whether the 0-registration status reflects a true data gap or actual absence of approval

> **Note for reviewers**: While this report focuses on the top-ranked TxGNN prediction (PEK, L4 evidence), the evidence pack also contains a higher-evidence signal for **Monoclonal Gammopathy / Multiple Myeloma** (Rank 7, **Evidence Level L1**) — supported by the landmark TEAMM Phase 3 RCT (*Lancet Oncology*, 2019) and 20 publications. This indication (infection prophylaxis in newly diagnosed myeloma patients) represents a substantially stronger repurposing candidate and warrants a separate, dedicated evaluation.

---
*This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

