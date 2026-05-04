---
layout: default
title: Digoxin
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 6
---

# Digoxin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Digoxin: From Heart Failure / Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Digoxin is a classic cardiac glycoside with decades of clinical use, primarily indicated for heart failure and atrial fibrillation rate control.
The TxGNN model predicts it may be effective for **Prinzmetal Angina (variant angina)**,
however only **0 clinical trials** and **2 publications** currently exist to support this direction — neither of which directly validates therapeutic efficacy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Heart failure; Atrial fibrillation (rate control) |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacology, Digoxin is a cardiac glycoside that inhibits the Na⁺/K⁺-ATPase pump, increasing intracellular calcium and thereby producing positive inotropic effects. It also slows conduction through the AV node via vagal enhancement, making it useful in heart failure and atrial fibrillation rate control.

Prinzmetal angina (variant angina) is driven by focal coronary artery vasospasm rather than fixed atherosclerotic obstruction. The standard of care is calcium channel blockers and long-acting nitrates, which directly relax coronary smooth muscle. Digoxin does not have a known mechanism for relaxing coronary vasospasm. Conversely, by augmenting sympathetic tone indirectly, Digoxin may theoretically worsen coronary vasospasm, raising a potential contraindication concern rather than a therapeutic opportunity.

The TxGNN high score (0.998) most likely reflects topological similarity between cardiovascular disease nodes in the knowledge graph — shared network neighbors such as heart rate, myocardial oxygen demand, and vasomotor regulation — rather than a genuine biological efficacy signal for this specific indication. The mechanistic mismatch, combined with the complete absence of clinical trial evidence, means this prediction does not constitute a viable repurposing candidate at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9206110](https://pubmed.ncbi.nlm.nih.gov/9206110/) | 1996 | Mechanistic Review | *Chinese Medical Sciences Journal* | Study of 30 patients with angina decubitus; identified hemodynamic mechanisms (increased pulmonary artery diastolic pressure) underlying recumbent angina — does not evaluate Digoxin as treatment |
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | *Acta Physiologica et Pharmacologica Bulgarica* | Chronopharmacology review of antihypertensive therapies and circadian rhythms — no direct mention of Digoxin for Prinzmetal angina |

> ⚠️ Neither publication directly supports Digoxin as a therapeutic agent for Prinzmetal angina. Both are incidental literature captures from the knowledge graph search.

---

## India Market Information

Digoxin currently has **no registered products** in the India market (market status: Not Marketed). No license records are available.

---

## Safety Considerations

**Drug Interactions (304 known interactions identified; representative selection below):**

| Interacting Drug | Severity | Notes |
|-----------------|----------|-------|
| Acarbose | Moderate | |
| Metformin | Moderate | |
| Rabeprazole | Moderate | |
| Doxycycline | Moderate | |
| Tetracycline | Moderate | |
| Amphotericin B | Moderate | |
| Amphotericin B (lipid complex) | Moderate | |
| Hydrocortisone | Moderate | |
| Dexamethasone | Moderate | |
| Betamethasone | Moderate | |
| Triamcinolone | Moderate | |
| Cholecalciferol | Moderate | |
| Calcium Phosphate | Moderate | |
| Acetylsalicylic acid | Moderate | |
| Epinephrine | Moderate | |
| Bupropion | Moderate | |
| Hyoscyamine | Minor | |
| Atropine | Minor | |
| Glycopyrronium | Minor | |
| Albiglutide | Minor | |

> Digoxin has a **narrow therapeutic index**. With 304 known interactions on record, polypharmacy risk is a major safety concern. Full contraindication and black-box warning data are not available in this Evidence Pack; please refer to the official package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Digoxin's primary mechanism (Na⁺/K⁺-ATPase inhibition, positive inotropy, AV nodal slowing) is pharmacologically misaligned with the vasospasm-driven pathophysiology of Prinzmetal angina, and the available literature provides no supportive evidence — only 2 tangentially related publications and zero clinical trials exist. The possibility that Digoxin could worsen coronary vasospasm via sympathomimetic effects adds a potential safety concern. The TxGNN score reflects graph topology rather than a plausible biological signal.

**To proceed, the following would be needed:**
- Mechanistic evidence (MOA data from DrugBank or primary literature) demonstrating any plausible pathway by which Digoxin could reduce coronary vasospasm
- At least one hypothesis-generating preclinical or case-based study specifically linking Digoxin to Prinzmetal angina benefit
- Formal safety evaluation ruling out pro-spasm risk in vasospastic angina patients
- Package insert / TFDA label review to determine if Prinzmetal angina or coronary vasospasm is listed as a contraindication
- India (CDSCO) regulatory status review if future development is contemplated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

