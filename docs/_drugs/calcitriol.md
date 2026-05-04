---
layout: default
title: Calcitriol
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 7
---

# Calcitriol
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

# Calcitriol: From Hypoparathyroidism and Renal Bone Disease to Hereditary Hypophosphatemic Rickets

## One-Sentence Summary

Calcitriol (1,25-dihydroxyvitamin D₃) is the biologically active hormonal form of Vitamin D, used globally for hypoparathyroidism, secondary hyperparathyroidism, and renal osteodystrophy, but currently **not registered in India**.
Among TxGNN's 7 predicted indications, **Hereditary Hypophosphatemic Rickets** is the most evidence-supported repurposing target, backed by **7 clinical trials** and **20 publications** — the only prediction in this analysis reaching L2 evidence level.
> ⚠️ Note: TxGNN's top-scored prediction (rank 1) uses the deprecated ontology term "obsolete vitamin D deficiency" with zero retrievable evidence; hereditary hypophosphatemic rickets (rank 7 by model score, rank 1 by evidence strength) is therefore the primary focus of this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in India; globally indicated for hypoparathyroidism, secondary hyperparathyroidism, and renal osteodystrophy |
| Predicted New Indication | Hereditary Hypophosphatemic Rickets |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L2 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Hereditary Hypophosphatemic Rickets — most commonly X-linked Hypophosphatemia (XLH), caused by loss-of-function mutations in the *PHEX* gene — is defined by chronic FGF23 overproduction from bone. Elevated FGF23 simultaneously suppresses two critical renal processes: tubular phosphate reabsorption (via NaPi-2a/2c transporters) and 1α-hydroxylase (CYP27B1) activity. This creates a dual deficit — renal phosphate wasting alongside inappropriately low endogenous Calcitriol synthesis — leading to defective bone and cartilage mineralization, manifesting as rickets in children and osteomalacia in adults.

Calcitriol's therapeutic rationale is mechanistically precise: by supplying the active hormone exogenously, it bypasses FGF23-mediated CYP27B1 suppression entirely. Combined with oral phosphate supplementation, Calcitriol restores intestinal calcium and phosphate absorption through upregulation of TRPV6, calbindin-D9k, and NaPi-2b, facilitating normal bone mineralization. This Calcitriol + phosphate regimen has constituted the global standard of care for XLH for over four decades, and Phase 4 trials are now focused on weight-based dosing optimization in pediatric patients.

