---
layout: default
title: Urofollitropin
parent: 僅模型預測 (L5)
nav_order: 513
evidence_level: L5
indication_count: 10
---

# Urofollitropin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Urofollitropin: From Infertility Treatment to Migraine Disorder

## One-Sentence Summary

Urofollitropin is a purified urinary follicle-stimulating hormone (FSH) preparation, used clinically for ovulation induction in infertility treatment and assisted reproductive technology (ART).
The TxGNN model predicts it may be effective for **Migraine Disorder**, with **0 clinical trials** and **0 relevant publications** currently supporting this direction.
The biological plausibility connecting FSH receptor agonism to migraine pathophysiology is extremely weak, and this prediction is assessed as model-only evidence (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in India regulatory database (known use: infertility / ovulation induction) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in our database. Based on known pharmacological information, Urofollitropin is a purified human FSH preparation. It acts as an FSH receptor (FSHR) agonist, primarily stimulating ovarian granulosa cells to promote follicle development and estrogen biosynthesis, and acting on testicular Sertoli cells to support spermatogenesis. Its established clinical utility is in reproductive endocrinology, not in neurological conditions.

The mechanistic link between FSH receptor agonism and migraine disorder is not supported by current science. Brain astrocytes have been reported to express FSHR, but no mechanistic research demonstrates that FSH modulates migraine-related neurotransmission, cortical spreading depression (CSD), or trigeminovascular activation through this pathway. While menstrual migraine is associated with estrogen fluctuations, FSH's indirect role in promoting estrogen synthesis is far too attenuated to constitute a translational rationale — and this pathway would be entirely absent in male patients or postmenopausal women without ovarian function.

Among all 10 predicted indications in this report, the most biologically plausible candidate is Postural Orthostatic Tachycardia Syndrome (POTS, rank 8): POTS preferentially affects women of reproductive age, FSH receptors have been reported in cardiovascular smooth muscle, and estrogen fluctuations are known to influence vascular tone and autonomic regulation. However, even for POTS, no preclinical animal models or clinical observational data currently exist to validate this hypothesis. All other predictions — including cardiac arrhythmias (His bundle tachycardia, multifocal atrial tachycardia), structural neurological emergencies (cauda equina syndrome), and peripheral vascular disease (Raynaud disease) — have no plausible intersection with FSH receptor pharmacology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **Data Quality Note**: A PubMed query for the related indication "migraine with or without aura, susceptibility to" (rank 9) returned 20 results. Upon review, every paper concerns epilepsy genetics (e.g., SCN1A polymorphisms, MTHFR variants, anti-epileptogenic targets) and was captured due to keyword overlap between migraine–epilepsy comorbidity research. None are relevant to Urofollitropin or FSH receptor biology. These 20 papers are excluded from evidence assessment; the effective literature count remains zero.

---

## India Market Information

Urofollitropin has no registered products in the Indian regulatory (CDSCO) database and is not currently marketed in India. No authorization number, brand name, or approved indication data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note**: The DDInter drug interaction database file was not available at the time of this assessment (data gap DG001). CDSCO package insert warnings and contraindications have not yet been retrieved (data gap DG001, severity: Blocking). Safety screening cannot be completed until these data are obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Urofollitropin are rated L5 (model prediction only), with zero supporting clinical trials or relevant literature across the entire indication set. The predicted conditions — spanning migraine variants, cardiac arrhythmias, neurological emergencies, and vasospastic disease — have no biologically plausible connection to FSH receptor agonism, and the drug is not marketed in India, meaning no local safety or regulatory baseline exists.

**To proceed, the following is needed:**

- Retrieve CDSCO package insert (or international equivalents, e.g., USFDA label for Bravelle/Fertinex) to complete safety screening — currently a **Blocking** data gap
- Obtain MOA data from DrugBank API (DB00094) to enable formal mechanism-of-action analysis
- Restore the DDInter database file (`ddinter_code_A.csv`) to enable drug interaction screening
- For any indication to advance to S1 evaluation, at minimum L4 evidence (preclinical in vitro/in vivo studies) must be identified — specifically: FSHR expression studies in target tissues, and functional data linking FSH signalling to disease-relevant pathways
- If further exploration is warranted, POTS (rank 8) is the recommended priority indication for a focused literature search, given it has the highest biological plausibility of the batch (FSHR in vascular smooth muscle; female sex hormone–autonomic interaction)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

