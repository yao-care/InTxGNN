---
layout: default
title: Fluorouracil
parent: Model Prediction Only (L5)
nav_order: 366
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fluorouracil: predicted new indication Botryoid-type embryonal rhabdomyosarcoma of the vagina (evidence level L5). Approved use: Gastric cancer, metastatic colon cancer, pancreatic adenocarcinoma…"
monitor_inn: "Fluorouracil"
predicted_indications: ["botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "liver sarcoma", "sickle cell-hemoglobin c disease syndrome", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "sickle cell-hemoglobin E disease syndrome"]
---

# Fluorouracil
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

# Fluorouracil: From Gastric Cancer and Skin Conditions to Botryoid-Type Embryonal Rhabdomyosarcoma of the Vagina

## One-Sentence Summary

Fluorouracil is an antimetabolite chemotherapy drug, originally used for gastric cancer, colon cancer metastases, pancreatic adenocarcinoma, and skin conditions such as actinic keratosis and basal cell carcinoma.
The TxGNN model predicts it may be effective for **botryoid-type embryonal rhabdomyosarcoma of the vagina**, but **no clinical trials and no publications** currently support this specific prediction.
The evidence is model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric cancer, metastatic colon cancer, pancreatic adenocarcinoma, basal cell carcinoma, actinic keratosis and related skin diseases (the India licence records contain no approved-indication text) |
| Predicted New Indication | Botryoid-type embryonal rhabdomyosarcoma of the vagina |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, fluorouracil is a thymidylate synthase inhibitor and antimetabolite that disrupts DNA and RNA synthesis in rapidly dividing cells. Its efficacy in gastrointestinal and skin cancers is established, and a cytotoxic effect in a highly proliferative embryonal sarcoma is mechanistically plausible.

However, the TxGNN score is the only support for this prediction. Standard rhabdomyosarcoma regimens (such as VAC/VDC) do not rely on fluorouracil, so the link remains speculative.

**Other predicted indications (all rated Hold):**

| Rank | Predicted Indication | Score | Evidence Level | Notes |
|---|---|---|---|---|
| 2 | Rhabdomyosarcoma (disease) | 99.74% | L4 | Four papers, all old, mixed-topic or anecdotal; none isolates a fluorouracil-specific effect |
| 3 | Parameningeal embryonal rhabdomyosarcoma | 99.74% | L5 | Prediction only; drug delivery to the site is unaddressed |
| 4 | Embryonal extrahepatic bile duct rhabdomyosarcoma | 99.73% | L5 | Fluorouracil is used in biliary carcinoma, but this is a different tumour type |
| 5 | Prostate embryonal rhabdomyosarcoma | 99.71% | L5 | Prediction only |
| 6 | Extrahepatic bile duct rhabdomyosarcoma | 99.71% | L5 | The single paper retrieved covers bile duct carcinoma, not rhabdomyosarcoma |
| 7 | Liver sarcoma | 99.68% | L4 | Most papers concern colorectal liver metastases; the few on liver sarcoma are retrospective or anecdotal |
| 8–10 | Sickle cell syndromes (Hb C, Hb E, HPFH) | 99.62% | L5 | Speculative fetal haemoglobin induction; hydroxyurea is far better supported, and fluorouracil toxicity is unattractive for a chronic non-malignant disease |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature was retrieved for the top-ranked indication (vaginal botryoid rhabdomyosarcoma). The closest related evidence, for the broader indication of rhabdomyosarcoma (rank 2), is shown below:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3884137](https://pubmed.ncbi.nlm.nih.gov/3884137/) | 1985 | Review | Cancer | Overview of adjuvant chemotherapy for childhood sarcomas, including rhabdomyosarcoma |
| [6277228](https://pubmed.ncbi.nlm.nih.gov/6277228/) | 1981 | Review | Ann Acad Med Singapore | General review of curable cancers, including childhood rhabdomyosarcoma |
| [3951398](https://pubmed.ncbi.nlm.nih.gov/3951398/) | 1986 | Cohort | Med Pediatr Oncol | Childhood nasopharyngeal carcinoma series (different tumour type) |
| [42483493](https://pubmed.ncbi.nlm.nih.gov/42483493/) | 2026 | Case report | Case Rep Oncol Med | Adult lingual rhabdomyosarcoma; cisplatin plus 5-fluorouracil was followed by disease progression, and a later vincristine/actinomycin D-based regimen was used |

These papers are indirect and do not demonstrate a fluorouracil-specific benefit in rhabdomyosarcoma.

---

## India Market Information

Twenty valid single-ingredient injectable registrations are on record; the licence records contain no approved-indication text. Five examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 91285 | Fivoflu 250mg Injection | Vial of 5 ml injection | Not recorded |
| 90158 | Fivotop 500 Injection | Ampoule of 10 ml injection | Not recorded |
| 85231 | Fluracil 500mg Injection | Vial of 10 ml injection | Not recorded |
| 91059 | Flocil 250mg Injection | Vial of 5 ml injection | Not recorded |
| 87925 | Fivocil 500mg Injection | Vial of 5 ml injection | Not recorded |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine antimetabolite) |
| Myelosuppression Risk | Medium to high; knowledge-graph contraindications include thrombocytopenia, neutropenia, agranulocytosis and leukopenia |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes; consider DPD deficiency screening |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please also refer to the package insert warnings and precautions.

---

## Safety Considerations

- **Contraindications / conditions of concern (from the knowledge graph, not label text):** kidney disease, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, leukopenia, diarrheal disease, active peptic ulcer disease, pharyngitis, stomatitis, pyoureter, and dihydropyrimidine dehydrogenase deficiency.
- **Drug Interactions:** 361 interactions were identified in total. Those graded Moderate are **metronidazole** and **tinidazole**. Minor interactions include cimetidine and levofloxacin. Many others (e.g., omeprazole, pantoprazole, metformin, morphine, palonosetron) have no assigned severity.

Please refer to the package insert for label warnings, as these were not available in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials or literature for the lead indication, and standard rhabdomyosarcoma therapy does not include fluorouracil. Fluorouracil also has a significant myelosuppressive and mucosal toxicity profile.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical or clinical data showing a fluorouracil-specific effect in embryonal rhabdomyosarcoma
- Comparison against standard regimens (VAC/VDC) to define any unmet need
- Review of the other predicted indications (e.g., liver sarcoma) for any better-supported lead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

