---
layout: default
title: Nitroglycerin
parent: 僅模型預測 (L5)
nav_order: 495
evidence_level: L5
indication_count: 5
---

# Nitroglycerin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Nitroglycerin: From Angina Pectoris to Pulmonary Hypertension

## One-Sentence Summary

Nitroglycerin (glyceryl trinitrate) is one of the oldest and most established cardiovascular drugs, used for over a century as the frontline agent for acute relief of angina pectoris and coronary vasospasm.
The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, with **3 directly relevant completed clinical trials** and **20 publications** — including 2 published RCTs — currently supporting this direction.
The mechanistic rationale is direct and biologically well-founded: nitroglycerin's NO-donor activity targets the same NO-cGMP-PKG vasodilation pathway implicated in pulmonary vascular tone dysregulation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Angina pectoris (acute relief of coronary vasospasm and ischaemic chest pain) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L2 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Nitroglycerin is an organic nitrate that acts as an exogenous nitric oxide (NO) donor. It is metabolised by mitochondrial aldehyde dehydrogenase 2 (ALDH2) to release bioactive NO, which activates soluble guanylate cyclase (sGC). This triggers an increase in intracellular cyclic GMP (cGMP), which in turn activates protein kinase G (PKG), leading to vascular smooth muscle relaxation and vasodilation. In pulmonary hypertension, the central pathophysiology is excessive pulmonary vascular tone, elevated pulmonary vascular resistance (PVR), and increased mean pulmonary arterial pressure (mPAP) — precisely the haemodynamic targets of this mechanism.

The key translational insight is the delivery route. When administered via nebulisation or inhalation, nitroglycerin acts preferentially on the pulmonary circulation before systemic absorption occurs, maximising pulmonary vasoselectivity and minimising the systemic hypotension that limits intravenous use. This rationale mirrors that of inhaled nitric oxide (iNO), the established standard of care for pulmonary hypertensive crises — but nitroglycerin offers a substantially lower-cost, more widely accessible alternative that does not require specialised delivery equipment.

