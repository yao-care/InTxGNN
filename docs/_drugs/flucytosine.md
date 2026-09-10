---
layout: default
title: Flucytosine
parent: 僅模型預測 (L5)
nav_order: 356
evidence_level: L5
indication_count: 1
---

# Flucytosine
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

# Flucytosine: From Invasive Fungal Infections to Bone Paget Disease

## One-Sentence Summary

Flucytosine (DB01099) is an antifungal agent originally used for invasive fungal infections such as candidiasis and cryptococcosis, typically combined with amphotericin B. The TxGNN model predicts a possible effect on **Bone Paget Disease** with a very high similarity score, but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a purely computational hypothesis with no independent validation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Invasive fungal infections (candidiasis, cryptococcosis) — based on known pharmacology; no India licensing record exists |
| Predicted New Indication | Bone Paget Disease |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Flucytosine is an antimetabolite antifungal: it is taken up by fungal cells and converted by fungal cytosine deaminase into 5-fluorouracil (5-FU), which is then incorporated into fungal RNA/DNA to block nucleic acid synthesis. It has no comparable conversion pathway in human cells at therapeutic doses (humans have minimal cytosine deaminase activity), and is used clinically — almost always in combination with amphotericin B — for invasive candidiasis and cryptococcal meningitis.

Bone Paget disease, in contrast, is a disorder of localized bone remodeling driven by abnormally activated osteoclasts, with standard treatment (bisphosphonates) targeting osteoclast-mediated bone resorption directly. There is no established biological pathway connecting fungal cytosine deaminase/5-FU metabolism to osteoclast regulation or bone turnover.

Given this, the very high TxGNN score most likely reflects knowledge-graph embedding similarity (e.g., shared graph neighbors or indirect relational patterns) rather than a demonstrable pharmacological mechanism. Without any supporting mechanistic, preclinical, or clinical evidence, this prediction should be treated as a low-confidence hypothesis rather than a plausible repurposing candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

- **Drug Interactions**: 85 documented interactions on record. One **Major** interaction: **Deferiprone**. Numerous **Moderate** interactions, notably with nephrotoxic/renal-clearance-affecting agents that can raise Flucytosine levels and toxicity risk — **Amphotericin B** (conventional, lipid complex, liposomal, and cholesteryl sulfate formulations), **Vancomycin**, aminoglycosides (**Kanamycin, Neomycin, Streptomycin**), **Polymyxin B**, **Bacitracin**, **Pentamidine**, **Deferasirox**, and NSAIDs (**Ibuprofen**); also moderate interactions with 5-aminosalicylate agents (**Mesalazine, Balsalazide, Olsalazine, Sulfasalazine**) and radiopharmaceuticals (**Iobenguane I-131, Strontium chloride Sr-89**).

No safety data is available for warnings or contraindications in this evidence pack; please refer to the package insert for that information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction relies solely on a TxGNN model score (Evidence Level L5) with zero supporting clinical trials or literature, no established mechanistic link between antifungal 5-FU metabolism and osteoclast-driven bone pathology, a blocking gap in TFDA/local labeling data, and a drug that is not currently marketed in India. Combined with a substantial drug-interaction burden (85 interactions, including one Major), the current evidence does not justify moving beyond initial screening.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA label/warnings and contraindications) — currently blocking safety assessment
- Confirm original MOA via DrugBank (DG002) to properly evaluate mechanistic plausibility
- Independent preclinical or mechanistic rationale linking cytosine deaminase/5-FU pathway to osteoclast biology or bone turnover
- At minimum, case-report or in-vitro evidence before any further investment in this indication
- Full renal-function-based DDI risk assessment given Flucytosine's narrow therapeutic index and interaction profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

