---
layout: default
title: Durvalumab
parent: 僅模型預測 (L5)
nav_order: 216
evidence_level: L5
indication_count: 10
---

# Durvalumab
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

# Durvalumab: From Urothelial Carcinoma to Rare Genitourinary Cancer Subtypes

## One-Sentence Summary

Durvalumab (Imfinzi) is an anti-PD-L1 monoclonal antibody immunotherapy that has been clinically investigated in urothelial carcinoma, including a large-scale Phase 3 DANUBE trial (n=1,032), and is approved in several markets for lung cancer and biliary tract cancer.
The TxGNN model predicts it may be effective across **10 rare genitourinary and gynecologic cancer subtypes**, with the top prediction being **Prostatic Urethra Urothelial Carcinoma** (score: 99.98%).
Across all predictions, the best-supported indications are **Infiltrating Bladder Urothelial Carcinoma Sarcomatoid Variant** (Rank 3, L3 evidence, 2 trials) and **Endocervical Carcinoma** (Rank 6, L3 evidence, 2 trials + 1 publication), while the majority of rare subtypes remain at model-prediction level only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Urothelial carcinoma (DANUBE Phase 3 reference); NSCLC, SCLC, biliary tract cancer in other markets |
| Predicted New Indication (Top) | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 (top prediction); L3 for best-evidenced indication (Rank 3 & 6) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question (Rank 1) / Proceed with Guardrails (Ranks 3 & 6) / Hold (Ranks 5, 7–10) |

---

## All Predicted Indications — Summary

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|----------------|----------------|
| 1 | Prostatic Urethra Urothelial Carcinoma | 99.98% | L4 | Research Question |
| 2 | Kidney Pelvis Sarcomatoid Transitional Cell Carcinoma | 99.98% | L4 | Research Question |
| 3 | Infiltrating Bladder Urothelial Carcinoma Sarcomatoid Variant | 99.98% | L3 | Proceed with Guardrails |
| 4 | Renal Pelvis Papillary Urothelial Carcinoma | 99.98% | L4 | Research Question |
| 5 | Uterine Ligament Adenocarcinoma | 99.92% | L5 | Hold |
| 6 | Endocervical Carcinoma | 99.91% | L3 | Proceed with Guardrails |
| 7 | Adenoid Cystic Carcinoma of the Cervix Uteri | 99.91% | L5 | Hold |
| 8 | Uterine Ligament Serous Adenocarcinoma | 99.91% | L5 | Hold |
| 9 | Signet Ring Cell Variant Cervical Mucinous Adenocarcinoma | 99.90% | L5 | Hold |
| 10 | Intestinal Variant Cervical Mucinous Adenocarcinoma | 99.90% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established scientific literature, Durvalumab is an anti-PD-L1 (Programmed Death-Ligand 1) human IgG1κ monoclonal antibody. It selectively blocks the binding of PD-L1 to the PD-1 and CD80 (B7-1) receptors on T cells, thereby removing the "brakes" on anti-tumor immunity and allowing cytotoxic T lymphocytes to re-engage tumor cells. This class-wide mechanism explains why TxGNN generates high-confidence predictions across many PD-L1-expressing tumor types.

For the top four predictions (Ranks 1–4), all are urothelial carcinoma subtypes — sharing the same molecular landscape (high TMB, FGFR3 mutations, PD-L1 expression in 20–40% of cases) as the broader urothelial carcinoma cohort studied in DANUBE. The sarcomatoid variants (Ranks 2 and 3) are especially compelling: sarcomatoid differentiation involves epithelial-mesenchymal transition (EMT), a process that actively upregulates PD-L1 expression and enriches for tumor-infiltrating lymphocytes, theoretically conferring greater sensitivity to PD-L1 blockade than conventional urothelial histology.

