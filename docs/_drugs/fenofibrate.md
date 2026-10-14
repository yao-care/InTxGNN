---
layout: default
title: Fenofibrate
parent: Model Prediction Only (L5)
nav_order: 344
evidence_level: L5
indication_count: 7
---

# Fenofibrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Fenofibrate: From Hypertriglyceridemia to Hyperlipoproteinemia

## One-Sentence Summary

Fenofibrate is a lipid-lowering drug originally used for hypertriglyceridemia and other forms of hyperlipidemia.
The TxGNN model's top-ranked prediction is **homozygous familial hypercholesterolemia**, but the best-supported prediction is **hyperlipoproteinemia**, backed by **26 clinical trials** and **20 publications**. This is largely an on-label or near-label use rather than a true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertriglyceridemia, hyperlipidemia, familial hyperlipidemia, hypoalphalipoproteinemia (the approved-indication text in the India licences is blank) |
| Predicted New Indication | Homozygous familial hypercholesterolemia (rank 1); best-supported: hyperlipoproteinemia (rank 2) |
| TxGNN Prediction Score | 99.91% (homozygous FH); 99.65% (hyperlipoproteinemia) |
| Evidence Level | L4 (homozygous FH); L1 (hyperlipoproteinemia) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold for homozygous FH; Proceed with Guardrails for hyperlipoproteinemia |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. From the evidence reviewed, fenofibrate is a PPARα agonist. It increases lipoprotein lipase activity and fatty-acid oxidation and reduces apoC-III. This lowers triglycerides and VLDL and raises HDL-C. It also lowers LDL-C modestly.

**Homozygous FH (rank 1):** The mechanistic link is weak. This disease is driven by LDL receptor dysfunction, and PPARα activation is unlikely to produce meaningful LDL-C reduction. The only linked trial tests alirocumab, not fenofibrate. The only fenofibrate-specific literature is a 1984 study in type II hyperlipoproteinemia that included one homozygous patient, which is indirect evidence at best. The high TxGNN score therefore should not be read as clinical support.

**Hyperlipoproteinemia (rank 2):** This largely overlaps with fenofibrate's established indications (hypertriglyceridemia, mixed hyperlipidemia). Several Phase 3 randomized trials and head-to-head comparisons, including against gemfibrozil, support efficacy. It is better described as a near-label indication.

**Other predictions:** Familial hypercholesterolemia and autosomal dominant hypercholesterolemia are supported only by small 1980s studies, with a plausible role as an adjunct for residual hypertriglyceridemia. CETP deficiency, cholesterol 7α-hydroxylase deficiency, and hepatic lipase deficiency rest on preclinical data, a very small kinetic study, or no data at all.

---

## Clinical Trial Evidence

