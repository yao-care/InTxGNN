---
layout: default
title: Nefopam
parent: Model Prediction Only (L5)
nav_order: 584
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Nefopam: predicted new indication Craniostenosis cataract . The most evidence-supported alternative is… (evidence level L5). Approved use: Not stated on the India licences (analgesic by drug class)"
monitor_inn: "Nefopam"
predicted_indications: ["craniostenosis cataract", "mature cataract", "diabetes mellitus type 2 associated cataract", "tetanic cataract", "immature cataract", "cortical cataract", "nuclear senile cataract", "senile cataract", "diabetic cataract", "lumbar spinal stenosis"]
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

## Nefopam: From Pain Management (Indication Not Listed on Licences) to Lumbar Spinal Stenosis
{: .text-alpha }

## One-Sentence Summary

Nefopam is a centrally acting non-opioid analgesic that is marketed in India. The TxGNN model's top-ranked predictions are a cluster of cataract-related conditions, which have no supporting evidence. The only prediction with any literature behind it is **lumbar spinal stenosis** (perioperative pain), with **0 registered clinical trials** and **4 publications**, so the evidence remains early.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated on the India licences (analgesic by drug class) |
| Predicted New Indication | Craniostenosis cataract (top-ranked, no evidence). The most evidence-supported alternative is lumbar spinal stenosis (rank 10). |
| TxGNN Prediction Score | 99.98% (craniostenosis cataract); 99.97% (lumbar spinal stenosis) |
| Evidence Level | L5 (craniostenosis cataract); L4 (lumbar spinal stenosis) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this drug is not available in the compiled data. Based on general pharmacology, nefopam is a centrally acting non-opioid analgesic. It is understood to inhibit serotonin, norepinephrine and dopamine reuptake and to modulate voltage-gated sodium and calcium channels.

**The cataract predictions (ranks 1–9)** are not credible. Nefopam's actions have no known link to lens opacity, crystallin aggregation, the polyol pathway or calcium homeostasis. All nine terms carry nearly identical scores (99.97–99.98%), which suggests a systematic knowledge-graph artifact rather than independent signals. There are no trials or publications for any of them.

**Lumbar spinal stenosis (rank 10)** is biologically plausible as symptomatic pain management. Central analgesic and monoamine-reuptake actions could reduce postoperative pain and dysesthesia after spine surgery, and may reduce opioid use. This would be symptom control, not disease modification. Two retrieved publications (PMIDs 38068520 and 41937571) appear to be randomized perioperative studies, but the data compiled for this report contain only truncated abstracts. Their results cannot be confirmed, so the evidence level is capped at L4 pending full-text review.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

These publications relate to lumbar spinal stenosis. No literature exists for the cataract predictions.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38068520](https://pubmed.ncbi.nlm.nih.gov/38068520/) | 2023 | RCT (double-blind, randomized) | J Clin Med | Effect of 20 mg nefopam on dysesthesia, postoperative pain and satisfaction in 73 patients undergoing spine surgery for lumbar spinal stenosis. Results are not available in the compiled abstract. |
| [41937571](https://pubmed.ncbi.nlm.nih.gov/41937571/) | 2026 | RCT (double-blind, placebo-controlled) | Asian Spine J | Opioid-sparing effect of continuous postoperative intravenous nefopam after multilevel degenerative lumbar spinal fusion. Results are not available in the compiled abstract. |
| [31166320](https://pubmed.ncbi.nlm.nih.gov/31166320/) | 2019 | Clinical study | Zh Vopr Neirokhir Im N N Burdenko | Compares multimodal analgesia regimens in spinal stenosis surgery and their effect on failed back surgery syndrome. Nefopam involvement is unconfirmed. |
| [25535527](https://pubmed.ncbi.nlm.nih.gov/25535527/) | 2014 | Case report | J Korean Neurosurg Soc | Status epilepticus attributed to nefopam in a 71-year-old man admitted for lumbar spinal stenosis surgery. This is a safety signal. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 150449 | Nefodol Tablet (Medley Pharmaceuticals) | Strip of 10 tablets | Not stated |
| 151496 | Nefosar 20mg Injection (Abbott) | Ampoule of 1 ml injection | Not stated |
| 150485 | Nefosar Tablet (Abbott) | Strip of 10 tablets | Not stated |

Both oral (tablet) and injectable forms are available.

## Safety Considerations

- **Neurological risk**: The literature includes a case report of status epilepticus caused by nefopam in a patient undergoing lumbar spinal stenosis surgery (PMID 25535527). The abstract also notes other reported neurologic reactions (confusion, hallucinations, delirium, convulsions) and anticholinergic, cardiovascular and neuropsychiatric adverse effects.

Please refer to the package insert for further safety information, including warnings, contraindications and drug interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked cataract predictions have no mechanistic or clinical support and appear to be model artifacts. Lumbar spinal stenosis (perioperative pain) is plausible, with two apparent randomized studies, but their results are unverified and a seizure-related safety signal exists.

**To proceed, the following is needed:**
- Full-text review of PMIDs 38068520 and 41937571 to confirm design, outcomes and effect sizes
- Package insert warnings and contraindications for the India products (currently missing)
- Detailed mechanism of action data from DrugBank
- Confirmation of the approved indications on the India licences
- A seizure-risk assessment for the proposed perioperative spine surgery population
- Route compatibility assessment (oral and injectable forms are available; the required route has not been defined)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

