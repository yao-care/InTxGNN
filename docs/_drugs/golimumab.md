---
layout: default
title: Golimumab
parent: 僅模型預測 (L5)
nav_order: 396
evidence_level: L5
indication_count: 5
---

# Golimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Golimumab: From Inflammatory Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Golimumab is a fully human anti-TNF-α monoclonal antibody used for inflammatory arthritis (rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis) based on literature evidence in this pack.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**, with **3 clinical trials** and **6 publications** currently identified, though none directly tests golimumab in this population — evidence is mechanism-based rather than confirmatory.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this pack (no TFDA license on file); literature evidence (PMID 28530020) describes approval for rheumatoid arthritis, psoriatic arthritis, and axial spondyloarthritis (AS/nr-axSpA) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is flagged as a data gap in this pack (DG002). However, literature evidence within the pack (PMID 28530020, 20065639) describes golimumab as a fully human IgG1κ monoclonal antibody that binds both soluble and transmembrane TNF-α, blocking its interaction with TNF receptors — the basis for its approved use in rheumatoid arthritis (RA), psoriatic arthritis, axial spondyloarthritis, and (via the IV formulation in some markets) polyarticular juvenile idiopathic arthritis.

Rheumatoid vasculitis (RV) is a severe extra-articular complication of long-standing, seropositive RA, driven by immune-complex-mediated vascular inflammation in which TNF-α is implicated. One case report in this pack (PMID 29075910) notes that RV incidence has declined since the introduction of anti-TNF biologics, supporting the biological plausibility of TNF blockade for RV.

That said, the same evidence pack also contains a countervailing signal: a case report of anti-TNF therapy being associated with **paradoxical** large-vessel vasculitis (Takayasu's arteritis, PMID 22999907) arising *during* treatment. This means the mechanistic direction is not unambiguous — anti-TNF agents can, in rare instances, trigger or unmask vasculitic phenomena rather than suppress them. Combined with the complete absence of RV-specific trials, this uncertainty underlies the L4 evidence level and Hold recommendation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Observational study of tocilizumab (not golimumab) in RA patients with inadequate response to DMARDs; general RA practice patterns, not RV-specific |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large cohort study on risk of developing a second immune-mediated inflammatory disease (IMID) in patients on biologics; not a golimumab/RV intervention study |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty; no direct RV or golimumab efficacy data |

**Note:** None of the identified trials directly evaluates golimumab for rheumatoid vasculitis; all three are graded "C" (low relevance) in the source evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Network meta-analysis (RCTs) | Int J Mol Sci | Compares golimumab and 4 other TNF inhibitors vs. methotrexate on radiographic joint destruction in RA; not RV-specific |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Review | BMC Medicine | General overview of biologic therapies for autoimmune/rheumatologic disease |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Cohort | Semin Arthritis Rheum | Frequency and causes of end-stage renal disease in RA patients; not golimumab/RV-specific |
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Case report | Rheumatol Int | Severe pyoderma gangrenosum/septic arthritis in an RA patient on golimumab; notes RV incidence has declined in the anti-TNF era |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Case report | Joint Bone Spine | Two cases of Takayasu's arteritis (large-vessel vasculitis) arising **during** anti-TNF therapy — a paradoxical safety signal |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Case report | Ocul Immunol Inflamm | Golimumab successfully used off-label for Behçet disease-associated uveitis (a different vasculitis-associated condition) |

---

## Taiwan Market Information

Golimumab is currently **not marketed** in Taiwan (TFDA) per this evidence pack (0 registrations on file). No product license, brand name, or approved-indication text is available.

---

## Safety Considerations

- **Drug Interactions**: The DDI database records 352 total interactions for golimumab (20 sampled in this pack). Notable **Major**-level interactions include systemic corticosteroids (Hydrocortisone, Prednisone, Prednisolone, Dexamethasone, Betamethasone, Triamcinolone, Budesonide) — combined immunosuppression/infection risk — as well as Deferiprone and radiolabeled/immunogenic biologics (Iobenguane I-131, Ibritumomab tiuxetan, Tositumomab/Tositumomab I-131). **Moderate**-level interactions include Rosuvastatin, Simvastatin, Metronidazole, and Tinidazole. **Minor**-level interactions include zinc salts (sulfate, acetate, gluconate).

Key warnings and contraindications are not available in this evidence pack (TFDA label data flagged as a Blocking data gap, DG001) — refer to the package insert for full safety information.

---

## Other Predicted Indications in This Evidence Pack

This evidence pack (`TW-DB06674-multi`) contains 5 ranked TxGNN predictions for golimumab. Two other candidates have **substantially stronger** direct clinical evidence than the top-ranked prediction above and warrant separate attention:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|-------------|-----------------|-----------------|------|
| 3 | Inflammatory spondylopathy | 99.66% | **L1** | **Proceed with Guardrails** | Multiple completed Phase 3 RCTs directly testing golimumab in axial spondyloarthritis/ankylosing spondylitis (e.g. NCT01453725, NCT00265083, NCT03253796); this is a confirmatory extension of an already-approved mechanism, not a novel hypothesis |
| 5 | Polyarticular juvenile rheumatoid arthritis | 99.59% | **L1** | **Proceed with Guardrails** | Two independent Phase 3 RCTs of IV golimumab in pediatric pJIA (NCT02277444 completed n=130; NCT01230827 terminated n=173 — termination reason should be checked for safety signals) |
| 2 | Hypermobility of coccyx | 99.67% | L5 | Hold | No trials, no literature; structural/mechanical condition with no plausible link to TNF-α inhibition — likely knowledge-graph noise |
| 4 | Kummell disease | 99.61% | L5 | Hold | No trials, no literature; ischemic vertebral collapse, not an autoimmune/inflammatory condition — no plausible mechanistic basis |

If the goal is to identify the most actionable repurposing opportunity for golimumab from this pack, **inflammatory spondylopathy** or **polyarticular JIA** are better-supported candidates than rheumatoid vasculitis and merit their own dedicated evaluation.

---

## Conclusion and Next Steps

**Decision: Hold** (for Rheumatoid Vasculitis)

**Rationale:**
Evidence for golimumab in rheumatoid vasculitis is mechanism-based only (L4) — no clinical trial or study directly evaluates this combination, and the pack itself contains a countervailing case report of anti-TNF-associated paradoxical vasculitis, introducing safety uncertainty rather than confidence.

**To proceed, the following is needed:**
- TFDA label data (key warnings, contraindications) — currently a Blocking data gap (DG001)
- Formal DrugBank MOA confirmation (DG002)
- A dedicated study or registry cohort of RV patients treated with golimumab, given zero direct trials currently exist
- Clarification of the paradoxical vasculitis signal (PMID 22999907) before any safety sign-off
- Separately, consider fast-tracking evaluation of **inflammatory spondylopathy** and **polyarticular JIA** from the same pack, given their L1 evidence and existing Phase 3 RCT support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