Trials for the best-supported prediction, hyperlipoproteinemia (the 10 most relevant):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | Completed | 576 | Fenofibrate + ezetimibe coadministration in mixed hyperlipidemia |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Phase 3 | Completed | 587 | Fenofibrate + ezetimibe coadministration in mixed hyperlipidemia |
| [NCT00349375](https://clinicaltrials.gov/study/NCT00349375) | Phase 3 | Completed | 1040 | Fenofibrate 145 mg + simvastatin vs simvastatin alone in mixed dyslipidemia |
| [NCT00459745](https://clinicaltrials.gov/study/NCT00459745) | Phase 3 | Completed | 481 | Pravastatin vs fenofibrate vs the combination (Pravafen) in combined hyperlipidemia |
| [NCT00362934](https://clinicaltrials.gov/study/NCT00362934) | Phase 3 | Completed | 516 | Fenofibrate + simvastatin vs atorvastatin in mixed dyslipidemia |
| [NCT00362206](https://clinicaltrials.gov/study/NCT00362206) | Phase 3 | Completed | 423 | Fenofibrate + simvastatin vs pravastatin in mixed dyslipidemia |
| [NCT00352183](https://clinicaltrials.gov/study/NCT00352183) | Phase 3 | Completed | 450 | Fenofibrate + simvastatin vs simvastatin in mixed dyslipidemia |
| [NCT01956201](https://clinicaltrials.gov/study/NCT01956201) | Phase 3 | Unknown | 476 | Fenofibrate added to atorvastatin vs atorvastatin in mixed hypercholesterolemia |
| [NCT00349284](https://clinicaltrials.gov/study/NCT00349284) | Phase 3 | Completed | 181 | Fenofibrate vs ezetimibe vs combination in type IIb dyslipidemia |
| [NCT00754039](https://clinicaltrials.gov/study/NCT00754039) | Phase 4 | Completed | 129 | Colesevelam + fenofibrate (TriCor) vs TriCor alone in mixed hyperlipidemia |

For homozygous FH, the only linked trial ([NCT03510715](https://clinicaltrials.gov/study/NCT03510715), Phase 3, 18 participants) tests alirocumab and provides no direct evidence for fenofibrate.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11942772](https://pubmed.ncbi.nlm.nih.gov/11942772/) | 2002 | RCT | Endocr Pract | Micronized fenofibrate vs gemfibrozil in type IIa/IIb primary hyperlipoproteinemia (crossover) |
| [9110923](https://pubmed.ncbi.nlm.nih.gov/9110923/) | 1997 | RCT | Eur J Med Res | Bezafibrate vs micronized fenofibrate in type III hyperlipoproteinemia |
| [12816176](https://pubmed.ncbi.nlm.nih.gov/12816176/) | 2003 | RCT | Int J Clin Pharmacol Ther | Fenofibrate and simvastatin effects on sICAM-1 and MCP-1 in hyperlipoproteinemia |
| [2653622](https://pubmed.ncbi.nlm.nih.gov/2653622/) | 1989 | Clinical study | Cardiology | Placebo-controlled US study of fenofibrate in type IV/V hyperlipoproteinemia (n=147) |
| [3318454](https://pubmed.ncbi.nlm.nih.gov/3318454/) | 1987 | Clinical study | Am J Med | Fenofibrate in hypercholesterolemia and combined hyperlipidemia (randomized, 24 weeks, n=227) |
| [2226216](https://pubmed.ncbi.nlm.nih.gov/2226216/) | 1990 | Review | Drugs | Pharmacology and therapeutic use of fenofibrate in dyslipidaemia |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart J | Fenofibrate monotherapy is most clearly indicated for fasting triglycerides >500 mg/dl, to reduce acute pancreatitis risk |
| [6529448](https://pubmed.ncbi.nlm.nih.gov/6529448/) | 1984 | Clinical study | Atherosclerosis | Fenofibrate lowered VLDL, IDL and LDL in familial hypercholesterolemia and combined hyperlipidemia |
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Cohort | Pharmacol Res Commun | 22 type II patients: total cholesterol −22%, LDL −24%; one homozygous FH patient showed the greatest fall |
| [16224048](https://pubmed.ncbi.nlm.nih.gov/16224048/) | 2005 | Clinical kinetic study | Arterioscler Thromb Vasc Biol | Fenofibrate in 2 patients with complete hepatic lipase deficiency |

---

## India Market Information

Fenofibrate has 20 valid single-ingredient registrations in India and none have been cancelled. Five are listed below. The approved-indication text is not available in the data compiled for this report.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 228618 | Thunor F 75mg/10mg Tablet | Strip of 10 tablets | Not specified |
| 185695 | Rosovas F 160mg/10mg Tablet | Strip of 10 tablets | Not specified |
| 120868 | Lipicard 160 Tablet | Strip of 10 tablets | Not specified |
| 104604 | Hivast F 145mg/10mg Tablet | Strip of 10 tablets | Not specified |
| 85904 | Finabate 145mg Tablet | Strip of 10 tablets | Not specified |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** liver failure and liver disease, pancreatitis, gallbladder disease including cholelithiasis, myopathy and rhabdomyolysis, impaired renal function, thrombocytopenia, anemia, and leukopenia/neutropenia-type blood disorders.
- **Drug Interactions:** 199 interactions were found. The listed ones are Moderate level and include:
  - sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide);
  - many insulin products;
  - chenodeoxycholic acid;
  - esomeprazole.

  Monitor blood glucose when fenofibrate is combined with antidiabetic agents.

Please also refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (hyperlipoproteinemia); Hold (homozygous FH, CETP deficiency, 7α-hydroxylase deficiency, hepatic lipase deficiency); Research Question (familial and autosomal dominant hypercholesterolemia)**

**Rationale:**
- Hyperlipoproteinemia is supported by multiple completed Phase 3 randomized trials and randomized comparisons (L1), but it largely overlaps with existing indications.
- The top-scoring prediction, homozygous FH, lacks fenofibrate-specific evidence and has a weak mechanistic rationale, so it should not be pursued.
- For heterozygous and familial FH, fenofibrate's role is limited to an adjunct for residual hypertriglyceridemia, because statins, ezetimibe and PCSK9 inhibitors are far more effective on LDL-C.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India registrations (currently missing, and a blocking gap for safety screening)
- Approved-indication text for the India licences
- Detailed mechanism-of-action data
- For FH, a modern controlled study of fenofibrate as an adjunct in patients with elevated triglycerides
- A monitoring plan for liver and renal function, muscle toxicity, and glucose when co-prescribed with antidiabetic drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

