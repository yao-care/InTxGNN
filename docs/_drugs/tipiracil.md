---
layout: default
title: Tipiracil
parent: Model Prediction Only (L5)
nav_order: 833
evidence_level: L5
indication_count: 10
---

# Tipiracil
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

# Tipiracil: From Metastatic Colorectal Cancer to Cecum Villous Adenoma

## One-Sentence Summary

Tipiracil is a thymidine phosphorylase inhibitor combined with trifluridine to form TAS-102 (Lonsurf), originally used for metastatic/unresectable colorectal cancer. The TxGNN model predicts it may be effective for **Cecum Villous Adenoma**, but currently **no clinical trials or publications** directly support this specific direction — the evidence pack's own mechanistic review flags this as a likely false-positive driven by anatomical proximity rather than true biological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic/unresectable colorectal cancer (as component of TAS-102/Lonsurf; not independently marketed) |
| Predicted New Indication | Cecum villous adenoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Tipiracil itself is not cytotoxic. According to pharmacology data in this evidence pack, it acts as a thymidine phosphorylase inhibitor — its role is to block degradation of trifluridine (the actual antimetabolite), thereby increasing trifluridine's bioavailability and DNA-incorporation in tumour cells. This combination (TAS-102/Lonsurf) is approved for metastatic colorectal cancer and is under investigation for metastatic gastric cancer.

However, for the top-ranked prediction — cecum villous adenoma — the evidence pack's own mechanistic analysis argues **against** clinical plausibility rather than for it. Villous adenoma is a benign/pre-malignant lesion, and the standard of care is endoscopic resection, not systemic cytotoxic chemotherapy. The high TxGNN score most likely reflects the knowledge graph's tendency to cluster diseases by anatomical location ("colon/cecum") rather than a genuine mechanistic or clinical relationship to tipiracil's antimetabolite-potentiating activity.

The same anatomical-proximity pattern appears across ranks 2–9 in this evidence pack (colon lipoma, colonic lymphangioma, colon leiomyoma, cavernous hemangioma of colon, etc.) — all benign, non-proliferative, or vascular/structural lesions with no rationale for cytotoxic chemotherapy. Only rank 3 (rectosigmoid junction neoplasm, if malignant) and rank 6 (cecal disease, non-specific) fall within tipiracil's existing mechanistic scope, but neither represents a genuinely new indication signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

Tipiracil is currently **not marketed** in India, with zero registered authorizations on file. No product-level registration data (authorization number, brand name, dosage form, or approved indication text) is available for review.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite-potentiator; component of fluoropyrimidine-adjacent combination TAS-102) |
| Myelosuppression Risk | Medium–High — leukopenia and neutropenia reported as known adverse effects of trifluridine/tipiracil combination therapy (PMID 30677817) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential (leukopenia/neutropenia risk); monitor for diarrhea, vomiting, and fatigue as reported adverse effects |
| Handling Protection | Must follow cytotoxic drug handling regulations as component of an antineoplastic combination product |

---

## Safety Considerations

**Drug Interactions**: 13 moderate-level interactions identified (source: DDInter):

| Interacting Drug | Level |
|---|---|
| Cimetidine | Moderate |
| Tafenoquine | Moderate |
| Ketoconazole | Moderate |
| Brigatinib | Moderate |
| Crizotinib | Moderate |
| Encorafenib | Moderate |
| Ethinylestradiol | Moderate |
| Lenvatinib | Moderate |
| Medroxyprogesterone acetate | Moderate |
| Megestrol acetate | Moderate |
| Ribociclib | Moderate |
| Rucaparib | Moderate |
| Vandetanib | Moderate |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 (model prediction only) with zero clinical trials or publications supporting cecum villous adenoma specifically, and the mechanistic rationale itself concludes the prediction likely reflects a knowledge-graph anatomical-proximity artifact rather than genuine biological plausibility — villous adenoma is a benign lesion managed by endoscopic resection, not cytotoxic chemotherapy.

**To proceed, the following is needed:**
- TFDA/regulatory-authority product label (warnings and contraindications) — currently unavailable and blocking any safety pre-assessment (S1)
- Formal DrugBank-sourced mechanism of action confirmation (currently inferred only from pharmacology interaction records)
- Preclinical or mechanistic evidence specifically addressing benign colorectal adenoma biology, if this indication is to be pursued further
- Re-evaluation of lower-ranked candidates (e.g., rectosigmoid junction neoplasm, if malignant subtype) that fall within tipiracil's existing mechanistic scope, rather than pursuing anatomically-clustered benign lesions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

