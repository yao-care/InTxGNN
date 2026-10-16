---
layout: default
title: Diphenhydramine
parent: Model Prediction Only (L5)
nav_order: 275
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Diphenhydramine: predicted new indication Rosacea conjunctivitis (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, atopic conjunctivitis…"
---

# Diphenhydramine
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

# Diphenhydramine: From Allergic Rhinitis and Conjunctivitis to Rosacea Conjunctivitis

## One-Sentence Summary

Diphenhydramine is a first-generation antihistamine, originally used for allergic rhinitis, vasomotor rhinitis, several forms of allergic conjunctivitis (atopic, papillary, vernal) and insomnia.
The TxGNN model predicts it may be effective for **rosacea conjunctivitis**, but **no clinical trials and no publications** were identified to support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis, insomnia (no approved-indication text is available in the India licence records, so these come from the knowledge graph) |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on well-established pharmacology, diphenhydramine is a first-generation H1 histamine receptor antagonist with additional mild anticholinergic and local anaesthetic effects. It is already used for allergic conjunctivitis and rhinitis, where it relieves itching and redness by blocking histamine.

The plausible link to rosacea conjunctivitis is symptomatic relief of ocular itching and hyperaemia through H1 blockade. However, rosacea-associated eye disease is driven mainly by meibomian gland dysfunction, tear film instability, Demodex or bacterial colonisation, and neurovascular and innate-immune dysregulation (for example MMPs, IL-1 and TNF). Histamine plays a minor or unproven role in these processes.

The high TxGNN score most likely reflects network proximity to other conjunctivitis indications rather than disease-specific mechanistic evidence. The prediction should therefore be treated as a hypothesis, not a supported finding.

## India Market Information

Diphenhydramine is marketed in India with 20 valid single-ingredient registrations and no cancelled ones. Approved-indication text is not recorded for these registrations. The main authorisations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 28971 | Benacof 25mg Soft Gelatin Capsule | Strip of 10 soft gelatin capsules | Not recorded |
| 145847 | Matdryl Syrup | Bottle of 100 ml syrup | Not recorded |
| 21615 | Aden-Rex Syrup | Bottle of 100 ml syrup | Not recorded |
| 154621 | Novadryl 25mg Capsule | Strip of 10 capsules | Not recorded |
| 247305 | Zendryl 25mg Capsule | Strip of 10 capsules | Not recorded |

The registered products are oral forms (capsules, tablets, dispersible tablets) and liquids (syrups, expectorant). No ophthalmic formulation appears among them, which matters for an eye-surface indication.

## Safety Considerations

**Drug Interactions:** The interaction screening found 394 interacting drugs. Examples include:
- **Major:** potassium citrate, eliglustat
- **Moderate:** anticholinergics (hyoscyamine, atropine, glycopyrronium, dicyclomine, clidinium, methscopolamine, mepenzolate), opioids and related agents (morphine, loperamide, eluxadoline), and other agents (bupropion, lorcaserin, dronabinol, nabilone, metoclopramide, glycerol phenylbutyrate)

Many of the moderate interactions involve additive anticholinergic or central nervous system depressant effects.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (Evidence Level L5), and the biology of rosacea eye disease does not clearly involve histamine. The model score alone is not enough to justify moving forward.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently missing, and a blocker for safety screening)
- Detailed mechanism of action data from DrugBank
- A literature and trial search specific to antihistamines in ocular rosacea or meibomian gland dysfunction
- Assessment of route compatibility, since no ophthalmic diphenhydramine product is registered in India
- Preclinical or small exploratory evidence that H1 blockade improves rosacea-related ocular symptoms
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

