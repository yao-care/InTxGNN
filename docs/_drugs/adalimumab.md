---
layout: default
title: Adalimumab
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 6
---

# Adalimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Adalimumab: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Adalimumab is a fully humanized anti-TNF-α monoclonal antibody, widely approved globally for the treatment of rheumatoid arthritis, ankylosing spondylitis, and psoriatic arthritis.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**, with **5 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid Arthritis (globally established primary indication; no India registration on file) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the India regulatory database. Based on information drawn from clinical trial descriptions and literature within this evidence pack, Adalimumab is a fully humanized IgG1 monoclonal antibody that specifically binds to and neutralizes tumor necrosis factor-alpha (TNF-α), thereby blocking its interaction with the p55 and p75 TNF receptor subtypes. It is one of the most frequently prescribed TNF-α inhibitors globally, with established efficacy in RA, ankylosing spondylitis, psoriatic arthritis, and inflammatory bowel disease.

Rheumatoid vasculitis (RV) is one of the most severe extra-articular manifestations of RA, characterized by systemic inflammation of blood vessel walls mediated by immune complex deposition, complement activation, and sustained TNF-α signaling. TNF-α plays a central pathogenic role by promoting vascular endothelial activation and inflammatory cell infiltration into vessel walls—mechanistically the same pathway that Adalimumab targets in the joint. A 2021 systematic review (PMID 33058033) confirms that biological agents, including TNF-α inhibitors, have been incorporated into the therapeutic armamentarium for RV. Case reports also document direct clinical benefit: digital vasculitis with necrotizing ulceration in an RA patient responded well to Adalimumab (PMID 25133007), and an acute pulmonary hypertension crisis emerged following Adalimumab dose reduction in an RV patient (PMID 30773522), highlighting the drug's active role in suppressing RV activity.

However, an important dual safety concern must be noted: TNF-α inhibitors—including Adalimumab—can paradoxically induce vasculitis-like events in some patients (PMID 28719435, PMID 28123776). This means careful patient selection, monitoring, and attribution of any new vasculitic symptoms are essential before and during treatment.

---

## Clinical Trial Evidence

