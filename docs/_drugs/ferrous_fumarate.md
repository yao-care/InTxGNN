---
layout: default
title: Ferrous Fumarate
parent: Model Prediction Only (L5)
nav_order: 347
evidence_level: L5
indication_count: 1
---

# Ferrous Fumarate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Ferrous Fumarate: From Iron-Deficiency Anemia to Non-syndromic Esophageal Malformation

## One-Sentence Summary

Ferrous fumarate is an oral iron salt conventionally used to treat iron-deficiency anemia (this original indication is general pharmacological knowledge — the evidence pack itself contains no confirmed indication text, as the drug has no India/Taiwan license record). The TxGNN model predicts a possible link to **non-syndromic esophageal malformation**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags the link as mechanistically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron-deficiency anemia (general pharmacological knowledge; not present in evidence pack — no license record) |
| Predicted New Indication | Non-syndromic esophageal malformation |
| TxGNN Prediction Score | 99.49% (rank #8604 among candidates) |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (MOA marked as data gap). Based on known pharmacology, ferrous fumarate supplies ferrous iron to support hemoglobin/heme synthesis and is used to correct iron-deficiency states — a metabolic replacement mechanism, not a developmental or structural one.

Non-syndromic esophageal malformation (e.g., esophageal atresia / tracheoesophageal fistula) is a congenital structural defect arising during embryonic foregut development. There is no established biological pathway by which iron repletion would influence esophageal morphogenesis, and no drug is known to reverse a structural malformation pharmacologically.

The model's own rationale for this candidate states that the high TxGNN score most likely reflects sparse or spuriously co-occurring graph nodes (e.g., "iron/anemia" and "congenital/pediatric" clusering together in the knowledge graph) rather than a genuine mechanistic signal. Combined with the complete absence of clinical, preclinical, or literature evidence, this prediction should be treated as a low-confidence model artifact rather than a credible repurposing hypothesis at this stage.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Ferrous fumarate has no license records in this evidence pack — market status is "Not Marketed" with 0 registrations on file. No product/authorization details are available to summarize.

## Safety Considerations

**Drug Interactions** (80 total interactions on file; representative entries below):
- **Proton pump inhibitors / acid suppressants** (Moderate): Omeprazole, Esomeprazole, Lansoprazole, Dexlansoprazole, Pantoprazole — reduced gastric acidity may impair iron absorption.
- **Tetracycline-class antibiotics** (Moderate): Doxycycline, Tetracycline, Minocycline — mutual absorption reduction via chelation.
- **Fluoroquinolones** (Moderate): Levofloxacin — chelation reduces antibiotic absorption.
- **Antacids / mineral salts** (Moderate): Magnesium oxide, Calcium carbonate, Aluminum hydroxide, Magaldrate, Sodium sulfate, Triethylenetetramine — reduced iron absorption.
- **Pancrelipase** (Moderate).
- **H2-receptor antagonist** (Minor): Cimetidine.
- **Zinc salts** (Minor): Zinc sulfate, Zinc acetate — competitive absorption interference.

Key warnings and contraindications are not available in the evidence pack; please refer to the package insert for this information once obtained.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 (model prediction only) with zero supporting clinical trials or literature, and the drug's own mechanistic rationale finds no plausible biological link between iron repletion and a congenital structural esophageal defect. A blocking data gap (missing TFDA/label safety data) also prevents any S1 safety pre-assessment.

**To proceed, the following is needed:**
- TFDA/regulatory label data — warnings and contraindications (blocking gap, DG001)
- Confirmed mechanism of action documentation (DG002)
- Any preclinical or mechanistic evidence linking iron metabolism to esophageal/foregut development, to justify further investment
- Reassessment of the TxGNN candidate ranking (#8604) to confirm this is not a low-priority artifact before allocating further review resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

