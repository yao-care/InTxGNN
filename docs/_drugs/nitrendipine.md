---
layout: default
title: Nitrendipine
parent: 僅模型預測 (L5)
nav_order: 492
evidence_level: L5
indication_count: 4
---

# Nitrendipine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Nitrendipine: From Hypertension to Migraine Disorder

## One-Sentence Summary

Nitrendipine is a second-generation dihydropyridine (DHP) calcium channel blocker (CCB) used in the treatment of mild to moderate hypertension. The TxGNN model predicts it may be effective for **migraine disorder** (top-ranked prediction, score 99.42%), with **0 clinical trials** and **3 publications** supporting this direction. This is a multi-indication evaluation: additional predictions include **pulmonary hypertension** (L3 evidence, Proceed with Guardrails) and **Prinzmetal angina** (L3 evidence, Proceed with Guardrails), both carrying substantially stronger mechanistic and clinical support.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mild to moderate hypertension |
| Predicted New Indication | Migraine Disorder (Rank #1 of 4 predicted) |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L4 (migraine disorder); L3 (pulmonary hypertension, Prinzmetal angina); L5 (migraine with brainstem aura) |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (migraine disorder) / Proceed with Guardrails (pulmonary hypertension, Prinzmetal angina) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available for nitrendipine (Data Gap DG002). Based on pharmacological target data and published literature, nitrendipine is a synthetic 1,4-dihydropyridine CCB with high vascular selectivity. It exerts its primary effects by blocking L-type voltage-gated calcium channels (Cav1.1–Cav1.4) in vascular smooth muscle cells, reducing transmembrane calcium influx and producing arterial vasodilation. Pharmacological binding data also confirms activity at KCa3.1 (intermediate-conductance calcium-activated potassium channel, KCNN4 gene), which may further contribute to vascular tone regulation. This mechanism forms the proven basis for its use in hypertension.

For **migraine disorder** (Rank #1), the prediction is mechanistically plausible because cortical spreading depression (CSD) — the neurophysiological correlate of migraine aura — depends critically on transient, excess transmembrane calcium influx, and intracranial vascular dysregulation is a core feature of migraine attacks. The CCB class has well-established precedents in this space: flunarizine (non-selective CCB) carries Level A guideline recommendation for migraine prophylaxis (IHS/EAN), and verapamil is standard of care for cluster headache prevention. However, nitrendipine's defining characteristic — high peripheral vascular selectivity — is precisely the property that raises uncertainty about migraine efficacy. Whether peripheral vasomodulation alone is sufficient to suppress CSD, without meaningful CNS penetration, remains unproven. The three available publications are limited to general DHP pharmacology reviews and a single abdominal migraine case report.

For **pulmonary hypertension** (Rank #3) and **Prinzmetal angina** (Rank #4), the mechanistic connection to nitrendipine's known pharmacology is far more direct and better evidenced. Pulmonary arterial smooth muscle contraction is highly L-type calcium channel-dependent; CCB blockade measurably reduces pulmonary vascular resistance (PVR) and right ventricular afterload, with multiple small human hemodynamic studies specifically using nitrendipine confirming this. Per 2022 ESC/ERS PAH guidelines, high-dose CCBs are first-line therapy for vasoreactive PAH patients. Variant (Prinzmetal) angina is caused by focal coronary arterial spasm driven by aberrant calcium-mediated smooth muscle contraction — DHP-CCBs are guideline-recommended first-line agents (2023 ESC Chronic Coronary Syndrome guidelines), and one direct Japanese clinical study (n=21) demonstrated significant reduction in nitrendipine-treated anginal attack frequency from 2.1 to 0.7 per day.

---

## Clinical Trial Evidence

### Migraine Disorder (Rank #1)

No clinical trials specifically investigating nitrendipine for migraine disorder are currently registered.

---

### Pulmonary Hypertension (Rank #3)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04330300](https://clinicaltrials.gov/study/NCT04330300) | Phase 4 | Suspended | 2,414 | COVID-19 ACEi/ARB investigation — **not relevant** to nitrendipine in PAH; trial suspended; classified as Grade C (database keyword mismatch on "pulmonary hypertension") |

> **Note:** The single retrieved trial is not directly applicable. No dedicated nitrendipine PAH trials are registered.

---

### Prinzmetal Angina (Rank #4)

No clinical trials specifically investigating nitrendipine for Prinzmetal/vasospastic angina are currently registered.

---

## Literature Evidence

### Migraine Disorder (Rank #1) — 3 Publications

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [9760558](https://pubmed.ncbi.nlm.nih.gov/9760558/) | 1998 | Case Series | Neurol Neurochir Pol | 35-year-old woman with abdominal migraine (nocturnal attacks with nausea, vomiting, transient loss of consciousness) — nitrendipine treatment noted; attacks resolved |
| [3319491](https://pubmed.ncbi.nlm.nih.gov/3319491/) | 1987 | Pharmacology Review | Drugs | Review of five second-generation DHP-CCBs including nitrendipine; documents greater vascular selectivity vs. nifedipine and discussion of wider clinical utility beyond hypertension |
| [15449971](https://pubmed.ncbi.nlm.nih.gov/15449971/) | 2004 | Review | Am J Cardiovasc Drugs | Grapefruit juice interactions with cardiovascular drugs including nitrendipine; irreversible CYP3A4 inactivation significantly increases oral bioavailability — relevant pharmacokinetic safety context |

---

### Pulmonary Hypertension (Rank #3) — Top 10 of 20 Publications

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [2013178](https://pubmed.ncbi.nlm.nih.gov/2013178/) | 1991 | Prospective Clinical Study | Clin Cardiol | 11 PAH patients with pulmonary fibrosis: sublingual nitrendipine 5 mg significantly reduced mean PAP from 32 to 29 mmHg at rest and from 55 to 49 mmHg during exercise |
| [2468866](https://pubmed.ncbi.nlm.nih.gov/2468866/) | 1988 | Acute Hemodynamic Study | J Cardiovasc Pharmacol | 10 PAH patients: sublingual nitrendipine reduced systemic BP, right atrial pressure, and improved cardiac output; some reduction in arterial oxygenation noted as a concern |
| [1339619](https://pubmed.ncbi.nlm.nih.gov/1339619/) | 1992 | Comparative Study | Chin J Tuberc Respir Dis | Nitrendipine IV (100 µg/kg) significantly lowered PAP in pigs with acute hypoxic PAH; effect comparable to captopril |
| [2937355](https://pubmed.ncbi.nlm.nih.gov/2937355/) | 1986 | Animal Study | Am Rev Respir Dis | Nitrendipine pretreatment in rats attenuated pulmonary vascular remodeling and right ventricular hypertrophy induced by 30-day intermittent hypobaric hypoxia |
| [7712585](https://pubmed.ncbi.nlm.nih.gov/7712585/) | 1994 | Animal Study | Chin J Tuberc Respir Dis | Nitrendipine and nifedipine both prevented chronic hypoxic PAH and right ventricular hypertrophy in rats; preventive effect comparable to L-arginine (NO precursor) |
| [8762482](https://pubmed.ncbi.nlm.nih.gov/8762482/) | 1995 | Animal Study | Chin J Tuberc Respir Dis | Nitrendipine IV significantly reduced PAP in pig hypoxic PAH model; study examined role of endothelin in PAH development alongside CCB treatment |
| [2468868](https://pubmed.ncbi.nlm.nih.gov/2468868/) | 1988 | Clinical Study | J Cardiovasc Pharmacol | 25 patients with angina + hypertension: nitrendipine 20 mg reduced aortic pressure, pulmonary wedge pressure, and ischemia burden; supports hemodynamic pleiotropic effects |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Review | Cardiovasc Drugs Ther | Comprehensive CCB review; states calcium antagonists are drugs of choice for pulmonary, coronary, cerebral, and mesenteric artery spasms — class framework for nitrendipine |
| [3049099](https://pubmed.ncbi.nlm.nih.gov/3049099/) | 1988 | Review | Eur Heart J | Mechanistic review confirming that CCBs act against all vasoconstrictor/spastic responses in pulmonary, cerebral, mesenteric, and renal arteries |
| [2693846](https://pubmed.ncbi.nlm.nih.gov/2693846/) | 1989 | Review | Magnesium | Pharmacological basis for CCB use; confirms nitrendipine's inhibition of Ca²⁺ entry into vascular smooth muscle as primary antihypertensive and vasodilatory mechanism |

---

### Prinzmetal Angina (Rank #4) — 5 Publications

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [1920816](https://pubmed.ncbi.nlm.nih.gov/1920816/) | 1991 | Clinical Study | Jpn Heart J | **Direct nitrendipine study:** single-blind, n=21 variant angina patients; anginal attack frequency reduced significantly from 2.1 ± 0.3 to 0.7 per day at 10–20 mg/day; Holter ECG improvements confirmed |
| [3345765](https://pubmed.ncbi.nlm.nih.gov/3345765/) | 1988 | Clinical Observation | Eur Heart J | Patient with Prinzmetal's angina showing intermittent ST elevation during exercise — characterises the coronary vasospasm mechanism directly targeted by DHP-CCBs |
| [14689111](https://pubmed.ncbi.nlm.nih.gov/14689111/) | 2003 | Review | Herz | Differential CCB therapy review; explicitly addresses DHP-CCB use in vasospastic angina; discusses endothelial function improvement and coronary protection |
| [7711361](https://pubmed.ncbi.nlm.nih.gov/7711361/) | 1995 | Drug Review | Drugs Aging | Review of nilvadipine; notes antihypertensive efficacy comparable to nitrendipine; discusses DHP class potential in cerebrovascular disease and angina |
| [2909138](https://pubmed.ncbi.nlm.nih.gov/2909138/) | 1989 | Clinical Study | Am J Cardiol | Felodipine (DHP-CCB class) significantly reduced hyperventilation-induced ischemic attacks in variant angina — class-level evidence supporting DHP mechanism in coronary vasospasm |

---

### Migraine with Brainstem Aura (Rank #2, L5)

No clinical trials or publications are available. Theoretical mechanistic consideration only: posterior circulation vasospasm in this rare migraine subtype may theoretically respond to CCB vasodilation, but vasodilators require caution in basilar-type migraine to avoid hemodynamic complications (blood-flow steal). **Decision: Hold.**

---

## India Market Information

Nitrendipine is **not currently marketed in India**. No CDSCO regulatory authorizations are on record, and no licensed products exist in the domestic market.

For reference, nitrendipine is available in select international markets under the following brand names: Bayotensin, Baypress, Bylotensin, Deiten, Nidrel, Nitrepin. These authorizations may serve as reference products for any future regulatory pathway in India.

---

## Safety Considerations

Formal warnings and contraindications data are not available for the India market (Data Gap DG001 — Blocking severity). Please refer to the approved package insert from a jurisdiction where nitrendipine is licensed (e.g., Germany, European reference market).

**Pharmacological Target Profile** (from pharmacology database — reflects known binding activity, not drug-drug interactions):

| Target | Gene | Species | Clinical Relevance |
|--------|------|---------|-------------------|
| Cav1.2 (L-type Ca²⁺, α1C) | — | Dog | Primary smooth muscle/cardiac target; basis of vasodilatory effect |
| Cav1.3 (L-type Ca²⁺, α1D) | CACNA1D | Human | Cardiac and neuronal L-type channel; relevant to CNS activity questions |
| Cav1.4 (L-type Ca²⁺, α1F) | CACNA1F | Human | Retinal L-type channel; monitor for visual effects |
| Cav1.1 (L-type Ca²⁺, α1S) | Cacna1s | Rat | Skeletal muscle channel; lower clinical relevance at therapeutic doses |
| KCa3.1 | KCNN4 | Human | Intermediate-conductance K⁺ channel; may modulate vascular smooth muscle tone |

**Drug Interactions:** No traditional drug-drug interaction data is available in the current evidence pack. CYP3A4 inhibition by grapefruit juice is documented to significantly increase nitrendipine bioavailability (PMID 15449971) — a relevant clinical consideration for dosing management.

---

## Conclusion and Next Steps

**Decision: Hold (migraine disorder) / Proceed with Guardrails (pulmonary hypertension, Prinzmetal angina)**

**Rationale:**

For **migraine disorder** (top TxGNN rank): Despite a high model score (99.42%), the available evidence is insufficient to support clinical development. Only one case report and two pharmacology reviews exist, with no dedicated clinical trials. Nitrendipine's high peripheral vascular selectivity and limited CNS penetration are unresolved concerns that distinguish it from guideline-supported CCBs in migraine prophylaxis (e.g., flunarizine, which has broader CNS activity). A Hold decision is appropriate until CNS pharmacokinetics and mechanistic studies are available.

For **pulmonary hypertension**: Multiple small prospective hemodynamic studies specifically in nitrendipine demonstrate measurable PAP reduction in PAH patients with pulmonary fibrosis, supported by animal model data on vascular remodeling prevention. Per 2022 ESC/ERS guidelines, high-dose CCBs are a validated first-line option in vasoreactive PAH — a patient-selection criterion that defines a clear, guardable pathway. Proceed with Guardrails.

For **Prinzmetal (vasospastic) angina**: One direct Japanese clinical study (n=21) demonstrated significant efficacy with nitrendipine 10–20 mg/day, and DHP-CCBs are guideline-recommended first-line agents for this indication. The primary gap is the absence of India regulatory approval. Proceed with Guardrails.

**To proceed, the following is needed:**

- **DG001 remediation (Blocking):** Download and parse the package insert from a jurisdiction where nitrendipine is approved (Germany or Japan) to obtain full warnings, contraindications, and precaution data
- **DG002 remediation (High):** Query DrugBank API for complete MOA data, particularly CNS penetration characteristics, to resolve the migraine indication uncertainty
- For **migraine disorder:** Commission a systematic review of all DHP-CCBs in migraine prophylaxis, with CNS penetration as a stratification variable; use nimodipine (CNS-penetrant DHP) as a mechanistic benchmark
- For **pulmonary hypertension:** Design patient eligibility criteria around acute vasoreactivity testing (per ESC/ERS 2022); confirm nitrendipine formulation availability in India or identify manufacturing pathway
- For **Prinzmetal angina:** Initiate CDSCO regulatory pathway assessment; evaluate feasibility of a bridging study using the existing Japanese clinical data (PMID 1920816) as the primary evidence anchor
- Comparative positioning analysis of nitrendipine vs. commonly available CCBs in India (amlodipine, diltiazem) to establish clinical differentiation and competitive rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