> ⚠️ **Important**: None of the 5 retrieved clinical trials were specifically designed to evaluate Adalimumab in rheumatoid vasculitis. No dedicated Phase 2/3 RCTs for this specific indication currently exist.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completed | 808 | Cross-sectional observational study of biologic DMARD treatment patterns in Chinese RA patients; single-visit design with no follow-up; provides background data on RA population receiving biologics but not designed to evaluate vasculitis endpoints |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Non-interventional observational study of Tocilizumab (not Adalimumab) in RA patients with inadequate DMARD response in Eastern Europe; 6-month follow-up; indirectly relevant as comparator context |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large pharmacovigilance study evaluating incident IMID risk in patients receiving biologics or immunosuppressants for a single IMID condition; provides broad safety background for Adalimumab in systemic inflammatory contexts; study status requires verification |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Study assessing preoperative immunosuppressant management (including Adalimumab hold/continue) in rheumatology patients undergoing elective total shoulder arthroplasty; not related to vasculitis indication |
| [NCT05111743](https://clinicaltrials.gov/study/NCT05111743) | N/A | Completed | 9,261 | ⚠️ **Misclassified**: Retrospective cohort study of brolucizumab for wet age-related macular degeneration — completely unrelated to rheumatoid vasculitis; should be excluded from this indication analysis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical Rheumatology | PRISMA-based systematic review of biological therapy in rheumatoid vasculitis; covers TNF-α inhibitors including adalimumab; highest-level available evidence for biologic use in RV |
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Network Meta-analysis | Int J Mol Sci | Network meta-analysis of 36 RCTs comparing 5 TNFi agents (infliximab, etanercept, adalimumab, certolizumab, golimumab) on joint destruction in RA; confirms TNFi class efficacy including adalimumab across doses |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Pharmacovigilance | RMD Open | BSRBR-RA registry analysis comparing drug-specific risk of lupus-like and vasculitis-like events in TNFi-treated RA patients vs nbDMARDs; critical data for understanding both therapeutic and paradoxical vasculitis risk |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | Review | J Clin Med | Review of RA-associated episcleritis and scleritis treatment; discusses biologics including adalimumab for management of RA-related ocular vasculitic inflammation |
| [38931826](https://pubmed.ncbi.nlm.nih.gov/38931826/) | 2024 | PK Study | Pharmaceutics | Population PK analysis of adalimumab and etanercept biosimilar dosing intervals in RA patients; explores whether therapeutic drug levels can be achieved faster with alternative dosing strategies |
| [25133007](https://pubmed.ncbi.nlm.nih.gov/25133007/) | 2014 | Case Report | Case Rep Rheumatol | 42-year-old female with 15-year RA history and digital vasculitis (necrotizing ulcer of 1st and 2nd fingertips); responded well to adalimumab — direct clinical evidence of benefit in RV |
| [30773522](https://pubmed.ncbi.nlm.nih.gov/30773522/) | 2019 | Case Report | Internal Medicine | Acute pulmonary hypertension crisis in RV patient 8 months after adalimumab dose reduction; underscores the importance of sustained TNFi therapy in controlling systemic RV and risks of tapering |
| [28719435](https://pubmed.ncbi.nlm.nih.gov/28719435/) | 2018 | Case Report | Am J Dermatopathol | First reported case of leukocytoclastic vasculitis with cutaneous perivascular hemophagocytosis associated with adalimumab therapy; key safety signal for paradoxical TNFi-induced vasculitis |
| [21385558](https://pubmed.ncbi.nlm.nih.gov/21385558/) | 2011 | Case Report | Clin Exp Rheumatol | Successful use of anti-IL-6 receptor antibody (tocilizumab) in a patient with multidrug-refractory, anti-TNF-resistant systemic RV; provides alternative pathway data when adalimumab fails or is contraindicated |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Case Report | Internal Medicine | ANCA-associated necrotizing glomerulonephritis emerging during combined abatacept + adalimumab therapy for RA; tocilizumab attenuated the nephritis; highlights complex immune interactions in RV management |

---

## India Market Information

Adalimumab (DrugBank ID: DB00051) currently has **no registered products in India** (CDSCO). No license records are available in this evidence pack.

Although Adalimumab is globally approved by the FDA (USA), EMA (EU), and PMDA (Japan) for indications including rheumatoid arthritis, ankylosing spondylitis, psoriatic arthritis, Crohn's disease, and psoriasis, it has not yet received CDSCO marketing authorization in India as of the data cutoff (2026-04-04). Any clinical application in India would require regulatory filing and approval.

---

## Safety Considerations

**Drug Interactions** (353 total documented; major and moderate interactions listed below):

*Major interactions:*

| Interacting Drug | Level | Note |
|------|------|------|
| Betamethasone | Major | Combined immunosuppression increases serious infection risk |
| Budesonide | Major | Combined immunosuppression increases serious infection risk |
| Dexamethasone | Major | Combined immunosuppression increases serious infection risk |
| Hydrocortisone | Major | Combined immunosuppression increases serious infection risk |
| Prednisolone | Major | Combined immunosuppression increases serious infection risk |
| Prednisone | Major | Combined immunosuppression increases serious infection risk |
| Triamcinolone | Major | Combined immunosuppression increases serious infection risk |
| Triamcinolone (ophthalmic) | Major | Combined immunosuppression increases serious infection risk |
| Deferiprone | Major | Risk of agranulocytosis/neutropenia with concurrent use |
| Ibritumomab tiuxetan | Major | Additive immunosuppression; increased risk of serious infection and bone marrow suppression |
| Iobenguane (I-131) | Major | Additive immunosuppression |
| Tositumomab (I-131) | Major | Additive immunosuppression |
| Tositumomab | Major | Additive immunosuppression |

*Moderate interactions:*

| Interacting Drug | Level | Note |
|------|------|------|
| Metronidazole | Moderate | Pharmacodynamic interaction; monitor closely |
| Tinidazole | Moderate | Pharmacodynamic interaction; monitor closely |
| Rosuvastatin | Moderate | Monitor for signs of statin-related myopathy |
| Simvastatin | Moderate | Monitor for signs of statin-related myopathy |

> Formal package insert warnings and contraindications for the India market are not yet available (Data Gap DG001). Refer to the globally approved prescribing information. Key known precautions include: mandatory tuberculosis (TB) screening and treatment of latent TB before initiation; monitoring for serious infections, hepatitis B reactivation, malignancy, demyelinating disorders, and heart failure.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Adalimumab's TNF-α inhibition is biologically plausible for rheumatoid vasculitis given TNF-α's central role in RV pathology, and the best available evidence (systematic review PMID 33058033; case series with clinical response PMID 25133007, 30773522) is encouraging. However, the absence of dedicated Phase 2/3 RCTs, the paradoxical vasculitis induction risk documented with TNFi therapy, and the zero-registration status in India mean this cannot advance to clinical use without further research and regulatory groundwork.

**To proceed, the following is needed:**
- Design and conduct a prospective cohort study or dedicated Phase 2 RCT specifically enrolling confirmed rheumatoid vasculitis patients, using standardized outcome tools (BVAS, VDI)
- Establish clear patient selection criteria distinguishing TNFi-responsive RV from paradoxical TNFi-induced vasculitis, with predefined monitoring and stopping rules
- Obtain the formal India package insert / MOA documentation to complete safety assessment (Data Gaps DG001 and DG002)
- Initiate CDSCO regulatory filing for India market authorization before any clinical use
- Mandate pre-treatment latent TB screening and hepatitis B serology for all patients
- Establish a drug monitoring plan tracking anti-adalimumab antibodies (immunogenicity) and trough levels to optimize dosing in the RV patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

