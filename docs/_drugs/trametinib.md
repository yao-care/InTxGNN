---
layout: default
title: Trametinib
parent: 僅模型預測 (L5)
nav_order: 846
evidence_level: L5
indication_count: 10
---

# Trametinib
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

# Trametinib: From Cutaneous BRAF-Mutant Melanoma to Non-Cutaneous Melanoma

## One-Sentence Summary

> Trametinib is a MEK1/2 inhibitor originally approved (in combination with the BRAF inhibitor dabrafenib) for **BRAF V600E/K mutation-positive cutaneous melanoma**, as well as anaplastic thyroid cancer and NSCLC with the same mutation.
> The TxGNN model predicts it may also be effective for **non-cutaneous melanoma** (mucosal, acral, uveal/ocular and other rare-site subtypes),
> with **50 clinical trials** currently supporting BRAF/MEK inhibition across melanoma populations, and case-level literature specifically describing activity in non-cutaneous subtypes (conjunctival, eyelid, lacrimal sac melanoma).

Note: this Evidence Pack (`TW-DB08911-multi`) actually scores 10 candidate indications for trametinib. Most (choroideremia, scrotum melanoma, balloon cell melanoma) are pure network-similarity artifacts with **no mechanistic basis and no supporting studies** (all scored L5/Hold). This report focuses on **non-cutaneous melanoma**, the only candidate with strong trial evidence (L2) and a clear pharmacological rationale; other melanoma-subtype candidates (acral lentiginous, nodular, superficial spreading — all L3) are summarized in the closing section.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | BRAF V600E/K mutation-positive metastatic **cutaneous melanoma** (± dabrafenib); also anaplastic thyroid cancer and NSCLC in combination with dabrafenib (per DrugBank pharmacology record — India label text not available, see below) |
| Predicted New Indication | Non-cutaneous melanoma |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L2 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Trametinib is a reversible, highly selective allosteric inhibitor of MEK1 and MEK2 (MAP2K1/MAP2K2), the kinases immediately downstream of BRAF in the MAPK/ERK signaling cascade. In BRAF V600E/K-mutant tumors this pathway is constitutively active, driving proliferation; blocking MEK downstream of the mutated BRAF protein shuts down the signal regardless of exactly where in the pathway the mutation acts. This is why trametinib is almost always used together with a BRAF inhibitor (dabrafenib) — dual blockade of BRAF and MEK produces deeper, more durable responses than either agent alone and is now standard of care in BRAF-mutant cutaneous melanoma.

