---
layout: default
title: Ribavirin
parent: Model Prediction Only (L5)
nav_order: 736
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ribavirin: predicted new indication Chronic hepatitis B virus infection (evidence level L5). Approved use: Chronic hepatitis C virus infection"
monitor_inn: "Ribavirin"
predicted_indications: ["primitive portal vein thrombosis", "hepatoportal sclerosis", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "hepatic porphyria", "IgG4-related pachymeningitis", "eosinophilic angiocentric fibrosis", "IgG4-related aortitis"]
---

# Ribavirin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Ribavirin: From Chronic Hepatitis C to Chronic Hepatitis B Virus Infection

## One-Sentence Summary

Ribavirin is an oral antiviral nucleoside analogue originally used for chronic hepatitis C virus infection and respiratory syncytial virus infection.
The TxGNN model predicts it may be effective for **chronic hepatitis B virus infection**, with **15 clinical trials** and **20 publications** compiled for this report.
Most of this evidence concerns hepatitis C, so support for hepatitis B specifically is limited and mostly indirect. Ribavirin has not been shown to work against hepatitis B on its own.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus infection; respiratory syncytial virus infection (the approved indication text in the India license records is blank) |
| Predicted New Indication | Chronic hepatitis B virus infection |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L1 (formally met by one completed Phase 3 trial, but see the note below) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

