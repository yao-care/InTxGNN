---
layout: default
title: Probenecid
parent: 僅模型預測 (L5)
nav_order: 500
evidence_level: L5
indication_count: 3
---

# Probenecid
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

Using the report structure exactly as specified in your prompt. A few data-fidelity notes before the report:

- `drug.original_indications` is empty and `original_moa` is `[Data Gap]` (DG002) — no original indication/MOA is present in the evidence pack itself. I've used Probenecid's well-established pharmacological classification (uricosuric agent) only where the template's fallback language explicitly calls for it, and flagged it clearly as outside the evidence pack.
- `taiwan_regulatory.licenses` is empty (0 registrations, 未上市) → per your Prohibition #5 ("do not list empty sections"), the Market Information table is omitted rather than shown empty.
- Probenecid is not antineoplastic → Cytotoxicity section omitted per the rules.
- `key_warnings`/`contraindications` are both `[Data Gap]` → excluded per Prohibition #1; only the DDI data (which has real content) is reported under Safety.
- I added one short subsection ("Other Candidate Indications Considered") that isn't in your template's fixed list, because omitting ranks #2 and #3 — which carry real safety signal — would violate "do not omit data." It sits between the reasoning section and the trial/literature tables so the required section order is otherwise untouched.

---

# Probenecid: From Gout and Hyperuricemia to Renal Hypouricemia

## One-Sentence Summary

Probenecid is a classic uricosuric agent historically used to treat gout and chronic hyperuricemia by blocking renal urate reabsorption; its formal original-indication and mechanism-of-action records are not present in this evidence pack (Data Gap DG002). The TxGNN model's top prediction is **Renal Hypouricemia**, scoring **99.73%**, but this is backed by **0 clinical trials** and **20 publications that describe the disease itself** rather than treatment with probenecid — and the evidence pack's own mechanistic rationale flags the prediction as pharmacologically **inverted**, not merely unproven. Combined with a Blocking-severity gap in TFDA safety labeling, the evidence supports a **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout / hyperuricemia (uricosuric agent) — *not present in evidence pack; general pharmacological classification only, see Data Gap DG002* |
| Predicted New Indication | Renal Hypouricemia (hypouricemia, renal) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| India Market Status | ✗ 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed DrugBank mechanism-of-action data is not available for Probenecid (Data Gap DG002). Based on the mechanistic rationale supplied alongside this prediction, Probenecid acts by inhibiting the renal tubular transporters **URAT1 (SLC22A12)** and **OAT1/OAT3**, which blocks urate *reabsorption* and thereby lowers serum uric acid — the pharmacological basis for its traditional use in gout/hyperuricemia.

Renal Hypouricemia is caused by the *opposite* problem: loss-of-function mutations in the same gene, **URAT1/SLC22A12**, that cause patients to already lose too much urate through the kidneys. TxGNN's high score most likely reflects that the drug's molecular target and the disease's causal gene are the *same knowledge-graph node* (URAT1), which the model reads as a strong association — not that the drug corrects the disease.

Mechanistically, this direction is inverted: a drug that further inhibits URAT1-mediated reabsorption would be expected to *worsen* urinary urate loss in a condition already defined by excessive urate loss, rather than treat it. The evidence pack's own rationale states there is "no therapeutic justification" for this pairing. This is a useful illustration of a TxGNN false-positive pattern — shared-target similarity without directional pharmacological logic — rather than a genuine repurposing signal.

---

## Other Candidate Indications Considered (Also Hold)

| Rank | Disease | TxGNN Score | Evidence Level | Trials / Literature | Key Concern |
|------|---------|-------------|-----------------|----------------------|-------------|
| 2 | Lesch-Nyhan Syndrome | 99.39% | L4 | 0 / 4 (all old, tier 3) | HGPRT deficiency causes urate *overproduction*; standard care is xanthine-oxidase inhibition (e.g. allopurinol), not increased excretion. A uricosuric agent risks worsening uric acid crystalluria/nephrolithiasis in this population. |
| 3 | HGPRT Partial Deficiency (Kelley-Seegmiller spectrum) | 99.37% | L5 | 0 / 0 | Same overproduction/excretion mismatch as above, but with **zero** supporting literature or trials — a pure graph-topology extrapolation from the Lesch-Nyhan node. |

