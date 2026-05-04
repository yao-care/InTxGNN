---
layout: default
title: Amantadine
parent: 僅模型預測 (L5)
nav_order: 44
evidence_level: L5
indication_count: 4
---

# Amantadine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Amantadine: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Amantadine is a well-established agent used for Parkinson's disease and influenza A, acting primarily through non-competitive NMDA receptor antagonism and dopaminergic enhancement. The TxGNN model predicts it may be effective for **Rasmussen Subacute Encephalitis**, a rare, chronic autoimmune encephalitis causing progressive unilateral brain destruction. Currently, **no clinical trials and no publications** specifically support this repurposing direction — the prediction rests entirely on model inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease; influenza A (not currently marketed in India) |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory data on record. Based on known pharmacological information, Amantadine functions as a **non-competitive NMDA receptor antagonist** (blocking glutamate-mediated excitotoxicity) and a **dopaminergic agent** (promoting dopamine release and inhibiting reuptake). These dual mechanisms underlie its established use in Parkinson's disease, where it reduces motor symptoms and drug-induced dyskinesia.

Rasmussen Encephalitis (RE) is a rare, progressive autoimmune condition characterised by T-cell-mediated unilateral hemispheric inflammation and neuronal destruction. While the primary pathology is immune-driven, secondary **glutamate excitotoxicity via NMDA receptor over-activation** contributes to neuronal death and propagation of seizure activity. A subset of RE patients also carry antibodies against GluR3 (an AMPA receptor subunit), suggesting cross-talk with glutamate receptor pathways. Amantadine's NMDA antagonism theoretically could reduce this secondary excitotoxic cascade — analogous to the rationale supporting Memantine use in neuroinflammatory conditions.

However, the mechanistic link is **indirect and weak**. RE's core pathophysiology is autoimmune, not dopaminergic or glutamatergic in origin. Amantadine does not address the T-cell-mediated inflammation that drives the disease. The TxGNN high score likely reflects broad network connectivity between "antiviral/antiparkinson" drug nodes and "encephalitis/CNS inflammation" disease nodes in the knowledge graph, rather than a specific mechanistic fit. This should be treated as a hypothesis-generating signal, not a clinically actionable finding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Amantadine currently has **no registered products** in India. There are no active licenses, approved dosage forms, or approved indications on record.

---

## Safety Considerations

Formal package insert warnings and contraindications data are not available in this evidence pack. Please refer to the original package insert for complete safety information.

**Key Drug Interactions** (93 interactions on record; selected below by clinical significance):

| Interacting Drug | Severity | Clinical Note |
|-----------------|----------|--------------|
| Bupropion | **Major** | Increased risk of seizures and CNS toxicity; concurrent use generally contraindicated |
| Atropine | Moderate | Additive anticholinergic effects; risk of urinary retention, confusion, dry mouth |
| Scopolamine | Moderate | Additive anticholinergic effects |
| Hyoscyamine | Moderate | Additive anticholinergic effects |
| Glycopyrronium | Moderate | Additive anticholinergic effects |
| Dicyclomine | Moderate | Additive anticholinergic effects |
| Trospium | Moderate | Additive anticholinergic effects |
| Methscopolamine | Moderate | Additive anticholinergic effects |
| Mepenzolate | Moderate | Additive anticholinergic effects |
| Propantheline | Moderate | Additive anticholinergic effects |
| Clidinium | Moderate | Additive anticholinergic effects |
| Metoclopramide | Moderate | Pharmacodynamic antagonism; amantadine may reduce metoclopramide efficacy |
| Polyethylene glycol 3350 | Moderate | Altered GI transit may affect amantadine absorption |
| Picosulfuric acid | Moderate | Altered GI transit may affect amantadine absorption |
| Sodium sulfate | Moderate | Altered GI transit may affect amantadine absorption |

> ⚠️ The full interaction list contains 93 entries. The anticholinergic burden is a particularly notable concern for elderly or neurologically impaired patients. Verify all concurrent medications before any clinical trial design.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high confidence score (99.48%), but this reflects network topology in the knowledge graph rather than disease-specific mechanistic evidence. Rasmussen Encephalitis is a rare autoimmune CNS disease whose primary pathology — T-cell-mediated neuroinflammation — is not directly addressed by Amantadine's known mechanisms. There are zero supporting clinical trials and zero supporting publications. This is a model-only prediction (L5) with weak-to-moderate indirect mechanistic plausibility.

**To proceed to the next stage, the following is needed:**

- **MOA confirmation**: Retrieve full Amantadine DrugBank entry including mechanism, pharmacodynamics, and pharmacokinetics
- **Preclinical evidence search**: Broaden literature review to include NMDA antagonism in autoimmune encephalitis animal models
- **RE patient population context**: Confirm whether any RE sub-types (anti-GluR3+) might be selectively responsive to glutamate pathway modulation
- **Comparator analysis**: Review Memantine (structurally and mechanistically similar NMDA antagonist) for any RE-related case reports or small series
- **Safety profile completion**: Obtain TFDA/FDA/EMA package insert to document formal contraindications and warnings, particularly regarding CNS adverse effects (confusion, hallucinations, seizures) relevant to encephalitis patients
- **Orphan drug pathway assessment**: Given RE's ultra-rare status, evaluate eligibility for orphan drug designation in India, which may lower the evidence threshold for exploratory IND
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

