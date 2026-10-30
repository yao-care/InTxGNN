---
layout: default
title: Rosuvastatin
parent: Model Prediction Only (L5)
nav_order: 755
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-30
monitor_inn: "Rosuvastatin"
predicted_indications: ["cholesterol-ester transfer protein deficiency", "brain stem infarction", "HIV infectious disease", "hypoalphalipoproteinemia", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "ABri amyloidosis"]
description: "Rosuvastatin: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Rosuvastatin
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

## Rosuvastatin: Cholesterol-ester transfer protein deficiency
{: .text-alpha }

## One-Sentence Summary

Rosuvastatin is a statin (HMG-CoA reductase inhibitor) originally used for hypertriglyceridemia, hyperlipoproteinemia, atherosclerosis, stroke-related disorders and homozygous familial hypercholesterolemia.
The top-ranked prediction is **cholesterol-ester transfer protein deficiency**, which has no registered clinical trials.
The only genuinely novel prediction with a body of evidence is **HIV infectious disease** (a research question, not a recommendation).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9954 |
| Evidence Level | L5 for rank 1; L1 for Familial Hypercholesterolemia |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | 20 |
| Recommended Decision | Hold for rank 1; Proceed with Guardrails for Familial Hypercholesterolemia |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, rosuvastatin is a statin that inhibits HMG-CoA reductase, reducing hepatic cholesterol synthesis and upregulating LDL receptors, which lowers LDL-C and triglycerides.

**Rank 1 (cholesterol-ester transfer protein deficiency):** This is a model prediction only, with no trials or publications. CETP deficiency raises HDL-C and alters lipoprotein metabolism, and no direct mechanistic or clinical link to rosuvastatin is documented. It should be treated as a hypothesis.

**Familial hypercholesterolemia:** The LDL clearance deficit in this condition is directly addressed by statin-induced LDL receptor upregulation. Homozygous familial hypercholesterolemia is already among the original indications, so this is mostly an established use. Guardrails: pediatric dosing, monitoring for myopathy and liver enzymes, and limited response in homozygous patients with null LDLR variants, who often need add-on therapy.

**Other predictions in the list:**
- **Hyperlipidemia**: an established use, with large Phase 3 programmes.
- **HIV infectious disease** (rank 5, L2): the rationale is lipid-lowering and anti-inflammatory effects reducing cardiovascular risk in people with HIV. The trials mostly address surrogate cardiovascular endpoints and drug interactions with antiretrovirals, not HIV itself, and results are mixed.
- **Brain stem infarction, hypoalphalipoproteinemia, CYP7A1-deficiency hypercholesterolemia:** only indirect or preclinical support.
- **Hepatic lipase deficiency hyperlipidemia, ABri amyloidosis, a rare neurodevelopmental disorder:** prediction only, no evidence.

---

## Clinical Trial Evidence

