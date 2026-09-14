---
layout: default
title: Vancomycin
parent: 僅模型預測 (L5)
nav_order: 872
evidence_level: L5
indication_count: 10
---

# Vancomycin
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

# Vancomycin: From Gram-Positive Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

> Vancomycin is a glycopeptide antibiotic with an established clinical role in treating serious Gram-positive bacterial infections (e.g., MRSA), a use referenced repeatedly in this Evidence Pack's mechanistic analyses even though it is not captured in the record's structured indication fields.
> The TxGNN model assigns its **highest prediction score (99.92%)** to **Diffuse Scleroderma**, but this association is currently supported by only **1 case report** and **no clinical trials** — and that single report describes a drug-related allergic rash, not therapeutic efficacy.
> Evidence quality is at the lowest tier (L5), and the pipeline's own scoring recommends **Hold**.

> **Note:** This Evidence Pack screened 10 candidate indications for Vancomycin. Among them, *streptococcal pneumonia* (rank 9) is substantially better supported (L3, "Proceed with Guardrails") because it aligns with vancomycin's already-established role in treating penicillin-resistant *S. pneumoniae*. The top-ranked candidate featured below is simply the single highest TxGNN score in the pack, not the strongest repurposing hypothesis overall — see Conclusion for detail.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in structured fields (original_indications and licenses are both empty in this record). Vancomycin's established clinical use — serious Gram-positive bacterial infections, e.g., MRSA — is referenced throughout the evidence pack's mechanistic rationale text. |
| Predicted New Indication | Diffuse Scleroderma |
| TxGNN Prediction Score | 99.92% (rank 1,889 overall) |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is marked as a data gap (DG002) in this record. Based on the pharmacological class information embedded in this Evidence Pack's own rationale text, Vancomycin is a **glycopeptide antibiotic** that inhibits bacterial **peptidoglycan (cell wall) synthesis**, giving it activity restricted to Gram-positive organisms.

Diffuse scleroderma is an autoimmune connective-tissue disease with no infectious pathophysiology. The pack's own repurposing rationale states explicitly: *"對自體免疫結締組織疾病（硬皮症）無已知機轉關聯"* — there is no known mechanistic link between Vancomycin's cell-wall-synthesis-inhibition activity and autoimmune fibrotic disease.

The only supporting literature (PMID 31541072) is a case report of a drug-associated exfoliative rash with sepsis and eosinophilia, i.e., an **adverse-reaction narrative**, not evidence of therapeutic benefit in scleroderma. This pattern is consistent with a TxGNN knowledge-graph co-occurrence artifact rather than a biologically grounded repurposing hypothesis, and it explains why the pipeline's own scoring stage already flags the recommendation as **Hold**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case Report | The American Journal of Case Reports | Describes a 56-year-old man with diffuse exfoliative rash, sepsis, and eosinophilia following antibiotic treatment (including vancomycin exposure history). Reports a suspected drug hypersensitivity/adverse reaction — not a treatment outcome for scleroderma. |

---

## India Market Information

No CDSCO/India market authorizations are on file for Vancomycin in this record (`market_status`: Not Marketed; `total_licenses`: 0).

---

## Safety Considerations

**Drug Interactions**: A DDI query returned **454 total interactions** on file. Selected examples from the returned set:

- **Major-level**: Human immunoglobulin G (intravenous); Human botulinum neurotoxin A/B immune globulin; Vibrio cholerae CVD 103-HgR strain live antigen (live)
- **Moderate-level**: Ketorolac, Ibuprofen, Diclofenac, Celecoxib (NSAIDs); Amikacin, Capreomycin, Amphotericin B/Amphotericin B (lipid complex) (nephrotoxicity-related co-administration); Ethinylestradiol, Estradiol; Metformin; Carboplatin; Bacitracin; Mesalazine, Balsalazide; Ibandronate; Cholestyramine

Label-level warnings and contraindications are not available in this record (blocked by data gap DG001 — see Conclusion).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (diffuse scleroderma) has no mechanistic plausibility, no clinical trial evidence, and a single supporting citation that describes an adverse drug reaction rather than efficacy — evidence level L5. A blocking data gap (DG001: no TFDA/CDSCO label warnings or contraindications on file) also prevents this candidate from entering the S1 safety pre-screen regardless of efficacy evidence.

**To proceed, the following is needed:**
- Official product label / package insert data (warnings, contraindications) to close blocking gap DG001
- Formal DrugBank MOA confirmation to close gap DG002
- If pursuing repurposing evaluation for Vancomycin further, prioritize re-review of **streptococcal pneumonia** (rank 9 in this pack), which already carries L3 evidence and a "Proceed with Guardrails" recommendation grounded in existing clinical practice (vancomycin as an established option for penicillin-resistant *S. pneumoniae*)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

