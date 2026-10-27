---
layout: default
title: Bicalutamide
parent: Model Prediction Only (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bicalutamide: predicted new indication Female breast carcinoma (evidence level L5). Approved use: Not listed in the India license data compiled for this report"
monitor_inn: "Bicalutamide"
predicted_indications: ["hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "Ambras type hypertrichosis universalis congenita", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "leprosy", "multiple endocrine neoplasia", "pulmonary hypertension", "female breast carcinoma", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Bicalutamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Bicalutamide: From Prostate Cancer to Female Breast Carcinoma
{: .text-alpha }

## One-Sentence Summary

Bicalutamide is a nonsteroidal androgen receptor antagonist, marketed in India as 50 mg tablets. It is a long-established anti-androgen, but the India license records compiled for this report do not list an approved indication.
The TxGNN model's top-ranked prediction is hypertrichosis, but the best-supported candidate is **female breast carcinoma**, with **1 Phase 2 clinical trial** and **20 publications** pointing in this direction.
The evidence is hypothesis-generating: the clinical data come from a combination regimen, and the one single-arm trial of bicalutamide plus an aromatase inhibitor was terminated after poor results.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the India license data compiled for this report |
| Predicted New Indication | Female breast carcinoma (best-supported candidate; the TxGNN top-ranked prediction is hypertrichosis) |
| TxGNN Prediction Score | 99.11% (female breast carcinoma); 99.69% (hypertrichosis, rank 1) |
| Evidence Level | L2 (female breast carcinoma); L3 (hypertrichosis) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Proceed with Guardrails (female breast carcinoma); hypertrichosis is a research question |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From its known drug class, bicalutamide is a nonsteroidal androgen receptor (AR) antagonist. It is widely used in prostate cancer, but this report could not confirm that from the India license records.

A substantial share of breast cancers express AR. This includes the luminal androgen receptor (LAR) subtype of triple-negative breast cancer (TNBC) and apocrine carcinoma, which is typically ER-negative and AR-positive. Blocking AR in these tumours is a biologically coherent strategy. Preclinical work supports it: bicalutamide with curcumin, inhibition of MDA-MB-231 proliferation and invasion, synergy with an ERK inhibitor, and enhancement of chemotherapy in inflammatory mammary cancer models.

The clinical picture is mixed. A Phase 2 trial combines bicalutamide with nivolumab and ipilimumab, so the effect of bicalutamide alone cannot be isolated. A separate Phase 2 single-arm study of bicalutamide plus an aromatase inhibitor in ER+/AR+, AI-resistant advanced breast cancer showed no synergy (clinical benefit rate 16.7%, objective response rate 0%) and was terminated.

For hypertrichosis (the top TxGNN prediction), AR blockade plausibly reduces androgen-dependent hair growth. The only evidence is a comment on a retrospective study of bicalutamide for minoxidil-induced hypertrichosis in female pattern hair loss, which is not primary evidence.

## Clinical Trial Evidence

Female breast carcinoma:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03650894](https://clinicaltrials.gov/study/NCT03650894) | Phase 2 | Active, not recruiting | 30 | Nivolumab + ipilimumab + bicalutamide in metastatic HER2-negative breast cancer; tests AR blockade with checkpoint therapy while avoiding or delaying chemotherapy. Single-arm combination, so bicalutamide's own contribution is unclear. |

Other predicted indications have only weakly relevant trials. For multiple endocrine neoplasia, the two linked trials are NCT03878524 (Phase 1, terminated, 2 participants) and NCT02615223 (NA, unknown status, 120 participants, prostate cancer endocrine therapy), neither specific to the disease.

## Literature Evidence

Female breast carcinoma (selected from 20 publications):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31434793](https://pubmed.ncbi.nlm.nih.gov/31434793/) | 2020 | Phase 2 single-arm study | The Oncologist | Bicalutamide plus aromatase inhibitor in ER+/AR+ advanced breast cancer showed no synergy; clinical benefit rate 16.7%, objective response rate 0%; study terminated |
| [40853613](https://pubmed.ncbi.nlm.nih.gov/40853613/) | 2025 | Review | Current Medical Science | Anti-androgen therapy in TNBC, including bicalutamide combinations with chemotherapy and immunotherapy |
| [29940524](https://pubmed.ncbi.nlm.nih.gov/29940524/) | 2018 | Review | Cancer Treatment Reviews | AR as a potential target in the LAR subtype of TNBC |
| [35027319](https://pubmed.ncbi.nlm.nih.gov/35027319/) | 2022 | Review | Clinical Breast Cancer | Molecular and clinical features of apocrine carcinoma (ER-negative, AR-positive) |
| [21633166](https://pubmed.ncbi.nlm.nih.gov/21633166/) | 2011 | Preclinical/molecular classification | J Clin Invest | Identified six TNBC subtypes, including LAR, for selecting targeted therapies |
| [40974527](https://pubmed.ncbi.nlm.nih.gov/40974527/) | 2026 | Preclinical | Science China Life Sciences | ERK inhibitor GDC-0994 synergised with bicalutamide, triggering ferroptosis in TNBC |
| [31917699](https://pubmed.ncbi.nlm.nih.gov/31917699/) | 2020 | Preclinical | Anti-Cancer Drugs | Bicalutamide plus curcumin had a strong effect on AR-positive TNBC |
| [32332626](https://pubmed.ncbi.nlm.nih.gov/32332626/) | 2020 | Preclinical (in vitro) | Medicine | Bicalutamide inhibited proliferation and invasion of MDA-MB-231 cells |
| [39063165](https://pubmed.ncbi.nlm.nih.gov/39063165/) | 2024 | Preclinical | Int J Mol Sci | Bicalutamide enhanced doxorubicin and docetaxel in inflammatory mammary cancer models |
| [24740738](https://pubmed.ncbi.nlm.nih.gov/24740738/) | 2014 | Review | J Mol Endocrinol | Reviews the role of AR in breast cancer, including its inhibitory role in ER-positive disease |

Hypertrichosis: [35304167](https://pubmed.ncbi.nlm.nih.gov/35304167/) (2022, J Am Acad Dermatol) is a comment on a retrospective review of 35 patients using bicalutamide for minoxidil-induced hypertrichosis in female pattern hair loss.

## India Market Information

All 20 licenses are valid single-ingredient products; the license data compiled for this report list no approved indication text. Five main licenses:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 29956 | Bicalon 50mg Tablet (Celon Laboratories) | Strip of 10 tablets | Not listed |
| 217737 | Tabi Tablet (Dr Reddy's Laboratories) | Strip of 10 tablets | Not listed |
| 37476 | Caluran 50 Tablet (Sun Pharmaceutical) | Strip of 10 tablets | Not listed |
| 34195 | Calutide 50 Tablet (Cipla) | Strip of 10 tablets | Not listed |
| 34259 | Caluran 50 CP Tablet (Sun Pharmaceutical) | Bottle of 30 tablets | Not listed |

## Cytotoxicity

Bicalutamide is a hormonal (anti-androgen) therapy rather than a conventional cytotoxic agent, and no cytotoxicity data were compiled for this report. Please refer to the package insert warnings and precautions.

## Safety Considerations

- **Disease associations flagged by the knowledge graph** (derived from drug-disease contraindication edges in the TxGNN knowledge graph, not from label text): liver disease, gallbladder disease, drug-induced liver injury, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, anaemia (including macrocytic anaemia), and interstitial lung disease.
- **Drug interactions:** 389 interactions are recorded. The two classed as Major in the sample reviewed are **cisapride** and **dolasetron**. Moderate interactions include famotidine, loperamide, aprepitant, clarithromycin, levofloxacin, granisetron, eliglustat, budesonide and several laxatives (bisacodyl, lactulose, lactitol, magnesium citrate, magnesium hydroxide, glycerin, mineral oil, castor oil). Metronidazole is Minor.

Package insert warnings and contraindications were not available; please refer to the package insert.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (female breast carcinoma). Hypertrichosis remains a research question; the other predicted indications should be held.

**Rationale:**
Female breast carcinoma has the strongest support among the predictions: a Phase 2 trial of bicalutamide in combination, consistent preclinical data, and a clear biological rationale in AR-positive subtypes. Against this, the trial cannot isolate bicalutamide's effect, and a Phase 2 bicalutamide plus aromatase inhibitor study was terminated with no objective responses. The remaining predictions (for example leprosy, Dandy-Walker syndrome, nephrogenic syndrome of inappropriate antidiuresis) have no trials or literature and no plausible mechanism.

**To proceed, the following is needed:**
- Restrict to AR-positive subtypes (LAR TNBC, apocrine carcinoma) with biomarker selection
- Randomised data, or at least bicalutamide-containing arms that can be compared, before treating results as more than hypothesis-generating
- Package insert warnings and contraindications from the India license holder, which are currently missing and block safety screening
- Detailed mechanism of action data and the approved indication text for the India licenses
- For hypertrichosis, retrieval and appraisal of the primary retrospective study of 35 patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

