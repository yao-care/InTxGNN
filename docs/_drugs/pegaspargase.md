---
layout: default
title: Pegaspargase
parent: High Evidence (L1-L2)
nav_order: 646
evidence_level: L1
indication_count: 10
---

# Pegaspargase
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

# Pegaspargase: From Acute Lymphoblastic Leukemia to Precursor Lymphoblastic Lymphoma/Leukemia

## One-Sentence Summary

Pegaspargase is a PEGylated *E. coli*-derived L-asparaginase, internationally established as a core component of multi-agent chemotherapy for acute lymphoblastic leukemia (ALL) — though this indication is not yet registered in the local (India) market.
The TxGNN model's top prediction, **Precursor Lymphoblastic Lymphoma/Leukemia**, is essentially the same disease entity as ALL under current WHO classification, so this is best read as a **confirmation of an already-established indication** rather than a novel repurposing signal.
It is backed by **50 clinical trials** (multiple large Phase 3 COG/international protocols) and **20 publications**, giving it the highest achievable evidence tier (L1) in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Lymphoblastic Leukemia (ALL) — per literature evidence (e.g. PMID 31030380: "indicated in the USA and EU for the treatment of ALL"); no local (India) license record exists |
| Predicted New Indication | Precursor Lymphoblastic Lymphoma/Leukemia |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The `original_moa` field is marked as a data gap, and no local approved-indication text exists because the drug is not currently registered in India. However, the evidence pack's own mechanistic rationale supplies a well-established MOA: Pegaspargase is a PEGylated form of L-asparaginase that depletes plasma asparagine. Leukemic lymphoblasts characteristically lack asparagine synthetase and cannot synthesize their own asparagine, making them highly sensitive to this depletion. This is described in the evidence pack as "the drug's core, already-established mechanism of action — not a speculative link."

Precursor lymphoblastic lymphoma/leukemia and acute lymphoblastic leukemia are, in fact, the same biological disease entity (differing mainly by degree of marrow versus extramedullary/nodal involvement), which is why the asparagine-depletion mechanism applies identically to both labels. This explains why the "predicted new indication" is supported by pivotal Phase 3 registration trials rather than early hypothesis-generating studies — the model is essentially re-discovering the drug's standard-of-care indication.

