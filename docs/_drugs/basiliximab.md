---
layout: default
title: Basiliximab
parent: Model Prediction Only (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Basiliximab: predicted new indication Plasma cell myeloma (evidence level L5). Approved use: Not specified in the Indian licence data compiled for this report"
monitor_inn: "Basiliximab"
predicted_indications: ["plasma cell myeloma", "bronchitis", "indolent plasma cell myeloma", "hemoglobinopathy", "gastric carcinoma", "diffuse gastric adenocarcinoma", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "Jeune syndrome situs inversus"]
---

# Basiliximab
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

## Basiliximab: From Transplant Rejection Prophylaxis to Plasma Cell Myeloma
{: .text-alpha }

## One-Sentence Summary

Basiliximab is an anti-CD25 (IL-2 receptor alpha) monoclonal antibody marketed in India as Simulect Injection. The TxGNN model predicts it may be relevant for **plasma cell myeloma**, with **3 clinical trials** and **4 publications** currently linked to this direction. These studies concern transplant-related immune modulation and GVHD prevention, not direct anti-myeloma activity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the Indian licence data compiled for this report |
| Predicted New Indication | Plasma cell myeloma |
| TxGNN Prediction Score | 95.61% |
| Evidence Level | L2 (as assigned in the compiled data; the supporting trials are small Phase 1/2 studies with no efficacy conclusions, so this level should be read cautiously) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold (research question only) |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. From its known pharmacology, basiliximab blocks the IL-2 receptor alpha chain (CD25) on activated T cells and regulatory T cells (Tregs). This limits T-cell activation, and it can deplete or suppress Tregs.

In myeloma, basiliximab has been studied as a supportive agent rather than an anti-myeloma drug. One approach uses it to deplete activated T cells and prevent graft-versus-host disease (GVHD) after nonmyeloablative allogeneic transplant. The other uses it to reduce Tregs around autologous stem cell transplantation, which may release the anti-myeloma immune response, since Tregs reconstitute rapidly after transplant and can suppress it.

The link is therefore immunomodulatory and transplant-related. There is no evidence that basiliximab kills plasma cells directly. Basiliximab is also used to prevent rejection after transplantation, and this setting overlaps with the transplant context of myeloma treatment.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01526096](https://clinicaltrials.gov/study/NCT01526096) | Phase 1 | Completed | 30 | Pilot of regulatory T-cell depletion during autologous stem cell transplantation in myeloma; the most mechanistically relevant study, but exploratory with no efficacy conclusion |
| [NCT00975975](https://clinicaltrials.gov/study/NCT00975975) | Phase 2 | Completed | 17 | Basiliximab plus cyclosporine for GVHD prevention after nonmyeloablative allotransplant in blood cancers; endpoint is GVHD, not myeloma control |
| [NCT00594308](https://clinicaltrials.gov/study/NCT00594308) | NA | Terminated | 10 | Basiliximab plus cyclosporine vs cyclosporine alone for GVHD prevention; very small and terminated early, so little interpretable efficacy evidence |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31940591](https://pubmed.ncbi.nlm.nih.gov/31940591/) | 2020 | Phase 1 trial report | Journal for Immunotherapy of Cancer | Pilot of Treg depletion around autologous stem cell transplantation for myeloma, motivated by immune dysfunction as a cause of post-transplant progression |
| [12476283](https://pubmed.ncbi.nlm.nih.gov/12476283/) | 2002 | Cohort | Bone Marrow Transplantation | Basiliximab was reported to be well tolerated and effective in 17 patients with steroid-refractory acute GVHD, including one with multiple myeloma |
| [42379467](https://pubmed.ncbi.nlm.nih.gov/42379467/) | 2026 | Case report/Review | American Journal of Kidney Diseases | Kidney transplantation after CAR T-cell therapy in myeloma; context is transplant management, not basiliximab efficacy against myeloma |
| [28320553](https://pubmed.ncbi.nlm.nih.gov/28320553/) | 2017 | Case reports | American Journal of Kidney Diseases | Four kidney transplants in patients with myeloma-related kidney failure; transplant context only |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 201030 | Simulect Injection (Novartis India Ltd) | Vial of 1 injection | Not stated in the compiled licence data |

## Safety Considerations

- **Drug Interactions:** 69 interactions were identified in the data compiled for this report. Those listed include:
  - **Major:** adalimumab, baricitinib, certolizumab pegol, and BCG live vaccine (Tice substrain)
  - **Moderate:** alemtuzumab, alefacept, anakinra, azathioprine, canakinumab, roflumilast, and several vaccines (tetanus toxoid, anthrax, adenovirus type 4, live cholera)
  - **Minor:** zinc salts (acetate, gluconate, sulfate, chloride)

  The pattern reflects additive immunosuppression and interference with vaccines, especially live vaccines.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold (research question only)**

**Rationale:**
The evidence for myeloma consists of a Phase 1 Treg-depletion pilot and two small GVHD-prevention studies, with no efficacy data against myeloma itself. The mechanism is supportive and immunomodulatory rather than anti-tumour. Strong immunosuppression is also a potential concern in cancer, and the safety data for this product is incomplete.

**To proceed, the following is needed:**
- Results and efficacy outcomes from the completed Treg-depletion pilot (NCT01526096 / PMID 31940591), and larger controlled studies in myeloma
- Detailed mechanism-of-action data
- Package insert warnings, contraindications, and the approved indication for Simulect in India
- A safety review of infection risk and drug interactions in myeloma patients

## Other Predicted Indications (Brief Note)

- **Hemoglobinopathy (95% below the top score; 94.28%):** A completed Phase 4 trial of 205 patients (NCT02342145) supports basiliximab for acute GVHD prevention in unrelated stem cell transplant for thalassemia major. The benefit is in the transplant setting, not the underlying globin disorder. This is worth reviewing as a separate transplant-supportive use.
- **Bronchitis, gastric carcinoma, and other entries:** These have no supporting therapeutic rationale. The bronchitis signal likely reflects term overlap with bronchiolitis obliterans syndrome after lung transplant, and the gastric carcinoma literature is a coincidental case report. Several others (indolent myeloma, beta-thalassemia with other manifestations, rare syndromes) rest on model prediction alone.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

