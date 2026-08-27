---
layout: default
title: Itopride
parent: 僅模型預測 (L5)
nav_order: 354
evidence_level: L5
indication_count: 10
---

# Itopride
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

# Itopride: From Functional Dyspepsia to Small Bowel Crohn Disease

## One-Sentence Summary

Itopride is a dual-mechanism prokinetic agent (dopamine D2 antagonist + acetylcholinesterase inhibitor) approved for functional dyspepsia and non-ulcer dyspepsia.
The TxGNN model predicts it may be effective for **Small Bowel Crohn Disease** with a score of **99.90%**,
however **no clinical trials and no supporting literature** currently exist for this indication, placing the evidence at Level L5 (model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Functional dyspepsia / Non-ulcer dyspepsia |
| Predicted New Indication | Small Bowel Crohn Disease |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (model prediction only, no actual studies) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data pack. Based on known information, Itopride combines dopamine D2 receptor antagonism with acetylcholinesterase (AChE) inhibition. By blocking D2 receptors in the enteric nervous system, it removes the inhibitory brake on gastrointestinal motility; simultaneously, AChE inhibition increases local acetylcholine levels, enhancing smooth muscle contractility throughout the GI tract. Its established efficacy in functional dyspepsia and non-ulcer dyspepsia confirms a predominantly gut-directed pharmacological profile.

The predicted link to small bowel Crohn disease is mechanistically tenuous. Crohn disease is driven by dysregulated mucosal immunity — T-cell-mediated inflammation, cytokine cascades (TNF-α, IL-12/23), and transmural granulomatous injury — none of which are direct targets of Itopride. While D2 antagonism carries a theoretical mild enteric anti-inflammatory potential, this remains speculative and has not been demonstrated in inflammatory bowel disease models.

The high TxGNN score most likely reflects co-occurrence of gastrointestinal tract nodes in the underlying knowledge graph rather than a direct biological mechanism. Itopride's prokinetic action might offer symptomatic relief of dysmotility features that co-exist with Crohn disease, but this is a supportive role at best, not a disease-modifying one.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Itopride in Small Bowel Crohn Disease.

---

## Literature Evidence

Currently no related literature available for Itopride in Small Bowel Crohn Disease.

---

## India Market Information

Itopride is currently **not marketed in India** and holds **zero registered licenses**. No product authorization data is available for this market.

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ Note: CDSCO package insert warnings, contraindications, and drug interaction data were identified as data gaps in this evidence pack. Safety review cannot be completed until these materials are retrieved from official sources.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model yields a high prediction score, but the mechanistic link between Itopride's prokinetic dual action and the immune-inflammatory pathology of small bowel Crohn disease is not supported by any clinical trials or published literature. The prediction is assessed as a likely knowledge-graph false positive arising from shared GI tract node proximity. Proceeding without a credible mechanistic hypothesis and with zero clinical evidence would not be a productive use of development resources at this stage.

**To proceed, the following is needed:**

- **Mechanistic validation**: Identify whether Itopride's D2 antagonism has any documented effect on intestinal mucosal immunity or Crohn-related inflammatory pathways (in vitro / animal data minimum)
- **MOA data gap resolution**: Retrieve full DrugBank mechanism-of-action profile to enable proper target-disease mapping
- **Safety data gap resolution**: Download and parse the CDSCO / approved market package insert to complete contraindication and warning review
- **Literature expansion**: Conduct a broader PubMed search combining "itopride" with "inflammatory bowel disease", "intestinal inflammation", or "Crohn" to verify the zero-evidence finding
- **Indication re-ranking review**: Consider deprioritising rank 1 and focusing development resources on mechanistically stronger candidates from this same pack — notably **gastric dilatation** (rank 8) and **hiatus hernia** (rank 4), both of which have direct pathophysiological overlap with Itopride's known prokinetic mechanism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

