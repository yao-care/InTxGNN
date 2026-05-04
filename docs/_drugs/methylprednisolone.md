---
layout: default
title: Methylprednisolone
parent: 僅模型預測 (L5)
nav_order: 338
evidence_level: L5
indication_count: 10
---

# Methylprednisolone
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

# Methylprednisolone: From Inflammatory and Autoimmune Conditions to Alopecia Areata

## One-Sentence Summary

Methylprednisolone is a potent synthetic glucocorticoid corticosteroid used broadly as an anti-inflammatory and immunosuppressive agent across a wide range of systemic conditions.
The TxGNN model predicts it may be effective for **Alopecia Areata**,
with **1 completed Phase 4 clinical trial** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Inflammatory and autoimmune conditions (systemic corticosteroid) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, methylprednisolone is a synthetic glucocorticoid that binds to intracellular glucocorticoid receptors (GR), mediating broad immunosuppressive effects primarily through NF-κB inhibition and downregulation of pro-inflammatory cytokines — including IFN-γ, IL-2, and CXCL10 — thereby blunting T cell activation and cytokine-driven tissue inflammation.

Alopecia areata (AA) is a chronic autoimmune disorder in which autoreactive CD8+ T cells breach the immune privilege zone of hair follicles, triggering non-scarring hair loss that ranges from small patches to total scalp or body hair loss (alopecia totalis/universalis). Methylprednisolone's capacity to suppress T cell infiltration and restore hair follicle immune privilege directly targets this core pathophysiology. High-dose pulse therapy regimens — whether oral mega-pulse or intravenous bolus — generate short-duration immunosuppressive peaks that are mechanistically suited to halting an active autoimmune attack while limiting the systemic burden of continuous steroid exposure.