Because the drug is absent from the India regulatory dataset, the practical repurposing question here is less "does the mechanism transfer to a new disease" and more "should this internationally standard oncology agent be introduced/registered locally," which changes the nature of the guardrails needed (see Conclusion).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01190930](https://clinicaltrials.gov/study/NCT01190930) | Phase 3 | Active, not recruiting | 9,350 | COG trial comparing risk-adapted chemotherapy regimens in standard-risk B-ALL/localized B-LLy; pegaspargase is a core induction component |
| [NCT00671034](https://clinicaltrials.gov/study/NCT00671034) | Phase 3 | Completed | 166 | Pivotal RCT comparing calaspargase pegol vs. pegaspargase combination chemotherapy in high-risk pediatric ALL; supported regulatory approval |
| [NCT01117441](https://clinicaltrials.gov/study/NCT01117441) | Phase 3 | Completed | 6,136 | International collaborative treatment protocol for pediatric/adolescent ALL comparing combination chemotherapy regimens |
| [NCT00506597](https://clinicaltrials.gov/study/NCT00506597) | N/A | Completed | 33 | Evaluated Erwinia asparaginase (same-mechanism alternate formulation) as substitute for patients allergic to E. coli/PEG-asparaginase |
| [NCT00186875](https://clinicaltrials.gov/study/NCT00186875) | Phase 2 | Completed | 47 | Etoposide/teniposide-based induction regimen efficacy in relapsed/refractory pediatric ALL |
| [NCT03564470](https://clinicaltrials.gov/study/NCT03564470) | Phase 2/3 | Unknown | 120 | Precision-diagnosis-directed therapy incorporating a PEG-asparaginase-intensified protocol for adult Ph-like ALL |
| [NCT03959085](https://clinicaltrials.gov/study/NCT03959085) | Phase 3 | Recruiting | 5,951 | Evaluates inotuzumab ozogamicin added to risk-adapted post-induction chemo-immunotherapy for high-risk B-ALL/B-LLy |
| [NCT03914625](https://clinicaltrials.gov/study/NCT03914625) | Phase 3 | Active, not recruiting | 6,720 | Studies blinatumomab combined with chemotherapy (incl. pegaspargase) for standard-risk B-ALL/B-LLy, including Down syndrome patients |
| [NCT01225874](https://clinicaltrials.gov/study/NCT01225874) | N/A | Completed | 3,762 | Biomarker-based classification study for pediatric B-precursor ALL induction treatment (ALinC 17) |
| [NCT02716233](https://clinicaltrials.gov/study/NCT02716233) | Phase 3 | Active, not recruiting | 2,044 | French national protocol optimizing L-asparaginase use in pediatric/adolescent ALL treatment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | RCT | J Clin Oncol | COG AALL1231 phase III trial testing bortezomib in newly diagnosed T-ALL/T-LL; also reduced use of prophylactic cranial radiotherapy |
| [27114587](https://pubmed.ncbi.nlm.nih.gov/27114587/) | 2016 | RCT | J Clin Oncol | COG AALL0232 — dexamethasone and high-dose methotrexate improved outcomes in high-risk B-ALL |
| [32813610](https://pubmed.ncbi.nlm.nih.gov/32813610/) | 2020 | RCT | J Clin Oncol | COG AALL0434 phase III trial testing nelarabine in newly diagnosed T-ALL |
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | Cohort | J Clin Oncol | DFCI 11-001 compared efficacy/toxicity of calaspargase pegol vs. standard pegaspargase in childhood ALL |
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Cohort | Blood Advances | GIMEMA LAL1913 — pegaspargase-modified risk-oriented program improved outcomes in adult Ph-negative ALL/LL |
| [39322712](https://pubmed.ncbi.nlm.nih.gov/39322712/) | 2024 | Phase 2 Cohort | Leukemia | Long-term follow-up of venetoclax added to hyper-CVAD/nelarabine/pegylated asparaginase in T-ALL/LBL |
| [21454191](https://pubmed.ncbi.nlm.nih.gov/21454191/) | 2011 | Cohort | Clin Lymphoma Myeloma Leuk | Augmented hyper-CVAD with intensified vincristine/dexamethasone/asparaginase in adult relapsed ALL salvage therapy |
| [32552472](https://pubmed.ncbi.nlm.nih.gov/32552472/) | 2020 | Cohort | J Clin Oncol | COG AALL0434 — Capizzi methotrexate/pegaspargase regimen showed successful outcomes in newly diagnosed pediatric T-LL |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Review | Haematologica | Expert panel consensus on recognition, prevention and management of asparaginase/pegaspargase-associated adverse events in adults |
| [31977001](https://pubmed.ncbi.nlm.nih.gov/31977001/) | 2020 | Review | Blood | Review on managing pegaspargase toxicities, which are unique among chemotherapy agents used in adult ALL |

---

## India Market Information

Pegaspargase currently has **no registered products in India** (`total_licenses: 0`, market status: Not Marketed). No authorization records are available to summarize.

---

## Cytotoxicity

Pegaspargase is an antineoplastic agent (asparagine-depleting enzyme therapy), a standard component of multi-agent chemotherapy for ALL, and is therefore in scope for cytotoxicity assessment.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — antimetabolic enzyme therapy (asparagine-depleting agent), distinct in mechanism from alkylators/antimetabolite nucleoside analogs |
| Myelosuppression Risk | Low-to-moderate when used alone; pegaspargase itself is not primarily myelosuppressive, but it is virtually always combined with myelosuppressive agents (vincristine, corticosteroids, anthracyclines), which drives overall regimen-level marrow toxicity (PMID 40109190, 31977001) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential; liver function (AST/ALT/bilirubin); lipase/amylase for pancreatitis risk (PMID 41023283, 01393249); triglycerides for hypertriglyceridemia (PMID 30823860); coagulation panel — fibrinogen/antithrombin (PMID 01094392); blood glucose; hypersensitivity monitoring |
| Handling Protection | Must follow institutional cytotoxic/hazardous drug handling regulations (preparation, administration, and disposal) despite its enzyme-based rather than classic alkylating mechanism |

---

## Safety Considerations

- **Drug Interactions**: DDI query returned 378 total interactions. A sample of Moderate-level interactions (source: DDInter) includes: Acarbose, Doxycycline, Hydrocortisone, Albiglutide, Alogliptin, Metformin, Bupropion, Triamcinolone, Acetylsalicylic acid, Dexamethasone, Betamethasone, Tetracycline, Budesonide, Canagliflozin, Chenodeoxycholic acid, Chlorpropamide, Clarithromycin, Dapagliflozin, Saxagliptin, and Dulaglutide. Given the volume (378 total), a full DDI screen against the patient's concurrent medication list is recommended before administration rather than relying on this sample.

Key warnings and contraindications are not available in this evidence pack (data gap DG001 — blocking) and should be sourced from the official product label before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The asparagine-depletion mechanism is well-established and directly evidenced by two pivotal Phase 3 trials plus a large body of RCT-level literature — this is not a speculative repurposing signal but confirmation of pegaspargase's internationally recognized standard-of-care role in ALL/precursor lymphoblastic lymphoma. The blocking factor is not efficacy evidence but the absence of local (India) regulatory and label data.

**To proceed, the following is needed:**
- Official product label (warnings, contraindications) from the manufacturer or a comparable regulatory authority (TFDA/FDA/EMA) — currently a **blocking** gap (DG001) for safety sign-off
- Formal DrugBank/MOA documentation to close the mechanism-of-action data gap (DG002)
- Clarification of regulatory pathway/intent, since the drug has zero current India registrations — this is fundamentally a market-entry question for an established oncology agent, not an exploratory repurposing hypothesis
- A full concurrent-medication DDI screen given the large interaction count (378 total, only 20 sampled here)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

