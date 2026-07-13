---
layout: default
title: Idoxuridine
parent: 僅模型預測 (L5)
nav_order: 294
evidence_level: L5
indication_count: 10
---

# Idoxuridine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Idoxuridine: From Herpes Simplex Virus Infection to Vulvovaginal Candidiasis

## One-Sentence Summary

Idoxuridine (IDU) is one of the earliest antiviral drugs developed, historically used as a topical treatment for herpes simplex virus (HSV) keratitis and cutaneous herpetic lesions.
The TxGNN model predicts it may be effective for **Vulvovaginal Candidiasis** (top-ranked prediction, score 99.92%);
however, this prediction is currently supported by **no clinical trials** and only **1 tangentially related publication** — and the mechanistic rationale is fundamentally unsupported, as IDU has no antifungal activity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Herpes simplex virus (HSV) infection — topical treatment for herpetic keratitis and mucocutaneous herpes |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Idoxuridine (5-iodo-2′-deoxyuridine) acts as a thymidine analogue: it is incorporated into viral DNA during replication, producing dysfunctional viral strands and halting HSV-1 and HSV-2 reproduction. This mechanism is specific to DNA viruses that depend on thymidine kinase for nucleoside phosphorylation — a pathway absent in fungi and protozoa.

The TxGNN model's top-ranked prediction of vulvovaginal candidiasis (score 99.92%) is almost certainly driven by shared **anatomical location nodes** in the knowledge graph (vulvar/vaginal anatomy) rather than any pharmacological mechanism. Candida species are fungi, not DNA viruses, and Idoxuridine has no established antifungal mechanism, no known antifungal in vitro activity, and no clinical evidence supporting efficacy against candidiasis. The single literature hit retrieved for this indication (PMID 4564724) concerns herpesvirus infection of the female genital tract — a completely different pathogen — and does not mention Candida.

Among all 10 predicted indications in this Evidence Pack, **herpetic vulvovaginitis** (rank #5, score 99.59%) is the only prediction with genuine pharmacological alignment: HSV-2 is the primary causative agent, and IDU's antiviral mechanism directly applies. Historical topical use in genital herpes has been documented, and it may retain niche research value for acyclovir-resistant strains carrying UL23 (thymidine kinase) mutations. However, Idoxuridine has been clinically superseded by acyclovir and valacyclovir for this indication. All other top-ranked predictions (candidiasis, trichomoniasis, bacterial vaginosis, atrophic vaginitis) are mechanistically incompatible.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for vulvovaginal candidiasis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [4564724](https://pubmed.ncbi.nlm.nih.gov/4564724/) | 1972 | Clinical Report | Obstetrics and Gynecology | Report on Herpesvirus hominis (HSV) infection of the female genital tract — discusses IDU in the context of herpes, not candidiasis; retrieved due to anatomical keyword overlap |

---

## India Market Information

Idoxuridine is not currently registered or marketed in India. No authorization records are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN rank-1 prediction (vulvovaginal candidiasis) is mechanistically incompatible with Idoxuridine's mode of action as a DNA virus replication inhibitor. The high model score (99.92%) reflects anatomical co-localization in the knowledge graph, not pharmacological relevance, and no clinical or preclinical evidence supports antifungal efficacy. This candidate does not meet the minimum threshold for progression.

**To proceed, the following is needed:**

- **Indication re-targeting**: Reframe the repurposing candidate around **herpetic vulvovaginitis** (rank #5), the only mechanistically supported indication in this Evidence Pack, before investing further evaluation resources
- **Resistance niche assessment**: Investigate IDU activity against acyclovir-resistant HSV-2 (UL23 thymidine kinase–deficient mutants) as a potential clinical differentiator vs. first-line antivirals
- **Safety data retrieval**: Obtain complete package insert warnings, contraindications, and local toxicity data (especially for topical/mucosal formulations) before any clinical consideration — currently a blocking data gap
- **MOA documentation**: Retrieve full DrugBank mechanism-of-action record and any available in vitro selectivity data for the IDU/HSV-2 axis
- **India regulatory pathway review**: Determine whether IDU has ever been registered in India or neighboring markets and clarify the regulatory pathway for a potential new topical antiviral indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