For the gynecologic predictions (Ranks 5–10), the mechanistic basis is more variable. Endocervical carcinoma (Rank 6) benefits from HPV-driven immunogenicity — viral neoantigens stimulate TIL infiltration and PD-L1 upregulation, a profile historically associated with improved checkpoint inhibitor response, particularly in MSI-H/dMMR tumors. In contrast, adenoid cystic carcinoma (Rank 7) and uterine ligament variants (Ranks 5 and 8) are classified as "immune cold" tumors with low PD-L1 expression and sparse TIL infiltration, making the mechanistic rationale for immunotherapy substantially weaker.

---

## Clinical Trial Evidence

### Infiltrating Bladder Urothelial Carcinoma Sarcomatoid Variant (Rank 3 — Best Evidence in Urothelial Group)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03912818](https://clinicaltrials.gov/study/NCT03912818) | Phase 2 | Terminated | 7 | Durvalumab + neoadjuvant chemotherapy (MVAC/GC) specifically in variant histology bladder cancer including sarcomatoid subtype. Only 7 patients enrolled before early termination — severely underpowered. Provides initial feasibility signal but conclusions are unreliable. |
| [NCT02812420](https://clinicaltrials.gov/study/NCT02812420) | Early Phase 1 | Active, Not Recruiting | 54 | Durvalumab + Tremelimumab (anti-CTLA-4) pre-surgical study in muscle-invasive, high-risk urothelial carcinoma ineligible for cisplatin-based neoadjuvant chemotherapy. Provides safety framework for dual immune checkpoint blockade in the urothelial setting. |

### Kidney Pelvis Sarcomatoid Transitional Cell Carcinoma (Rank 2 — Indirect Evidence Only)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02812420](https://clinicaltrials.gov/study/NCT02812420) | Early Phase 1 | Active, Not Recruiting | 54 | Broad urothelial/transitional cell carcinoma pre-surgical study; inclusion of renal pelvis subtype not confirmed. Provides indirect mechanistic and safety support only. |

### Endocervical Carcinoma (Rank 6 — Best Evidence in Gynecologic Group)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Phase 1 | Completed | 20 | Hypofractionated (SBRT) radiotherapy + Tremelimumab + Durvalumab in recurrent/metastatic cervical, vaginal, or vulvar cancers. Completed trial: provides definitive safety, dosing, and tolerability data. Exploits synergy between radiation-induced PD-L1 upregulation and dual checkpoint blockade. |
| [NCT04065269](https://clinicaltrials.gov/study/NCT04065269) | Phase 2 | Active, Not Recruiting | 174 | ATARI trial: ATR inhibitor ceralasertib (AZD6738) ± olaparib or ± Durvalumab in relapsed gynecologic cancers stratified by ARID1A mutation status. Large Phase 2 (n=174, enrollment complete); results anticipated 2026. This trial could upgrade evidence to L2 upon readout. |

> **Ranks 1, 4, 5, 7, 8, 9, 10:** No registered clinical trials found.

---

## Literature Evidence

### Endocervical Carcinoma (Rank 6)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Narrative Review | Biomedical Journal | Review of small cell neuroendocrine carcinoma of the cervix, discussing HPV association, molecular basis, and emerging therapeutic approaches including immunotherapy. Provides contextual understanding of immunotherapy rationale in rare, aggressive cervical malignancies. |

> **All other predicted indications (Ranks 1–5, 7–10):** No related literature currently available.

---

## India Market Information

Durvalumab currently has **no registered products** in India. The drug is not marketed in the Indian market as of April 4, 2026. No authorization numbers, product names, or approved indications are available.

For regulatory reference: Durvalumab (Imfinzi) holds approvals in the US (FDA), EU (EMA), and Japan (PMDA) for NSCLC, extensive-stage SCLC, and biliary tract cancer. An application for Indian market entry has not been recorded in this dataset.

---

## Cytotoxicity

Durvalumab is an antineoplastic agent (immunotherapy class). The following applies:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — Anti-PD-L1 monoclonal antibody (not conventional cytotoxic) |
| Myelosuppression Risk | Low (not myelosuppressive by mechanism; lymphocyte subset changes may occur; immune-mediated cytopenias are rare irAEs) |
| Emetogenicity Classification | Minimal (biological agent; not emetogenic by chemical mechanism) |
| Monitoring Items | Liver function tests (ALT/AST/bilirubin), thyroid function (TSH/fT4), CBC with differential, renal function (creatinine), cortisol/ACTH (adrenal insufficiency risk), blood glucose; clinical vigilance for immune-related adverse events (irAEs) across all organ systems |
| Handling Protection | Standard aseptic technique for IV biologics; no dedicated cytotoxic drug handling precautions required per NIOSH classification — verify per institutional pharmacy policy |

---

## Safety Considerations

**Drug Interactions (81 total interactions recorded):**

| Severity | Interacting Drug(s) | Clinical Implication |
|---------|---------------------|---------------------|
| **Major** | Adalimumab | Combining two immunomodulatory biologics creates risk of unpredictable immune dysregulation; concurrent use generally contraindicated |
| **Moderate** | Corticosteroids (Hydrocortisone, Dexamethasone, Prednisolone, Methylprednisolone, Betamethasone, Budesonide, Triamcinolone, Deflazacort, Prednisone) | Systemic corticosteroids may attenuate Durvalumab's anti-tumor immune activity; however, they are also first-line treatment for irAEs — manage with dose-timing strategy |
| **Moderate** | Alefacept, Alemtuzumab, Anakinra | Additive immunosuppression risk; avoid concomitant use |
| **Moderate** | Roflumilast | PDE4 inhibitor with immunomodulatory activity; interaction mechanism warrants monitoring |
| **Moderate** | Anthrax vaccine, Clostridium tetani toxoid | Immunotherapy may reduce vaccine immunogenicity; complete vaccinations before starting Durvalumab where possible |
| **Minor** | Zinc supplements (acetate, gluconate, sulfate, chloride) | Low clinical significance; routine monitoring sufficient |

Full warnings and contraindications (including immune-related adverse events: pneumonitis, hepatitis, colitis, endocrinopathies, nephritis, dermatitis) should be obtained directly from the prescribing information/package insert, which was not available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Research Question (Ranks 1, 2, 4) / Proceed with Guardrails (Ranks 3 & 6) / Hold (Ranks 5, 7–10)**

**Rationale:**
Ranks 3 and 6 have sufficient Level 3 evidence — including at least one completed or near-completion clinical trial directly involving Durvalumab in the relevant tumor category — to justify moving forward with defined protocol guardrails; meanwhile, the top TxGNN prediction (prostatic urethra urothelial carcinoma) and three urothelial subtypes (Ranks 1, 2, 4) remain at L4 and require prospective study design before investment; the five gynecologic rare subtypes (Ranks 5, 7–10) lack both clinical and mechanistic support and should be placed on hold pending basic biomarker characterization.

**To proceed, the following is needed:**

- **Blocking — Resolve DG001:** Download and parse Durvalumab's package insert from the CDSCO/FDA/EMA to obtain full warnings and contraindications before initiating any safety evaluation (S1 gate)
- **High Priority — Resolve DG002:** Query DrugBank API for confirmed mechanism of action data to complete mechanistic link analysis
- **For Rank 3 (Bladder Sarcomatoid):** Investigate the reason for NCT03912818 early termination; assess feasibility of designing a new basket trial encompassing sarcomatoid urothelial variants across anatomical sites
- **For Rank 6 (Endocervical):** Monitor NCT04065269 (ATARI trial) results expected by August 2026; a positive readout could elevate evidence to L2
- **Biomarker Screening Plan:** Establish PD-L1 expression (CPS/TPS), MSI/MMR status, TMB, and ARID1A mutation testing protocols for patient selection across all actionable indications
- **India Regulatory Pathway:** Assess the timeline and requirements for filing a new drug application (NDA) for Durvalumab with CDSCO, given zero current market presence in India
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

