---
layout: default
title: Nimodipine
parent: 僅模型預測 (L5)
nav_order: 393
evidence_level: L5
indication_count: 2
---

# Nimodipine
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

# Nimodipine: From Cerebral Vasospasm to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Nimodipine is a dihydropyridine-class L-type calcium channel blocker, approved internationally for the prevention of neurological deficits caused by cerebral vasospasm following subarachnoid hemorrhage.
The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**, with **0 clinical trials** and **0 publications** currently supporting this direction.
The entire evidence base rests on model prediction alone, and the mechanistic rationale remains highly speculative.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cerebral vasospasm / Subarachnoid hemorrhage (no India regulatory record available) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Nimodipine is a dihydropyridine calcium channel blocker with strong CNS selectivity. It blocks voltage-gated L-type calcium channels preferentially in cerebral vasculature, preventing calcium-mediated vasospasm after subarachnoid hemorrhage. Its high lipophilicity allows it to cross the blood-brain barrier, which distinguishes it from other dihydropyridines used primarily for cardiovascular indications.

Homozygous Familial Hypercholesterolemia (HoFH) is a rare, life-threatening genetic disorder caused by loss-of-function mutations in LDLR, APOB, PCSK9, or LDLRAP1 genes. These mutations severely impair hepatic LDL clearance, resulting in plasma LDL-C levels often exceeding 500 mg/dL and premature cardiovascular disease. Current treatments include LDL apheresis, lomitapide, evinacumab, and PCSK9 inhibitors—all directly targeting lipoprotein metabolism pathways.

The mechanistic bridge between Nimodipine and HoFH is theoretically tenuous. Intracellular calcium signaling has been proposed to modulate hepatic LDL receptor expression and cholesterol efflux in some preclinical models, but no direct experimental or clinical evidence links L-type calcium channel blockade to meaningful LDL reduction in HoFH. The TxGNN high score (99.29%) most likely reflects indirect graph connections between calcium channel biology and lipid metabolism nodes in the knowledge graph—not direct pharmacological evidence. This prediction requires strong preclinical validation before any further consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

**Drug Interactions**: Nimodipine has 147 known interactions in the DDInter database. The following are the most clinically significant:

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Clarithromycin | **Major** | Strong CYP3A4 inhibitor — can markedly elevate nimodipine plasma concentrations, increasing hypotension risk |
| Dolasetron | **Major** | Potential additive QT-prolonging or cardiac effects |
| Aprepitant | Moderate | CYP3A4 inhibition may increase nimodipine exposure |
| Cimetidine | Moderate | H2 blocker may increase nimodipine bioavailability |
| Magnesium sulfate | Moderate | Additive hypotensive and neuromuscular blocking effects |
| Morphine | Moderate | Additive CNS/cardiovascular depression |
| Calcium salts (carbonate, chloride, phosphate, acetate) | Moderate | May pharmacodynamically antagonise calcium channel blockade |
| SGLT2 inhibitors (Canagliflozin, Dapagliflozin, Empagliflozin) | Moderate | Haemodynamic interaction; risk of hypotension |
| Miconazole | Moderate | Azole antifungal CYP3A4 inhibition |
| Bupropion | Moderate | CNS interaction; monitor for adverse effects |

> Formal package-insert warnings and contraindications were not available in this Evidence Pack. Please refer to the approved prescribing information (FDA label or equivalent) for complete safety guidance before any clinical evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is zero clinical or published literature evidence supporting Nimodipine for homozygous familial hypercholesterolemia. The prediction is L5 (model-only), the mechanistic hypothesis is speculative and biologically indirect, and Nimodipine is currently not marketed in India—adding regulatory and commercial barriers on top of the evidence gap.

**To proceed, the following is needed:**

- **MOA verification**: Retrieve full DrugBank entry and primary pharmacology literature to establish whether any calcium channel–LDL receptor interaction has been experimentally demonstrated
- **Label review**: Obtain and parse the FDA/EMA prescribing information to document formal warnings, contraindications, and special population restrictions
- **Preclinical signal search**: Conduct a targeted literature review for in vitro or animal studies linking dihydropyridine calcium channel blockers to LDL metabolism or LDLR upregulation
- **Graph audit**: Review the TxGNN knowledge graph edges that drive this score to determine whether the connection is biologically meaningful or an artefact of indirect path traversal
- **Secondary prediction review**: The second-ranked prediction (Nephrogenic Syndrome of Inappropriate Antidiuresis, score 99.05%) likewise has zero supporting evidence and an ultra-rare disease background; it should remain on Hold pending the same preclinical validation threshold
- **Revisit decision** only if a credible mechanistic hypothesis with at least one supporting in vitro experiment can be identified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

