---
layout: default
title: Simvastatin
parent: Model Prediction Only (L5)
nav_order: 774
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-30
monitor_inn: "Simvastatin"
predicted_indications: ["brain stem infarction", "cholesterol-ester transfer protein deficiency", "HIV infectious disease", "ABri amyloidosis", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
description: "Simvastatin: predicted new indication Brain stem infarction (evidence level L5). Approved use: Not recorded in the local data"
---

# Simvastatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Simvastatin: Brain stem infarction
{: .text-alpha }

## One-Sentence Summary

Simvastatin is a statin originally used to treat lipid disorders (such as hypertriglyceridaemia, hyperlipoproteinaemia and homozygous familial hypercholesterolaemia) and atherosclerotic and cerebrovascular disease.
The TxGNN model predicts it may be effective for **familial hypercholesterolaemia**, with **9 clinical trials** and **20 publications** currently supporting this direction.
This indication substantially overlaps with simvastatin's existing lipid-lowering uses, so it is closer to an on-label or extended-label use than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Brain stem infarction |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | 20 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Simvastatin inhibits HMG-CoA reductase, the rate-limiting enzyme of hepatic cholesterol synthesis. Lower intracellular cholesterol upregulates LDL receptors on liver cells, which increases clearance of LDL cholesterol from the blood. This is the established mechanism for LDL-C lowering in familial hypercholesterolaemia. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description relies on the known pharmacology of the statin class.

Familial hypercholesterolaemia is an inherited condition that causes very high LDL-C and premature coronary disease. The drug's original indications already include lipid disorders and atherosclerosis, including homozygous familial hypercholesterolaemia. The predicted indication is therefore a close extension of existing use.

Statin monotherapy is often not enough in these patients, because response depends on residual LDL-receptor function. Combination therapy, such as simvastatin with ezetimibe, is common in the trials listed below.

---

## Clinical Trial Evidence

Several trials list simvastatin only as background therapy. Only the two trials marked "direct" below test a simvastatin-containing regimen head-to-head.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE: ezetimibe plus high-dose simvastatin vs simvastatin alone on carotid atherosclerosis progression in heterozygous FH (direct) |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Completed | 248 | Ezetimibe co-administered with simvastatin vs simvastatin alone in adolescents with heterozygous FH (direct) |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe added to atorvastatin or simvastatin in homozygous FH; simvastatin is background therapy |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | Long-term open-label safety of ezetimibe added to atorvastatin or simvastatin in homozygous FH |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Completed | 249 | Alirocumab vs placebo in heterozygous FH on lipid-modifying therapy; simvastatin likely background |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Phase 3 | Completed | 153 | Alirocumab vs placebo in children and adolescents with heterozygous FH; indirect evidence |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Completed | 442 | Renal effects of rosuvastatin vs simvastatin over 6 weeks in type IIa/IIb dyslipidaemia, including heterozygous FH |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label alirocumab in children with homozygous FH; simvastatin is not the investigational agent |
| [NCT01890967](https://clinicaltrials.gov/study/NCT01890967) | Phase 2 | Completed | 527 | Dose-ranging of a PCSK9 antibody (LY3015014) in primary hypercholesterolaemia; statins are background |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | Clinical trial (ENHANCE) | N Engl J Med | Simvastatin with or without ezetimibe in familial hypercholesterolaemia, assessing atherosclerosis progression |
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Systematic review | Cochrane Database Syst Rev | Statins for children with familial hypercholesterolaemia |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematic review | Cochrane Database Syst Rev | Updated Cochrane review of statins in children with FH |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Saf | Benefits and risks of simvastatin in familial hypercholesterolaemia |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opin Drug Saf | Benefit-risk assessment of simvastatin in FH |
| [41824590](https://pubmed.ncbi.nlm.nih.gov/41824590/) | 2026 | Guideline | J Am Coll Cardiol | 2026 ACC/AHA multisociety dyslipidaemia management guideline |
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Guideline | Circulation | Same 2026 ACC/AHA guideline, published in a second journal |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guidelines for dyslipidaemia and cardiovascular prevention |
| [9666952](https://pubmed.ncbi.nlm.nih.gov/9666952/) | 1998 | Clinical trial | QJM | High-dose atorvastatin compared with simvastatin-fenofibrate and simvastatin-cholestyramine in 54 patients with severe heterozygous FH |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Cross-sectional study | J Clin Med | Simvastatin 10 mg and cellular immunity in 26 children with FH |

---

## India Market Information

Twenty valid single-ingredient registrations are listed. The licence records carry no approved-indication text. Five representative entries:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 248009 | Zocor 10mg Tablet (MSD Pharmaceuticals) | Strip of 15 tablets | Not specified in the data |
| 204716 | Simlip 20mg Tablet (Cipla) | Strip of 10 tablets | Not specified in the data |
| 204665 | Starstat 40mg Tablet (Lupin) | Strip of 10 tablets | Not specified in the data |
| 234458 | Vastatin 20mg Tablet (Aurobindo Pharma) | Strip of 10 tablets | Not specified in the data |
| 200277 | Simvotin 10 Tablet (Sun Pharmaceutical) | Strip of 10 tablets | Not specified in the data |

---

## Safety Considerations

- **Contraindications (knowledge-graph data, not label text)**: the knowledge graph links simvastatin to contraindications in the following areas:
  - Muscle: myopathy, muscular disease, rhabdomyolysis
  - Liver and biliary: liver disease, gallbladder disease, pancreatitis
  - Metabolic: diabetes mellitus, hyperglycaemia, diabetic ketoacidosis, gout
  - Blood and circulation: thrombocytopenia, blood coagulation disease, hypotensive disorder
  - Cardiac: acute coronary syndrome, coronary artery disease, myocardial infarction
  - Others: peptic ulcer disease, substance abuse or dependence, hypophosphataemia
  These are model-derived associations and need confirmation against the product label.
- **Drug Interactions**: 696 interactions were recorded. Major-level ones include **amiodarone**, **amlodipine** and **fenofibrate**. Moderate-level ones include zidovudine, paclitaxel, nifedipine, omeprazole, aprepitant and ethanol. Strong CYP3A4 inhibitors, including HIV protease inhibitors and cobicistat, greatly raise simvastatin exposure and the risk of myopathy and rhabdomyolysis.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two directly relevant Phase 3 trials (ENHANCE and the adolescent ezetimibe-plus-simvastatin study) and several systematic reviews and guidelines support simvastatin in familial hypercholesterolaemia. The indication overlaps with existing lipid-lowering uses, and the drug is widely marketed in India. Most listed trials use simvastatin as background therapy, so its specific contribution is often indirect.

**To proceed, the following is needed:**
- India package insert warnings and contraindications, which are currently missing and block formal safety screening
- Detailed mechanism-of-action data from DrugBank
- Confirmation of the approved indication wording on Indian licences
- A monitoring plan for myopathy, liver function and interacting co-medications, especially in children and adolescents

---

### Other Predicted Indications (Brief Note)

| Predicted Indication | Evidence Level | Decision | Comment |
|------|------|------|------|
| Hypercholesterolaemia, autosomal dominant | L1 | Proceed with Guardrails | Overlaps substantially with familial hypercholesterolaemia and shares the same trials |
| HIV infectious disease | L3 | Research Question | Relevant to managing antiretroviral-associated dyslipidaemia and drug interactions, not to treating HIV; one pilot study found no anti-HIV activity |
| Brain stem infarction | L5 | Hold | No simvastatin-specific evidence |
| CETP deficiency; CYP7A1-deficiency hypercholesterolaemia; ABri amyloidosis; neurodevelopmental disorder with ataxic gait | L5 | Hold | Model prediction only, no trials or publications |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

