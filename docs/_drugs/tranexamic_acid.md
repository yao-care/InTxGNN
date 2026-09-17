---
layout: default
title: Tranexamic Acid
parent: Model Prediction Only (L5)
nav_order: 847
evidence_level: L5
indication_count: 1
---

# Tranexamic Acid
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

# Tranexamic Acid: From Bleeding Control to Amenorrhea

## One-Sentence Summary

> Tranexamic acid is an antifibrinolytic agent traditionally used to reduce excessive bleeding (e.g., menorrhagia, trauma-related and surgical hemorrhage).
> The TxGNN model predicts a possible association with **Amenorrhea (disease)**,
> but this prediction is currently supported only by **2 review-type publications** and **no clinical trials**, and the underlying rationale raises concerns about a possible knowledge-graph semantic artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in regulatory data; drug class is used to reduce bleeding (e.g., menorrhagia, trauma/surgical hemorrhage) |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the evidence pack (MOA marked as a data gap). Based on known pharmacology, tranexamic acid is an antifibrinolytic agent that inhibits the conversion of plasminogen to plasmin, thereby reducing fibrin degradation and limiting bleeding. It is used clinically to reduce excessive bleeding, such as menorrhagia, trauma-related hemorrhage, and surgical blood loss.

This mechanism points in the **opposite direction** from the predicted indication. Amenorrhea (disease) refers to the *absence* of menstruation, whereas tranexamic acid is a hemostatic (bleeding-reduction) agent, not an agent that induces or treats absence of menstrual bleeding. The two supporting publications actually discuss (1) pharmacological management of abnormal uterine *bleeding*, and (2) menses *prophylaxis and suppression* in hematologic cancer patients — the latter concerning deliberately induced amenorrhea (e.g., via hormonal therapy) as a management goal, with tranexamic acid appearing only as an adjunct for breakthrough bleeding, not as a treatment for amenorrhea itself.

Given this mismatch, the very high TxGNN score (99.19%) most plausibly reflects a **semantic confusion artifact** in the knowledge graph — conflating "menstrual suppression / induced amenorrhea" with the disease entity "amenorrhea" — rather than a genuine pharmacological signal. This prediction requires manual clarification before it can be considered a credible repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Review | Menopause (New York, N.Y.) | Evidence-based review of pharmacological therapy for abnormal uterine *bleeding*; discusses agent selection by etiology, bleeding amount, and patient status — not amenorrhea treatment. |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Review | Journal of Oncology Pharmacy Practice | Systematic approach to menses prophylaxis and *suppression* (i.e., induced amenorrhea) in pre-menopausal hematologic cancer patients; TXA discussed as adjunct for breakthrough bleeding management, not as a primary amenorrhea therapy. |

---

## India Market Information

Currently not marketed in India; no registration records available (0 licenses on file).

---

## Safety Considerations

- **Drug Interactions**: 35 documented interactions identified. Notable patterns:
  - **Major** — Concomitant use with estrogen-containing hormonal therapies (e.g., Ethinylestradiol, Estradiol, Conjugated estrogens, Norethisterone, Drospirenone, Diethylstilbestrol, Etonogestrel, and related topical/oral estrogen formulations) due to additive prothrombotic/thromboembolic risk.
  - **Major** — Concomitant use with procoagulant blood products (e.g., Factor IX Complex (Human), Anti-inhibitor coagulant complex) and Carfilzomib, due to increased thrombotic risk.
  - **Moderate** — Concomitant use with thrombolytic agents (e.g., Alteplase, Anistreplase), due to pharmacologically antagonistic (antifibrinolytic vs. fibrinolytic) effects.

Detailed prescribing warnings and contraindications are not currently available and require TFDA/package insert data before clinical use decisions can be made.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale itself suggests the high TxGNN score is likely a knowledge-graph artifact confusing "induced/suppressed menstruation" with the disease "amenorrhea," rather than genuine pharmacological plausibility. Evidence is limited to two review articles with no supporting clinical trials, and no regulatory or MOA data is currently available to support a safety assessment.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications (currently a Blocking data gap — required for S1 safety screening)
- Confirmed mechanism of action data from DrugBank
- Manual disease-entity review to confirm whether "amenorrhea (disease)" in the knowledge graph is distinct from "induced/suppressed menstruation," to rule out a semantic mapping error
- If the prediction is confirmed as a genuine signal after entity clarification, primary literature (not just reviews) and ideally clinical trial data before re-evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

