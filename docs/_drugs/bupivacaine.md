---
layout: default
title: Bupivacaine
parent: Model Prediction Only (L5)
nav_order: 121
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Bupivacaine: predicted new indication Acrodermatitis chronica atrophicans (evidence level L5). Approved use: Dermatitis"
monitor_inn: "Bupivacaine"
predicted_indications: ["neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis"]
---

# Bupivacaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Bupivacaine: From Dermatitis to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Bupivacaine is a long-acting local anaesthetic that, in the knowledge graph used for this prediction, is linked to dermatitis as its original indication.
The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans**,
but **no clinical trials and no publications** currently support this direction, and the data compiled for this report found no credible mechanistic link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis (from the knowledge graph; no approved indication text is available in the India licence records) |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, bupivacaine is a sodium channel-blocking local anaesthetic. It has no known antimicrobial activity.

Acrodermatitis chronica atrophicans is a late-stage skin manifestation of *Borrelia* infection and is treated with antibiotics. The very high score (99.23%) appears to reflect closeness to dermatological terms in the knowledge graph (the original indication is dermatitis) rather than a biological rationale. At most, local anaesthesia could ease pain in affected skin, but that would not treat the disease itself.

The other top predictions show the same pattern:

- **Neonatal dermatomyositis (99.15%)**: an immune-mediated disease treated with corticosteroids and immunomodulators. Bupivacaine can damage muscle at high local concentrations, which is a safety concern here rather than a rationale. Neonatal use adds further risk of systemic local anaesthetic toxicity.
- **Childhood connective-tissue-disease-associated interstitial lung disease (99.11%)**: involves autoimmune inflammation and lung fibrosis. Bupivacaine has no anti-fibrotic or immunomodulatory action, and the link appears to be a graph artefact.
- **Amyopathic dermatomyositis (99.03%)**: the link is weak and indirect. Local anaesthesia might theoretically ease itch or pain, but no evidence exists, and the muscle toxicity caution applies.

## India Market Information

Bupivacaine has 20 valid single-ingredient registrations, all injectable. The licence records contain no approved indication text. The five listed below are examples.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 27290 | Bupicain 5mg Injection | Vial of 20 ml injection | Not stated in the records |
| 124998 | Levo Anawin 0.25% Injection | Vial of 10 ml injection | Not stated in the records |
| 159193 | Numbcaine Heavy 20mg Injection | Vial of 4 ml injection | Not stated in the records |
| 29364 | Bupicain Heavy 80mg Injection | Vial of 4 ml injection | Not stated in the records |
| 3383 | Anawin 0.25% Injection | Vial of 20 ml injection | Not stated in the records |

## Safety Considerations

- **Knowledge-graph contraindications** (these come from drug-disease contraindication links in the graph, not from label text). The listed conditions include:
  - Cardiovascular: hypertension, hypotension, atrial fibrillation, coronary artery disease, myocardial infarction, sudden cardiac arrest, heart conduction disease.
  - Respiratory: COPD, respiratory failure.
  - Liver and kidney: liver failure, liver disease, kidney disease.
  - Other: epilepsy, hypothyroidism, diabetes mellitus, diabetic ketoacidosis, inflammatory bowel disease, benign prostatic hyperplasia, angle-closure glaucoma, substance abuse/dependence, hemoglobinopathy.
- **Drug interactions**: 56 interactions were recorded. Two are rated Moderate: aprepitant and liposomal morphine. The remainder, such as pantoprazole, omeprazole, vancomycin, atropine, dexamethasone and ondansetron, have no severity rating.
- **Population-specific concerns** raised for the predicted indications:
  - Neonates and children: risk of systemic local anaesthetic toxicity.
  - Dermatomyositis: potential muscle toxicity at high local concentrations.
  - Lung disease: respiratory compromise.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5). There are no clinical trials or publications, and the mechanistic review found no credible disease-modifying link for any of the top four predicted indications. The high scores most likely reflect knowledge-graph proximity to dermatological terms.

**To proceed, the following is needed:**
- Mechanism of action data, to allow a proper mechanistic analysis
- Package insert warnings and contraindications from the India market, which are currently missing and block safety screening
- Preclinical or clinical evidence for any predicted indication
- Assessment of route compatibility: all registered forms are injectable
- Safety review for neonatal, paediatric and myopathic populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

