---
layout: default
title: Cladribine
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 7
---

# Cladribine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

Using the drug-repurposing evidence pack you provided, here is the evaluation report. Note upfront: the JSON's own `taiwan_regulatory` block, `TFDA` remediation source, and `TW-DB00242` candidate ID all indicate this is a **Taiwan (TFDA)** dataset, not India/CDSCO as the generic prompt header states — I've labeled the market-status section accordingly rather than guessing at India-specific data that isn't in the pack.

Also flagging per the "no guessing" rule: `drug.original_indications` is empty and `taiwan_regulatory.licenses` is empty, so the original indication cannot be extracted from this evidence pack — I've marked it as a data gap rather than filling it in from outside knowledge.

---

# Cladribine: From Original Indication (Not Specified in Evidence Pack) to Parameningeal Embryonal Rhabdomyosarcoma

## One-Sentence Summary

Cladribine's original approved indication is not recorded in this evidence pack (drug-level data gap), and the compound is not currently marketed in Taiwan. The TxGNN model predicts potential efficacy for **Parameningeal Embryonal Rhabdomyosarcoma**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure knowledge-graph association with no independent validation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (data gap — `drug.original_indications` and `taiwan_regulatory.licenses` are both empty) |
| Predicted New Indication | Parameningeal Embryonal Rhabdomyosarcoma |
| TxGNN Prediction Score | 99.77% (raw score 0.9977; graph rank 4548) |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for cladribine is flagged as a **High-severity data gap (DG002)** in this evidence pack — no `original_moa` value is available directly from DrugBank. However, the pack's own mechanistic-rationale notes (attached to the related "rhabdomyosarcoma (disease)" candidate) describe cladribine as a **purine nucleoside analog** whose cytotoxic selectivity depends on a high intracellular ratio of deoxycytidine kinase (dCK) to 5′-nucleotidase (5′-NT) activity — a profile characteristic of lymphoid lineage cells (B/T cells), which is consistent with cladribine's known clinical use in hairy-cell leukemia-type lymphoid malignancies.

Because the original indication is not recorded here, a direct comparison between the original and predicted indications cannot be made from this evidence pack alone. What can be assessed is the biological plausibility of extending a lymphoid-selective cytotoxic mechanism to rhabdomyosarcoma, which is a tumor of **myogenic (skeletal muscle precursor) lineage**, not lymphoid lineage.

On that basis, the evidence pack's own rationale concludes the mechanistic fit is weak: rhabdomyosarcoma's cell-of-origin biology does not match the dCK/5′-NT selectivity profile that underlies cladribine's known activity, and no published data demonstrate this ratio in rhabdomyosarcoma. The high TxGNN score (99.77%) reflects a strong graph-embedding association, not a validated pharmacological mechanism — this is the classic profile of an L5 (model-prediction-only) candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

(Confirmed by explicit zero-result queries against ClinicalTrials.gov and ICTRP for "parameningeal embryonal rhabdomyosarcoma" + cladribine, dated 2026-03-27.)

## Literature Evidence

Currently no related literature available.

(Confirmed by an explicit zero-result PubMed query for "parameningeal embryonal rhabdomyosarcoma" + cladribine, dated 2026-03-27. Note: a separate, lower-ranked candidate indication in this batch — "liver sarcoma" — did return one tangentially related case report (PMID 15241520) on cladribine in smoldering systemic mastocytosis, but the evidence pack's own rationale flags that match as likely a keyword/indexing overlap rather than genuine clinical evidence, and it does not apply to the top-ranked indication evaluated in this report.)

## Taiwan Market Information

No approved products are currently registered in Taiwan for cladribine (`market_status`: 未上市 / Not Marketed; `total_licenses`: 0). No license records are available to summarize.

## Cytotoxicity

Cladribine is classified here as antineoplastic based on its documented mechanism (purine nucleoside antimetabolite with dCK/5′-NT-dependent cytotoxic selectivity), which falls within a recognized cytotoxic chemotherapy category.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside antimetabolite) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (no specific toxicity data in this evidence pack; TFDA label data is a Blocking data gap — DG001) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions (no data in this evidence pack) |
| Monitoring Items | Please refer to the package insert warnings and precautions (no data in this evidence pack) |
| Handling Protection | Cytotoxic drug handling regulations should apply, consistent with its conventional cytotoxic classification |

## Safety Considerations

- **Drug Interactions**: DDI screening returned 344 total interactions. Major-level interactions include corticosteroids (Hydrocortisone, Triamcinolone, Dexamethasone, Betamethasone, Budesonide, Prednisolone, Prednisone, Triamcinolone ophthalmic), radioimmunotherapy/radiopharmaceutical agents (Ibritumomab tiuxetan, Iobenguane I-131, Tositumomab, Tositumomab I-131, Samarium (153Sm) lexidronam, Strontium chloride Sr-89), and Deferiprone. Moderate-level interactions include Dipyridamole, Cilostazol, Eltrombopag, and Palifermin. Acetylsalicylic acid shows an interaction of unclassified ("Unknown") severity.

Key warnings and contraindications are not available in this evidence pack — this is flagged as a **Blocking data gap (DG001: TFDA label warnings/contraindications)**, meaning this candidate cannot yet complete a full S1 safety pre-screen.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has zero clinical trial or literature support, a mechanistic rationale that the evidence pack itself assesses as weak (lymphoid-selective mechanism vs. myogenic tumor biology), and a Blocking-severity data gap on TFDA safety labeling (DG001) that prevents even an initial safety screen. The high TxGNN score alone (L5, prediction-only) is insufficient to advance this candidate.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001 — Blocking; required before any S1 safety evaluation)
- Confirmed mechanism of action from DrugBank (DG002 — required for mechanistic-link analysis)
- The original approved indication(s) for cladribine, to properly assess original-vs-new indication similarity
- Preclinical or in-vitro data establishing whether rhabdomyosarcoma cell lines exhibit the dCK/5′-NT activity profile relevant to cladribine's cytotoxic selectivity
- Any future clinical trial, case report, or preclinical publication specifically evaluating cladribine in rhabdomyosarcoma (none currently exist)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

