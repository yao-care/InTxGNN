---
layout: default
title: Gemfibrozil
parent: Moderate Evidence (L3-L4)
nav_order: 389
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-28
description: "Gemfibrozil: predicted new indication Rheumatoid arthritis (evidence level L4). Approved use: Hypertriglyceridemia"
monitor_inn: "Gemfibrozil"
predicted_indications: ["rheumatoid arthritis", "multiple endocrine neoplasia", "HIV infectious disease", "hypoalphalipoproteinemia", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "methemoglobinemia, alpha type", "sclerosing cholangitis", "methemoglobin reductase deficiency"]
---

# Gemfibrozil
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **9** 
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

## Gemfibrozil: From Hypertriglyceridemia to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Gemfibrozil is a PPAR-alpha agonist originally used to treat hypertriglyceridemia.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but the support so far consists only of **animal and related-drug preclinical studies**, with **no registered clinical trials**.
Other predicted indications (HIV-associated lipid disorders and hypoalphalipoproteinemia) have considerably stronger evidence and are noted below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertriglyceridemia |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L4 |
| India Market Status | Marketed (valid licences: 8 of 8) |
| Number of Registrations | 8 (valid: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Gemfibrozil activates PPAR-alpha, a nuclear receptor that regulates fat metabolism. This is how it lowers triglycerides and raises HDL cholesterol. PPAR signalling also has anti-inflammatory and immune-modulating effects, including influence on T-cell and cytokine pathways. These are processes involved in rheumatoid arthritis. Detailed mechanism-of-action data were not available in the data compiled for this report, so this link rests on the known pharmacology of the drug class.

Direct evidence is thin. A rat study (2019) found that gemfibrozil combined with a reduced steroid dose gave a similar outcome to the full steroid dose in adjuvant-induced arthritis. A 2026 animal study with bezafibrate, a related pan-PPAR agonist, reported reduced experimental arthritis through PPAR-dependent pathways. Neither is human data, and the original lipid indication is only indirectly related to joint inflammation.

## Clinical Trial Evidence

Currently no related clinical trials registered for rheumatoid arthritis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | Preclinical (rat model) | Modern Rheumatology | Gemfibrozil plus reduced-dose prednisolone gave a similar picture to full-dose steroid in adjuvant-induced arthritis |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | Preclinical (related drug) | International Immunopharmacology | Bezafibrate, a pan-PPAR agonist, attenuated experimental arthritis via PPAR-dependent pathways |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | Preclinical (mechanistic) | Journal of Immunology | Nitric oxide and Foxp3 regulation in T cells; background on immune mechanisms |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 168871 | Oxipace 300mg Tablet | Strip of 10 tablets | Not specified |
| 121328 | Lopid Capsule | Strip of 10 capsules | Not specified |
| 97053 | Gempar 300mg Capsule | Strip of 10 capsules | Not specified |
| 194412 | Regulipid Tablet | Strip of 30 tablets | Not specified |
| 221144 | Triglyd 600mg Tablet | Strip of 10 tablets | Not specified |

Eight valid single-ingredient registrations exist in total.

## Safety Considerations

- **Contraindications (not from label text; the TxGNN model (deep learning) may reflect similarities it learned between related diseases, not biological evidence)**: liver disease, gallbladder disease, cholelithiasis and related biliary stone conditions, primary biliary cholangitis, impaired renal function, thrombocytopenia, leukopenia, anaemia (including macrocytic anaemia).
- **Drug Interactions**: 129 interactions were identified. Major ones include:
  - Statins: rosuvastatin and simvastatin
  - Antidiabetic agents: pioglitazone and repaglinide
  - Antidiarrhoeals: loperamide and eluxadoline
  - Moderate interactions include insulins, nateglinide, rosiglitazone, chlorpropamide, tolazamide, rifaximin and chenodeoxycholic acid.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by human evidence. There are no registered trials, and the literature is limited to animal studies and a related-drug study. The mechanistic link is plausible but unproven.

**To proceed, the following is needed:**
- Controlled preclinical confirmation with gemfibrozil itself, and any early-phase human data in rheumatoid arthritis
- Detailed mechanism-of-action data
- Package insert warnings and contraindications from the Indian market
- A drug-interaction plan, since rheumatoid arthritis patients commonly take multiple medications

---

## Other Predicted Indications (Supplementary)

| Rank | Predicted Indication | Score | Evidence Level | Decision | Notes |
|---|---|---|---|---|---|
| 3 | HIV infectious disease | 0.9980 | L2 | Research Question | Supports managing protease-inhibitor-associated hypertriglyceridaemia, not treating HIV itself. Includes a randomized double-blind study ([PMID 12409741](https://pubmed.ncbi.nlm.nih.gov/12409741/)) and a comparative effectiveness study ([PMID 23892238](https://pubmed.ncbi.nlm.nih.gov/23892238/)). One Phase 1 trial ([NCT00039663](https://clinicaltrials.gov/study/NCT00039663)) was low relevance. Interaction risk with statins and antiretrovirals requires guardrails. |
| 4 | Hypoalphalipoproteinemia (low HDL) | 0.9977 | L3 | Proceed with Guardrails | Several small, older crossover and comparison studies (1989–2000) showing lipoprotein changes. Mostly surrogate endpoints. No registered trials. |
| 9 | Sclerosing cholangitis | 0.9970 | L5 | Hold | Literature covers fibrate safety in cholestatic disease, not efficacy. Hepatotoxicity concern. |
| 2, 5, 6, 7, 10 | Multiple endocrine neoplasia; brachydactyly-syndactyly syndrome; colobomatous microphthalmia-rhizomelic dysplasia syndrome; methemoglobinemia, alpha type; methemoglobin reductase deficiency | 99.70–0.9983 | L5 | Hold | No clinical or literature evidence and no plausible mechanistic link. Computational prediction only. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

