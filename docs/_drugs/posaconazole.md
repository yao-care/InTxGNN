---
layout: default
title: Posaconazole
parent: 僅模型預測 (L5)
nav_order: 680
evidence_level: L5
indication_count: 1
---

# Posaconazole
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

# Posaconazole: From Invasive Fungal Infection Prophylaxis to Pneumocystosis

## One-Sentence Summary

Posaconazole is a triazole antifungal used mainly for antifungal prophylaxis (e.g., against *Aspergillus*) in transplant and hematologic malignancy patients. The TxGNN model predicts it may be effective for **Pneumocystosis (PCP)**, but this is currently supported only by **2 clinical trials** (both low-relevance, indirect matches) and **5 publications** (mostly reviews/guidelines, none an RCT of posaconazole for PCP).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Invasive fungal infection prophylaxis (e.g., *Aspergillus*) in transplant/hematologic malignancy patients — not formally documented in this dataset |
| Predicted New Indication | Pneumocystosis (Pneumocystis jirovecii pneumonia) |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for posaconazole is not available in this dataset. Based on general drug class knowledge, posaconazole is a triazole antifungal that inhibits fungal CYP51 (lanosterol 14α-demethylase), blocking ergosterol synthesis in the fungal cell membrane.

However, this mechanistic link to pneumocystosis is weak. *Pneumocystis jirovecii* is an atypical fungus whose cell membrane relies primarily on host-derived cholesterol rather than fungal ergosterol, so azole activity against it has historically been considered limited and inconsistent. Standard PCP treatment and prophylaxis today remains TMP-SMX; posaconazole's established clinical role is antifungal prophylaxis against molds such as *Aspergillus* in transplant/hematologic malignancy patients, not direct treatment of *Pneumocystis*.

Given this, the mechanistic connection is indirect inference rather than direct evidence — consistent with the model's L4 evidence classification and the "Hold" recommendation below.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Active, not recruiting | 602 | Evaluates IV rezafungin (an echinocandin, not posaconazole) vs. standard antimicrobial regimen to prevent invasive fungal disease in allogeneic transplant recipients; rezafungin itself has no activity against *Pneumocystis* — matched by keyword only, not a direct posaconazole/PCP trial |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform trial comparing post-transplant cyclophosphamide-based GVHD prophylaxis regimens after mismatched unrelated donor stem cell transplant; population overlaps with immunocompromised patients at PCP risk, but posaconazole/PCP is not a primary study endpoint |

Both trials were graded **C (low relevance)** — neither directly tests posaconazole for pneumocystosis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2025 | Review/Guideline | The Lancet. Infectious Diseases | UK best-practice update on diagnosing serious fungal diseases, including Pneumocystis, via non-culture-based tests |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Guideline | Chinese Journal of Tuberculosis and Respiratory Diseases | 2025 clinical practice guideline for diagnosis/management of invasive pulmonary fungal disease |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Medical Weekly | Overview of invasive candidiasis, aspergillosis, cryptococcosis and PCP; notes posaconazole's established role is mold-active prophylaxis (reducing invasive candidiasis/aspergillosis), not primary PCP treatment |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transplant Infectious Disease | Retrospective review of infectious complications, including fungal infections, in liver transplant patients with acute GVHD |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review (PK/PD) | Clinical Pharmacokinetics | Reviews pulmonary epithelial lining fluid penetration of antifungal agents, relevant to posaconazole PK in lung tissue |

No publication directly reports clinical outcomes of posaconazole used to treat or prevent pneumocystosis.

## India Market Information

Posaconazole currently has no marketing authorization in this dataset (0 registrations, market status: not marketed). No product/license information is available.

## Safety Considerations

- **Drug Interactions**: 269 total interactions identified (source: DDInter). Notable **Major**-level interactions include Loperamide, Triamcinolone, and Budesonide. Additional **Moderate**-level interactions include Famotidine, Ranitidine, Rabeprazole, Hydrocortisone, Aprepitant, Omeprazole, Dexamethasone, Betamethasone, Bisacodyl, Cimetidine, Clarithromycin, Picosulfuric acid, Polyethylene glycol (with electrolytes), and Saxagliptin.

Package insert warnings and contraindications are not available in this dataset and must be sourced separately before any safety review.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted association rests on indirect mechanistic inference rather than direct clinical evidence — the two matched trials are low-relevance keyword matches, and the literature covers general antifungal diagnostics/prophylaxis rather than posaconazole treating pneumocystosis specifically. Combined with an unresolved blocking data gap on package insert warnings/contraindications, this candidate is not ready to advance past S0.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap — required for initial safety screening, S1)
- Confirmed mechanism-of-action data from DrugBank
- Direct clinical or preclinical evidence evaluating posaconazole specifically against *Pneumocystis jirovecii*, given its low ergosterol-dependent membrane biology
- Confirmed original approved indication(s) and formulation/route data for comparison with pneumocystosis treatment requirements
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

