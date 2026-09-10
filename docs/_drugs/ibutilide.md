---
layout: default
title: Ibutilide
parent: 僅模型預測 (L5)
nav_order: 415
evidence_level: L5
indication_count: 2
---

# Ibutilide
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

# Ibutilide: From Atrial Fibrillation/Flutter to Rheumatoid Arthritis

## One-Sentence Summary

Ibutilide is a Class III antiarrhythmic used intravenously for acute termination of atrial fibrillation/flutter; it is not currently marketed in Taiwan. The TxGNN model predicts a possible effect on **Rheumatoid Arthritis**, but this prediction is currently supported by **no clinical trials and no literature** — it is a model-only signal (Evidence Level L5) with a mechanistic rationale that the evidence pack itself flags as weak and speculative.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial Fibrillation / Atrial Flutter (IV, acute termination) — derived from known pharmacology noted in the evidence pack; no Taiwan license record available |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Ibutilide is not available in this evidence pack (MOA field marked as a data gap). Based on the mechanistic notes accompanying the prediction, Ibutilide is a Class III antiarrhythmic that activates the slow inward sodium current and blocks the delayed rectifier potassium current (IKr), prolonging atrial and ventricular action potentials and effective refractory periods. Its only established clinical use is IV administration for acute termination of atrial fibrillation/flutter.

Rheumatoid arthritis is driven by autoimmune inflammatory pathways (TNF-α, IL-6, RANKL, synovial proliferation) that have no established connection to cardiac ion-channel modulation. The evidence pack's own rationale states there is no known immunomodulatory or anti-inflammatory activity for Ibutilide, and characterizes the mechanistic link to rheumatoid arthritis as speculative rather than substantiated. Given the absence of any clinical trial, literature, or preclinical signal connecting the two, this prediction should be treated as an early-stage hypothesis generated purely from the knowledge-graph model, not as a mechanistically grounded candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Ibutilide is not currently marketed in Taiwan (0 registrations on file), so no product license records are available for review.

---

## Safety Considerations

**Drug Interactions**: Ibutilide has 125 recorded interactions in the DDI database. Notable **Major**-severity interactions include: Clarithromycin, Picosulfuric acid, Polyethylene glycol (3350 with electrolytes), Dolasetron, Eliglustat, Palonosetron, Sodium sulfate, Levofloxacin, Ondansetron, Granisetron, and Cisapride. Several of these (e.g., ondansetron, granisetron, dolasetron, palonosetron, cisapride, clarithromycin, levofloxacin) are themselves QT-prolonging agents, consistent with Ibutilide's Class III mechanism and raising particular concern for additive QT-prolongation/arrhythmia risk. Moderate-level interactions were also recorded with Famotidine, Loperamide, Bisacodyl, Lactitol, Lactulose, Polyethylene glycol (3350), Castor oil, and Glycerin; a Minor interaction was recorded with Metronidazole.

Package-insert warnings and contraindications are not yet available for this drug (TFDA label data gap, flagged as Blocking).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the prediction is unsupported by any clinical trial or literature evidence (L5, decision stage S0), and the evidence pack's own mechanistic assessment characterizes the drug–disease link as speculative. Combined with the absence of TFDA label data (a Blocking gap), this candidate cannot proceed to safety evaluation yet.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — Blocking gap, required before any S1 safety review
- Detailed mechanism-of-action confirmation from DrugBank/primary literature
- Preclinical or mechanistic studies exploring any plausible link between Class III antiarrhythmic activity and autoimmune/rheumatoid pathways
- Clarification of regulatory pathway, since Ibutilide is not currently marketed in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