**Note on the evidence level:** The L1 rule asks for two or more completed Phase 3 RCTs. Only one completed Phase 3 trial tests ribavirin in chronic hepatitis B (NCT00114361). In that trial ribavirin was given together with peginterferon, so its own contribution cannot be separated out. A conservative reading is therefore weaker than L1.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ribavirin is a guanosine nucleoside analogue with broad antiviral activity. It is generally understood to work by inhibiting IMPDH (and so depleting the cell's GTP pool) and by modulating the immune response. It is established in hepatitis C, usually together with peginterferon.

Hepatitis B and hepatitis C are both chronic viral liver infections. They often occur together in the same patients, especially in regions where both are common. This is why ribavirin-containing regimens have been tried in hepatitis B and in HBV/HCV co-infection.

The mechanistic link, however, is weak. Ribavirin's direct activity against HBV is limited. Any benefit seen in trials appears to come from combination with peginterferon, where ribavirin may boost the immune response. The very high TxGNN score reflects the drug's closeness to hepatitis C in the knowledge graph and is not clinical proof of efficacy in hepatitis B.

## Clinical Trial Evidence

Of the 15 trials compiled, the table lists those most relevant to hepatitis B. Many other trials are hepatitis C studies in which ribavirin was only a background drug, and they give little direct information about hepatitis B.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00114361](https://clinicaltrials.gov/study/NCT00114361) | Phase 3 | Completed | 138 | Peginterferon alfa-2a plus ribavirin vs peginterferon alone in HBeAg-negative chronic hepatitis B. This is the most direct test, but ribavirin's own effect cannot be separated from peginterferon. |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Phase 2/3 | Completed | 120 | Pilot study of interferon alpha-2b plus ribavirin in chronic hepatitis. The population (HBV or HCV) is unclear from the available title, and the pilot design limits the strength of the evidence. |
| [NCT00154869](https://clinicaltrials.gov/study/NCT00154869) | Phase 3 | Unknown | 320 | Peginterferon alfa-2a plus ribavirin in chronic hepatitis C and in HBV/HCV co-infection. Ribavirin's role against HBV cannot be confirmed. |
| [NCT03759782](https://clinicaltrials.gov/study/NCT03759782) | Phase 3 | Unknown | 24 | Pilot testing whether ribavirin's immune-modulating properties can boost standard nucleoside-analogue therapy for HBV. |
| [NCT00117533](https://clinicaltrials.gov/study/NCT00117533) | Phase 4 | Unknown | 20 | Pilot of pegylated interferon alfa-2b plus ribavirin in patients with dual hepatitis B and D infection. |
| [NCT01447420](https://clinicaltrials.gov/study/NCT01447420) | Phase 4 | Completed | 129 | Peginterferon plus ribavirin and IL-28B expression in genotype 1 hepatitis C. Only indirect evidence for HBV. |
| [NCT02219477](https://clinicaltrials.gov/study/NCT02219477) | Phase 3 | Completed | 36 | Direct-acting antiviral regimen with ribavirin in hepatitis C with decompensated cirrhosis. No evidence of anti-HBV activity. |
| [NCT01425970](https://clinicaltrials.gov/study/NCT01425970) | Phase 2 | Terminated | 210 | INX-08189 with peginterferon and ribavirin in hepatitis C genotypes 2 and 3. Terminated early, and the evidence is indirect. |
| [NCT01195181](https://clinicaltrials.gov/study/NCT01195181) | Phase 4 | Completed | 506 | Surveillance and control program for chronic hepatitis C. It does not test ribavirin in HBV. |
| [NCT01795911](https://clinicaltrials.gov/study/NCT01795911) | Phase 2 | Completed | 165 | Peginterferon lambda with ribavirin and direct-acting agents in genotype 1 hepatitis C. Indirect evidence for HBV. |

## Literature Evidence

The publications compiled are almost all narrative reviews. No randomized trial publication was identified in this set. Most discuss hepatitis B and C together, and several mention ribavirin only in the hepatitis C context.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | HCV/HBV co-infection carries a high risk of liver disease progression. Peginterferon plus ribavirin was previously recommended for co-infected patients who are HCV RNA positive. |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | Update on treatment and outcomes of dual HCV/HBV infection. |
| [16838649](https://pubmed.ncbi.nlm.nih.gov/16838649/) | 2006 | Review | Nihon Rinsho | HCV-HBV co-infection. Peginterferon alpha-2b plus ribavirin is the most effective initial regimen for hepatitis C. |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Review | Expert Rev Anti Infect Ther | Treatment options for chronic hepatitis B and C in children. |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | Review | Annu Rev Med | Current treatment strategies for chronic hepatitis B and C. |
| [25048716](https://pubmed.ncbi.nlm.nih.gov/25048716/) | 2015 | Review | Hepatology | Immunological aspects of antiviral therapy in chronic HBV and HCV infection. |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | Review | World J Gastroenterol | IL28B polymorphism is linked to response to peginterferon plus ribavirin in hepatitis C. Its relevance to hepatitis B is less clear. |
| [26284971](https://pubmed.ncbi.nlm.nih.gov/26284971/) | 2015 | Review | Curr Opin Virol | Effect of IL28B genotype on hepatitis B and C. |

## India Market Information

Ribavirin is marketed in India with 20 valid single-ingredient registrations. The approved indication text is blank in the license records, so no indication is shown. The five main registrations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 185023 | Ribasure Capsule | Bottle of 140 capsules | Not stated in the records |
| 104577 | Heptos 200mg Capsule | Strip of 10 capsules | Not stated in the records |
| 186691 | Rebetol 200mg Capsule | Strip of 12 capsules | Not stated in the records |
| 236046 | Virazide 200mg Capsule | Strip of 4 capsules | Not stated in the records |
| 187852 | Ribavin 50mg Syrup | Bottle of 30 ml syrup | Not stated in the records |

Other registered forms include 100 mg capsules and tablets in several strengths.

## Safety Considerations

- **Disease-based cautions (from knowledge-graph contraindication links, not label text):** The links include chronic obstructive pulmonary disease, asthma, interstitial lung disease and sarcoidosis. They also include cirrhosis of liver, impaired renal function, and cardiovascular conditions such as myocardial infarction, coronary artery disease and atherosclerosis. Further links cover blood disorders (sickle cell anaemia, haemolytic anaemia, other anaemias, hemoglobinopathy and pancytopenia), as well as pancreatitis and autoimmune hepatitis. These come from a prediction model's data, so please confirm them against the official package insert.
- **Drug Interactions:** 105 potential interactions were recorded. Examples include calcitriol, pantoprazole, glimepiride, mesalazine, doxycycline, metformin, omeprazole, prednisone, amphotericin B and morphine. Severity levels are not classified in the available data.
- **Signal from the literature:** Several case reports describe porphyria cutanea tarda emerging or worsening during peginterferon plus ribavirin therapy. Ribavirin-related haemolysis and iron overload may contribute, so ribavirin should be treated as a possible risk factor in porphyria and not as a treatment for it.

Please also refer to the package insert for full warnings and contraindications, as these were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Only one completed Phase 3 trial directly tests ribavirin in chronic hepatitis B, and it used ribavirin with peginterferon, so ribavirin's independent benefit is unproven. The literature is mostly narrative reviews, the mechanistic link is weak, and the high TxGNN score mainly reflects closeness to hepatitis C. Package insert safety data were also not available, so safety screening cannot yet proceed.

**To proceed, the following is needed:**
- The package insert warnings and contraindications from the India manufacturers or regulator
- Detailed mechanism of action data, especially on any direct anti-HBV activity
- Confirmation of the HBV or HCV population in NCT00275938 and NCT00154869
- Results from the ongoing or unknown-status HBV-focused pilots (NCT03759782, NCT00117533)
- Evidence that separates ribavirin's effect from peginterferon in HBV, for example a randomized comparison against peginterferon alone with full results
- A safety plan covering haemolytic anaemia, cardiopulmonary disease and renal impairment

**Other predicted indications:** The nine other predictions (for example hepatopulmonary syndrome, hepatic porphyria, portal vein thrombosis and IgG4-related disease) have no supporting efficacy evidence and should stay on Hold. The literature on hepatic porphyria points to a safety concern and not a benefit.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

