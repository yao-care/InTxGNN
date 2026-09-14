---
layout: default
title: Tizanidine
parent: 僅模型預測 (L5)
nav_order: 834
evidence_level: L5
indication_count: 6
---

# Tizanidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Tizanidine: From Muscle Spasticity to Migraine Prevention

## One-Sentence Summary

> Tizanidine is a centrally acting α2-adrenergic receptor agonist, conventionally used as a muscle relaxant for spasticity.
> The TxGNN model predicts it may be effective for **Migraine Disorder** prevention,
> with **2 clinical trials** (including an ongoing Phase 3 RCT) and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Muscle spasticity/spasm (central α2-agonist muscle relaxant) — not currently marketed in India, so no formal approved indication text is available in the regulatory record |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action documentation for tizanidine is not available in this evidence pack. However, the underlying pharmacological rationale is captured in the repurposing evidence: tizanidine is a centrally acting α2-adrenergic receptor agonist that inhibits excitatory neurotransmitter release from the locus coeruleus and the trigeminovascular system.

This mechanism is analogous to clonidine, another α2-agonist that has long been used off-label as a prophylactic agent for chronic daily headache and migraine. The class-effect logic — α2-agonists dampening central noradrenergic and trigeminovascular hyperexcitability — provides a plausible biological bridge between tizanidine's established muscle-relaxant use and its predicted role in migraine prevention.

This is further supported by a substantial body of literature (dating back to 2001–2002) specifically evaluating tizanidine in chronic daily headache/migraine prophylaxis, culminating in a currently recruiting Phase 3 RCT designed explicitly to test this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05484349](https://clinicaltrials.gov/study/NCT05484349) | Phase 3 | Recruiting | 189 | Multicenter, randomized, double-blind, placebo-controlled study evaluating oral tizanidine HCl for preventing migraine attacks in adult episodic migraine patients (with/without aura); pivotal trial, results not yet available |
| [NCT02403687](https://clinicaltrials.gov/study/NCT02403687) | N/A | Completed | 300 | 24-week observational study on analgesic efficacy (focused on topical NSAIDs); only moderately relevant to tizanidine-specific migraine use |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12167135](https://pubmed.ncbi.nlm.nih.gov/12167135/) | 2002 | RCT | Headache | Double-blind, placebo-controlled multicenter study assessing tizanidine as adjunctive prophylactic therapy for chronic daily headache/migraine |
| [11318882](https://pubmed.ncbi.nlm.nih.gov/11318882/) | 2001 | Open-label study | Headache | Dose-titration study of tizanidine tablets for prophylaxis of chronic daily headache; establishes efficacy and tolerability |
| [31365643](https://pubmed.ncbi.nlm.nih.gov/31365643/) | 2019 | Guideline/Consensus | Arquivos de neuro-psiquiatria | Brazilian Headache Society consensus on chronic migraine treatment |
| [40983294](https://pubmed.ncbi.nlm.nih.gov/40983294/) | 2025 | Preclinical/Formulation | J Control Release | Supramolecular co-crystal of tizanidine + meloxicam shows synergistic anti-migraine efficacy |
| [12696998](https://pubmed.ncbi.nlm.nih.gov/12696998/) | 2003 | Review | CNS Drugs | Reviews baclofen, tizanidine and botulinum toxin A as preventative treatments for migraine and tension-type headache |
| [15115635](https://pubmed.ncbi.nlm.nih.gov/15115635/) | 2004 | Review | Curr Pain Headache Rep | Reviews emerging prophylactic migraine options including tizanidine |
| [17115988](https://pubmed.ncbi.nlm.nih.gov/17115988/) | 2006 | Review | Headache | Prophylactic treatment of chronic daily headache, includes tizanidine among evidence-supported agents |
| [21770931](https://pubmed.ncbi.nlm.nih.gov/21770931/) | 2011 | Review | Headache | Reviews clinical trials on chronic migraine prophylaxis, including tizanidine |
| [23293866](https://pubmed.ncbi.nlm.nih.gov/23293866/) | 2013 | Review | Headache | Rational approach to chronic migraine management; lists tizanidine among agents with demonstrated efficacy |
| [11903539](https://pubmed.ncbi.nlm.nih.gov/11903539/) | 2002 | Case study | Headache | Low-dose tizanidine combined with NSAIDs for detoxification from analgesic rebound headache |

---

## India Market Information

Tizanidine is currently **not marketed** in India (0 registered licenses). No product authorization, dosage form, or approved indication text is available for this review.

---

## Safety Considerations

**Drug Interactions:**
Tizanidine has 249 documented drug-drug interactions in the source database. Selected clinically significant ones include:

- **Major:** Famotidine, Morphine, Cimetidine, Dolasetron, Obeticholic acid
- **Moderate:** Hyoscyamine, Loperamide, Atropine, Clarithromycin, Dicyclomine, Difenoxin, Dronabinol, Palonosetron, Sodium sulfate, Nabilone, Naltrexone, Levofloxacin, Metoclopramide, Picosulfuric acid, Polyethylene glycol (3350 with electrolytes)

Given the volume (249 total interactions), a full interaction check against the patient's concurrent medications is recommended before use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A pivotal Phase 3 RCT (NCT05484349) is actively recruiting to directly test tizanidine for migraine prevention, and this is reinforced by a long-standing literature base including an earlier completed placebo-controlled trial (Saper 2002) and consistent class-effect mechanistic rationale (α2-agonist, analogous to clonidine). However, the key confirmatory trial has not yet reported results, and the drug is not currently marketed in India.

**To proceed, the following is needed:**
- Await completion and results of NCT05484349 (expected completion 2025-12-25)
- Obtain formal TFDA/India labeling data — key warnings and contraindications are currently a blocking data gap
- Obtain confirmed mechanism-of-action documentation from DrugBank
- Establish a market registration/access pathway in India, since the drug currently has no local marketing authorization
- Full drug-interaction review given the high interaction count (249 documented)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

