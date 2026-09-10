---
layout: default
title: Hyoscyamine
parent: 僅模型預測 (L5)
nav_order: 413
evidence_level: L5
indication_count: 1
---

# Hyoscyamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Hyoscyamine: From Gastrointestinal Spasm to Gastroduodenitis

## One-Sentence Summary

Hyoscyamine is a muscarinic anticholinergic antispasmodic, clinically used to relieve gastrointestinal spasm, pain, and hypermotility. The TxGNN model predicts it may be effective for **Gastroduodenitis**, but this direction is currently supported by **0 clinical trials** and only **1 weakly-related publication**, so the prediction should be treated as a hypothesis, not a validated finding.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | GI spasm / antispasmodic use (based on known pharmacology; no formal approved-indication text available in this dataset) |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

A formal, sourced mechanism-of-action record for Hyoscyamine is not available in this dataset (flagged as a High-severity data gap, DG002). Based on the pharmacological description captured during evidence review, Hyoscyamine is a competitive antagonist at muscarinic acetylcholine receptors (M1–M3), which suppresses smooth-muscle contraction and glandular secretion. Clinically, this underlies its use as an antispasmodic for GI spasm, pain, and excessive motility.

This anticholinergic action could theoretically ease the spasmodic abdominal pain that sometimes accompanies gastroduodenitis. However, it does not address the underlying pathology of gastroduodenitis, which is typically mucosal inflammation driven by *H. pylori* infection or NSAID exposure. Anticholinergic drugs have no anti-inflammatory or mucosal-protective effect.

The very high TxGNN score (99.59%) most likely reflects a learned association pattern between "GI symptom-relief drugs" and GI diagnoses in the knowledge graph, rather than a true disease-modifying mechanism. This prediction should therefore be interpreted as a potential symptomatic-adjunct signal at best, not evidence of a treatment effect on gastroduodenitis itself.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10696836](https://pubmed.ncbi.nlm.nih.gov/10696836/) | 2000 | Review/Procedural | Endoscopy | Discusses IV sedation practice variation and premedication for endoscopy/colonoscopy (e.g., propofol use, informed consent); does not directly evaluate Hyoscyamine efficacy in gastroduodenitis, and its relevance to this indication is unconfirmed (marked "pending" in evidence classification). |

## India Market Information

Hyoscyamine currently has no market authorization records in this dataset (market status: not marketed; 0 registrations), so no product/license table is available.

## Safety Considerations

- **Drug Interactions**: 207 total interactions on file. Notable moderate-level interactions include additive CNS/anticholinergic or respiratory-depressant effects with opioids (Fentanyl, Alfentanil, Codeine, Dihydrocodeine, Tramadol) and additive anticholinergic burden with other anticholinergic/antihistaminic agents (Amitriptyline, Amoxapine, Chlorpheniramine, Acrivastine, Phenyltoloxamine, Ambenonium, Amantadine) and with Ethanol. Minor interactions were noted with Acetaminophen and Hydrochlorothiazide.

Formal key warnings and contraindications (e.g., from a Taiwan/regional product label) are not available in this dataset — this is flagged as a **Blocking** data gap (DG001), meaning a full safety (S1) assessment cannot be completed until label data is obtained.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a single, weakly-relevant review article and no clinical trials (Evidence Level L5), and a blocking data gap on official label warnings/contraindications prevents even a preliminary safety assessment. The proposed mechanism also does not address the underlying inflammatory pathology of gastroduodenitis.

**To proceed, the following is needed:**
- Official product label / regulatory warnings and contraindications (DG001, blocking)
- A sourced, verifiable mechanism-of-action reference (DG002)
- Targeted literature/clinical-trial search specifically on Hyoscyamine (or anticholinergic antispasmodics) in gastroduodenitis or related dyspeptic/spasmodic GI conditions, since the current single hit is off-topic
- Confirmation of Hyoscyamine's original approved indication(s) from a regulatory source, since none were available in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

