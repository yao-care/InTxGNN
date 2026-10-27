---
layout: default
title: Methotrexate
parent: Model Prediction Only (L5)
nav_order: 535
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Methotrexate: predicted new indication Pulmonary blastoma (evidence level L5). Approved use: Acute lymphoblastic leukemia, non-Hodgkin lymphoma…"
monitor_inn: "Methotrexate"
predicted_indications: ["pulmonary blastoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "Hodgkins lymphoma", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
---

# Methotrexate
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

## Methotrexate: From Acute Lymphoblastic Leukemia, Rheumatoid Arthritis and Psoriasis to Pulmonary Blastoma
{: .text-alpha }

## One-Sentence Summary

Methotrexate is an antifolate drug originally used for acute lymphoblastic leukemia, lymphomas (including non-Hodgkin lymphoma and mycosis fungoides), rheumatoid arthritis and psoriasis.
The TxGNN model's top-ranked prediction is **pulmonary blastoma**, but no clinical trials or publications were found for it, so this prediction rests on the model score alone.
Among the other top-10 predictions, **Hodgkin lymphoma** (44 trials, 20 publications, mostly indirect) and **rhabdomyosarcoma** (4 trials, 18 publications, including one Phase 2 trial of high-dose methotrexate) have more supporting data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic leukemia, non-Hodgkin lymphoma, rheumatoid arthritis, psoriasis, mycosis fungoides (from the knowledge graph; no approved-indication text is available for the Indian licenses) |
| Predicted New Indication | Pulmonary blastoma |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

Other predictions in the top 10 (for context):

| Rank | Predicted Indication | Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 2 | Primary pulmonary lymphoma | 99.45% | L4 | Hold |
| 3 | Small cell lung carcinoma | 99.43% | L4 | Hold |
| 4 | Well-differentiated fetal adenocarcinoma of the lung | 99.42% | L5 | Hold |
| 5 | Hodgkin lymphoma | 99.32% | L3 | Research question |
| 6 | Rhabdomyosarcoma | 99.25% | L2 | Research question |
| 7 | CLL/SLL with mutated IGHV | 99.23% | L5 | Hold |
| 8 | Pregerminal center CLL/SLL | 99.23% | L5 | Hold |
| 9 | Parameningeal embryonal rhabdomyosarcoma | 99.21% | L5 | Hold |
| 10 | Botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.21% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, methotrexate is an antifolate that inhibits dihydrofolate reductase (DHFR), which limits DNA synthesis in rapidly dividing cells. Its efficacy in leukemia and lymphoma is established, and mechanistically it could be applicable to other fast-proliferating tumours.

For **pulmonary blastoma** (rank 1), the data compiled for this report contain no trials, literature or mechanistic evidence. The high score likely reflects proximity to other thoracic and malignant diseases in the knowledge graph. No specific link between methotrexate and this rare lung tumour is supported here, so the prediction should be treated as a hypothesis only.

For the better-supported predictions:

- **Primary pulmonary lymphoma:** Non-Hodgkin lymphoma is already an original indication, and high-dose methotrexate is used in extranodal large B-cell lymphoma and primary CNS lymphoma. The supplied literature is mostly case reports and general reviews, with no pulmonary-specific methotrexate evidence evident from the titles.
- **Hodgkin lymphoma:** The VBM regimen (vinblastine, bleomycin, methotrexate) plus radiotherapy has been studied in early-stage disease, with reported complete remission rates of 94–100%. Pulmonary toxicity was considerable in early trials. Most listed trials are mixed lymphoma or transplant studies in which methotrexate is a component or a GVHD agent.
- **Rhabdomyosarcoma:** A Phase 2 trial of high-dose methotrexate in untreated high-risk children (PMID 9329466) supports activity, but methotrexate is not a standard backbone agent in this disease.
- **Small cell lung carcinoma:** Historical regimens (1981–1992) used methotrexate in combination, but the listed trials concern non-small cell lung cancer, not SCLC.

---

## Clinical Trial Evidence

Pulmonary blastoma (rank 1): Currently no related clinical trials registered.

For the most evidence-supported predictions, representative trials are shown below.

**Hodgkin lymphoma (rank 5)**: 44 trials were retrieved; selected examples:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03206671](https://clinicaltrials.gov/study/NCT03206671) | Phase 3 | Active, not recruiting | 650 | NHL-BFM B-NHL 2013 protocol: role of rituximab in mature aggressive B-cell lymphoma in children (non-Hodgkin, not Hodgkin) |
| [NCT00002471](https://clinicaltrials.gov/study/NCT00002471) | Phase 2 | Completed | N/A | Intensive short-course combination chemotherapy in poor-risk non-lymphoblastic lymphoma and recurrent NHL |
| [NCT00290498](https://clinicaltrials.gov/study/NCT00290498) | Phase 2 | Completed | 67 | Rituximab-HCVAD alternating with rituximab-methotrexate-cytarabine vs R-CHOP in high-risk aggressive B-cell NHL |
| [NCT00005977](https://clinicaltrials.gov/study/NCT00005977) | Phase 3 | Completed | 83 | Dose intensification of methotrexate in advanced small non-cleaved cell NHL and B-cell ALL |
| [NCT00928018](https://clinicaltrials.gov/study/NCT00928018) | Phase 3 | Completed | 139 | Tacrolimus/sirolimus/methotrexate GVHD prophylaxis after transplant for lymphoma (methotrexate used for GVHD prevention, not antilymphoma activity) |
| [NCT00574496](https://clinicaltrials.gov/study/NCT00574496) | Phase 2 | Completed | 25 | Salvage chemotherapy then allogeneic transplant in high-risk or relapsed Hodgkin lymphoma |
| [NCT00045539](https://clinicaltrials.gov/study/NCT00045539) | Phase 2 | Completed | N/A | Methotrexate plus thiotepa in newly diagnosed primary CNS lymphoma |

None of these trials tests methotrexate specifically in Hodgkin lymphoma.

**Rhabdomyosarcoma (rank 6)**:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00357084](https://clinicaltrials.gov/study/NCT00357084) | Phase 2 | Completed | 53 | Methotrexate plus glucocorticoids for acute GVHD after transplant (not tumour treatment; rhabdomyosarcoma relevance unverified) |
| [NCT00112645](https://clinicaltrials.gov/study/NCT00112645) | Phase 1 | Completed | 10 | Allogeneic transplant toxicity in pediatric solid tumours; methotrexate likely used for GVHD prophylaxis |

**Small cell lung carcinoma (rank 3)**: The trials below concern NSCLC, not SCLC.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03520842](https://clinicaltrials.gov/study/NCT03520842) | Phase 2 | Completed | 22 | Regorafenib plus oral methotrexate in KRAS-mutated NSCLC |
| [NCT05663866](https://clinicaltrials.gov/study/NCT05663866) | Phase 2 | Active, not recruiting | 68 | Methotrexate, dexamethasone or montelukast to prevent amivantamab infusion reactions (supportive care) |

---

## Literature Evidence

Pulmonary blastoma (rank 1): Currently no related literature available.

Selected publications for the better-supported predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9329466](https://pubmed.ncbi.nlm.nih.gov/9329466/) | 1997 | Phase 2 trial | J Pediatr Hematol Oncol | High-dose methotrexate in untreated children and adolescents with high-risk unresectable or metastatic rhabdomyosarcoma |
| [14635074](https://pubmed.ncbi.nlm.nih.gov/14635074/) | 2003 | Clinical study | Cancer | VBM chemotherapy plus irradiation in early-stage favourable Hodgkin lymphoma (Italian lymphoma study group) |
| [21592816](https://pubmed.ncbi.nlm.nih.gov/21592816/) | 2012 | Review | Crit Rev Oncol Hematol | Nine small VBM trials: complete remission 94–100%, 5-year PFS 75–95%; pulmonary toxicity in early trials |
| [36614297](https://pubmed.ncbi.nlm.nih.gov/36614297/) | 2023 | Retrospective cohort | Int J Mol Sci | BOMP-EPI regimen (including methotrexate) in adult relapsed or metastatic rhabdomyosarcoma |
| [2991478](https://pubmed.ncbi.nlm.nih.gov/2991478/) | 1985 | Phase 3 | J Clin Oncol | MACC (methotrexate-containing) vs CCV/AV with radiotherapy in limited-stage small-cell lung carcinoma |
| [6284535](https://pubmed.ncbi.nlm.nih.gov/6284535/) | 1981 | Review | Eur J Respir Dis | Methotrexate among the commonly used agents in SCLC combination chemotherapy |
| [2983855](https://pubmed.ncbi.nlm.nih.gov/2983855/) | 1985 | Clinical study | Cancer | Adding methotrexate to VAC in 50 SCLC patients did not improve the incidence of complete response |
| [30842385](https://pubmed.ncbi.nlm.nih.gov/30842385/) | 2019 | Cohort | Rinsho Ketsueki | High-dose methotrexate plus rituximab in primary CNS lymphoma (6 patients) |
| [38720609](https://pubmed.ncbi.nlm.nih.gov/38720609/) | 2024 | Case report | Kyobu Geka | Primary pulmonary DLBCL arising from methotrexate-associated lymphoproliferative disorder |
| [32152484](https://pubmed.ncbi.nlm.nih.gov/32152484/) | 2020 | Review | Nat Rev Clin Oncol | Folate receptor α in oncology; general antifolate rationale |

Note that several papers describe methotrexate as a cause of lymphoproliferative disorders (including Hodgkin-like lesions), which is a safety signal rather than efficacy evidence.

---

## India Market Information

There are 20 valid licenses, all for single-ingredient products. Approved-indication text is not available in the data compiled for this report. Five main authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 134442 | Mexate 7.5 Tablet (Zydus Cadila) | Strip of 4 tablets | Not available |
| 84059 | Folitrax 15 Tablet (Ipca Laboratories) | Strip of 10 tablets | Not available |
| 185645 | RA Mex 15mg Tablet (Sun Pharmaceutical) | Strip of 10 tablets | Not available |
| 143291 | Methocel 500mg Injection (Celon Laboratories) | Vial of 5 ml injection | Not available |
| 139555 | Merex 1000mg Injection (Intas Pharmaceuticals) | Vial of 10 ml injection | Not available |

Both oral tablets (2.5–15 mg) and injectables (15 mg to 1000 mg vials) are marketed, which covers low-dose and high-dose use.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite, antifolate class) |
| Myelosuppression Risk | High at oncology doses; the knowledge graph lists contraindications including leukopenia, thrombocytopenia and anemia |
| Emetogenicity Classification | Low to moderate for oral low-dose use; moderate for high-dose intravenous use |
| Monitoring Items | CBC with differential, liver and renal function; methotrexate levels with high-dose regimens |
| Handling Protection | Must follow cytotoxic drug handling regulations. Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Contraindications (knowledge graph associations, not label text)**: liver failure, liver disease, kidney disease, gallbladder disease, thrombocytopenia, leukopenia, anemia (including macrocytic anemia), peptic and gastric ulcer, ulcerative colitis, inflammatory bowel disease, interstitial lung disease, pulmonary fibrosis (including postinflammatory), stomatitis, substance abuse/dependence, pyoureter, and immune system disease.
- **Drug Interactions**: 784 interactions are recorded. Examples classified as **Major**: rabeprazole, amoxicillin and acetylsalicylic acid. Many **Moderate** ones include doxycycline, tetracycline, clarithromycin, corticosteroids (hydrocortisone, dexamethasone, budesonide), amphotericin B, mesalazine, balsalazide and pioglitazone. Potassium citrate is Minor.
- **Other signals from the literature**: pulmonary toxicity (relevant to any lung indication) and methotrexate-associated lymphoproliferative disorders.

Please refer to the package insert for label warnings; they were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, pulmonary blastoma, has only a model score (L5) with no supporting trials or literature, and the knowledge graph flags interstitial lung disease and pulmonary fibrosis as contraindications, which is a concern for lung-targeted use. The more evidence-rich predictions (Hodgkin lymphoma, rhabdomyosarcoma) are better framed as research questions than as ready-to-advance candidates, because the trials found mostly involve methotrexate as a component or for GVHD prophylaxis rather than as a tested antitumour agent.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian product labels (a blocking gap for safety screening)
- Mechanism of action data from DrugBank to support mechanistic-link analysis
- For pulmonary blastoma: any preclinical or case-level evidence, since none was found
- For Hodgkin lymphoma and rhabdomyosarcoma: a focused review of methotrexate-specific studies (VBM regimens and the Phase 2 high-dose methotrexate trial), with relevance grading of the pending items
- Route and dose compatibility assessment (oral low-dose vs high-dose intravenous) for each candidate indication
- A pulmonary and hematological safety monitoring plan for any lung-related indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

