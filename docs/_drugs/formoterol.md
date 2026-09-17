---
layout: default
title: Formoterol
parent: Model Prediction Only (L5)
nav_order: 374
evidence_level: L5
indication_count: 6
---

# Formoterol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Formoterol: From Long-Acting Bronchodilation to Confirmed Use in Bronchitis, Obstructive Lung Disease, and Asthma

## One-Sentence Summary

Formoterol (DrugBank DB00983) is a long-acting β2-adrenergic agonist (LABA) whose original indication data was not provided in this evidence pack, though it is clinically well known as a bronchodilator for obstructive airway disease. The TxGNN model returned **six** candidate indications for this drug; three are well supported by real clinical evidence (**Bronchitis/COPD**, **Obstructive Lung Disease**, **Asthma** — each with **L1 evidence** and dozens of Phase 3 RCTs), while the other three (Respiratory Malformation, Rienhoff Syndrome, Asthma-Susceptibility Trait) have little or no supporting evidence and are flagged in this pack itself as likely knowledge-graph label noise. Overall: **strong signal for airway-obstruction indications, no signal for structural/genetic disease labels.**

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in dataset (Formoterol is an established long-acting β2-agonist bronchodilator) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Predicted Indications Screened | 6 |
| Highest TxGNN Score | Respiratory malformation — 99.92% (flagged as data noise, no supporting evidence) |
| Most Clinically Credible Predictions | Bronchitis (chronic/COPD), Obstructive Lung Disease, Asthma — all L1 evidence |
| Overall Recommended Decision | **Proceed with Guardrails** (bronchitis/COPD, obstructive lung disease, asthma) — **Hold** (respiratory malformation, Rienhoff syndrome, asthma-susceptibility trait) |

### All Predicted Indications at a Glance

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------------|-----------------|------------------|-----------------|
| 1 | Respiratory malformation | 99.92% | L4 | S0 | Hold |
| 2 | Bronchitis (chronic bronchitis/COPD) | 99.92% | L1 | S2 | Proceed with Guardrails |
| 3 | Rienhoff syndrome | 99.90% | L5 | S0 | Hold |
| 4 | Obstructive lung disease | 99.90% | L1 | S3 | Proceed with Guardrails |
| 5 | Asthma | 99.74% | L1 | S3 | Proceed with Guardrails |
| 6 | Asthma-related traits, susceptibility to | 99.50% | L5 | S0 | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on well-established pharmacology, Formoterol is a **long-acting β2-adrenergic receptor agonist (LABA)**. It activates β2 receptors on airway smooth muscle, raising intracellular cAMP and producing sustained bronchodilation (onset within minutes, duration ~12 hours).

This mechanism explains why three of the six TxGNN predictions are mechanistically sound: **Bronchitis (COPD phenotype)**, **Obstructive Lung Disease**, and **Asthma** are all conditions defined by reversible or partially reversible airflow limitation — exactly the physiological target of a LABA. This is corroborated by the evidence pack: dozens of completed Phase 3 RCTs (often as fixed-dose combinations with inhaled corticosteroids or LAMAs) already establish formoterol's efficacy and safety in these exact populations, which is why these three predictions reach evidence level **L1** and decision stage **S2–S3**.

The remaining three predictions are mechanistically implausible and are explicitly annotated as such in the source rationale:
- **Respiratory malformation** is a structural/congenital anomaly; a bronchodilator cannot correct anatomical defects. The clinical trials and literature returned for this label are actually asthma/COPD/Symbicort studies, indicating a knowledge-graph disease-label mismatch rather than a genuine signal.
- **Rienhoff syndrome** is a connective-tissue disorder linked to TGF-β signaling, with no known relationship to β2-adrenergic/cAMP pathways, and has zero supporting trials or literature.
- **Asthma-related traits, susceptibility to** describes genetic predisposition, not a treatable disease state — a bronchodilator addresses symptoms after onset, not underlying susceptibility, and again has zero supporting evidence.

---

## Detailed Evidence — Credible Indications

### 1. Bronchitis (Chronic Bronchitis / COPD Phenotype) — L1, Proceed with Guardrails

**Mechanistic note:** Strong physiological basis for chronic bronchitis/COPD; weaker for acute (typically viral) bronchitis without airflow obstruction — this distinction should not be blurred in labeling.

