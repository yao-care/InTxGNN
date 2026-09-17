---
layout: default
title: Trastuzumab
parent: High Evidence (L1-L2)
nav_order: 849
evidence_level: L1
indication_count: 10
---

# Trastuzumab
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Trastuzumab: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

Trastuzumab is a monoclonal antibody established for the treatment of HER2-overexpressing breast cancer. The TxGNN model predicts it may also be effective for **progesterone-receptor (PR) positive breast cancer**, a HER2+/PR+ molecular subgroup that sits largely within trastuzumab's existing clinical use rather than representing a truly novel indication. This direction is supported by **36 registered clinical trials** (including several completed Phase 3 RCTs) and **20 publications**, though few trials specifically isolate the PR-positive subgroup as a standalone eligibility criterion.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (well-established use; no formal India registration record found in this evidence pack — see Data Gap below) |
| Predicted New Indication | Progesterone-Receptor Positive Breast Cancer |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Trastuzumab is a humanized IgG1 monoclonal antibody directed against the extracellular domain of HER2/erbB-2. It inhibits proliferation of HER2-overexpressing tumor cells and also acts as a potent mediator of antibody-dependent cell-mediated cytotoxicity (ADCC), as described across the trial evidence (e.g., NCT01785420).

Progesterone-receptor positive breast cancer, as predicted here, refers specifically to the subset of breast cancers that are **both HER2-overexpressing and PR-positive** — a well-recognized clinical subgroup (sometimes called "triple-positive" when ER is also positive). This is not a mechanistically distant new indication; it is a hormone-receptor-defined stratification within trastuzumab's existing HER2-targeted therapeutic space. Studies such as TBCRC 023 (NCT00999804, lapatinib + trastuzumab in HER2-overexpressing breast cancer) and the dedicated letrozole + trastuzumab trial in ErbB2+/ER-and-or-PR+ metastatic breast cancer (PMID 26253814 context; NCT00134680) directly support activity in this HR-positive HER2+ population.

