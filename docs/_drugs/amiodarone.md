---
layout: default
title: Amiodarone
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 10
---

# Amiodarone
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

# Amiodarone: From Ventricular Arrhythmias to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Amiodarone is a broad-spectrum Class III antiarrhythmic drug with multi-channel blocking properties, clinically established for the treatment of life-threatening ventricular and supraventricular arrhythmias.
The TxGNN model predicts it may be effective for **Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)**,
with **0 clinical trials** and **10 publications** currently supporting this direction — the majority of which describe Amiodarone as a rescue agent rather than a dedicated CPVT therapy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ventricular arrhythmias / cardiac antiarrhythmic (Class III agent) |
| Predicted New Indication | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory database. Based on known pharmacological information, Amiodarone is a multi-channel antiarrhythmic agent that primarily prolongs the cardiac action potential by blocking K⁺ channels (IKr/IKs), while also demonstrating Na⁺ channel (use-dependent, Class I), Ca²⁺ channel (Class IV), and β-adrenergic receptor blocking (Class II) activity. This broad multi-channel profile makes it one of the most potent antiarrhythmic drugs available for suppressing reentrant circuits, abnormal automaticity, and triggered activity.

The mechanistic connection to CPVT is theoretically plausible: Amiodarone's β-adrenergic blocking activity can attenuate catecholamine-driven calcium overload, and its Na⁺/Ca²⁺ channel blockade can suppress the triggered activity that results from delayed afterdepolarisations (DADs). Both CPVT and the indications for which Amiodarone is currently used share the common feature of life-threatening ventricular arrhythmias provoked by adrenergic stress.

