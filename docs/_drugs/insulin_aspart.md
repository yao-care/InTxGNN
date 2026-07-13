---
layout: default
title: Insulin Aspart
parent: 僅模型預測 (L5)
nav_order: 307
evidence_level: L5
indication_count: 10
---

# Insulin Aspart
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

# Insulin Aspart: From Rapid-Acting Bolus Insulin to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin aspart (NovoRapid®/NovoLog®/Fiasp®) is a rapid-acting human insulin analog globally established as the standard mealtime bolus insulin for diabetes management, but currently **not approved in India**.
The TxGNN model predicts it may be effective for **Type 1 Diabetes Mellitus (T1DM)**, with **50 clinical trials** and **20 publications** currently supporting this direction — a high-confidence prediction that validates the drug's core globally established indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No India regulatory data (drug not currently approved in India) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Insulin aspart is a structurally modified rapid-acting human insulin analog in which proline at position B28 is substituted by aspartic acid (Asp28). This single amino acid change reduces the self-aggregation of insulin molecules into hexamers, accelerating dissociation into monomers and subsequent subcutaneous absorption. The result is an earlier peak plasma concentration (~40–50 minutes post-injection versus ~2–3 hours for regular human insulin) and a shorter duration of action, enabling more physiological postprandial glucose coverage when injected immediately before or just after meals.

Type 1 diabetes mellitus is defined by autoimmune destruction of pancreatic beta cells, producing absolute insulin deficiency. Patients require lifelong exogenous insulin replacement encompassing both basal coverage and bolus (mealtime) supplementation. Insulin aspart's pharmacokinetic profile directly addresses the postprandial glucose excursions that drive the microvascular and macrovascular complications of T1DM — retinopathy, nephropathy, neuropathy, and cardiovascular disease. It functions by binding the insulin receptor, stimulating glucose uptake in peripheral tissues (muscle, adipose), suppressing hepatic glycogenolysis, and inhibiting gluconeogenesis.

