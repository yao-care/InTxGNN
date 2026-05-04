---
layout: default
title: Isosorbide Dinitrate
parent: 僅模型預測 (L5)
nav_order: 255
evidence_level: L5
indication_count: 10
---

# Isosorbide Dinitrate
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

# Isosorbide Dinitrate: From Angina Pectoris to Vascular Disease

## One-Sentence Summary

Isosorbide dinitrate (ISDN) is a well-established organic nitrate used globally for over 60 years to treat angina pectoris and heart failure, but currently not registered in India.
The TxGNN model predicts it may be effective for **Vascular Disease** — encompassing coronary artery disease, acute heart failure, and cerebral small vessel disease — with **multiple completed Phase 3 clinical trials** and **20 publications** supporting this direction.
With a TxGNN prediction score of **99.97%** and an evidence level of **L1**, this represents the strongest actionable repurposing signal in this analysis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Angina pectoris / Heart failure (globally established; no Indian registration on record) |
| Predicted New Indication | Vascular Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on prediction selection:** The TxGNN model's highest-ranked predictions by score (Ranks 1–5: alopecia-related conditions and pulmonary hypertension) carry L5 or L3 evidence levels and have no or limited clinical trial data. **Vascular Disease** (TxGNN model score rank 1,018) is selected as the primary repurposing focus because it has the strongest clinical evidence and the most actionable regulatory pathway for Indian market introduction.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, isosorbide dinitrate is an organic nitrate that acts as a prodrug for nitric oxide (NO). In vascular smooth muscle, NO activates guanylyl cyclase, raising cGMP levels and causing smooth muscle relaxation. This produces three complementary effects: (1) venous dilation that reduces cardiac preload, (2) arterial dilation that lowers afterload, and (3) direct coronary artery dilation that improves myocardial oxygen delivery. These actions explain ISDN's foundational role in managing ischemic and congestive cardiac conditions.

These mechanisms map directly onto the pathophysiology of multiple vascular disease subtypes. In coronary artery disease and angina, ISDN reduces myocardial oxygen demand while improving perfusion — an approach validated across decades of clinical trials. In acute decompensated heart failure, the combined preload and afterload reduction relieves pulmonary congestion and improves cardiac output. A newer and important repurposing direction is cerebral small vessel disease (lacunar stroke): NO-mediated endothelial protection may slow progressive ischemic injury in small cerebral arteries, a hypothesis now being tested in dedicated Phase 2/3 RCTs (LACI-2 programme). The secondary prediction of pulmonary hypertension (L3 evidence, 20 publications) also carries mechanistic plausibility — NO-mediated pulmonary vascular dilation can reduce pulmonary vascular resistance — though systemic hypotension risk limits selectivity.