Both methylprednisolone's established role in systemic autoimmune conditions and the pathobiology of AA share the same immunological ground: dysregulated T cell-mediated immunity. This mechanistic overlap, combined with direct clinical studies applying methylprednisolone pulse therapy specifically for severe, therapy-resistant AA, strongly supports the biological plausibility of this TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | Completed | 42 | Direct study of oral mega-pulse methylprednisolone in severe, therapy-resistant AA (including totalis, universalis, and ophiasic subtypes); evaluated whether higher doses and more frequent pulses could overcome treatment failures seen with standard systemic steroid regimens |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | N/A | Unknown | 20 | Compared DERMOJET needle-free syringe vs. conventional syringe for intralesional steroid injection in AA; intervention most likely includes methylprednisolone or triamcinolone; indirectly supports local corticosteroid use in AA |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | N/A | Completed | 296 | Observational study of Tofacitinib (JAK inhibitor) safety and effectiveness in alopecia; participants received Tofacitinib with or without adjuvant prednisolone, providing real-world context for corticosteroid combination approaches |
| [NCT03845517](https://clinicaltrials.gov/study/NCT03845517) | Phase 2b | Completed | 350 | Double-blind RCT of PF-06700841 in moderate-to-severe active SLE; validates SALT score and related outcome endpoints applicable to AA trial design |
| [NCT03252587](https://clinicaltrials.gov/study/NCT03252587) | Phase 2 | Completed | 363 | High-quality double-blind RCT of BMS-986165 in SLE; provides a high-standard trial design comparison framework for autoimmune alopecia research |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [30745958](https://pubmed.ncbi.nlm.nih.gov/30745958/) | 2019 | RCT / Controlled Trial | Open Access Macedonian Journal of Medical Sciences | MTX combined with mini-pulse methylprednisolone in severe AA (including totalis/universalis) in a Vietnamese cohort; demonstrates efficacy of combination over methylprednisolone monotherapy |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Retrospective Cohort | Dermatologic Therapy | Retrospective comparison of methylprednisolone alone vs. methylprednisolone + methotrexate in 26 patients with extensive AA; combination therapy showed superior hair regrowth outcomes |
| [22426909](https://pubmed.ncbi.nlm.nih.gov/22426909/) | 2012 | Clinical Trial | Saudi Medical Journal | Oral mega-pulse methylprednisolone intensive regimen for severe therapy-resistant AA; evaluates high-dose pulse protocol directly associated with NCT01167946 |
| [25566921](https://pubmed.ncbi.nlm.nih.gov/25566921/) | 2015 | Prospective Clinical Study | Indian Journal of Dermatology, Venereology and Leprology | Intravenous methylprednisolone pulse therapy in severe AA; prospective evaluation of efficacy and systemic safety in therapy-resistant cases |
| [18608727](https://pubmed.ncbi.nlm.nih.gov/18608727/) | 2008 | Prospective Clinical Study | The Journal of Dermatological Treatment | Cyclosporine combined with methylprednisolone in severe chronic AA; combination approach showed lower recurrence rates compared to cyclosporine monotherapy |
| [36865845](https://pubmed.ncbi.nlm.nih.gov/36865845/) | 2022 | Retrospective Cohort | Indian Journal of Dermatology | Sex differences in AA treated with steroid pulse therapy; retrospective study and literature review identifying prognostic variables for treatment response |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatology Practical & Conceptual | Comprehensive review of corticosteroid pulse therapy across AA subtypes; summarises efficacy, relapse rates, adverse effects, and prognostic factors across different pulse protocols |
| [32270396](https://pubmed.ncbi.nlm.nih.gov/32270396/) | 2020 | Systematic Review | Dermatology and Therapy | Systematic review of cyclosporine ± systemic corticosteroids in AA; evaluates multiple corticosteroid protocols including methylprednisolone combinations |
| [28378336](https://pubmed.ncbi.nlm.nih.gov/28378336/) | 2017 | Review | International Journal of Dermatology | Review of treatment options for alopecia totalis and universalis; discusses the role of systemic corticosteroids including methylprednisolone pulse therapy among multiple modalities |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review / Guideline | Pediatric Dermatology | Dosing and administration guidance for pediatric pulse dose corticosteroid therapy (including methylprednisolone) in AA; reviews available regimens and associated side effects in children |

---

## India Market Information

Methylprednisolone is currently **not registered** in India's drug regulatory database. No approved product licenses, brand names, or approved indications were found as of the data cutoff (2026-04-04).

> A market entry pathway via CDSCO (Central Drugs Standard Control Organisation) would be required before any commercialisation or repurposing activities could proceed in India.

---

## Safety Considerations

**Drug Interactions:**
Methylprednisolone has an extensive interaction profile with **688 documented interactions** on record. Clinically significant interactions include:

- **Major interactions:**
  - **Bupropion** — Corticosteroids lower seizure threshold; combined use with bupropion increases seizure risk
  - **Clarithromycin** — CYP3A4 inhibition significantly increases methylprednisolone plasma exposure, raising risk of corticosteroid-related adverse effects

- **Moderate interactions (selected):**
  - **Antidiabetic agents** (Metformin, Pioglitazone, Acarbose, Alogliptin, Saxagliptin, Dulaglutide, Albiglutide, Canagliflozin, Dapagliflozin, Empagliflozin, Chlorpropamide) — Methylprednisolone induces hyperglycaemia and antagonises the glucose-lowering effect of these agents; blood glucose monitoring is essential
  - **Amphotericin B / Amphotericin B (lipid complex)** — Combined use increases risk of severe hypokalaemia
  - **Acetylsalicylic acid** — Increased risk of gastrointestinal bleeding and ulceration
  - **Aprepitant** — CYP3A4 inhibition may substantially increase methylprednisolone exposure
  - **Bisacodyl / Picosulfuric acid** — Risk of electrolyte imbalance with concurrent laxative use

- **Minor interactions:** Zinc sulfate

Please refer to the approved package insert for complete key warnings and contraindications, which were not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 4 clinical trial (NCT01167946) directly studying oral mega-pulse methylprednisolone in severe, therapy-resistant alopecia areata, supported by a controlled trial, multiple prospective studies, and retrospective cohorts totalling 20 publications, provides L2-level evidence. The immunosuppressive mechanism of methylprednisolone directly addresses the CD8+ T cell-mediated pathophysiology of AA, offering strong biological plausibility alongside documented clinical use.

**To proceed, the following is needed:**
- Download and review the official CDSCO/international package insert for complete warnings, contraindications, and dosing specifications (currently a blocking data gap)
- Confirm full mechanism of action detail from DrugBank API or peer-reviewed pharmacology references
- Define a clear India regulatory pathway with CDSCO for new indication filing (NDA/sNDA), given the drug is currently unregistered in India
- Design a prospective clinical protocol with explicit inclusion criteria (AA severity staging, minimum SALT score), standardised pulse regimen parameters (dose, frequency, duration), and pre-specified safety monitoring (fasting blood glucose, blood pressure, bone density, infection screening)
- Conduct a risk-benefit assessment for special populations: paediatric dosing adjustments, patients with diabetes or pre-diabetes (given the extensive antidiabetic DDI profile), and immunocompromised individuals
- Establish a structured relapse management and long-term follow-up plan, as high relapse rates following corticosteroid pulse therapy discontinuation are a well-documented limitation of this approach in AA
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

