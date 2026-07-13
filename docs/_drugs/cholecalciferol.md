---
layout: default
title: Cholecalciferol
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 7
---

# Cholecalciferol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cholecalciferol: From Vitamin D Supplementation to Familial Isolated Hypoparathyroidism Due to Impaired PTH Secretion

## One-Sentence Summary

Cholecalciferol (Vitamin D3) is a fat-soluble prohormone widely used as a nutritional supplement to correct vitamin D deficiency and support skeletal health.
The TxGNN model predicts it may be effective for **Familial Isolated Hypoparathyroidism Due to Impaired PTH Secretion** with a score of **99.79%**,
however, **no clinical trials or published literature** directly support this specific repurposing direction, placing this prediction at evidence level L5 — and importantly, the underlying mechanism of Cholecalciferol activation is itself impaired by the very disease being predicted.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vitamin D deficiency / nutritional supplement for bone and calcium metabolism (no formal approved indication recorded in India) |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 (model prediction only — no supporting studies) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacology, Cholecalciferol (Vitamin D3) is a fat-soluble prohormone that requires two sequential hydroxylation steps to become biologically active: the first in the liver (producing 25-hydroxyvitamin D / calcifediol), and the second in the kidney (producing 1,25-dihydroxyvitamin D / calcitriol). This second step is critically dependent on PTH stimulation of renal 1α-hydroxylase — a pathway that is directly disrupted in the very condition being predicted.

Familial isolated hypoparathyroidism due to impaired PTH secretion is a rare genetic disorder characterized by insufficient PTH production, resulting in hypocalcemia and hyperphosphatemia. The fundamental mechanistic obstacle is that without PTH, the kidney cannot efficiently convert Cholecalciferol into its active form. This is precisely why established clinical practice for hypoparathyroidism uses **active vitamin D analogues** — calcitriol or alfacalcidol — that bypass the PTH-dependent activation step entirely, rather than Cholecalciferol itself.

The high TxGNN score most likely reflects **graph-level proximity** between Cholecalciferol and the calcium/phosphate regulatory network nodes in the knowledge graph, rather than a genuine prediction of direct clinical utility for Cholecalciferol in this condition. Network proximity in a biological knowledge graph is not equivalent to clinical applicability, and in this case the mechanistic evidence actively argues against Cholecalciferol as the treatment agent.

---

## Clinical Trial Evidence

Currently no related clinical trials testing Cholecalciferol for familial isolated hypoparathyroidism due to impaired PTH secretion are registered.

---

## Literature Evidence

Currently no related literature directly addressing Cholecalciferol for familial isolated hypoparathyroidism due to impaired PTH secretion is available.

---

## India Market Information

Cholecalciferol currently has no registered products in the Indian market based on the available regulatory data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|----------------------|--------------|-------------|---------------------|
| — | — | — | No registered products found |

---

## Safety Considerations

**Drug Interactions (56 total interactions identified):**

The following Major interactions require particular attention:

| Interacting Drug | Level | Clinical Note |
|-----------------|-------|---------------|
| Calcifediol | Major | Concurrent use risks additive vitamin D toxicity and hypercalcemia |
| Calcitriol | Major | Concurrent use risks additive vitamin D toxicity and hypercalcemia |
| Dihydrotachysterol | Major | Concurrent use risks additive vitamin D toxicity and hypercalcemia |
| Doxercalciferol | Major | Concurrent use risks additive vitamin D toxicity and hypercalcemia |

**Notable Moderate interactions (selected):**

| Category | Drugs | Concern |
|---------|-------|---------|
| Thiazide diuretics | Bendroflumethiazide, Benzthiazide, Chlorothiazide, Chlorthalidone | Enhanced hypercalcemia risk |
| Bile acid sequestrants | Cholestyramine, Colesevelam, Colestipol | Reduced Cholecalciferol absorption |
| Anticonvulsants | Carbamazepine, Amobarbital, Butabarbital, Butalbital | Accelerated Cholecalciferol catabolism |
| Cardiac glycosides | Digitoxin, Digoxin | Hypercalcemia may potentiate glycoside toxicity |
| Topical vitamin D analogues | Calcipotriol (topical), Calcitriol (topical) | Additive systemic vitamin D effect |

For full warnings, contraindications, and prescribing precautions, please refer to the approved package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns Cholecalciferol a high prediction score (99.79%) for familial isolated hypoparathyroidism due to impaired PTH secretion, this prediction directly conflicts with established pharmacology — PTH deficiency impairs the renal activation of Cholecalciferol itself, making active vitamin D analogues (calcitriol or alfacalcidol) the pharmacologically and clinically appropriate agents for this disease. There is no clinical trial or literature evidence to support this repurposing direction.

**To proceed, the following would be needed:**

- **Mechanistic clarification:** Investigate whether Cholecalciferol has any adjunctive role alongside active vitamin D analogues in PTH-deficient states (e.g., hepatic 25-hydroxylation remains intact and calcifediol levels may be relevant)
- **Clinical evidence:** Identify any case series, observational data, or mechanistic studies specifically examining Cholecalciferol (not calcitriol) in familial isolated hypoparathyroidism
- **Regulatory dossier:** No Indian market approval exists; complete safety data from the approved package insert (key warnings, contraindications) must be obtained before any clinical evaluation
- **India regulatory pathway:** Since Cholecalciferol is not currently marketed in India, the full regulatory registration pathway for this indication would need to be mapped
- **Consider alternative predictions:** Among the 7 TxGNN predictions in this evidence pack, **renal osteodystrophy** (rank 6, L3 evidence, "Proceed with Guardrails") and **hypophosphatemic rickets** (rank 5, L3 evidence, "Research Question") carry substantially stronger mechanistic and clinical backing for Cholecalciferol, and may be more productive repurposing directions to evaluate

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

