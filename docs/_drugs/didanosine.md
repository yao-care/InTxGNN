---
layout: default
title: Didanosine
parent: Model Prediction Only (L5)
nav_order: 264
evidence_level: L5
indication_count: 3
monitor_inn: "Didanosine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-30
description: "Didanosine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infection and AIDS"
---

# Didanosine
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

## Didanosine: From HIV Infection and AIDS to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Didanosine is a nucleoside reverse transcriptase inhibitor, with HIV infection and AIDS recorded as its original indications in the knowledge graph.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but there are **0 clinical trials** and only **2 preclinical publications**, and neither shows antiviral efficacy in infected cats.
The prediction is therefore a model output with very little supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection and AIDS (relations recorded in the knowledge graph; the local licence records contain no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9933 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (5 of 5) – CDSCO approval status is not included in this data |
| Number of Registrations | 5 (valid: 5) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, didanosine is a nucleoside reverse transcriptase inhibitor. Its active metabolite blocks viral DNA synthesis by chain termination. Feline immunodeficiency virus (FIV) is a lentivirus related to HIV, so a shared reverse transcriptase target is plausible.

The two retrieved papers do not support the prediction directly. They use FIV-infected animals or lentivirus models to study didanosine-induced sensory neuropathy and neuronal autophagy. They do not test whether didanosine controls FIV infection in cats. The high TxGNN score most likely reflects network proximity to the HIV/AIDS indication rather than independent evidence.

Because no cited study shows efficacy against feline immunodeficiency disease, the evidence level is L5 (model prediction only). This is also a veterinary condition, not a human indication, which limits its relevance for human drug repurposing.

Two other predictions are in the data. Simian immunodeficiency virus infection (same score, 0.9933) has preclinical support, including didanosine rescuing pigtail macaques from a lethal SIV dose (PMID 9282812). It is an HIV research model and mostly supports the existing HIV use. A neurodevelopmental disorder with ataxic gait (score 0.9926) has no supporting data at all.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17616550](https://pubmed.ncbi.nlm.nih.gov/17616550/) | 2007 | Preclinical animal study | Brain | In an FIV-infected model, didanosine caused sensory neuropathy with impaired mitochondrial and neurotrophic factor gene expression. This is a toxicity finding, not efficacy. |
| [19380511](https://pubmed.ncbi.nlm.nih.gov/19380511/) | 2009 | Preclinical mechanistic study | FASEB J | Lentivirus infection suppressed neuronal autophagy through CXCR3 activation. Antiretroviral therapy was neuroprotective in the models. |

---

## India Market Information

The licence records contain no approved indication text. All five are single-ingredient, valid registrations.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 66713 | Dinosin 100mg Tablet | Bottle of 60 tablets | Not stated in the record |
| Registration No. 237405 | Virosine DR 250mg Capsule | Packet of 30 capsules | Not stated in the record |
| Registration No. 68259 | Dinosin 250mg Tablet | Strip of 30 tablets | Not stated in the record |
| Registration No. 69362 | Dinosin 400mg Capsule | Strip of 30 capsules | Not stated in the record |
| Registration No. 239969 | Virosine DR 400mg Capsule | Packet of 30 capsules | Not stated in the record |

---

## Safety Considerations

- **Drug Interactions**: 153 interactions are recorded in total. Moderate-level ones include aspirin (acetylsalicylic acid), metronidazole, levofloxacin, naltrexone, nitisinone, orlistat, rosuvastatin, simvastatin and tinidazole. Minor-level ones include ranitidine, doxycycline, minocycline and tetracycline.
- **Contraindication relations in the knowledge graph** (not label text): these include kidney disease, liver disease, peripheral neuropathy, diabetes mellitus, hypertension, coronary artery disease, hypertriglyceridemia and nephrolithiasis.
- **Neurotoxicity signal**: the retrieved literature documents didanosine-induced sensory neuropathy and mitochondrial toxicity in an animal model.

Please refer to the package insert for label warnings and contraindications, as these were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a TxGNN model (deep learning) score alone. No clinical trial or cited study shows didanosine working against feline immunodeficiency disease, and the retrieved papers mainly document toxicity. The condition is also veterinary, so it is not a human repurposing target.

**To proceed, the following is needed:**
- Veterinary efficacy data in FIV-infected cats
- Mechanism of action data from DrugBank
- Package insert warnings and contraindications from the Indian regulator
- A decision on whether the SIV macaque findings should be treated as a research question rather than a repurposing candidate
- A neurotoxicity and mitochondrial toxicity risk assessment before any new use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