However, the core pathophysiology of CPVT — mutations in the RYR2 or CASQ2 genes causing abnormal spontaneous calcium release from the sarcoplasmic reticulum — cannot be directly corrected by Amiodarone. Unlike Flecainide, which binds directly to the RYR2 channel and suppresses pathological calcium leak at its source, Amiodarone acts downstream and non-specifically. The theoretical rationale is mechanistically reasonable but lacks the target specificity required for definitive CPVT treatment, which explains the absence of dedicated clinical trials.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Amiodarone in catecholaminergic polymorphic ventricular tachycardia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Narrative Review | Expert Opinion on Pharmacotherapy | Comprehensive review of pharmacological treatment for ventricular arrhythmias; Amiodarone highlighted as important for both acute conversion and chronic prevention, with context for its role across arrhythmia subtypes |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case Series | Pacing Clin Electrophysiol | 14-year-old boy with CPVT (CASQ2 mutation) developed ICD-induced arrhythmic storm; Flecainide successfully suppressed storming where other agents (including Amiodarone context) were insufficient — highlights mechanism gap |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Case Report | BMJ Case Reports | Young child in out-of-hospital cardiac arrest received 40 defibrillation shocks and multimodal pharmacotherapy including Amiodarone; eventually diagnosed with CPVT — illustrates Amiodarone as acute rescue agent |
| [17125720](https://pubmed.ncbi.nlm.nih.gov/17125720/) | 2006 | Case Report | Rev Española de Cardiología | CPVT patient with ICD-triggered arrhythmic storm; Amiodarone used in acute management of electrical storm, providing clinical context for its emergency role |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Case Report | Anesthesia & Analgesia | Neonate with long QT syndrome and refractory polymorphic VT managed with multimodal therapy including Amiodarone, esmolol and lidocaine plus ventricular pacing; demonstrates Amiodarone's role in neonatal refractory arrhythmia |
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Retrospective Cohort | Life (Basel) | Systematic review of CPVT patients in China — clinical characteristics, genetic basis (RYR2 vs. CASQ2), and arrhythmic outcomes; establishes disease profile and treatment landscape |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Registry/Database Study | Reviews Cardiovasc Med | Retrospective cohort of Chinese CPVT patients examining clinical characteristics, genetic basis, healthcare utilisation, and costs; provides real-world burden data |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case Report | Medicine | 9-year-old with RYR2 mutation (c.7580T>G) CPVT misdiagnosed for 6 years; highlights diagnostic delays and treatment challenges in paediatric CPVT |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Case Report | Turk Pediatri Arsivi | CPVT presenting as sudden cardiac arrest in a 2-year-old; detailed description of acute arrhythmia management and diagnosis in the absence of structural heart disease |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Case Report | Front Cardiovasc Med | Teenager with CPVT successfully managed by right cardiac sympathetic denervation after left denervation failure; illustrates the role of non-pharmacological escalation when medications are insufficient |

---

## India Market Information

Amiodarone currently has **no registered products in the India market** as captured in this dataset. No license records are available for review.

> Note: Amiodarone is a widely used antiarrhythmic agent globally (approved in the US, EU, and many Asian markets). The absence from this dataset may reflect a data coverage gap rather than regulatory unavailability. Independent verification against the CDSCO database is recommended.

---

## Safety Considerations

**Drug Interactions**: Amiodarone has an extensive drug interaction profile with **355 known interactions** documented. Clinically significant interactions include:

**Major interactions:**
- **Agalsidase beta** — Amiodarone may inhibit lysosomal enzyme activity, reducing efficacy of enzyme replacement therapy for Fabry disease
- **Hydrocortisone / Dexamethasone** — Combined use may increase cardiac risk; corticosteroid-induced electrolyte disturbances (hypokalaemia) can potentiate QT prolongation
- **Amphotericin B** (and all formulations: cholesteryl sulfate, lipid complex, liposomal) — Risk of additive hypokalaemia and QTc prolongation
- **Cisapride** — Severe combined QT prolongation risk; concurrent use generally contraindicated
- **Clarithromycin** — CYP3A4 inhibition increases Amiodarone plasma levels; combined QT prolongation risk
- **Clotrimazole** — Azole antifungal CYP interaction; QTc prolongation risk
- **Dolasetron** — 5-HT3 antagonist with QTc prolongation; additive cardiac risk
- **Eliglustat** — CYP2D6/3A4 interaction; Amiodarone is a CYP2D6 inhibitor, increasing Eliglustat exposure significantly

**Moderate interactions (selected):** Famotidine, Aprepitant, Bisacodyl, Budesonide (including nasal), Castor oil, Cimetidine

Please refer to the package insert for complete warnings, contraindications, and full safety information, including thyroid toxicity (hypo/hyperthyroidism), pulmonary toxicity, hepatotoxicity, and ocular effects.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for Amiodarone specifically in CPVT is limited to L4 (preclinical and case-report level), with no dedicated clinical trials and existing publications describing Amiodarone primarily as an acute rescue agent rather than a targeted CPVT therapy. Critically, Amiodarone does not address the core RYR2/CASQ2 calcium release defect, and more mechanism-specific agents (beta-blockers, Flecainide) are the current standard of care.

**To proceed, the following is needed:**
- Obtain CDSCO/TFDA package insert to fill critical data gaps: formal warnings, contraindications, and approved indications (currently blocking for safety screening)
- Retrieve detailed MOA from DrugBank API (DB01118) to complete mechanistic link analysis
- Conduct a structured literature search specifically comparing Amiodarone versus Flecainide and beta-blockers in CPVT to determine if any subpopulation (e.g., CASQ2 vs. RYR2 genotype, refractory to first-line therapy) may benefit
- Consider whether the more robustly supported indications in this report — **incessant infant ventricular tachycardia (L3, Proceed with Guardrails)** and **ventricular tachycardia (L1, Proceed with Guardrails)** — are prioritised for the India repurposing pathway before pursuing CPVT
- Assess Amiodarone's long-term toxicity profile (particularly thyroid and pulmonary effects) against the typically young/paediatric CPVT population to evaluate feasibility of chronic use

> ⚠️ **Research Disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

