---
layout: default
title: Morphine
parent: Model Prediction Only (L5)
nav_order: 569
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-04
monitor_inn: "Morphine"
predicted_indications: ["myofascial pain syndrome", "manic bipolar affective disorder", "Tourette syndrome", "restless legs syndrome", "attention deficit hyperactivity disorder, inattentive type", "migraine disorder", "trichotillomania", "methemoglobinemia", "migraine with brainstem aura", "specific developmental disorder"]
description: "Morphine: predicted new indication Myofascial pain syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Morphine
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

## Morphine: Myofascial pain syndrome
{: .text-alpha }

## One-Sentence Summary

Morphine is a mu-opioid receptor agonist, a long-established strong analgesic. The TxGNN model predicts it may be useful for **myofascial pain syndrome**, but no clinical trials are registered and none of the 10 publications retrieved tests morphine in this condition, so the evidence level is **L5**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Myofascial pain syndrome |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (15 of 15) – CDSCO approval status is not included in this data |
| Number of Listed Products | 15 (valid: 15) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Morphine is a mu-opioid receptor agonist with well-established analgesic activity. A link to musculoskeletal and myofascial pain is therefore plausible in principle, because pain signalling is reduced.

The supporting literature is indirect, though. The retrieved papers cover opioid use in temporomandibular joint dysfunction, exercise programmes that reduce opioid use in patients with long-term opioid-treated pain, and adjunctive infiltration comparisons after surgery. Opioids are generally not recommended as first-line therapy for myofascial pain, because of dependence risk and limited efficacy in this condition. The high score is a computational prediction and does not reflect demonstrated benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41664327](https://pubmed.ncbi.nlm.nih.gov/41664327/) | 2026 | Randomized trial | Asian Spine J | Dexmedetomidine plus morphine vs plain ropivacaine for myofascial infiltration in spinal fusion. The setting is postoperative pain, not myofascial pain syndrome. |
| [35066974](https://pubmed.ncbi.nlm.nih.gov/35066974/) | 2022 | Retrospective cohort | Pain Pract | A structured stretching programme for myofascial pain in "legacy pain" patients was studied for pain resolution and opioid usage. Morphine was not the intervention. |
| [21419546](https://pubmed.ncbi.nlm.nih.gov/21419546/) | 2011 | Review | J Oral Maxillofac Surg | Long-term opioid use in temporomandibular joint dysfunction can be neither supported nor refuted by current evidence. |
| [16713811](https://pubmed.ncbi.nlm.nih.gov/16713811/) | 2006 | Review | J Oral Maxillofac Surg | Arthrocentesis followed by intra-articular morphine infusion in refractory temporomandibular joint pain. |
| [16967674](https://pubmed.ncbi.nlm.nih.gov/16967674/) | 2006 | Review | J Calif Dent Assoc | Oral medications, infusions and injections for differential diagnosis of orofacial pain. |
| [39793344](https://pubmed.ncbi.nlm.nih.gov/39793344/) | 2025 | Clinical study | Eur J Obstet Gynecol Reprod Biol | Pudendal nerve block for pain after onabotulinumtoxinA injection in myofascial pelvic pain. Not morphine-specific. |
| [21691691](https://pubmed.ncbi.nlm.nih.gov/21691691/) | 2011 | Descriptive study | Rev Assoc Med Bras | Therapeutic approach in 56 patients with failed back surgery pain syndrome. |
| [17870625](https://pubmed.ncbi.nlm.nih.gov/17870625/) | 2008 | RCT | Eur J Pain | Epidural analgesia (bupivacaine and morphine) vs intercostal nerve cryoanalgesia after thoracotomy. Off-target. |
| [7478690](https://pubmed.ncbi.nlm.nih.gov/7478690/) | 1995 | Animal study | Pain | Visceral pain episodes and referred lumbar muscle hyperalgesia in rats. |
| [15176410](https://pubmed.ncbi.nlm.nih.gov/15176410/) | 2004 | Case report | Nervenarzt | Botulinum toxin A injected into stump-muscle trigger points for phantom and stump pain. Not morphine. |

## India Market Information

Morphine is marketed in India, and all 15 licences in the local records are valid. The records carry no approved indication text. Five representative licences:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 135738 | Morcontin 30mg Tablet CR | Strip of 10 controlled-release tablets | Not recorded |
| Registration No. 134780 | Morcontin 10mg Tablet | Strip of 10 tablets | Not recorded |
| Registration No. 233823 | Vermor 10 Injection | Ampoule of 1 ml injection | Not recorded |
| Registration No. 60882 | Duramor 30mg Tablet | Strip of 10 tablets | Not recorded |
| Registration No. 118182 | Koxma Tag Syrup | Bottle of 100 ml syrup | Not recorded |

## Safety Considerations

- **Drug Interactions**: The interaction data lists 721 interacting drugs. Major-level interactions include other opioids and central nervous system depressants:
  - fentanyl
  - codeine
  - dihydrocodeine
  - tramadol
  - butalbital
  - dichloralphenazone
  - alprazolam
  - ethanol
- Moderate-level interactions include chlorpheniramine, cetirizine, nifedipine, hydrochlorothiazide and metformin.
- For package insert warnings and contraindications, please refer to the product label.
- Dependence, respiratory depression and sedation are recognised class risks of opioids. They weigh heavily in a chronic, non-cancer condition such as myofascial pain.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No clinical trial is registered, and no retrieved study tests morphine in myofascial pain syndrome. The one randomized trial concerns postoperative pain after spinal fusion. The evidence is therefore L5, resting on the model prediction alone.
- Opioids are generally not first-line for this condition, and their dependence risk is a significant concern.

**To proceed, the following is needed:**
- Controlled clinical studies of morphine specifically in myofascial pain syndrome, with comparison against standard non-opioid care
- Detailed mechanism-of-action data
- Package insert warnings and contraindications for the marketed products
- A risk-benefit assessment covering dependence, tolerance and opioid-induced hyperalgesia in chronic use

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