Non-cutaneous melanoma is not a single disease but a family of rare-site subtypes (mucosal, acral, uveal, conjunctival, eyelid, lacrimal sac) that share the same melanocytic lineage as cutaneous melanoma. The key caveat is that BRAF V600 mutation frequency is **lower and more variable** in these subtypes — acral and mucosal melanomas are more often driven by NRAS or KIT, and uveal melanoma is typically GNAQ/GNA11-driven rather than BRAF-driven. However, in the subset of non-cutaneous melanomas that *do* carry a BRAF V600 mutation, the MAPK/ERK dependency is mechanistically identical to cutaneous disease, and published case reports document clinical responses to BRAF/MEK dual inhibition in conjunctival melanoma (PMID 27893585), bulbar conjunctival melanoma (PMID 31361915), and lacrimal sac melanoma (PMID 31747798). This supports mechanistic extrapolation **conditional on confirmed BRAF V600 mutation status** rather than a blanket class effect.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01972347](https://clinicaltrials.gov/study/NCT01972347) | Phase 2 | Active, not recruiting | 35 | Neoadjuvant dabrafenib + trametinib in resectable AJCC Stage IIIB-C BRAF V600-mutant melanoma; direct trametinib use, graded highly relevant |
| [NCT02910700](https://clinicaltrials.gov/study/NCT02910700) | Phase 2 | Active, not recruiting | 52 | Triplet nivolumab + dabrafenib + trametinib in BRAF-mutated Stage III-IV melanoma |
| [NCT01584648](https://clinicaltrials.gov/study/NCT01584648) | Phase 3 | Completed | 423 | Pivotal COMBI-d trial: dabrafenib+trametinib vs dabrafenib+placebo, first-line BRAF V600E/K melanoma |
| [NCT01597908](https://clinicaltrials.gov/study/NCT01597908) | Phase 3 | Completed | 704 | COMBI-v: dabrafenib+trametinib vs vemurafenib monotherapy, BRAF V600E/K melanoma |
| [NCT01245062](https://clinicaltrials.gov/study/NCT01245062) | Phase 3 | Completed | 322 | METRIC: trametinib monotherapy vs chemotherapy (dacarbazine/paclitaxel), BRAF V600E/K melanoma |
| [NCT01941927](https://clinicaltrials.gov/study/NCT01941927) | Phase 2 | Completed | 20 | Trametinib + AKT inhibitor GSK2141795 in **BRAF wild-type** melanoma — relevant model for BRAF-negative non-cutaneous subtypes |
| [NCT02083354](https://clinicaltrials.gov/study/NCT02083354) | Phase 2 | Completed | 77 | Dabrafenib+trametinib in BRAF V600-mutant **acral lentiginous** or cutaneous melanoma |
| [NCT02039947](https://clinicaltrials.gov/study/NCT02039947) | Phase 2 | Completed | 127 | Dabrafenib+trametinib in BRAF-mutant melanoma with **brain metastases** |
| [NCT02224781](https://clinicaltrials.gov/study/NCT02224781) | Phase 3 | Active, not recruiting | 267 | DREAMseq: sequencing of immunotherapy vs dabrafenib+trametinib in Stage III-IV BRAF V600-mutant melanoma |
| [NCT03149029](https://clinicaltrials.gov/study/NCT03149029) | Phase 2 | Active, not recruiting | 16 | Abbreviated MAPK-targeted therapy (dabrafenib+trametinib) plus pembrolizumab, unresectable/metastatic melanoma |

*40 additional trials are recorded in the underlying evidence base (mostly dabrafenib+trametinib combination or trametinib-monotherapy studies establishing BRAF/MEK activity in melanoma broadly); the above 10 were prioritized for direct relevance to trametinib use and to non-cutaneous-relevant contexts (BRAF wild-type, acral, brain metastasis).*

---

## Literature Evidence

Currently no dedicated publications are indexed under the "non-cutaneous melanoma" candidate itself. However, subtype-specific case evidence exists for closely related predicted candidates in this Evidence Pack and directly informs the mechanistic rationale above:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27893585](https://pubmed.ncbi.nlm.nih.gov/27893585/) | 2017 | Case report | Ophthalmic Plast Reconstr Surg | Conjunctival melanoma with BRAF V600E mutation responsive to systemic BRAF/MEK inhibition |
| [31361915](https://pubmed.ncbi.nlm.nih.gov/31361915/) | 2020 | Case report/Review | Clin Exp Dermatol | Two cases of BRAF-mutated bulbar conjunctival (epithelioid) melanoma treated with BRAF-targeted therapy |
| [31747798](https://pubmed.ncbi.nlm.nih.gov/31747798/) | 2019 | Case report/Review | J Investig Med High Impact Case Rep | Lacrimal sac malignant melanoma, 15 Japanese patients reviewed |

---

## India Market Information

Trametinib currently has **no registered license in India** (`market_status: 未上市 / Not Marketed`, 0 total registrations). No brand names, dosage forms, or approved indication text are available from the local regulatory dataset. Global label information (via DrugBank pharmacology data) indicates approval for BRAF V600 mutation-positive cutaneous melanoma (monotherapy and adjuvant, combined with dabrafenib), anaplastic thyroid cancer (combined with dabrafenib), and EMA orphan designation for BRAF V600E-mutant glioma.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK1/2 inhibitor; non-cytotoxic mechanism) |
| Myelosuppression Risk | Low — MEK inhibitors are not classically myelosuppressive; mild anemia/lymphopenia has been reported but severe neutropenia is uncommon |
| Emetogenicity Classification | Low |
| Monitoring Items | Cardiac function (LVEF, echocardiogram — class effect of MEK inhibitors), ophthalmologic exam (risk of retinal vein occlusion/retinal pigment epithelial detachment), blood pressure, skin toxicity assessment, liver function tests, CBC |
| Handling Protection | Oral hazardous antineoplastic agent — follow institutional cytotoxic/hazardous-drug handling precautions (e.g., NIOSH antineoplastic list) despite the non-cytotoxic mechanism of action |

---

## Safety Considerations

Official India-specific warnings and contraindications are not available in this Evidence Pack (data gap DG001, flagged **Blocking** — TFDA/CDSCO label text has not yet been retrieved).

- **Drug Interactions**: 17 documented interactions (DDInter, all rated Moderate), predominantly with other kinase inhibitors and CYP-metabolized oncology agents: Fostamatinib, Elagolix, Apalutamide, Brigatinib, Dabrafenib, Encorafenib, Isavuconazonium, Lasmiditan, Midostaurin, Sarecycline, Enzalutamide, Erdafitinib, Gilteritinib, Idelalisib, Tucatinib. Co-administration in a repurposing protocol should include a structured DDI screen given the number of oncology-drug overlaps.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Non-cutaneous melanoma has genuine mechanistic plausibility and Phase 2/3-level evidence (L2) for BRAF/MEK inhibition in BRAF-mutant melanoma populations, but the guardrail is essential: BRAF V600 mutation status must be confirmed before use, since non-cutaneous subtypes have lower and more variable BRAF mutation rates than cutaneous melanoma. Related subtypes with mutation-confirmed responses (acral lentiginous L3, nodular L3, superficial spreading L3) support the same conditional logic. Candidates with no mechanistic or trial support (choroideremia, scrotum melanoma, balloon cell melanoma — all L5) should remain on Hold and not be pursued further under this repurposing program.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: obtain official India (CDSCO) label warnings/contraindications before any S1 safety review can proceed
- Resolve high-priority data gap DG002: confirm DrugBank-sourced MOA record to formalize the mechanistic dossier
- Since the drug is not currently registered in India, a regulatory pathway (new registration or import license) must be scoped before any clinical use
- Require BRAF V600 mutation testing protocol as an eligibility gate for any non-cutaneous melanoma repurposing study
- Given the DDI count, build an oncology-specific interaction checklist for co-administered targeted/immuno-oncology agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

