---
layout: default
title: Glimepiride
parent: 僅模型預測 (L5)
nav_order: 313
evidence_level: L5
indication_count: 9
---

# Glimepiride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Glimepiride: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Glimepiride is a second-generation sulfonylurea used to treat Type 2 Diabetes Mellitus by stimulating pancreatic insulin secretion.
The TxGNN model predicts it may be effective for **Focal Stiff Limb Syndrome**, a rare autoimmune neurological disorder,
but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests entirely on the model score, and the underlying rationale itself flags it as likely knowledge-graph noise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (based on known pharmacological classification; Taiwan license data is not available — drug is not marketed locally) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| India Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank query in this evidence pack (data gap DG002, High severity). Based on known pharmacological information, Glimepiride is a second-generation sulfonylurea, part of the oral antidiabetic sulfonylurea class. Its established mechanism involves binding the SUR1 subunit of the ATP-sensitive potassium (K_ATP) channel on pancreatic beta cells, causing channel closure, cell depolarization, calcium influx, and stimulated insulin secretion. Its efficacy in Type 2 Diabetes Mellitus is well established and long-standing.

The TxGNN model's top-ranked prediction, Focal Stiff Limb Syndrome, sits within the stiff person syndrome (SPS) spectrum — a rare autoimmune neurological disorder driven by GAD65-antibody-mediated impairment of GABAergic neurotransmission. This is mechanistically distant from Glimepiride's established insulin-secretagogue action. As explicitly noted in the evidence pack's own repurposing rationale, although K_ATP channels are also expressed in neurons, there is no established direct link between K_ATP channel blockade and the autoimmune GABAergic pathology underlying stiff person syndrome — the connection is described as weak and highly suspected to be an artifact of node proximity in the knowledge graph rather than a genuine pharmacological signal.

This concern is reinforced by the broader candidate set: ranks 5–8 (drug-induced localized lipodystrophy, centrifugal lipodystrophy, pressure-induced localized lipoatrophy, idiopathic localized lipodystrophy) are four distinct lipodystrophy/lipoatrophy syndromes clustered at nearly identical scores (~0.996), which strongly suggests a systematic "fat tissue / metabolic disease" node clustering effect rather than a drug-specific signal. The only candidate in this list with a biologically traceable (if indirect) rationale is rank 9, pancreatic agenesis — sulfonylureas have documented clinical use in K_ATP-channel-mutation (KCNJ11/ABCC8) neonatal diabetes (PNDM) — but pancreatic agenesis itself is caused by distinct developmental transcription factor defects (PTF1A, GATA6), not K_ATP channel dysfunction, making even this link indirect and speculative, and it is explicitly unsupported by any clinical or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

Glimepiride is currently **not marketed** in this jurisdiction (未上市) and holds **no active local drug licenses** (total_licenses = 0). No license records are available to summarize authorization number, product name, dosage form, or approved indication.

---

## Safety Considerations

**Drug Interactions**: The DDI database recorded **599 total documented interactions** for Glimepiride. Notable interaction categories from the returned sample (levels as reported, mostly Moderate unless noted) include:

- **Ethanol** – Moderate (may potentiate hypoglycemia)
- **Beta-blockers** (Acebutolol) – Moderate (may mask hypoglycemia warning signs)
- **H2-receptor antagonists** (Famotidine, Ranitidine) – Moderate
- **NSAIDs** (Ibuprofen, Ketorolac) – Moderate (may potentiate hypoglycemic effect)
- **Sympathomimetics** (Phenylephrine, Pseudoephedrine, Epinephrine, Salbutamol, Formoterol) – Moderate (may raise blood glucose / antagonize glycemic control)
- **Thiazide diuretics** (Hydrochlorothiazide) – Moderate (hyperglycemic effect)
- **Systemic corticosteroids** (Hydrocortisone) – Moderate (hyperglycemic effect); **topical corticosteroids** (Hydrocortisone topical, Alclometasone topical) – Minor
- **Estrogens** (Ethinylestradiol) – Moderate (may reduce glycemic control)
- **GLP-1 receptor agonist** (Albiglutide) – Moderate (additive hypoglycemia risk)
- **Acetazolamide, Acitretin, Nitazoxanide** – Moderate

Detailed key warnings and contraindications from the TFDA package insert are a **Blocking** data gap (DG001) and are not yet available in this evidence pack — please refer to the package insert once obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All 9 predicted indications rest solely on the TxGNN model score (L5 evidence, S0 decision stage) with zero supporting clinical trials or published literature, and several of the underlying rationale narratives explicitly flag the candidates — including the top-ranked one — as likely knowledge-graph artifacts rather than genuine pharmacological signal.
- A Blocking data gap (TFDA warnings/contraindications, DG001) independently prevents entry into Stage 1 safety evaluation regardless of the indication's merit.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — Blocking gap, must be resolved before any S1 safety screening
- Confirmed mechanism of action from DrugBank API — High-severity gap, needed for rigorous mechanistic assessment
- If further investigation is warranted, a targeted literature/clinical search on sulfonylurea use in K_ATP-channel-mutation neonatal diabetes, as a lead-in to evaluating the pancreatic agenesis hypothesis (rank 9) — the only candidate with a biologically traceable, if indirect, rationale
- Independent expert/clinical review of the full TxGNN candidate list before committing further resources, given that the evidence pack's own rationale text flags likely noise in the top-ranked predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

