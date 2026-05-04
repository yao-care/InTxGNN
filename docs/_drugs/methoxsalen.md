---
layout: default
title: Methoxsalen
parent: 僅模型預測 (L5)
nav_order: 333
evidence_level: L5
indication_count: 10
---

# Methoxsalen
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

# Methoxsalen: From PUVA Therapy (CTCL / Psoriasis) to Localized Pagetoid Reticulosis

## One-Sentence Summary

Methoxsalen is a psoralen (furocoumarin) compound that functions as the photosensitizing agent in PUVA (Psoralen + UVA) therapy, with established clinical use in psoriasis, vitiligo, and cutaneous T-cell lymphoma (CTCL) — including FDA-approved applications in mycosis fungoides and Sézary syndrome, as well as extracorporeal photopheresis (ECP).
The TxGNN model predicts it may be effective for **Localized Pagetoid Reticulosis (Woringer-Kolopp Disease)**, a rare indolent variant of CTCL presenting as a solitary intraepidermal T-cell plaque.
Currently, **0 clinical trials** and **0 publications** are directly available for this specific indication; the prediction rests entirely on mechanistic extrapolation from its established role in closely related CTCL disorders.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | PUVA therapy for psoriasis, vitiligo, and CTCL (mycosis fungoides / Sézary syndrome) |
| Predicted New Indication | Localized Pagetoid Reticulosis (Woringer-Kolopp Disease) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Methoxsalen is a psoralen that undergoes photoactivation by long-wave ultraviolet A (UVA) light, forming covalent monoadducts and interstrand crosslinks with pyrimidine bases in DNA. This halts cell division and triggers apoptosis preferentially in rapidly proliferating or aberrant lymphocytes. The mechanism underpins both topical/systemic PUVA therapy and extracorporeal photopheresis (ECP), in which patient leukocytes are treated with methoxsalen ex vivo before UVA irradiation — a technique FDA-approved for erythrodermic CTCL. Detailed MOA documentation from DrugBank was not available in the current evidence pack, and full confirmation should be obtained.

Localized Pagetoid Reticulosis (Woringer-Kolopp disease) is a rare, indolent variant of CTCL characterised by a solitary, slowly expanding cutaneous plaque with intraepidermal proliferation of CD8+ (or CD4+) neoplastic T cells. Because PUVA therapy is already an established first-line option for localized, early-stage CTCL variants, the mechanistic logic is biologically sound: the same DNA crosslinking and T-cell apoptosis pathway that underlies PUVA's efficacy in mycosis fungoides can be directly extrapolated to this histologically related condition. The extreme rarity of the disease (fewer than 200 cases reported globally) largely explains the absence of dedicated clinical trials.

It is important to recognise this remains an **indirect mechanistic extrapolation** with no published case series or prospective evidence specifically addressing methoxsalen in pagetoid reticulosis. The TxGNN model's high score (99.97%) most likely reflects the shared T-cell ontology and spatial co-occurrence of CTCL variants in the knowledge graph, rather than independently validated clinical efficacy. Comparing with the rank-2 prediction — indolent primary cutaneous T-cell lymphoma (score 99.91%, L3 evidence, 2 supporting publications on ECP) — this prediction is plausible but requires further empirical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Methoxsalen is currently **not marketed in India**. No drug licences have been registered with the Indian regulatory authority (CDSCO), and no approved product information is available from domestic sources.

---

## Cytotoxicity

Methoxsalen is used as the active photosensitizing agent in PUVA photochemotherapy and ECP for CTCL (a T-cell malignancy), qualifying it for oncology-specific safety review.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Photochemotherapy agent — Psoralen class; mechanism: photoactivated DNA interstrand crosslinking and apoptosis induction in aberrant T lymphocytes |
| Myelosuppression Risk | Low — primary toxicity is phototoxicity and cutaneous carcinogenesis, not bone marrow suppression |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (hepatotoxicity risk); ophthalmological examination (UVA-induced cataract risk — UV-protective eyewear mandatory during and for 24 h after dosing); long-term skin cancer surveillance (squamous cell carcinoma risk with cumulative PUVA exposure) |
| Handling Protection | Standard precautions; patients must avoid sunlight and UV exposure for 8–24 h post-dose; systemic methoxsalen has a narrow therapeutic window requiring dose adjustment by body weight |

---

## Safety Considerations

**Drug Interactions (126 interactions identified; representative moderate-level interactions shown below):**

| Interacting Drug | Level | Clinical Concern |
|-----------------|-------|-----------------|
| Doxycycline / Doxycycline (topical) | Moderate | Additive phototoxicity risk |
| Tetracycline / Tetracycline (topical) | Moderate | Additive phototoxicity risk |
| Minocycline / Minocycline (topical) | Moderate | Additive phototoxicity risk |
| Levofloxacin | Moderate | Additive phototoxicity risk |
| Promethazine | Moderate | Additive phototoxicity risk |
| Sulfasalazine | Moderate | Additive phototoxicity risk |
| Sulfamethizole | Moderate | Additive phototoxicity risk |
| Chlorpropamide / Glimepiride / Glipizide / Glyburide / Tolazamide / Tolbutamide / Acetohexamide | Moderate | Possible pharmacokinetic interaction with sulfonylureas |
| Ibuprofen / Flurbiprofen | Moderate | Additive phototoxicity risk |
| Alosetron | Moderate | Interaction mechanism under review |

A total of 126 drug interactions have been identified in the DDInter database. The predominant interaction pattern is **additive phototoxicity** with other photosensitizing agents (tetracyclines, fluoroquinolones, phenothiazines, sulfonamides, NSAIDs). Please refer to the package insert for complete warnings, contraindications, and carcinogenicity data, which were not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
The mechanistic basis for using methoxsalen (via PUVA) in localized pagetoid reticulosis is biologically plausible given the shared T-cell pathobiology with CTCL, but the complete absence of dedicated clinical trials or published case series means this cannot be advanced beyond hypothesis generation at this stage. Additionally, methoxsalen is not currently registered in India, creating an additional regulatory barrier.

**To proceed, the following is needed:**

- **Evidence generation**: Systematic case series or retrospective registry data documenting PUVA outcomes specifically in pagetoid reticulosis patients
- **Regulatory pathway**: Assessment of CDSCO registration requirements for methoxsalen in India, given zero current approvals
- **Safety data**: Retrieval and review of CDSCO/TFDA-equivalent package insert for complete key warnings and contraindications (currently a blocking data gap)
- **MOA documentation**: DrugBank API query to formally document methoxsalen's mechanism of action and support mechanistic link analysis
- **Administration feasibility**: Evaluation of whether topical PUVA (preferred for localized lesions) vs. systemic PUVA is appropriate, given the solitary plaque presentation of Woringer-Kolopp disease
- **Consider rank-2 prediction first**: The indolent primary cutaneous T-cell lymphoma indication (rank 2, L3 evidence, 2 supporting publications on ECP) offers a more evidence-supported entry point and may be a preferable initial focus

> **Research disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

