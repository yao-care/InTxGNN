---
layout: default
title: Nefopam
parent: Model Prediction Only (L5)
nav_order: 584
evidence_level: L5
indication_count: 10
monitor_inn: "Nefopam"
predicted_indications: ["immature cataract", "mature cataract", "craniostenosis cataract", "diabetes mellitus type 2 associated cataract", "tetanic cataract", "cortical cataract", "nuclear senile cataract", "senile cataract", "diabetic cataract", "lumbar spinal stenosis"]
last_modified_at: 2026-10-30
description: "Nefopam: predicted new indication Immature cataract (evidence level L5). Approved use: Not stated in the licence records (analgesic drug class)"
---

# Nefopam
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

## Nefopam: From Pain Relief (Analgesia) to Immature Cataract
{: .text-alpha }

## One-Sentence Summary

Nefopam is a centrally acting, non-opioid analgesic that is currently marketed in India as tablets and an injection. The TxGNN model predicts it may be effective for **immature cataract**, but there are **0 clinical trials** and **0 publications** for this disease, so the prediction rests on the model score alone. A separate prediction in the same list, lumbar spinal stenosis, has some supporting literature and is covered below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records (analgesic drug class) |
| Predicted New Indication | Immature cataract |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (3 of 3) – CDSCO approval status is not included in this data |
| Number of Listed Products | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in a structured form. Based on the compiled information, nefopam inhibits serotonin, norepinephrine and dopamine reuptake and modulates voltage-gated sodium and calcium channels. These actions fit pain relief.

No mechanistic link to lens opacification has been established. The score of 0.9998 comes from the TxGNN model (deep learning) and is shared by most cataract subtypes in the list (immature, mature, craniostenosis, type 2 diabetes-associated, tetanic, cortical, nuclear senile and senile cataract). Diabetic cataract scores 0.9997. This pattern may reflect similarities the model learned between related diseases, not biological evidence. The prediction should be treated as a hypothesis without supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Another Prediction with Literature: Lumbar Spinal Stenosis

Lumbar spinal stenosis (TxGNN score 0.9997) is the only predicted indication in this list with published studies. The studies concern pain control around spine surgery, not treatment of the disease itself, and nefopam is already an analgesic. No registered clinical trials were provided. The evidence level is set conservatively at L3, and the recommendation is "Research Question".

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38068520](https://pubmed.ncbi.nlm.nih.gov/38068520/) | 2023 | Randomized, double-blind study | J Clin Med | 73 patients having spine surgery for lumbar spinal stenosis received nefopam 20 mg or saline. The study looked at dysesthesia, postoperative pain and satisfaction. |
| [41937571](https://pubmed.ncbi.nlm.nih.gov/41937571/) | 2026 | Randomized, double-blind, placebo-controlled trial | Asian Spine J | Opioid-sparing effect of postoperative continuous intravenous nefopam in multilevel degenerative lumbar spinal fusion. |
| [31166320](https://pubmed.ncbi.nlm.nih.gov/31166320/) | 2019 | Clinical study or review (design to be confirmed) | Zh Vopr Neirokhir Im N N Burdenko | Compared multimodal analgesia regimens during spinal stenosis surgery and their effect on the rate of failed back surgery syndrome. |
| [25535527](https://pubmed.ncbi.nlm.nih.gov/25535527/) | 2014 | Case report | J Korean Neurosurg Soc | Status epilepticus after nefopam in a 71-year-old man admitted for lumbar spinal stenosis surgery. |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 150449 | Nefodol Tablet | Strip of 10 tablets | Medley Pharmaceuticals |
| 151496 | Nefosar 20mg Injection | Ampoule of 1 ml injection | Abbott |
| 150485 | Nefosar Tablet | Strip of 10 tablets | Abbott |

All three licences are valid single-ingredient products, available in oral and injectable forms. The licence records do not include approved indication text.

---

## Safety Considerations

- **Seizure risk:** A published case report describes status epilepticus after nefopam (PMID 25535527). Seizure-risk guardrails would be needed in any further development.
- No drug interactions were found in the queried data, and no disease contraindications were recorded in the knowledge graph.

For other safety information, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The immature cataract prediction has no clinical trials and no publications, and no plausible mechanism links nefopam to lens opacity. The identical score across the cataract cluster points to a model artifact. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanistic or preclinical evidence linking nefopam to lens biology, before any further work on the cataract predictions
- The package insert warnings and contraindications from the India licence documents
- The approved indication text for the three licences
- If the lumbar spinal stenosis question is pursued, confirmation of the study designs and a review of seizure-risk safety
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

