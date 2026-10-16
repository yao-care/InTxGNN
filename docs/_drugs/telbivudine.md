---
layout: default
title: Telbivudine
parent: Model Prediction Only (L5)
nav_order: 811
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Telbivudine: predicted new indication Chronic hepatitis C virus infection (evidence level L5). Approved use: Chronic hepatitis B virus infection"
---

# Telbivudine
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

# Telbivudine: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Telbivudine is an oral nucleoside analogue originally used to treat chronic hepatitis B virus (HBV) infection.
The TxGNN model predicts it may be effective for **chronic hepatitis C virus infection**, but this is currently a **model-only prediction**, with **0 clinical trials** and **6 publications**, none of which report telbivudine activity against hepatitis C virus (HCV).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus infection (registration records list no indication text, so this comes from the drug-disease relationship data) |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Published literature describes telbivudine as a thymidine nucleoside analogue that selectively inhibits HBV DNA polymerase. Its efficacy in chronic hepatitis B is well established.

The mechanistic link to hepatitis C is weak. HCV replicates through an RNA-dependent RNA polymerase (NS5B), which differs structurally and functionally from HBV DNA polymerase. HCV is now treated with direct-acting antivirals. The high score most likely reflects the closeness of hepatitis B and hepatitis C in the knowledge graph, since both are chronic viral hepatitis. It does not reflect demonstrated antiviral activity.

The retrieved literature supports this reading. Most papers are reviews covering both hepatitis B and C, and none shows telbivudine acting against HCV.

Hepatitis B itself appears as the second-ranked prediction. This is the approved indication, with Phase 3 and Phase 4 trials, and it acts as a positive control for the model rather than a true repurposing finding.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25233195](https://pubmed.ncbi.nlm.nih.gov/25233195/) | 2014 | Review | J Perinatol | Hepatitis B and C in pregnancy and efforts to reduce mother-to-child transmission. No telbivudine-specific HCV data. |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Effects of hepatitis B and C antiviral drugs, including telbivudine for hepatitis B, on kidney function. |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | Current and future treatment of chronic hepatitis B and C, mainly interferon and lamivudine. |
| [18340426](https://pubmed.ncbi.nlm.nih.gov/18340426/) | 2008 | Review | Der Internist | German recommendations for antiviral therapy of hepatitis B and C. Telbivudine is listed as an option for hepatitis B only. |
| [21999649](https://pubmed.ncbi.nlm.nih.gov/21999649/) | 2011 | Review | Paediatr Drugs | Management of chronic liver disease in children, including viral hepatitis. |
| [23697556](https://pubmed.ncbi.nlm.nih.gov/23697556/) | 2013 | Cohort | J Interferon Cytokine Res | Serum IL-37 levels and HBeAg seroconversion in HBV patients on telbivudine. HBV-specific, not HCV. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 223925 | Telbihep 600mg Tablet | Strip of 10 tablets (oral) | Zydus Cadila |
| 203070 | Sebivo 600mg Tablet | Strip of 15 tablets (oral) | Novartis India Ltd |

Both are valid single-ingredient registrations.

## Safety Considerations

- **Conditions flagged as contraindication-related:** kidney disease, pyoureter, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, peripheral nervous system disease, peripheral neuropathy, fatty liver disease, non-alcoholic steatohepatitis, lactic acidosis, dermatomyositis, myositis. These come from drug-disease relationship data, not from package insert text.
- **Drug interactions:** 96 interacting drugs are recorded. The 20 listed in the data are all rated Moderate. They include:
  - corticosteroids (hydrocortisone, prednisone, dexamethasone, betamethasone, budesonide, triamcinolone)
  - amphotericin B formulations
  - aminoglycosides and other antibiotics (kanamycin, neomycin, vancomycin, metronidazole)
  - statins (rosuvastatin, simvastatin)
  - aminosalicylates (mesalazine, sulfasalazine, balsalazide, olsalazine)
  - orlistat

Package insert warnings were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on model score. There are no clinical trials, no plausible mechanism (HBV DNA polymerase versus HCV NS5B), and no literature showing activity against HCV. Effective direct-acting antivirals already exist for hepatitis C. The neuromuscular and renal safety signals add further caution.

**To proceed, the following is needed:**
- In vitro HCV replicon or enzyme data showing any telbivudine activity against HCV
- Detailed mechanism of action data
- Package insert warnings and contraindications from the India registrations
- A clear comparison against current direct-acting antiviral regimens to justify any clinical development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

