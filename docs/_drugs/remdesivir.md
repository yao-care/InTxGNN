---
layout: default
title: Remdesivir
parent: Model Prediction Only (L5)
nav_order: 733
evidence_level: L5
indication_count: 10
---

# Remdesivir
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

# Remdesivir: From an Unspecified Original Indication to Multiple Endocrine Neoplasia

## One-Sentence Summary

Remdesivir is a nucleotide analog antiviral that inhibits viral RNA polymerase and is marketed in India as an injectable product. The TxGNN model predicts it may be effective for **multiple endocrine neoplasia**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone and the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Indian licence records compiled for this report |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general knowledge, remdesivir is a nucleotide analog prodrug that inhibits viral RNA-dependent RNA polymerase, and its established use is against RNA viruses such as SARS-CoV-2.

Multiple endocrine neoplasia is a hereditary tumour syndrome (for example, MEN1 or RET mutations). Remdesivir has no known target in its pathophysiology, so no plausible mechanistic link can be identified. The high TxGNN score appears to be a knowledge-graph artefact rather than a pharmacological signal. No supporting trials or literature were found.

Other predictions were also reviewed. The most biologically plausible, **HIV infection** (score 99.32%, L4), has only a theoretical rationale. Remdesivir is not an established antiretroviral, and the retrieved literature concerns COVID-19, not HIV. The remaining predictions (simian immunodeficiency virus infection, feline AIDS, homozygous familial hypercholesterolaemia, Prinzmetal angina, leprosy, antithrombin deficiency type 2, a rare neurodevelopmental disorder, and cytomegalovirus infection) also lack a convincing mechanism or direct evidence.

## Clinical Trial Evidence

Currently no related clinical trials are registered for multiple endocrine neoplasia.

For reference, one trial was retrieved for the second-ranked prediction (HIV infection). It is only weakly relevant:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04385719](https://clinicaltrials.gov/study/NCT04385719) | Phase 2 | Completed | 24 | Pharmacokinetic study in healthy Ugandan volunteers of how tenofovir/lamivudine or atazanavir/ritonavir affect remdesivir blood levels. It does not assess efficacy in HIV. |

## Literature Evidence

Currently no related literature is available for multiple endocrine neoplasia.

For the HIV-infection prediction, the retrieved publications are almost all about COVID-19 and are not direct evidence for HIV. The most notable are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33264556](https://pubmed.ncbi.nlm.nih.gov/33264556/) | 2021 | RCT | N Engl J Med | Interim WHO Solidarity trial of repurposed antivirals, including remdesivir, in hospitalised COVID-19 |
| [38675889](https://pubmed.ncbi.nlm.nih.gov/38675889/) | 2024 | RCT | Viruses | No remdesivir resistance observed in the Phase 3 SIMPLE trials in severe and moderate COVID-19 |
| [34696838](https://pubmed.ncbi.nlm.nih.gov/34696838/) | 2021 | Review | The Enzymes | Mechanisms of nucleotide analogs inhibiting viral RNA replication, comparing SARS-CoV-2 RdRp with HIV reverse transcriptase |
| [36347057](https://pubmed.ncbi.nlm.nih.gov/36347057/) | 2022 | Review | Topics in Antiviral Medicine | CROI 2022 update on antiviral advances for HIV, COVID-19 and viral hepatitis |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 189883 | Remdiz 100mg Injection (Glenmark Pharmaceuticals Ltd) | Vial of 1 injection | Not stated |
| 187652 | Remwin 100mg Injection (Sun Pharmaceutical Industries Ltd) | Vial of 1 injection | Not stated |
| 185844 | Remdac Injection (Zydus Cadila) | Vial of 1 injection | Not stated |
| 35394 | Cipremi Injection (Cipla Ltd) | Vial of 1 injection | Not stated |
| 60746 | Desrem Injection (Mylan Pharmaceuticals Pvt Ltd) | Vial of 1 injection | Not stated |

All five registrations are valid single-ingredient products, and all are injectables.

## Safety Considerations

**Drug Interactions**: The interaction screening returned 100 interactions in total. The 20 retrieved are all rated Moderate, including:
- Antibiotics: doxycycline, minocycline, tetracycline, clarithromycin, levofloxacin, vancomycin, kanamycin, neomycin
- Antifungals: amphotericin B (including the lipid complex)
- Antidiabetics: acarbose, pioglitazone
- Aminosalicylates: mesalazine, balsalazide, olsalazine
- Others: bupropion, naltrexone, chenodeoxycholic acid, oxandrolone, oxymetholone

For other warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The multiple endocrine neoplasia prediction has no clinical trial or literature support (L5) and no plausible mechanistic link to a viral polymerase inhibitor. The high TxGNN score alone does not justify further investment.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator or manufacturers
- Mechanism of action data from DrugBank
- Original approved indication text for the Indian licences
- Preclinical or mechanistic evidence linking remdesivir to MEN-related pathways, if this indication is to be pursued
- Alternatively, redirect evaluation to a more plausible antiviral indication, such as HIV infection, with direct efficacy data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