**Clinical Trial Evidence**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01462942](https://clinicaltrials.gov/study/NCT01462942) | Phase 3 | Completed | 2,443 | Aclidinium/formoterol fixed-dose combination vs. components/placebo in stable COPD; large confirmatory maintenance bronchodilator trial |
| [NCT01437397](https://clinicaltrials.gov/study/NCT01437397) | Phase 3 | Completed | 1,692 | Aclidinium bromide/formoterol fumarate fixed-dose combinations vs. monotherapies over 24 weeks in moderate-to-severe COPD |
| [NCT00064415](https://clinicaltrials.gov/study/NCT00064415) | Phase 3 | Completed | 799 | Open-label chronic safety study of arformoterol over 12 months in COPD |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Phase 3 | Completed | 741 | Multicenter RCT of (R,R)-formoterol (arformoterol) bronchodilator effect and safety in COPD |
| [NCT01572792](https://clinicaltrials.gov/study/NCT01572792) | Phase 3 | Completed | 921 | Long-term extension study of aclidinium/formoterol combinations in moderate-to-severe COPD |
| [NCT00250679](https://clinicaltrials.gov/study/NCT00250679) | Phase 3 | Completed | 443 | Long-term safety study of arformoterol tartrate inhalation solution BID in COPD |
| [NCT06571942](https://clinicaltrials.gov/study/NCT06571942) | Phase 4 | Recruiting | 128 | Ongoing triple inhaled therapy vs. COPD/chronic bronchitis without obstruction from biomass exposure |

**Literature Evidence**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27916620](https://pubmed.ncbi.nlm.nih.gov/27916620/) | 2017 | RCT | Chest | Efficacy/safety of glycopyrrolate/formoterol MDI (co-suspension technology) in COPD (PINNACLE-1/2) |
| [31920296](https://pubmed.ncbi.nlm.nih.gov/31920296/) | 2019 | RCT | Int J Chron Obstruct Pulmon Dis | Long-term safety/efficacy of budesonide/glycopyrronium/formoterol MDI in Japanese COPD patients |
| [28821260](https://pubmed.ncbi.nlm.nih.gov/28821260/) | 2017 | RCT | Respiratory Research | 24-hour bronchodilation and inspiratory capacity improvements with glycopyrrolate/formoterol in COPD |
| [37696312](https://pubmed.ncbi.nlm.nih.gov/37696312/) | 2023 | RCT | Respiratory Medicine | Tiotropium add-on to budesonide/formoterol in bronchiolitis obliterans post-HSCT |
| [20714376](https://pubmed.ncbi.nlm.nih.gov/20714376/) | 2010 | Review | Int J Chron Obstruct Pulmon Dis | Review of nebulized formoterol (Perforomist) clinical efficacy and safety in COPD |
| [31015757](https://pubmed.ncbi.nlm.nih.gov/31015757/) | 2019 | Meta-analysis | Int J Chron Obstruct Pulmon Dis | Comparative risks of budesonide/formoterol vs. placebo/monotherapy in stable COPD |
| [41654451](https://pubmed.ncbi.nlm.nih.gov/41654451/) | 2026 | Pharmacovigilance | Clinical Therapeutics | Real-world adverse event analysis of budesonide/formoterol using FAERS/JADER/CVAR databases |

---

### 2. Obstructive Lung Disease — L1, Proceed with Guardrails

**Clinical Trial Evidence**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04609878](https://clinicaltrials.gov/study/NCT04609878) | Phase 3 | Completed | 2,274 | Budesonide/glycopyrronium/formoterol vs. components/Symbicort in inadequately controlled asthma |
| [NCT02345161](https://clinicaltrials.gov/study/NCT02345161) | Phase 3 | Completed | 1,811 | FF/UMEC/VI once-daily triple therapy vs. budesonide/formoterol twice-daily in COPD |
| [NCT02676076](https://clinicaltrials.gov/study/NCT02676076) | Phase 3 | Completed | 1,153 | 52-week trial: extrafine beclometasone/formoterol/glycopyrronium vs. beclometasone/formoterol in uncontrolled asthma |
| [NCT01911364](https://clinicaltrials.gov/study/NCT01911364) | Phase 3 | Completed | 3,686 | 52-week trial of beclometasone+formoterol+glycopyrrolate vs. tiotropium combinations in severe COPD |
| [NCT00649025](https://clinicaltrials.gov/study/NCT00649025) | Phase 3 | Completed | 438 | Fluticasone/formoterol single-inhaler vs. fluticasone alone in moderate-to-severe asthma |
| [NCT01908140](https://clinicaltrials.gov/study/NCT01908140) | Phase 3 | Completed | 933 | Aclidinium/formoterol vs. salmeterol/fluticasone over 24 weeks in symptomatic COPD |

**Literature Evidence**

Currently no related literature available (PubMed query returned 0 results for this disease label).

---

### 3. Asthma — L1, Proceed with Guardrails

**Mechanistic/safety note:** Formoterol's β2-agonist mechanism is standard-of-care for asthma bronchodilation, but **LABA monotherapy carries a known class-level warning for increased asthma-related mortality risk** — it must be used in fixed combination with an inhaled corticosteroid (ICS), not alone. This is a critical guardrail for any repurposing pathway.

**Clinical Trial Evidence**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01444430](https://clinicaltrials.gov/study/NCT01444430) | Phase 3 | Completed | 12,460 | Large safety study evaluating serious asthma-related events: Symbicort (budesonide/formoterol) vs. ICS alone |
| [NCT04609878](https://clinicaltrials.gov/study/NCT04609878) | Phase 3 | Completed | 2,274 | Efficacy/safety of budesonide/glycopyrronium/formoterol in inadequately controlled asthma |
| [NCT03015259](https://clinicaltrials.gov/study/NCT03015259) | Phase 3 | Completed | 1,762 | Therapeutic equivalence of budesonide/formoterol inhaler vs. Symbicort reference in adult asthma |
| [NCT02676076](https://clinicaltrials.gov/study/NCT02676076) | Phase 3 | Completed | 1,153 | 52-week superiority trial of triple vs. dual formoterol-containing combination in uncontrolled asthma |
| [NCT00419952](https://clinicaltrials.gov/study/NCT00419952) | Phase 3 | Completed | 742 | 52-week safety comparison of Symbicort pMDI vs. budesonide alone in African American asthma patients |
| [NCT00649025](https://clinicaltrials.gov/study/NCT00649025) | Phase 3 | Completed | 438 | Fluticasone/formoterol vs. fluticasone alone over 12 weeks in moderate-to-severe asthma |
| [NCT05755906](https://clinicaltrials.gov/study/NCT05755906) | Phase 3 | Completed | 374 | Budesonide/formoterol MDI vs. budesonide MDI in inadequately controlled asthma (LITHOS) |
| [NCT01676987](https://clinicaltrials.gov/study/NCT01676987) | Phase 3 | Completed | 181 | Single-capsule budesonide-formoterol combination vs. budesonide alone in uncontrolled asthma |

**Literature Evidence**

Currently no related literature available (PubMed query returned 0 results for this disease label).

---

## Low-Confidence Predictions (Not Recommended to Pursue)

| Disease | Score | Evidence | Assessment |
|---|---|---|---|
| Respiratory malformation | 99.92% | L4, Hold | Trials/literature returned are actually asthma/COPD/Symbicort studies mismatched to this label; a bronchodilator cannot address structural anomalies. Judged as knowledge-graph label noise. |
| Rienhoff syndrome | 99.90% | L5, Hold | Zero trials, zero literature. Connective-tissue/TGF-β disorder with no known mechanistic link to β2-agonism. |
| Asthma-related traits, susceptibility to | 99.50% | L5, Hold | Zero trials, zero literature. Describes genetic predisposition, not a treatable disease state. |

---

## India Market Information

Formoterol is currently **not marketed** in this jurisdiction (0 registrations on file). No license records are available to summarize.

---

## Safety Considerations

**Drug Interactions:** A total of **462 interactions** were identified (drug-level, not indication-specific); representative examples from the dataset include:

- **Additive cardiovascular/sympathomimetic stimulation** — Ephedrine, Ephedrine (nasal), Diethylpropion, Isometheptene (all Moderate)
- **QT-prolongation risk** — Cisapride, Dolasetron (both Moderate)
- **CYP3A4 interaction** — Clarithromycin (Moderate), may increase systemic formoterol exposure
- **Antidiabetic agents** — Acarbose, Albiglutide, Alogliptin, Canagliflozin, Chlorpropamide, Dapagliflozin, Dulaglutide, Empagliflozin (all Moderate) — β2-agonists can antagonize glycemic control and mask hypoglycemia symptoms
- **Inhaled corticosteroids** — Beclomethasone, Betamethasone, Budesonide, Dexamethasone (all Minor) — reflect expected therapeutic co-administration rather than a hazard
- Famotidine (Moderate)

**Known class-level warning (from clinical literature, not the safety.key_warnings field):** LABA monotherapy in asthma is associated with increased risk of asthma-related death; formoterol should not be used as asthma monotherapy without a concomitant ICS.

Detailed TFDA-equivalent label warnings and contraindications are not available in this dataset (blocking data gap — see Conclusion).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Bronchitis/COPD, Obstructive Lung Disease, and Asthma only) — **Hold** on Respiratory Malformation, Rienhoff Syndrome, and Asthma-Susceptibility Trait.

**Rationale:**
- Three of six predicted indications are backed by dozens of completed Phase 3 RCTs with large enrollments and a clear, well-established mechanistic rationale (L1 evidence, S2–S3 decision stage) — these represent genuine, high-confidence repurposing/label-expansion signals rather than novel discoveries, since formoterol is already a recognized therapy in these disease areas globally.
- The remaining three indications lack any credible clinical or literature support and are explicitly flagged in the underlying evidence as likely knowledge-graph label noise or mechanistically implausible; pursuing them would not be justified.

**To proceed, the following is needed:**
- Official TFDA/local regulatory label (warnings, contraindications) — currently a **Blocking** data gap (DG001) preventing safety pre-screening (S1)
- Formal mechanism-of-action documentation from DrugBank (currently a **High**-severity data gap, DG002)
- Clarification of "bronchitis" sub-phenotype (chronic/COPD-associated vs. acute viral) before any labeling claim, to avoid indication over-generalization
- Confirmation of LABA/ICS combination requirement in any asthma-related regulatory submission, given the class-level mortality warning
- Local market entry assessment, since the drug currently holds zero registrations in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

