---
layout: default
title: Docusate
parent: Model Prediction Only (L5)
nav_order: 280
evidence_level: L5
indication_count: 2
---

# Docusate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Docusate: From Constipation and Anemia to Plummer-Vinson Syndrome

## One-Sentence Summary

Docusate is a stool softener (anionic surfactant) whose recorded indications include constipation, and several anemia types, most likely because it appears in combination products with iron or folate.
The TxGNN model predicts it may be effective for **Plummer-Vinson syndrome**,
but there are currently **no clinical trials and no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constipation disorder; iron deficiency anemia, folic acid deficiency anemia, and other anemia types (from the knowledge graph; the approved indication text on the Indian licences is blank) |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Docusate is known as a stool softener (an anionic surfactant), and it has an established role in constipation. It has no known effect on iron absorption, blood cell production, or the esophageal changes seen in Plummer-Vinson syndrome.

Plummer-Vinson syndrome typically presents with iron deficiency anemia, difficulty swallowing and esophageal webs. The high score most likely reflects the closeness of this disease to the anemia terms (iron deficiency anemia, hypochromic anemia) linked to docusate in the knowledge graph. Those anemia links probably arise because docusate is sold in combination with iron or folate, where it offsets constipation, rather than because it treats anemia itself.

A second prediction, **vitamin B12- and folate-independent constitutional megaloblastic anemia** (score 99.15%), follows the same pattern. It is a very rare, genetically driven condition, and docusate has no recognized action on DNA synthesis, vitamin B12 or folate metabolism, or red cell maturation. It also has no supporting trials or literature.

Overall, the prediction appears to come from shared graph associations and not from a true pharmacological link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 122099 | Laxicon SG Capsule (Stadmed Pvt Ltd) | Strip of 10 capsules | Not stated |
| Registration No. 199671 | Smuth Capsule (Aristo Pharmaceuticals Pvt Ltd) | Strip of 10 capsules | Not stated |

Both licences are valid single-ingredient oral capsule products.

## Safety Considerations

- **Drug Interactions** (4 recorded; none rated major):
  - Lactulose: Moderate
  - Mineral oil: Moderate
  - Phenolphthalein: Moderate
  - Linaclotide: Minor
- **Conditions flagged as contraindications in the knowledge graph** (from drug-disease relationship data, not package insert text): peptic ulcer disease, ulcerative colitis, inflammatory bowel disease, appendicitis, gastroenteritis, chronic atrophic gastritis, potassium deficiency disease, sickle cell anemia, hemolytic anemia, hereditary persistence of fetal hemoglobin, primary hyperoxaluria, hereditary hemochromatosis, hemosiderosis, iron metabolism disease, Wilson disease, Leber hereditary optic neuropathy.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or publications behind it (evidence level L5). The high model score likely reflects network proximity to anemia terms, not a real pharmacological effect, and there is no plausible mechanism linking a stool softener to Plummer-Vinson syndrome.

**To proceed, the following is needed:**
- Mechanism of action data for docusate, to assess any plausible link
- Package insert warnings and contraindications from the Indian regulator's records, needed before any safety screening
- Evidence of any clinical or preclinical signal for docusate in Plummer-Vinson syndrome, such as case reports or mechanistic studies
- Confirmation of whether the anemia indications in the knowledge graph come from iron or folate combination products, which would explain the prediction as an artefact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

