---
layout: default
title: Hydroxyurea
parent: Model Prediction Only (L5)
nav_order: 415
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Hydroxyurea: predicted new indication Female breast carcinoma (evidence level L5). Approved use: Melanoma, sickle cell anemia…"
monitor_inn: "Hydroxyurea"
predicted_indications: ["female breast carcinoma", "sickle cell-hemoglobin E disease syndrome", "sickle cell-hemoglobin d disease syndrome", "sickle cell-hemoglobin c disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "cervical adenosarcoma", "colon mucinous adenocarcinoma", "rectum mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma"]
---

# Hydroxyurea
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

## Hydroxyurea: From Melanoma and Sickle Cell Anemia to Breast Carcinoma
{: .text-alpha }

## One-Sentence Summary

Hydroxyurea is an oral ribonucleotide reductase inhibitor, originally used for melanoma, sickle cell anemia and ovarian cancer.
The TxGNN model's top-ranked prediction is **female breast carcinoma**, but it has **no registered clinical trials** and only preclinical or indirect publications behind it.
The best-supported repurposing direction in the data compiled for this report is **sickle cell-hemoglobin C disease (HbSC)**, with **1 Phase 2 trial** and **a 2025 NEJM Evidence publication**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Melanoma, sickle cell anemia, hereditary persistence of fetal hemoglobin, ovarian cancer (the registration records in India contain no approved indication text) |
| Predicted New Indication | Female breast carcinoma (rank 1); best-supported alternative: sickle cell-hemoglobin C disease |
| TxGNN Prediction Score | 99.97% (breast carcinoma); 99.67% (HbSC) |
| Evidence Level | L4 (breast carcinoma); L2 (HbSC) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold (breast carcinoma); Proceed with Guardrails (HbSC) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. Based on known information, hydroxyurea inhibits ribonucleotide reductase, which depletes deoxyribonucleotide pools and causes replication stress. It also raises fetal hemoglobin (HbF), which reduces sickle hemoglobin polymerization.

**Breast carcinoma.** Preclinical studies use hydroxyurea as a replication-stress tool in breast cancer cells. They cover RPA2-mediated DNA repair, ATR inhibition and BRCA-related replication fork biology. This supports biological plausibility only. No breast cancer trial of hydroxyurea is registered. Older Phase 1 combination studies from 1991–1992 (with 5-FU, leucovorin and cisplatin) were not breast-specific, and the 2024 lipid-conjugate paper is an in-silico design study.

**HbSC disease.** HbF induction is the established mechanism in sickle cell anemia, so extending it to HbSC is reasonable. It is less certain than in HbSS because HbC also contributes to red cell dehydration and viscosity. This indication has direct clinical data.

**Other sickle syndromes.** The other sickle-related predictions (HPFH-sickle, HbSE, HbSD, HbS/beta-thalassemia) rest on the same HbF logic but have little genotype-specific evidence. The remaining predictions (cervical adenosarcoma and mucinous adenocarcinomas of the colon, rectum and gallbladder) rest only on the model score.

---

## Clinical Trial Evidence

**Female breast carcinoma:** Currently no related clinical trials registered.

**Sickle cell-hemoglobin C disease (best-supported alternative):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00532883](https://clinicaltrials.gov/study/NCT00532883) | Phase 2 | Terminated | 44 | Hydroxyurea and magnesium pidolate, alone and combined, for reducing red cell density and pain episodes in HbSC; early termination limits conclusions |

**Sickle cell-beta-thalassemia (indirect only):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03653338](https://clinicaltrials.gov/study/NCT03653338) | Phase 1/2 | Recruiting | 5 | T-cell depleted alternative donor transplant in severe sickle cell disease; hydroxyurea is not the intervention tested |
| [NCT01962415](https://clinicaltrials.gov/study/NCT01962415) | Phase 2 | Recruiting | 100 | Reduced-intensity conditioning for transplant in non-malignant disorders; not a test of hydroxyurea efficacy |

---

## Literature Evidence

**Female breast carcinoma (preclinical or indirect):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | In-silico/Preclinical | Drug Research | Design of hydroxyurea-lipid conjugates targeting the PI3K/AKT/mTOR pathway; no clinical data |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | Preclinical | DNA Repair | Valproic acid sensitizes breast cancer cells to hydroxyurea by inhibiting RPA2-mediated DNA repair |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | Preclinical | DNA Repair | A valproic acid analogue as a potential breast carcinoma therapy, building on hydroxyurea sensitization |
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Phase 1 | Am J Clin Oncol | 5-FU, leucovorin and then hydroxyurea in advanced GI and breast cancer; not breast-specific |
| [1733549](https://pubmed.ncbi.nlm.nih.gov/1733549/) | 1992 | Phase 1/2 | Cancer Chemother Pharmacol | 5-FU, leucovorin, hydroxyurea and cisplatin with radiotherapy in solid tumors; not breast-specific |
| [30159181](https://pubmed.ncbi.nlm.nih.gov/30159181/) | 2018 | Case report | Case Rep Hematol | Coexisting breast cancer and essential thrombocythemia, with discussion of therapeutic challenges |

**Sickle cell-hemoglobin C disease:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39647172](https://pubmed.ncbi.nlm.nih.gov/39647172/) | 2025 | Clinical study | NEJM Evidence | Safety and efficacy of hydroxyurea in children and adults with HbSC; design and results should be confirmed against the full text |
| [36047926](https://pubmed.ncbi.nlm.nih.gov/36047926/) | 2022 | Systematic review | Cochrane Database Syst Rev | Hydroxyurea for sickle cell disease; mostly HbSS data, indirect for HbSC |
| [26615793](https://pubmed.ncbi.nlm.nih.gov/26615793/) | 2016 | Observational | Am J Hematol | Effects of hydroxyurea in patients with HbSC |
| [22949140](https://pubmed.ncbi.nlm.nih.gov/22949140/) | 2013 | Observational | Pediatr Blood Cancer | In 15 children with severe HbSC, hydroxyurea raised MCV and HbF and reduced acute chest syndrome and pain hospitalizations; thrombocytopenia was the main side effect |
| [36799926](https://pubmed.ncbi.nlm.nih.gov/36799926/) | 2023 | Observational | Blood Adv | Most adults with severe HbSC in Ghana are not treated with hydroxyurea |
| [42360692](https://pubmed.ncbi.nlm.nih.gov/42360692/) | 2026 | Real-world cohort | Br J Haematol | Retrospective pre-post study of hydroxyurea effectiveness and safety in adults with HbSC in Quebec |

---

## India Market Information

Twenty valid single-ingredient registrations are listed; five are shown below. The registration records contain no approved indication text. All are oral forms (capsule or tablet).

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 104805 | Hondrea 500mg Capsule (Alkem Laboratories) | Strip of 10 capsules | Not stated in registration record |
| 104101 | Hydab 500mg Capsule (Fresenius Kabi India) | Strip of 10 capsules | Not stated in registration record |
| 103709 | Hydrea 500mg Capsule (Sarabhai Chemicals) | Strip of 10 capsules | Not stated in registration record |
| 134720 | Mylostat 500mg Capsule (Zydus Cadila) | Strip of 10 capsules | Not stated in registration record |
| 105353 | Hdyshil 500mg Tablet (Shilpa Medicare) | Strip of 10 tablets | Not stated in registration record |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite, ribonucleotide reductase inhibitor) |
| Myelosuppression Risk | Significant. The knowledge graph lists leukopenia, thrombocytopenia and anemia as contraindicated conditions, and thrombocytopenia was the main side effect in HbSC children |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, plus renal function (the knowledge graph lists kidney disease as a contraindicated condition) |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindicated conditions (knowledge graph, not label text):** kidney disease, pyoureter, thrombocytopenia, anemia, macrocytic anemia, leukopenia, cutaneous vasculitis.
- **Drug Interactions:** 309 interactions were identified. Most are of unclassified severity. Examples include levofloxacin (minor), doxycycline, amphotericin B, hydrocortisone, acetylsalicylic acid, metformin, omeprazole, simvastatin and prednisone. The severity of most of these interactions has not been classified.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold for female breast carcinoma; Proceed with Guardrails for HbSC disease**

**Rationale:**
- Breast carcinoma has the highest TxGNN score (99.97%) but only preclinical, in-silico and non-specific Phase 1 support (L4), and no registered trials.
- HbSC has the strongest evidence (L2): a Phase 2 trial (terminated), observational studies and a 2025 NEJM Evidence study.
- The remaining sickle syndromes (HPFH-sickle, HbSE, HbSD, HbS/beta-thalassemia) are research questions at best.
- The cervical adenosarcoma and mucinous adenocarcinoma predictions (colon, rectum, gallbladder) rest on the model score alone and should be held.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian labels. This is a blocking gap for safety screening.
- Confirmation of the design and results of the 2025 HbSC publication (PMID 39647172) against the full text.
- A myelosuppression and blood-count monitoring plan, particularly because thrombocytopenia was reported in HbSC children.
- Mechanism-of-action data from DrugBank.
- For breast carcinoma, Phase 1/2 data or a defined preclinical-to-clinical plan before any further consideration.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

