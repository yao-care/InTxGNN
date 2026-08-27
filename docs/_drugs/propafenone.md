---
layout: default
title: Propafenone
parent: 僅模型預測 (L5)
nav_order: 505
evidence_level: L5
indication_count: 8
---

# Propafenone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Propafenone: From Antiarrhythmic Therapy to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Propafenone is a Class Ic antiarrhythmic (sodium-channel blocker) historically used to treat cardiac arrhythmias, though this Evidence Pack does not contain a confirmed original-indication label. Among eight TxGNN-predicted indications, the most credible signal is **Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)**, supported by **9 mechanistic/observational publications** (no clinical trials yet registered) showing that propafenone directly inhibits the cardiac ryanodine receptor (RyR2) responsible for CPVT's arrhythmogenic calcium leak. Note that TxGNN's single *highest*-scoring prediction — manic bipolar affective disorder — is **not** used as the headline result, because the underlying literature shows the opposite causal direction (propafenone *causing* mania as an adverse effect, not treating it); this is explained in detail below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in dataset (Propafenone is a Class Ic antiarrhythmic/sodium-channel blocker; original indication data is a documented gap — see DG001/DG002) |
| Predicted New Indication | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) |
| TxGNN Prediction Score | 99.79% (global rank #4,266) |
| Evidence Level | L3 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on the top-ranked TxGNN signal:** The single highest-scoring prediction in this pack (manic bipolar affective disorder, 99.80%, rank #4,206) is deliberately **not** presented as the headline finding. See the section below for why.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for propafenone is currently a documented data gap (DG002). Based on information embedded in the supporting literature itself, propafenone is a **Class Ic antiarrhythmic** that blocks cardiac sodium channels; it is chemically related to bupropion and shares structural features with flecainide, another Class Ic agent.

The mechanistic case for CPVT is unusually strong for a model prediction because it does not rely solely on the drug's primary sodium-channel action. Multiple in-vitro mechanistic studies in this pack (PMID 26121139, 21270101, 21798265) demonstrate that propafenone — like flecainide — also directly inhibits the **ryanodine receptor 2 (RyR2)** channel on the sarcoplasmic reticulum, reducing diastolic Ca²⁺ leak ("Ca²⁺ waves"). This is the exact molecular defect underlying CPVT, which is caused by gain-of-function RyR2 mutations that produce delayed afterdepolarizations and triggered ventricular arrhythmia. A 35-year case report (PMID 30820400) documents durable clinical benefit from propafenone in a CPVT patient, consistent with this proposed secondary, RyR2-mediated mechanism.

This is a case where a **non-canonical, secondary pharmacological action** (RyR2 inhibition), rather than the drug's approved primary mechanism, plausibly explains the TxGNN association — a pattern worth flagging explicitly to reviewers rather than treating the prediction score alone as sufficient justification.

**Why the top-ranked prediction (manic bipolar affective disorder) is excluded:** The three supporting publications (PMID 2579063, 11949740, 32124390) are **adverse-event case reports and a drug-interaction review**, describing propafenone-*induced* mania/organic psychosis — not evidence that propafenone treats mania. There is no known pharmacological mechanism by which a cardiac sodium-channel blocker would exert mood-stabilizing or antimanic effects. This is a textbook example of a knowledge-graph **causality-direction confound**, where "drug and disease co-occur in adverse-event literature" is misread by the model as a treatment relationship. It is retained in the raw data for transparency but should not be advanced past preliminary screening.

| PMID | Year | Type | Journal | Why It Does *Not* Support Repurposing |
|------|------|------|---------|----------------------------------------|
| [2579063](https://pubmed.ncbi.nlm.nih.gov/2579063/) | 1985 | Case Report (Adverse Effect) | J Clin Psychiatry | Mania *caused by* propafenone administration |
| [11949740](https://pubmed.ncbi.nlm.nih.gov/11949740/) | 2001 | Case Report (Adverse Effect) | Int J Psychiatry Med | Organic psychosis from a venlafaxine–propafenone interaction |
| [32124390](https://pubmed.ncbi.nlm.nih.gov/32124390/) | 2020 | Review | Pharmacol Rep | Reviews harmful antipsychotic–cardiovascular drug interactions, not efficacy |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for CPVT (or for any of the eight predicted indications in this pack).

---

## Literature Evidence

*(For CPVT — the recommended primary candidate)*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Systematic Review | Life (Basel) | Clinical characteristics, genetics, and arrhythmic outcomes of CPVT patients from China |
| [39564160](https://pubmed.ncbi.nlm.nih.gov/39564160/) | 2024 | Cohort | Ann Pediatr Cardiol | 10+ year follow-up of long-term clinical course in CPVT patients |
| [23965883](https://pubmed.ncbi.nlm.nih.gov/23965883/) | 2013 | Cohort | Zhongguo Dang Dai Er Ke Za Zhi | Long-term outcomes and predictors of ventricular arrhythmia in CPVT |
| [26121139](https://pubmed.ncbi.nlm.nih.gov/26121139/) | 2015 | In Vitro Mechanistic | PLoS ONE | RyR2 channel activity determines potency/efficacy of flecainide and R-propafenone against arrhythmogenic Ca²⁺ waves |
| [21270101](https://pubmed.ncbi.nlm.nih.gov/21270101/) | 2011 | In Vitro Mechanistic | Circ Arrhythm Electrophysiol | RyR2 inhibition determines efficacy of Class I antiarrhythmics (incl. propafenone) in CPVT |
| [21798265](https://pubmed.ncbi.nlm.nih.gov/21798265/) | 2011 | In Vitro Mechanistic | J Mol Cell Cardiol | Efficacy/potency of Class I antiarrhythmics for suppressing Ca²⁺ waves in calsequestrin-deficient myocytes |
| [36082968](https://pubmed.ncbi.nlm.nih.gov/36082968/) | 2023 | Genetic/Mechanistic Study | Clin Exp Pharmacol Physiol | Characterizes a gain-of-function RyR2 mutation (R1760W) underlying CPVT |
| [30820400](https://pubmed.ncbi.nlm.nih.gov/30820400/) | 2019 | Case Report | HeartRhythm Case Rep | 35-year effective treatment of CPVT with propafenone |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case Report | Medicine | Delayed CPVT diagnosis (RYR2 c.7580T>G) in a 9-year-old child |

---

## Other Predicted Indications (Preliminary Screening — Not Yet Actionable)

The remaining six predictions in this pack have no clinical trial or literature evidence and are supported only by mechanistic reasoning (Evidence Level L5, decision stage S0, recommendation Hold). Listed for completeness only:

| Rank | Disease | TxGNN Score | Mechanistic Plausibility |
|------|---------|-------------|---------------------------|
| 3 | Periodic paralysis with transient compartment-like syndrome | 99.67% | Weak — analogy to mexiletine's use in Nav1.4-related periodic paralysis; no direct evidence |
| 4 | Prinzmetal angina | 99.45% | Weak — pathology is coronary vasospasm; propafenone has no known antispasmodic action and carries proarrhythmic risk in ischemic disease |
| 5 | Incessant infant ventricular tachycardia | 99.44% | Moderate — Class Ic agents have off-label pediatric use for refractory VT, but no supporting data here |
| 6 | Arrhythmogenic right ventricular cardiomyopathy | 99.42% | Moderate — consistent with clinical practice of using Class Ic agents adjunctively in ARVC, but unsupported in this pack |
| 7 | Nephrogenic syndrome of inappropriate antidiuresis | 99.23% | Very weak — driven by AVPR2 signaling, unrelated to cardiac sodium-channel pharmacology; likely embedding-space artifact |
| 8 | Trichotillomania | 99.17% | Very weak — no plausible mechanistic overlap; likely prediction noise |

---

## India Market Information

Propafenone currently has **no registered marketing authorization in India** (0 registrations; market status: Not Marketed). No dosage form, brand, or approved-indication data is available for this drug in the dataset.

---

## Safety Considerations

**Drug Interactions:** DrugBank/DDInter records **190 total interactions** for propafenone. Within the subset returned, two are flagged **Major**:
- **Dolasetron** (Major)
- **Eliglustat** (Major)

The remaining sampled interactions are predominantly **Moderate**, including several 5-HT3 antagonists and GI-motility/QT-interval-relevant agents (Famotidine, Cimetidine, Clarithromycin, Ondansetron, Palonosetron, Lorcaserin, Bupropion, Aprepitant, Levofloxacin, and several laxative/bowel-prep agents), with one **Minor** interaction (Metronidazole). Given propafenone's own QT/conduction effects, interactions with other QT-prolonging or CYP2D6/CYP3A4-modulating agents warrant particular attention.

Key warnings and contraindications are not available in this dataset (blocked pending TFDA/label data acquisition — see Conclusion).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (specific to CPVT; all other predicted indications remain at Hold)

**Rationale:**
CPVT is supported by a coherent mechanistic thread (RyR2 channel inhibition), a long-duration case report of clinical benefit, and multiple independent in-vitro/cohort studies (Evidence Level L3) — a materially stronger evidentiary basis than the model's top-ranked but causality-inverted "manic bipolar affective disorder" signal, which should be disregarded. However, a **Blocking** data gap (DG001 — missing official label warnings/contraindications) currently prevents this candidate from completing even the S1 safety pre-screen, so "Proceed with Guardrails" is conditional on resolving that gap before any further evaluation.

**To proceed, the following is needed:**
- Official product label (warnings, contraindications) — currently blocking (DG001)
- Confirmed original indication and detailed mechanism-of-action data (DG002)
- Prospective or registry-based clinical evidence specifically in CPVT (no trials currently registered)
- Formal reassessment of the "manic bipolar affective disorder" TxGNN signal as a known false-positive pattern (reverse-causality/adverse-event confound), to avoid downstream misinterpretation
- India market/regulatory pathway assessment, given the drug currently has zero registrations in-country
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