This TxGNN prediction (99.95% score, L1 evidence) is best understood as a **strong positive validation**: insulin aspart is already a global first-line standard of care in T1DM basal-bolus regimens, with Phase 3 RCT evidence spanning multiple continents, age groups (pediatric through adult), and special populations (pregnancy). Its absence from India's regulatory approval record represents a market access gap rather than a therapeutic novelty. The evidence base is exceptional and warrants expedited regulatory consideration for India market entry.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02670915](https://clinicaltrials.gov/study/NCT02670915) | Phase 3 | Completed | 834 | Global RCT comparing faster-acting insulin aspart (Fiasp) vs. standard NovoRapid® (insulin aspart), both with insulin degludec, in children and adolescents with T1DM; largest pediatric Phase 3 trial for this agent |
| [NCT01486940](https://clinicaltrials.gov/study/NCT01486940) | Phase 3 | Completed | 598 | Multinational open-label RCT comparing insulin detemir + insulin aspart vs. NPH insulin + human soluble insulin in T1DM basal-bolus regimen; highest-grade direct evidence for aspart as bolus component |
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Phase 3 | Completed | 350 | BEGIN™ Young 1: 26-week multinational RCT (Africa, Asia, Europe, USA) comparing insulin degludec vs. detemir, with insulin aspart as the bolus in children/adolescents aged 1–17 with T1DM |
| [NCT06199505](https://clinicaltrials.gov/study/NCT06199505) | Phase 2 | Completed | 153 | Active-controlled RCT (China) comparing GZR101 vs. insulin degludec/insulin aspart (IDegAsp) in T2DM; insulin aspart serves as active reference comparator arm |
| [NCT00700648](https://clinicaltrials.gov/study/NCT00700648) | N/A | Completed | 3,024 | Multicenter observational safety and efficacy study of intravenous insulin aspart infusion in hospitalized patients in India; largest India-based dataset, directly relevant to local safety profile |
| [NCT00675493](https://clinicaltrials.gov/study/NCT00675493) | N/A | Completed | 942 | 24-week observational study of biphasic insulin aspart 30 (NovoMix® 30) in T1DM and T2DM patients under routine clinical practice conditions in Romania; real-world HbA1c evaluation |
| [NCT04711382](https://clinicaltrials.gov/study/NCT04711382) | N/A | Completed | 438 | Prospective multicenter real-world study (Belgium) evaluating switch from traditional mealtime insulin to faster-acting insulin aspart (Fiasp) in T1DM; supports external validity |
| [NCT05224258](https://clinicaltrials.gov/study/NCT05224258) | N/A | Completed | 240 | Global study (US, Canada, Australia) evaluating MiniMed™ 780G automated insulin delivery system using Fiasp (insulin aspart) in T1DM adults and children; technology integration evidence |
| [NCT04196231](https://clinicaltrials.gov/study/NCT04196231) | Phase 4 | Completed | 258 | BEYOND trial: fixed-ratio basal insulin + GLP-1RA or SGLT-2i vs. basal-bolus regimen (with insulin aspart as bolus) in T2DM; durability of glycemic control comparison |
| [NCT01271517](https://clinicaltrials.gov/study/NCT01271517) | Phase 4 | Unknown | 120 | Long-acting basal insulin analogs (with insulin aspart as mealtime comparator) in newly diagnosed pediatric T1DM; evaluates preservation of endogenous insulin production and GH/IGF-I axis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [21333580](https://pubmed.ncbi.nlm.nih.gov/21333580/) | 2011 | Systematic Review (RCT-based) | Diabetes & Metabolism | Systematic comparison of insulin aspart vs. regular human insulin and biphasic aspart vs. premixed human insulin in T1DM/T2DM; demonstrated superiority of aspart in postprandial glycemic control |
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | The Lancet | ONWARDS 6: once-weekly insulin icodec vs. once-daily insulin degludec in T1DM basal-bolus regimen; provides high-quality Phase 3a comparative context for bolus insulin (aspart) use |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes & Endocrinology | EXPECT trial: non-inferiority RCT of insulin degludec vs. detemir, both combined with insulin aspart, in pregnant women with T1DM; direct head-to-head evidence with aspart as the common bolus |
| [37804858](https://pubmed.ncbi.nlm.nih.gov/37804858/) | 2023 | RCT | Lancet Diabetes & Endocrinology | CopenFast: open-label single-centre RCT comparing faster-acting insulin aspart vs. standard insulin aspart in T1DM/T2DM during pregnancy; evaluated fetal growth, HbA1c, and hypoglycemia |
| [40129237](https://pubmed.ncbi.nlm.nih.gov/40129237/) | 2025 | RCT | Diabetes, Obesity & Metabolism | Double-blind crossover RCT: faster-acting aspart vs. insulin aspart in T1DM adults using non-automated insulin pump + CGM; efficacy and safety comparison with CGM-based endpoints |
| [41697686](https://pubmed.ncbi.nlm.nih.gov/41697686/) | 2026 | Review | JAMA | Comprehensive current review of T1DM: epidemiology, autoimmune pathophysiology, complications, and insulin therapy including bolus analog selection (2026 evidence synthesis) |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes & Endocrinology | Management of T1DM in pregnancy: lifestyle, pharmacological treatment (including insulin aspart), and advanced technologies (CGM, CSII, closed-loop); covers time-in-range targets |
| [15871555](https://pubmed.ncbi.nlm.nih.gov/15871555/) | 2003 | Review | Treatments in Endocrinology | Spotlight on insulin aspart: rapid subcutaneous absorption, HbA1c reductions vs. regular human insulin in T1DM and T2DM clinical trials |
| [12215068](https://pubmed.ncbi.nlm.nih.gov/12215068/) | 2002 | Review | Drugs | Foundational comprehensive pharmacological review of insulin aspart: PK/PD, randomized clinical trials, and clinical use in T1DM and T2DM management |
| [31902063](https://pubmed.ncbi.nlm.nih.gov/31902063/) | 2020 | Review | Diabetes Therapy | Narrative review of insulin management in adult T1DM: MDI vs. CSII, bolus analog selection, glycemic target strategies, and hypoglycemia management |

---

## India Market Information

Insulin aspart currently has **no registered products** in India (CDSCO). There are 0 active licenses on record, and the drug's market status is classified as **Not Marketed** in India.

> No India marketing authorization data is available for insulin aspart. Despite its global use as a first-line rapid-acting insulin analog (approved in the US, EU, Japan, and many other jurisdictions), formal CDSCO registration has not been identified in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** India-specific prescribing information (TFDA/CDSCO package insert, including warnings and contraindications) is a **blocking data gap** (DG001) that must be resolved before India-specific safety assessment can be completed. No drug-drug interaction data was found in the DDI query. Globally, key safety considerations for insulin aspart class include hypoglycemia risk, injection-site reactions, and insulin antibody development — these should be confirmed against the local regulatory label.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Insulin aspart is globally established as a first-line rapid-acting bolus insulin for T1DM, supported by multiple Phase 3 RCTs across diverse populations (pediatric, adult, pregnant), a 99.95% TxGNN prediction score, and an L1 evidence classification. The India market gap represents a regulatory access barrier, not a scientific uncertainty. The evidence base is strong enough to support a CDSCO marketing authorization application.

**To proceed, the following is needed:**
- **CDSCO marketing authorization application (MAA):** File the registration dossier with CDSCO; assess whether a local Indian bridging pharmacokinetic/pharmacodynamic study is required under Schedule Y regulations
- **Local package insert (blocking gap DG001):** Obtain and review India-specific prescribing information including warnings, contraindications, and population-specific dosing guidance; this is required before any India safety assessment can proceed
- **Mechanism of action documentation (high-priority gap DG002):** Complete formal MOA documentation from DrugBank API for regulatory submission support
- **Drug-drug interaction profile:** DDI data was not found in the current query; a comprehensive DDI review referencing global labels is required for the Indian submission dossier
- **Cold-chain infrastructure confirmation:** Insulin aspart requires 2–8°C storage; confirm India supply-chain and distribution cold-chain readiness
- **Special population data:** Confirm availability of pediatric dosing guidance and pregnancy safety data (EXPECT trial data available) for Indian regulatory reviewers
- **Pharmacovigilance plan:** Develop an India-specific Risk Management Plan (RMP) per CDSCO pharmacovigilance requirements, with particular emphasis on hypoglycemia monitoring in the Indian patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

