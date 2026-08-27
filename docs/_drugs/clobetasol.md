---
layout: default
title: Clobetasol
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 1
---

# Clobetasol
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

# Clobetasol: From Inflammatory Dermatoses to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Clobetasol is a super-potent (class IV) topical corticosteroid conventionally used for inflammatory and pruritic dermatoses.
The TxGNN model predicts it may be effective for **Primary Cutaneous T-Cell Lymphoma (CTCL)**,
with **0 registered clinical trials** but **20 supporting publications**, including a cohort study and a direct comparative efficacy study, currently backing this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record in this jurisdiction (drug is not locally marketed; no approved-label indication text available) |
| Predicted New Indication | Primary Cutaneous T-Cell Lymphoma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Clobetasol is not available from DrugBank in this evidence pack (flagged as a High-severity data gap). Based on established pharmacology, Clobetasol propionate is a superpotent (class IV) topical corticosteroid known to suppress local inflammation and T-cell–mediated immune responses — it inhibits cytokine release and induces apoptosis of infiltrating lymphocytes. This mechanism gives it a direct, plausible effect on the malignant T-cell infiltrates that characterize cutaneous T-cell lymphoma (CTCL), particularly early-stage (patch-stage) mycosis fungoides.

The relationship between Clobetasol's conventional use in inflammatory/pruritic skin disease and the predicted new indication is mechanistically close: both settings involve pathological T-cell activity within the skin, and topical corticosteroids are already recognized in clinical practice (e.g., NCCN guidance, and the classic Zackheim case series below) as a standard first-line option for early-stage CTCL. This lends strong mechanistic plausibility to the TxGNN prediction.

That said, the supporting evidence is concentrated in **early/patch-stage** mycosis fungoides. Evidence for advanced tumor-stage disease or other CTCL subtypes (e.g., Sézary syndrome) is not established, and the prediction should not be extrapolated beyond early-stage disease without further data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32603400](https://pubmed.ncbi.nlm.nih.gov/32603400/) | 2020 | Cohort | Cutis | Observational study of topical clobetasol propionate 0.05% cream in early-stage mycosis fungoides; confirmed efficacy of superpotent topical corticosteroids with manageable cutaneous adverse effects |
| [39741016](https://pubmed.ncbi.nlm.nih.gov/39741016/) | 2025 | Comparative study | Anais Brasileiros de Dermatologia | Compared efficacy of clobetasol propionate versus bexarotene in early-stage mycosis fungoides |
| [14686970](https://pubmed.ncbi.nlm.nih.gov/14686970/) | 2003 | Case series | Dermatologic Therapy | ~200 patients with patch-stage mycosis fungoides treated with high-potency topical corticosteroids (predominantly clobetasol) at UCSF; response rate >90% with minor side effects; established topical clobetasol as first-line treatment for early-stage MF |
| [30677799](https://pubmed.ncbi.nlm.nih.gov/30677799/) | 2018 | Review | Dermatology Online Journal | Review of lymphomatoid papulosis, a CD30+ lymphoproliferative disorder within the CTCL spectrum, with excellent long-term prognosis |
| [17083888](https://pubmed.ncbi.nlm.nih.gov/17083888/) | 2006 | Review | Dermatology Online Journal | Review of CD30+ large T-cell lymphoma diagnostic distinction and management within the CTCL spectrum |
| [25027222](https://pubmed.ncbi.nlm.nih.gov/25027222/) | 2014 | Case Report | Nederlands Tijdschrift voor Geneeskunde | 9-year-old girl with hypopigmented mycosis fungoides successfully treated with clobetasol 0.05% ointment, 4 days/week |
| [28031140](https://pubmed.ncbi.nlm.nih.gov/28031140/) | 2016 | Case Report | Skinmed | Patient with cutaneous angioimmunoblastic T-cell lymphoma initially treated with topical clobetasol before diagnosis was established |
| [36846176](https://pubmed.ncbi.nlm.nih.gov/36846176/) | 2023 | Case Report | Clinical Case Reports | Mycosis fungoides presenting with psoriasiform plaques; initially managed with topical corticosteroids; includes literature review |
| [28804923](https://pubmed.ncbi.nlm.nih.gov/28804923/) | 2017 | Case Report | Pediatric Dermatology | Hypopigmented mycosis fungoides with large-cell transformation in an 8-year-old child |
| [23773745](https://pubmed.ncbi.nlm.nih.gov/23773745/) | 2013 | Case Report | Annales de Dermatologie et de Venereologie | Case report and literature review of papular mycosis fungoides, an early incipient form of the disease |

---

## Safety Considerations

**Drug Interactions**: A DDI screen (source: DDInter) identified **175** potential interacting drugs; interaction severity levels are not yet classified (all recorded as "Unknown" in the current dataset). Notable interacting agents include other systemic/topical corticosteroids (Prednisone, Prednisolone, Hydrocortisone, Triamcinolone) — combined use may raise the risk of additive immunosuppression or HPA-axis suppression — and Vitamin A / Calcitriol, relevant if co-administered with other topical vitamin A or D analogues in dermatologic regimens.

Detailed prescribing warnings and contraindications for Clobetasol are not yet available in this evidence pack — this is flagged as a **Blocking** data gap that must be resolved before a formal safety pre-assessment (S1) can proceed (see Conclusion below).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong and is reinforced by a cohort study, a direct clobetasol-vs-bexarotene comparative study, and a well-established historical case series (>200 patients, >90% response) supporting topical clobetasol as first-line therapy in early-stage mycosis fungoides — consistent with the L3 evidence level and TxGNN's high prediction score (99.51%). However, no clinical trials are registered for this specific indication, the drug is not currently marketed in this jurisdiction, and key local safety documentation (TFDA warnings/contraindications) is missing, warranting a guarded rather than unconditional recommendation.

**To proceed, the following is needed:**
- TFDA-approved product label data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action (MOA) data from DrugBank — currently a High-severity data gap (DG002)
- Clarification of local market/import pathway, since the drug currently holds no local registrations
- Scoping of any future trial or protocol strictly to early-stage/patch-stage CTCL, given the lack of evidence for advanced-stage or other CTCL subtypes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

