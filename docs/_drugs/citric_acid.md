---
layout: default
title: Citric Acid
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 8
---

# Citric Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Citric Acid: From No Registered Indication to Stomach Disease (Predicted)

## One-Sentence Summary

Citric acid (DrugBank DB04272) has no recorded approved indication and is not currently marketed in India; its original mechanism of action is not yet documented in this evidence pack.
The TxGNN model predicts a possible association with **Stomach Disease**, with **29 clinical trials** and **20 publications** retrieved during evidence collection — but on review, the overwhelming majority are keyword co-occurrence noise rather than direct evidence of therapeutic use.
The strongest genuine signal is citric acid's established role as a **diagnostic adjuvant** (13C-urea breath test) and as a **citrate-salt calcium supplement**, not as a treatment for gastric disease itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on record (drug is not currently marketed in India) |
| Predicted New Indication | Stomach Disease |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for citric acid is not currently available in this evidence pack. Based on known pharmacology, citric acid is a naturally occurring component of human gastric juice and a common pharmaceutical excipient (effervescent formulations, citrate salts, pH modifiers). It is also used clinically as an oral adjuvant meal to improve gastric distension and diagnostic accuracy in the **13C-urea breath test** for *Helicobacter pylori* detection — a diagnostic, not therapeutic, application.

The link between citric acid and "stomach disease" in the retrieved evidence is therefore largely indirect: most of the 29 clinical trials returned by the search (e.g., mosapride vs. metoclopramide, ETEC vaccine studies, ketone supplement trials) share only superficial keyword overlap with "stomach" and do not involve citric acid as an intervention at all. The genuinely relevant subset relates to **calcium citrate** (a citrate salt, not citric acid as a therapeutic agent) used for calcium supplementation in conditions such as hypoparathyroidism and post-gastrectomy calcium malabsorption, where citrate's acid-independent absorption is mechanistically plausible in low-gastric-acid states.

