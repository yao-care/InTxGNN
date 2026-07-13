---
layout: default
title: Estramustine
parent: 僅模型預測 (L5)
nav_order: 286
evidence_level: L5
indication_count: 10
---

# Estramustine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Estramustine: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Estramustine (Emcyt/Estracyt) is a hybrid cytotoxic agent combining estradiol-17β and a nornitrogen mustard carbamate, originally developed and FDA-approved for palliative treatment of metastatic and/or progressive prostate cancer.
The TxGNN model predicts it may be applicable to **Prostate Cancer/Brain Cancer Susceptibility** — a mechanistic association node in the knowledge graph — with **0 clinical trials** and **0 publications** directly supporting this specific combined susceptibility indication.
The prediction is anchored on EMBP (estramustine-binding protein) expression in malignant brain tumors, but this remains a model-derived association with no translational clinical evidence to date.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer (metastatic/progressive; palliative treatment) |
| Predicted New Indication | Prostate Cancer/Brain Cancer Susceptibility |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally available in this Evidence Pack. Based on published literature within the evidence pack, Estramustine exerts its antitumor effects by binding to microtubule-associated proteins (MAPs) and tubulin, causing depolymerization of cytoplasmic microtubules and cell cycle arrest at the G2/M phase. Importantly, it selectively accumulates in prostate tissue through a specific 46 kDa glycoprotein known as estramustine-binding protein (EMBP), which mediates tissue selectivity. The drug also carries an estrogenic component that suppresses the hypothalamic–pituitary–gonadal axis, reducing circulating androgens.

The TxGNN model likely established the "prostate cancer/brain cancer susceptibility" node via EMBP biology: multiple studies have demonstrated EMBP expression in malignant gliomas in both rats and humans (PMID 11131983). Elevated EMBP levels in rat astrocytoma correlated with poor prognosis, creating a molecular bridge between prostate-specific drug binding and brain tumor tissue in the knowledge graph. The estramustine-binding site has also been identified in breast cancer (PMID 1888147) and melanoma cells, suggesting EMBP is not strictly prostate-confined. This broad tissue distribution of the target protein is the biological rationale the model may have exploited.

However, "prostate cancer/brain cancer susceptibility" as a clinical entity is ambiguous — it is a knowledge graph concept representing co-susceptibility or mechanistic overlap rather than a defined treatment indication. A separate Phase II study of Taxol + Estramustine in recurrent glioblastoma multiforme exists (PMID 10930101), suggesting translational interest in brain tumors does exist, but the current Evidence Pack did not retrieve this under the susceptibility node. Without a clear and actionable clinical question, this prediction cannot be advanced without further target clarification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for the "prostate cancer/brain cancer susceptibility" indication.

---

## Literature Evidence

Currently no related literature available specifically for the "prostate cancer/brain cancer susceptibility" indication.

---

## India Market Information

Estramustine is currently not marketed in India. No product registrations or authorization numbers are on record.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Alkylating agent/Microtubule disruptor hybrid (estradiol–nornitrogen mustard conjugate) |
| Myelosuppression Risk | Low to moderate — Less myelosuppressive than classical alkylating agents due to EMBP-mediated selective tissue uptake; however, CBC monitoring is required, as leukopenia and thrombocytopenia have been reported |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver function tests (LFTs), renal function, serum calcium, cardiovascular monitoring (thromboembolic risk from estrogenic component including DVT and PE) |
| Handling Protection | Standard cytotoxic drug handling regulations apply — gloves, gown, and appropriate waste disposal required |

---

## Safety Considerations

Please refer to the package insert for key warnings and contraindications (formal India/FDA package insert data not available in this Evidence Pack).

**Drug Interactions** (111 interactions documented; clinically representative moderate interactions listed below):

| Interacting Drug | Level | Clinical Relevance |
|-----------------|-------|--------------------|
| Metformin | Moderate | Estrogenic component may alter insulin sensitivity and glucose metabolism |
| Dexamethasone | Moderate | Pharmacodynamic interaction; corticosteroid co-administration may amplify metabolic and adrenal effects |
| Hydrocortisone | Moderate | Additive steroid-estrogen metabolic interaction |
| Budesonide | Moderate | Potential additive adrenal axis suppression |
| Canagliflozin / Dapagliflozin / Empagliflozin | Moderate | Estrogenic effects may interfere with SGLT2 inhibitor-mediated glucose handling |
| Alogliptin / Linagliptin | Moderate | Possible pharmacokinetic interaction with DPP-4 inhibitor metabolism pathway |
| Amphotericin B | Moderate | Additive electrolyte disturbances (hypokalemia, hypomagnesemia) — close monitoring required |
| Calcium Phosphate / Calcium Acetate | Moderate | Calcium chelation may significantly reduce estramustine oral bioavailability — must not be co-administered with dairy products or calcium-containing supplements |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a near-perfect TxGNN prediction score (99.99%), the indication "prostate cancer/brain cancer susceptibility" is not a clinically actionable treatment target — zero clinical trials and zero publications were retrieved for this combined susceptibility node, and the disease definition itself is ambiguous in a drug repurposing context.

**To proceed, the following is needed:**

- **Clarify the clinical question**: If the intent is to explore Estramustine for brain tumors (glioblastoma/glioma), re-query the Evidence Pack using "glioblastoma multiforme" or "malignant glioma" as the target indication to retrieve the existing Phase II data (PMID 10930101)
- **Remediate DG001**: Download and parse the FDA/EMA package insert PDF to obtain full warnings, contraindications, and precaution data
- **Remediate DG002**: Query DrugBank API for complete MOA and pharmacodynamic profile of Estramustine (DB01196)
- **Preclinical validation**: Confirm EMBP expression levels and estramustine cytotoxicity in relevant brain tumor cell lines before considering clinical development for neurological indications
- **India market pathway**: Assess regulatory filing requirements for India given current "Not Marketed" status — a new drug application pathway would be required
- **Consider investigating rank 8 (Female Breast Carcinoma) as an alternative repurposing target**, which has 2 completed Phase II clinical trials and 20 supporting publications, representing a substantially stronger evidence base for near-term development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

