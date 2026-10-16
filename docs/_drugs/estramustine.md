---
layout: default
title: Estramustine
parent: Model Prediction Only (L5)
nav_order: 324
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Estramustine: predicted new indication Prostate cancer/brain cancer susceptibility (evidence level L5). Approved use: Prostate cancer"
---

# Estramustine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Estramustine: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Estramustine is an oral cytotoxic drug, originally used to treat prostate cancer.
The TxGNN model's top-ranked prediction is **prostate cancer/brain cancer susceptibility**, but this prediction has **no clinical trials and no publications** behind it. The best-supported direction in the data is **female breast carcinoma** (1 Phase 2 trial and 17 publications), and a "male reproductive organ cancer" category is dominated by prostate cancer, which is the drug's existing indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (the India licence records contain no indication text) |
| Predicted New Indication | Prostate cancer/brain cancer susceptibility (top-ranked prediction) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 for the top-ranked prediction (model prediction only) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

**Note on the top-ranked prediction:** It is a genetic susceptibility entity that overlaps with prostate cancer mainly by name. The high score probably reflects graph proximity to prostate cancer. The sections below therefore also cover the other candidates that have real evidence (breast carcinoma and the male reproductive organ cancer category).

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From the literature, estramustine is an estradiol conjugated to a nitrogen mustard carbamate. It binds tubulin and microtubule-associated proteins, depolymerises microtubules, and disrupts the nuclear matrix. It is concentrated in prostatic tissue through estramustine-binding protein (EMBP).

For the top-ranked prediction, no mechanistic link to a susceptibility phenotype has been shown. The score most likely reflects graph proximity to prostate cancer rather than a real therapeutic signal. The same is true of the other benign or rare prostate and ovarian entities (fibroma of prostate, prostate leiomyoma, benign prostate phyllodes tumor, Brenner tumor, breast fibrocystic disease). HIV infection also has no plausible mechanism.

The most credible new direction is **female breast carcinoma**. EMBP expression has been described in human breast cancer, and estramustine potentiates taxanes in refractory breast cancer. A Phase 1 study with paclitaxel and a single-agent report after anthracycline and taxane failure suggest activity. Taxanes alone are standard in breast cancer, so the added value of estramustine is unproven.

## Clinical Trial Evidence

**Top-ranked prediction (prostate cancer/brain cancer susceptibility):** Currently no related clinical trials registered.

