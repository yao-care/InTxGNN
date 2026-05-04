---
layout: default
title: Mometasone
parent: 僅模型預測 (L5)
nav_order: 363
evidence_level: L5
indication_count: 1
---

# Mometasone
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

# Mometasone: From Allergic Rhinitis & Skin Disorders to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Mometasone is a potent synthetic glucocorticoid used intranasally and topically for allergic rhinitis, asthma, nasal polyposis, and inflammatory skin conditions.
The TxGNN model predicts it may be effective for **Primary Cutaneous T-Cell Lymphoma (CTCL)**,
with **0 registered clinical trials** and **2 case report publications** currently available to support this direction — placing it at an early exploratory stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis, asthma, nasal polyposis, allergic skin disorders |
| Predicted New Indication | Primary cutaneous T-cell lymphoma (CTCL) |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 (mechanism-based; no controlled trials) |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Mometasone is a high-potency synthetic glucocorticoid that exerts its effects by binding to the glucocorticoid receptor (GR, encoded by *NR3C1*). Upon activation, the GR–ligand complex translocates to the nucleus and modulates transcription of target genes. This mechanism underpins its well-established anti-inflammatory and immunosuppressive actions in allergic and inflammatory conditions.

The connection to CTCL — a malignancy of skin-resident T lymphocytes — is mechanistically plausible via at least three pathways: (1) **direct pro-apoptotic signalling** in malignant T cells through GR-α activation of the BIM/PUMA pathway; (2) **tumour microenvironment disruption** via suppression of NF-κB, IL-2, IL-4, and IL-13, which are key Th2 cytokines that sustain the neoplastic milieu; and (3) **anti-proliferative effects** on lymphoid cells that are characteristic of all potent glucocorticoids.

This biological rationale is not merely theoretical. NCCN guidelines already list Class I–II topical corticosteroids as a standard treatment option for early-stage Mycosis Fungoides (MF, the most common CTCL subtype, accounting for ~75% of cases) at stages IA–IIA. Mometasone, a Class II corticosteroid, falls squarely within this recommended class. The existing clinical gap is that most supporting evidence has been generated with Class I agents (e.g., clobetasol propionate), and mometasone-specific CTCL data remain sparse. The TxGNN knowledge graph prediction likely surfaces this connection by recognising the shared GR-mediated pharmacology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Mometasone in primary cutaneous T-cell lymphoma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25442255](https://pubmed.ncbi.nlm.nih.gov/25442255/) | 2015 | Case Report | Journal of Cutaneous Pathology | Reports an 11-year-old boy with a 7-year history of CD8⁺CD56⁺ cytotoxic-phenotype Mycosis Fungoides; illustrates challenges in paediatric CTCL diagnosis and documents corticosteroid use as part of clinical management |
| [40821495](https://pubmed.ncbi.nlm.nih.gov/40821495/) | 2025 | Case Report | Proceedings (Baylor University Medical Center) | Reports a 62-year-old woman with refractory cutaneous pseudolymphoma; mometasone was used unsuccessfully prior to escalation to tapinarof, indirectly demonstrating mometasone's involvement in cutaneous lymphoproliferative management |

---

## India Market Information

Mometasone currently has **no registered products** in India (0 approvals on record). This drug is classified as **not marketed** in India under the available regulatory data.

---

## Safety Considerations

**Drug-Target Interaction (Pharmacology):**
Mometasone is a synthetic glucocorticoid that acts as a ligand at the **Glucocorticoid Receptor (GR / NR3C1, Entrez Gene: 2908)**. Marketed formulations include:
- **Nasonex®** (intranasal, for allergic rhinitis and nasal polyposis)
- **Elocon®** (topical, for inflammatory skin disorders)
- **Enerzair® Breezhaler®** (QVM149, fixed-dose combination with indacaterol/glycopyrronium, for uncontrolled asthma — completed Phase 3)

Please refer to the package insert for complete warnings, contraindications, and safety information, as these data were not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for mometasone in CTCL is biologically coherent and grounded in NCCN-recognised clinical practice for early MF, but the current evidence pack contains only 2 case reports — neither of which was a designed CTCL treatment study — and zero registered clinical trials. This is insufficient to advance beyond a research question stage.

**To proceed, the following is needed:**

- **Regulatory safety data**: Retrieve the full prescribing information (package insert) from the TFDA or CDSCO to complete the S1 safety screening — currently a blocking data gap
- **Systematic literature review**: Conduct a structured PubMed/Embase search specifically for mometasone or class II topical corticosteroids in Mycosis Fungoides/CTCL to capture any evidence missed by the current query
- **MOA gap closure**: Query DrugBank API for complete pharmacology data including binding affinity, selectivity versus other steroid receptors (MR, AR, PR), and any reported GR-mediated apoptosis data in lymphoid cells
- **Benchmark against class I steroids**: Identify published efficacy data for clobetasol in CTCL as a comparator to estimate the potential relative efficacy of mometasone (Class II)
- **Feasibility assessment for investigator-initiated trial**: Given the existing NCCN framework, a small prospective observational study or retrospective chart review at a dermatology-oncology centre may be achievable as a first step before formal trial registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

