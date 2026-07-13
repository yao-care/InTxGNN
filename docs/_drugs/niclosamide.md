---
layout: default
title: Niclosamide
parent: 僅模型預測 (L5)
nav_order: 458
evidence_level: L5
indication_count: 10
---

# Niclosamide
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

# Niclosamide: From Anthelmintic (Tapeworm Infection) to Heart Disease

## One-Sentence Summary

Niclosamide is a WHO Essential Medicine and FDA-approved anthelmintic drug, classically used to treat intestinal tapeworm infections by disrupting parasitic mitochondrial oxidative phosphorylation.
The TxGNN model predicts it may be effective for **Heart Disease** with a score of **99.88%**,
with **3 registered clinical trials** (all withdrawn or terminated before enrollment, yielding zero usable data) and **15 publications** retrieved, several of which are animal and human-cell studies directly demonstrating cardioprotective effects.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Tapeworm infections (anthelmintic) |
| Predicted New Indication | Heart Disease |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Niclosamide is a salicylanilide anthelmintic whose classical mechanism kills intestinal cestodes by uncoupling mitochondrial oxidative phosphorylation, collapsing their proton gradient and starving them of ATP. Importantly, this mitochondrial-targeting property does not vanish in human tissues — research over the past decade has revealed that niclosamide also inhibits multiple intracellular signaling pathways that are central to cardiac pathophysiology, including Wnt/β-catenin, STAT3, mTOR/AMPK, and NF-κB.

Three specific mechanistic links to heart disease have been identified in the literature. First, niclosamide modulates **TMEM16A** (a calcium-activated chloride channel expressed in vascular smooth muscle and cardiac fibroblasts), affecting vascular tone and fibrotic remodeling — though the direction of effect appears context-dependent and warrants caution. Second, inhibition of **Wnt/β-catenin** reduces adverse cardiac remodeling, a pathway activated after myocardial injury. Third, **STAT3 inhibition** counters the neurohormonal activation that drives progressive heart failure. The most compelling preclinical evidence comes from PMID 34736968, which demonstrated that niclosamide directly attenuated pressure overload-induced heart failure in mice by enhancing cardiomyocyte mitochondrial respiration and ATP output. Separately, PMID 39515588 showed that niclosamide inhibited osteogenic calcification of **human** heart valvular interstitial cells via the AMPK/mTOR pathway, with direct relevance to calcific aortic valve disease.

Currently, detailed mechanistic data (MOA) from DrugBank is unavailable due to a data gap. Based on published literature, niclosamide's multi-pathway inhibitory profile provides a biologically plausible bridge from its anthelmintic origins to cardiac applications, but the absence of any completed clinical trial in cardiac indications means this prediction remains at an exploratory stage.

---

## Clinical Trial Evidence

