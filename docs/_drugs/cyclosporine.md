---
layout: default
title: Cyclosporine
parent: 僅模型預測 (L5)
nav_order: 218
evidence_level: L5
indication_count: 7
---

# Cyclosporine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cyclosporine: From Transplant Rejection Prophylaxis to Chronic Granulomatous Disease

## One-Sentence Summary

> Cyclosporine is a calcineurin-inhibitor immunosuppressant classically used to prevent organ/graft rejection and to treat select autoimmune conditions.
> The TxGNN model predicts a possible signal for **Chronic Granulomatous Disease, Autosomal Recessive**,
> but this is currently supported by only **1 clinical trial** and **1 publication**, both of which relate to cyclosporine's role as GVHD prophylaxis during stem-cell transplant rather than as direct CGD therapy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No Taiwan license data available (drug not currently marketed in Taiwan). Based on general pharmacological knowledge, cyclosporine is internationally indicated for prevention of solid-organ/bone-marrow transplant rejection and select autoimmune diseases. |
| Predicted New Indication | Chronic Granulomatous Disease, Autosomal Recessive |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for cyclosporine is not available in this evidence pack. Based on known pharmacology, cyclosporine binds cyclophilin to inhibit calcineurin, blocking T-cell activation and IL-2 transcription — its established efficacy is in suppressing T-cell–mediated rejection and autoimmune inflammation.

Chronic Granulomatous Disease (CGD), however, is caused by NADPH oxidase gene defects that impair phagocyte (neutrophil/macrophage) bactericidal killing — a phagocyte defect, not a T-cell–driven pathology. The disease-modifying treatment for CGD is allogeneic hematopoietic stem cell transplantation (HSCT), and cyclosporine appears in this context only as **GVHD prophylaxis** supporting the transplant procedure, not as a therapy targeting CGD's underlying mechanism.

Consequently, the mechanistic link between cyclosporine and CGD is weak and indirect: the drug's association with CGD in the source evidence stems from its routine use as immunosuppression during HSCT for CGD patients, not from any direct pharmacological action against the CGD phenotype.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01917708](https://clinicaltrials.gov/study/NCT01917708) | Phase 1 | Completed | 10 | Assessed abatacept combined with cyclosporine and mycophenolate mofetil as GVHD prophylaxis in children/adolescents undergoing unrelated allogeneic HSCT for serious non-malignant diseases; cyclosporine was a background regimen component, not the study drug (relevance grade C — indirect). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22078471](https://pubmed.ncbi.nlm.nih.gov/22078471/) | 2012 | Cohort | Journal of Allergy and Clinical Immunology | Reports excellent survival after sibling or unrelated-donor HSCT for CGD; cyclosporine is part of standard peri-transplant immunosuppression, not evaluated as a CGD-specific therapy. |

---

## Taiwan Market Information

Cyclosporine currently holds no marketing authorization in Taiwan (market status: Not Marketed; 0 registrations on file).

---

## Safety Considerations

- **Drug Interactions**: A DDI query returned 823 total interactions on record. Notable entries from the reviewed subset include:
  - **Major**: Loperamide
  - **Moderate**: Rabeprazole, Hydrocortisone, Amphotericin B (and lipid complex), Bupropion, Aprepitant, Mesalazine, Triamcinolone, Acetylsalicylic acid, Balsalazide, Dexamethasone, Betamethasone, Metronidazole, Budesonide (oral and nasal), Chlorpropamide, Cholic Acid
  - **Minor**: Ranitidine, Doxycycline

Detailed label warnings and contraindications (TFDA package insert) are not yet available for this drug (see DG001, blocking gap) — please refer to the package insert once obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between cyclosporine and CGD is weak and indirect — the only supporting trial and publication reflect cyclosporine's routine use as GVHD prophylaxis during HSCT for CGD, not a targeted pharmacological effect on CGD pathology. Evidence level is L4 (mechanism/preclinical-adjacent only), and the drug is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- TFDA package insert data (warnings/contraindications) — currently blocking (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Clinical evidence directly evaluating cyclosporine's effect on CGD outcomes, independent of its role as transplant-related immunosuppression
- Re-evaluation of Taiwan market entry strategy given current "Not Marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

