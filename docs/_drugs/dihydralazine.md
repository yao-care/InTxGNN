---
layout: default
title: Dihydralazine
parent: 僅模型預測 (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
---

# Dihydralazine
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

# Dihydralazine: From Hypertensive Crisis to Heart Disease

## One-Sentence Summary

Dihydralazine is a direct-acting arteriolar vasodilator historically used for hypertensive crises and as an adjunct in congestive heart failure, though it holds no current drug registration in India.
The TxGNN model predicts it may be effective for **Heart Disease**,
with **1 clinical trial** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertensive crisis; adjunct in congestive heart failure (historical use; no India registration) |
| Predicted New Indication | Heart Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is currently unavailable from DrugBank. Based on available literature, Dihydralazine belongs to the hydrazinophthalazine class and functions as a direct arteriolar vasodilator. It reduces systemic vascular resistance (afterload) without directly increasing myocardial contractility. Several French and European clinical studies from the 1980s (marketed as Nepressol) documented its use in NYHA class III–IV congestive heart failure as an adjunct to digitalis and diuretics, based on this afterload-reduction rationale.

The mechanistic link to heart disease is biologically plausible in the short term: reducing afterload allows a failing heart to increase cardiac output. However, this benefit is self-limiting. Pure arteriolar vasodilation reflexively activates the renin-angiotensin-aldosterone system (RAAS) and sympathetic nervous system, leading to compensatory sodium retention, tachycardia, and ultimately tachyphylaxis — exactly the pattern documented in the landmark 1984 European Heart Journal study (PMID 6479183), where long-term benefit was lost compared to placebo.

The TxGNN prediction therefore reflects an established but historically superseded pharmacological association. Dihydralazine was an early vasodilator used before ACE inhibitors demonstrated superior neurohormonal blockade and survival benefit. One active Phase 3 trial (NCT05230901) is re-exploring dihydralazine specifically in the context of post-TAVI myocardial fibrosis alongside spironolactone — a more targeted hypothesis that may offer a rationale for narrow re-evaluation, but cannot yet be attributed to dihydralazine's individual contribution.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT05230901](https://clinicaltrials.gov/study/NCT05230901) | Phase 3 | Recruiting | 300 | Evaluates antifibrotic therapy for regression of myocardial fibrosis post-TAVI in aortic stenosis patients with high fibrotic burden. Three arms: standard of care alone, Spironolactone + standard of care, or Spironolactone + Dihydralazine + standard of care. Dihydralazine is a combination partner, not the primary study drug; efficacy attributable to it specifically cannot be determined from this design. |

> ⚠️ The sole identified trial has **low direct relevance** to Dihydralazine as a therapy for heart disease (Relevance Grade C). No trials testing Dihydralazine as the primary intervention for heart disease were identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [1420010](https://pubmed.ncbi.nlm.nih.gov/1420010/) | 1992 | RCT | Br J Obstet Gynaecol | Compared epoprostenol vs dihydralazine in acute hypertensive crisis of pregnancy; dihydralazine served as the active comparator, supporting its established role in acute BP reduction |
| [29974489](https://pubmed.ncbi.nlm.nih.gov/29974489/) | 2018 | Network Meta-Analysis | Br J Clin Pharmacol | Network meta-analysis of antihypertensives for severe hypertension in pregnancy; includes comparative efficacy and safety data for dihydralazine vs labetalol, nifedipine and others |
| [3075406](https://pubmed.ncbi.nlm.nih.gov/3075406/) | 1988 | Comparative Clinical Study | Acta Physiol Hung | Short-term comparison of captopril (Lopirin, Tensiomin) vs dihydralazine in 15 patients with severe heart failure (NYHA III–IV); ACE inhibitors and dihydralazine both showed hemodynamic benefit acutely |
| [6479183](https://pubmed.ncbi.nlm.nih.gov/6479183/) | 1984 | Clinical Study | Eur Heart J | Long-term dihydralazine vs placebo in 14 severe CHF patients refractory to digitalis/diuretics; acute hemodynamic benefits confirmed but long-term efficacy lost — key tachyphylaxis evidence |
| [6803467](https://pubmed.ncbi.nlm.nih.gov/6803467/) | 1982 | Clinical Study | Z Kardiol | Acute and chronic hemodynamic effects of dihydralazine in severe congestive heart failure both at rest and during exercise |
| [7209863](https://pubmed.ncbi.nlm.nih.gov/7209863/) | 1980 | Clinical Study | Therapie | Tolerance and complications of dihydralazine treatment in severe heart failure; early clinical safety characterization |
| [22534703](https://pubmed.ncbi.nlm.nih.gov/22534703/) | 2012 | Case Report | Med Sci Monit | Management of NYHA class III/IV heart failure (LVEF 13%) during pregnancy; dihydralazine considered as part of multi-drug regimen in a life-threatening cardiac situation |
| [8497771](https://pubmed.ncbi.nlm.nih.gov/8497771/) | 1993 | Review | Schweiz Med Wochenschr | Review of hypertensive crisis management; discusses hemodynamic mechanisms and lists dihydralazine among available agents with notes on endothelial damage pathophysiology |
| [1695297](https://pubmed.ncbi.nlm.nih.gov/1695297/) | 1990 | Animal Study | J Cardiovasc Pharmacol | Hemodynamic comparison of isradipine vs dihydralazine in atherosclerotic and normal rabbits; dihydralazine produced arteriolar vasodilation but with less favorable organ perfusion profile than calcium antagonist |
| [15201535](https://pubmed.ncbi.nlm.nih.gov/15201535/) | 2004 | Cohort | J Hypertension | Plasma volume and hemodynamic disturbances in hypertensive pregnancy; provides physiological context for dihydralazine's afterload-targeting mechanism in cardiovascular disease states |

---

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug interactions) was returned from the standard sources. Please refer to the package insert for safety information.

> **Literature-derived safety signals worth flagging before any further use:**
>
> - **Drug-induced autoimmune hepatitis**: Dihydralazine is metabolized by CYP1A2, and multiple case series and mechanistic studies (PMID [2347920](https://pubmed.ncbi.nlm.nih.gov/2347920/), PMID [1513326](https://pubmed.ncbi.nlm.nih.gov/1513326/), PMID [9241657](https://pubmed.ncbi.nlm.nih.gov/9241657/)) have documented dihydralazine-induced hepatitis characterized by anti-CYP1A2 (anti-liver microsomal) autoantibodies. This is a rare but potentially serious idiosyncratic reaction requiring hepatic monitoring.
> - **Acetylator phenotype dependency**: Dihydralazine is acetylated by hepatic N-acetyltransferase (NAT2); slow acetylators may have higher plasma levels and elevated risk of drug-induced lupus-like syndrome — a known class effect of hydrazinophthalazines.
> - **Pregnancy context**: Multiple studies used dihydralazine in hypertensive emergencies of pregnancy, but a 2018 network meta-analysis (PMID 29974489) suggests newer agents (labetalol, nifedipine) may have more favorable profiles.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for heart disease reflects a known pharmacological history, not a new repurposing opportunity. Dihydralazine was clinically evaluated for heart failure in the 1980s and was superseded by ACE inhibitors and beta-blockers due to tachyphylaxis and the lack of neurohormonal benefits. The only active clinical trial uses dihydralazine as a combination partner in a highly specific post-TAVI fibrosis setting, making it impossible to derive independent efficacy conclusions. With zero India market registrations and no complete safety data on file, the current evidence base does not support advancing this candidate.

**To proceed, the following is needed:**

- Obtain complete MOA and safety data from DrugBank API and the EMA/ANSM (French) package insert for Nepressol
- Clarify whether the NCT05230901 trial can generate dihydralazine-specific efficacy and safety data via subgroup or secondary analysis
- Define a precise sub-indication (e.g., post-TAVI myocardial fibrosis, hypertensive heart disease with fibrotic remodeling) where dihydralazine's mechanism may offer benefit beyond current standard of care
- Assess NAT2 acetylator phenotype implications for patient stratification and safety risk management
- Review the full TFDA/India CDSCO database to confirm absence of any historical registration and evaluate regulatory pathway feasibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

