---
layout: default
title: Axitinib
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
---

# Axitinib
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

# Axitinib: From Advanced Renal Cell Carcinoma to Renal Cell Carcinoma Associated with Xp11.2 Translocations/TFE3 Gene Fusions

---

## One-Sentence Summary

Axitinib (Inlyta) is a potent, selective oral inhibitor of vascular endothelial growth factor receptors (VEGFR) 1, 2, and 3, approved internationally as second-line therapy for advanced renal cell carcinoma (RCC).
The TxGNN model predicts it may be effective for **Renal Cell Carcinoma Associated with Xp11.2 Translocations/TFE3 Gene Fusions** — a rare and aggressive RCC subtype — with **1 active Phase 2 clinical trial** currently evaluating this approach and **no published literature** specifically addressing this rare subtype.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Advanced renal cell carcinoma (globally approved; not registered in India) |
| Predicted New Indication | Renal Cell Carcinoma Associated with Xp11.2 Translocations/TFE3 Gene Fusions |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Axitinib is a second-generation oral tyrosine kinase inhibitor (TKI) with nanomolar-level selectivity for VEGFR1, VEGFR2, and VEGFR3 — its inhibitory concentration is approximately 10-fold lower than first-generation VEGFR TKIs such as sorafenib and sunitinib. Detailed mechanism of action data was not retrieved in this analysis (DrugBank DB06626 query returned limited pharmacological detail), but Axitinib's anti-angiogenic mechanism in conventional clear-cell RCC is well-characterised: VHL gene mutations drive aberrant HIF-1α accumulation, which massively upregulates VEGF/VEGFR signalling and creates a highly angiogenesis-dependent tumour microenvironment that is precisely targeted by Axitinib's VEGFR blockade. The clinical validation of this mechanism is robust — multiple Phase 3 RCTs including KEYNOTE-426 and JAVELIN Renal 101 have established Axitinib-combination regimens as standard first-line therapy for advanced RCC.

Xp11.2 translocation/TFE3 fusion RCC is a molecularly distinct subtype accounting for approximately 1–5% of adult RCC cases and a disproportionately larger fraction of paediatric RCC. These tumours carry chromosomal translocations that produce TFE3 fusion oncoproteins, which transcriptionally upregulate VEGF-related angiogenic signalling pathways. This downstream pathway overlap — elevated VEGFR activity — provides a direct mechanistic bridge between Axitinib's established target and this rare subtype. Critically, Xp11.2/TFE3 fusion RCC is notoriously resistant to conventional chemotherapy, and the subtype predominantly affects young patients where treatment options are severely limited. VEGFR-directed therapy therefore fills a genuine unmet clinical need.

The rationale is further strengthened by the synergistic logic of combining Axitinib with PD-1 immune checkpoint inhibition (ICI): Axitinib has been shown in conventional RCC to remodel the immunosuppressive tumour microenvironment by reducing regulatory T-cell infiltration and enhancing effector T-cell density, thereby potentiating the anti-tumour effect of PD-1 blockade. The same synergistic strategy — directly tested in this subtype via NCT03595124 (axitinib + nivolumab vs. nivolumab alone) — represents a scientifically well-motivated extension of the established Axitinib + ICI paradigm into a molecularly related but clinically distinct tumour type.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Phase 2 | Active, Not Recruiting | 15 | Randomised trial comparing axitinib + nivolumab vs. nivolumab alone, specifically designed for unresectable or metastatic TFE/translocation RCC (including Xp11.2 subtypes) across all age groups including children. Tests whether adding axitinib's VEGFR blockade to nivolumab's PD-1 checkpoint inhibition improves outcomes in this chemotherapy-refractory subtype. Estimated completion: November 2026. Results pending. |

---

## Literature Evidence

Currently no related literature available specifically addressing axitinib in renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions.

---

## India Market Information

Axitinib is **not currently registered or marketed in India (CDSCO)**. No product authorisations were identified in the regulatory database (total licences: 0). For reference, axitinib (Inlyta®, Pfizer) holds FDA approval (2012) and EMA approval for advanced clear-cell RCC in adults after failure of one prior systemic therapy, as well as first-line approvals in combination with pembrolizumab (KEYNOTE-426) and avelumab (JAVELIN Renal 101). Any clinical development or compassionate use programme in India would require an initial CDSCO registration pathway assessment.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective VEGFR tyrosine kinase inhibitor (non-conventional cytotoxic) |
| Myelosuppression Risk | Low (anaemia and lymphopenia occasionally reported; haematological toxicity is significantly lower than conventional cytotoxics) |
| Emetogenicity Classification | Low (oral targeted agent; nausea reported infrequently and is clinically manageable) |
| Monitoring Items | Blood pressure (hypertension is a class-effect of VEGFR TKIs), thyroid function, liver function (ALT/AST), renal function, CBC, urinalysis for proteinuria, signs of thromboembolism and wound healing complications |
| Handling Protection | Standard oral oncology precautions; cytotoxic-level containment protocols are not mandated for VEGFR TKIs, but institutional dispensing and spill guidelines should be followed |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for Axitinib in Xp11.2/TFE3 fusion RCC is scientifically sound and a dedicated Phase 2 randomised trial is actively generating data; however, with only 15 enrolled patients, no completed trials, and no published literature specific to this subtype, the evidence base is insufficient to support clinical deployment or regulatory application at this stage.

**To proceed, the following is needed:**
- Final results from NCT03595124 (estimated completion November 2026) — this is the pivotal data event
- Published peer-reviewed outcome data specifically for Xp11.2/TFE3 fusion RCC treated with VEGFR TKIs
- Full pharmacological profile from DrugBank (DB06626) to formally document VEGFR pathway selectivity and MOA
- Safety and pharmacokinetic data in paediatric and young adult populations (this subtype disproportionately affects younger patients, yet adult dosing assumptions may not apply)
- CDSCO registration assessment for axitinib in India before initiating any local clinical trial or access programme
- Biomarker-driven patient selection strategy: TFE3 FISH/IHC confirmation, VEGFR expression profiling, and exploration of molecular predictors of response

> ⚠️ *This report is intended for research reference only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before application in patient care.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

