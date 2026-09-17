---
layout: default
title: Tolfenamic Acid
parent: Model Prediction Only (L5)
nav_order: 837
evidence_level: L5
indication_count: 10
---

# Tolfenamic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Tolfenamic Acid: From Acute Migraine (International Use) to Headache Disorder

## One-Sentence Summary

> Tolfenamic acid is a fenamate NSAID with no current marketing authorization in Taiwan; internationally (e.g., UK) it is approved for acute migraine treatment.
> The TxGNN model predicts it may also be effective for **Headache Disorder** (broadly),
> supported by **20 published studies** — including multiple double-blind RCTs — though **no registered clinical trials** were found for this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally registered in Taiwan; internationally approved for acute migraine (UK) |
| Predicted New Indication | Headache Disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 (multiple historical double-blind RCTs in literature; no registered clinical trials) |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is currently a data gap. Based on available pharmacology literature, tolfenamic acid is an anthranilic acid (fenamate) derivative NSAID that acts as a potent inhibitor of prostaglandin biosynthesis and has also been reported to inhibit leukotriene synthesis. DrugBank pharmacology data additionally lists an interaction with **AKR1C3** (aldo-keto reductase family 1 member C3), an enzyme involved in prostaglandin F and steroid metabolism, consistent with the drug's anti-inflammatory pharmacology.

This mechanism directly supports the drug's already-established international use in acute migraine: prostaglandins are implicated in migraine-related vasodilation, sensitization of nociceptors, and hyperalgesia, and multiple older RCTs show tolfenamic acid performing comparably to ergotamine, sumatriptan, and paracetamol in acute attacks, and to propranolol/pizotifen in prophylaxis.

The TxGNN prediction of "Headache Disorder" is therefore largely a restatement/extension of an indication the molecule already has strong real-world and trial support for outside Taiwan, rather than a mechanistically novel repurposing hypothesis. The main gap is not scientific plausibility but the absence of Taiwan-specific regulatory data (label, market authorization) needed to act on it locally.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (no entries found in ClinicalTrials.gov or ICTRP for this indication).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2375249](https://pubmed.ncbi.nlm.nih.gov/2375249/) | 1990 | RCT (double-blind crossover) | Acta Neurol Scand | Tolfenamic acid 200/400 mg vs. paracetamol 500/1000 mg in acute common migraine |
| [3727918](https://pubmed.ncbi.nlm.nih.gov/3727918/) | 1986 | RCT (double-blind crossover) | Acta Neurol Scand | Tolfenamic acid vs. propranolol vs. placebo for migraine prophylaxis; both active drugs reduced attack frequency/duration |
| [7051739](https://pubmed.ncbi.nlm.nih.gov/7051739/) | 1982 | RCT (double-blind crossover) | Acta Neurol Scand | Tolfenamic acid significantly better than placebo for migraine prophylaxis (attack frequency, duration, vomiting) |
| [7976233](https://pubmed.ncbi.nlm.nih.gov/7976233/) | 1994 | RCT (double-blind crossover) | Acta Neurol Scand | Tolfenamic acid 100 mg TID vs. propranolol 40 mg TID for migraine prophylaxis in 76 patients |
| [9563211](https://pubmed.ncbi.nlm.nih.gov/9563211/) | 1998 | RCT (double-blind, parallel-group) | Headache | Tolfenamic acid rapid release vs. oral sumatriptan for acute migraine; comparable efficacy in 141 patients |
| [12474702](https://pubmed.ncbi.nlm.nih.gov/12474702/) | 2002 | RCT (double-blind, parallel-group) | Medicina (Kaunas) | Tolfenamic acid 300 mg vs. pizotifen 1.5 mg for migraine prevention in 192 patients |
| [89390](https://pubmed.ncbi.nlm.nih.gov/89390/) | 1979 | RCT (double-blind crossover) | Lancet | Tolfenamic acid vs. ergotamine vs. aspirin vs. placebo in 160 migraine attacks; efficacy comparable to ergotamine with fewer side effects |
| [6984358](https://pubmed.ncbi.nlm.nih.gov/6984358/) | 1982 | Clinical study | Cephalalgia | Tolfenamic acid combined with caffeine, metoclopramide, or pyridoxine in acute migraine (60 attacks) |
| [6394143](https://pubmed.ncbi.nlm.nih.gov/6394143/) | 1984 | Clinical study | Cephalalgia | Tolfenamic acid, metoclopramide, caffeine, and combinations tested in migraine attacks |
| [7816790](https://pubmed.ncbi.nlm.nih.gov/7816790/) | 1994 | Review | Pharmacology & Toxicology | Review of tolfenamic acid in acute and prophylactic migraine treatment, prostaglandin hypothesis |

---

## Taiwan Market Information

Tolfenamic acid currently holds **no marketing authorizations in Taiwan** (0 registrations, market status: Not marketed/Not Marketed). No license records are available.

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA-specific key warnings and contraindications are not yet available (see Data Gaps below); a pharmacology-level target interaction with AKR1C3 (aldo-keto reductase C3) is recorded in DrugBank, but its clinical drug-drug interaction relevance has not been established.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence for headache/migraine is substantial (multiple historical double-blind RCTs vs. placebo, propranolol, pizotifen, sumatriptan, and ergotamine), but the candidate cannot advance to formal safety review (S1) because TFDA label warnings/contraindications are a **Blocking** data gap, and the drug currently has zero marketing authorizations in Taiwan.

**To proceed, the following is needed:**
- TFDA label data (warnings, contraindications) — download and parse official package insert (DG001, Blocking)
- DrugBank-confirmed mechanism of action (DG002, High) to formally support the mechanistic rationale
- Classification/tiering of the currently "pending" literature evidence (study type, relevance) to firm up the evidence level
- Assessment of a regulatory pathway for Taiwan market entry, given current non-marketed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

