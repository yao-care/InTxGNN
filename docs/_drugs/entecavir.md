---
layout: default
title: Entecavir
parent: Moderate Evidence (L3-L4)
nav_order: 309
evidence_level: L3
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "Entecavir"
predicted_indications: ["chronic hepatitis C virus infection", "HIV infectious disease", "hepatitis C virus infection", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "hepatitis, viral, animal", "hepatitis E virus infection", "hepatitis A virus infection"]
description: "Entecavir: predicted new indication Chronic hepatitis C virus infection (evidence level L3). Approved use: Not recorded in the local data"
---

# Entecavir
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **9** 
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

## Entecavir: Chronic hepatitis C virus infection
{: .text-alpha }

## One-Sentence Summary

Entecavir is an oral nucleoside analogue originally used to treat chronic hepatitis B virus (HBV) infection.
The TxGNN model predicts it may be effective for **chronic hepatitis C virus infection**, but the supporting evidence is indirect: **2 clinical trials** and about **20 publications** were found, and they mostly concern preventing HBV reactivation in patients infected with both viruses, not treating HCV.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L3 (indirect evidence only; no direct evidence of anti-HCV activity) |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. From general knowledge, entecavir is a guanosine nucleoside analogue. Once converted to its triphosphate form inside cells, it inhibits the HBV polymerase and blocks viral DNA synthesis.

HCV is an RNA virus that replicates with a different enzyme (NS5B RNA-dependent RNA polymerase), and entecavir has no recognized direct activity against it. The high TxGNN score (deep learning model) may reflect similarities the model learned between related diseases, not biological evidence.

The one plausible clinical link is co-infection. In patients with both HBV and HCV, anti-HCV direct-acting antiviral (DAA) therapy can trigger HBV reactivation, and entecavir can suppress that reactivation. This is HBV management in co-infected patients rather than anti-HCV efficacy, so it does not support a true repurposing claim for HCV.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Anti-HCV direct-acting antivirals in HCV/HBV co-infected patients; examines the incidence and risk factors of HBV reactivation. Entecavir is not the test drug. |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | Not applicable | Unknown | 60 | Randomized, open-label study of whether prophylactic nucleos(t)ide analogue (12 vs 24 weeks) prevents HBV reactivation during DAA therapy for HCV. Aimed at HBV, not HCV. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34864158](https://pubmed.ncbi.nlm.nih.gov/34864158/) | 2022 | Randomized trial | Clin Gastroenterol Hepatol | Entecavir prevents HBV reactivation during DAA treatment of HCV/HBV dual infection |
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | HCV reactivation in anti-HCV-positive chronic hepatitis B patients (n=66) on nucleos(t)ide analogue therapy |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | Advances in treating HBV/HCV coinfection |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Antiviral drugs for hepatitis B and C and their effects on kidney function |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | Current treatment and future prospects in chronic hepatitis B and C |

---

## India Market Information

Entecavir has 20 valid single-ingredient registrations in India, all oral tablets. The approved indication text is not available for any of them. Five main registrations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 75964 | Entarica 0.5 Tablet (Fibrica Healthcare) | Strip of 10 tablets | Not available |
| 77463 | Entabest 0.5 Tablet (Shelton Pharmaceuticals) | Bottle of 30 tablets | Not available |
| 72382 | Entavir 0.5mg Tablet (Cipla) | Strip of 10 tablets | Not available |
| 72781 | Entehep 0.5 Tablet (Zydus Cadila) | Bottle of 30 tablets | Not available |
| 105508 | Hepalo 0.5 Tablet (Emcure Pharmaceuticals) | Strip of 10 tablets | Not available |

---

## Safety Considerations

- **Contraindications (TxGNN model (deep learning) associations, which may reflect similarities the model learned between related diseases, not biological evidence; not label text)**: impaired renal function, fatty liver disease, non-alcoholic steatohepatitis, lactic acidosis.
- **Drug Interactions**: 44 interactions were identified, and the 20 listed are all moderate. Several involve agents that can affect renal function: amphotericin B (including lipid, liposomal and cholesteryl sulfate forms), vancomycin, kanamycin, neomycin, polymyxin B, levofloxacin and amoxicillin. Others include metformin, the H2 blockers famotidine, ranitidine and cimetidine, the aminosalicylates mesalazine, balsalazide, olsalazine and sulfasalazine, and orlistat.
- **Other known signals (from the literature)**: lactic acidosis, post-treatment hepatitis flares, and rare thrombocytopenia.

Please refer to the package insert for the official warnings and contraindications. The Indian package insert data was not available when this report was compiled.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No evidence shows that entecavir acts against HCV. The available trials and papers concern preventing HBV reactivation in co-infected patients, which is already a use of entecavir's HBV activity. The high TxGNN score appears to come from network proximity between hepatitis viruses. HCV is also now curable with DAA regimens, so there is little unmet need for an entecavir-based approach.

**To proceed, the following is needed:**
- Mechanism of action data and any in vitro evidence of anti-HCV activity
- Indian package insert warnings and contraindications
- If the real interest is co-infection, a separate evaluation of HBV reactivation prophylaxis during DAA therapy, framed as an HBV indication rather than an HCV one
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

