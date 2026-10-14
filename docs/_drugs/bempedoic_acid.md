---
layout: default
title: Bempedoic Acid
parent: Model Prediction Only (L5)
nav_order: 94
evidence_level: L5
indication_count: 10
---

# Bempedoic Acid
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

# Bempedoic Acid: From LDL-Cholesterol Lowering to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Bempedoic acid is an oral cholesterol-lowering drug marketed in India. The TxGNN model's top-ranked prediction is hyperthyroidism, which has no supporting evidence. The only prediction with real literature support is **homozygous familial hypercholesterolemia (HoFH)**, backed by **0 clinical trials** and **18 publications**, mostly reviews plus one real-world study. This report therefore focuses on HoFH.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Indian licence records compiled for this report (the drug is a cholesterol-lowering agent) |
| Predicted New Indication | Homozygous familial hypercholesterolemia (best-supported candidate; the rank 1 prediction is hyperthyroidism) |
| TxGNN Prediction Score | 99.48% (hyperthyroidism, rank 1: 99.61%) |
| Evidence Level | L4 (HoFH); L5 for the other nine predictions |
| India Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold (HoFH may be treated as a research question) |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. Based on known information, bempedoic acid inhibits ATP-citrate lyase (ACLY), an enzyme upstream of HMG-CoA reductase in hepatic cholesterol synthesis. This increases LDL-receptor expression and lowers LDL-C. It also affects AMPK-related pathways.

HoFH is an extreme form of the same problem, with very high LDL-C caused by defective LDL-receptor function. The biological link to the drug's LDL-lowering action is therefore strong. A caveat applies: the drug's effect relies on residual LDL-receptor activity, so the response in HoFH is expected to be modest and to depend on genotype.

The other nine predictions are weak:
- **Hyperthyroidism, hyperthyroxinemia, thyroid hormone resistance:** no known link to thyroid hormone regulation. The high scores are probably network-propagation artifacts.
- **Infectious bovine rhinotracheitis, malignant catarrh:** veterinary viral diseases with no plausible human link. Both have identical scores, suggesting a shared graph artifact.
- **Cytomegalovirus infection:** only a theoretical hypothesis that viral replication depends on host lipid synthesis.
- **Drug-induced and pregnancy-associated osteoporosis, multiple endocrine neoplasia:** no mechanistic rationale or evidence. Pregnancy is also a safety concern for lipid-lowering agents.

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the ten predicted indications.

## Literature Evidence

All publications below relate to HoFH. No HoFH-specific RCT was identified.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41274797](https://pubmed.ncbi.nlm.nih.gov/41274797/) | 2026 | Real-world observational study | J Clin Lipidol | Evaluates efficacy and tolerability of bempedoic acid in HoFH patients |
| [41741298](https://pubmed.ncbi.nlm.nih.gov/41741298/) | 2026 | Expert consensus | J Clin Lipidol | National Lipid Association update on familial hypercholesterolemia diagnosis and management |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | Emerging LDL-C-lowering therapies, including bempedoic acid and inclisiran |
| [35466160](https://pubmed.ncbi.nlm.nih.gov/35466160/) | 2022 | Review | J Atheroscler Thromb | Advances in HoFH treatment; aggressive LDL-C reduction is central |
| [41106315](https://pubmed.ncbi.nlm.nih.gov/41106315/) | 2025 | Review | Exp Mol Pathol | Innovative therapies for HoFH |
| [37071085](https://pubmed.ncbi.nlm.nih.gov/37071085/) | 2024 | Review | Cardiol Rev | Evinacumab for HoFH, with other options including bempedoic acid |
| [34081216](https://pubmed.ncbi.nlm.nih.gov/34081216/) | 2021 | Review | Curr Cardiol Rep | Management of familial and refractory hypercholesterolemias beyond statins and PCSK9 inhibitors |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart J | Traditional and novel non-statin lipid-lowering drugs |
| [38576462](https://pubmed.ncbi.nlm.nih.gov/38576462/) | 2024 | Review | Am J Prev Cardiol | Importance of sustained LDL-C lowering in ASCVD prevention |
| [42761917](https://pubmed.ncbi.nlm.nih.gov/42761917/) | 2026 | Review | Methodist DeBakey Cardiovasc J | Overview of familial hypercholesterolemia |

## India Market Information

The compiled licence records do not include approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 25911 | Bemdac 180mg Tablet (Cadila Healthcare) | Strip of 10 tablets | Not stated |
| 25897 | Brillo 180mg Tablet (Sun Pharmaceutical) | Strip of 10 tablets | Not stated |
| 59914 | Dapcea Tablet (Biocon) | Strip of 10 tablets | Not stated |
| 26507 | Belmore Tablet (Cadila Pharmaceuticals) | Strip of 10 tablets | Not stated |
| 25839 | Bempesta Tablet (Torrent) | Strip of 10 tablets | Not stated |

Two more registrations exist: Nexred Tablet (Dr Reddy's, 150969) and Bempify Tablet 180mg (Lupin, 26183). All 7 are valid single-ingredient products.

## Safety Considerations

- **Drug Interactions:** 23 interactions were found. The 20 detailed entries include:
  - **Major:** hydrocortisone, prednisolone, prednisone, methylprednisolone, dexamethasone, betamethasone, triamcinolone, budesonide, deflazacort, fludrocortisone, levofloxacin, simvastatin
  - **Moderate:** rosuvastatin, empagliflozin, glyburide, repaglinide, rifaximin, selexipag, fexofenadine, revefenacin

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Nine of the ten predictions have no clinical or literature support and are likely artifacts of the model. HoFH is biologically plausible and has some literature, including one real-world study. However, there are no trials, no HoFH-specific RCT, and no safety label data, so it is best treated as a research question rather than a candidate to advance.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator or manufacturers (currently a blocking gap)
- Approved indication text for the Indian licences
- Detailed mechanism-of-action data from DrugBank
- Critical appraisal of the real-world HoFH study (PMID 41274797), including genotype-stratified response
- A planned HoFH-specific trial or registry, and a review of interaction management with statins (especially simvastatin) and corticosteroids
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