It is important to note that the anti-FGF23 monoclonal antibody burosumab (Crysvita) has demonstrated superior long-term outcomes over Calcitriol + phosphate in XLH and has received regulatory approval in the US, EU, Japan, and other markets. In resource-adequate settings, burosumab is now the preferred first-line approach. However, Calcitriol + phosphate remains a clinically validated, cost-accessible alternative — and is particularly relevant for India, where burosumab is not yet accessible.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Early Phase 1 | Active, Not Recruiting | 20 | **Most directly relevant trial**: Calcitriol monotherapy (without phosphate) in children and adults with XLH — dose escalation over 3 months evaluating serum phosphate, skeletal mineralization, growth, and nephrocalcinosis risk |
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Phase 4 | Unknown | 100 | High vs. low dose Calcitriol + neutral phosphate in XLH children — establishes evidence-based weight-adjusted dosing; strongest practice-level evidence in this analysis |
| [NCT06046820](https://clinicaltrials.gov/study/NCT06046820) | Phase 3 | Active, Not Recruiting | 27 | ENERGY 3 Study: INZ-701 (ENPP1 deficiency) — provides comparative efficacy framework relative to active vitamin D–based standard of care |
| [NCT04846647](https://clinicaltrials.gov/study/NCT04846647) | N/A | Completed | 260 | Observational study of FGF23 hypersecretion in genetic hypophosphatemia (completed April 2022); large cohort defining patient characteristics and pathophysiology |
| [NCT01526304](https://clinicaltrials.gov/study/NCT01526304) | N/A | Unknown | 150 | Cross-sectional study of FGF23/Klotho/Sclerostin in kidney stone formers; provides general FGF23-axis background |
| [NCT06921720](https://clinicaltrials.gov/study/NCT06921720) | N/A | Not Yet Recruiting | 65 | ³¹P-MRS ATP measurement in phosphate diabetes (XLH); novel energy metabolism biomarker study, not yet recruiting |
| [NCT00844740](https://clinicaltrials.gov/study/NCT00844740) | N/A | Withdrawn | 0 | Cinacalcet in familial hypophosphatemic rickets — withdrawn before enrollment, reflecting prior failed exploration of calcimimetic alternatives |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40295317](https://pubmed.ncbi.nlm.nih.gov/40295317/) | 2025 | Clinical Guideline Review | Calcified Tissue International | Current XLH diagnosis and therapy guidelines: Calcitriol + phosphate as established standard of care, with burosumab as emerging preferred option |
| [39181153](https://pubmed.ncbi.nlm.nih.gov/39181153/) | 2024 | Comprehensive Review | Lancet | X-linked hypophosphataemia: PHEX mutations, FGF23 excess, suppressed Calcitriol synthesis, and full treatment landscape |
| [36446330](https://pubmed.ncbi.nlm.nih.gov/36446330/) | 2022 | Systematic Review | Hormone Research in Paediatrics | Rickets, Vitamin D, and Ca/P metabolism: historical and current evidence synthesis for Calcitriol across rickets subtypes |
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Review | Nutrients | Rickets types and treatment: comparative evidence for Calcitriol, alphacalcidol, ergocalciferol, and cholecalciferol across genetic and nutritional rickets |
| [29292875](https://pubmed.ncbi.nlm.nih.gov/29292875/) | 2017 | Clinical Analysis | Pediatric Endocrinology Reviews | Early Calcitriol + phosphate therapy outcomes in 127 XLH patients across 49 centres: growth response and height trajectories |
| [35226335](https://pubmed.ncbi.nlm.nih.gov/35226335/) | 2022 | Longitudinal Cohort | Journal of Endocrinological Investigation | Growth and body proportion from birth to adulthood in hereditary hypophosphatemic rickets: limb disproportion pattern under treatment |
| [31392510](https://pubmed.ncbi.nlm.nih.gov/31392510/) | 2020 | Review | Pediatric Nephrology | Mineralized tissues in hypophosphatemic rickets: bone, growth plates, and dentition — mechanistic role of Calcitriol in mineralization |
| [3839245](https://pubmed.ncbi.nlm.nih.gov/3839245/) | 1985 | Clinical Study | Journal of Clinical Investigation | High-dose Calcitriol + phosphate heals osteomalacia in XLH where conventional vitamin D therapy failed; key early efficacy demonstration |
| [6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/) | 1980 | Clinical Trial | New England Journal of Medicine | Seminal trial in 11 children with vitamin D-resistant rickets: Calcitriol raised intestinal phosphate absorption and elevated circulating 1,25-OH₂D above normal range |
| [2492895](https://pubmed.ncbi.nlm.nih.gov/2492895/) | 1989 | Cohort Study | Calcified Tissue International | Axial and appendicular bone mineral density in 17 children with familial hypophosphatemia monitored at 6-month intervals following Calcitriol + phosphate initiation |

---

## India Market Information

Calcitriol is currently **not registered in India**. There are no marketing authorizations on record. Regulatory approval from the CDSCO (Central Drugs Standard Control Organisation) would be required before this drug can be legally marketed or prescribed in India.

---

## Safety Considerations

**Drug Interactions (339 total interactions identified):**

*Major interactions requiring active clinical management:*
- **Cholecalciferol** (Major): Additive vitamin D activity — cumulative hypercalcemia and hypercalciuria risk
- **Calcifediol** (Major): Additive vitamin D precursor effect — serum calcium monitoring mandatory
- **Burosumab** (Major): Anti-FGF23 antibody combination may unpredictably elevate endogenous + exogenous Calcitriol, leading to severe hypercalcemia

*Notable moderate interactions:*
- **Thiazide diuretics** (Hydrochlorothiazide, Chlorothiazide, Chlorthalidone, Bendroflumethiazide, Benzthiazide): Reduce renal calcium excretion, amplifying Calcitriol-induced hypercalcemia
- **Cardiac glycosides** (Digoxin, Digitoxin): Calcitriol-induced hypercalcemia sensitizes myocardium to digitalis toxicity — cardiac monitoring required
- **Anticonvulsants** (Carbamazepine, Fosphenytoin, Amobarbital, Butalbital, Butabarbital): CYP450 induction accelerates Calcitriol catabolism, significantly reducing efficacy
- **Bile acid sequestrants** (Cholestyramine, Colesevelam, Colestipol): Impair fat-soluble vitamin absorption — separate dosing by ≥4 hours
- **Aluminum hydroxide**: Impairs phosphate absorption and alters Calcitriol metabolism — avoid concurrent use
- **Calcipotriol (topical)**: Systemic absorption contributes an additive vitamin D effect

> Complete warnings and contraindications: Please retrieve and review the full package insert (CDSCO/manufacturer label). Formal safety data was not available in this Evidence Pack (Data Gap DG001).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Calcitriol combined with phosphate supplementation has been the evidence-based standard of care for hereditary hypophosphatemic rickets for over 40 years, supported by a Phase 4 dosing optimization RCT (NCT03820518, n=100) and an ongoing calcitriol monotherapy trial (NCT03748966), alongside multiple published clinical series dating back to seminal NEJM and JCI publications. The mechanism is directly tied to FGF23-mediated suppression of endogenous Calcitriol synthesis — making this a replacement therapy with strong biological grounding, not an exploratory repurposing. In the Indian context, where burosumab remains inaccessible, Calcitriol + phosphate represents the primary viable evidence-based intervention for this rare pediatric skeletal disorder.

**To proceed, the following is needed:**

- **Regulatory pathway**: Submit a New Drug Application (NDA) or import license application to CDSCO — Calcitriol is not currently registered in India
- **Resolve data gaps**: Retrieve the full package insert to address DG001 (TFDA/CDSCO warnings and contraindications) and DG002 (complete MOA documentation)
- **Hypercalcemia monitoring protocol**: Establish regular monitoring of serum calcium, urinary calcium-to-creatinine ratio, and serum creatinine — particularly critical given 3 major DDIs with other vitamin D compounds
- **Nephrocalcinosis surveillance**: Renal ultrasound at baseline and periodic follow-up, especially in pediatric patients on long-term Calcitriol + phosphate
- **Pediatric dosing guidelines**: Adopt weight-based dosing protocol informed by Phase 4 trial data (NCT03820518); standardize starting dose (typically 0.25–1.5 μg/day) and phosphate supplementation regimen
- **Positioning vs. burosumab**: Define patient population and access criteria where Calcitriol + phosphate is the preferred choice, in anticipation of eventual burosumab availability in India
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

