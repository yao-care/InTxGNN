---
layout: default
title: Disopyramide
parent: 僅模型預測 (L5)
nav_order: 252
evidence_level: L5
indication_count: 10
---

# Disopyramide
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

# Disopyramide: From Cardiac Arrhythmia to Tourette Syndrome

## One-Sentence Summary

Disopyramide is a Class Ia antiarrhythmic agent that blocks cardiac sodium channels to suppress ventricular and supraventricular arrhythmias.
The TxGNN model predicts it may be effective for **Tourette Syndrome**,
however this prediction is currently supported by **0 clinical trials** and **0 publications**, making it a model-only signal requiring substantial further investigation before any development decision.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cardiac arrhythmia (Class Ia antiarrhythmic; no India registration on file) |
| Predicted New Indication | Tourette Syndrome |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data for Disopyramide is not currently available in the evidence pack. Based on known pharmacology, Disopyramide is a Class Ia antiarrhythmic agent that blocks fast sodium (Na⁺) channels in cardiac tissue and prolongs the effective refractory period. It also carries a clinically significant anticholinergic side-effect profile through muscarinic receptor (M1/M2) antagonism.

The proposed link to Tourette Syndrome rests on the observation that M1 muscarinic receptors play a modulatory role in basal ganglia circuitry — the same circuitry implicated in tic generation. In theory, anticholinergic activity could influence that circuit. However, established anticholinergic agents have not demonstrated efficacy for Tourette Syndrome, and the anticholinergic burden of Disopyramide may in fact worsen cognitive side effects relevant to this patient population (predominantly children and adolescents).

The most plausible explanation for this TxGNN prediction is an indirect knowledge-graph path through shared protein–protein interaction network nodes (e.g., Na⁺ channel subunits expressed in neuronal tissue) rather than a direct pharmacological mechanism. The prediction should be treated as a hypothesis-generating signal only, not as mechanistic evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Disopyramide has no registered products in India. No license records are available.

---

## Safety Considerations

**Drug Interactions (258 total interactions on file):**

The following are the highest-severity interactions identified:

| Severity | Interacting Drug | Clinical Relevance |
|----------|-----------------|-------------------|
| **Major** | Potassium citrate | Urine alkalinisation reduces disopyramide renal clearance, raising plasma levels and toxicity risk |
| **Major** | Clarithromycin | CYP3A4 inhibition elevates disopyramide levels; combined QT prolongation risk |
| **Major** | Picosulfuric acid | Electrolyte depletion (hypokalaemia) potentiates arrhythmia and QT prolongation |

Selected Moderate interactions (out of a larger list):

| Severity | Interacting Drug |
|----------|-----------------|
| Moderate | Atropine / Hyoscyamine / Glycopyrronium / Clidinium (additive anticholinergic effects) |
| Moderate | Hydrocortisone / Dexamethasone / Betamethasone / Budesonide / Triamcinolone (hypokalaemia, QT risk) |
| Moderate | Famotidine / Cimetidine (altered renal excretion) |
| Moderate | Amphotericin B / Amphotericin B (lipid complex) (hypokalaemia) |
| Moderate | Loperamide / Bisacodyl (motility effects compound anticholinergic burden) |
| Moderate | Aprepitant (CYP3A4 modulation) |
| Moderate | Chlorpropamide (hypoglycaemia risk) |

Please refer to the package insert for full warnings and contraindications, as those data were not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.86%), but this reflects knowledge-graph topology rather than pharmacological plausibility — the mechanistic rationale for Disopyramide in Tourette Syndrome is weak, and the drug's anticholinergic profile may be contraindicated in the target population. There is zero clinical or preclinical literature supporting this indication.

**To reconsider this candidate, the following would be needed:**

- Retrieve and review the full Disopyramide package insert (from a reference market such as the US FDA or EMA) to document contraindications and black-box warnings — currently a blocking data gap
- Confirm the full MOA via DrugBank API query (currently a high-severity data gap)
- Conduct a systematic literature search in neuropsychiatric databases (e.g., PsycINFO, EMBASE) using broader terms (Na⁺ channel blockers + tic disorders; anticholinergics + Tourette) to rule out any unpublished or non-indexed signals
- Evaluate whether India-specific registration is feasible given the drug is currently not marketed domestically
- If mechanistic rationale emerges, commission a scoping review before any preclinical investment

> **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

