---
layout: default
title: Framycetin
parent: Model Prediction Only (L5)
nav_order: 383
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Framycetin: predicted new indication Sclerosing cholangitis (evidence level L5). Approved use: Not stated in the available license records (marketed as topical crea…"
monitor_inn: "Framycetin"
predicted_indications: ["sclerosing cholangitis", "urinary tract infection (disease)", "congenital prothrombin deficiency", "gonococcal urethritis", "Ureaplasma urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis"]
---

# Framycetin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Framycetin: From Topical Antibacterial Use to Sclerosing Cholangitis
{: .text-alpha }

## One-Sentence Summary

Framycetin is an aminoglycoside antibiotic, marketed in India mainly as topical skin creams and a medicated bandage.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This is a model prediction only and should not be read as clinical support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available license records (marketed as topical cream and bandage products) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, framycetin is an aminoglycoside antibiotic with poor systemic absorption. Aminoglycosides act on the bacterial 30S ribosome and have broad Gram-negative activity.

The proposed link to sclerosing cholangitis is the gut-liver axis. Primary sclerosing cholangitis is hypothesised to involve gut microbiome changes and bile-acid-related inflammation. A gut-restricted antibiotic could theoretically modulate these. However, aminoglycosides have no established role in this disease; oral vancomycin is the antibiotic most studied. The high TxGNN score is therefore not clinical support.

**Other predicted indications (all L5, all Hold):**

| Rank | Predicted Indication | Score | Assessment |
|---|---|---|---|
| 2 | Urinary tract infection | 99.42% | Biologically plausible (Gram-negative activity, renal excretion), but framycetin is mainly used topically or orally. Systemic use is limited by nephrotoxicity and ototoxicity. Gentamicin and amikacin are better characterised. |
| 3 | Congenital prothrombin deficiency | 99.41% | No plausible mechanism. Likely a graph artifact. Oral antibiotics may reduce vitamin K-producing gut flora and worsen coagulopathy, so this is more a safety concern. |
| 4 | Gonococcal urethritis | 99.28% | Class-level plausibility, but guidelines rely on ceftriaxone-based regimens. |
| 5 | Ureaplasma urethritis | 99.28% | Ureaplasma is usually treated with tetracyclines or macrolides. Aminoglycoside activity against mycoplasmas is inconsistent. |
| 6 | Uterine inflammatory disease | 99.18% | Aminoglycosides (usually gentamicin plus clindamycin) are used in endometritis regimens, but there is no framycetin-specific evidence. |
| 7 | Xanthogranulomatous pyelonephritis | 99.18% | Antibacterial link is plausible, but nephrotoxicity in a diseased kidney is a significant concern. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 203335 | Sofraderm Cream (Torque Pharmaceuticals) | Cream, 15 g tube | Not stated |
| 201125 | Sofra Tuffle Bandage (Sanofi India) | Bandage, 1 per packet | Not stated |
| 199532 | Soframycin 1% Skin Cream (Encube Ethicals) | Cream, 30 g tube | Not stated |
| 199593 | Soframycin 1% Skin Cream (Encube Ethicals) | Cream, 100 g tube | Not stated |
| 200712 | Sofracen 1% Cream (Universal Lab) | Cream, 15 g tube | Not stated |

All five registrations are valid single-ingredient products, and all are topical or dressing formats.

## Safety Considerations

- **Route mismatch:** All marketed products in India are topical creams or a bandage. The predicted indications (sclerosing cholangitis, urinary tract and genital infections, pyelonephritis) would need oral or systemic exposure, which is not currently available as a marketed form.
- **Class concerns:** Systemic aminoglycosides carry nephrotoxicity and ototoxicity risks, which are especially relevant for renal indications.
- **Coagulation:** Oral antibiotics can reduce vitamin K-producing gut flora, which is relevant to the coagulation-related prediction.

No drug interactions were found in the data compiled for this report. Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predictions are model-only (L5), with no clinical trials or literature. The top prediction, sclerosing cholangitis, has no established role for aminoglycosides. The available India products are topical only, which does not match the predicted indications.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India products
- Mechanism of action data (for example, from DrugBank)
- A systematic literature search for framycetin or oral aminoglycosides in primary sclerosing cholangitis and the gut-liver axis
- A route-compatibility assessment (an oral or gut-restricted formulation would be required)
- Preclinical or in vitro evidence before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

