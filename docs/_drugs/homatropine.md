---
layout: default
title: Homatropine
parent: Model Prediction Only (L5)
nav_order: 405
evidence_level: L5
indication_count: 4
---

# Homatropine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Homatropine: From Ophthalmic Mydriasis to Cauda Equina Syndrome

## One-Sentence Summary

Homatropine is an anticholinergic (antimuscarinic) agent whose established clinical uses are ophthalmic mydriasis/cycloplegia and as a component of antitussive combination products; it has no formal approved-indication record in the India market dataset. The TxGNN model's top-ranked prediction is **Cauda Equina Syndrome**, but this pairing is supported by **zero clinical trials and zero publications**, and the evidence pack's own mechanistic review flags it as a likely knowledge-graph artifact rather than a genuine pharmacological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (no approved-indication text in the market registry); known clinical use is ophthalmic mydriasis/cycloplegia and as an antitussive combination ingredient |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the drug record (marked as a data gap). Based on known pharmacology, Homatropine is a semisynthetic muscarinic (M2/M3) receptor antagonist, used clinically as an ophthalmic mydriatic/cycloplegic agent and as an antitussive combination ingredient; it has no history of systemic use in neurologic or urologic indications.

Cauda equina syndrome is a surgical emergency caused by mechanical compression of the lumbosacral nerve roots (e.g., disc herniation, tumor), and the standard of care is emergent decompressive surgery — this is not a pathology that an antimuscarinic mechanism can address. The evidence pack's own mechanistic assessment concludes there is no plausible pharmacological link, and attributes the high TxGNN score most likely to graph-level confounding with the comorbid feature "neurogenic bladder" rather than a real drug–disease relationship. On this basis, the top-ranked prediction is not considered a credible repurposing candidate.

Of note, two lower-ranked predictions in this pack — obsolete neurogenic bladder (rank 2) and overactive bladder (rank 4) — have a mechanistically coherent rationale (M3-receptor antagonism reducing detrusor overactivity, analogous to approved OAB antimuscarinics such as oxybutynin and solifenacin). However, these also currently have no supporting clinical trials or literature and remain at evidence level L5, so they would need independent evaluation rather than being folded into this report's primary subject.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## India Market Information

Homatropine has no market authorizations on file in this dataset (0 registrations; market status: not marketed). No product/license records are available to summarize.

## Safety Considerations

- **Drug Interactions**: 17 interactions on record. Two are classified **Major** — Potassium chloride and Potassium citrate (additive risk related to reduced gastrointestinal motility from antimuscarinic effect). The remaining 15 are classified **Moderate**, primarily other antimuscarinic/anticholinergic agents (Dicyclomine, Glycopyrronium, Hyoscyamine, Mepenzolate, Methscopolamine, Propantheline, Ipratropium, Cyclizine, Phenindamine, Phenylephrine, Thiethylperazine), an opioid/antitussive-adjacent group (Opium, Hydrocodone), and cholinesterase-related agents (Edrophonium, Physostigmine) that may antagonize its effect.

Key warnings and contraindications are not available in the current dataset; refer to the package insert for that information once available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (cauda equina syndrome) has no clinical trial or literature support (L5) and is explicitly assessed in the evidence pack as a probable knowledge-graph artifact rather than a mechanistically valid signal, and the condition itself requires surgical rather than pharmacological management.

**To proceed, the following is needed:**
- India/TFDA-equivalent label warnings and contraindications (currently a Blocking data gap — required before any safety pre-screening can proceed)
- Verified mechanism-of-action source (currently a data gap; pharmacology above is inferred from general drug-class knowledge, not a cited MOA record)
- If the antimuscarinic-bladder candidates (overactive bladder / neurogenic bladder) are to be pursued instead, dedicated preclinical or clinical evidence generation is needed, as none currently exists for any of the four predicted indications in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

