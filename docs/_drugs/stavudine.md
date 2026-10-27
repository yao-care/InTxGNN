---
layout: default
title: Stavudine
parent: Model Prediction Only (L5)
nav_order: 790
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Stavudine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease"
monitor_inn: "Stavudine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Stavudine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Stavudine: From HIV Infection / AIDS to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Stavudine is a nucleoside reverse transcriptase inhibitor originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but there are **no clinical trials** and **no publications** supporting this specific prediction.
This is a veterinary indication, so it falls outside the scope of human drug repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (from the knowledge graph, as no approved indication text is available in the licence records) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 13 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, stavudine is a thymidine analogue nucleoside reverse transcriptase inhibitor (NRTI). It terminates viral DNA chain elongation, and its efficacy in HIV/AIDS is established.

Feline immunodeficiency virus (FIV) is a lentivirus whose reverse transcriptase is related to that of HIV-1, so a mechanistic rationale is plausible. The very high TxGNN score is most likely driven by the close similarity to the original HIV/AIDS indication, not by independent evidence for FIV.

Two other predictions were also reviewed:
- **Simian immunodeficiency virus (SIV) infection (score 99.55%)**: SIV is a primate lentivirus closely related to HIV, and its reverse transcriptase is susceptible to NRTIs. However, this is a non-human animal infection model. It is best viewed as a preclinical model of the existing HIV indication, not a new human indication.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter (score 99.51%)**: No clear mechanistic link exists. Stavudine's mitochondrial toxicity and its risk of peripheral neuropathy argue against benefit and may raise safety concerns. The score likely reflects network-level associations only.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked predicted indication (or for the two other predictions reviewed).

## Literature Evidence

Currently no related literature is available for the top-ranked indication (feline acquired immunodeficiency syndrome).

For the second-ranked prediction (SIV infection), the following preclinical and indirect publications were found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22013040](https://pubmed.ncbi.nlm.nih.gov/22013040/) | 2012 | Animal study (non-human primate) | Journal of Virology | Fatal pancreatitis in SIV-infected macaques treated with didanosine and stavudine after CTLA-4 and IDO blockade; a safety signal |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro study | Antiviral Therapy | Susceptibility of HIV-2, SIV and SHIV to 16 approved anti-HIV drugs and one experimental drug |
| [11435599](https://pubmed.ncbi.nlm.nih.gov/11435599/) | 2001 | In vitro study | Journal of Virology | Dideoxynucleoside efficacy against human foamy virus; tangential to SIV |

One further retrieved paper (PMID 9021177) concerns a different compound (SRR-SB3) and has low relevance to stavudine, so it is not listed.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 80569 | Emduo E 30 Kit | Packet of 3 kit | Not specified |
| Registration No. 211828 | Stahope 40mg Tablet | Bottle of 60 tablets | Not specified |
| Registration No. 241251 | Virostav 30mg Tablet | Strip of 10 tablets | Not specified |
| Registration No. 240904 | Virostav 40mg Tablet | Strip of 10 tablets | Not specified |
| Registration No. 209713 | Stag 30mg Capsule | Strip of 10 capsules | Not specified |

All 13 registrations are currently valid single-ingredient licences.

## Safety Considerations

- **Contraindications / conditions of concern (knowledge graph, not label text)**: kidney disease, pancreatitis, liver disease, fatty liver disease, non-alcoholic steatohepatitis, gallbladder disease, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, peripheral neuropathy and other peripheral nervous system disease, lactic acidosis, substance abuse/dependence, obesity disorder, and monogenic obesity.
- **Drug Interactions**: 134 interactions were identified in total. Those rated moderate include metronidazole, naltrexone, orlistat, rosuvastatin, simvastatin and tinidazole. Others are of unknown severity, for example metformin, omeprazole, pantoprazole, lansoprazole, prednisone, morphine and vancomycin.
- **Mechanism-related concerns**: stavudine's mitochondrial toxicity (inhibition of mitochondrial DNA polymerase gamma) is associated with peripheral neuropathy and lactic acidosis. The macaque study also reported fatal pancreatitis with dideoxynucleoside combinations.

Please refer to the package insert for full warnings and precautions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest on model scores alone (Evidence Level L5 for the top indication, L4 for SIV). The top two are veterinary or animal-model infections that do not support human repurposing. The third has no plausible mechanism and raises safety concerns.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India-marketed products
- Mechanism of action data from DrugBank
- A decision on whether veterinary indications are in scope; if not, a review of lower-ranked predictions for human diseases
- Any human clinical or mechanistic evidence for a new indication before reconsidering the decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

