---
layout: default
title: Tizanidine
parent: Model Prediction Only (L5)
nav_order: 841
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Tizanidine: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the licence data (the drug is known as a muscle relaxan…"
monitor_inn: "Tizanidine"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "Tourette syndrome", "ulerythema ophryogenesis"]
---

# Tizanidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Tizanidine: From Spasticity-Related Muscle Tone Disorders to Migraine Disorder

## One-Sentence Summary

Tizanidine is a centrally acting alpha-2 adrenergic agonist marketed in India as a muscle relaxant. The approved indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **migraine disorder**, with **1 Phase 3 clinical trial** (results not yet verified) and **16 publications** (including 1 placebo-controlled RCT in chronic daily headache) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data (the drug is known as a muscle relaxant for spasticity) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L1 (as assigned in the compiled data; see the caveat below) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 15 |
| Recommended Decision | Proceed with Guardrails |

**Evidence level caveat:** The only Phase 3 migraine trial (NCT05484349) has an unknown status and no verified results. The strongest completed evidence is a placebo-controlled RCT in chronic daily headache, not episodic migraine. The L1 grade should therefore be read cautiously.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from DrugBank. Based on known pharmacology, tizanidine is a central alpha-2 adrenergic agonist. It is used to reduce muscle tone and spasticity.

The relationship between the two indications is plausible. By modulating trigeminal and brainstem pain-signalling pathways, an alpha-2 agonist may reduce how often migraine attacks occur. Lowering tension in the neck and head muscles may also help, since this is thought to contribute to chronic daily headache.

The strongest direct clinical evidence so far concerns chronic daily headache (chronic migraine, migrainous headache and tension-type headache), not episodic migraine. Several reviews list tizanidine among preventive options, with limited and mixed supporting data.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05484349](https://clinicaltrials.gov/study/NCT05484349) | Phase 3 | Unknown | 189 | Multicentre, randomised, double-blind, placebo-controlled study of oral tizanidine for preventing migraine attacks in adults with episodic migraine; no results verified |

One further registered study (NCT02403687, a topical NSAID analgesic study) was found, but it has no clear link to tizanidine or migraine and is not listed.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12167135](https://pubmed.ncbi.nlm.nih.gov/12167135/) | 2002 | RCT | Headache | Double-blind, placebo-controlled multicentre study of tizanidine as add-on prophylaxis for chronic daily headache |
| [31365643](https://pubmed.ncbi.nlm.nih.gov/31365643/) | 2019 | Consensus guideline | Arq Neuropsiquiatr | Brazilian Headache Society consensus on chronic migraine treatment |
| [12696998](https://pubmed.ncbi.nlm.nih.gov/12696998/) | 2003 | Review | CNS Drugs | Muscle-tone drugs (baclofen, tizanidine, botulinum toxin A) as preventives for migraine and tension-type headache; evidence limited and mixed |
| [20464578](https://pubmed.ncbi.nlm.nih.gov/20464578/) | 2010 | Review | Neurol Sci | Review of double-blind placebo-controlled trials of chronic migraine prophylaxis |
| [15115635](https://pubmed.ncbi.nlm.nih.gov/15115635/) | 2004 | Review | Curr Pain Headache Rep | Emerging migraine preventives, including tizanidine |
| [17115988](https://pubmed.ncbi.nlm.nih.gov/17115988/) | 2006 | Review | Headache | Prophylactic treatment of chronic daily headache; tizanidine among the agents with evidence |
| [11318882](https://pubmed.ncbi.nlm.nih.gov/11318882/) | 2001 | Open-label study | Headache | Dose-titration study of tizanidine for chronic daily headache prophylaxis |
| [11903539](https://pubmed.ncbi.nlm.nih.gov/11903539/) | 2002 | Clinical report | Headache | Low-dose tizanidine with NSAIDs for detoxification from analgesic rebound headache |
| [40983294](https://pubmed.ncbi.nlm.nih.gov/40983294/) | 2025 | Preclinical/formulation | J Control Release | Tizanidine–meloxicam supramolecular co-assembly with enhanced anti-migraine effect |
| [23293866](https://pubmed.ncbi.nlm.nih.gov/23293866/) | 2013 | Review | Headache | Rational approach to chronic migraine management; tizanidine among options |

## India Market Information

Fifteen valid single-ingredient registrations exist; five are shown below. Approved indication text is not available in the licence data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 217069 | Tizan 4mg Tablet (Sun Pharmaceutical) | Strip of 10 tablets | Not stated |
| 214866 | Tizan 2 Tablet (Sun Pharmaceutical) | Strip of 10 tablets | Not stated |
| 199785 | Sirdalud 2mg Tablet (Novartis India) | Strip of 6 tablets | Not stated |
| 138570 | Myodine 2mg Tablet (Bangalore Antibiotics & Biologicals) | Strip of 10 tablets | Not stated |
| 97202 | Ginox Tablet (Gold Line) | Strip of 10 tablets | Not stated |

One registration (Ginox Gel, 96677) is a topical gel. The remaining products are oral tablets, so an oral route is available for a migraine-prevention indication.

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): liver failure, kidney disease, pyoureter, psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder and hypotensive disorder.
- **Drug interactions:** 249 interactions are recorded. Major-level examples include famotidine, cimetidine, morphine, dolasetron and obeticholic acid. Moderate-level examples include hyoscyamine, loperamide, atropine, clarithromycin, levofloxacin, metoclopramide, naltrexone and dicyclomine. Strong CYP1A2 inhibitors such as fluvoxamine and ciprofloxacin also warrant caution.
- **Other concerns noted in the analysis:** sedation, hypotension and hepatotoxicity risk.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A Phase 3 placebo-controlled migraine prevention trial is registered, and a placebo-controlled RCT supports tizanidine in chronic daily headache. However, the migraine trial has no verified results, and the existing clinical evidence is mainly for chronic daily headache. The safety burden (sedation, hypotension, liver risk, many interactions) calls for guardrails.

**To proceed, the following is needed:**
- Results or status update for NCT05484349 in episodic migraine
- Package insert warnings and contraindications (currently a blocking data gap)
- Mechanism of action data from DrugBank
- A liver function and blood pressure monitoring plan, and an interaction-screening plan (especially CYP1A2 inhibitors)

## Other Predicted Indications (Brief Note)

The other predicted indications are weaker and do not currently support a decision to proceed:
- **Migraine with brainstem aura** (score 99.71%): Hold. Evidence is indirect, with no trials.
- **Migraine with or without aura, susceptibility to** (score 99.54%): Research question. This is a genetic susceptibility entity and should be assessed under migraine disorder.
- **Tourette syndrome** (score 99.17%): Hold. Other alpha-2 agonists (clonidine, guanfacine) are used for tics, but there are no tizanidine-specific data.
- **Atrophoderma vermiculata** (score 99.31%) and **ulerythema ophryogenesis** (score 99.13%): Hold. These are model predictions only, with no trials, no literature and no plausible mechanism.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

