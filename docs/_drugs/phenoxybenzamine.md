---
layout: default
title: Phenoxybenzamine
parent: Model Prediction Only (L5)
nav_order: 663
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
description: "Phenoxybenzamine: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Adrenal gland pheochromocytoma (also listed: phaeochromocytoma…"
monitor_inn: "Phenoxybenzamine"
predicted_indications: ["primary hereditary glaucoma", "open-angle glaucoma"]
---

# Phenoxybenzamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Phenoxybenzamine: From Pheochromocytoma to Primary Hereditary Glaucoma
{: .text-alpha }

## One-Sentence Summary

Phenoxybenzamine is an alpha-adrenergic blocker originally used for pheochromocytoma and related neuroendocrine or adrenal tumours.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma** (with open-angle glaucoma as a second prediction), but **no clinical trials and no publications** currently support this direction. The prediction is based on computational modelling only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adrenal gland pheochromocytoma (also listed: phaeochromocytoma, sympathetic paraganglioma, adrenal gland cancer, duodenum cancer, small intestine cancer, heart cancer). The approved indication text on the India licences is blank. |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 0.9955 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (4 of 4) – CDSCO approval status is not included in this data |
| Number of Listed Products | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Phenoxybenzamine is an irreversible, non-selective alpha-adrenergic antagonist. According to the Clinical Pharmacology section of the US FDA-approved prescribing information for phenoxybenzamine: "Phenoxybenzamine hydrochloride is a long-acting, adrenergic, alpha -receptor-blocking agent, which can produce and maintain “chemical sympathectomy” by oral administration. It increases blood flow to the skin, mucosa and abdominal viscera, and lowers both supine and erect blood pressures." ([DailyMed: phenoxybenzamine hydrochloride prescribing information, Amneal Pharmaceuticals NY LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0be6a394-cd10-42fc-97cf-ad53d81d8d93), label version 2026-07-03; accessed 2026-11-19.) This description comes from general pharmacological knowledge. It is used in pheochromocytoma to control the effects of excess catecholamines, such as high blood pressure.

A theoretical link to glaucoma is that alpha-adrenergic blockade could lower intraocular pressure, either by reducing aqueous humour production or by changing outflow, or by modulating ocular vascular tone. This is the only rationale available, and it has not been verified.

There are important reasons for caution:
- Primary hereditary glaucoma is mainly driven by genetic defects in the trabecular meshwork or anterior segment development (for example MYOC, CYP1B1). Alpha-blockade is unlikely to address these.
- The original indication (a catecholamine-secreting tumour) is biologically unrelated to glaucoma. The prediction rests on a model score, not on a shared disease mechanism.
- Systemic alpha-blockade carries risks such as orthostatic hypotension, reflex tachycardia, nasal congestion and miosis.
- The second prediction, **open-angle glaucoma** (score 0.9948), has the same limitations. Established glaucoma treatments already exist (prostaglandin analogues, beta-blockers, alpha-2 agonists, carbonic anhydrase inhibitors). Any benefit of an irreversible systemic alpha-antagonist would need to be shown against its safety concerns, and topical or ocular-targeted delivery would likely be required.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 29256 | Biophenox 50mg Injection | Vial of 1 injection | Not specified |
| 85821 | Fenoxene Capsule | Strip of 10 capsules | Not specified |
| 250700 | Zaxyben 50mg Injection | Vial of 1 ml injection | Not specified |
| 86893 | Fenoxene 50mg Injection | Vial of 1 ml injection | Not specified |

All four registrations are valid single-ingredient products. Available routes are injectable and oral. No ophthalmic (topical eye) formulation is registered.

## Safety Considerations

- **Disease contraindications (from the knowledge graph, not label text)**: kidney disease, pyoureter, hypotensive disorder, coronary artery disease.
- **Drug interactions**: 32 interactions were identified in total. All of the 20 listed are of Moderate severity. Main examples:
  - Opioids: morphine, codeine, hydrocodone, opium
  - SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin
  - Prostacyclin-pathway agents: epoprostenol, iloprost, selexipag, treprostinil
  - Cannabinoids: dronabinol, nabilone
  - Others: bupropion, promethazine, amifostine, mepyramine, iobenguane (I-123), nitrous acid

Package insert warnings and contraindications are not available in the data compiled for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a computational basis (L5). There are no clinical trials or publications, the mechanistic link to hereditary glaucoma is weak, and systemic alpha-blockade has notable safety concerns.

**To proceed, the following is needed:**
- A systematic literature search on alpha-blockers and intraocular pressure or glaucoma
- Preclinical assessment, such as IOP effects in animal models
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications from the India regulatory sources, which are needed before any safety screening
- Evaluation of an ocular-targeted (topical) delivery route, since none is currently registered
- A comparison against established glaucoma therapies to show a meaningful benefit

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report, so t" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: phenoxybenzamine hydrochloride prescribing information, Amneal Pharmaceuticals NY LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0be6a394-cd10-42fc-97cf-ad53d81d8d93) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

