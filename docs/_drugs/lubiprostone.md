---
layout: default
title: Lubiprostone
parent: Model Prediction Only (L5)
nav_order: 508
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lubiprostone: predicted new indication Alopecia (evidence level L5). Approved use: Chronic constipation and irritable bowel syndrome"
monitor_inn: "Lubiprostone"
predicted_indications: ["alopecia", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "diffuse alopecia areata", "pulmonary hypertension", "kyphoscoliotic heart disease", "Raynaud disease", "pulmonary hypertension, primary, autosomal recessive", "phaeochromocytoma", "peripheral vascular disease"]
---

# Lubiprostone
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

# Lubiprostone: From Chronic Constipation to Alopecia

## One-Sentence Summary

Lubiprostone is a ClC-2 chloride channel activator (a prostone-class compound) used to treat chronic constipation and irritable bowel syndrome.
The TxGNN model predicts it may be effective for **alopecia**, but **no clinical trials and no publications** currently support this direction.
The prediction is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic constipation and irritable bowel syndrome (from pharmacology data; the India license record has no indication text) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From pharmacology data, lubiprostone is a ClC-2 chloride channel activator (target gene CLCN2) that acts on the gut epithelium. It is a bicyclic fatty acid derived from prostaglandin E1, and it has minimal systemic absorption.

No established mechanistic link between ClC-2 activation and hair follicle biology was identified. The high score is likely driven by shared network neighbours in the knowledge graph, such as prostaglandin-related pathways. Prostaglandin analogues such as bimatoprost do affect hair growth, but lubiprostone does not act on the same receptors. This explanation is therefore speculative and cannot be verified.

The other top predictions fall into two groups:
- **Hair disorders:** congenital hypotrichosis milia (99.93%), hypotrichosis simplex of the scalp (99.93%) and diffuse alopecia areata (99.93%). These likely echo the same signal as alopecia rather than providing independent support. Alopecia areata is autoimmune, and lubiprostone has no known immunomodulatory action relevant to it.
- **Vascular and other conditions:** pulmonary hypertension (99.86%), kyphoscoliotic heart disease (99.81%), Raynaud disease (99.64%), autosomal recessive primary pulmonary hypertension (99.54%), phaeochromocytoma (99.50%) and peripheral vascular disease (99.40%). The vascular links rest on the prostanoid scaffold shared with prostacyclin or alprostadil analogues. Lubiprostone has little systemic exposure and no demonstrated vasodilatory effect. No plausible mechanism was identified for phaeochromocytoma.

All ten predictions have evidence level L5 and a Hold recommendation.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 121000 | Lubowel 24 Soft Gelatin Capsule (Sun Pharmaceutical Industries Ltd) | Strip of 15 soft gelatin capsules (oral) | Not stated in the license record |

## Safety Considerations

- **Drug Interactions:**
  - Idelalisib: Moderate interaction (DDInter).
  - ClC-2 (CLCN2): this is the pharmacological target of lubiprostone, not an interacting drug.

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based model score. There are no clinical trials or publications, and no plausible mechanism links a gut-acting ClC-2 activator with minimal systemic absorption to hair loss. The package insert safety data are also missing.

**To proceed, the following is needed:**
- Obtain the package insert (warnings and contraindications) from the India Pharma source
- Obtain mechanism of action data from DrugBank
- Perform a systematic literature and trial search on lubiprostone or prostone compounds and hair growth
- Run preclinical studies (for example, hair follicle models) to test any biological plausibility
- Assess route compatibility, since the only available route is oral and a topical or systemic route may be needed for hair or vascular indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

