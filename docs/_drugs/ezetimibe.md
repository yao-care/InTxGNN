---
layout: default
title: Ezetimibe
parent: Model Prediction Only (L5)
nav_order: 336
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
monitor_inn: "Ezetimibe"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
description: "Ezetimibe: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Ezetimibe
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

## Ezetimibe: Cholesterol-ester transfer protein deficiency
{: .text-alpha }

## One-Sentence Summary

Ezetimibe is a cholesterol absorption inhibitor, originally used to treat hyperlipidemia, familial hyperlipidemia, homozygous familial hypercholesterolemia and sitosterolemia.
This prediction is essentially an on-label or closely related use, so it has low novelty as a true repurposing candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9909 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Ezetimibe inhibits NPC1L1-mediated intestinal cholesterol absorption, which lowers LDL-C and apolipoprotein B. Detailed mechanism of action data are not available in the data compiled for this report, but this mechanism is well established for its approved use in hyperlipidemia.

Hyperlipoproteinemia is a closely related lipid disorder to the original indications. The mechanism that lowers cholesterol in hyperlipidemia applies directly, so this prediction is better seen as an extension within the same disease family than as a new therapeutic area. The label scope should be checked before it is counted as repurposing.

Other predictions from the model:
- Heterozygous and paediatric populations are the main extension. Ezetimibe gives additive LDL-C lowering with statins in patients with LDL receptor defects.
- One preclinical mouse report links NPC1L1 deficiency to altered FGF15 and bile acid pool. There are no human data for this ultra-rare condition. Status: Research Question.
- **Cholesterol-ester transfer protein deficiency (0.9909, L5)**: Not supported. This condition raises HDL-C and does not mainly need LDL lowering. The retrieved literature does not evaluate ezetimibe. Status: Hold.

## Clinical Trial Evidence

The table lists the most relevant trials for hyperlipoproteinemia.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00753883](https://clinicaltrials.gov/study/NCT00753883) | Phase 4 | Completed | 40 | Open-label randomized comparison of ezetimibe added to a statin versus statin alone for LDL lowering in hypercholesterolemia |
| [NCT03847506](https://clinicaltrials.gov/study/NCT03847506) | Phase 4 | Completed | 127 | Double-blind trial of ezetimibe/rosuvastatin plus candesartan/amlodipine in hypertension with hyperlipidemia |
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Phase 3 | Terminated | 49 | Open-label treatment-use study of ezetimibe 10 mg/day in homozygous FH or sitosterolemia |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe added to atorvastatin or simvastatin in homozygous FH |
| [NCT01984424](https://clinicaltrials.gov/study/NCT01984424) | Phase 3 | Completed | 511 | Evolocumab versus ezetimibe in statin-intolerant patients (ezetimibe as comparator, indirect evidence) |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Phase 3 | Completed | 1220 | Ezetimibe/simvastatin plus extended-release niacin in type IIa/IIb hyperlipidemia |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | Completed | 576 | Fenofibrate plus ezetimibe in mixed hyperlipidemia |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | Completed | 611 | Ezetimibe/simvastatin plus fenofibrate in mixed hyperlipidemia |
| [NCT00705211](https://clinicaltrials.gov/study/NCT00705211) | N/A | Completed | 1794 | 52-week post-marketing surveillance of Zetia in Japan, supporting long-term safety |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE: ezetimibe plus high-dose simvastatin versus simvastatin alone in heterozygous FH |

Note: the withdrawn trial NCT06789432 (0 participants) provides no evidence.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT (phase 3) | Lancet | TANDEM: obicetrapib/ezetimibe fixed-dose combination for LDL-C reduction |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oral PCSK9 inhibitor enlicitide in heterozygous FH |
| [25282519](https://pubmed.ncbi.nlm.nih.gov/25282519/) | 2015 | RCT | Lancet | RUTHERFORD-2: evolocumab in heterozygous FH despite statin with or without ezetimibe |
| [37850379](https://pubmed.ncbi.nlm.nih.gov/37850379/) | 2024 | RCT | Circulation | ORION-5: inclisiran in homozygous FH |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Review | Mol Med Rep | Advances in drugs targeting hyperlipidemia |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | New and emerging LDL-C and apoB lowering therapies on top of statins, ezetimibe and PCSK9 inhibitors |
| [30702994](https://pubmed.ncbi.nlm.nih.gov/30702994/) | 2019 | Review | Circ Res | Overview of cholesterol-lowering agents |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Review | J Cardiovasc Pharmacol Ther | Comprehensive review of PCSK9 inhibitors |
| [35101175](https://pubmed.ncbi.nlm.nih.gov/35101175/) | 2022 | Cohort | Lancet | Worldwide retrospective cohort of homozygous FH |
| [38599725](https://pubmed.ncbi.nlm.nih.gov/38599725/) | 2024 | Review | Indian Heart J | Familial hypercholesterolemia, including its burden in India |

Most of these studies concern other lipid-lowering agents in which ezetimibe is a comparator or background therapy, so they support the disease setting more than ezetimibe itself.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 73458 | Ezechol 10mg Tablet | Strip of 10 tablets | Not available |
| 76024 | Ezibloc 10mg Tablet | Strip of 10 tablets | Not available |
| 73905 | Ezitrol 10mg Tablet | Strip of 10 tablets | Not available |
| 75189 | Ezedoc 5mg Tablet | Strip of 10 tablets | Not available |
| 78059 | Ezee Fresh Capsule | Strip of 10 capsules | Not available |

There are 20 valid single-ingredient registrations in total, all oral (tablets, plus one capsule product). The five above are examples.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: pancreatitis, liver disease, gallbladder disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, substance abuse/dependence, rhabdomyolysis, nodular fasciitis.
- **Drug Interactions**: 171 interactions were identified. Those rated Moderate are chenodeoxycholic acid, eluxadoline, rosuvastatin and simvastatin. Others, such as calcitriol, pantoprazole, glimepiride, metformin, omeprazole and morphine, have no severity rating.

Please refer to the package insert for warnings and contraindications, since label text was not available for this report.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ezetimibe has multiple completed Phase 3 trials and a long post-marketing record in lipid disorders, and the predicted indication is a close relative of its approved uses. Because this is largely on-label, novelty is low, and the evidence is strongest for combination use with statins.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indication text for the Indian registrations (currently missing, and a blocking gap for safety screening)
- Confirmation of whether hyperlipoproteinemia is already covered by the approved label
- Detailed mechanism of action data
- Monitoring plan for liver and muscle safety, especially when combined with statins
- Review of the interaction profile for commonly co-prescribed drugs
- The other predictions (CYP7A1 deficiency, CETP deficiency) should not advance: the first stays a research question, and the second should be held
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