The evidence pack itself flags that the empty `original_indications` field is a **database curation gap**, not evidence that the mechanism is unclear — trastuzumab's anti-HER2 mechanism and its applicability to HER2+/PR+ tumors are well documented in the clinical trial and guideline literature (e.g., ASCO 2022 guideline update, PMID 35640077).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) | Phase 2 | Active, not recruiting | 128 | Randomized neoadjuvant trial of lapatinib + trastuzumab, with/without endocrine therapy, in HER2-overexpressing breast cancer |
| [NCT05802225](https://clinicaltrials.gov/study/NCT05802225) | Phase 3 | Active, not recruiting | 398 | BCD-178 vs Perjeta as neoadjuvant HER2-targeted therapy in HER2-positive breast cancer |
| [NCT00446030](https://clinicaltrials.gov/study/NCT00446030) | Phase 2 | Completed | 127 | Docetaxel-based regimens ± bevacizumab/trastuzumab for adjuvant treatment of node-positive/high-risk breast cancer; cardiac safety endpoint |
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Phase 2 | Completed | 33 | Letrozole + trastuzumab in ErbB2-positive, ER and/or PR-positive metastatic breast cancer — directly matches the predicted PR+/HER2+ population |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Phase 2 | Unknown | 7 | Chemotherapy-free neoadjuvant aromatase inhibitor + pertuzumab/trastuzumab in HR+ (ER+ and/or PR+), HER2+ localized breast cancer |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3270 | Adjuvant chemotherapy alone vs chemotherapy + trastuzumab in node-positive/high-risk HER2-low invasive breast cancer |
| [NCT00005970](https://clinicaltrials.gov/study/NCT00005970) | Phase 3 | Completed | 3436 | AC followed by paclitaxel with/without trastuzumab as adjuvant treatment for HER2-overexpressing node-positive/high-risk breast cancer |
| [NCT01785420](https://clinicaltrials.gov/study/NCT01785420) | Phase 3 | Recruiting | 1100 | Placebo-controlled trial of short-duration preoperative trastuzumab in HER2-positive operable breast cancer |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | Completed | 652 | Taxane-based chemotherapy + lapatinib vs + trastuzumab as first-line therapy in HER2-positive metastatic breast cancer |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Completed | 454 | Atezolizumab vs placebo added to neoadjuvant chemo + trastuzumab + pertuzumab in early HER2-positive breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | RCT (monarcHER) | The Lancet Oncology | Abemaciclib + trastuzumab ± fulvestrant vs chemo + trastuzumab in HR+/HER2+ advanced breast cancer |
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | RCT (ExteNET), Phase 3 | The Lancet Oncology | Neratinib after trastuzumab-based adjuvant therapy in HER2-positive breast cancer |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT long-term follow-up (NeoSphere) | The Lancet Oncology | 5-year outcomes of neoadjuvant pertuzumab + trastuzumab in HER2-positive breast cancer |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | RCT, Phase 3 | British Journal of Cancer | Pertuzumab biosimilar + trastuzumab + docetaxel in HER2-positive, ER/PR-negative breast cancer (equivalence trial) |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | J Clin Oncol | ASCO guideline update on systemic therapy for advanced HER2-positive breast cancer |
| [26253814](https://pubmed.ncbi.nlm.nih.gov/26253814/) | 2015 | Review | Breast (Edinburgh) | Clinical implications of intrinsic molecular subtypes of breast cancer, incl. HER2/HR interplay |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Review | Pharmacological Research | Overview of targeted and cytotoxic inhibitors used in breast cancer treatment |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | Cohort/multi-omics | Theranostics | Molecular portraits and trastuzumab responsiveness of ER+/PR+/HER2+ ("triple-positive") breast cancer |
| [34983437](https://pubmed.ncbi.nlm.nih.gov/34983437/) | 2022 | Retrospective cohort | BMC Cancer | Trastuzumab + fulvestrant combination therapy in HR+/HER2+ advanced breast cancer |
| [40544074](https://pubmed.ncbi.nlm.nih.gov/40544074/) | 2025 | Cost-effectiveness analysis | Clinical Therapeutics | Economic comparison of HER2-targeted ADCs in HR+/HER2-low metastatic breast cancer |

---

## India Market Information

No CDSCO registration records are available for Trastuzumab in this evidence pack — the drug's `market_status` is recorded as **Not Marketed** with **0 total licenses**. This should be treated as a data gap requiring direct verification against CDSCO records before any regulatory or commercial decision is made.

---

## Cytotoxicity

Trastuzumab is an antineoplastic biologic (targeted anti-HER2 monoclonal antibody), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-HER2 humanized monoclonal antibody; not a conventional cytotoxic chemotherapeutic) |
| Myelosuppression Risk | Low as monotherapy; risk becomes moderate-to-high when co-administered with cytotoxic partners (e.g., taxanes, anthracyclines) seen across the trial evidence above |
| Emetogenicity Classification | Low (monoclonal antibody backbone; emetogenicity in combination regimens is driven by the chemotherapy partner, not trastuzumab itself) |
| Monitoring Items | Cardiac function (baseline and serial LVEF via echocardiogram/MUGA — key class-specific risk), infusion-related reactions, pulmonary function if combined with taxanes, CBC when co-administered with myelosuppressive chemotherapy |
| Handling Protection | Handle per institutional hazardous drug policy for biologic/monoclonal antibody agents; formal TFDA/CDSCO-level handling and disposal guidance is not available in this evidence pack (see Data Gap DG001) |

---

## Safety Considerations

- **Drug Interactions**: DDI screening returned 94 total interactions. Notable **Major**-severity interactions include Deferiprone, Samarium (153Sm) lexidronam, Adalimumab, and Baricitinib. Notable **Moderate**-severity interactions include Warfarin, Dicoumarol, Paclitaxel, Zidovudine, Chloramphenicol (systemic and ophthalmic), Roflumilast, Palifermin, Strontium chloride Sr-89, Alemtuzumab, Alefacept, Anakinra, Azathioprine, Canakinumab, and Clostridium tetani toxoid antigen.

Formal key warnings and contraindications from an official product label are not available in this evidence pack and must be sourced directly from the manufacturer's package insert before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted PR-positive breast cancer indication is supported by strong, high-quality evidence (L1: multiple completed Phase 3 RCTs) and is mechanistically coherent, since it represents a hormone-receptor-defined subgroup within trastuzumab's existing HER2-targeted therapeutic space rather than an unrelated new use. However, this drug is currently **not marketed in India (0 registrations)**, and a **blocking safety data gap** (missing official label warnings/contraindications) prevents completion of even a preliminary safety screen.

**To proceed, the following is needed:**
- Official India (CDSCO) product label with warnings, contraindications, and dosing information (currently blocking — DG001)
- Formal, source-verified mechanism of action documentation from DrugBank or the manufacturer (currently a data gap — DG002)
- Confirmation of India market entry/registration pathway, since the drug is presently unmarketed in this jurisdiction
- Trial-level relevance grading for the ~26 "pending" clinical trials and ~15 "pending" publications currently listed without a relevance assessment
- Clarification of whether the predicted indication should be scoped narrowly to HER2+/PR+ tumors (where mechanistic support is strongest) rather than PR-positive breast cancer broadly (which includes HER2-negative disease outside trastuzumab's mechanism of action)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

