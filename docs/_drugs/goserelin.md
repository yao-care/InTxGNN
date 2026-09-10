---
layout: default
title: Goserelin
parent: 僅模型預測 (L5)
nav_order: 397
evidence_level: L5
indication_count: 3
---

# Goserelin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using the drug-repurposing evaluation report template supplied in the system prompt to structure this directly from the Evidence Pack (no additional skill needed — this is a template-fill task, not a TxGNN pipeline operation).

Two notes before the report: (1) the pack's `taiwan_regulatory` field and the `[Data Gap]` items (TFDA 仿單/MOA) indicate this is a **Taiwan** evidence pack — I've labeled market sections "Taiwan" rather than "India" accordingly, since following the literal template label would misstate the data source. (2) `original_indications` and Taiwan `licenses` are both empty, so no original-indication text exists in the pack itself; Goserelin's original indications (GnRH agonist for prostate/breast cancer, endometriosis) are widely established external knowledge, flagged as such below rather than presented as pack-sourced.

---

# Goserelin: From Hormone-Sensitive Cancer/Endometriosis to Amenorrhea (Ovarian Suppression)

## One-Sentence Summary

Goserelin is a GnRH agonist (marketed internationally as Zoladex) originally used for hormone-sensitive prostate cancer, breast cancer, and endometriosis by inducing medical gonadal suppression. The TxGNN model predicts it may be effective for **Amenorrhea**, with **7 clinical trials** (including multiple completed Phase 3 RCTs) and **19 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not present in this Evidence Pack (Taiwan license data empty). Internationally documented as a GnRH agonist for prostate cancer, breast cancer, and endometriosis — general external knowledge, not sourced from this pack |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (MOA flagged as a High-severity data gap, DG002). Based on generally known pharmacology, Goserelin is a synthetic GnRH agonist: continuous administration causes pituitary desensitization, suppressing FSH/LH secretion and consequently ovarian estrogen production — producing a reversible, drug-induced (medical) amenorrhea.

This is not a mechanistically distant repurposing hypothesis. Inducing amenorrhea/ovarian suppression is already one of Goserelin's established pharmacological effects, used clinically for ovarian protection during chemotherapy in premenopausal breast cancer, and for endometriosis-related pain control via estrogen suppression. The TxGNN prediction essentially recovers a well-documented on-label pharmacological action rather than proposing a novel biological pathway.

