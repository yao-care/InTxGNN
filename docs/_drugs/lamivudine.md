---
layout: default
title: Lamivudine
parent: Model Prediction Only (L5)
nav_order: 469
evidence_level: L5
indication_count: 5
monitor_inn: "Lamivudine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "chronic hepatitis C virus infection"]
last_modified_at: 2026-10-31
description: "Lamivudine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: Chronic hepatitis B virus infection, HIV infectious disease, AIDS"
---

# Lamivudine
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

## Lamivudine: From HIV/Hepatitis B Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Lamivudine is a nucleoside reverse transcriptase inhibitor whose relations to chronic hepatitis B, HIV infection and AIDS are recorded in the knowledge graph, and it is marketed in India under many single-ingredient registrations.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV infection in cats)**, with **0 clinical trials** and **3 publications** (all veterinary or preclinical) currently supporting this direction.
This is a veterinary research question rather than a new human indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus infection, HIV infectious disease, AIDS (relations recorded in the knowledge graph; the licence records compiled for this report contain no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

The evidence level is L5 because no cited study investigates lamivudine alone in this disease. The three cat or in vitro FIV studies test multi-drug regimens, so the contribution of lamivudine cannot be separated. The system's preliminary rating was L3, but it is lowered here under the evidence ceiling rule.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Lamivudine is known as a nucleoside reverse transcriptase inhibitor (NRTI), a class that blocks viral DNA synthesis by the viral reverse transcriptase.

Feline immunodeficiency virus (FIV) is a lentivirus that causes an AIDS-like disease in cats. Its reverse transcriptase is homologous to that of HIV-1, and several NRTIs active against HIV also act against FIV. FIV infection in cats is therefore used as an animal model of HIV. A shared mechanism is plausible.

The caveats are important. The studies retrieved are veterinary observations and in vitro work, not human trials. Lamivudine was always given in combination (with zidovudine, or with zidovudine and abacavir), so its individual effect is unknown. This prediction mainly supports the mechanism rather than opening a new human use.

Other predictions in the list were also reviewed:
- **Simian immunodeficiency virus infection (score 0.9993)**: macaque studies show viral suppression with combination regimens including lamivudine and the same M184V resistance mutation seen in HIV. This is an animal model of the existing HIV use, not a new human indication.
- **Chronic hepatitis C (score 0.9911)**: HCV replicates through an RNA-dependent RNA polymerase without a reverse transcription step, so direct anti-HCV activity is not expected. The retrieved papers are general HBV/HCV reviews, and the link likely reflects co-mention with HBV. Repurposing is not warranted.
- **A rare neurodevelopmental disorder and an obsolete familial combined hyperlipidemia term**: model output only, with no studies and no evident mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22816032](https://pubmed.ncbi.nlm.nih.gov/22816032/) | 2012 | Veterinary cohort | Viruses | Compared zidovudine alone and with interferon-α, lamivudine or valproic acid in naturally FIV-infected cats over one year, using clinical, viral load and CD4+/CD8+ measures |
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | Veterinary long-term follow-up | J Feline Med Surg | Effects of long-term antiretroviral therapy (starting with zidovudine) over 5–6 years in FIV-infected domestic cats |
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | In vitro / preclinical | Antiviral Res | Combined zidovudine, lamivudine and abacavir suppressed FIV replication in vitro; FIV is discussed as a model for HIV |

---

## India Market Information

At least 20 single-ingredient registrations are on record (the list may be partial). The records contain no approved-indication text. Main entries:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 125461 | Lamidac 100mg Tablet (Zydus Cadila) | Strip of 10 tablets | Not stated in records |
| 104911 | Heptavir 150mg Tablet (Hetero Drugs Ltd) | Strip of 10 tablets | Not stated in records |
| 124322 | Lavir 150mg Tablet (Emcure Pharmaceuticals Ltd) | Bottle of 60 tablets | Not stated in records |
| 239597 | Virolam 150mg Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not stated in records |
| 226962 | Tapivir 100mg Tablet (Taj Pharma India Ltd) | Strip of 10 tablets | Not stated in records |

All dosage forms listed are oral.

---

## Safety Considerations

Package insert warnings and contraindications are not available in the data compiled for this report. Please refer to the package insert for label safety information.

**Knowledge-graph contraindication relations** (these come from the knowledge graph, not label text): liver failure, liver disease, fatty liver disease, non-alcoholic steatohepatitis, kidney disease, pancreatitis, gallbladder disease, lactic acidosis, neutropenia, agranulocytosis, anemia, macrocytic anemia, myopathy, myositis, dermatomyositis, hypertriglyceridemia, obesity disorder, and others.

**Drug interactions:** 145 interactions were found. Those with a moderate level are lactitol, mannitol, naltrexone, orlistat and sorbitol. Others (for example metformin, omeprazole, pantoprazole, morphine and vancomycin) have an unclassified level.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence is a few veterinary and preclinical studies of lamivudine-containing combinations, with no clinical trials and no isolated lamivudine effect. The prediction is mechanistically plausible but offers little new human therapeutic value, and the other high-scoring predictions have no meaningful support.

**To proceed, the following is needed:**
- Studies that test lamivudine alone against FIV, to establish a clear drug-specific effect
- Mechanism of action data for lamivudine
- Package insert warnings and contraindications from the India regulatory record
- A decision on whether a veterinary indication is within the scope of the repurposing programme
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

