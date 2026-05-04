---
layout: default
title: Alfacalcidol
parent: 僅模型預測 (L5)
nav_order: 32
evidence_level: L5
indication_count: 5
---

# Alfacalcidol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Alfacalcidol: From Renal Osteodystrophy to Familial Isolated Hypoparathyroidism Due to Impaired PTH Secretion

## One-Sentence Summary

Alfacalcidol (1α-hydroxycholecalciferol) is a synthetic active vitamin D analog designed to bypass the kidney's 1α-hydroxylation step, widely used in clinical practice for renal osteodystrophy, general hypoparathyroidism, and vitamin D-dependent rickets. The TxGNN model predicts it may be effective for **familial isolated hypoparathyroidism due to impaired PTH secretion** — a rare genetic condition in which PTH deficiency disrupts the vitamin D activation cascade, creating a direct mechanistic opportunity for alfacalcidol. Currently, **no specific clinical trials** and **no publications** targeting this precise rare subtype have been identified, though the mechanistic alignment is rated "Primary MOA Match."

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Renal osteodystrophy; hypoparathyroidism; vitamin D-dependent rickets (no India regulatory data available) |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L3 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Alfacalcidol is a synthetic 1α-hydroxylated vitamin D analog. After oral administration, it undergoes 25-hydroxylation in the liver to form calcitriol (1,25-dihydroxyvitamin D₃) — the biologically active form — without requiring renal 1α-hydroxylase activity. This design specifically allows it to restore VDR (Vitamin D Receptor) signalling in the intestine and kidneys even when PTH-driven renal activation is absent. Detailed MOA data from DrugBank is currently pending retrieval, but alfacalcidol's pharmacological mechanism is well-established in the scientific literature.

In familial isolated hypoparathyroidism due to impaired PTH secretion, the parathyroid glands fail to produce adequate PTH. Under normal physiology, PTH is the key inducer of renal 1α-hydroxylase, which converts circulating 25-OH D₃ into active calcitriol. Without sufficient PTH, this enzymatic step is severely impaired, leading to hypocalcaemia, hyperphosphataemia, and secondary mineralisation defects. Alfacalcidol directly bypasses this PTH-dependent renal activation step — entering the VDR pathway downstream of the defect in a one-to-one pathophysiological correspondence. This makes the mechanistic link not merely plausible but structurally precise.

The evidence pack rates this mechanistic alignment as a **"Primary MOA Match"** — meaning this rare disease falls squarely within alfacalcidol's core pharmacological design intent. While no clinical trials or publications have been specifically registered for this genetic subtype, alfacalcidol is already used in clinical practice for general hypoparathyroidism, with case series evidence from related conditions (e.g., postsurgical hypoparathyroidism, Fanconi syndrome with renal tubular acidosis) corroborating its role in restoring calcium-phosphate homeostasis when the PTH–kidney axis is disrupted.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific indication.

---

## Literature Evidence

Currently no related literature available specifically addressing familial isolated hypoparathyroidism due to impaired PTH secretion in the context of alfacalcidol therapy.

> **Note:** Supporting mechanistic evidence is available from closely related conditions. For instance, 8 publications were identified linking alfacalcidol use to renal tubular acidosis with secondary hypoparathyroid-like physiology (see ranked indication #5), and the repurposing rationale for this indication is well-supported by decades of clinical pharmacology literature on vitamin D analogs in PTH-deficient states.

---

## India Market Information

Alfacalcidol currently has **no regulatory authorizations** recorded in India. The drug is classified as **not marketed** in the India market, with zero registered product licences on file.

---

## Safety Considerations

Please refer to the package insert for safety information. Full warning text and contraindications from CDSCO (India) or the originating regulatory authority have not yet been retrieved (Data Gap DG001 — severity: Blocking). Until this data is obtained, formal safety-stage screening (S1) cannot be completed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alfacalcidol's mechanism of action aligns with direct one-to-one precision to the pathophysiology of familial isolated hypoparathyroidism due to impaired PTH secretion — this disease was, in effect, the pharmacological target that motivated the drug's original molecular design. The absence of disease-specific clinical trial data reflects the rarity of the condition rather than a mechanistic weakness. However, the drug's lack of India market registration and missing safety data require resolution before any regulatory or clinical step can be taken.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Retrieve full package insert from the originating regulatory authority to extract warnings, contraindications, and dosing guidance for hypoparathyroidism subtypes
- **Resolve DG002 (High):** Confirm MOA data via DrugBank API to formally document the VDR agonist pathway for regulatory submissions
- **India regulatory pathway:** Assess whether alfacalcidol can be registered or imported under orphan drug or rare disease provisions in India
- **Disease-specific dosing research:** Review available case literature on alfacalcidol in PTH-deficient hypoparathyroidism to inform dosing protocols for this genetic subtype
- **Safety monitoring plan:** Design a patient monitoring protocol focusing on hypercalcaemia, hypercalciuria, and renal function — key risks of active vitamin D analog therapy in the absence of normal PTH counter-regulation
- **Expert consultation:** Engage an endocrinologist specialising in rare calcium-phosphate disorders to validate clinical applicability and design a compassionate use or investigator-initiated trial framework
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