Both angina pectoris and pulmonary hypertension involve dysregulated vascular tone — one in the coronary circulation, the other in the pulmonary. The shared NO-cGMP-PKG signalling axis creates a direct mechanistic bridge. Clinical application of nebulised nitroglycerin in perioperative pulmonary hypertension is already embedded in cardiac surgery practice, particularly for children with congenital heart disease and pulmonary arterial hypertension. The TxGNN model's high prediction score (99.61%) reflects this convergence of mechanism, disease biology, and existing clinical precedent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT07214129](https://clinicaltrials.gov/study/NCT07214129) | N/A | Completed | 20 | Directly assessed safety and vasoreactive efficacy of nebulised nitroglycerin in pulmonary arterial hypertension (PAH); provides acute haemodynamic and safety data per 6th World PH Symposium criteria |
| [NCT05741229](https://clinicaltrials.gov/study/NCT05741229) | N/A | Completed | 80 | Evaluated nebulised nitroglycerin as adjuvant therapy for persistent pulmonary hypertension of the newborn (PPHN); assessed echocardiographic parameters (biventricular function, PA pressure) and clinical outcomes — results published as PMID 40888971 (2025 RCT) |
| [NCT04594629](https://clinicaltrials.gov/study/NCT04594629) | Phase 1 | Unknown | 120 | Head-to-head comparison of nebulised nitroglycerin (2.5–5 µg/kg/min) vs nebulised PGI2 (epoprostenol) for perioperative pulmonary hypertension management in valve replacement surgery; largest sample in this category |
| [NCT03259165](https://clinicaltrials.gov/study/NCT03259165) | Phase 2 | Terminated | 52 | N-FURIOUS pilot trial: nitroglycerin vs furosemide for acute pulmonary oedema in the emergency department using lung ultrasound-guided therapy; termination reason requires investigation |
| [NCT00449059](https://clinicaltrials.gov/study/NCT00449059) | Phase 4 | Completed | 20 | Evaluated acute effect of nitroglycerin infusion on blood pressure and heart rate in cardiac transplant recipients with cyclosporine-induced hypertension; provides post-transplant haemodynamic data in a high-risk population |
| [NCT01120964](https://clinicaltrials.gov/study/NCT01120964) | Phase 1/2 | Completed | 22 | Randomised placebo-controlled trial of IV L-citrulline (NO precursor) vs placebo in children undergoing cardiopulmonary bypass; evaluated NO-pathway pharmacokinetics relevant to pulmonary hypertension dosing design in paediatric cardiac surgery |
| [NCT06107465](https://clinicaltrials.gov/study/NCT06107465) | Phase 2/3 | Unknown | 60 | RCT comparing low-dose (<100 µg/min) vs high-dose (>100 µg/min) nitroglycerin for sympathetic crashing acute pulmonary oedema in the ED; evaluates time to resolution of hypertension, hypoxia, and need for mechanical ventilation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [40888971](https://pubmed.ncbi.nlm.nih.gov/40888971/) | 2025 | RCT | European Journal of Pediatrics | Nebulised nitroglycerin as adjuvant therapy for PPHN (n=80 full-term neonates, randomised); significant improvement in echocardiographic parameters and oxygen saturation index compared to control |
| [29880427](https://pubmed.ncbi.nlm.nih.gov/29880427/) | 2018 | RCT | Journal of Cardiothoracic and Vascular Anesthesia | Dobutamine + nitroglycerin vs milrinone for perioperative pulmonary hypertension in mitral valve replacement; compared haemodynamic outcomes in young patients with severe PH |
| [39549131](https://pubmed.ncbi.nlm.nih.gov/39549131/) | 2024 | Network Meta-Analysis | Clinical Drug Investigation | Network meta-analysis of vasodilator therapies (including NTG) for PH in patients undergoing mitral valve replacement surgery; positions nitroglycerin within the comparative efficacy landscape |
| [34082850](https://pubmed.ncbi.nlm.nih.gov/34082850/) | 2021 | Clinical Review | Cardiology in the Young | Comprehensive review of inhaled nitroglycerin for acute PAH in children with congenital heart disease; discusses evidence, dosing, and safety relative to iNO |
| [16707530](https://pubmed.ncbi.nlm.nih.gov/16707530/) | 2006 | Clinical Study | British Journal of Anaesthesia | Acute effects of inhaled nitroglycerin on pulmonary and systemic haemodynamics in children with PAH and congenital heart disease; demonstrated selective reduction in pulmonary arterial pressure |
| [6407380](https://pubmed.ncbi.nlm.nih.gov/6407380/) | 1983 | Clinical Haemodynamic Study | Annals of Internal Medicine | Nitroglycerin administered to 9 patients with chronic pulmonary hypertension; cardiac index increased 40%, stroke volume increased 40%, PVR decreased 40%, and mean PAP decreased — foundational haemodynamic evidence |
| [6423015](https://pubmed.ncbi.nlm.nih.gov/6423015/) | 1984 | Clinical Study | Bulletin Européen de Physiopathologie Respiratoire | Sublingual NTG (1 mg) vs ISDN in 27 COPD patients with PH undergoing right heart catheterisation; NTG uniquely reduced pulmonary vascular resistance without worsening oxygenation |
| [31250045](https://pubmed.ncbi.nlm.nih.gov/31250045/) | 2019 | Clinical Study | European Journal of Clinical Pharmacology | ALDH2 gene polymorphism significantly influences nitroglycerin pharmacokinetics and vasodilatory efficacy in infants with congenital heart disease and PAH — important for dosing in Asian populations |
| [29096811](https://pubmed.ncbi.nlm.nih.gov/29096811/) | 2017 | Review | Journal of the American College of Cardiology | Comprehensive review of NTG and nitrogen oxides in cardiovascular therapeutics; covers vasodilation, NO biology, haemodynamic effects, tolerance, and non-haemodynamic properties |
| [39799613](https://pubmed.ncbi.nlm.nih.gov/39799613/) | 2025 | Review | American Journal of Emergency Medicine | Updated emergency medicine review of sympathetic crashing acute pulmonary oedema (SCAPE); positions high-dose nitroglycerin as a key intervention, with practical dosing guidance |

---

## India Market Information

Nitroglycerin (DB00727) currently has **no registered products** in the India drug approval database. No authorisation records, dosage forms, or approved indications are on file.

> **Note:** This reflects the absence of regulatory registration data in the current dataset and does not necessarily indicate unavailability through other channels (e.g., hospital formulary procurement or generic import). Verification with CDSCO directly is recommended before concluding on actual market access.

---

## Safety Considerations

Detailed package insert warnings and contraindications are not available in the current dataset. The following information is drawn from the drug interaction database.

**Drug Interactions (228 interactions on record; key moderate-level interactions listed):**

| Interacting Drug | Interaction Level | Clinical Note |
|-----------------|-------------------|---------------|
| Morphine | Moderate | Additive hypotensive effect; monitor blood pressure when co-administered in acute settings |
| Bupropion | Moderate | May potentiate hypotension; use with caution |
| Canagliflozin | Moderate | SGLT2 inhibitors may increase risk of hypotension with nitroglycerin |
| Dapagliflozin | Moderate | Same class risk as Canagliflozin; volume depletion compounds vasodilatory effects |
| Empagliflozin | Moderate | Same class risk; haemodynamic monitoring recommended |
| Dronabinol | Moderate | Cannabinoids may enhance hypotensive effects |
| Nabilone | Moderate | Same mechanism as Dronabinol |
| Rosiglitazone | Moderate | Thiazolidinediones may enhance fluid retention and augment hypotensive risk |
| Sapropterin | Moderate | BH4 cofactor for NO synthesis; additive vasodilatory potential |

Minor interactions are noted with multiple anticholinergic agents (Hyoscyamine, Atropine, Glycopyrronium, Scopolamine, Trospium, Mepenzolate, Methscopolamine, Propantheline, Dicyclomine) — these reduce nitroglycerin's mucosal absorption and therapeutic response.

> **Important:** Full contraindication data (e.g., concomitant PDE5 inhibitors such as sildenafil, severe anaemia, closed-angle glaucoma, hypertrophic obstructive cardiomyopathy) are not included in the current dataset. Please refer to the package insert and current prescribing information before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two published randomised controlled trials (PMID 40888971, PMID 29880427), multiple completed Phase 1–4 clinical trials, and over two decades of haemodynamic studies collectively establish that nebulised or inhaled nitroglycerin exerts clinically meaningful pulmonary vasodilation in paediatric congenital heart disease, persistent pulmonary hypertension of the newborn, and perioperative pulmonary hypertension in valve surgery. The mechanism (NO → sGC → cGMP → PKG → smooth muscle relaxation) is direct and biologically well-founded. However, evidence in adults with idiopathic or group 1 PAH remains limited, tolerance development (nitrate tolerance) with sustained use is a known liability, and the drug is currently not registered in India — meaning regulatory and pharmacovigilance infrastructure must be established before formalised use.

**To proceed, the following is needed:**

- **Mechanism of action data (MOA):** Retrieve full DrugBank entry for DB00727 to confirm pharmacological classification, target proteins, and bioavailability parameters
- **India regulatory pathway assessment:** CDSCO registration status and import/compassionate use pathways for nitroglycerin formulations (especially nebulised or inhalation-grade)
- **Package insert safety review:** Download and parse TFDA/CDSCO or US FDA label to extract formal contraindications, warnings, and special population restrictions (pregnancy, renal/hepatic impairment)
- **Nitrate tolerance mitigation plan:** Any sustained-use protocol for pulmonary hypertension must incorporate nitrate-free intervals or combination with hydralazine to prevent tolerance attenuation
- **PDE5 inhibitor co-prescription review:** Absolute contraindication with sildenafil/tadalafil/vardenafil must be flagged in any clinical protocol, as these are first-line PH agents
- **Paediatric vs adult subgroup stratification:** Current evidence is heavily paediatric (PPHN, CHD); a dedicated adult PAH cohort study or Phase 2 trial is needed to confirm efficacy in the primary adult indication
- **ALDH2 pharmacogenomics consideration:** The 2019 study (PMID 31250045) shows ALDH2 polymorphism — prevalent in East and South Asian populations — significantly modifies nitroglycerin response; genotyping guidance should be incorporated into any India-context protocol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

