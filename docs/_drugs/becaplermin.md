---
layout: default
title: Becaplermin
parent: 僅模型預測 (L5)
nav_order: 93
evidence_level: L5
indication_count: 10
---

# Becaplermin
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

# Becaplermin: From Diabetic Neuropathic Ulcers to Amenorrhea

## One-Sentence Summary

Becaplermin (Regranex®) is a recombinant human platelet-derived growth factor-BB (rhPDGF-BB), originally approved in the United States for promoting healing of lower extremity diabetic neuropathic ulcers; it carries no registered product authorizations in India.
The TxGNN model's highest-ranked prediction suggests potential efficacy in **Amenorrhea** (score 99.86%), followed by 9 additional predicted indications spanning reproductive disorders, breast cancer subtypes, and pulmonary hypertension.
However, no clinical trials support any of the 10 predicted indications, and all carry a **Hold** recommendation — several with active FDA Black Box Warning contraindications and documented directional mechanistic safety risks.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Lower extremity diabetic neuropathic ulcers (US approval; not registered in India) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on publicly known information, Becaplermin is a recombinant form of human PDGF-BB — a potent mitogen and chemoattractant that stimulates fibroblast, smooth muscle cell, and mesenchymal cell proliferation and migration to promote granulation tissue formation and wound healing. Its established therapeutic role is in diabetic neuropathic ulcer management.

