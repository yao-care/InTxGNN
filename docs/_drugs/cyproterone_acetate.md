---
layout: default
title: Cyproterone Acetate
parent: High Evidence (L1-L2)
nav_order: 220
evidence_level: L2
indication_count: 10
---

# Cyproterone Acetate
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Cyproterone Acetate: From Androgen-Dependent Disorders to Amenorrhea (Hyperandrogenic Menstrual Irregularity)

## One-Sentence Summary

Cyproterone acetate (CPA) is an antiandrogen/progestogen historically used for androgen-dependent conditions (hirsutism, acne, hyperandrogenism) and as a component of combined oral contraceptives; it is **not currently marketed in Taiwan** (0 registrations). Among 10 TxGNN-predicted indications in this evidence pack, the only one with substantive clinical support is **Amenorrhea**, backed by **4 clinical trials and 14 publications**, including a Phase IV RCT directly testing CPA-containing formulations. The nominal #1 TxGNN-ranked prediction (migraine disorder) and several others (thrombophilia, antithrombin deficiency, Prinzmetal angina) have **no supporting evidence and, on closer review, actively contradict CPA's known prothrombotic safety profile** — these are flagged below rather than promoted.

> **Note on methodology**: This evidence pack contains 10 ranked TxGNN candidates. Rather than mechanically reporting the raw #1 TxGNN score (migraine disorder, L5/L4, no trials, safety-contradictory), this report highlights the candidate with actual decision-relevant evidence (Amenorrhea, L2, S3, "Proceed with Guardrails") and documents the others as screened-out/rejected signals for transparency.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Androgen-dependent conditions (hirsutism, acne, PCOS-related hyperandrogenism); chemical castration in prostate cancer/BPH; component of combined oral contraceptives *(sourced from DrugBank pharmacology data — formal `original_indications`/`original_moa` fields are not populated in this pack)* |
| Predicted New Indication | Amenorrhea (hyperandrogenic menstrual irregularity / PCOS) |
| TxGNN Prediction Score | 99.28% (score 0.9928; internal rank 11,216) |
| Evidence Level | L2 |
| Taiwan Market Status | Not marketed (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not formally available in this evidence pack (`original_moa` = data gap). However, pharmacology data captured in the DDI record show CPA's primary molecular target is the **Androgen Receptor (AR)**, consistent with its established clinical use as an antiandrogen: it is used for "chemical castration in patients with various androgen-dependent diseases... and is used to treat acne and hirsutism in females," with its progestogen activity also exploited in combined oral contraceptive pills.

Amenorrhea in the context of PCOS/hyperandrogenism is mechanistically the *least novel* of the 10 candidates — it is essentially an already-established use of CPA (typically as ethinyl estradiol + cyproterone acetate, e.g. Diane-35-type formulations) for correcting menstrual irregularity driven by excess androgen. Suppressing gonadotropin secretion and free testosterone with CPA restores ovarian cyclicity, which explains why this is the only candidate with real trial and literature support.

By contrast, the top TxGNN-ranked candidates (migraine disorder, migraine with brainstem aura, Prinzmetal angina, antithrombin deficiency, heparin cofactor 2 deficiency, factor 5 excess with thrombosis, breast fibrocystic disease) have **no clinical trial or literature evidence** in this pack, and several are flagged by the evidence itself as mechanistically **contradictory** — CPA/ethinyl estradiol combinations are well documented to *increase* thromboembolic risk, making them a plausible relative contraindication rather than a treatment opportunity for clotting-disorder-related diagnoses.

---

## Clinical Trial Evidence (Amenorrhea)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01103518](https://clinicaltrials.gov/study/NCT01103518) | Phase 4 | Unknown | 100 | Randomized, double-blind comparison of two ethinyl estradiol + cyproterone acetate preparations for menstrual irregularities of hyperandrogenic origin |
| [NCT04831151](https://clinicaltrials.gov/study/NCT04831151) | N/A | Unknown | 42 | Effect of CPA-containing vs. drospirenone-containing combined oral contraceptives on blood metabolomics in PCOS |
| [NCT02744131](https://clinicaltrials.gov/study/NCT02744131) | N/A | Unknown | 100 | OCP (EE+CPA) vs. metformin for clinical/hormonal/metabolic features of PCOS in Indian women |
| [NCT02729545](https://clinicaltrials.gov/study/NCT02729545) | Phase 2 | Completed | 60 | Tung's acupuncture vs. Diane-35 (CPA/EE) as control for ovarian function in PCOS (CPA used as active comparator, not primary intervention) |

---

## Literature Evidence (Amenorrhea)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2946604](https://pubmed.ncbi.nlm.nih.gov/2946604/) | 1986 | Multicenter Clinical Trial | Fertility and Sterility | Compared low-dose (Diane, 2mg) vs. high-dose (Androcur, 100mg) CPA in 158 patients with severe hirsutism; both effective, similar dropout rates |
| [9130733](https://pubmed.ncbi.nlm.nih.gov/9130733/) | 1997 | Cohort/Clinical Study | Human Reproduction | GnRH agonist + EE-CPA pill vs. EE-CPA pill alone in PCOD-related hyperandrogenism; evaluated added benefit of GnRH-a |
| [2528199](https://pubmed.ncbi.nlm.nih.gov/2528199/) | 1989 | Review | Rev Fr Gynecol Obstet | CPA identified as the most effective available antiandrogen for skin hyperandrogenism; recommends co-prescribing estrogen to prevent amenorrhea |
| [6232474](https://pubmed.ncbi.nlm.nih.gov/6232474/) | 1984 | Review | Obstet Gynecol Annual | Review of polycystic ovarian disease management |
| [17162716](https://pubmed.ncbi.nlm.nih.gov/17162716/) | 2006 | Case Report | Gynecol Endocrinol | Hormonal therapy inducing therapeutic amenorrhea used to manage recurrent catamenial pneumothorax |
| [1589384](https://pubmed.ncbi.nlm.nih.gov/1589384/) | 1992 | Case Report | Postgrad Med J | CPA + ethinyl estradiol used for 3 years to manage hirsutism/secondary amenorrhea from androgen-producing adrenal adenomas |
| [2137793](https://pubmed.ncbi.nlm.nih.gov/2137793/) | 1990 | Case Series | Fertility and Sterility | GnRH agonist + antiandrogen therapy reversed hirsutism while preserving fertility in familial virilization syndrome |
| [23365131](https://pubmed.ncbi.nlm.nih.gov/23365131/) | 2013 | Case Report | J Clin Endocrinol Metab | Virilizing ovarian tumor case in McCune-Albright syndrome |
| [35592826](https://pubmed.ncbi.nlm.nih.gov/35592826/) | 2022 | Case Report | Ann Med Surg | Congenital adrenal hyperplasia (21-hydroxylase deficiency) presenting with virilization in adolescence |
| [12266391](https://pubmed.ncbi.nlm.nih.gov/12266391/) | 1984 | Review | J Bras Ginecol | Review of a new ovulation-inhibitor antiandrogen |

---

## Screened-Out TxGNN Candidates (No Evidence or Safety-Contradictory)

For transparency, the remaining 9 predicted indications from this evidence pack were reviewed and **not** advanced, despite high TxGNN scores:

| Rank | Disease | TxGNN Score | Evidence | Why Rejected |
|------|---------|------|------|------|
| 1 | Migraine disorder | 99.66% | 3 literature (no trials) | Indirect hormone-therapy literature only; CPA/estrogen combinations are a relative contraindication in migraine with aura due to vascular risk |
| 2 | Migraine with brainstem aura | 99.58% | None | No evidence; hormonal combinations are contraindicated in this migraine subtype |
| 3 | Prinzmetal angina | 99.52% | None | No evidence; no known mechanistic link (coronary vasospasm) |
| 4 | Antithrombin deficiency type 2 | 99.48% | None | **Mechanism-contradictory** — CPA/OC combinations increase thrombosis risk; relative contraindication, not a treatment opportunity |
| 5 | Heparin cofactor 2 deficiency | 99.45% | None | Same as above |
| 6 | Factor 5 excess with spontaneous thrombosis | 99.45% | None | Same as above (Factor V Leiden interaction documented as risk-additive) |
| 7 | Migraine susceptibility | 99.34% | None | Genetic susceptibility marker, not a treatable indication |
| 9 | Breast fibrocystic disease | 99.15% | None | Plausible mechanism (progestogen effect) but zero supporting evidence |
| 10 | Thrombophilia | 99.03% | 18 literature (all reverse-signal) | **Mechanism-contradictory** — all 18 papers document CPA/EE combinations *increasing* venous/arterial thromboembolic risk (APC resistance, thrombin generation); this is a safety signal, not a repurposing opportunity |

---

## Safety Considerations

**Formal `key_warnings` and `contraindications` fields are not populated in this evidence pack (data gap) — please refer to the package insert for official safety information.**

**Important Safety Signal (from literature evidence, not formal safety fields):** Across the "thrombophilia" candidate's 18 associated publications, CPA-containing combined hormonal formulations (particularly with ethinyl estradiol) are consistently associated with **increased venous and arterial thromboembolic risk** — including deep vein thrombosis, cerebral venous sinus thrombosis, and interaction with inherited thrombophilia (e.g., Factor V Leiden). This should be treated as a safety caution for any CPA use, including the amenorrhea/PCOS indication discussed above.

**Drug Target Data:** CPA's primary pharmacological target is the Androgen Receptor (AR, human), confirming its antiandrogen mechanism (CAS 427-51-0). No formal DDI severity level was returned for this record.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for the Amenorrhea/PCOS indication only)

**Rationale:**
- One Phase IV RCT plus a consistent body of cohort and case evidence supports CPA (as EE+CPA combinations) for correcting hyperandrogenic amenorrhea/menstrual irregularity — this is largely an extension of already-documented antiandrogen/contraceptive use rather than a novel mechanism.
- Thromboembolic risk is a well-documented safety guardrail that must accompany any use recommendation.
- All other TxGNN-predicted indications in this pack (migraine, Prinzmetal angina, thrombophilia-related disorders, breast fibrocystic disease) lack supporting evidence and, for the clotting-disorder predictions, are mechanistically contradicted by CPA's known prothrombotic profile — these should remain on **Hold**.

**To proceed, the following is needed:**
- Official TFDA/CDSCO package insert warnings and contraindications (currently a Blocking data gap per `DG001`)
- Formal mechanism-of-action documentation (`DG002`)
- A thrombosis-risk-focused safety review before any amenorrhea/PCOS repurposing pathway advances past S3
- Confirmation that no Taiwan marketing authorization currently exists (0 registrations recorded) before any regulatory pathway planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

