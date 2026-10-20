---
layout: default
title: Loperamide
parent: Model Prediction Only (L5)
nav_order: 499
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Loperamide: predicted new indication Acute contagious conjunctivitis (evidence level L5). Approved use: Diarrheal disease, dysentery"
monitor_inn: "Loperamide"
predicted_indications: ["acute contagious conjunctivitis", "amebic dysentery", "conjunctivitis", "gastroduodenitis", "pseudomembranous conjunctivitis", "parasitic conjunctivitis", "chronic follicular conjunctivitis", "conjunctival folliculosis", "serous conjunctivitis except viral", "Angelucci syndrome"]
---

# Loperamide
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

# Loperamide: From Diarrheal Disease to Acute Contagious Conjunctivitis

## One-Sentence Summary

Loperamide is a peripherally acting anti-diarrheal drug, originally used to treat diarrheal disease and dysentery.
The TxGNN model predicts it may be effective for **acute contagious conjunctivitis**, but this is a model-only prediction with **0 clinical trials** and **0 publications** supporting it.
The prediction has no plausible biological rationale and should be treated with strong caution.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diarrheal disease, dysentery |
| Predicted New Indication | Acute contagious conjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, loperamide is a peripheral mu-opioid receptor agonist that acts on gut myenteric neurons to reduce motility and secretion. Its CNS penetration is limited by P-glycoprotein efflux.

The original indications (diarrheal disease, dysentery) are gastrointestinal, while the predicted indication is an eye infection. No mechanistic link was identified: loperamide has no known antimicrobial or anti-inflammatory activity on the ocular surface, and neither systemic nor topical ocular delivery is established.

The very high score (0.9997) appears to be a graph-based artifact. Several other conjunctivitis subtypes received nearly identical scores (for example conjunctivitis, pseudomembranous conjunctivitis, parasitic conjunctivitis and chronic follicular conjunctivitis), which suggests the signal comes from shared neighbours in the knowledge graph rather than disease-specific biology. Among the other top-10 predictions, the closest to the original use is amebic dysentery, but the available literature points toward harm rather than benefit (see Safety Considerations).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for acute contagious conjunctivitis.

---

## India Market Information

Loperamide is marketed in India as an oral single-ingredient product, with 20 valid registrations and none cancelled. Approved indication text is not available for these registrations. The main authorizations are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 107712 | Imodium Capsule (Janssen Pharmaceuticals) | Strip of 4 capsules | Not specified |
| 122803 | Lopidus Capsule (Zydus Healthcare Limited) | Strip of 10 capsules | Not specified |
| 121870 | Loramyl 2mg Tablet (Adonis Laboratories Pvt Ltd) | Strip of 10 tablets | Not specified |
| 184200 | Ridol 2mg Tablet (Gufic Bioscience Ltd) | Strip of 10 tablets | Not specified |
| 125941 | Lomid M Syrup (Agron Remedies Pvt Ltd) | Bottle of 30 ml syrup | Not specified |

No ophthalmic formulation is registered.

---

## Safety Considerations

- **Contraindications (from knowledge-graph disease associations, not label text)**: liver disease, gallbladder disease, paralytic ileus, intestinal obstruction, familial visceral myopathy, dysentery, infectious diarrheal disease, intestinal infectious disease.
- **Drug Interactions**: 591 interactions are recorded. Examples classed as Major: abiraterone, ranitidine, fosamprenavir, gemfibrozil. Examples classed as Moderate: codeine, dihydrocodeine, tramadol, chlorpheniramine, cetirizine, ethanol, salbutamol.
- **Safety signals in the literature**:
  - A case report describes fulminant amoebic colitis (toxic megacolon) after heavy loperamide use, consistent with the known caution against antimotility agents in invasive dysentery.
  - A 2026 case report describes loperamide-induced respiratory depression in a patient with severe chemotherapy-related gastrointestinal inflammation. Impaired mucosal barrier or efflux may raise systemic exposure.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for acute contagious conjunctivitis rests on a model score alone (L5), with no trials, no literature and no plausible mechanism. The related predictions in the top 10 are either equally unsupported or carry safety signals.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis for ocular activity, plus evidence of an ocular delivery route (none exists today)
- Preclinical studies in ocular infection or inflammation models
- Mechanism of action data and package insert warnings and contraindications for the India registrations
- Re-evaluation of the model prediction for graph-propagation artifacts, given the identical scores across conjunctivitis subtypes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