**Female breast carcinoma (rank 8):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003066](https://clinicaltrials.gov/study/NCT00003066) | Phase 2 | Unknown | 40 | Docetaxel plus estramustine phosphate in metastatic breast cancer; small single-arm study |

**Male reproductive organ cancer (rank 6)**, a category dominated by prostate cancer, the existing indication (selected trials):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00004001](https://clinicaltrials.gov/study/NCT00004001) | Phase 3 | Completed | 770 | Docetaxel + estramustine vs mitoxantrone + prednisone in hormone-refractory prostate cancer |
| [NCT00055731](https://clinicaltrials.gov/study/NCT00055731) | Phase 3 | Completed | 413 | Adjuvant hormonal therapy with or without docetaxel and estramustine in advanced or high-risk prostate cancer |
| [NCT00004054](https://clinicaltrials.gov/study/NCT00004054) | Phase 3 | Completed | 397 | Androgen suppression and radiotherapy with or without paclitaxel/estramustine/etoposide in high-risk localised prostate cancer |
| [NCT00002855](https://clinicaltrials.gov/study/NCT00002855) | Phase 3 | Completed | 306 | Androgen ablation alone vs chemo/hormonal therapy as initial treatment; compares regimens, not estramustine alone |
| [NCT00024167](https://clinicaltrials.gov/study/NCT00024167) | Phase 3 | Terminated | 265 | Consolidation therapy with or without strontium-89; estramustine's contribution cannot be isolated |
| [NCT00541281](https://clinicaltrials.gov/study/NCT00541281) | Phase 2 | Completed | 150 | Weekly docetaxel/estramustine/prednisone vs docetaxel/prednisone, PSA response endpoint |
| [NCT00193193](https://clinicaltrials.gov/study/NCT00193193) | Phase 2 | Completed | 100 | Weekly paclitaxel, low-dose estramustine and carboplatin, weekly vs every 4 weeks |
| [NCT00003084](https://clinicaltrials.gov/study/NCT00003084) | Phase 2 | Completed | 75 | Randomised comparison of two estramustine-containing regimens in androgen-independent prostate cancer |
| [NCT00016107](https://clinicaltrials.gov/study/NCT00016107) | Phase 2 | Completed | 72 | Estramustine, docetaxel and bevacizumab, single-arm |
| [NCT00002775](https://clinicaltrials.gov/study/NCT00002775) | Phase 1/2 | Unknown | 37 | Docetaxel plus estramustine in metastatic prostate cancer |

These trials support the existing prostate cancer label, not a new indication.

## Literature Evidence

**Female breast carcinoma (rank 8):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11697838](https://pubmed.ncbi.nlm.nih.gov/11697838/) | 2001 | Phase 2 trial | Ann Oncol | Single-agent estramustine phosphate is active in advanced breast cancer after anthracycline and taxane failure |
| [12377650](https://pubmed.ncbi.nlm.nih.gov/12377650/) | 2002 | Phase 2 | Ann Oncol | Weekly docetaxel plus estramustine in metastatic breast cancer |
| [9071337](https://pubmed.ncbi.nlm.nih.gov/9071337/) | 1997 | Phase 1 trial | Semin Oncol | Estramustine phosphate plus paclitaxel in advanced breast cancer |
| [11396364](https://pubmed.ncbi.nlm.nih.gov/11396364/) | 2001 | Review | Oncology (Williston Park) | Estramustine potentiates taxanes in prostate and refractory breast cancers |
| [15811618](https://pubmed.ncbi.nlm.nih.gov/15811618/) | 2005 | Systematic review | Lancet Oncol | Docetaxel in solid tumours, including breast cancer |
| [24722887](https://pubmed.ncbi.nlm.nih.gov/24722887/) | 2015 | Retrospective case series | Int J Clin Oncol | Estramustine phosphate in heavily pretreated metastatic breast cancer |
| [9738564](https://pubmed.ncbi.nlm.nih.gov/9738564/) | 1998 | Phase 1 | J Clin Oncol | Estramustine phosphate with short paclitaxel infusions in women with solid tumours |
| [1888147](https://pubmed.ncbi.nlm.nih.gov/1888147/) | 1991 | Basic research | Anticancer Res | EMBP detected in 6 of 17 breast cancers |

**Benign reproductive system neoplasm (rank 4):** 8 publications, all biomarker, binding-protein or uptake studies in prostate cancer and benign prostatic hyperplasia (for example [8821700](https://pubmed.ncbi.nlm.nih.gov/8821700/), 1996, Eur Urol). None tests therapeutic efficacy in a benign neoplasm.

**Top-ranked prediction:** Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 77750 | Estramin 140mg Capsule (Samarth Life Sciences Pvt Ltd) | Strip of 10 capsules | Not recorded in the compiled data |
| 77563 | Estram 140mg Capsule (United Biotech Pvt Ltd) | Strip of 10 capsules | Not recorded in the compiled data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimicrotubule agent; estradiol–nitrogen mustard carbamate conjugate) |
| Myelosuppression Risk | Low (one breast cancer study cites lack of haematological toxicity), but monitoring is still advised, especially in combination with taxanes |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC, liver and renal function, blood pressure, fluid status, calcium, glucose, and signs of thromboembolism |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindication-related conditions (knowledge-graph associations, not label text):** hypertension, epilepsy, kidney disease, liver disease, gallbladder disease, congestive heart failure, diabetes mellitus and diabetic ketoacidosis, hypercalcaemia, thrombophlebitis, migraine, coronary artery disease and myocardial infarction, cerebrovascular disorder, hyperbilirubinaemia and Gilbert syndrome, haemoglobinopathy, and gynaecomastia/breast hypertrophy. Erectile dysfunction, premature ejaculation and psychologic dyspareunia are also listed.
- **Drug Interactions:** 111 interactions were identified, all of the 20 listed in the data being Moderate. They include:
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
  - Antidiabetic agents: acarbose, metformin, canagliflozin, dapagliflozin, empagliflozin, alogliptin, linagliptin, chlorpropamide, albiglutide, dulaglutide
  - Amphotericin B (including lipid complex)
  - Calcium products: calcium acetate, calcium phosphate, topical calcitriol
- The large interaction burden is a particular concern in patients on antiretrovirals or multiple medications.
- Breast cancer use also requires weighing thromboembolic and cardiovascular toxicity.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (prostate cancer/brain cancer susceptibility) has a very high score but no trials, no literature and no plausible mechanism, so it is likely a graph artefact. The only direction with real evidence is female breast carcinoma, which has a single small Phase 2 trial (status unknown) and no Phase 3 data. It is best treated as a research question, not an actionable repurposing candidate. The substantial prostate cancer evidence supports the existing label, not a new use.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India licences (currently missing, and a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- For breast carcinoma: prospective randomised data showing the added value of estramustine over taxane alone, and a thromboembolic and cardiovascular risk assessment
- Confirmation of the approved indication text on the India licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

