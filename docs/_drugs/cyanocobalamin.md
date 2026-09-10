---
layout: default
title: Cyanocobalamin
parent: 僅模型預測 (L5)
nav_order: 212
evidence_level: L5
indication_count: 1
---

# Cyanocobalamin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Cyanocobalamin: From Vitamin B12 Deficiency to Biotin Metabolic Disease

## One-Sentence Summary

Cyanocobalamin (vitamin B12, DB00115) is a cobalamin-class vitamin whose established use is treating vitamin B12 deficiency; detailed Taiwan-approved indication text and mechanism-of-action data are not currently available. The TxGNN model predicts a possible link to **Biotin Metabolic Disease** with a **99.60% prediction score**, but the identified evidence base (15 clinical trials, 20 publications) is largely generic B-vitamin/nutrition research rather than trials or literature specific to cyanocobalamin in biotin metabolic disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin B12 deficiency (general pharmacology; Taiwan-specific approved indication text unavailable — drug not currently marketed in Taiwan) |
| Predicted New Indication | Biotin metabolic disease |
| TxGNN Prediction Score | 99.60% (rank 7182) |
| Evidence Level | L4 |
| Taiwan (TFDA) Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for cyanocobalamin is not available (DrugBank query returned no structured MOA). Based on known pharmacology, cyanocobalamin is a synthetic form of vitamin B12 (cobalamin), acting as a cofactor for methionine synthase and methylmalonyl-CoA mutase; its established clinical role is correcting vitamin B12 deficiency and related megaloblastic anemia/neurological disease.

"Biotin metabolic disease" refers to disorders of vitamin B7 (biotin) metabolism, such as biotinidase deficiency and multiple carboxylase deficiency — a distinct cofactor system from cobalamin, with no established shared biochemical pathway. The TxGNN score of 99.60% is therefore more likely explained by **ontology adjacency** than by a direct mechanistic link: cobalamin-, folate-, biotin-, and thiamine-responsive inborn errors of metabolism are frequently grouped together in the literature and knowledge-graph structure as a single "vitamin-responsive/cofactor-responsive IEM" cluster, which can inflate similarity scores between individually unrelated cofactor systems.