> **Important context:** The three trials below were retrieved via a Niclosamide + heart disease search. None were specifically designed to treat cardiac indications — they targeted COVID-19 or inflammatory bowel disease. None enrolled patients or generated outcome data.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04542434](https://clinicaltrials.gov/study/NCT04542434) | Phase 2 | Withdrawn | 0 | Double-blind RCT for moderate COVID-19 with GI symptoms; withdrawn before any enrollment. No data available. Cardiac relevance is indirect via COVID-19 complications. |
| [NCT04372082](https://clinicaltrials.gov/study/NCT04372082) | Phase 3 | Withdrawn | 0 | Hydroxychloroquine + Diltiazem + Niclosamide combination for non-severe COVID-19 in patients with cardiovascular comorbidities; withdrawn before enrollment. No data available. |
| [NCT03521232](https://clinicaltrials.gov/study/NCT03521232) | Phase 1/2 | Terminated | 27 | Niclosamide enema (150 mg and 450 mg) for mild-to-moderate ulcerative proctitis; terminated early. Provides limited systemic safety and pharmacokinetic data, but no cardiac endpoints. |

---

## Literature Evidence

Listed in order of direct relevance to heart disease:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34736968](https://pubmed.ncbi.nlm.nih.gov/34736968/) | 2021 | Animal Study | Eur J Pharmacol | Niclosamide attenuated pressure overload-induced heart failure in mice; enhanced mitochondrial respiration and ATP production in cardiomyocytes — direct in vivo cardiac validation |
| [39515588](https://pubmed.ncbi.nlm.nih.gov/39515588/) | 2024 | Cell Study (Human-derived) | Biochem Pharmacol | Niclosamide inhibited calcification of **human** heart valvular interstitial cells via AMPK/mTOR pathway; directly relevant to calcific aortic valve disease |
| [38288981](https://pubmed.ncbi.nlm.nih.gov/38288981/) | 2024 | Nanoparticle/Animal Study | ACS Appl Mater Interfaces | Platelet membrane-encapsulated niclosamide nanoparticles activated STAT3/Bcl-2 to protect against myocardial infarction injury in mice; proof-of-concept for targeted cardiac delivery |
| [38814250](https://pubmed.ncbi.nlm.nih.gov/38814250/) | 2024 | Mechanistic/Cell Study | J Gen Physiol | Under physiological Ca²⁺ conditions, niclosamide **potentiates** (not inhibits) TMEM16A and induces vasoconstriction — a key safety signal requiring dose-response characterization |
| [39102426](https://pubmed.ncbi.nlm.nih.gov/39102426/) | 2024 | Mechanistic Study | PLoS Pathog | SARS-CoV-2 spike-induced senescent syncytia exacerbate heart failure; niclosamide may interrupt this pathway, linking its antiviral TMEM16 inhibition to cardiac benefit in post-COVID patients |
| [36684586](https://pubmed.ncbi.nlm.nih.gov/36684586/) | 2022 | Cell Study | Front Cardiovasc Med | Screening of >3,000 FDA/EMA drugs identified niclosamide as a top inhibitor of TMEM16F-mediated platelet procoagulant activity triggered by SARS-CoV-2 spike protein — relevant to COVID-associated thrombosis and cardiac injury |
| [33827113](https://pubmed.ncbi.nlm.nih.gov/33827113/) | 2021 | Cell Study | Nature | Niclosamide identified as the most effective TMEM16 inhibitor blocking SARS-CoV-2 spike-induced syncytia; connects antiviral mechanism to pulmonary and cardiac pathology |
| [41453737](https://pubmed.ncbi.nlm.nih.gov/41453737/) | 2025 | Mechanistic/Animal | Am J Transplant | TMEM16F-CLIC1 interaction mediates dendritic cell cross-decoration after heart transplantation in mice; niclosamide is implicated as a potential modulator of this rejection pathway |

---

## India Market Information

Niclosamide is **not currently marketed in India**. No drug licenses or registrations are on record with CDSCO. Any development for a new cardiac indication would require a full regulatory pathway from the ground up, including IND filing, local clinical trials, and new drug application submission.

---

## Safety Considerations

Safety package insert data (key warnings, contraindications) is not available in this evidence pack due to a data gap — the TFDA package insert has not yet been retrieved.

A clinically significant safety signal has emerged from the literature that is directly relevant to any cardiac application:

- **TMEM16A potentiation and vasoconstriction (PMID 38814250):** Under physiological calcium concentrations, niclosamide was found to *potentiate* rather than inhibit TMEM16A, leading to acute vasoconstriction. This off-target cardiovascular effect is opposite to what an antifibrotic/cardioprotective agent would ideally produce, and must be fully characterized before cardiac indication development proceeds.

Please also refer to the standard anthelmintic package insert for general warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the mechanistic case for niclosamide in heart disease is scientifically coherent — backed by direct animal and human cell data — no clinical trial has ever targeted a cardiac indication, all retrieved trials produced zero data, the drug is not marketed in India, and a potential vasoconstriction safety signal has been identified that directly conflicts with a cardioprotective profile.

**To proceed, the following is needed:**

- **MOA data gap closure:** Retrieve full DrugBank pharmacology entry (DB06803) to confirm primary cardiac molecular targets and off-target profile
- **Safety package insert:** Download and parse the TFDA/reference country package insert PDF to extract key warnings, contraindications, and hematological monitoring requirements
- **DDI database:** Resolve the missing DDI data file (`ddinter_code_A.csv`) and re-query for interactions with common cardiac co-medications (antihypertensives, anticoagulants, statins)
- **TMEM16A safety resolution:** Commission a dose-response study to define the concentration range at which niclosamide potentiates vs. inhibits TMEM16A, and determine whether therapeutic oral doses reach levels that cause vasoconstriction
- **Bioavailability assessment:** Niclosamide has notoriously poor systemic absorption via the oral route; cardiac applications will likely require novel formulations (nanoparticles, prodrugs, or IV) — a formulation strategy must be defined
- **Indication narrowing:** "Heart disease" is too broad for a development program. Based on available evidence, **calcific aortic valve disease** (PMID 39515588, human cell data) or **heart failure with preserved ejection fraction** (PMID 34736968, animal model) are the most tractable sub-indications to pursue first
- **Regulatory pathway mapping:** Since niclosamide is not registered in India, a full regulatory development plan (Phase 1 safety in Indian population → cardiac Phase 2) must be scoped before any go decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

