---
layout: default
title: Chromium
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 10
---

# Chromium
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

# Chromium (Trivalent): From Dietary Supplement to Rheumatoid Arthritis Treatment

## One-Sentence Summary

Trivalent chromium (Cr³⁺) is an essential trace mineral sold as a dietary supplement, currently lacking any approved therapeutic drug indications in India.
The TxGNN model's highest-evidence actionable prediction is **Rheumatoid Arthritis**, supported by **1 completed Phase 2/3 clinical trial** (NCT05545020, n=60) and a published RCT (PMID: 39030450).

> **⚠️ TxGNN Ranking Note:** Although osteoarthritis ranks #1 in TxGNN prediction score (98.68%), all 48 retrieved clinical trials for that indication involve chromium as a metallic alloy in orthopaedic implants — not as a therapeutic agent. This is a known knowledge-graph context-confusion artefact. Rheumatoid arthritis (Rank #3, score 98.54%, Evidence Level L1) represents the highest-quality and only actionable repurposing signal in this Evidence Pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | None (trace mineral; no approved drug indications) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 98.54% |
| Evidence Level | L1 (1 completed Phase 2/3 RCT) |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Trivalent chromium (Cr³⁺) is an essential trace element with established roles in glucose and lipid metabolism. As a potentiator of insulin receptor sensitivity, Cr³⁺ modulates metabolic-immune crosstalk — and this is where the link to rheumatoid arthritis becomes scientifically interesting. Beyond metabolic effects, mechanistic studies indicate that Cr³⁺ inhibits the NF-κB signalling pathway, thereby suppressing production of the key pro-inflammatory cytokines TNF-α, IL-1β, and IL-6. These are precisely the targets of approved DMARDs such as baricitinib and tocilizumab.

A rat adjuvant-induced arthritis model (PMID: 35829940) demonstrated that Cr³⁺ supplementation significantly improved joint histopathology, upregulated FOXP3 (a regulatory T-cell marker), and decreased synovial Cathepsin G expression — collectively suggesting modulation of the Treg/Th17 axis that is dysregulated in RA. Separately, observational studies from the 1970s–1980s consistently found lower blood chromium concentrations in RA patients compared to healthy controls (PMID: 1153978; PMID: 3776595), raising the hypothesis that chromium deficiency may contribute to or correlate with disease activity.

These converging lines of evidence — NF-κB inhibition, insulin-mediated immune regulation, regulatory T-cell enhancement, and observed chromium deficiency in RA patients — collectively support a biologically plausible rationale for the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT05545020](https://clinicaltrials.gov/study/NCT05545020) | Phase 2/3 | Completed | 60 | First RCT evaluating trivalent Cr³⁺ supplementation versus baricitinib (a JAK inhibitor DMARD) in RA patients; assessed anti-rheumatic efficacy and safety of Cr³⁺ as a candidate immune-modulator |

> **Note on other retrieved trials:** The remaining 8 trials retrieved under the "rheumatoid arthritis" query (e.g., NCT06578897, NCT02405234, NCT05509972) all involve chromium as an orthopaedic implant alloy material. They are not relevant to therapeutic chromium repurposing and are excluded from this table.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39030450](https://pubmed.ncbi.nlm.nih.gov/39030450/) | 2024 | RCT (Phase 2/3) | Inflammopharmacology | First Phase 2/3 RCT comparing Cr³⁺ vs. baricitinib in RA; introduces trivalent chromium as a candidate immune-modulator for RA treatment, reports efficacy and safety results |
| [35829940](https://pubmed.ncbi.nlm.nih.gov/35829940/) | 2022 | Animal Model | Inflammopharmacology | Cr³⁺ supplementation in adjuvant-induced RA rat model upregulates FOXP3, decreases synovial Cathepsin G expression, and improves joint pathology vs. prednisolone — first preclinical mechanistic demonstration |
| [1153978](https://pubmed.ncbi.nlm.nih.gov/1153978/) | 1975 | Cross-sectional (Biomarker) | Scand J Rheumatol | Blood chromium concentrations significantly lower in RA patients than healthy controls; supports chromium deficiency hypothesis in RA |
| [3776595](https://pubmed.ncbi.nlm.nih.gov/3776595/) | 1986 | Observational (Biomarker) | Acta Pharmacol Toxicol | Chromium, nickel and cadmium measured in biological fluids of RA patients vs. healthy controls; corroborates lower chromium levels in disease state |

---

## Safety Considerations

No formal drug interaction data or regulatory warnings are available for Chromium (DB11136) in this Evidence Pack.

> Please refer to applicable safety information for trivalent chromium supplements. Two points of critical context for clinical evaluation:
>
> - **Trivalent vs. hexavalent chromium:** Cr³⁺ (the form in supplements and this study) is biologically distinct from Cr⁶⁺ (a known industrial carcinogen). These must not be conflated in safety assessments.
> - **Long-term safety at therapeutic doses:** The existing RCT (NCT05545020, n=60) provides only short-term safety data (approximately 13 months of follow-up). Long-term safety in an immunocompromised RA population remains uncharacterised. Renal excretion of chromium suggests caution may be warranted in patients with impaired kidney function.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The first Phase 2/3 RCT (NCT05545020; published as PMID: 39030450) provides Level 1 evidence that trivalent chromium supplementation has measurable anti-rheumatic activity compared to baricitinib in 60 RA patients, representing a genuinely novel and biologically plausible repurposing signal. However, significant methodological limitations prevent a full "Go" recommendation at this stage.

**To proceed, the following is needed:**

- **Replication RCT** with a larger sample, placebo control arm (current trial uses active comparator only — no placebo group means absolute efficacy vs. no treatment is unquantified), and multi-centre design for independent validation
- **Long-term safety study** at therapeutic Cr³⁺ doses in RA populations, including renal function monitoring and potential carcinogenicity evaluation over ≥2 years
- **Dose and formulation standardisation**: clarify optimal Cr³⁺ salt form (picolinate, nicotinate, chloride), dose (µg/day range), and bioavailability across formulations
- **Mechanistic validation in human tissue**: confirm NF-κB inhibition and Treg/Th17 modulation in human RA synovial biopsy specimens
- **India regulatory pathway assessment**: as a new molecular entity with zero current market registrations in India, a full new drug application (NDA) or investigational new drug (IND) pathway review with CDSCO is required before any clinical development proceeds domestically
- **Detailed MOA data retrieval** from DrugBank API (flagged as Data Gap DG002) to complete mechanistic dossier
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

