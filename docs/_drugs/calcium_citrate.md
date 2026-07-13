---
layout: default
title: Calcium Citrate
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 10
---

# Calcium Citrate
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

# Calcium Citrate: From Calcium Supplementation to Hemoglobinopathy

## One-Sentence Summary

Calcium citrate (DB11093) is a widely used calcium salt supplement, primarily administered to address calcium deficiency and support bone health, though no formally approved indication appears in the current regulatory data.
The TxGNN model predicts it may be effective for **Hemoglobinopathy**,
with a high prediction score of **99.37%** — however, **no clinical trials and no published literature** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Calcium supplementation (no formally approved indication on record) |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for calcium citrate in this dataset. Based on known pharmacology, calcium citrate is an oral calcium salt that provides bioavailable calcium ions (Ca²⁺), which participates in a broad range of physiological processes including muscle contraction, intracellular signalling, enzymatic reactions, and haemostasis.

The mechanistic link proposed by the TxGNN model centres on the role of calcium in regulating the **Gardos channel (KCNN4)** — a calcium-activated potassium channel critical to red blood cell (RBC) volume regulation. In sickle cell disease (a major subtype of hemoglobinopathy), elevated intracellular Ca²⁺ activates the Gardos channel, leading to RBC dehydration and increased sickle haemoglobin polymerisation. However, the therapeutic direction is **paradoxical**: effective treatment requires *reducing* intracellular calcium (calcium channel blockade), not supplementing it. Calcium citrate, by providing exogenous Ca²⁺, would theoretically act in the opposite direction.

The high TxGNN score most likely reflects non-specific knowledge graph connections between calcium metabolism and RBC biology rather than a genuine therapeutic hypothesis. Multiple hops in the knowledge graph (e.g., calcium → erythrocyte metabolism → haemoglobin structure) may have inflated the score without capturing the direction of the mechanistic relationship. Given the absence of any supporting clinical or preclinical evidence, and a plausible counter-argument against the mechanism, this prediction warrants caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Calcium citrate in hemoglobinopathy.

---

## Literature Evidence

Currently no related literature available for Calcium citrate in hemoglobinopathy.

---

## India Market Information

Calcium citrate is currently **not marketed in India**. No product registrations or licenses are on record for this compound.

---

## Safety Considerations

**Drug Interactions (84 interactions identified):**

Calcium citrate has a clinically significant drug interaction profile. Key interactions include:

| Severity | Interacting Drugs | Clinical Concern |
|----------|------------------|-----------------|
| **Major** | Dolutegravir, Bictegravir | Calcium chelation reduces absorption of integrase inhibitors; co-administration not recommended or requires strict timing separation |
| **Moderate** | Alendronic acid, Risedronic acid, Ibandronate | Calcium impairs bisphosphonate absorption; administer at least 2 hours apart |
| **Moderate** | Doxycycline, Tetracycline | Calcium forms insoluble complexes with tetracyclines, reducing antibiotic efficacy |
| **Moderate** | Baloxavir marboxil | Divalent cations reduce antiviral absorption |
| **Moderate** | Amlodipine, Nifedipine, Diltiazem | Calcium may antagonise calcium channel blocker pharmacodynamics |
| **Moderate** | Acebutolol, Atenolol, Bisoprolol, Betaxolol, Carvedilol | Reduced beta-blocker absorption via calcium chelation |
| **Moderate** | Hydrochlorothiazide, Chlorothiazide | Thiazide diuretics reduce urinary calcium excretion; co-administration may increase hypercalcaemia risk |
| **Moderate** | Calcipotriol (topical), Calcitriol (topical) | Additive vitamin D analogue effects may increase systemic calcium load |

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high score (99.37%) to hemoglobinopathy, but the proposed mechanism is pharmacologically inconsistent — calcium supplementation acts in the *opposite* direction to established therapeutic strategies for sickle cell disease (which require intracellular calcium reduction). There is zero supporting clinical trial or literature evidence, placing this firmly at evidence level L5.

**To proceed, the following would be needed:**

- Preclinical (in vitro / in vivo) studies specifically evaluating oral calcium citrate in haemoglobinopathy models, with attention to intracellular vs. extracellular calcium dynamics
- Clarification of whether TxGNN's prediction reflects a specific disease subtype where calcium supplementation may address secondary complications (e.g., bone loss in thalassaemia) rather than primary disease modification
- Detailed MOA documentation from DrugBank to verify whether any indirect pathway supports this indication
- Review of the package insert (formal label) for approved indications, contraindications, and warnings — not yet available in this dataset (Data Gap DG001)
- Epidemiological signal review: given published concerns about oral calcium supplements increasing cardiovascular risk (Bolland et al., BMJ 2010/2011), the safety profile for long-term use in this population should be evaluated before any further development step
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