One important caveat for interpretation: in most of the supporting trials, "amenorrhea" functions as an induced protective/intermediate endpoint (e.g., preserving ovarian function during chemotherapy, or as a treatment tool for endometriosis/fibroid-related bleeding) rather than amenorrhea being treated as a standalone target disease. This framing should be clarified before advancing past guardrail review.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02483767](https://clinicaltrials.gov/study/NCT02483767) | Phase 3 | Completed | 98 | RCT: goserelin + chemo vs. chemo alone for ovarian function preservation in premenopausal breast cancer during chemotherapy |
| [NCT02132390](https://clinicaltrials.gov/study/NCT02132390) | Phase 3 | Unknown | 300 | Adjuvant toremifene ± goserelin in premenopausal HR+ breast cancer, with/without chemo-induced amenorrhea |
| [NCT03475758](https://clinicaltrials.gov/study/NCT03475758) | Phase 2 | Unknown | 100 | Goserelin for ovarian protection during cyclophosphamide-containing chemotherapy; menstruation outcome |
| [NCT00068601](https://clinicaltrials.gov/study/NCT00068601) | Phase 3 | Completed | 257 | LHRH analog (goserelin) during chemo to reduce ovarian failure in early-stage, HR-negative breast cancer |
| [NCT00488722](https://clinicaltrials.gov/study/NCT00488722) | N/A | Unknown | N/A | Zoladex 3.6mg + CEF neoadjuvant chemo in HR+ premenopausal operable breast cancer; goserelin induces reversible amenorrhea similar to ovarian ablation |
| [NCT01218581](https://clinicaltrials.gov/study/NCT01218581) | Phase 2/3 | Completed | 32 | Aromatase inhibitors vs. GnRH agonists for fertility-preserving management of uterine adenomyosis |
| [NCT00427245](https://clinicaltrials.gov/study/NCT00427245) | Phase 3 | Completed | 400 | OPTION trial: goserelin vs. no goserelin to prevent early menopause in premenopausal breast cancer patients undergoing chemotherapy |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17159194](https://pubmed.ncbi.nlm.nih.gov/17159194/) | 2007 | RCT | J Clin Oncol | IBCSG Trial VIII: chemo + goserelin vs. either alone — impact on amenorrhea, hot flashes, QOL in premenopausal node-negative breast cancer |
| [12488406](https://pubmed.ncbi.nlm.nih.gov/12488406/) | 2002 | RCT | J Clin Oncol | ZEBRA study: goserelin vs. CMF chemo as adjuvant therapy in premenopausal node-positive breast cancer |
| [28472240](https://pubmed.ncbi.nlm.nih.gov/28472240/) | 2017 | RCT | Ann Oncol | Anglo Celtic OPTION trial: GnRH agonist for protection against chemo-induced ovarian toxicity in early breast cancer |
| [8513962](https://pubmed.ncbi.nlm.nih.gov/8513962/) | 1993 | RCT | Fertil Steril | Goserelin vs. low-dose oral contraceptive for endometriosis-associated pelvic pain |
| [14679153](https://pubmed.ncbi.nlm.nih.gov/14679153/) | 2003 | RCT | J Natl Cancer Inst | Adjuvant chemo followed by goserelin vs. either modality alone in node-negative premenopausal breast cancer |
| [25187267](https://pubmed.ncbi.nlm.nih.gov/25187267/) | 2015 | Cohort | Cancer Res Treat | Goserelin ovarian ablation improves survival in Stage II/III HR+ breast cancer patients without chemo-induced amenorrhea |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Cohort | J Clin Oncol | Clinical review on whether estradiol monitoring is needed during goserelin-based ovarian suppression |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Review | J R Army Med Corps | Review of therapeutic induction of amenorrhoea, including GnRH analogue goserelin |
| [12353820](https://pubmed.ncbi.nlm.nih.gov/12353820/) | 2002 | Review | Breast Cancer Res Treat | Overview of LHRH agonists (goserelin) in early breast cancer — reversible ovarian ablation |
| [12734855](https://pubmed.ncbi.nlm.nih.gov/12734855/) | 2003 | Review | Br J Surg | Review of ovarian ablation in adjuvant treatment of pre/perimenopausal breast cancer |

## Taiwan Market Information

Goserelin currently has no Taiwan drug license registered in this Evidence Pack (`market_status: 未上市`, `total_licenses: 0`). No product/dosage-form/indication records are available to tabulate.

## Safety Considerations

**Drug Interactions**: DDInter records 371 total interactions for goserelin. Notable entries include:

- **Major**: Dolasetron
- **Moderate**: Famotidine, Clarithromycin, Palonosetron, and multiple antidiabetic agents (Acarbose, Metformin, Glimepiride, Chlorpropamide, Alogliptin, Linagliptin, Saxagliptin, Canagliflozin, Dapagliflozin, Empagliflozin, Albiglutide, Dulaglutide), plus bowel-prep/laxative agents (Bisacodyl, Picosulfuric acid, Polyethylene glycol 3350 w/ electrolytes), Loperamide

This list reflects only the 19 sample interactions included in the pack, not all 371 — full DDI review is recommended before clinical use.

Key warnings and contraindications are not available in this Evidence Pack (blocking data gap DG001 — TFDA label not yet obtained/parsed).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is supported by multiple completed Phase 3 RCTs (OPTION trial n=400, IBCSG Trial VIII, ZEBRA study) demonstrating goserelin's ability to induce/protect ovarian function suppression, with a mechanistically consistent, well-established pharmacological basis (GnRH agonist-induced medical amenorrhea). However, the drug is not currently marketed in Taiwan, and TFDA label safety data (warnings/contraindications) is a blocking gap.

**To proceed, the following is needed:**
- TFDA 仿單警語與禁忌事項 (DG001, blocking) — obtain and parse from TFDA official source
- Formal MOA documentation from DrugBank (DG002)
- Clarification of clinical framing: induced-amenorrhea-as-ovarian-protection vs. amenorrhea as a standalone treatment target, to define the correct regulatory pathway
- Taiwan market entry / license status confirmation before any local development plan

**Note:** Two additional TxGNN predictions (renal hypoplasia, renal hypoplasia bilateral — scores ~0.99, rank ~13,800) were screened at L5/Hold: no clinical trials, no literature, and no plausible mechanistic link to a GnRH agonist (congenital structural anomalies vs. pharmacologically modulated pathway). These are treated as knowledge-graph embedding noise and are not carried forward.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

