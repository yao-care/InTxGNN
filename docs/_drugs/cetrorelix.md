---
layout: default
title: Cetrorelix
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
---

# Cetrorelix
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

# Cetrorelix: From Controlled Ovarian Stimulation to Hypertrichosis

## One-Sentence Summary

Cetrorelix (Cetrotide®) is a synthetic peptide GnRH antagonist, internationally approved for inhibiting premature LH surges in women undergoing controlled ovarian stimulation as part of assisted reproductive therapy.
The TxGNN model predicts it may be effective for **Hypertrichosis**, with **0 clinical trials** and **0 publications** currently supporting this direction — the prediction rests entirely on model inference.
Given the weak mechanistic rationale and absence of any supporting evidence, this candidate requires significant scrutiny before further investment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Controlled ovarian stimulation (fertility treatment) — inhibition of premature LH surges |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data (MOA) is not available in this Evidence Pack. However, based on pharmacological profiling from the drug interaction database, Cetrorelix is a **competitive GnRH receptor antagonist** — it binds directly to the pituitary GnRH1 receptor (encoded by *GNRHR*, Entrez Gene ID 2798) and competitively blocks endogenous GnRH. The downstream consequence is a rapid, dose-dependent suppression of LH and FSH release, which in turn reduces gonadal androgen and estrogen production.

The theoretical link to hypertrichosis runs through this anti-androgenic cascade: GnRH antagonism → ↓ pituitary LH/FSH → ↓ gonadal androgen secretion → potential reduction of androgen-driven hair follicle stimulation. This pathway is mechanistically plausible only for **androgenic hypertrichosis** — a minority subtype where excess androgens drive abnormal hair growth (overlapping with hirsutism).

However, a critical distinction must be noted. **Hypertrichosis is not equivalent to hirsutism.** True hypertrichosis — particularly the generalised or congenital forms — is typically **androgen-independent**, arising from genetic mutations, drug side-effects, or paraneoplastic processes rather than HPG axis dysregulation. The TxGNN model likely exploits hair-biology nodes in the knowledge graph to make this connection, but the mechanistic bridge is weak for the disease entity as defined. The overall mechanistic rationale is therefore narrow and applies only to a specific androgenic subtype, not to hypertrichosis broadly.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Cetrorelix has no registered products in India. No license records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note from pharmacology data:** Cetrorelix acts as a ligand at the GnRH1 receptor (GNRHR). Its primary pharmacological effect — suppression of the hypothalamic-pituitary-gonadal (HPG) axis — should be considered in any new indication assessment, particularly in paediatric, pregnant, or hypogonadal populations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model yields a high confidence score (99.98%), but this reflects the model's graph-based inference rather than real-world evidence. There are zero clinical trials, zero publications, and no India regulatory presence. More critically, the mechanistic link between GnRH antagonism and hypertrichosis is valid only for a narrow androgenic subtype; the majority of hypertrichosis cases are androgen-independent and would not respond to this mechanism.

**To proceed, the following is needed:**

- **Subtype clarification:** Confirm whether the target population is androgenic hypertrichosis (e.g., associated with PCOS or adrenal androgen excess) rather than non-androgenic forms — only the former has any mechanistic basis.
- **MOA documentation:** Retrieve full DrugBank MOA entry for Cetrorelix to confirm secondary targets or off-target effects that could explain non-androgenic hair biology effects.
- **Safety package:** Obtain the CDSCO/international prescribing information to assess key warnings and contraindications before any indication expansion.
- **Benchmark comparison:** Assess whether existing anti-androgenic agents (e.g., spironolactone, finasteride) already address androgenic hypertrichosis with stronger evidence — if so, the marginal value of Cetrorelix repurposing is low.
- **Mechanistic experiment:** If androgenic subtype is confirmed as target, at minimum a preclinical or observational pilot study is needed to elevate evidence beyond L5 before any clinical investment is justified.

---

> **Additional Context — Other Predicted Indications in This Pack**
>
> Among the 10 TxGNN predictions reviewed, two carry stronger mechanistic rationale than the top-ranked hypertrichosis:
>
> - **Central Precocious Puberty 1 (CPP1, Rank #10, L4):** KISS1R gain-of-function mutation activates the GnRH axis prematurely. Cetrorelix directly antagonises GnRH receptor — the class (GnRH agonist depots) is already the standard of care for CPP. GnRH antagonist use in CPP remains an evidence gap but is mechanistically sound and arguably the **highest-priority repurposing candidate** in this batch.
> - **Aromatase Excess Syndrome (AEXS, Rank #9, L4):** Cetrorelix → ↓LH → ↓gonadal androgen substrate → indirect reduction of estrogen synthesis via CYP19A1 aromatase. Case reports support GnRH analogue use in AEXS as adjunct therapy.
>
> Ranks #2–8 include several predictions with **mechanistic contradictions** (e.g., familial male-limited precocious puberty, where LH receptor is constitutively active and GnRH blockade is ineffective) or genetic structural disorders entirely unrelated to the HPG axis (Ambras syndrome, Dandy-Walker malformation, dental malformation syndromes). These should remain deprioritised.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