Given this, the prediction should be treated as a **hypothesis requiring manual verification of the TxGNN disease-node definition**, not as evidence of a genuine pharmacological relationship. This assessment is reinforced by the absence of any clinical trial or publication directly testing cyanocobalamin in biotin metabolic disease patients.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | Completed | 6,824 | Universal newborn genomic screening panel (126 treatable genetic diseases); may include biotinidase deficiency but is a screening, not treatment, study — not specific to cyanocobalamin (Grade C). |
| [NCT01474486](https://clinicaltrials.gov/study/NCT01474486) | N/A | Completed | 40 | Multi-micronutrient palliative intervention in CHF patients; not specific to biotin metabolic disease or cyanocobalamin alone (Grade C). |
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | N/A | Unknown | 200 | Cross-over RCT of Q10 ubiquinol + multivitamin B/E in autism (incl. Phelan-McDermid syndrome); no clear link to biotin metabolic disease (Grade C). |
| [NCT03444155](https://clinicaltrials.gov/study/NCT03444155) | N/A | Completed | 30 | Pilot comparison of natural vs. synthetic vitamin B-complex bioavailability; not disease-specific (Grade C). |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Phase 2 | Completed | 75 | Vitamin/mineral supplementation for neuropathy/nephropathy in type 2 diabetes; unrelated to biotin metabolic disease (Grade C). |
| [NCT04586348](https://clinicaltrials.gov/study/NCT04586348) | Phase 4 | Active, not recruiting | 794 | Prenatal iodine supplementation and neurodevelopment; no direct relevance to cyanocobalamin or biotin metabolic disease (Grade C). |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Transdermal vitamin absorption in post-bariatric-surgery patients; general micronutrient study, not disease-specific (Grade C). |
| [NCT02426775](https://clinicaltrials.gov/study/NCT02426775) | Phase 3 | Completed | 33 | Long-term effectiveness of carglumic acid in propionic/methylmalonic acidemia; related organic acidemias but no direct cyanocobalamin-biotin link (Grade C). |
| [NCT00572741](https://clinicaltrials.gov/study/NCT00572741) | N/A | Completed | 39 | Targeted nutritional intervention for oxidative stress/methylation defects in autism; not biotin-metabolic-disease specific (Grade C). |
| [NCT01558193](https://clinicaltrials.gov/study/NCT01558193) | N/A | Completed | 202 | Multivitamin/mineral ± fatty acid supplementation and behavior; unrelated to target indication (Grade C). |

*(An additional 5 trials returned by the search were not yet relevance-graded — NCT02302729, NCT03655223, NCT05832190, NCT04067921, NCT01643187.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review (Tier 1) | Handbook of Clinical Neurology | Reviews vitamin-responsive disorders including cobalamin, folate, biotin, B1, and E — the most directly relevant source, discussing cobalamin and biotin as parallel but distinct cofactor-dependent disease categories. |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Review/Case Series (Tier 2) | Pediatric Clinics of North America | Discusses megavitamin-responsive aminoacidopathies where B-vitamin cofactors (including B12 and biotin) activate deficient apoenzymes. |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review (Tier 2) | Acta Vitaminologica et Enzymologica | Reviews vitamins implicated in inborn metabolic errors via malabsorption, metabolic errors, or vitamin-dependent syndromes. |
| [11031989](https://pubmed.ncbi.nlm.nih.gov/11031989/) | 2000 | Review (Tier 2) | Ryoikibetsu Shokogun Shirizu | Japanese-language review of vitamin dependency syndromes; abstract not available. |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review (Tier 2) | International Journal of Molecular Sciences | Reviews vitamin B12's cofactor role (methylmalonyl-CoA/biotin-adjacent pathway, methionine synthesis) and neurological effects of deficiency. |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review (Tier 3) | Endocrine, Metabolic & Immune Disorders Drug Targets | Reviews vitamins (including B-group and biotin) in type 2 diabetes; general, not disease-specific. |
| [29173522](https://pubmed.ncbi.nlm.nih.gov/29173522/) | 2017 | Review (Tier 3) | Gastroenterology Clinics of North America | Reviews vitamin/mineral deficiencies in IBD; general micronutrient context. |
| [7015958](https://pubmed.ncbi.nlm.nih.gov/7015958/) | 1980 | Review (Tier 3) | Annals of the New York Academy of Sciences | Reviews interactions among B-complex vitamins including thiamin and riboflavin. |
| [36476407](https://pubmed.ncbi.nlm.nih.gov/36476407/) | 2023 | Preclinical (Tier 3) | The Journal of Endocrinology | Rat study: B12 deficiency induces glucose intolerance and a prediabetic-like phenotype. |
| [1368195](https://pubmed.ncbi.nlm.nih.gov/1368195/) | 1992 | Review — industrial process (Tier 3) | Journal of Chemical Technology and Biotechnology | Reviews biotechnological production of vitamins/coenzymes; not clinically relevant. |

*(10 additional publications were returned but remain unclassified/pending review.)*

---

## Taiwan Market Information

No marketed cyanocobalamin products are currently registered with TFDA under this evidence pack (0 licenses, market status: 未上市 / Not marketed).

---

## Safety Considerations

**Drug Interactions**: 313 total documented interactions on file. Representative interactions include:
- **Minor** — reduced absorption with acid-reducing agents: Famotidine, Ranitidine, Ranitidine (bismuth citrate), Cimetidine, Nizatidine (H2 blockers); Omeprazole, Esomeprazole, Pantoprazole, Lansoprazole, Rabeprazole, Dexlansoprazole (PPIs); and Potassium chloride.
- **Unknown clinical significance** — Metformin, Glimepiride, Rosiglitazone, Acarbose, Doxycycline, Morphine, Mesalazine, Sucralfate.

Taiwan-specific label warnings and contraindications are not currently available in this evidence pack; please refer to the package insert once TFDA labeling data is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the review indicates it is likely driven by ontology adjacency (cofactor-responsive IEMs being clustered together) rather than a genuine biochemical link between cobalamin and biotin pathways. No clinical trial or publication was found that directly tests cyanocobalamin in biotin metabolic disease — all trials are Grade C (tangential) or unassessed, and the strongest literature source (PMID 23622402) discusses cobalamin and biotin as parallel, not overlapping, disorders.

**To proceed, the following is needed:**
- Cyanocobalamin MOA data from DrugBank (DG002, High severity)
- TFDA label warnings/contraindications (DG001, Blocking — required before any S1 safety screening)
- Manual review of the TxGNN "biotin metabolic disease" node definition to rule out an ontology-clustering artifact
- Targeted search for any case reports or trials specifically evaluating cobalamin/B12 supplementation in biotinidase deficiency or multiple carboxylase deficiency patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

