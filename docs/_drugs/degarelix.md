---
layout: default
title: Degarelix
parent: Model Prediction Only (L5)
nav_order: 240
evidence_level: L5
indication_count: 10
---

# Degarelix
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

# Degarelix: From Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Degarelix is a GnRH receptor antagonist marketed in India as an injectable. The data compiled for this report do not list an approved indication text for it. The TxGNN model predicts it may be effective for **hypertrichosis**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India license data (see note below) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 13 |
| Recommended Decision | Hold |

Note: the license records contain no approved-indication text. Degarelix is generally known as a GnRH antagonist used in androgen-deprivation therapy for advanced prostate cancer, but this is background knowledge and is not confirmed by the data compiled for this report.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, degarelix is a GnRH receptor antagonist. It suppresses LH and FSH and thereby lowers gonadal androgen production.

The link to hypertrichosis is weak. Hypertrichosis is generally non-androgen-dependent hair overgrowth, so suppressing androgens has no clear mechanistic rationale. The very high TxGNN score is a graph-based prediction and is not backed by any clinical or literature evidence. It likely reflects proximity to hair-phenotype nodes in the knowledge graph.

The other top predictions share this problem. Most are hair, congenital malformation or urticaria conditions with no plausible GnRH link. Two reproductive endocrine candidates are more biologically adjacent:
- **Central precocious puberty** (score 99.67%): GnRH-dependent, so antagonism is mechanistically plausible. However, GnRH agonists are already the standard of care, degarelix is unstudied in children, and there is no evidence in the data.
- **Familial male-limited precocious puberty** (score 99.84%): caused by activating LHCGR mutations that act independent of GnRH, so efficacy is doubtful.

These two are flagged as research questions rather than holds.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Thirteen valid single-ingredient registrations exist. The main ones are listed below. No approved-indication text is recorded for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 85113 | Firmagon 120mg Injection | Vial of 1 injection | Ferring Pharmaceuticals |
| 84652 | Firmagon 80mg Injection | Vial of 1 injection | Ferring Pharmaceuticals |
| 63578 | Degrinta 120mg Injection | Vial of 1 injection | Intas Pharmaceuticals Ltd |
| 60011 | Degapride 80mg Injection | Vial of 1 injection | Sun Pharmaceutical Industries Ltd |
| 61482 | Deghor 120 Injection | Vial of 1 injection | Glenmark Pharmaceuticals Ltd |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (GnRH antagonist), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Contraindications (knowledge-graph signals, not label text)**: long QT syndrome, familial long QT syndrome, torsades de pointes, liver disease, gallbladder disease, potassium deficiency disease.
- **Drug Interactions**: 217 interactions were found in total. The 20 retrieved include:
  - **Major**: cisapride and dolasetron, both relevant to QT prolongation.
  - **Moderate**: clarithromycin, levofloxacin, ondansetron, granisetron, palonosetron, famotidine, loperamide, and several laxatives and bowel-preparation agents (bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes, lactulose, lactitol, magnesium citrate, magnesium hydroxide, castor oil, glycerin, mineral oil).
  - **Minor**: metronidazole.
- **Hypersensitivity**: injection-site reactions and rare hypersensitivity are known with degarelix. This argues for caution in allergic conditions such as urticaria.

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predictions are supported only by the TxGNN graph score, with no clinical trials or literature. Most have no plausible mechanistic link to GnRH antagonism. Central precocious puberty is the only biologically plausible candidate, and it already has an established GnRH agonist standard of care.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India Pharma source (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for the India registrations, to confirm the original indication
- For central precocious puberty, a focused literature and trial search, plus an assessment of pediatric safety and of advantages over GnRH agonists
- A QT-risk review, given the knowledge-graph contraindication signals and the major QT-related interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

