---
layout: default
title: Ammonium Chloride
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 2
---

# Ammonium Chloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Ammonium Chloride: From Expectorant / Urinary Acidifier to Acute Laryngopharyngitis

## One-Sentence Summary

Ammonium chloride is a classic expectorant and urinary acidifying agent, traditionally used in cough remedies and to correct metabolic alkalosis.
The TxGNN model predicts it may be effective for **Acute Laryngopharyngitis**,
with **0 clinical trials** and **0 publications** currently supporting this direction — the prediction rests entirely on knowledge graph topology.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Expectorant; urinary acidifier; metabolic alkalosis correction |
| Predicted New Indication | Acute Laryngopharyngitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Ammonium chloride is a small inorganic salt that exerts its pharmacological effects primarily through **urinary and systemic acidification**. As an expectorant, it is believed to stimulate bronchial gland secretion via a gastric reflex mechanism, thereby increasing the water content of respiratory mucus and reducing its viscosity. This indirectly facilitates mucociliary clearance — the primary physical defense of the upper and lower airways.

Acute laryngopharyngitis is characterised by mucosal inflammation, oedema, and accumulation of viscous secretions in the larynx and pharynx. The theoretical mechanistic bridge is that ammonium chloride's ability to thin and mobilise respiratory secretions could relieve symptoms associated with mucosal congestion. Furthermore, as an acidifying agent, it may shift the local pH of pharyngeal secretions in a manner that transiently reduces inflammatory exudate viscosity.

However, it is important to note that the detailed mechanism of action (MOA) for this specific repurposing context is **not available in the current dataset**. The reasoning above is drawn from established pharmacological knowledge of ammonium chloride and represents a theoretical inference rather than a data-driven conclusion. The TxGNN high score (99.94%) most likely reflects proximity in the knowledge graph topology — i.e., shared nodes with respiratory or ENT disease clusters — rather than validated clinical efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

**Drug Interactions** (21 interactions identified; selected key interactions below):

| Interacting Drug | Severity | Clinical Note |
|-----------------|----------|---------------|
| Amphetamine | Moderate | Ammonium chloride acidifies urine, increasing renal excretion of amphetamine and reducing its efficacy/duration |
| Benzphetamine | Moderate | Same mechanism as amphetamine — urinary acidification accelerates elimination |
| Dextroamphetamine | Moderate | Clinically relevant: may reduce therapeutic effect of dextroamphetamine in ADHD management |
| Lisdexamfetamine | Moderate | Prodrug of dextroamphetamine; same interaction risk applies |
| Metamfetamine | Moderate | Enhanced urinary excretion of methamphetamine |
| Ephedrine | Minor | Urinary acidification may slightly increase ephedrine clearance |
| Pseudoephedrine | Minor | Similar to ephedrine; modest pharmacokinetic effect |
| Tricyclic antidepressants (Amitriptyline, Clomipramine, Desipramine, Doxepin, Imipramine, Nortriptyline, Protriptyline, Trimipramine) | Minor | Acidification may modestly alter TCA plasma levels |
| Methadone | Minor | Urinary acidification can increase methadone renal clearance |
| Mexiletine / Flecainide | Minor | Increased renal excretion of these antiarrhythmics under acidic urine conditions |

> **Note:** The pattern of interactions is mechanistically coherent — ammonium chloride acidifies urine (lowers urinary pH), which increases ionisation of basic drugs and promotes their renal elimination. Clinicians should be aware when co-administering with amphetamine-class compounds (Moderate risk).

> Key warnings and contraindications are not available in the current dataset. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is currently at evidence level L5 — the prediction is derived solely from TxGNN knowledge graph modelling, with zero supporting clinical trials and zero supporting publications. Additionally, ammonium chloride has no registered products in India (0 licenses), meaning there is no existing regulatory or commercial infrastructure to build upon. The theoretical mechanistic rationale is plausible but unverified.

**To proceed, the following is needed:**

- **Mechanism of action confirmation**: Retrieve full MOA data from DrugBank API (DG002 data gap) to establish a stronger mechanistic narrative
- **Regulatory baseline**: Obtain the drug's package insert warnings and contraindications from an authoritative source (DG001 data gap — currently Blocking for S1 safety evaluation)
- **Targeted literature search**: Conduct a manual PubMed/Embase search using broader MeSH terms (e.g., "ammonium chloride AND pharyngitis", "expectorant AND laryngopharyngitis") to identify any indirect or preclinical evidence
- **Preclinical feasibility review**: Assess whether any in vitro or animal model data supports anti-inflammatory or mucolytic effects in the laryngopharyngeal mucosa
- **Formulation pathway**: Identify suitable dosage forms (oral solution, lozenge, inhalation) appropriate for laryngopharyngeal delivery before any clinical hypothesis can be tested
- **Regulatory pathway in India**: Determine whether a new drug application would be required or whether ammonium chloride could be developed as an OTC expectorant under existing frameworks

> ⚠️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