Overall, mechanistic plausibility exists mainly for **diagnostic use** (urea breath test adjuvant) and for **citrate-salt formulations** in calcium malabsorption contexts, rather than for direct treatment of "stomach disease" as a therapeutic indication. This distinction is important and should be clarified before any further development is considered.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03812380](https://clinicaltrials.gov/study/NCT03812380) | Phase 3 | Terminated | 62 | Evaluated effervescent calcium magnesium **citrate** to prevent PPI-related complications (fractures, hypomagnesemia, CKD risk) in patients with gastric ulcer/GERD; trial terminated before completion |
| [NCT03425747](https://clinicaltrials.gov/study/NCT03425747) | Phase 4 | Completed | 26 | Compared calcium **citrate** vs. calcium carbonate for chronic hypoparathyroidism; relevant to calcium absorption independent of gastric acid, not a gastric-disease treatment trial itself |
| [NCT02830789](https://clinicaltrials.gov/study/NCT02830789) | NA | Completed | 38 | Compared calcium **citrate** vs. calcium carbonate for secondary hyperparathyroidism after Roux-en-Y gastric bypass, where gastric acid deficiency impairs carbonate absorption |
| [NCT04350346](https://clinicaltrials.gov/study/NCT04350346) | NA | Unknown | 70 | Motilitone vs. Gasmotin for functional dyspepsia in gallstone patients; no citric acid intervention — keyword co-occurrence only |
| [NCT06826443](https://clinicaltrials.gov/study/NCT06826443) | Phase 3 | Not yet recruiting | 100 | Mosapride vs. metoclopramide for enteral feeding intolerance in ICU patients; no citric acid intervention |
| [NCT02180334](https://clinicaltrials.gov/study/NCT02180334) | Phase 4 | Completed | 12 | Mosapride + DPP-4 inhibitor effect on incretin hormones; no citric acid intervention |

**Note:** Of the 29 trials retrieved for "stomach disease," the remaining ~23 (e.g., ETEC vaccine trials, ketone-supplement performance studies, H. pylori microbiome studies, oncology chemotherapy trials) were assessed as low relevance / keyword co-occurrence and are not included above, as they do not involve citric acid as an intervention.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31505905](https://pubmed.ncbi.nlm.nih.gov/31505905/) | 2019 | Cohort | Gut and Liver | Citric acid test meal improves accuracy of the 13C-urea breath test for H. pylori detection in Asian populations — a diagnostic, not therapeutic, application |
| [9379358](https://pubmed.ncbi.nlm.nih.gov/9379358/) | 1997 | Preclinical | J Pharm Pharmacol | A bismuth–citric acid complex salt (MX1) showed gastroprotective effect against stress-induced ulcers in rats |
| [35900644](https://pubmed.ncbi.nlm.nih.gov/35900644/) | 2022 | Cohort | Metabolomics | High serum citric acid (inversely correlated with alkaline phosphatase) detectable in Koreans prior to gastric cancer onset — potential biomarker, not treatment |
| [6027230](https://pubmed.ncbi.nlm.nih.gov/6027230/) | 1967 | Descriptive/Biochemical | Gastroenterology | Foundational study quantifying citric acid as a natural constituent of human gastric juice |
| [4000241](https://pubmed.ncbi.nlm.nih.gov/4000241/) | 1985 | Cohort | New England Journal of Medicine | Citrate-form calcium is better absorbed than carbonate-form in achlorhydric patients, supporting citrate's acid-independent absorption mechanism |
| [37477784](https://pubmed.ncbi.nlm.nih.gov/37477784/) | 2024 | Review | Clin Transl Oncol | Reviews energy metabolism (including the citric acid/TCA cycle) as a therapeutic target in gastric cancer — mechanistic context, not a citric acid intervention study |
| [38959111](https://pubmed.ncbi.nlm.nih.gov/38959111/) | 2024 | Cohort | Cell Reports | Metabolic subtyping of gastric cancer identifies a subtype with upregulated TCA (citric acid) cycle activity and distinct prognosis |
| [9889978](https://pubmed.ncbi.nlm.nih.gov/9889978/) | 1998 | Review | Adv Microb Physiol | Reviews H. pylori physiology/metabolism in the stomach; citric acid not a direct intervention |

**Note:** The remaining publications retrieved (e.g., cuproptosis in gastric cancer, dietary fiber/obesity, veterinary cobalamin deficiency) reference "citric acid" only in a biochemical or unrelated context and were excluded as low relevance.

---

## India Market Information

Citric acid is **not currently marketed in India** under this evidence pack (0 registrations on record). No product licenses, brand names, or approved indication text are available for review.

---

## Safety Considerations

**Drug Interactions:** Query of the DDI database returned 15 documented interactions, most involving reduced absorption of fluoroquinolone antibiotics via chelation with citrate/citrate-containing products:

| Interacting Drug | Severity |
|---|---|
| Aluminum hydroxide | Major |
| Ciprofloxacin | Moderate |
| Levofloxacin | Moderate |
| Moxifloxacin | Moderate |
| Norfloxacin | Moderate |
| Ofloxacin | Moderate |
| Gatifloxacin | Moderate |
| Gemifloxacin | Moderate |
| Lomefloxacin | Moderate |
| Enoxacin | Moderate |
| Nalidixic acid | Moderate |
| Trovafloxacin | Moderate |
| Grepafloxacin | Moderate |
| Sparfloxacin | Moderate |
| Cinoxacin | Moderate |

Co-administration with fluoroquinolone antibiotics should be spaced apart to avoid chelation-mediated reduction in antibiotic absorption; the combination with aluminum hydroxide warrants particular caution given its Major-level rating.

No key warnings or contraindications data are currently available; please refer to the package insert for further safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted association between citric acid and stomach disease is not supported by direct clinical or trial evidence — the retrieved trials and literature point mainly to citric acid's role as a **diagnostic adjuvant** (urea breath test) or as a **citrate salt** for calcium supplementation, not as a gastric-disease treatment. Combined with a blocking data gap in India regulatory/label safety information (DG001) and the drug's current non-marketed status in India, there is insufficient basis to proceed at this time.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for citric acid (DG002)
- India/TFDA-equivalent package insert warnings and contraindications (DG001, blocking)
- Clarification of whether the intended repurposing use is diagnostic (breath-test adjuvant) or therapeutic, since current evidence supports only the former
- A dedicated, disease-specific evidence review distinguishing citric acid itself from citrate-salt formulations (e.g., calcium citrate), which behave differently pharmacologically
- If therapeutic use is intended, prospective or at minimum well-designed observational studies directly testing citric acid (not citrate salts or unrelated comparator drugs) in stomach disease populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

