---
layout: default
title: Lacosamide
parent: 僅模型預測 (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
---

# Lacosamide
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

# Lacosamide: From Focal Epilepsy to Manic Bipolar Affective Disorder

## One-Sentence Summary

Lacosamide (brand name Vimpat®) is a third-generation antiepileptic drug (AED) approved in multiple countries for the treatment of focal (partial onset) seizures in adults and adolescents.
The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**, with **1 clinical trial** and **14 publications** currently supporting this direction.
The mechanistic rationale is plausible — Lacosamide shares neuronal membrane-stabilising properties with established mood stabilisers such as Lamotrigine and Valproate — though the clinical evidence base remains early-stage and requires cautious interpretation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Focal (partial onset) epilepsy / partial seizures |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L2 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available from the Evidence Pack. Based on information extracted from the supporting literature, Lacosamide exerts its primary pharmacological effect through **selective enhancement of the slow inactivation of voltage-gated sodium (Nav) channels** — in particular Nav1.3, Nav1.7, and Nav1.1 — thereby prolonging the inactivated state and reducing repetitive high-frequency neuronal firing. A secondary mechanism involves binding to **Collapsin Response Mediator Protein 2 (CRMP-2)**, which regulates microtubule dynamics, ion channel trafficking, and synaptic plasticity. Taken together, these actions stabilise neuronal membrane excitability in a sustained, state-dependent manner (PMID 28845834).

This mechanism closely parallels that of other anticonvulsants already used as first- and second-line mood stabilisers in bipolar disorder. Lamotrigine (also a Nav channel blocker) and Valproate (an HDAC inhibitor / sodium channel modulator) are both guideline-recommended for bipolar maintenance. If Lacosamide achieves comparable membrane stabilisation with a potentially more favourable tolerability profile, there is a mechanistically coherent rationale for its mood-stabilising potential. Notably, the CRMP-2 pathway may also modulate hippocampal neuroplasticity and emotional regulation circuits — an additional biological link to affective disorders.

One important caveat: the only registered clinical trial (NCT07412132) targets the **depressive phase** of bipolar disorder rather than the **manic phase**. The TxGNN-predicted label is "manic bipolar affective disorder," creating a partial indication mismatch. The mechanistic argument for the depressive pole (Nav channel suppression reducing cortical hyperexcitability) is stronger in the existing literature. Any translation effort must carefully distinguish between bipolar subtypes and episode polarity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT07412132](https://clinicaltrials.gov/study/NCT07412132) | Phase 3 | Recruiting | 40 | Double-blind RCT evaluating Lacosamide as augmentation to first- or second-line treatment in moderate-to-severe **major depressive episodes** of Bipolar I and II. Initiated January 2026; results expected 2027. Note: the trial targets the depressive pole, not the manic pole — indication sub-type alignment should be confirmed. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [30251375](https://pubmed.ncbi.nlm.nih.gov/30251375/) | 2018 | Retrospective Cohort | Psychiatry and Clinical Neurosciences | Lacosamide vs. other anticonvulsants over 30 days in hospitalised patients with bipolar disorder without comorbid epilepsy — first controlled-design study directly in BD. |
| [33666402](https://pubmed.ncbi.nlm.nih.gov/33666402/) | 2021 | Open-label Pilot Trial | Journal of Clinical Psychopharmacology | 12-week pilot trial evaluating efficacy and safety of Lacosamide for bipolar depression; provides preliminary tolerability and response data. |
| [32693579](https://pubmed.ncbi.nlm.nih.gov/32693579/) | 2020 | Review | ACS Chemical Neuroscience | Reviews CRMP-2 as a druggable target for neurodegenerative and neuropsychiatric diseases; discusses Lacosamide's CRMP-2 binding as a secondary mechanism relevant to mood circuits. |
| [29957667](https://pubmed.ncbi.nlm.nih.gov/29957667/) | 2018 | Review | Therapeutic Drug Monitoring | Updated review of TDM for all 27 licensed AEDs; explicitly notes that several AEDs including Lacosamide are used off-label for pain and bipolar disorder, supporting broad psychiatric utility. |
| [28845834](https://pubmed.ncbi.nlm.nih.gov/28845834/) | 2017 | Case Report | Acta Bio-Medica | Case of clinical mood stabilisation with Lacosamide in a patient with comorbid mood disorder, PTSD, and fronto-temporal epilepsy; describes Nav channel slow-inactivation as the mechanistic basis. |
| [30275630](https://pubmed.ncbi.nlm.nih.gov/30275630/) | 2018 | Case Report / Safety Signal | Indian Journal of Psychological Medicine | Reports Lacosamide-precipitated neutropenia in a patient with bipolar disorder and comorbid epilepsy — important safety signal for haematological monitoring when used in psychiatric populations. |
| [29253680](https://pubmed.ncbi.nlm.nih.gov/29253680/) | 2018 | Prospective Multicenter Study | Epilepsy & Behavior | Prospective study of Lacosamide's effect on depression and anxiety symptoms in focal epilepsy patients; found improvements in mood outcomes, suggesting an intrinsic mood-modifying effect beyond seizure control. |
| [38304661](https://pubmed.ncbi.nlm.nih.gov/38304661/) | 2024 | Case Report | Cureus | Complex case of a pregnant patient with Bipolar I, comorbid epilepsy, and PNES; Lacosamide featured as part of the polypharmacy management — highlights real-world use and safety complexity in vulnerable populations. |

---

## India Market Information

Lacosamide is currently **not registered or marketed in India**. No approved license records are available.

> ⚠️ This means there is no approved product label, no locally reviewed safety data, and no established supply chain in India. Any clinical development or access programme would need to begin from regulatory submission.

---

## Safety Considerations

Detailed safety data (package insert warnings, contraindications, drug interaction profiles) was not retrievable for this report.

One safety signal identified from the literature is worth noting:

- **Haematological toxicity**: A case of Lacosamide-precipitated **neutropenia** has been reported in a patient with bipolar disorder and comorbid epilepsy ([PMID 30275630](https://pubmed.ncbi.nlm.nih.gov/30275630/)). This warrants baseline and periodic monitoring of full blood counts if Lacosamide is used in psychiatric populations.

For complete safety information — including cardiac conduction effects (PR interval prolongation, known from AED class), teratogenicity risk, and CYP2C19 interaction potential — please refer to the current Vimpat® package insert or equivalent regulatory product information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A Phase 3 RCT is actively recruiting (NCT07412132), and a retrospective cohort study plus an open-label pilot trial provide initial supportive signals. The mechanistic link via Nav channel stabilisation is biologically coherent and analogous to approved mood stabilisers. However, the evidence base is still early-stage, the trial targets the depressive rather than the manic pole, and the drug is not marketed in India — all of which constrain immediate clinical translation.

**To proceed, the following is needed:**

- **Confirm indication sub-type**: Clarify whether the target is manic episodes, depressive episodes, or bipolar maintenance — the current trial (NCT07412132) addresses depressive episodes only, which does not perfectly align with the TxGNN-predicted label of "manic bipolar."
- **Obtain complete safety data**: Retrieve and review the full Vimpat® package insert (SmPC / USPI) to document cardiac conduction warnings, teratogenicity, contraindications, and drug interaction profile — currently all marked as data gaps.
- **Regulatory pathway assessment**: Since Lacosamide has zero India registrations, determine whether a new drug application or a research import licence would be required before any India-based trial could proceed.
- **Monitor NCT07412132**: Track results of the ongoing Phase 3 trial (completion expected 2027); positive results would upgrade evidence to L1 and materially strengthen the repurposing case.
- **Haematological monitoring plan**: Given the neutropenia signal (PMID 30275630), establish a CBC monitoring protocol as part of any clinical use protocol.
- **Dose optimisation research**: The effective dose in psychiatric indications (vs. 200–400 mg/day for epilepsy) has not been established; dose-finding studies may be required.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

