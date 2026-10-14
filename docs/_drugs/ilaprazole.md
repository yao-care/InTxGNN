---
layout: default
title: Ilaprazole
parent: High Evidence (L1-L2)
nav_order: 423
evidence_level: L1
indication_count: 5
---

# Ilaprazole
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **5** 
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

# Ilaprazole: From Peptic Ulcer Disease to Active Peptic Ulcer Disease

## One-Sentence Summary

Ilaprazole is a proton pump inhibitor originally used for peptic ulcer disease, gastroesophageal reflux disease and esophagitis.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, which is closely related to its existing use, with **2 clinical trials** and **6 publications** directly linked to this prediction.
Because peptic ulcer disease is already an original indication, this is largely an on-label use rather than true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, gastroesophageal reflux disease, esophagitis, peptic esophagitis |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L1 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Ilaprazole inhibits the H+/K+ ATPase (the gastric proton pump, encoded by ATP4A) in parietal cells. This suppresses gastric acid secretion, and pharmacology data compiled for this report indicate it does so more potently than omeprazole. Detailed mechanism of action data is otherwise not available in the compiled data.

Peptic ulcers are acid-driven, so lowering gastric acid promotes healing. Active peptic ulcer disease is a direct extension of the drug's original peptic ulcer indication, and the mechanism applies directly.

Other predictions are weaker. For gastric ulcer (score 99.58%), evidence is strong, with several completed Phase 3 trials, but much of it comes from duodenal ulcer populations. For gastrojejunal ulcer, gastroduodenitis and peptic ulcer perforation, the support is only indirect or absent, and these remain research questions.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Ilaprazole vs pantoprazole triple therapy for H. pylori eradication in gastric and/or duodenal ulcer patients (7 days) |
| [NCT06284876](https://clinicaltrials.gov/study/NCT06284876) | Phase 3 | Recruiting | 416 | Non-inferiority of ilaprazole 10 mg vs active control in preventing NSAID-associated peptic ulcer at Week 24; results not yet available |

Further trials, mostly in duodenal ulcer and gastric ulcer (for example NCT00952978, Phase 3, n=496, vs omeprazole), support the broader ulcer indication.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22070512](https://pubmed.ncbi.nlm.nih.gov/22070512/) | 2012 | RCT | Curr Med Res Opin | Phase III trial of ilaprazole 10 mg/d vs omeprazole 20 mg/d in duodenal ulcer |
| [30789856](https://pubmed.ncbi.nlm.nih.gov/30789856/) | 2019 | RCT | J Clin Gastroenterol | Ilaprazole vs rabeprazole in duodenal ulcer; dose-effect relationship |
| [20679904](https://pubmed.ncbi.nlm.nih.gov/20679904/) | 2011 | RCT | J Clin Gastroenterol | Ilaprazole vs omeprazole in duodenal ulcer; efficacy, safety and dose-response |
| [19434360](https://pubmed.ncbi.nlm.nih.gov/19434360/) | 2009 | RCT | J Gastroenterol | Ulcer-healing effects of ilaprazole vs omeprazole in gastric and duodenal ulcers |
| [27605258](https://pubmed.ncbi.nlm.nih.gov/27605258/) | 2016 | RCT | Clin Drug Investig | Ilaprazole vs active control in reflux esophagitis |
| [24801687](https://pubmed.ncbi.nlm.nih.gov/24801687/) | 2014 | Preclinical (animal) | Dig Dis Sci | Intravenous ilaprazole more potent than oral against gastric lesions in rats |

## India Market Information

Twenty valid single-ingredient registrations are listed; five are shown below. The data compiled for this report contain no approved indication text for these products.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 108413 | Iladif 10mg Tablet | Strip of 10 tablets | Overseas Healthcare Pvt Ltd |
| 15005 | Ambila 10mg Tablet | Strip of 10 tablets | Ambience Pharma |
| 107991 | Iladac 10 Tablet | Strip of 10 tablets | Zydus Cadila |
| 108021 | Ilapro 10 Tablet | Strip of 10 tablets | Ajanta Pharma Ltd |
| 110365 | Ilabest 10mg Tablet | Strip of 10 tablets | Lupin Ltd |

All products are oral tablets.

## Safety Considerations

- **Drug Interactions**: The only interaction record is its pharmacological target, ATP4A (the gastric proton pump), which is the intended mechanism rather than a clinical drug-drug interaction. No clinically relevant drug interactions are listed in the data.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several randomized Phase 3 trials and RCTs support ilaprazole in ulcer healing, and peptic ulcer disease is already an original indication with 20 registrations in India. The "guardrails" are needed because the package insert safety data are missing, and much of the evidence comes from duodenal ulcer populations rather than the exact predicted condition.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India product labels (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Results from the ongoing NSAID-associated ulcer prevention trial (NCT06284876)
- Approved indication text for the Indian registrations, to confirm label coverage
- For the lower-ranked predictions (gastrojejunal ulcer, gastroduodenitis, peptic ulcer perforation): direct clinical evidence before any consideration; they currently stay at Research Question or Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

