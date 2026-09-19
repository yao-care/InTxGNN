---
layout: default
title: Otilonium
parent: Model Prediction Only (L5)
nav_order: 617
evidence_level: L5
indication_count: 10
---

# Otilonium
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

# Otilonium: From Local Intestinal Antispasmodic Action to Hypertrichosis Prediction

## Summary

Otilonium (DrugBank DB13500) has an empty original indication list in the evidence package and a missing mechanism of action (MOA), which can only be inferred from the candidate mechanism hint text as a **local intestinal antimuscarinergic/calcium channel antagonist** (in international literature, primarily used for irritable bowel syndrome-related indications, with extremely low systemic absorption). The TxGNN model's top-ranked predicted indication is **Hypertrichosis**, with a prediction score of 98.94%, but there are **zero clinical trials and zero literature** supporting this, and this score clusters with another 8 candidates completely unrelated in mechanism (Dandy-Walker syndrome, polyps at various sites, etc.) within the 0.985–0.989 range, strongly suggesting this is model noise rather than a true signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indications | Not recorded in Taiwan regulatory data (`licenses` is empty, `total_licenses` = 0); according to candidate mechanism hint text, internationally classified as irritable bowel syndrome-related local intestinal antispasmodic, not from the approval source of this evidence package |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 98.94% |
| Evidence Level | L5 (model prediction only, no clinical trials, no literature) |
| Taiwan Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why This Prediction Lacks Convincingness

Detailed mechanism of action (MOA) data for Otilonium is currently unavailable (DG002, High severity). Based on the mechanism hint provided in the evidence package, Otilonium is a local intestinal antimuscarinergic/calcium channel antagonist with extremely low systemic absorption, with primary pharmacological targets on intestinal smooth muscle, and there is no known biological intersection with hair growth regulatory pathways (hair follicle cycling, androgen receptor signaling, etc.).

More critically, this candidate (Hypertrichosis) and 8 other candidates ranked 2–10 in the same batch (Dandy-Walker syndrome, Ambras-type congenital universal hypertrichosis, odontogenic developmental malformation syndrome, hair shaft structural abnormalities, polyps of the vocal cord/middle ear/uterus/external auditory canal/frontal sinus, etc.) have prediction scores almost entirely clustered within 0.985–0.989, and **all except rank 4 have zero trials and zero literature**. This pattern—spanning multiple anatomical regions with unrelated etiologies yet highly concentrated scores—is a typical feature of model noise due to sparse adjacency in knowledge graphs or unstable embeddings, not drug-specific signals.

Although rank 4 (odontogenic/periodontal-related malformation syndrome) retrieved 20 literature records, upon detailed review of the titles and abstracts of each paper, all content addresses general pathophysiology of periodontal disease, diabetes comorbidity, non-surgical treatment, etc., **with none mentioning Otilonium or its pharmacological components**; this is keyword co-occurrence rather than mechanism evidence and cannot serve as corroboration.

---

## Clinical Trial Evidence

Currently, no relevant clinical trial registrations are available.

---

## Literature Evidence

Currently, no relevant literature data are available.

---

## Taiwan Market Information

Otilonium is currently **Not marketed** in Taiwan, with no valid product approval certificates (`total_licenses` = 0); no registration data can be listed.

---

## Safety Considerations

Please refer to the safety information contained in the product label.

(DDI query returned no results; warnings and contraindications are both data gaps DG001, classified as Blocking level, and S1 safety preliminary assessment cannot be conducted at this time.)

---

## Conclusions and Further Recommendations

**Decision: Hold**

**Rationale:**
This candidate has an evidence level of L5, with zero clinical trials and zero literature, and mechanistically lacks a reasonable connection to known pharmacological actions (local intestinal smooth muscle regulation); the cross-anatomical score clustering pattern observed in this batch further supports this as model noise rather than a biologically meaningful signal, and progression to the next stage is not recommended.

**If progression is desired, the following must be supplemented:**
- Complete warnings and contraindications data from TFDA/original product label (DG001, Blocking, obstructing S1 safety preliminary assessment)
- Detailed MOA data from DrugBank or original product information (DG002, High)
- If reassessment is warranted in the future, it is recommended to prioritize reviewing candidate indications more mechanistically related to Otilonium's known intestinal pharmacological action, rather than this batch of hypertrichosis and polyp-related noise

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

