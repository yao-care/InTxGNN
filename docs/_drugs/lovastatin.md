---
layout: default
title: Lovastatin
parent: Model Prediction Only (L5)
nav_order: 506
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Lovastatin: predicted new indication Homozygous familial hypercholesterolemia (evidence level L5). Approved use: Hyperlipidemia, familial hyperlipidemia, hypertriglyceridemia…"
monitor_inn: "Lovastatin"
predicted_indications: ["homozygous familial hypercholesterolemia", "hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "cholesterol-ester transfer protein deficiency"]
---

# Lovastatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Lovastatin: From Hyperlipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Lovastatin is a statin (HMG-CoA reductase inhibitor) originally used to treat hyperlipidemia, familial hyperlipidemia and atherosclerosis.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia**, but the evidence is thin: the only listed trial tests a different drug (alirocumab), and the supporting literature consists mainly of small, older lovastatin studies with mixed results.
The strongest-supported neighbouring predictions, **hyperlipoproteinemia** and **familial hypercholesterolemia**, are essentially extensions of the existing indication rather than true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperlipidemia, familial hyperlipidemia, hypertriglyceridemia, atherosclerosis (from the knowledge graph; no approved indication text is available in the India licence records) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 (for the top-ranked prediction) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold (as a research question) |

For context, the other predictions were assessed as follows:

| Rank | Predicted Indication | Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 1 | Homozygous familial hypercholesterolemia | 99.89% | L3 | Research question / Hold |
| 2 | Hyperlipoproteinemia | 99.87% | L1 | Proceed with Guardrails |
| 3 | Hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency | 99.63% | L5 | Hold |
| 4 | Familial hypercholesterolemia | 99.48% | L1 | Proceed with Guardrails |
| 5 | Cholesterol-ester transfer protein deficiency | 99.42% | L5 | Hold |
| 6 | Hyperlipidemia due to hepatic triglyceride lipase deficiency | 99.13% | L4 | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, lovastatin is a statin that inhibits HMG-CoA reductase, the rate-limiting enzyme of cholesterol synthesis. This lowers hepatic cholesterol, increases LDL receptor expression and lowers LDL-C. Its efficacy in hyperlipidemia is established.

Homozygous familial hypercholesterolemia (HoFH) is a severe inherited form of LDL-receptor failure, so the link to the original indication is close. This is an extension of existing use rather than a new mechanism. The key limitation is that statin benefit in HoFH depends on residual LDL receptor activity. In receptor-negative children, lovastatin 2 mg/kg/day produced no fall in LDL-C (PMID 3397806). In receptor-defective patients, combinations with cholestyramine and probucol gave partial responses (PMID 1785747).

Several other predictions are better supported. Hyperlipoproteinemia and heterozygous familial hypercholesterolemia fall within the already labelled lipid-lowering space and have direct lovastatin data. Three predictions (7alpha-hydroxylase deficiency, CETP deficiency, hepatic lipase deficiency) have little or no supporting evidence. CETP deficiency raises HDL-C and generally does not call for LDL-lowering therapy.

## Clinical Trial Evidence

**Homozygous familial hypercholesterolemia (top-ranked prediction)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label alirocumab in children and adolescents with HoFH. Does not test lovastatin, so it is background only. |

**Related predictions (lovastatin-relevant trials)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00116870](https://clinicaltrials.gov/study/NCT00116870) | Phase 2/3 | Completed | 270 | Double-blind, placebo-controlled angiographic study of lovastatin on coronary atherosclerosis progression in coronary heart disease patients |
| [NCT00345657](https://clinicaltrials.gov/study/NCT00345657) | Phase 4 | Completed | 100 | Extended-release niacin/lovastatin versus usual care for dyslipidemia in primary care. The contribution of lovastatin cannot be separated. |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Phase 3 | Completed | 153 | Alirocumab versus placebo in children with heterozygous FH. Does not test lovastatin. |
| [NCT01890967](https://clinicaltrials.gov/study/NCT01890967) | Phase 2 | Completed | 527 | Dose-ranging study of LY3015014 in primary hypercholesterolemia. Does not test lovastatin. |

## Literature Evidence

**Homozygous familial hypercholesterolemia**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3397806](https://pubmed.ncbi.nlm.nih.gov/3397806/) | 1988 | Clinical study (small) | J Pediatr | Three receptor-negative HoFH children on lovastatin showed no LDL-C reduction |
| [1785747](https://pubmed.ncbi.nlm.nih.gov/1785747/) | 1991 | Clinical study | An Esp Pediatr | Lovastatin with probucol and cholestyramine in two HoFH patients; LDL-receptor status related to response |
| [3534334](https://pubmed.ncbi.nlm.nih.gov/3534334/) | 1986 | Case report | JAMA | Lovastatin normalised cholesterol in a child with HoFH after liver transplantation |
| [2209665](https://pubmed.ncbi.nlm.nih.gov/2209665/) | 1990 | Case report | Eur J Pediatr | LDL apheresis with and without lovastatin in a 7-year-old girl with HoFH |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Ann N Y Acad Sci | Pharmacologic and surgical treatment of dyslipidemic children, including lovastatin |

**Related predictions (heterozygous FH and hyperlipoproteinemia)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9917116](https://pubmed.ncbi.nlm.nih.gov/9917116/) | 1999 | RCT | JAMA | Lovastatin in adolescent males with heterozygous FH |
| [16140708](https://pubmed.ncbi.nlm.nih.gov/16140708/) | 2005 | Clinical trial | Pediatrics | Lipid-lowering efficacy and safety of lovastatin in adolescent girls with heterozygous FH |
| [3662274](https://pubmed.ncbi.nlm.nih.gov/3662274/) | 1987 | Multicentre study | Ann Intern Med | Efficacy and tolerability of lovastatin in heterozygous FH |
| [1418102](https://pubmed.ncbi.nlm.nih.gov/1418102/) | 1992 | Randomised comparison | Atherosclerosis | Lovastatin versus simvastatin in heterozygous FH |
| [2044638](https://pubmed.ncbi.nlm.nih.gov/2044638/) | 1991 | Clinical study | Eur J Clin Pharmacol | Lovastatin more effective for LDL-C lowering than gemfibrozil in type 2a/2b hyperlipoproteinemia |
| [2182974](https://pubmed.ncbi.nlm.nih.gov/2182974/) | 1990 | Clinical study | Metabolism | Lovastatin and clofibrate in type III hyperlipoproteinemia (n=12); total cholesterol fell from 500 to 278 mg/dL on lovastatin |

## India Market Information

Lovastatin is marketed in India as single-ingredient oral tablets, with 20 valid registrations and no cancelled ones. Approved indication text is not recorded in the licence data. The main authorisations are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 123364 | Lovex 10mg Tablet (Lupin Ltd) | Strip of 10 tablets | Not recorded |
| Registration No. 14707 | Aztatin 20mg Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not recorded |
| Registration No. 126892 | Lovacard 20mg Tablet (Cipla Ltd) | Strip of 10 tablets | Not recorded |
| Registration No. 128055 | Lotin 20mg Tablet (Intas Pharmaceuticals Ltd) | Strip of 10 tablets | Not recorded |
| Registration No. 125084 | Lipistat 20mg Tablet (RPG Life Sciences Ltd) | Strip of 10 tablets | Not recorded |

## Safety Considerations

- **Drug Interactions**: 247 interactions were identified. The most important is **clarithromycin (Major)**, a CYP3A4 inhibitor. Moderate interactions include aprepitant, omeprazole and other proton pump inhibitors, metronidazole, cimetidine, clotrimazole, miconazole, rosuvastatin, simvastatin, eluxadoline, naltrexone, pectin and troglitazone. Minor or unclassified interactions include exenatide, calcitriol and glimepiride.
- **Conditions of concern (from the knowledge graph, not label text)**: liver disease, gallbladder disease, myopathy and other muscle disease, rhabdomyolysis, thrombocytopenia, diabetes and hyperglycaemia, gout, blood coagulation disease, peptic ulcer disease, and acute coronary syndrome or myocardial infarction.
- **Population-specific points**: for any paediatric use, pregnancy avoidance and age-appropriate dosing need attention. A published report links lovastatin and nicotinic acid with rhabdomyolysis (PMID 3421570), which is relevant to niacin combinations.

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold (for homozygous familial hypercholesterolemia, as a research question)**

**Rationale:**
- The top-ranked prediction has no lovastatin-specific trial. Its published evidence is limited to small, older studies and case reports, with a clear lack of effect in receptor-negative patients.
- Newer therapies such as PCSK9 inhibitors are being studied in HoFH, and lovastatin has no clear role as a standalone agent there.
- Hyperlipoproteinemia and heterozygous familial hypercholesterolemia (both L1) can proceed with guardrails, but they are largely on-label or near-label uses, not true repurposing. Guardrails include paediatric dosing, pregnancy avoidance and management of CYP3A4-related interactions.
- The 7alpha-hydroxylase deficiency, CETP deficiency and hepatic lipase deficiency predictions have no supporting evidence and should stay on hold.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Genotype- or receptor-stratified data on lovastatin response in HoFH
- A comparison against current HoFH standard of care (high-intensity statins plus ezetimibe, PCSK9 inhibitors, apheresis)
- A drug interaction and myopathy risk management plan for any new population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

