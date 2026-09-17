---
layout: default
title: Hydroxyurea
parent: High Evidence (L1-L2)
nav_order: 411
evidence_level: L2
indication_count: 10
---

# Hydroxyurea
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Hydroxyurea: From Sickle Cell Anemia (HbSS) to Sickle Cell-Hemoglobin C Disease Syndrome

## One-Sentence Summary

Hydroxyurea is an S-phase-specific ribonucleotide reductase inhibitor whose efficacy in classic sickle cell anemia (HbSS) — via induction of fetal hemoglobin (HbF) — is already well documented in the literature. The TxGNN model predicts it may also be effective for **Sickle Cell-Hemoglobin C Disease Syndrome**, a related hemoglobinopathy genotype, and this direction is currently supported by **8 clinical trials** and **19 publications**, including two Cochrane systematic reviews and a 2025 NEJM Evidence trial report.

Note: this evidence pack covers 10 predicted indications for hydroxyurea (5 sickle-cell hemoglobinopathy variants and 5 unrelated oncology indications). This report focuses on the strongest-evidence candidate, Sickle Cell-Hemoglobin C Disease; the others are summarized in a table at the end of this section for context.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this evidence pack (`original_indications` field is empty); literature within the pack confirms hydroxyurea's proven use in classic sickle cell anemia (HbSS) |
| Predicted New Indication | Sickle Cell-Hemoglobin C Disease Syndrome |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L2 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank-sourced mechanism-of-action text is currently a data gap for this pack. However, the collected literature itself documents the mechanism: hydroxyurea is an S-phase-specific ribonucleotide reductase inhibitor that induces fetal hemoglobin (HbF) synthesis. Elevated HbF interferes with the polymerization of sickle hemoglobin (HbS), which is the pathological driver of vaso-occlusive crises across all sickle hemoglobinopathy genotypes, not just classic HbSS.

Sickle Cell-Hemoglobin C Disease (HbSC) is a compound heterozygous genotype (one HbS allele, one HbC allele) that shares the same HbS-polymerization pathophysiology as HbSS, just with a milder average phenotype. Because hydroxyurea's HbF-inducing mechanism does not depend on which second allele is present, mechanistic extrapolation from HbSS to HbSC is biologically plausible — a point echoed explicitly in the evidence pack's own rationale notes ("同HbF誘導機轉，惟直接針對...族群數據有限，多數證據來自一般鐮狀血球病族群之外推").

