---
layout: default
title: Clobetasone
parent: Model Prediction Only (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
---

# Clobetasone
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

# Clobetasone: From Topical Corticosteroid-Responsive Skin Conditions to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Clobetasone is a moderate-potency topical corticosteroid marketed in India in cream and ointment form.
The TxGNN model predicts it may be useful for **primary cutaneous T-cell lymphoma** (score 99.97%),
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it remains a model-based hypothesis only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available licence data |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, clobetasone is a moderate-potency topical corticosteroid that acts through the glucocorticoid receptor, producing anti-inflammatory and immunosuppressive effects in the skin.

Topical corticosteroids are used as skin-directed therapy for early-stage mycosis fungoides, the most common subtype of cutaneous T-cell lymphoma (CTCL). A symptomatic benefit (reduced inflammation, itch and plaque activity) is therefore plausible. However, higher-potency agents such as clobetasol are the ones typically studied for this purpose, and no data specific to clobetasone were supplied.

The other top predictions are weaker. Sezary syndrome is a leukaemic, systemic disease, so a topical moderate-potency agent is unlikely to modify it. Primary cutaneous B-cell lymphoma and granulomatous slack skin disease are doubtful or unsupported. Several predictions (Crohn's colitis, nephrotic syndrome, adrenocortical insufficiency) appear to reflect a corticosteroid class association rather than a feasible use of a topical skin product. Cystic teratoma and spinal cord dermoid cyst have no plausible mechanism and are likely spurious knowledge-graph results.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Clobetasone is marketed in India as single-ingredient licences (20 valid, none cancelled), all in topical forms. The approved indication text is not recorded for any of the licences. The first five are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 136517 | Miclogenta Cream | Tube of 5 gm cream | Not specified |
| 150645 | Nadoxin-C Cream | Tube of 10 gm cream | Not specified |
| 27677 | Butesone Cream | Tube of 15 gm cream | Not specified |
| 44302 | Clodis GM Cream | Tube of 15 gm cream | Not specified |
| 36746 | Clomed M Cream | Tube of 10 gm cream | Not specified |

## Safety Considerations

Please refer to the package insert for safety information.

One point from the prediction analysis is worth noting: topical corticosteroids can suppress the hypothalamic-pituitary-adrenal (HPA) axis, particularly with extensive or prolonged use. For the adrenocortical insufficiency prediction, this is more a safety concern than a therapeutic opportunity.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a TxGNN prediction (L5), with no clinical trials or literature for clobetasone. The mechanism is plausible only as symptomatic skin-directed therapy in early-stage CTCL, where higher-potency corticosteroids are the usual choice. Package insert safety information has not been obtained.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently blocking for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for the Indian licences
- A targeted literature search on topical corticosteroids, and clobetasone specifically, in early-stage mycosis fungoides / CTCL
- A comparison with higher-potency corticosteroids to see whether a moderate-potency agent offers any advantage (for example, a better safety profile)
- Route and formulation compatibility assessment for lymphoma indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