Critically, ISDN is not currently registered in India despite a robust, decades-long international evidence base. India carries a significant burden of coronary artery disease, heart failure, and cerebrovascular disease — all conditions for which ISDN has documented clinical benefit. Introducing this drug represents a regulatory repurposing opportunity rather than a purely scientific one: the science is established globally, and the gap is market access.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00803634](https://clinicaltrials.gov/study/NCT00803634) | Phase 3 | Completed | 117 | PRONTO trial: IV ISDN as standard-of-care comparator against clevidipine for blood pressure control in acute heart failure with elevated BP — highest-grade direct ISDN evidence in this dataset |
| [NCT03451591](https://clinicaltrials.gov/study/NCT03451591) | Phase 2/3 | Completed | 363 | LACI-2: cilostazol + isosorbide mononitrate vs placebo for lacunar stroke and cerebral small vessel disease prevention — signals a new cerebrovascular repurposing direction for nitrates |
| [NCT02135315](https://clinicaltrials.gov/study/NCT02135315) | N/A | Completed | 1,500 | Intensive vs standard BP control in NSTE-ACS; ISDN included as part of standard care — large real-world outcome dataset supporting routine vascular disease use |
| [NCT02481323](https://clinicaltrials.gov/study/NCT02481323) | Phase 2 | Completed | 57 | Isosorbide mononitrate ± cilostazol for cerebral small vessel disease: safety, tolerability, and cognitive endpoint pilot — new repurposing signal with completed data |
| [NCT02228408](https://clinicaltrials.gov/study/NCT02228408) | Phase 4 | Completed | 17 | Hydralazine/ISDN combination vs placebo in hemodialysis-dependent ESRD: 26-week safety and cardiovascular effects — relevant to high-risk renal population |
| [NCT01513070](https://clinicaltrials.gov/study/NCT01513070) | Phase 4 | Completed | 120 | ISDN vs TCM formula (Quick-Acting Heart Reliever) in moderate coronary stenosis: 6-month anginal frequency, plaque assessment, and quality-of-life outcomes |
| [NCT02789033](https://clinicaltrials.gov/study/NCT02789033) | Phase 3 | Completed | 68 | Phase 3 RCT: topical ISDN spray + chitosan gel in diabetic foot ulcers — peripheral vascular disease application, demonstrates local vasodilation benefit |
| [NCT03072121](https://clinicaltrials.gov/study/NCT03072121) | Phase 4 | Unknown | 440 | Coronary artery disease not amenable to revascularization; ISDN as active comparator/combination component against Shexiang Baoxin Pill |
| [NCT04661709](https://clinicaltrials.gov/study/NCT04661709) | Phase 4 | Unknown | 502 | Unstable angina pectoris double-blind RCT; ISDN as standard-of-care comparator — large active-controlled evidence base |
| [NCT00000478](https://clinicaltrials.gov/study/NCT00000478) | Phase 3 | Completed | N/A | ACIP study: asymptomatic cardiac ischemia pilot — foundational Phase 3 trial establishing ISDN therapy methodology in silent ischemia |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [3325229](https://pubmed.ncbi.nlm.nih.gov/3325229/) | 1987 | Comparative RCT | Current Medical Research and Opinion | Multi-centre RCT (n=200 coronary patients): ISDN retard vs isosorbide-5-mononitrate — comparable reduction in weekly anginal attack frequency and rescue nitrate consumption |
| [1094819](https://pubmed.ncbi.nlm.nih.gov/1094819/) | 1975 | Placebo-controlled | American Heart Journal | Double-blind study: oral ISDN 10 mg significantly improved cardiac output at rest and during supine exercise in patients with ≥75% coronary stenosis vs placebo |
| [805037](https://pubmed.ncbi.nlm.nih.gov/805037/) | 1975 | Clinical Trial | Chest | Chewable ISDN 5 mg vs sublingual NTG during treadmill exercise in 20 patients with documented ischemic heart disease; complete angina relief achieved in all patients despite continued exertion |
| [36219567](https://pubmed.ncbi.nlm.nih.gov/36219567/) | 2023 | RCT | Stroke and Vascular Neurology | LACI-2 statistical analysis plan: isosorbide mononitrate for cerebral SVD — first rigorous RCT design targeting NO-mediated endothelial protection in lacunar stroke prevention |
| [29682995](https://pubmed.ncbi.nlm.nih.gov/29682995/) | 2018 | RCT | Diabetes & Vascular Disease Research | Double-blind RCT: topical ISDN spray + chitosan gel improved diabetic foot ulcer healing outcomes vs standard care alone — demonstrates peripheral vascular efficacy |
| [1576038](https://pubmed.ncbi.nlm.nih.gov/1576038/) | 1992 | Review | AACN Clinical Issues in Critical Care Nursing | Comprehensive 130-year review: nitrates for angina, infarct size limitation, intractable heart failure, cardiogenic shock, severe valve regurgitation, hypertensive episodes, and portal hypertension |
| [9951954](https://pubmed.ncbi.nlm.nih.gov/9951954/) | 1999 | Review | Drugs | Long-acting isosorbide mononitrate: 30-minute onset, up to 17-hour duration, antianginal efficacy comparable to conventional preparations — formulation strategy reference |
| [3925742](https://pubmed.ncbi.nlm.nih.gov/3925742/) | 1985 | Review | American Heart Journal | Nitrate tolerance: demonstrable within 24 hours, reversible within 21 hours of withdrawal, cross-tolerance with nitroglycerin — critical consideration for chronic dosing strategy |
| [1969017](https://pubmed.ncbi.nlm.nih.gov/1969017/) | 1990 | Clinical Study | Lancet | ISDN + prostaglandin E1 synergy in peripheral vascular disease: reduced platelet deposition and improved platelet survival time — mechanistic rationale for combination approaches |
| [30687454](https://pubmed.ncbi.nlm.nih.gov/30687454/) | 2018 | Experimental Study | Oxidative Medicine and Cellular Longevity | Endothelin receptor antagonist macitentan reversed ISDN-induced endothelial dysfunction and vascular oxidative stress in animals — relevant insight for long-term nitrate safety management |

---

## India Market Information

Isosorbide dinitrate currently has **no registered products in India**. This represents a significant market gap, given the drug's extensive international evidence base and the high prevalence of cardiovascular disease in the Indian population.

| Item | Status |
|------|---------|
| Market Status | ✗ Not Marketed |
| Total Registered Products | 0 |
| Available Dosage Forms | None on record |
| Approved Indications | None on record |

---

## Safety Considerations

**Drug-Drug Interactions (141 total interactions recorded):**

The following are the most clinically relevant interactions, particularly in the context of common comorbidities in Indian patients:

| Interacting Drug | Level | Clinical Relevance |
|------|------|------|
| Canagliflozin | Moderate | SGLT2 inhibitor — additive blood pressure lowering; monitor closely in diabetic patients |
| Dapagliflozin | Moderate | SGLT2 inhibitor — same class concern; important given high diabetes prevalence in India |
| Empagliflozin | Moderate | SGLT2 inhibitor — same class concern |
| Ertugliflozin | Moderate | SGLT2 inhibitor — same class concern |
| Morphine | Moderate | Additive vasodilation and hypotension; caution in acute coronary syndrome management |
| Bupropion | Moderate | Monitor blood pressure during concurrent use |
| Rosiglitazone | Moderate | Thiazolidinedione — additive blood pressure reduction |
| Sapropterin | Moderate | BH4 cofactor for nitric oxide synthase — potential amplification of NO effect |
| Dronabinol / Nabilone | Moderate | Cannabinoids — additive hypotension risk |
| Opium | Moderate | Opioid class — combined vasodilatory and CNS depressant concern |
| Omeprazole | Minor | Minimal clinical significance |

> Complete warnings, contraindications, and special population data were not available in this Evidence Pack. Please refer to the reference country package insert (e.g., EMA, US FDA, or UK MHRA labelling for isosorbide dinitrate) for full prescribing information before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Isosorbide dinitrate carries Level 1 clinical evidence across multiple vascular disease subtypes, including completed Phase 3 trials and 60+ years of global real-world use. India's high cardiovascular disease burden and the drug's complete absence from the Indian market create a strong case for formal introduction — provided the regulatory and safety data gaps identified below are resolved.

**To proceed, the following is needed:**

- **Safety documentation (blocking):** Obtain full package insert or SmPC from a reference regulatory authority (US FDA, EMA, or MHRA); warnings and contraindications are currently unavailable and constitute a blocking data gap
- **Mechanism of action confirmation:** Complete DrugBank API query for DB00883 to formally document MOA for regulatory submission
- **Regulatory pathway assessment:** Determine the appropriate Indian CDSCO pathway — new drug application, reference product approval, or abbreviated route — given the drug's established global status
- **DDI risk stratification:** Prioritize review of the 141 documented interactions, especially SGLT2 inhibitors (moderate-level interactions), given high co-prescription prevalence in Indian diabetic/cardiovascular patients
- **Nitrate tolerance management plan:** Establish eccentric dosing schedule (nitrate-free interval) to mitigate tolerance development during chronic use
- **Formulation decision:** Determine optimal dosage form (sublingual tablet, oral sustained-release, IV, or topical spray) aligned with target indication and Indian distribution infrastructure
- **Secondary indication monitoring:** Track emerging Phase 2/3 data for cerebral small vessel disease (LACI-2 programme) and pulmonary hypertension (L3 signal with 20 publications) for future label expansion opportunities
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

