---
layout: default
title: Abatacept
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 10
---

# Abatacept
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

# Abatacept: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Abatacept (Orencia) is a selective T-cell costimulation modulator (CTLA4-Ig fusion protein) globally approved for rheumatoid arthritis (RA) and polyarticular juvenile idiopathic arthritis, though not yet licensed in India.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**, with **1 clinical trial** and **20 publications** currently identified in support of this direction.
Evidence remains predominantly at the case report and observational level (Evidence Level L3), positioning this as a promising research question rather than an established indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid Arthritis (globally approved by FDA/EMA; not licensed in India) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this evidence pack. Based on known pharmacological information, Abatacept is a fusion protein composed of the Fc region of IgG1 fused to the extracellular domain of CTLA-4. It selectively blocks the CD80/CD86–CD28 co-stimulatory axis required for full T-cell activation, thereby suppressing downstream T-effector cell proliferation, cytokine release, and B-cell helper function. This mechanism is distinct from cytokine-targeting biologics (e.g., anti-TNF or anti-IL-6 agents) in that it acts upstream at the T-cell priming stage.

Rheumatoid Vasculitis (RV) is a severe extra-articular complication of longstanding RA, characterised by immune complex deposition in vessel walls and T-cell-driven vascular inflammation. The pathological drivers of RV substantially overlap with those of RA itself — dysregulated CD4+ T-cell activation and B-cell-mediated humoral immunity are central to both conditions. Abatacept's mechanism of suppressing T-cell co-stimulation is therefore mechanistically congruent with interrupting the immunological processes underlying RV, particularly in patients where B-cell depletion (rituximab) is contraindicated or has failed.

