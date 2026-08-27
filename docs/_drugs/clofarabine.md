---
layout: default
title: Clofarabine
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
---

# Clofarabine
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

# Clofarabine: From Acute Lymphoblastic Leukemia to Myeloid Leukemia

## One-Sentence Summary

Clofarabine is a purine nucleoside antimetabolite historically established for relapsed/refractory acute lymphoblastic leukemia (ALL) in pediatric patients. The TxGNN model predicts it may also be effective for **Myeloid Leukemia (Acute Myeloid Leukemia, AML)**, a closely related hematologic malignancy, with **50 clinical trials** and **20 publications** currently supporting this direction — including two completed Phase 3 RCTs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsed/refractory acute lymphoblastic leukemia (ALL) in pediatric patients (established via international regulatory approval; no India licensing record exists since the product is not marketed there) |
| Predicted New Indication | Myeloid Leukemia (Acute Myeloid Leukemia, AML) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data (DrugBank MOA field) is currently a data gap. However, the evidence pack's own repurposing rationale describes Clofarabine as a purine nucleoside analog that inhibits ribonucleotide reductase and DNA polymerase, thereby depleting intracellular deoxynucleoside triphosphates required for DNA replication and repair. This mechanism produces direct cytotoxicity against highly proliferative hematopoietic blasts, and is consistent with mechanistic descriptions repeated across the clinical trial literature (e.g., PMID 15230627, PMID 16117562-style summaries embedded in trial texts).

