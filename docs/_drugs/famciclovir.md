---
layout: default
title: Famciclovir
parent: Model Prediction Only (L5)
nav_order: 337
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Famciclovir: predicted new indication Post-infectious neuralgia (evidence level L5). Approved use: Herpes zoster"
monitor_inn: "Famciclovir"
predicted_indications: ["post-infectious neuralgia", "sequela of COVID-19", "hepatitis C induced liver cirrhosis", "malignant pleural mesothelioma", "AIDS-related disorder", "malignant epithelioid mesothelioma", "chickenpox", "sarcomatoid mesothelioma", "malignant visceral pleura tumor", "anogenital human papillomavirus infection"]
---

# Famciclovir
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

# Famciclovir: From Herpes Zoster to Post-Infectious Neuralgia

## One-Sentence Summary

Famciclovir is an oral antiviral originally used to treat herpes zoster (shingles).
The TxGNN model predicts it may be useful for **post-infectious neuralgia**, which in practice mostly means postherpetic neuralgia. However, only **1 clinical trial** is linked to this prediction, it tests oxycodone rather than famciclovir, and **no publications** support it directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpes zoster |
| Predicted New Indication | Post-infectious neuralgia |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 (indirect evidence only; no famciclovir-specific study) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 18 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Famciclovir is an oral antiviral used against herpes zoster. Its efficacy in that condition is established, and mechanistically it may be applicable to the nerve pain that follows it.

Postherpetic neuralgia is the most common complication of herpes zoster. It is nerve pain that persists after the shingles rash has healed. Treating the acute zoster phase with an antiviral may reduce the risk or severity of the neuralgia that follows. This link is indirect. It rests on controlling the underlying viral infection, not on any proven pain-relieving or nerve-protective effect of famciclovir itself.

The only linked trial tests early oxycodone use, not famciclovir. The prediction is therefore best treated as a research question, not an established new use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | Not applicable | Unknown | 140 | Tests early oxycodone during acute herpes zoster to prevent postherpetic neuralgia. Famciclovir is not the intervention, so this gives no direct evidence for famciclovir. |

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Famciclovir has 18 valid registrations in India, all single-ingredient oral tablets. The table lists 5 of them. The data compiled for this report does not include approved indication text for these products.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 174328 | Penvir 250 Tablet (Hetero Drugs Ltd) | Strip of 6 tablets | Not specified |
| Registration No. 233684 | Virovir 250 Tablet (FDC Ltd) | Strip of 6 tablets | Not specified |
| Registration No. 87424 | Famtag 500mg Tablet (Ikon Remedies Pvt Ltd) | Strip of 3 tablets | Not specified |
| Registration No. 84755 | Famtrex 500mg Tablet (Cipla Ltd) | Strip of 7 tablets | Not specified |
| Registration No. 84301 | Famcimac 500 Tablet (Macleods Pharmaceuticals Pvt Ltd) | Strip of 3 tablets | Not specified |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: kidney disease and pyoureter. Renal function should be considered when dosing.
- **Drug Interactions**: 84 potential interactions are recorded, all with an unclassified severity level. Examples include calcitriol, doxycycline, metformin, glimepiride, omeprazole, pantoprazole, morphine, simvastatin, prednisone and vancomycin. Their clinical significance has not been graded.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high model score (99.75%) is not backed by famciclovir-specific evidence for post-infectious neuralgia. The only linked trial studies oxycodone, and no publications are linked. The proposed link is indirect: treating the acute zoster infection may reduce later neuralgia.

For context, the same data shows stronger support for famciclovir in the related condition **chickenpox** (varicella-zoster virus infection). It has two completed Phase 3 trials: a pediatric pharmacokinetics and safety study (NCT00098046) and a zoster efficacy and safety study versus aciclovir (NCT01327144). That prediction is a better candidate to move forward.

**To proceed, the following is needed:**
- Trials or studies that directly test famciclovir for preventing or treating postherpetic neuralgia (for example, incidence of neuralgia after antiviral treatment in acute zoster)
- Detailed mechanism of action data
- Package insert warnings and contraindications for the Indian products, including approved indication text
- A renal dosing plan, given the kidney disease association
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

