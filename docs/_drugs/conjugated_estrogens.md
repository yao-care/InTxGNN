---
layout: default
title: Conjugated Estrogens
parent: 僅模型預測 (L5)
nav_order: 210
evidence_level: L5
indication_count: 10
---

# Conjugated Estrogens
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

# Conjugated Estrogens: From Menopausal Hormone Therapy to Migraine Disorder

## One-Sentence Summary

> Conjugated estrogens (DrugBank DB00286) is a well-established estrogen mixture used in menopausal hormone replacement therapy; however, this evidence pack contains **no formal original-indication record** (India license data and DrugBank indication text are both empty).
> The TxGNN model predicts it may be effective for **Migraine Disorder**, with **0 clinical trials** and **16 supporting publications** currently available — all observational/review level, with no interventional trial evidence.
> Critically, several *other* TxGNN-predicted indications for this same drug (migraine with brainstem aura, thrombophilia, antithrombin deficiency) surface known **estrogen-related thrombotic and vascular contraindications**, which must inform how the top-ranked candidate is handled.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (no India license data; DrugBank original-indication field empty). Conjugated estrogens is generically classified as a menopausal hormone replacement therapy (HRT) agent. |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L3 (observational studies / reviews; no RCTs) |
| India Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a High-severity data gap, DG002). Based on known information, conjugated estrogens is a mixture of equine-derived estrogenic hormones widely used for menopausal symptom relief; its efficacy in stabilizing hormone-related symptoms is well established, though the evidence pack itself does not record a formal approved indication text.

Mechanistically, migraine — particularly menstrual and perimenopausal migraine *without* aura — is strongly linked to fluctuating estrogen levels. "Estrogen withdrawal" is a well-documented trigger of migraine attacks, and multiple cohort studies in this pack (e.g., PMID 1167630, 12390622, 11306204) suggest that maintaining a stable estrogen level via replacement therapy can reduce attack frequency in susceptible postmenopausal or perimenstrual women. This gives the top-ranked prediction reasonable biological plausibility.

However, this rationale applies specifically to migraine *without* aura. The evidence pack's own rank-2 candidate ("migraine with brainstem aura") is explicitly flagged as **Hold** because estrogen exposure in aura-subtype migraine is a recognized stroke risk factor (WHO MEC Category 4-type contraindication). Since the disease label evaluated here — "migraine disorder" — does not distinguish aura status, any further work must stratify by aura subtype before proceeding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27251885](https://pubmed.ncbi.nlm.nih.gov/27251885/) | 2016 | Cohort | Neurology | Compared daily sex hormone levels between women with and without migraine history; found migraine-specific hormone profiles. |
| [15455962](https://pubmed.ncbi.nlm.nih.gov/15455962/) | 2004 | Cohort | Southern Medical Journal | Pilot study of a novel, low-cost hormonal prophylactic strategy for menstrual-associated migraine. |
| [11306204](https://pubmed.ncbi.nlm.nih.gov/11306204/) | 2001 | Cohort | Maturitas | Evaluated how hormone replacement therapy influences the course of primary headaches in postmenopausal women. |
| [12390622](https://pubmed.ncbi.nlm.nih.gov/12390622/) | 2002 | Cohort | Headache | Compared three oral HRT regimens and their differing effects on migraine course in postmenopausal women. |
| [1167630](https://pubmed.ncbi.nlm.nih.gov/1167630/) | 1975 | Cohort | Neurology | Defined estrogen-withdrawal migraine and tested premenstrual estrogen supplementation for prevention. |
| [28994639](https://pubmed.ncbi.nlm.nih.gov/28994639/) | 2018 | Review | Post Reproductive Health | Reviews estrogen withdrawal as a trigger of migraine without aura and the rationale for stable estrogen replacement. |
| [29521155](https://pubmed.ncbi.nlm.nih.gov/29521155/) | 2018 | Review | Climacteric | Reviews hormonal fluctuation as a migraine trigger across reproductive life and the menopausal transition. |
| [2046918](https://pubmed.ncbi.nlm.nih.gov/2046918/) | 1991 | Review | Neurology | Foundational review on the relationship between estrogens, progestins, and headache (abstract not available). |
| [8309263](https://pubmed.ncbi.nlm.nih.gov/8309263/) | 1994 | Review | Mayo Clinic Proceedings | Compares transdermal vs. oral estrogen therapy effectiveness across various clinical situations. |
| [197509](https://pubmed.ncbi.nlm.nih.gov/197509/) | 1977 | Review | Postgraduate Medicine | General review on maximizing benefits and minimizing risks of estrogen replacement in menopause. |

---

## India Market Information

Conjugated estrogens currently has **no marketing authorization record in India** within this evidence pack (market status: 未上市 / Not Marketed; total registrations: 0).

---

## Safety Considerations

Please refer to the package insert for safety information. Formal warnings, contraindications, and drug-interaction data are unavailable in this evidence pack — this is recorded as a **Blocking** data gap (DG001: TFDA-equivalent label warnings/contraindications missing), which by itself prevents a full S1 safety assessment. The DDI query also failed at the source-file level (missing local DDInter data file).

**Additional caution from within this evidence pack:** other TxGNN-predicted indications for the same drug independently surface well-documented estrogen-related contraindications — activated protein C resistance and increased venous thromboembolism risk (thrombophilia, rank 10), contraindication in antithrombin/Factor V/heparin cofactor II deficiencies (ranks 3, 4, 6), and stroke risk in migraine-with-aura (rank 2). These are not part of the formal `safety` block but are directly relevant to evaluating migraine disorder, since migraineurs have an elevated baseline stroke/VTE risk.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for estrogen in menstrual/perimenopausal migraine (without aura) is biologically plausible and supported by multiple cohort studies and reviews (L3), but the evidence pack has a **Blocking** gap on formal safety warnings/contraindications, the drug is not currently marketed in India (0 registrations), and this same evidence pack independently flags serious estrogen-related thrombotic/vascular contraindications that directly overlap with migraine populations. Proceeding without resolving these would be premature.

**To proceed, the following is needed:**
- Obtain official label/package-insert data (warnings, contraindications) — resolves Blocking gap DG001
- Obtain detailed mechanism-of-action data from DrugBank — resolves High-severity gap DG002
- Fix the DDI data source (missing local DDInter file) so drug-interaction screening can run
- Stratify any future protocol by migraine-with-aura vs. without-aura, excluding aura subtype given the stroke-risk signal already found in this pack
- Assess India market-entry feasibility given current non-marketed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