All three candidates carry a `decision_stage: S0` and `recommendation: Hold` in the source data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cohort (molecular/genetic) | J Am Soc Nephrol | Sequenced SLC22A12 in 32 Japanese renal hypouricemia patients; established URAT1 loss-of-function as the causal mechanism |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricemia etiologies for rheumatologists |
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Review/Case report | Molecular Genetics and Metabolism | Overview of hereditary renal hypouricemia caused by SLC22A12 (URAT1) mutations |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Case report/Review | Am J Kidney Dis | Renal hypouricemia complicated by exercise-induced acute renal failure |
| [8976099](https://pubmed.ncbi.nlm.nih.gov/8976099/) | 1996 | Review | Nihon Rinsho | Classification of urate metabolism abnormalities (hyper- and hypouricemia) |
| [476267](https://pubmed.ncbi.nlm.nih.gov/476267/) | 1979 | Review | Biomedicine | Review of inborn hypouricemia due to isolated renal tubular defect across 8 families |
| [3813739](https://pubmed.ncbi.nlm.nih.gov/3813739/) | 1987 | Case report | Archives of Internal Medicine | Diabetic patients with renal hypouricemia from increased pyrazinamide-suppressible urate clearance |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Case report | Am J Kidney Dis | Siblings with hereditary renal hypouricemia and exercise-induced acute renal failure |
| [1944743](https://pubmed.ncbi.nlm.nih.gov/1944743/) | 1991 | Case series | Nephron | Type 1 diabetic patients with renal hypouricemia and elevated urate clearance |
| [1656732](https://pubmed.ncbi.nlm.nih.gov/1656732/) | 1991 | Case report | Am J Kidney Dis | Cholangiocarcinoma-associated severe renal hypouricemia |

**Important caveat:** none of the 20 retrieved publications evaluate Probenecid as a *treatment* for renal hypouricemia. Several (e.g. PMID 854144, 8341392, 7099326 — not tabled above) instead use **probenecid as a diagnostic challenge test**: patients with URAT1 loss-of-function show a *blunted* uricosuric response to probenecid, which is used to characterize the transport defect, not to treat it. This reinforces that the literature volume behind this candidate does not constitute therapeutic evidence.

---

## Safety Considerations

**Drug Interactions** (from DDI database; 71 total interactions on file, 20 retrieved in this query):

- **Major**: Phenylbutyric acid, Glycerol phenylbutyrate
- **Moderate**: Acetylsalicylic acid, Chlorpropamide, Glimepiride, Repaglinide, Nateglinide, Tolazamide, Glipizide, Glyburide, Acetohexamide, Tolbutamide
- **Minor**: Famotidine, Amoxicillin, Eluxadoline, Levofloxacin
- **Unknown/unclassified**: Pantoprazole, Morphine, Omeprazole, Lansoprazole

Notably, several Moderate-level interactions involve sulfonylurea antidiabetics (potential potentiation of hypoglycemic effect), and aspirin is known to antagonize probenecid's uricosuric action pharmacodynamically.

TFDA-specific warnings and contraindications are not available in this evidence pack (Data Gap DG001, Blocking severity) — please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking-severity data gap (missing TFDA warnings/contraindications, DG001) means the safety profile cannot clear even an initial S1 review.
- The top-ranked prediction (Renal Hypouricemia) is mechanistically inverted rather than merely under-evidenced — the drug's known pharmacology works against, not toward, this indication — and has zero clinical trials.
- The two lower-ranked candidates (Lesch-Nyhan Syndrome, HGPRT Partial Deficiency) share the same excretion-vs-overproduction mismatch and are supported by minimal-to-no literature or trials.
- All three candidates already carry a `Hold` recommendation and `S0` decision stage in the source scoring.

**To proceed, the following is needed:**
- TFDA/DrugBank package insert data (warnings, contraindications) to close DG001 and DG002
- A pharmacodynamic or preclinical study directly testing probenecid in a URAT1 loss-of-function (renal hypouricemia) model, rather than inferring from shared-gene association
- Independent review of whether the TxGNN score reflects a genuine signal or a shared-node graph artifact, before allocating further evaluation resources to this candidate
- If Lesch-Nyhan-spectrum indications are pursued further, an explicit safety assessment of uricosuric therapy risk (urolithiasis/urate nephropathy) in urate-overproduction states
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

