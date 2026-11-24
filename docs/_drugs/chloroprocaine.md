---
layout: default
title: Chloroprocaine
parent: Model Prediction Only (L5)
nav_order: 173
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Chloroprocaine: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not stated in the India licence record (drug class: local anaesthetic)"
monitor_inn: "Chloroprocaine"
predicted_indications: ["cauda equina syndrome"]
---

# Chloroprocaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Chloroprocaine: From Local Anaesthesia to Cauda Equina Syndrome (Prediction Likely Reflects an Adverse-Event Link)
{: .text-alpha }

## One-Sentence Summary

Chloroprocaine is a short-acting ester local anaesthetic, marketed in India as an injectable.
The TxGNN model predicts **Cauda Equina Syndrome** with a very high score, but the data compiled for this report show **no clinical trials** and only **4 publications**, which describe the syndrome as a *complication* of local anaesthetics, not a condition they treat.
The prediction most likely reflects a drug-harm association and not a therapeutic opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India licence record (drug class: local anaesthetic) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9901 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Chloroprocaine blocks voltage-gated sodium channels, which produces short-acting local anaesthesia. According to the Clinical Pharmacology section of the US FDA-approved prescribing information for chloroprocaine: "Chloroprocaine, like other local anesthetics, blocks the generation and the conduction of nerve impulses, presumably by increasing the threshold for electrical excitation in the nerve, by slowing the propagation of the nerve impulse and by reducing the rate of rise of the action potential. In general, the progression of anesthesia is related to the diameter, myelination and conduction velocity of affected nerve fibers." ([DailyMed: Nesacaine (chloroprocaine hydrochloride) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a844e68a-1462-40e4-be5e-f56214906eb9), label version 2022-09-01; accessed 2026-11-19.) This class effect is well established.

On review, the prediction does not appear to be therapeutically reasonable. The literature links chloroprocaine to cauda equina syndrome as a **possible cause**, through neurotoxicity after intrathecal or epidural exposure, particularly with older preservative-containing formulations. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence; it may therefore capture an adverse-event relationship between the drug and the disease.

Cauda equina syndrome is a surgical emergency, usually caused by compression or ischaemia of the nerve roots and needing decompression. Sodium channel blockade would not reverse that injury, so no plausible mechanism supports treatment benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22236346](https://pubmed.ncbi.nlm.nih.gov/22236346/) | 2012 | RCT | Acta Anaesthesiol Scand | Chloroprocaine vs lidocaine for selective spinal anaesthesia in outpatient TURP. This is an anaesthesia use, not a cauda equina syndrome treatment study. |
| [23320599](https://pubmed.ncbi.nlm.nih.gov/23320599/) | 2013 | Review | Acta Anaesthesiol Scand | Chloroprocaine as a spinal anaesthetic alternative to lidocaine. Neurological sequelae were described after large intrathecal doses of preservative-containing formulations. |
| [11368250](https://pubmed.ncbi.nlm.nih.gov/11368250/) | 2001 | Review | Drug Safety | Complications of regional anaesthesia (neural injury, local anaesthetic toxicity) and their prevention. |
| [9338907](https://pubmed.ncbi.nlm.nih.gov/9338907/) | 1997 | Case report | Regional Anesthesia | Two cases of cauda equina syndrome after spinal-epidural anaesthesia. Chloroprocaine had previously been implicated in its aetiology. |

None of these publications supports chloroprocaine as a treatment for cauda equina syndrome. The case report and the safety review describe it as a complication.

---

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 43204 | Clorquik 1% Injection | Ampoule of 5 ml Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease edges, not label text): kidney disease, pyoureter, liver disease, gallbladder disease, myasthenia gravis (including adult-onset), neuromuscular junction disease, butyrylcholinesterase deficiency, cardiovascular disease, heart disease.
- **Drug Interactions** (12 recorded):
  - **Major:** Nitrous acid.
  - **Moderate:** Sulfasalazine; other local anaesthetics in topical, nasal or ophthalmic use (lidocaine, benzocaine, tetracaine, oxybuprocaine, cinchocaine); cocaine (nasal and topical).
  - **Minor:** Hyaluronidase.
- **Neurotoxicity:** The literature on this prediction raises concern about cauda equina syndrome after intrathecal or epidural exposure, which is the opposite of the predicted benefit.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial support and no plausible therapeutic mechanism. The available literature points to chloroprocaine as a potential cause of cauda equina syndrome, so the high model score is probably an artefact of an adverse-event association. Pursuing this as a repurposing candidate is not supported.

**To proceed, the following is needed:**
- Confirmation that the prediction is not driven by adverse-event associations learned by the TxGNN model (deep learning), whose score may reflect similarities learned between related diseases, not biological evidence. Without that, it should be treated as a false positive.
- Any preclinical or clinical evidence of therapeutic benefit in cauda equina syndrome, which is not currently available.
- Package insert warnings and contraindications from the India regulator, and the approved indication text for the licensed product.
- Mechanism of action data from DrugBank.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data from DrugBank is not available in the compiled data, but t" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Nesacaine (chloroprocaine hydrochloride) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a844e68a-1462-40e4-be5e-f56214906eb9) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