Published case reports provide preliminary clinical proof-of-concept. Two cases describe rapid improvement in RV following abatacept therapy (PMID 29930884, PMID 22124545), including one patient refractory to methotrexate, TNF inhibitors, steroids, immunoadsorption plasmapheresis, and IL-6 inhibition. However, a cautionary case (PMID 27052429) documents new onset of RV *during* abatacept therapy with subsequent improvement only after switching to rituximab — underscoring that T-cell costimulation blockade alone may not be sufficient in all RV phenotypes, and patient selection will be critical.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing total shoulder arthroplasty; assesses flare rates and wound complications when biologics (including Abatacept) are held vs. continued. Abatacept is a background medication here — this trial does not directly evaluate RV treatment efficacy. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [29930884](https://pubmed.ncbi.nlm.nih.gov/29930884/) | 2018 | Case Series / Review | Cureus | Abatacept (CTLA4-Ig) used as therapeutic option for confirmed RV in a patient with RA and common variable immunodeficiency; rituximab was contraindicated due to risk of exacerbating immunodeficiency — describes rationale for choosing abatacept |
| [22124545](https://pubmed.ncbi.nlm.nih.gov/22124545/) | 2012 | Case Report | Modern Rheumatology | 38-year-old woman with RV refractory to MTX, TNF inhibitors, steroids, immunoadsorption plasmapheresis, and IL-6 inhibitor; abatacept administration produced rapid clinical improvement with near-normalisation of inflammatory markers |
| [30119075](https://pubmed.ncbi.nlm.nih.gov/30119075/) | 2018 | Case Series | Ophthalmic Plastic & Reconstructive Surgery | RA patient presenting with bilateral orbital lesions while on abatacept; biopsy revealed vasculitis with eosinophilic infiltrate; initial response to cyclophosphamide followed by disease progression — illustrates complex immune dynamics in biologic-treated RV |
| [27052429](https://pubmed.ncbi.nlm.nih.gov/27052429/) | 2016 | Case Report | Joint Bone Spine | New onset of RV during abatacept therapy; subsequent improvement achieved after switching to rituximab — important cautionary case highlighting that abatacept may be insufficient for some RV phenotypes |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | Narrative Review | Journal of Clinical Medicine | Overview of episcleritis and scleritis as ocular manifestations of RA (present in 2–15% of RA-associated scleritis); reviews biologic treatment escalation including T-cell pathway modulators in refractory cases |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Case Report | Internal Medicine (Tokyo) | ANCA-associated nephritis (pauci-immune pattern) developing during combined abatacept + adalimumab therapy; tocilizumab attenuated the vasculitic renal injury — relevant safety case for immune-mediated vascular events on biologic therapy |
| [31174819](https://pubmed.ncbi.nlm.nih.gov/31174819/) | 2018 | Review | Best Practice & Research Clinical Rheumatology | Review of CNS involvement in RA including cerebral vasculitis, rheumatoid nodules, and meningitis; discusses implications of biologics including abatacept for CNS manifestations |
| [41117362](https://pubmed.ncbi.nlm.nih.gov/41117362/) | 2026 | Review | European Journal of Clinical Investigation | Summarises early diagnostic and therapeutic approaches in inflammatory and autoimmune rheumatic diseases including RA and large-vessel vasculitis in polymyalgia rheumatica; provides updated context for vasculitic pathophysiology |
| [24493331](https://pubmed.ncbi.nlm.nih.gov/24493331/) | 2015 | Case-based Review | Clinical Rheumatology | Abatacept as successful therapy for myositis — demonstrates broader off-label efficacy of abatacept in T-cell-driven inflammatory conditions beyond RA; supports mechanistic plausibility in related autoimmune vasculopathies |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Review | BMC Medicine | Update on biologic therapies for autoimmune diseases; positions abatacept within the broader immune-modulating landscape and discusses limitations and adverse event profiles relevant to repurposing decisions |

---

## India Market Information

Abatacept is currently **not licensed in India**. No product registrations are on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | No registrations found | — | — |

> **Note:** Abatacept is approved globally under the brand name **Orencia** (Bristol-Myers Squibb) by the FDA (since 2005 for RA) and EMA, for Rheumatoid Arthritis and Polyarticular Juvenile Idiopathic Arthritis. Its absence from the Indian market represents an unmet access gap rather than a safety or efficacy concern at the global level.

---

## Safety Considerations

**Drug Interactions** (73 interactions identified total — selected key interactions shown below):

*Major interactions — avoid or use with extreme caution:*
- **Adalimumab**: Combining two biologics markedly increases serious infection risk; concomitant use is generally contraindicated
- **Baricitinib**: Biologic + JAK inhibitor combination substantially elevates infection risk; avoid concurrent use
- **Certolizumab pegol**: Same concern as adalimumab; dual biological immunosuppression is not recommended
- **BCG vaccine (live, Tice strain)**: Live vaccines must not be administered during abatacept therapy due to risk of disseminated infection in an immunocompromised host

*Moderate interactions — monitor closely:*
- **Anakinra, Canakinumab, Alemtuzumab, Alefacept**: Additive immunosuppression; increased infection and lymphopenia risk
- **Live/attenuated vaccines** (Anthrax, Cholera CVD 103-HgR, Adenovirus): Reduced vaccine efficacy and potential safety risk; timing of vaccination relative to therapy must be planned carefully
- **Azathioprine**: Additive myelosuppression and infection risk; monitor CBC and hepatic function
- **Roflumilast**: Additive immunosuppression; heightened infection surveillance warranted
- **Bifidobacterium longum infantis**: Probiotic use in immunocompromised patients requires caution

*Minor interactions — routine monitoring sufficient:*
- **Zinc acetate, Zinc gluconate, Zinc sulfate, Zinc chloride**: Minor interaction; no dose adjustment required under normal circumstances

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The mechanistic link between Abatacept's T-cell costimulation blockade and the T-cell-driven pathogenesis of Rheumatoid Vasculitis is biologically plausible, and published case reports confirm clinical responses in individual patients — particularly those unable to receive rituximab. However, evidence is entirely at the case report/case series level (L3), no randomised controlled trial data exist for this indication, and at least one case documents RV onset *during* abatacept therapy, signalling heterogeneity in response that requires further characterisation before any practice change can be recommended.

**To proceed, the following is needed:**
- Obtain full package insert (TFDA/FDA SmPC) to document complete safety warnings and contraindications (currently unavailable — a blocking data gap)
- Retrieve DrugBank MOA data to enable formal mechanistic linkage analysis
- Establish a prospective case registry for RV patients receiving abatacept to build structured real-world evidence
- Design a pilot clinical trial (Phase 2 open-label) comparing abatacept to rituximab in patients with confirmed RV — particularly targeting the subgroup where rituximab is contraindicated
- Define response biomarkers (e.g., T-cell subsets, ACPA, RF levels) to prospectively identify which RV patients are most likely to benefit from T-cell costimulation blockade
- Develop an India-specific regulatory and access strategy given zero current market presence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

