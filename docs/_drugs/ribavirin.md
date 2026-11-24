---
layout: default
title: Ribavirin
parent: High Evidence (L1-L2)
nav_order: 736
evidence_level: L1
indication_count: 9
monitor_inn: "Ribavirin"
predicted_indications: ["chronic hepatitis B virus infection", "hepatoportal sclerosis", "primitive portal vein thrombosis", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "hepatic porphyria", "IgG4-related pachymeningitis", "IgG4-related mediastinitis", "eosinophilic angiocentric fibrosis"]
last_modified_at: 2026-11-24
description: "Ribavirin: predicted new indication Chronic hepatitis B virus infection (evidence level L1). Approved use: Chronic hepatitis C virus infection"
---

# Ribavirin
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **9** 
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

## Ribavirin: From Chronic Hepatitis C Virus Infection to Chronic Hepatitis B Virus Infection
{: .text-alpha }

## One-Sentence Summary

Ribavirin is an oral antiviral nucleoside analogue. Chronic hepatitis C, hepatitis C and respiratory syncytial virus infection are listed as its known uses.
The TxGNN model predicts it may be effective for **chronic hepatitis B virus infection**.
The data compiled for this report include **15 clinical trials** and **20 publications**. Only a few trials test ribavirin in hepatitis B directly, and in those it is given together with peginterferon, so ribavirin's own contribution cannot be separated.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus infection (relation recorded in the knowledge graph; the local licence records contain no indication text) |
| Predicted New Indication | Chronic hepatitis B virus infection |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L1 (see note below) |
| India Market Status | Listed in a compiled Indian medicine price dataset (20 of 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | 20 (valid: 20) |
| Recommended Decision | Hold |

**Note on evidence level:** One completed Phase 3 trial directly studies hepatitis B (NCT00114361). A second Phase 2/3 pilot is also completed (NCT00275938). Both test ribavirin only as an add-on to interferon, so the evidence is weaker than "L1" suggests. The Phase 3 criterion for L1 is formally met only by one trial in hepatitis B, so I rate this **L2**: one completed Phase 3 trial that directly studies the predicted disease, with the caveats above.

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for ribavirin: "Ribavirin is an antiviral drug. […] The mechanism by which ribavirin contributes to its antiviral efficacy in the clinic is not fully understood. Ribavirin has direct antiviral activity in tissue culture against many RNA viruses. Ribavirin increases the mutation frequency in the genomes of several RNA viruses and ribavirin triphosphate inhibits HCV polymerase in a biochemical reaction." ([DailyMed: ribavirin prescribing information, Aurobindo Pharma Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eee304d0-c2ea-44f4-97d9-92a414d31b6c), label version 2024-02-06; accessed 2026-11-19.) Ribavirin is a nucleoside analogue with broad antiviral activity, generally described as depleting intracellular guanosine pools and modulating immune responses. Its efficacy in hepatitis C, always combined with interferon, is well established.

Hepatitis B and hepatitis C are both chronic viral liver infections. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Mechanistically, the link is weak. Hepatitis B is a DNA virus that replicates through reverse transcription, and ribavirin has no meaningful direct activity against it. Any benefit seen in hepatitis B trials is more plausibly due to the peginterferon partner or to immune modulation. Much of the literature concerns patients co-infected with hepatitis C and B, where ribavirin acts on the hepatitis C component.

## Clinical Trial Evidence

Of the 15 trials retrieved, most are hepatitis C studies with weak relevance to hepatitis B. The most relevant ones are listed first.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00114361](https://clinicaltrials.gov/study/NCT00114361) | Phase 3 | Completed | 138 | Peginterferon alfa-2a plus ribavirin vs peginterferon alone in HBeAg-negative chronic hepatitis B. This is the most direct test, but results are not summarized in the data compiled. |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Phase 2/3 | Completed | 120 | Pilot of interferon alpha-2b plus ribavirin in chronic hepatitis B. |
| [NCT03759782](https://clinicaltrials.gov/study/NCT03759782) | Phase 3 | Unknown | 24 | Ribavirin added to standard nucleoside analogue therapy for hepatitis B to exploit its immune-modulating properties (pilot). |
| [NCT00154869](https://clinicaltrials.gov/study/NCT00154869) | Phase 3 | Unknown | 320 | Peginterferon plus ribavirin in hepatitis C/B co-infection. |
| [NCT00117533](https://clinicaltrials.gov/study/NCT00117533) | Phase 4 | Unknown | 20 | Pegylated interferon alfa-2b plus ribavirin in dual hepatitis B and D infection (pilot). |
| [NCT01447420](https://clinicaltrials.gov/study/NCT01447420) | Phase 4 | Completed | 129 | Peginterferon plus ribavirin and IL-28B expression in hepatitis C genotype 1. Hepatitis C study. |
| [NCT01195181](https://clinicaltrials.gov/study/NCT01195181) | Phase 4 | Completed | 506 | Surveillance and care-improvement project for chronic hepatitis C. |
| [NCT02219477](https://clinicaltrials.gov/study/NCT02219477) | Phase 3 | Completed | 36 | Direct-acting antiviral regimen plus ribavirin in hepatitis C with decompensated cirrhosis. Hepatitis C study. |
| [NCT01425970](https://clinicaltrials.gov/study/NCT01425970) | Phase 2 | Terminated | 210 | INX-08189 with peginterferon and ribavirin in hepatitis C. Hepatitis C study. |
| [NCT01795911](https://clinicaltrials.gov/study/NCT01795911) | Phase 2 | Completed | 165 | Peginterferon lambda plus ribavirin in hepatitis C. Ribavirin is background therapy. |

## Literature Evidence

No randomized trial or primary study of ribavirin in hepatitis B appears in the retrieved literature. Almost all publications are reviews of hepatitis B and C together.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | Hepatitis C/B co-infection; peginterferon plus ribavirin was recommended for co-infected patients with detectable hepatitis C RNA. |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | Treatment and outcomes of dual hepatitis C and B infection. |
| [16838649](https://pubmed.ncbi.nlm.nih.gov/16838649/) | 2006 | Review | Nihon Rinsho | Hepatitis C/B co-infection; peginterferon alpha-2b plus ribavirin is the most effective initial therapy for hepatitis C. |
| [25048716](https://pubmed.ncbi.nlm.nih.gov/25048716/) | 2015 | Review | Hepatology | Immunological aspects of antiviral therapy in hepatitis B and C. |
| [26284971](https://pubmed.ncbi.nlm.nih.gov/26284971/) | 2015 | Review | Curr Opin Virol | Effect of IL28B genotype on hepatitis B and C. |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | Review | World J Gastroenterol | IL28B polymorphism and hepatitis B infection outcomes. |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Review | Expert Rev Anti Infect Ther | Treatment options for chronic hepatitis B and C in children. |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | Review | Annu Rev Med | Treatment strategies for chronic hepatitis B and C. |

## India Market Information

All 20 records are single-ingredient ribavirin products with valid status; the compiled data contain no approved-indication text. The list is complete (20 of 20).

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 100600 | Gatorib 200mg Tablet | Strip of 10 tablets | Valid |
| 104577 | Heptos 200mg Capsule | Strip of 10 capsules | Valid |
| 105204 | Heplovir Capsule | Bottle of 40 capsules | Valid |
| 185023 | Ribasure Capsule | Bottle of 140 capsules | Valid |
| 185221 | Ribavin 200 Capsule | Strip of 4 capsules | Valid |
| 186659 | Ribahep Capsule | Strip of 10 capsules | Valid |
| 186691 | Rebetol 200mg Capsule | Strip of 12 capsules | Valid |
| 187128 | Ribavin 100mg Capsule | Strip of 4 capsules | Valid |
| 187852 | Ribavin 50mg Syrup | Bottle of 30 ml Syrup | Valid |
| 189039 | Ribnoid 200 Capsule | Strip of 10 capsules | Valid |
| 189644 | Rinhib 200mg Capsule | Bottle of 42 capsules | Valid |
| 190355 | Ribnoid 200 Capsule | Bottle of 84 capsules | Valid |
| 191817 | Ribapro 200mg Capsule | Strip of 8 capsules | Valid |
| 194480 | Ropegus 100mg Tablet | Strip of 4 tablets | Valid |
| 196609 | Ropegus 200mg Tablet | Strip of 4 tablets | Valid |
| 234892 | Virofix 200mg Capsule | Bottle of 40 capsules | Valid |
| 236046 | Virazide 200mg Capsule | Strip of 4 capsules | Valid |
| 237512 | Virazide 100mg Capsule | Strip of 4 capsules | Valid |
| 237924 | Virbetol Tablet | Strip of 7 tablets | Valid |
| 238635 | Virazide 50mg Syrup | Bottle of 30 ml Syrup | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

No label warnings or contraindications are available in the data compiled for this report. Please refer to the package insert.

- **Knowledge-graph contraindication relations (not label text):** These include chronic obstructive pulmonary disease, asthma, cirrhosis of liver, sarcoidosis, sickle cell anaemia and other haemoglobinopathies, haemolytic and other anaemias, pancytopenia, aplastic anaemia, myocardial infarction, coronary artery disease, atherosclerosis, interstitial lung disease, impaired renal function, pancreatitis, periodontitis and autoimmune hepatitis.
- **Drug Interactions:** 105 interactions are recorded, all with unclassified severity. Examples include pantoprazole, omeprazole, metformin, glimepiride, morphine, prednisone, amphotericin B and doxycycline.
- **Signals from the literature:** Several case reports describe porphyria cutanea tarda emerging during peginterferon/ribavirin therapy. One report describes interferon-associated pulmonary granulomatosis in a patient also receiving ribavirin. Haemolysis is a plausible concern given the anaemia-related relations above, though this is inferred and not from label text.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Only one completed Phase 3 trial studies ribavirin in hepatitis B, and it tests ribavirin as an add-on to peginterferon, so ribavirin's own effect cannot be isolated. There is no plausible direct mechanism against hepatitis B. The high TxGNN score (0.9986) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases such as hepatitis C, not biological evidence. Established hepatitis B therapies also exist, and the safety profile is demanding.

**To proceed, the following is needed:**
- Results of NCT00114361 and NCT00275938, to determine whether adding ribavirin improved outcomes over peginterferon alone
- Outcome data from the pilot of ribavirin with nucleoside analogues (NCT03759782)
- Mechanism of action data and package insert warnings and contraindications
- A safety plan covering haemolysis, anaemia, and cardiovascular and pulmonary risk

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: ribavirin prescribing information, Aurobindo Pharma Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eee304d0-c2ea-44f4-97d9-92a414d31b6c) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