This is also historically supported: as literature entry PMID 26615793 notes, hydroxyurea's clinical and laboratory efficacy was proven in adult HbSS patients decades ago, and clinical use has since been cautiously extended to HbSC patients, motivated by their still-significant burden of vaso-occlusive pain, acute chest syndrome, and avascular necrosis despite a historically "milder disease" label.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00532883](https://clinicaltrials.gov/study/NCT00532883) | Phase 2 | Terminated | 44 | Hydroxyurea vs. magnesium pidolate, alone and combined, for reducing RBC density and pain episodes in HbSC disease |
| [NCT02640573](https://clinicaltrials.gov/study/NCT02640573) | Phase 2 | Terminated | 1 | Treatment of adult patients with HbSC disease using hydroxyurea |
| [NCT02336373](https://clinicaltrials.gov/study/NCT02336373) | Phase 2 | Terminated | 32 | Hydroxyurea treatment effects in youth with HbSC disease |
| [NCT03474965](https://clinicaltrials.gov/study/NCT03474965) | Phase 2 | Completed | 117 | Crizanlizumab with/without hydroxyurea/hydroxycarbamide in pediatric sickle cell VOC, incl. SC genotype |
| [NCT03264989](https://clinicaltrials.gov/study/NCT03264989) | Phase 2 | Completed | 57 | Crizanlizumab with/without hydroxyurea in adult sickle cell VOC |
| [NCT03128515](https://clinicaltrials.gov/study/NCT03128515) | Phase 3 | Completed | 187 | NOHARM: first placebo-controlled RCT of hydroxyurea dosing/safety in a malaria-endemic sickle cell population |
| [NCT03763656](https://clinicaltrials.gov/study/NCT03763656) | Phase 1/2 | Completed | 33 | Pharmacokinetic study of oral hydroxyurea solution in children with sickle cell anemia |
| [NCT01987908](https://clinicaltrials.gov/study/NCT01987908) | Phase 2 | Terminated | 35 | Comparator trial noting hydroxyurea as the only approved SCD drug, evaluated against Aes-103 |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39647172](https://pubmed.ncbi.nlm.nih.gov/39647172/) | 2025 | RCT | NEJM Evidence | Trial examining safety and efficacy of hydroxyurea treatment specifically in patients with HbSC disease, a genotype with no established disease-modifying therapy |
| [36047926](https://pubmed.ncbi.nlm.nih.gov/36047926/) | 2022 | Systematic Review | Cochrane Database of Systematic Reviews | Updated Cochrane review of hydroxyurea (hydroxycarbamide) for sickle cell disease |
| [28426137](https://pubmed.ncbi.nlm.nih.gov/28426137/) | 2017 | Systematic Review | Cochrane Database of Systematic Reviews | Earlier Cochrane review update on hydroxyurea for sickle cell disease |
| [26615793](https://pubmed.ncbi.nlm.nih.gov/26615793/) | 2016 | Clinical Study | American Journal of Hematology | Evaluates hydroxyurea safety/utility in HbSC patients, 20 years after efficacy was proven in adult HbSS |
| [22949140](https://pubmed.ncbi.nlm.nih.gov/22949140/) | 2013 | Clinical Study | Pediatric Blood & Cancer | Long-term hydroxyurea response in 15 children with severe HbSC: increased MCV/HbF, fewer chest syndrome/hospitalization episodes; thrombocytopenia was the main side effect |
| [11464988](https://pubmed.ncbi.nlm.nih.gov/11464988/) | 2001 | Clinical Study | Journal of Pediatric Hematology/Oncology | Pilot evaluation of hydroxyurea laboratory/clinical response in pediatric HbSC patients |
| [36799926](https://pubmed.ncbi.nlm.nih.gov/36799926/) | 2023 | Review | Blood Advances | Notes most adults with severe HbSC disease are not treated with hydroxyurea despite disease burden, highlighting an access/practice gap |
| [11406036](https://pubmed.ncbi.nlm.nih.gov/11406036/) | 2001 | Systematic Review | Cochrane Database of Systematic Reviews | Original Cochrane review establishing hydroxyurea's HbF-raising rationale for sickle cell disease |
| [37439373](https://pubmed.ncbi.nlm.nih.gov/37439373/) | 2023 | Clinical Study | Haematologica | Plasma metabolomics in sickle cell patients (incl. HbSC) as a function of hydroxyurea treatment |
| [39229085](https://pubmed.ncbi.nlm.nih.gov/39229085/) | 2024 | Preprint | bioRxiv | CureSCi metadata catalog harmonizing studies for secondary analysis of hydroxyurea use in sickle cell disease |

---

### Other Predicted Indications in This Pack (Summary)

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|-----------------|------------------|
| 2 | Hereditary Persistence of Fetal Hemoglobin–Sickle Cell Disease | 99.67% | L4 | Research Question |
| 3 | Sickle Cell-Hemoglobin E Disease Syndrome | 99.67% | L2 | Proceed with Guardrails |
| 4 | Sickle Cell-Hemoglobin D Disease Syndrome | 99.67% | L2 | Proceed with Guardrails |
| 6 | Sickle Cell-Beta-Thalassemia Disease Syndrome | 99.67% | L4 | Research Question |
| 1 | Female Breast Carcinoma | 99.97% | L5 | Hold — no supporting trials or literature |
| 7 | Cervical Adenosarcoma | 99.40% | L5 | Hold — no supporting trials or literature |
| 8 | Colon Mucinous Adenocarcinoma | 99.32% | L5 | Hold — no supporting trials or literature |
| 9 | Rectum Mucinous Adenocarcinoma | 99.31% | L5 | Hold — no supporting trials or literature |
| 10 | Gallbladder Mucinous Adenocarcinoma | 99.28% | L5 | Hold — no supporting trials or literature |

The oncology-related predictions (breast, cervical, colon, rectum, gallbladder) rest purely on hydroxyurea's general antiproliferative mechanism, with zero clinical trial or literature hits returned in this pack's queries — these remain model-score-only (L5) and are not actionable without further evidence generation.

---

## India Market Information

Currently no market authorizations are recorded (`total_licenses = 0`, market status: Not Marketed).

---

## Cytotoxicity

Hydroxyurea is classified as a conventional cytotoxic agent (S-phase-specific ribonucleotide reductase inhibitor), as reflected in its established antineoplastic use and in the mechanistic rationale throughout this evidence pack.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (ribonucleotide reductase inhibitor, S-phase specific) |
| Myelosuppression Risk | High — literature in this pack (PMID 22949140) identifies thrombocytopenia as the most significant treatment-limiting side effect in HbSC patients on hydroxyurea; neutropenia is also a recognized dose-limiting toxicity in the broader sickle cell/oncology literature |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (frequent during dose titration, then periodic maintenance monitoring), renal function, hepatic function |
| Handling Protection | Should be handled per institutional cytotoxic/hazardous drug handling protocols despite oral administration |

---

## Safety Considerations

Key warnings and contraindications are not currently available in this evidence pack (flagged as a **Blocking** data gap — TFDA label warnings/contraindications must be obtained before this candidate can pass initial safety screening, per DG001).

**Drug Interactions**: A DDI query returned 309 total interacting drugs. Among the sampled entries, most are recorded with an "Unknown" severity level pending further classification; one has a graded severity:
- Levofloxacin — Minor

Other frequently co-prescribed drugs flagged in the DDI dataset (severity not yet classified) include doxycycline, amphotericin B, hydrocortisone, famotidine, acetylsalicylic acid, pantoprazole, acarbose, morphine, metformin, omeprazole, rosiglitazone, lansoprazole, vancomycin, lactulose, triamcinolone, prednisone, simvastatin, nystatin, and potassium chloride. Given the high total interaction count (309) and the predominance of unclassified severities, a full DDI severity review is recommended before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Sickle Cell-Hemoglobin C Disease Syndrome)

**Rationale:**
Multiple completed and ongoing trials plus two Cochrane systematic reviews and a 2025 NEJM Evidence trial support hydroxyurea's mechanistic and clinical rationale in HbSC disease, extrapolated from decades of proven efficacy in classic HbSS. However, the Blocking-severity absence of TFDA label warnings/contraindications (DG001) means this candidate cannot yet pass initial safety screening (S1), and the drug is currently unmarketed in this jurisdiction (0 registrations).

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA (or equivalent local regulator) product label warnings/contraindications
- Resolve DG002: obtain detailed MOA data from DrugBank to formalize the mechanistic-link analysis
- Full DDI severity classification (309 entries, mostly "Unknown" severity)
- Regulatory pathway assessment given current "Not Marketed" status
- If pursuing sickle-cell genotype variants beyond HbSC (HbSE, HbSD — also L2), consolidate into a single genotype-class label-expansion strategy rather than separate submissions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

