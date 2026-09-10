---
layout: default
title: Ropinirole
parent: 僅模型預測 (L5)
nav_order: 746
evidence_level: L5
indication_count: 10
---

# Ropinirole
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

# Ropinirole: From Parkinson's Disease/Restless Legs Syndrome to Attention-Deficit/Hyperactivity Disorder

## One-Sentence Summary

> Ropinirole is a non-ergot dopamine D2/D3 receptor agonist, historically associated with Parkinson's disease and restless legs syndrome (RLS) management based on the supporting literature in this evidence pack.
> The TxGNN model predicts it may be effective for **Attention-Deficit/Hyperactivity Disorder (ADHD)**,
> but this is currently supported only by **0 clinical trials** and **8 publications**, none of which are randomized controlled trials directly testing ropinirole in ADHD.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from registry data (drug is not marketed in India, `total_licenses = 0`). Literature context in this pack references ropinirole's established use in Parkinson's disease and restless legs syndrome. |
| Predicted New Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on the pharmacology referenced in the supporting literature, ropinirole is a non-ergot dopamine D2/D3 receptor agonist, a class conventionally used for Parkinson's disease and RLS.

The link to ADHD is indirect rather than a direct pharmacological rationale. Most of the supporting literature discusses the **comorbidity between RLS and ADHD** rather than ropinirole's action on ADHD's core neurobiology. Only one publication (PMID 15866437) describes a pediatric case in which ropinirole — prescribed to treat RLS/periodic limb movement symptoms in a child who already had ADHD — coincided with improvement in both sleep and ADHD symptoms. This is a single case report, not a controlled study of ropinirole as an ADHD therapy.

Mechanistically, dopaminergic dysregulation is implicated in ADHD pathophysiology (most ADHD drugs, e.g., methylphenidate, act on dopamine/norepinephrine reuptake), so a dopamine agonist is biologically plausible as a candidate. However, the current evidence base does not distinguish whether any benefit is via direct ADHD-relevant circuitry or secondary to RLS symptom relief improving sleep and attention. The mechanistic link should be considered weak and hypothesis-generating only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16218085](https://pubmed.ncbi.nlm.nih.gov/16218085/) | 2005 | Review | Sleep | Reviews the RLS–ADHD association, hypothetical shared mechanisms, and rationale for shared pharmacologic treatment when co-occurring. |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Revue neurologique | General review of RLS pathophysiology and diagnostic criteria; does not directly address ADHD treatment. |
| [15866437](https://pubmed.ncbi.nlm.nih.gov/15866437/) | 2005 | Case Report | Pediatric neurology | 6-year-old with ADHD and comorbid RLS/PLMS treated with ropinirole (for RLS) showed improvement in both RLS symptoms and ADHD symptoms. |
| [30950895](https://pubmed.ncbi.nlm.nih.gov/30950895/) | 2019 | Case Report (unrelated) | Cornea | Describes corneal edema in patients exposed to systemic dopaminergic agents; unrelated to ADHD. |
| [30460371](https://pubmed.ncbi.nlm.nih.gov/30460371/) | 2019 | Case Report (unrelated) | Acta dermato-venereologica | Treatment-induced delusions of infestation linked to elevated brain dopamine; unrelated to ADHD. |
| [24992083](https://pubmed.ncbi.nlm.nih.gov/24992083/) | 2014 | Cohort (unrelated drug) | Clinical neuropharmacology | Compares piribedil vs. pramipexole/ropinirole on vigilance in Parkinson's disease patients with daytime sleepiness; not ADHD-related. |
| [17483695](https://pubmed.ncbi.nlm.nih.gov/17483695/) | 2007 | Preclinical (animal model) | J Neuropathol Exp Neurol | A11-lesioned, iron-deprived mouse model proposed as an RLS model; does not test ropinirole or ADHD endpoints. |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Basic Science | Pharmacological research | Receptor heteromerization study (α2A adrenoceptor/dopamine D4 variants) relevant to ADHD/impulse-control biology, but not a ropinirole efficacy study. |

---

## India Market Information

Currently no registration records available in India — the drug is recorded as **Not Marketed** (`total_licenses = 0`), so no authorization/product/dosage-form entries exist in this evidence pack.

---

## Safety Considerations

**Drug Interactions**: DDI screening identified **167 total interactions**. The interactions flagged at **Moderate** severity include:
- Morphine
- Morphine (liposomal)
- Cimetidine
- Dronabinol
- Nabilone
- Opium
- Obeticholic acid
- Metoclopramide

The remaining flagged interactions (e.g., Calcitriol, Phentermine, Pantoprazole, Glimepiride, Mesalazine, Doxycycline, Clotrimazole, Acarbose, Sucralfate, Palonosetron, Rosiglitazone, Lactulose) are recorded at **Unknown** severity level in the source database and require independent verification before clinical use.

Key warnings and contraindications from the local regulatory label are not currently available (Blocking data gap, DG001 — TFDA/India label PDF not yet retrieved and parsed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The ADHD signal rests on TxGNN's prediction score alone plus a single pediatric case report where ropinirole treated comorbid RLS rather than ADHD directly; there is no clinical trial evidence, and the drug currently has no market presence or registered license in India. This does not meet the bar to proceed even with guardrails.

**To proceed, the following is needed:**
- Resolve Blocking gap DG001: obtain and parse the official label (TFDA or equivalent) for warnings/contraindications — this is required before any S1 safety screening.
- Resolve High-severity gap DG002: confirm ropinirole's formal MOA (D2/D3 agonism) via DrugBank API to support mechanistic review.
- Seek prospective or controlled studies testing ropinirole specifically for ADHD (not RLS-ADHD comorbidity) before advancing past S0.
- Note: within this same evidence pack, the **schizophrenia** candidate (rank 5) has a stronger evidence base (L3, decision_stage S1, "Research Question," including a systematic review/meta-analysis, PMID 31688399) and may warrant separate evaluation as a higher-priority research question relative to the ADHD signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

