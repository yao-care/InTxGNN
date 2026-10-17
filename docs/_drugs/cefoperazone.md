---
layout: default
title: Cefoperazone
parent: High Evidence (L1-L2)
nav_order: 155
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Cefoperazone: predicted new indication Sclerosing cholangitis (evidence level L1). Approved use: Not stated in the registration records (cefoperazone is an injectable…"
monitor_inn: "Cefoperazone"
predicted_indications: ["sclerosing cholangitis", "rheumatoid arthritis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "gout", "bronchitis", "meningococcal infection", "infectious otitis media", "IgG4-related sclerosing cholangitis"]
---

# Cefoperazone
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Cefoperazone: From Antibacterial Therapy to Sclerosing Cholangitis

## One-Sentence Summary

Cefoperazone is a third-generation cephalosporin antibiotic, marketed in India as an injectable.
The TxGNN model's top-ranked new indication for it is **sclerosing cholangitis**, but **no clinical trials and no publications** support this prediction.
The best-supported predicted use is pneumonia, which is an established antibacterial use rather than true repurposing (see "Other Predicted Indications").

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records (cefoperazone is an injectable cephalosporin antibacterial) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cefoperazone is a third-generation cephalosporin that inhibits bacterial cell wall synthesis. Its efficacy is established in bacterial infections, but there is no data showing a mechanistic link to sclerosing cholangitis.

The only loose connection is that cefoperazone is excreted substantially in bile. That could matter for biliary infection or cholangitis from bacterial causes. It does not support a disease-modifying effect in primary sclerosing cholangitis, which is a chronic, immune-mediated, fibrosing disease. The high score is a computational prediction only.

---

## India Market Information

There are 20 valid registrations, all injectable. Approved indication text is not recorded for any of them. Five examples:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 142898 | Magna SB 1000mg/1000mg Injection | Vial of 1 Injection | Aristo Pharmaceuticals Pvt Ltd |
| 83839 | Edelcef 500mg Injection | Vial of 1 Powder for Injection | Edelweiss Lifecare Pvt Ltd |
| 213258 | Sulcetis SB 1g Injection | Vial of 1 Injection | Atlantis Formulations Pvt Ltd |
| 53383 | C Bactum Forte 2000mg/1000mg Injection | Vial of 1 Injection | Vhb Life Sciences Inc |
| 252967 | Zonefor 250mg Injection | Vial of 1 Injection | Fortune Labs |

---

## Safety Considerations

- **Contraindication signals (knowledge-graph, not label text):** liver disease, gallbladder disease, blood coagulation disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, congenital prothrombin deficiency, vitamin K deficiency hemorrhagic disease, digestive system disease, intestinal disease.
  - Liver and gallbladder disease are directly relevant to a biliary indication such as sclerosing cholangitis.
- **Drug Interactions:** 14 moderate-level interactions were identified:
  - Aminoglycosides: kanamycin, neomycin, streptomycin, amikacin (including liposomal), gentamicin
  - Anticoagulants: warfarin, heparin
  - Others: ethanol, chloramphenicol, picosulfuric acid, ethinylestradiol, mycophenolic acid, pemetrexed
  - Ethanol and the anticoagulants correspond to the known disulfiram-like reaction and bleeding risks.

Package insert warnings and contraindications were not available, so please refer to the package insert for the full safety profile.

---

## Other Predicted Indications

Because the top-ranked prediction has no support, here is how the other candidates compare:

| Predicted Indication | Evidence Level | Supporting Evidence | Assessment |
|------|------|------|------|
| **Pneumonia** (rank 3, score 99.93%) | L1 | 2 trials, 19 publications, including a randomized noninferiority trial of cefoperazone-sulbactam vs cefepime in hospital-acquired pneumonia ([PMID 31138577](https://pubmed.ncbi.nlm.nih.gov/31138577/)) and a comparison vs piperacillin-tazobactam ([PMID 34168466](https://pubmed.ncbi.nlm.nih.gov/34168466/)) | Proceed with Guardrails. This is an established antibacterial use. The trials are [NCT07671755](https://clinicaltrials.gov/study/NCT07671755) (completed, n=80, colistin ± cefoperazone-sulbactam for MDR *A. baumannii* ventilator-associated pneumonia) and [NCT02060149](https://clinicaltrials.gov/study/NCT02060149) (Phase 1/2, status unknown, n=90, indirect evidence). Guardrails are antimicrobial stewardship, local resistance patterns, and bleeding and alcohol-reaction risks. |
| Bronchitis (rank 7) | L3 | Mostly 1980s open-label or comparative studies | Research question. Most bronchitis is viral, so stewardship applies. |
| Meningococcal infection (rank 8) | L3 | One small 1987 preliminary report in bacterial meningitis | Research question. CSF penetration is inferior to ceftriaxone and cefotaxime. |
| Infectious otitis media (rank 9) | L4 | Only indirect bacteriology and other-drug studies | Hold |
| Rheumatoid arthritis, gout, IgG4-related sclerosing cholangitis, colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome | L4–L5 | None relevant (the RA papers are case reports of infections in RA patients) | Hold. No plausible mechanism. |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, sclerosing cholangitis, rests only on a model score. It has no trials, no literature, and no plausible mechanism for an antibiotic. The knowledge-graph also flags liver and gallbladder disease as contraindications. The genuinely supported direction is pneumonia, which is an established antibacterial use rather than new repurposing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from India registration documents, which are currently missing and block safety screening
- Mechanism of action data
- For sclerosing cholangitis: any preclinical or clinical signal beyond the model score, before further investment
- For pneumonia: confirmation of the approved indication text and a stewardship and local-resistance review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

