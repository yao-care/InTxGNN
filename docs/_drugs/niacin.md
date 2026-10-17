---
layout: default
title: Niacin
parent: Model Prediction Only (L5)
nav_order: 590
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Niacin: predicted new indication Homozygous familial hypercholesterolemia (evidence level L5). Approved use: Hypertriglyceridemia, hyperlipidemia, familial hyperlipidemia…"
monitor_inn: "Niacin"
predicted_indications: ["homozygous familial hypercholesterolemia"]
---

# Niacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Niacin: From Hyperlipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Niacin (vitamin B3) is originally used to treat hyperlipidemia, including hypertriglyceridemia and familial hyperlipidemia, and to correct vitamin deficiency.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia (HoFH)**.
However, there are **no registered clinical trials** and **no HoFH-specific niacin studies** in the data compiled for this report. Support comes only from **17 publications**, mostly reviews, in which niacin appears as one of several adjunct options.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertriglyceridemia, hyperlipidemia, familial hyperlipidemia, vitamin deficiency disorder (from the knowledge graph; the Indian licence records contain no indication text) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 (no clinical trials; only indirect literature and mechanistic reasoning) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Niacin lowers LDL cholesterol, triglycerides and lipoprotein(a) and raises HDL cholesterol. It is thought to do this by inhibiting hepatic DGAT2, which reduces VLDL and LDL production, and by suppressing fat-cell lipolysis through the GPR109A receptor. Formal mechanism-of-action data were not available for this report, so this description is based on general pharmacological knowledge.

Niacin's existing indications already include hyperlipidemia and familial hyperlipidemia. HoFH is a severe, rare form of inherited high cholesterol, so the target pathway is biologically plausible.

There is an important limitation. HoFH is caused by absent or severely impaired LDL receptor function. Niacin's effect partly depends on mechanisms that do not rely on that receptor, so any response is expected to be limited. The literature supplied mentions niacin only as one of several non-statin adjunct options in reviews and guideline statements. The very high TxGNN score is a model output, not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the publications below tested niacin specifically in HoFH. Only the most relevant are listed, with reviews and statements prioritised. No randomised controlled trials were found.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26376908](https://pubmed.ncbi.nlm.nih.gov/26376908/) | 2015 | Scientific statement | Arterioscler Thromb Vasc Biol | Placebo-controlled trials showed that bile acid sequestrants, niacin and fibrates each reduce cardiovascular endpoints as monotherapy; discusses the role of non-statin LDL-lowering therapy |
| [24506448](https://pubmed.ncbi.nlm.nih.gov/24506448/) | 2014 | Review | Expert Rev Cardiovasc Ther | Reviews non-statin options (fibrates, ezetimibe, bile acid sequestrants, n-3 fatty acids, niacin) for residual risk and statin intolerance |
| [23959229](https://pubmed.ncbi.nlm.nih.gov/23959229/) | 2013 | Review | Nat Rev Cardiol | Lipid-lowering agents beyond statins can supplement or replace statins in severe hypercholesterolaemia or mixed dyslipidaemia |
| [26370207](https://pubmed.ncbi.nlm.nih.gov/26370207/) | 2015 | Review | Drugs | Challenges in diagnosing and treating HoFH, a rare genetic disorder with impaired LDL receptor function |
| [27797643](https://pubmed.ncbi.nlm.nih.gov/27797643/) | 2016 | Review | Metab Syndr Relat Disord | Modern management of familial hypercholesterolemia, including the homozygous form |
| [25257073](https://pubmed.ncbi.nlm.nih.gov/25257073/) | 2014 | Review | Atheroscler Suppl | Current achievements and unmet needs in HoFH, including apheresis and lipid-lowering drugs |
| [36422206](https://pubmed.ncbi.nlm.nih.gov/36422206/) | 2022 | Review | Medicina (Kaunas) | Literature analysis of diagnosis and treatment options for familial hypercholesterolemia |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | Pharmacokinetic study | Pharmacotherapy | Studied the effect of lomitapide (approved for HoFH) on the pharmacokinetics of several lipid-lowering drugs, including niacin |
| [2912428](https://pubmed.ncbi.nlm.nih.gov/2912428/) | 1989 | Clinical study | Arteriosclerosis | Drug regimens in children with familial hypercholesterolemia, including 3 with the homozygous form |
| [23074505](https://pubmed.ncbi.nlm.nih.gov/23074505/) | 2007 | Health technology assessment | Ont Health Technol Assess Ser | Evidence-based analysis of LDL apheresis in refractory homozygous and heterozygous FH |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 151623 | Nialip 250mg Tablet (Dr Reddy's Laboratories Ltd) | Strip of 7 tablets | Not specified |
| 150631 | Nicoglow 250mg Tablet (Glowderma Labs Pvt Ltd) | Strip of 10 tablets | Not specified |

Both are valid single-ingredient oral products.

## Safety Considerations

- **Drug Interactions**: 178 interactions were recorded. Those listed are mostly **Moderate**, with glucose-lowering drugs prominent: metformin, sulfonylureas (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), GLP-1 agonists (albiglutide, dulaglutide, exenatide), DPP-4 inhibitor alogliptin, acarbose and several insulins. Interaction with acetylsalicylic acid is rated Minor. Blood glucose should be monitored when niacin is combined with these drugs.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible, but the evidence is at L4: there are no clinical trials and no HoFH-specific niacin studies. Niacin appears only as one of several adjunct options in general reviews. HoFH involves impaired LDL receptor function, so niacin's benefit is expected to be limited. The high TxGNN score is not clinical evidence.

**To proceed, the following is needed:**
- Evidence specific to niacin in HoFH, such as case series, small trials or post-hoc analyses, and a comparison with established HoFH therapies
- Detailed mechanism of action data
- Package insert warnings and contraindications from the Indian licences, which currently carry no indication text
- A dedicated safety review, including the glucose-related interactions and use in this patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