Shown as a known use (up to 10 most relevant trials). The rank 1 prediction, CETP deficiency, has no registered clinical trials.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00355615](https://clinicaltrials.gov/study/NCT00355615) | Phase 3 | Completed | 173 | Rosuvastatin vs placebo for 12 weeks, then 40 weeks open label, in children aged 10–17 with heterozygous FH; primary endpoint LDL-C reduction |
| [NCT01078675](https://clinicaltrials.gov/study/NCT01078675) | Phase 3 | Completed | 315 | Open-label 2-year efficacy, safety and pharmacokinetic study in children and adolescents (6 to <18 years) with FH |
| [NCT02226198](https://clinicaltrials.gov/study/NCT02226198) | Phase 3 | Completed | 20 | Double-blind, placebo-controlled crossover study in children and adolescents with homozygous FH |
| [NCT02434497](https://clinicaltrials.gov/study/NCT02434497) | Phase 3 | Completed | 9 | Open-label extension evaluating long-term safety in paediatric homozygous FH |
| [NCT00654602](https://clinicaltrials.gov/study/NCT00654602) | Phase 3 | Completed | 1500 | 48-week open-label study of efficacy and safety in Fredrickson type IIa/IIb dyslipidaemia, including heterozygous FH |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Completed | 442 | Renal effects of rosuvastatin vs simvastatin in type IIa/IIb dyslipidaemia, including heterozygous FH |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Completed | 249 | Alirocumab vs placebo in heterozygous FH on lipid-modifying therapy; rosuvastatin's role (background therapy or test drug) is unclear |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Phase 3 | Completed | 153 | Alirocumab in children with heterozygous FH on stable statin therapy; rosuvastatin's role is unclear |
| [NCT06910098](https://clinicaltrials.gov/study/NCT06910098) | N/A | Completed | 195 | Effect of different rosuvastatin doses on LDL, CPK and AST levels |
| [NCT07474649](https://clinicaltrials.gov/study/NCT07474649) | Phase 3 | Not yet recruiting | 103 | Bempedoic acid/ezetimibe plus high-intensity atorvastatin or rosuvastatin on coronary plaque; no results yet |

---

## Literature Evidence

Shown for Familial Hypercholesterolemia (up to 10 most relevant, RCTs first).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20223367](https://pubmed.ncbi.nlm.nih.gov/20223367/) | 2010 | RCT | J Am Coll Cardiol | Efficacy and safety of rosuvastatin in children with familial hypercholesterolemia |
| [28838366](https://pubmed.ncbi.nlm.nih.gov/28838366/) | 2017 | Cohort | J Am Coll Cardiol | Rosuvastatin efficacy in children with homozygous FH and its association with underlying genetic mutations |
| [26387811](https://pubmed.ncbi.nlm.nih.gov/26387811/) | 2016 | Pharmacokinetic study | Eur J Clin Pharmacol | Population pharmacokinetics of rosuvastatin in paediatric heterozygous FH |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | Rosuvastatin was superior to atorvastatin, simvastatin and pravastatin in improving lipid profile in hypercholesterolaemia across 6–52 week trials; low propensity for drug interactions |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | Rosuvastatin in the management of hyperlipidemia, including homozygous FH |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guidelines for dyslipidemia management and cardiovascular prevention |
| [36928267](https://pubmed.ncbi.nlm.nih.gov/36928267/) | 2023 | Cohort | J Atheroscler Thromb | Real-world LDL-C goal achievement in high-risk patients in Japan |
| [40254247](https://pubmed.ncbi.nlm.nih.gov/40254247/) | 2025 | Mechanistic study | Toxicology | Statin myotoxicity in iPSC-derived muscle cells from FH patients, comparing lipophilic and hydrophilic statins |
| [20531065](https://pubmed.ncbi.nlm.nih.gov/20531065/) | 2010 | Case report | South Med J | Rare severe thrombocytopenia during rosuvastatin treatment |
| [33976097](https://pubmed.ncbi.nlm.nih.gov/33976097/) | 2021 | Review | Med Lett Drugs Ther | Evinacumab for homozygous FH |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 191412 | Rosutime 10mg Tablet (TTK Healthcare Ltd) | Strip of 10 tablets | Not specified |
| 193515 | Rosmi 5mg Tablet (Cadila Pharmaceuticals Ltd) | Strip of 10 tablets | Not specified |
| 36307 | Crevast 20 Tablet (Eris Lifesciences Ltd) | Strip of 15 tablets | Not specified |
| 184168 | Rosuvas 20 Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not specified |
| 185654 | Rosave CV 20mg/75mg Capsule (Alembic Pharmaceuticals Ltd) | Strip of 10 capsules | Not specified |

All 20 registrations are valid. Several products carry rosuvastatin in combination with other agents (for example, the "CV" capsules), although the data classify all 20 as single-ingredient licences.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not from label text): liver disease, gallbladder disease, hypothyroidism, myxedema, congenital hypothyroidism, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, substance abuse/dependence, rhabdomyolysis, nodular fasciitis, injury, proteinuria.
- **Drug Interactions:** 524 interactions are recorded. Major-level examples include **fenofibrate** and **atazanavir**. Moderate-level examples include atorvastatin, ezetimibe, bempedoic acid, amiodarone, paclitaxel, zidovudine, adalimumab, trastuzumab emtansine, alpelisib, apalutamide, asparaginase, auranofin, ethanol and sodium citrate. Minor-level examples include levonorgestrel, norethisterone and desogestrel.
- **Literature signals:** rare thrombocytopenia (case report), statin-associated incident diabetes, worsened insulin resistance in HIV-infected adults on rosuvastatin, and statin-associated muscle symptoms.

The package-insert warnings and contraindications for the Indian products have not been obtained. Please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold (CETP deficiency, the top-ranked prediction, and the other low-evidence predictions)**

**Rationale:**
- The top-scored prediction, cholesterol-ester transfer protein deficiency (0.9954), has no trials or literature and rests on the model score alone.
- HIV infectious disease (L2) is worth investigating as a research question, but the evidence is mostly surrogate and mixed.

**To proceed, the following is needed:**
- Package-insert warnings and contraindications from the Indian regulatory source (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for the Indian licences
- Paediatric dosing guidance, and a myopathy and liver-enzyme monitoring plan
- A review of the major drug interactions (fenofibrate, atazanavir) and dose adjustment in renal impairment and in Asian patients
- Any further evaluation of the HIV indication should focus on clinical outcomes rather than lipid or inflammatory surrogates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