Acute lymphoblastic leukemia (the drug's established indication) and myeloid leukemia (the predicted new indication) are both acute leukemias arising from malignant clonal proliferation of hematopoietic precursor cells in the bone marrow. Notably, the evidence pack itself flags (in the rationale for the separately-ranked "acute lymphoblastic leukemia" candidate) that ALL is Clofarabine's actual known core indication — its absence from the structured `original_indications` field reflects incomplete database curation rather than a true clinical gap. This context strengthens the plausibility of the AML prediction: it is not a leap across unrelated biology, but an extension within the same lineage of acute leukemias.

Mechanistically, Clofarabine's antimetabolite activity is not lineage-restricted — it targets rapidly dividing blasts regardless of myeloid or lymphoid origin — and it has already been extensively combined with AML-standard agents such as cytarabine, idarubicin, and fludarabine in numerous trials over two decades, including large randomized studies. This body of real-world combination use, rather than a purely theoretical model output, is what elevates this candidate to the highest evidence tier (L1) among the ten indications evaluated for this drug.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01471444](https://clinicaltrials.gov/study/NCT01471444) | Phase 3 | Completed | 256 | RCT comparing fludarabine-clofarabine vs. fludarabine alone (both with IV busulfan) prior to allogeneic HSCT for AML/MDS — highest-grade direct evidence |
| [NCT01289457](https://clinicaltrials.gov/study/NCT01289457) | Phase 1/2 | Completed | 282 | Randomized comparison of clofarabine+idarubicin+cytarabine (CIA) vs. fludarabine+idarubicin+cytarabine (FLAI) in AML and high-risk MDS |
| [NCT01794702](https://clinicaltrials.gov/study/NCT01794702) | Phase 1/2 | Completed | 65 | Decitabine followed by clofarabine+idarubicin+cytarabine (CIA) in acute leukemia; established dose and assessed disease control |
| [NCT00932412](https://clinicaltrials.gov/study/NCT00932412) | Phase 2 | Completed | 735 | Large randomized multicenter study: clofarabine/intermediate-dose cytarabine (CLARA) vs. high-dose cytarabine consolidation in newly-diagnosed AML |
| [NCT00703820](https://clinicaltrials.gov/study/NCT00703820) | Phase 3 | Completed | 324 | AML08 trial: clofarabine+cytarabine vs. conventional induction therapy in newly diagnosed pediatric AML |
| [NCT00088218](https://clinicaltrials.gov/study/NCT00088218) | Phase 2 | Completed | 95 | Randomized study of clofarabine alone vs. clofarabine+low-dose cytarabine in untreated patients ≥60 years with AML/high-risk MDS |
| [NCT01295307](https://clinicaltrials.gov/study/NCT01295307) | Phase 2 | Completed | 86 | Clofarabine salvage therapy in relapsed/refractory AML, assessed as bridge to allogeneic HSCT |
| [NCT01457885](https://clinicaltrials.gov/study/NCT01457885) | Phase 2 | Completed | 75 | Myeloablative allogeneic HSCT using clofarabine+busulfan (CloBu4) regimen for non-remission AML |
| [NCT00067028](https://clinicaltrials.gov/study/NCT00067028) | Phase 2 | Completed | 116 | Randomized Phase I/II comparison of clofarabine+cytarabine vs. clofarabine+idarubicin vs. triple combination in relapsed/refractory AML, high-grade MDS, and CML blast phase |
| [NCT00081822](https://clinicaltrials.gov/study/NCT00081822) | Phase 1 | Completed | 23 | Dose-finding study of clofarabine+cytarabine in older adults (≥60y) with newly diagnosed AML |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31246522](https://pubmed.ncbi.nlm.nih.gov/31246522/) | 2019 | RCT (Phase III) | J Clin Oncol | AML08 multicenter randomized Phase III trial: clofarabine can replace anthracyclines/etoposide in remission induction for childhood AML, reducing cumulative drug toxicity exposure |
| [31281098](https://pubmed.ncbi.nlm.nih.gov/31281098/) | 2019 | Review | Lancet Oncology | Editorial summary on clofarabine and cytarabine combination for AML |
| [25457773](https://pubmed.ncbi.nlm.nih.gov/25457773/) | 2015 | Review | Crit Rev Oncol Hematol | Comprehensive review of clofarabine's role in adult AML, monotherapy and combination strategies |
| [36336258](https://pubmed.ncbi.nlm.nih.gov/36336258/) | 2023 | Cohort | Transplant Cell Ther | Clofarabine+busulfan myeloablative conditioning shows antileukemic activity with acceptable toxicity in active/refractory myeloid malignancies undergoing allo-HCT |
| [32187883](https://pubmed.ncbi.nlm.nih.gov/32187883/) | 2020 | Cohort | Cancer Medicine | Clofarabine+cytarabine+mitoxantrone (CLAM) achieved high response rates as effective bridge to allogeneic HSCT in relapsed/refractory AML |
| [29773602](https://pubmed.ncbi.nlm.nih.gov/29773602/) | 2018 | Phase IB Trial | Haematologica | Clofarabine, high-dose cytarabine, and liposomal daunorubicin in pediatric relapsed/refractory AML; identified recommended Phase II dose |
| [31637757](https://pubmed.ncbi.nlm.nih.gov/31637757/) | 2020 | Phase I/II Trial | Am J Hematol | Optimally-dosed clofarabine with low-dose TBI as non-myeloablative conditioning for HSCT in AML patients unfit for intensive regimens |
| [22957815](https://pubmed.ncbi.nlm.nih.gov/22957815/) | 2013 | Review | Leukemia & Lymphoma | Review of clofarabine's mechanism (ribonucleotide reductase/DNA polymerase inhibition) and role in AML |
| [18756533](https://pubmed.ncbi.nlm.nih.gov/18756533/) | 2008 | Cohort | Cancer | Clofarabine combinations (with idarubicin) as feasible and effective AML salvage therapy |
| [15230627](https://pubmed.ncbi.nlm.nih.gov/15230627/) | 2004 | Drug Profile/Review | Drugs in R&D | Foundational pharmacological profile describing clofarabine's dual inhibition of DNA polymerase and ribonucleotide reductase |

---

## India Market Information

Clofarabine is currently **not marketed in India** — there are no registration/license records in the available regulatory dataset (total registrations: 0). No dosage form, brand name, or approved indication text is available for the India market at this time.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — purine nucleoside antimetabolite (inhibits ribonucleotide reductase and DNA polymerase) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions — quantified toxicity data is not available in this evidence pack; numerous trials used dose-escalation/MTD designs and combined it with other myelosuppressive agents (cytarabine, idarubicin), indicating significant hematologic toxicity requiring close monitoring |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver function tests, renal function tests (standard monitoring for cytotoxic antimetabolite regimens per trial protocols) |
| Handling Protection | Must follow cytotoxic/hazardous drug handling regulations applicable to antineoplastic agents |

---

## Safety Considerations

**Drug Interactions**: A DDI query returned 466 total interactions, predominantly classified as Moderate severity (source: DDInter). Representative interacting agents include:
- Antifungals/antibiotics: Amphotericin B (all formulations), Clarithromycin, Clotrimazole, Kanamycin, Levofloxacin, Minocycline, Neomycin
- Antidiabetics: Acarbose, Pioglitazone
- Aminosalicylates: Mesalazine, Balsalazide, Olsalazine
- Other: Bupropion, Chenodeoxycholic acid, Naltrexone, Nicotinamide, Nitisinone

Key warnings and contraindications are not currently available in the source data — please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The myeloid leukemia (AML) prediction reaches the highest evidence tier (L1), supported by two completed Phase 3 RCTs (NCT01471444, n=256; NCT00703820, n=324) plus dozens of Phase 1/2 combination studies spanning two decades, and a coherent mechanistic link to the drug's established use in the closely related ALL indication. However, Clofarabine is not currently registered or marketed in India, and critical drug-level safety data (TFDA/label warnings, contraindications, confirmed MOA) remain outstanding blocking/high-severity data gaps.

**To proceed, the following is needed:**
- TFDA/India-approved package insert data — warnings, precautions, and contraindications (currently a Blocking data gap)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent primary source (currently a High-severity data gap)
- A regulatory pathway assessment for India market entry, since the product currently has zero registrations
- A formal myelosuppression/hematologic monitoring and cytotoxic-handling protocol tailored to local clinical practice
- Consideration of the other TxGNN-predicted indications in this candidate set (e.g., precursor lymphoblastic lymphoma/leukemia, L2) as secondary, lower-priority repurposing targets, while several low-evidence predictions (ganglioneuroblastoma, neuroblastoma, retroperitoneal neoplasm, and the CLL/SLL molecular subtypes) should remain on **Hold** pending any clinical or literature signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

