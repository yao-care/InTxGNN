---
layout: default
title: Rivaroxaban
parent: 僅模型預測 (L5)
nav_order: 740
evidence_level: L5
indication_count: 4
---

# Rivaroxaban
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Rivaroxaban: From Anticoagulation to Rheumatoid Arthritis

## One-Sentence Summary

Rivaroxaban is a direct Factor Xa inhibitor used for venous thromboembolism treatment/prophylaxis and stroke prevention in atrial fibrillation. TxGNN's top prediction suggests possible efficacy in **rheumatoid arthritis** (score 99.57%), but on review the supporting literature addresses coagulation biomarkers and VTE risk in autoimmune disease — not rivaroxaban treating RA itself — so the signal appears to be a **confounded comorbidity association rather than a genuine repurposing lead**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no India licenses on file; clinically rivaroxaban is a DOAC used for VTE/AF stroke prevention) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on general pharmacological knowledge, rivaroxaban is a direct Factor Xa inhibitor; its efficacy in VTE treatment/prophylaxis and stroke prevention in atrial fibrillation is well established.

The proposed mechanistic link to rheumatoid arthritis — that Factor Xa/thrombin signaling via PAR-1/PAR-2 receptors may contribute to synovial inflammation — is biologically plausible in theory, but **none of the retrieved literature actually tests rivaroxaban as a treatment for RA**. The three supporting papers cover (1) a general VTE diagnosis/treatment review, (2) thrombin generation assays as a research tool in autoimmune disease, and (3) rivaroxaban vs. apixaban adherence in atrial fibrillation — none evaluate anti-inflammatory or disease-modifying effects in RA patients.

The most likely explanation is that TxGNN's high score reflects the well-known **epidemiological association between RA and elevated VTE risk** (RA patients are frequently co-prescribed anticoagulants for comorbid thrombotic disease), rather than a true drug-repurposing signal. This is explicitly flagged in the evidence pack's own rationale as a case where TxGNN's score does not indicate a new therapeutic pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | General review of DVT/PE diagnosis and treatment; does not address RA or anti-inflammatory use of rivaroxaban |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | La Revue de médecine interne | Discusses thrombin generation assay as a tool to assess hypercoagulability in autoimmune disease (e.g., antiphospholipid syndrome); not RA-specific and not a treatment study |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PLoS One | Compares medication adherence between rivaroxaban and apixaban in atrial fibrillation; unrelated to RA |

**Note:** No literature in this evidence pack directly evaluates rivaroxaban as an RA treatment.

---

## India Market Information

Currently no India registration — rivaroxaban is not marketed in the evaluated jurisdiction per this evidence pack (`total_licenses: 0`).

---

## Safety Considerations

- **Drug Interactions**: 313 total interactions identified via DDInter. Notable Major-severity interactions include:
  - Acetylsalicylic acid (Major)
  - Cobicistat (Major)
  - Deferasirox (Major)
  - Ibritumomab tiuxetan (Major)
  - Tositumomab (I-131) (Major)

  Additional Moderate-severity interactions include CYP3A4/P-gp modulators such as clarithromycin, cimetidine, dexamethasone, miconazole, clotrimazole, aprepitant, and rolapitant.

Key warnings and contraindications are not available in this evidence pack — please refer to the official package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Rivaroxaban is not currently marketed in this jurisdiction (0 registrations), and the top-ranked predicted indication (rheumatoid arthritis, L4 evidence) is not supported by any literature actually testing anti-inflammatory or RA-specific efficacy — the retrieved evidence reflects comorbidity/DDI research rather than a therapeutic signal. The remaining three candidates in this evidence pack (gout, HIV infectious disease, brachydactyly-syndactyly syndrome) were independently reviewed and also received **Hold** with L4–L5 evidence; all were flagged as likely confounded associations (DDI/PK studies or coincidental literature co-occurrence) rather than genuine repurposing leads.

**To proceed, the following is needed:**
- Confirmed original MOA and approved indication data (currently marked as data gaps)
- India/local regulatory filing status and package insert (key warnings, contraindications)
- A mechanistic or preclinical study specifically linking Factor Xa inhibition to RA disease activity, if this candidate is to be revisited
- Re-screening of TxGNN outputs to filter out comorbidity-driven false positives before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