For the highest-ranked prediction, **amenorrhea**, the mechanistic connection is tenuous at best. While PDGF-BB has documented physiological expression in the endometrium and ovarian stroma, the primary etiologies of amenorrhea — hypothalamic-pituitary-ovarian axis dysregulation, endometrial scarring (Asherman's syndrome), or structural abnormalities — have no established PDGF-driven therapeutic targets. The TxGNN score of 0.9986 most likely reflects a **graph homophily propagation artifact**, where reproductive system nodes cluster closely in the knowledge graph, generating spuriously high scores rather than genuine therapeutic signals.

A critical observation across all 10 predicted indications is a recurring **directional mismatch**: for pulmonary hypertension (Rank 5) and multiple breast cancer subtypes (Ranks 3, 4, 6, 7, 8), existing peer-reviewed literature demonstrates that PDGF pathway **activation** drives disease pathology rather than offering a therapeutic opportunity. This fundamentally undermines these predictions as viable repurposing candidates, regardless of TxGNN score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Becaplermin across any of the 10 predicted indications (amenorrhea, erectile dysfunction, HER2+ breast carcinoma, PR-negative breast cancer, pulmonary hypertension, PR+ breast cancer, normal breast-like subtype, breast luminal A/B, hypogonadotropic hypogonadism, or Leydig cell hypoplasia).

---

## Literature Evidence

No literature directly supporting Becaplermin as a treatment for amenorrhea (Rank 1, the top-predicted indication) was identified.

For broader mechanistic context, the following selected papers from other predicted indications highlight important biological signals — particularly safety warnings regarding PDGF-B's pathological role in several predicted conditions:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33591958](https://pubmed.ncbi.nlm.nih.gov/33591958/) | 2021 | Translational Mechanistic | JCI Insight | Macrophage-derived PDGF-B directly induces muscularization of distal pulmonary arterioles in PH models — Becaplermin (PDGF-BB agonist) would be expected to accelerate this pathological remodeling ⚠️ |
| [18420966](https://pubmed.ncbi.nlm.nih.gov/18420966/) | 2008 | Clinical/Translational | Am J Respir Crit Care Med | PDGF promotes PASMC proliferation and migration; elevated PDGF expression found in idiopathic PAH lung tissue — PDGF pathway is pathological, not therapeutic, in PAH ⚠️ |
| [39901736](https://pubmed.ncbi.nlm.nih.gov/39901736/) | 2025 | Preclinical | Am J Hypertension | PDGF-BB-induced PASMCs used as a standard PAH disease induction model — confirms PDGF-BB as a disease driver, not a treatment |
| [38614383](https://pubmed.ncbi.nlm.nih.gov/38614383/) | 2024 | Preclinical Pharmacology | Eur J Pharmacol | Corosolic acid treats PAH by **attenuating** PDGF signaling in macrophages and SMCs — therapeutic strategy is PDGF inhibition, the opposite of Becaplermin's action ⚠️ |
| [21733044](https://pubmed.ncbi.nlm.nih.gov/21733044/) | 2011 | In vivo Preclinical | Cancer Science | Soluble PDGFRβ (decoy receptor that **inhibits** PDGF-BB/DD) suppresses intraosseous breast cancer growth — suggests PDGF-BB activation may promote bone metastasis ⚠️ |
| [28245285](https://pubmed.ncbi.nlm.nih.gov/28245285/) | 2017 | Basic Science / Mechanistic | PLoS ONE | PDGFR/STAT3 signaling regulates corpus cavernosum smooth muscle phenotypic transition toward synthetic (pro-fibrotic) type in rats — direction of effect with Becaplermin in ED is ambiguous |

> **Data quality note for Ranks 8 & 9:** Literature retrieved for "breast tumor luminal A or B" (19 papers) and "hypogonadotropic hypogonadism with anosmia" (20 papers) consisted entirely of false positives — B-cell immunology/HBV papers and COVID-19 anosmia papers, respectively — due to keyword matching artifacts ("B" matching B cells/Hepatitis B; "anosmia" matching COVID-19 symptom literature). Effective evidence for these indications after filtering: **zero**.

---

## India Market Information

Becaplermin is not registered in India. No CDSCO product authorizations are on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | No India registrations found |

---

## Safety Considerations

- **FDA Black Box Warning — Cancer Mortality Risk**: Becaplermin carries an FDA Black Box Warning stating that patients who used 3 or more tubes had an increased rate of cancer mortality compared to controls. This warning directly contraindicates investigation for any malignancy-related indication and is relevant to Ranks 3 (HER2+ breast carcinoma), 4 (PR-negative breast cancer), 6 (PR+ breast cancer), 7 (normal breast-like subtype), and 8 (breast luminal A/B) in this report.

- **Directional Mechanistic Risk — Pulmonary Hypertension (Rank 5)**: At least 5 of the 20 retrieved papers use PDGF-BB as a standard **disease induction stimulus** in experimental PAH models, and multiple therapeutic agents are evaluated precisely by their ability to suppress PDGF signaling. Administering a PDGF-BB agonist to PAH patients would theoretically accelerate pulmonary vascular remodeling and worsen disease.

- **Directional Mechanistic Risk — Breast Cancer Bone Metastasis (Rank 4)**: PMID 21733044 demonstrates that blocking PDGFRβ signaling suppresses breast cancer intraosseous growth, suggesting that PDGF pathway activation (Becaplermin's mechanism) may be pro-metastatic in this context.

Please refer to the US prescribing information (Regranex®) and any applicable CDSCO/TFDA package insert for complete warnings, contraindications, and adverse event profiles.

---

## Conclusion and Next Steps

**Decision: Hold (All 10 Predicted Indications)**

**Rationale:**
None of the 10 TxGNN-predicted indications reaches a clinically actionable evidence level. The top prediction (amenorrhea, L5) rests solely on model output with no biological or clinical corroboration, and the underlying mechanistic link to PDGF signaling is speculative. The best-evidenced prediction (pulmonary hypertension, 20 literature hits, L4) presents a clear and concerning safety paradox: the literature almost uniformly frames PDGF-BB as a driver of disease induction rather than a treatment target. Five breast cancer predictions are additionally constrained by the FDA Black Box Warning against use in malignancy patients.

**To proceed, the following is needed:**

- **Resolve Data Gaps**: Retrieve Becaplermin's complete MOA, pharmacokinetics, and safety profile from DrugBank API; download and parse TFDA/CDSCO prescribing information to characterize warnings and contraindications (currently both flagged as Data Gaps)
- **Cancer indications (Ranks 3, 4, 6, 7, 8)**: Require a compelling mechanistic rationale and explicit regulatory strategy to address the FDA Black Box Warning before any oncology repurposing investigation can ethically proceed
- **Pulmonary hypertension (Rank 5)**: Requires robust preclinical evidence demonstrating net therapeutic benefit despite PDGF-B's documented pro-remodeling role — current evidence strongly suggests harm
- **Redirect repurposing focus**: Consider indications more aligned with PDGF-BB's established wound-healing and tissue-repair biology — for example, chronic non-healing ulcers in non-diabetic populations, radiation-induced tissue injury, or systemic sclerosis-related cutaneous fibrosis — rather than the current Top 10 predictions
- **Improve literature retrieval quality**: Implement keyword disambiguation in the PubMed pipeline to eliminate false positives for generic term searches ("B" for B cells/Hepatitis B, "anosmia" for COVID-19 anosmia); an estimated 39 of the total retrieved papers across all indications were irrelevant false positives
- **CDSCO registration pathway**: Should a viable indication be identified, a de novo CDSCO registration process would be required, as there are no existing India approvals to leverage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

