---
layout: default
title: Tolfenamic Acid
parent: Model Prediction Only (L5)
nav_order: 844
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tolfenamic Acid: predicted new indication Headache disorder (evidence level L5). Approved use: Not stated in the available India licence data"
monitor_inn: "Tolfenamic acid"
predicted_indications: ["headache disorder", "tendinitis", "rheumatoid arthritis", "trigeminal autonomic cephalalgia", "idiopathic granulomatous myositis", "myositis fibrosa", "fibromyalgia", "exostosis", "inclusion body myositis", "osteoarthritis susceptibility"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Tolfenamic Acid: From an Unspecified Labelled Indication to Headache Disorder
{: .text-alpha }

## One-Sentence Summary

Tolfenamic acid is an NSAID marketed in India as Clotan Capsule. The approved indication text is not available in the data compiled for this report, but its published use is in migraine and rheumatic disease. The TxGNN model predicts it may be effective for **headache disorder**, with **no registered clinical trials** but **19 publications** (including several randomised double-blind studies in migraine) supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available India licence data |
| Predicted New Indication | Headache disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L1 (see note below) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* The literature includes several randomised double-blind trials in migraine (1979–2004), but none is a registered Phase 3 trial, so L1 rests on published RCTs rather than on the strict "two completed Phase 3 RCTs" definition. No clinical trial registry records are available.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. Based on known information, tolfenamic acid is an NSAID of the fenamate class. It inhibits cyclooxygenase and reduces prostaglandin synthesis, and it has also been reported to affect leukotriene pathways.

Prostaglandins sensitise nociceptors and are involved in platelet aggregation, vasodilatation and neurogenic inflammation, all of which are implicated in migraine. This makes a prostaglandin-inhibiting drug a plausible treatment for headache disorders.

One practical consideration is that absorption of oral tolfenamic acid is delayed during a migraine attack, probably because of gastric stasis. Combination with metoclopramide has been studied to address this.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6394143](https://pubmed.ncbi.nlm.nih.gov/6394143/) | 1984 | RCT | Cephalalgia | Tolfenamic acid, metoclopramide, caffeine and their combinations tested in migraine attacks |
| [2375249](https://pubmed.ncbi.nlm.nih.gov/2375249/) | 1990 | RCT | Acta Neurol Scand | Double-blind crossover comparison of tolfenamic acid (200 or 400 mg) and paracetamol in migraine without aura |
| [3727918](https://pubmed.ncbi.nlm.nih.gov/3727918/) | 1986 | RCT | Acta Neurol Scand | Tolfenamic acid and propranolol both significantly reduced attack number and duration versus placebo in prophylaxis |
| [9563211](https://pubmed.ncbi.nlm.nih.gov/9563211/) | 1998 | RCT | Headache | Rapid-release tolfenamic acid had an effect comparable to sumatriptan in acute migraine (141 patients) |
| [12474702](https://pubmed.ncbi.nlm.nih.gov/12474702/) | 2002 | RCT | Medicina (Kaunas) | Tolfenamic acid 300 mg compared with pizotifen for migraine prevention (192 patients) |
| [7976233](https://pubmed.ncbi.nlm.nih.gov/7976233/) | 1994 | RCT | Acta Neurol Scand | Tolfenamic acid versus propranolol for prophylaxis in 76 patients; both drugs significantly effective |
| [89390](https://pubmed.ncbi.nlm.nih.gov/89390/) | 1979 | RCT | Lancet | As effective as ergotamine in reducing attack duration and intensity, with less nausea |
| [7816790](https://pubmed.ncbi.nlm.nih.gov/7816790/) | 1994 | Review | Pharmacol Toxicol | Review of tolfenamic acid in acute and prophylactic migraine treatment |
| [10234467](https://pubmed.ncbi.nlm.nih.gov/10234467/) | 1999 | Retrospective study | Cephalalgia | Adding tolfenamic acid to sumatriptan decreased migraine recurrence |
| [15222892](https://pubmed.ncbi.nlm.nih.gov/15222892/) | 2004 | Randomised open-label | BMC Neurol | Rizatriptan alone versus combined with rofecoxib or tolfenamic acid for recurrence |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 34436 | Clotan Capsule (Torrent Pharmaceuticals Ltd) | Strip of 10 capsules | Not stated in available data |

---

## Safety Considerations

- **Drug Interactions**: The only recorded interaction entry is a pharmacological target association with AKR1C3 (a human enzyme), not a drug–drug interaction with a defined severity level.
- **Pharmacokinetic note**: Migraine attacks delay oral absorption of tolfenamic acid.
- **Long-term tolerability**: A 6-month rheumatic-disease study (600 mg/day) reported mostly mild side effects, mainly diarrhoea and other gastrointestinal disturbances, with some patients stopping treatment.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple randomised, double-blind studies show tolfenamic acid is effective in acute and prophylactic migraine treatment, with efficacy comparable to ergotamine, sumatriptan and propranolol. The mechanism is plausible. However, the evidence is largely from the 1980s–1990s, there are no registered trials, and the safety label data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for Clotan Capsule (currently a blocking gap)
- The approved indication text for the Indian licence
- Detailed mechanism-of-action data
- Review of the older RCTs against current migraine trial standards (e.g., current endpoints and comparators)
- A safety monitoring plan, particularly for gastrointestinal, renal and cardiovascular risks common to NSAIDs

---

## Other Predicted Indications (Brief Note)

Rheumatoid arthritis also has L1-level literature support, including randomised double-blind comparisons with phenylbutazone, aspirin and ibuprofen. It would support symptomatic relief only, not disease modification, and is a candidate for separate evaluation. The other predictions (tendinitis, trigeminal autonomic cephalalgia, myositis variants, fibromyalgia, exostosis, osteoarthritis susceptibility) have no supporting evidence and remain on Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

