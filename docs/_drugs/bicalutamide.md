---
layout: default
title: Bicalutamide
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
---

# Bicalutamide
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

# Bicalutamide: From Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Bicalutamide is a non-steroidal androgen receptor (AR) antagonist, clinically established as hormonal therapy for prostate cancer.
The TxGNN model's top-ranked prediction suggests it may be effective for **Hypertrichosis**, but this is currently supported only by **0 clinical trials** and **1 letter/comment** in the literature — evidence level L4.
Notably, among all 10 predicted indications reviewed, **Female Breast Carcinoma (Rank 9, Evidence Level L2)** represents the most clinically promising repurposing candidate, with 1 active Phase 2 trial and 20 publications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer (androgen receptor antagonist; not registered in India) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bicalutamide is a well-characterized non-steroidal antiandrogen. It competitively blocks the androgen receptor (AR), preventing testosterone and dihydrotestosterone from binding and activating AR-dependent gene transcription. It is primarily used for prostate cancer — where AR signaling is the dominant oncogenic driver — and is also employed clinically for androgen-dependent conditions such as hirsutism (androgen-driven excessive hair growth in women). Formal MOA data was not retrieved from the database in this report run; the description above is based on established pharmacological knowledge.

The connection between bicalutamide and **hypertrichosis** is indirect. Androgenic hormones stimulate hair follicle growth in androgen-sensitive regions, so AR blockade can reduce androgen-driven hair excess — this is the rationale for bicalutamide's use in hirsutism. However, **hypertrichosis** is defined specifically as hair overgrowth occurring **independent of androgen stimulation**, arising instead from genetic mutations, systemic medications (such as minoxidil), or metabolic disorders. Its pathophysiology is fundamentally distinct from hirsutism, and AR signaling plays no established primary role.

The single piece of literature identified is a published letter commenting on the use of bicalutamide to manage **minoxidil-induced hypertrichosis** — a drug side effect — rather than a study treating hypertrichosis as a primary disease. This is an indirect, highly context-specific observation, not evidence for a standalone indication. The mechanistic link between bicalutamide's AR antagonism and the broader category of "hypertrichosis" remains weak and unsupported by direct research.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35304167](https://pubmed.ncbi.nlm.nih.gov/35304167/) | 2022 | Letter/Comment | Journal of the American Academy of Dermatology | A commentary addressing the management of minoxidil-induced hypertrichosis in female pattern hair loss; bicalutamide is discussed as a management tool for a drug side effect, not as a primary treatment for hypertrichosis as a disease entity |

---

## India Market Information

Bicalutamide is currently not registered or marketed in India. There are no approved product licenses on record.

---

## Cytotoxicity

Bicalutamide is used as an anticancer hormonal therapy (prostate cancer) and warrants cytotoxicity documentation.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Non-steroidal Androgen Receptor Antagonist (antiandrogen class) |
| Myelosuppression Risk | Low (bicalutamide does not cause significant bone marrow suppression) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (LFTs) periodically due to hepatotoxicity risk; PSA and testosterone levels for oncology use; baseline CBC |
| Handling Protection | Standard oral medication handling; institutional cytotoxic precautions may apply per local policy |

---

## Safety Considerations

**Drug Interactions**: Bicalutamide has **389 documented drug interactions** (DDInter database). Clinically significant examples include:

- **Major interactions**: Cisapride (QT prolongation / cardiac arrhythmia risk), Dolasetron (QT prolongation risk)
- **Moderate interactions** (selected): Clarithromycin, Levofloxacin, Granisetron, Aprepitant, Budesonide (including nasal formulation), Famotidine, Eliglustat, Loperamide, Glycerin, as well as multiple laxatives/bowel agents (Lactulose, Lactitol, Bisacodyl, Magnesium citrate, Magnesium hydroxide, Castor oil, Mineral oil)
- **Minor interactions**: Metronidazole

Please refer to the package insert for complete warnings and contraindications. Specific label safety data was not available in this Evidence Pack and should be obtained by parsing the drug label PDF.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN rank-1 prediction (hypertrichosis) lacks both mechanistic plausibility and direct clinical evidence — hypertrichosis is non-androgen-dependent, and the sole literature reference is an indirect letter/comment on a drug side effect. The evidence does not justify proceeding with this indication.

---

**A more actionable finding from this analysis:**

Among the 10 predicted indications evaluated, **Female Breast Carcinoma (Rank 9, Evidence Level L2)** is the most evidence-grounded and mechanistically sound repurposing candidate and warrants a dedicated evaluation report:

| Item | Detail |
|------|--------|
| Mechanism | AR is expressed in 70–90% of luminal breast cancers and ~10–15% of triple-negative breast cancers (LAR subtype); bicalutamide's AR antagonism can suppress AR-driven tumor proliferation and Wnt/β-catenin signaling |
| Clinical Evidence | 1 active Phase 2 trial ([NCT03650894](https://clinicaltrials.gov/study/NCT03650894): bicalutamide + nivolumab + ipilimumab in HER2-negative metastatic breast cancer, n=30); 20 supporting publications including in vitro, in vivo, and review studies |
| Biomarker Requirement | AR immunohistochemistry positivity (≥10% nuclear staining recommended for patient selection) |
| Recommendation | **Proceed with Guardrails** |

**To proceed with the Female Breast Carcinoma indication, the following is needed:**

- Formal MOA data retrieved from DrugBank API (currently a data gap — DG002)
- Complete safety profile from the drug label PDF (DG001 — blocking item for S1 safety screening)
- Results from NCT03650894 when available (trial currently active, not recruiting)
- AR+ patient biomarker selection strategy and IHC cutoff specification
- India regulatory pathway assessment for an AR+ breast cancer indication
- Pharmacoeconomic feasibility analysis for India market entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

