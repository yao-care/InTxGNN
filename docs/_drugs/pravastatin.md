---
layout: default
title: Pravastatin
parent: Moderate Evidence (L3-L4)
nav_order: 695
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-14
description: "Pravastatin: predicted new indication Homozygous familial hypercholesterolemia (evidence level L4). Approved use: Not stated in the India licence records. The knowledge graph lists hy…"
---

# Pravastatin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **9** 
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

# Pravastatin: From Hyperlipidemia and Atherosclerotic Disease to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Pravastatin is a statin (HMG-CoA reductase inhibitor) originally used for lipid disorders such as hypertriglyceridemia and hyperlipoproteinemia, and for atherosclerosis and stroke-related conditions.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia (HoFH)**, but the data compiled for this report contain **1 clinical trial** (which does not test pravastatin) and **12 publications** (mostly reviews of other lipid-lowering drugs), so direct support is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India licence records. The knowledge graph lists hypertriglyceridemia, stroke, cerebrovascular disorder, cerebral infarction, atherosclerosis, familial combined hyperlipidemia and hyperlipoproteinemia |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold (research question only) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Pravastatin is known as a statin that inhibits HMG-CoA reductase, lowering hepatic cholesterol synthesis and upregulating hepatic LDL receptors, which lowers LDL cholesterol. Its efficacy in hyperlipidemia and atherosclerotic disease is established, and mechanistically it may be applicable to familial hypercholesterolemia.

There is an important limitation. Statin response depends on residual LDL receptor activity. In homozygous FH, particularly receptor-negative patients, the effect is expected to be limited. One review in the data (Prescrire, 2004) also states that statins are not very effective in homozygous FH.

The same prediction approach also ranks **familial hypercholesterolemia (heterozygous/general)** much more strongly supported (evidence level L2, score 99.34%). Pediatric studies show pravastatin lowers LDL-C in FH, including a placebo-controlled study in 72 children and a 20-year follow-up of statins in children with FH. That use is largely an extension of its existing lipid-lowering role rather than a novel repurposing.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label alirocumab in children and adolescents (8–17 years) with HoFH. It does not evaluate pravastatin; statins may appear only as background therapy |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Statins for children with familial hypercholesterolemia |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Updated review of statins for children with familial hypercholesterolemia |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guidelines for dyslipidemia and cardiovascular prevention |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | Rosuvastatin review; reports it was superior to pravastatin in improving the lipid profile |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review | Am J Cardiovasc Drugs | Ezetimibe, a cholesterol absorption inhibitor |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | Rosuvastatin in hyperlipidemia, including HoFH |
| [15532136](https://pubmed.ncbi.nlm.nih.gov/15532136/) | 2004 | Review | Prescrire Int | Notes statins are not very effective in homozygous FH |
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | Phase 4 RCT | Lancet HIV | Pitavastatin versus pravastatin in HIV with dyslipidemia (not HoFH) |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 178181 | Prastatin 10mg Tablet | Strip of 10 tablets | Not specified |
| 176144 | Prastatin 20mg Tablet | Strip of 10 tablets | Not specified |
| 177163 | Pravator 20mg Tablet | Strip of 10 tablets | Not specified |
| 179420 | Pravator 10mg Tablet | Strip of 10 tablets | Not specified |

All four licences are valid single-ingredient oral tablets, from Emcure Pharmaceuticals and Sun Pharmaceutical Industries.

## Safety Considerations

- **Contraindicated or cautioned conditions (from the knowledge graph, not label text)**: kidney disease, liver disease, gallbladder disease, myopathy and other muscle diseases, rhabdomyolysis, thrombocytopenia, peptic ulcer disease, gout, hemophilia, anaemia, and others.
- **Drug Interactions**: 239 interactions were recorded. Moderate-level ones include metronidazole, clarithromycin, eluxadoline, naltrexone, pectin, rosuvastatin, simvastatin and tinidazole. Combining pravastatin with other statins (rosuvastatin, simvastatin) warrants particular care.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a very high model score, but the only linked trial tests alirocumab rather than pravastatin, and the literature is mostly reviews of other agents. HoFH is also biologically unfavourable for statins, which depend on residual LDL receptor function. The better-supported opportunity is heterozygous familial hypercholesterolemia, which is largely an existing lipid-lowering use. HIV-associated dyslipidemia is a separate candidate (L3, Proceed with Guardrails) based on small trials.

**To proceed, the following is needed:**
- Pravastatin-specific data in HoFH, stratified by LDL receptor status
- Detailed mechanism of action data
- India package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text for the Indian licences
- Dosing and interaction guidance for combination with PCSK9 inhibitors or other lipid-lowering agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

