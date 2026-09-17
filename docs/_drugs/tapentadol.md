---
layout: default
title: Tapentadol
parent: Model Prediction Only (L5)
nav_order: 800
evidence_level: L5
indication_count: 3
---

# Tapentadol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Tapentadol: From Moderate-to-Severe Pain to Migraine Disorder

## One-Sentence Summary

Tapentadol is a centrally-acting opioid analgesic (μ-opioid agonist plus norepinephrine reuptake inhibitor) used for moderate-to-severe pain; it is **not currently marketed in India**. The TxGNN model predicts a possible new indication in **Migraine Disorder**, but this signal is currently supported by **0 clinical trials** and only **2 indirectly relevant publications** — neither of which studies tapentadol itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate-to-severe pain (opioid analgesic class; no India-specific approved indication text available — drug not registered locally) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 (model prediction only) |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank (flagged as a High-severity data gap). Based on the repurposing rationale generated for this candidate, Tapentadol is a µ-opioid receptor agonist combined with a norepinephrine reuptake inhibitor (NRI). The NRI component theoretically overlaps with the mechanism of some SNRI-class migraine prophylactic agents, which modulate descending pain-inhibitory pathways.

However, this mechanistic overlap is weak and should not be over-interpreted. International headache society guidelines and most clinical practice guidelines explicitly **recommend against** using opioids for acute or preventive migraine treatment, because they lack demonstrated superiority over triptans/NSAIDs and carry a well-documented risk of medication-overuse headache (MOH) and migraine chronification. The predicted association appears to be driven primarily by network-level similarity in the knowledge graph rather than by a validated pharmacological or clinical rationale, and the supporting literature (below) does not mention tapentadol at all.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27096578](https://pubmed.ncbi.nlm.nih.gov/27096578/) | 2016 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Reviews dipyrone (metamizole), a non-opioid analgesic, for postoperative and migraine pain; does not evaluate tapentadol |
| [27096438](https://pubmed.ncbi.nlm.nih.gov/27096438/) | 2016 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Reviews sumatriptan plus naproxen for acute migraine attacks; does not evaluate opioids or tapentadol |

*Note: Both publications discuss migraine pharmacotherapy in general but provide no direct evidence for tapentadol's use in migraine. They are included as background context only.*

## India Market Information

Tapentadol has **no registered product licenses in India** according to the regulatory data on file (0 total licenses). No dosage form or approved indication text is available for local review.

## Safety Considerations

**Drug Interactions** (120 total interactions on file; source: DDInter). Selected Major-severity interactions relevant to opioid/serotonergic risk:

- **Bupropion** — Major
- **Morphine** — Major (additive CNS/respiratory depression)
- **Lorcaserin** — Major (serotonergic risk)
- **Diethylpropion** — Major
- **Dolasetron** — Major
- **Palonosetron** — Major
- **Phentermine** — Major

Additional Moderate-level interactions include anticholinergics (Atropine, Hyoscyamine, Glycopyrronium, Dicyclomine, Trospium), Naloxone, Epinephrine, and cannabinoid-class agents (Dronabinol, Nabilone).

Key warnings and contraindications from the local package insert are not yet available (Blocking data gap — TFDA/India label not yet retrieved); these must be obtained before any safety sign-off.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a single network-derived score (L5, no clinical or drug-specific literature support), and the mechanistic argument is weak — established migraine treatment guidelines actively discourage opioid use due to MOH and chronification risk. The drug is also not currently marketed in India, and core safety documentation (label warnings/contraindications) is missing.

**To proceed, the following is needed:**
- Resolve Blocking gap DG001: retrieve and parse the official package insert (warnings/contraindications) before any S1 safety review
- Resolve High-severity gap DG002: confirm mechanism of action via DrugBank API
- Obtain confirmed original indication and regulatory status (approval history in source market, e.g., US/EU label)
- Targeted literature/trial search specifically for "tapentadol AND migraine" to determine if any drug-specific evidence exists beyond the network prediction
- Reassess against migraine treatment guidelines to formally document why opioid-class agents are generally not recommended, before considering further investment in this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

