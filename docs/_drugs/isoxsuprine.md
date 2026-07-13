---
layout: default
title: Isoxsuprine
parent: 僅模型預測 (L5)
nav_order: 327
evidence_level: L5
indication_count: 10
---

# Isoxsuprine
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

# Isoxsuprine: From Peripheral Vascular Disease to Benign Prostatic Hyperplasia

## One-Sentence Summary

Isoxsuprine is a β-sympathomimetic vasodilator historically used for peripheral vascular disorders and uterine relaxation (tocolysis), though no formal approved indications are recorded in the current dataset.
The TxGNN model predicts it may be effective for **Benign Prostatic Hyperplasia (BPH)**, with a near-perfect prediction score of 99.9999%.
However, **no clinical trials and no supporting literature** currently exist for this indication, placing this prediction at the lowest evidence tier (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in current dataset (historically: peripheral vascular disease, tocolysis) |
| Predicted New Indication | Benign Prostatic Hyperplasia (BPH) |
| TxGNN Prediction Score | 99.9999% |
| Evidence Level | L5 — Model prediction only, no actual studies |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available for Isoxsuprine in this dataset. Based on established pharmacological knowledge, Isoxsuprine is a β2-adrenergic agonist with secondary α-adrenergic blocking properties, producing vasodilation and uterine smooth muscle relaxation. It has historically been used for peripheral vascular insufficiency conditions (such as Raynaud's disease and arteriosclerosis obliterans) and as a tocolytic agent for preterm labor.

The theoretical link to BPH rests on the premise that β2-agonism can relax smooth muscle broadly — including potentially the prostatic stroma and bladder neck. However, BPH is pharmacologically managed primarily through **α1-adrenergic receptor blockade** (e.g., tamsulosin, alfuzosin) and 5-alpha reductase inhibition (e.g., finasteride). These are the validated receptor targets for reducing urinary outflow obstruction. Isoxsuprine's mechanism does not align with either of these established pathways.

The TxGNN model's exceptionally high score (0.99999) most likely reflects non-specific connectivity between **"smooth muscle"** and **"vascular"** nodes in the knowledge graph, rather than a disease-specific mechanistic pathway to BPH. This is a known limitation of graph-based prediction models: high topological proximity does not always translate to therapeutic relevance. Without clinical or preclinical evidence to validate this signal, the prediction should be treated with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Isoxsuprine in Benign Prostatic Hyperplasia.

---

## Literature Evidence

Currently no related literature available for Isoxsuprine in Benign Prostatic Hyperplasia.

---

## India Market Information

Isoxsuprine is currently **not marketed in India**. No product registrations or license records are available in the dataset.

---

## Safety Considerations

**Drug Interactions (20 moderate-level interactions identified):**

All identified interactions are classified as **Moderate** severity. Key interaction groups include:

- **SGLT2 Inhibitors** — Canagliflozin, Dapagliflozin, Empagliflozin, Ertugliflozin: Isoxsuprine's vasodilatory and sympathomimetic effects may compound cardiovascular and haemodynamic changes seen with SGLT2 inhibitors.
- **Prostacyclin Analogues / Pulmonary Vasodilators** — Epoprostenol, Iloprost, Selexipag, Treprostinil: Additive vasodilatory effects; risk of hypotension.
- **Phenothiazine Antihistamines** — Promethazine, Methdilazine, Thiethylperazine, Alimemazine: Possible additive CNS and cardiovascular effects.
- **Other Vasodilators** — Pentoxifylline, Minoxidil (topical): Additive hypotensive potential.
- **Other agents** — Amifostine, Brimonidine (ophthalmic and topical), Ozanimod, Procarbazine, Nitrous acid: Moderate interactions requiring monitoring.

> **Additional safety note (from evidence for "respiratory failure" indication):** Published literature documents that β-mimetic agents in the Isoxsuprine class can induce **pulmonary oedema**, particularly at tocolytic doses (PMID [6726706](https://pubmed.ncbi.nlm.nih.gov/6726706/)). This is a known class-effect adverse event and is relevant to systemic or high-dose administration.

Please refer to the package insert for full warnings and contraindications, as formal prescribing information was not available in the current dataset.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score for BPH is extremely high numerically, but is unsupported by any clinical trials, observational studies, or published literature. The mechanistic rationale is weak — Isoxsuprine's β2-agonism does not align with the established α1-adrenergic and 5-alpha reductase pharmacology of BPH treatment. Furthermore, the drug is not currently marketed in India, and full safety documentation (warnings, contraindications) is unavailable. Proceeding without foundational evidence would not meet minimum repurposing evaluation standards.

**To proceed, the following is needed:**

- **MOA documentation**: Retrieve complete mechanism of action from DrugBank API (DB08941) to confirm receptor targets and pharmacodynamic profile.
- **Safety package**: Download and parse the full prescribing information / package insert (from relevant regulatory source) to identify contraindications and key warnings before any clinical consideration.
- **Preclinical evidence search**: Conduct a broader literature search for any in vitro or in vivo studies of Isoxsuprine or β2-agonists in prostate smooth muscle, urodynamics, or BPH models.
- **Comparator context**: Evaluate whether any β-agonist class drug has demonstrated benefit in BPH to determine if this is a class effect worth investigating.
- **Regulatory pathway assessment**: Determine whether Isoxsuprine can be registered in India and what pathway (new indication NDA, off-label guidance) would apply if evidence were to emerge.

> ⚠️ *This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require formal clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

