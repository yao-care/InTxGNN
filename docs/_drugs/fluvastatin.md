---
layout: default
title: Fluvastatin
parent: Model Prediction Only (L5)
nav_order: 375
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fluvastatin: predicted new indication Hyperlipoproteinemia (evidence level L5). Approved use: Arteriosclerosis disorder"
monitor_inn: "Fluvastatin"
predicted_indications: ["hyperlipoproteinemia", "homozygous familial hypercholesterolemia", "hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "familial hypercholesterolemia", "HIV infectious disease", "cholesterol-ester transfer protein deficiency", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "fibroma of prostate"]
---

# Fluvastatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Fluvastatin: From Atherosclerosis and Familial Combined Hyperlipidemia to Hyperlipoproteinemia

## One-Sentence Summary

Fluvastatin is a statin, originally used for atherosclerosis, arteriosclerosis and familial combined hyperlipidemia.
The TxGNN model predicts it may be effective for **hyperlipoproteinemia**, with **1 registered clinical trial** (which tests a different drug) and **20 publications** in the data compiled for this report. Most of the supporting publications are fluvastatin studies in related lipid disorders.
This is closer to an on-label or near-label use than to true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Arteriosclerosis disorder; atherosclerosis; familial combined hyperlipidemia (from the knowledge graph; the India licence records contain no indication text) |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (see note below) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* The only registered trial for this indication (NCT03510715) tests alirocumab, not fluvastatin. The L1 rating therefore rests on the fluvastatin literature, which includes a pediatric randomized trial and several combination-therapy trials. It does not rest on completed Phase 3 trials of fluvastatin for this exact indication.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, fluvastatin is an HMG-CoA reductase inhibitor. It reduces cholesterol synthesis in the liver and upregulates LDL receptors, which lowers LDL cholesterol and apolipoprotein B.

Atherosclerosis and hyperlipoproteinemia are closely linked, since raised lipoproteins drive atherosclerotic disease. The predicted indication shares the core lipid-lowering mechanism of the original indications. The prediction is therefore mechanistically sound, though it is better described as an on-label or near-label use than as repurposing.

Other predictions in the ranked list vary in strength:
- **Familial hypercholesterolemia (heterozygous):** Strong support. NCT00171236 is a completed Phase 3 fluvastatin trial in 84 children, and the literature includes high-dose and combination regimens.
- **Homozygous familial hypercholesterolemia:** Weak support. These patients have little or no residual LDL receptor function, so statin efficacy is expected to be limited. Evidence level is L4, and the decision is Research Question.
- **HIV infection:** Fluvastatin is mainly studied for antiretroviral-associated dyslipidemia, not for antiviral effect. Evidence level is L3, and the decision is Research Question.
- **Lower-ranked predictions** (for example CETP deficiency, 7-alpha-hydroxylase deficiency, animal retroviral diseases and prostate fibroma) have no trial or literature support and are rated Hold.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Alirocumab (a PCSK9 inhibitor) in children and adolescents with homozygous FH. It does not involve fluvastatin, so it is indirect evidence that only confirms the disease area. |

Trials for related predictions that bear on this assessment:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00171236](https://clinicaltrials.gov/study/NCT00171236) | Phase 3 | Completed | 84 | Fluvastatin in children with heterozygous familial hypercholesterolemia. Direct evidence for the drug in a related lipid disorder. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17062478](https://pubmed.ncbi.nlm.nih.gov/17062478/) | 2006 | RCT (pediatric) | Acta Paediatr | Fluvastatin in children and adolescents with heterozygous FH, assessing lipid profiles and vascular changes |
| [15598476](https://pubmed.ncbi.nlm.nih.gov/15598476/) | 2004 | RCT (12-month, double-blind) | Clin Ther | Fluvastatin plus fenofibrate vs fluvastatin alone in combined hyperlipidemia, type 2 diabetes and coronary heart disease |
| [10856536](https://pubmed.ncbi.nlm.nih.gov/10856536/) | 2000 | RCT (double-blind, n=333) | Atherosclerosis | FACT study: fluvastatin plus bezafibrate in coronary artery disease with mixed hyperlipidaemia |
| [11219479](https://pubmed.ncbi.nlm.nih.gov/11219479/) | 2001 | Randomized trial | Clin Ther | Fluvastatin 80 mg extended-release vs immediate-release in primary hypercholesterolemia |
| [8157036](https://pubmed.ncbi.nlm.nih.gov/8157036/) | 1993 | Double-blind clinical study | Eur J Clin Pharmacol | High-dose fluvastatin in 52 patients with familial hypercholesterolaemia |
| [10067240](https://pubmed.ncbi.nlm.nih.gov/10067240/) | 1998 | Clinical study | Ter Arkh | Variability of lipid-lowering effect of simvastatin and fluvastatin in primary hyperlipoproteinemia |
| [7604789](https://pubmed.ncbi.nlm.nih.gov/7604789/) | 1995 | Clinical study | Am J Cardiol | Fluvastatin effects on lipid profile and apolipoproteins in 31 Chinese patients with hypercholesterolemia |
| [7604807](https://pubmed.ncbi.nlm.nih.gov/7604807/) | 1995 | Open-label study | Am J Cardiol | Triple therapy (fluvastatin, bezafibrate, cholestyramine) in severe familial hypercholesterolemia |
| [8462180](https://pubmed.ncbi.nlm.nih.gov/8462180/) | 1993 | Review | Circulation | Review of drug treatment of dyslipoproteinemia, focusing on fluvastatin |
| [11347136](https://pubmed.ncbi.nlm.nih.gov/11347136/) | 2001 | Review | Nihon Rinsho | Review of fluvastatin (no abstract available) |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 123431 | Lescol XL 80mg Tablet (Novartis India Ltd) | Strip of 14 tablets | Not stated in the registration record |
| 85524 | Fluvalip 40mg Tablet (Nectazen Pharmaceuticals) | Strip of 10 tablets | Not stated in the registration record |

Both registrations are valid single-ingredient oral products.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (these are graph associations, not package-insert text): liver disease, gallbladder disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, hypotensive disorder, substance abuse/dependence, rhabdomyolysis, nodular fasciitis and injury.

**Drug Interactions:** The data records 159 interactions. Those listed as Moderate include:
- Other statins (rosuvastatin, simvastatin)
- Glyburide
- Nateglinide
- Metronidazole
- Tinidazole
- Aprepitant
- Naltrexone
- Nitisinone
- Oxandrolone
- Pectin

Other entries have an unrated level, for example aspirin, cimetidine, famotidine, pantoprazole, doxycycline and calcitriol.

Please refer to the package insert for the full warnings and contraindications, which were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Fluvastatin's lipid-lowering mechanism directly matches hyperlipoproteinemia, and the fluvastatin literature includes randomized trials in related disorders. However, the only registered trial for this exact indication tests a different drug. The strongest direct evidence (NCT00171236) is in heterozygous FH. The package-insert safety review is also incomplete.

**To proceed, the following is needed:**
- Package-insert warnings and contraindications from the India product labels (a blocking data gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the approved indication text for the India registrations
- A DDI management plan, particularly for combination use with other lipid-lowering agents
- Pediatric dosing and monitoring guidance if pediatric use is considered
- Muscle and liver monitoring, given the knowledge-graph contraindication signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

