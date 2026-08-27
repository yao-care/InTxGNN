---
layout: default
title: Netarsudil
parent: 僅模型預測 (L5)
nav_order: 480
evidence_level: L5
indication_count: 2
---

# Netarsudil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Netarsudil: From Glaucoma/Ocular Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Netarsudil (Rhopressa®) is a Rho-associated protein kinase (ROCK) inhibitor, FDA-approved since December 2017 for the treatment of open-angle glaucoma and ocular hypertension, acting through a novel triple mechanism involving trabecular outflow enhancement, aqueous humor production reduction, and episcleral venous pressure lowering.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma** — a genetically defined subtype encompassing mutations in *MYOC*, *OPTN*, and related genes — with **1 tangentially related clinical trial** (Grade C, not specific to the hereditary subtype) and **no direct publications** currently available for this specific indication.
The mechanistic basis is theoretically sound given that IOP control remains the primary treatment goal in hereditary forms, but the absence of subgroup-specific clinical evidence places the evidence at **Level 4**, warranting a Hold decision pending dedicated studies.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma and ocular hypertension (U.S. FDA-approved December 2017; not registered in India) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Netarsudil operates through three convergent pharmacological mechanisms that collectively reduce intraocular pressure (IOP): **(1) ROCK1/ROCK2 inhibition** — by dephosphorylating contractile proteins in the trabecular meshwork, netarsudil reduces outflow resistance and enhances aqueous drainage through the conventional pathway, the primary route responsible for most IOP regulation; **(2) Norepinephrine transporter (NET) inhibition** — blocking norepinephrine reuptake in the ciliary body modulates adrenergic tone and reduces aqueous humor production; **(3) Episcleral venous pressure reduction** — an experimentally demonstrated downstream effect that further facilitates aqueous outflow. This triple convergence on IOP-regulatory nodes gives netarsudil a mechanistic profile distinct from prostaglandin analogues or beta-blockers, and one directly aligned with the core pathophysiology of glaucoma.

Primary hereditary glaucoma encompasses genetically determined glaucoma forms, including juvenile open-angle glaucoma caused by *MYOC* mutations (~3% of adult POAG), *OPTN*-linked normal-tension glaucoma, and *NTF4*/*TBK1*-associated forms. Despite their different genetic origins, the shared pathological endpoint — elevated IOP and progressive optic nerve damage — is identical to common sporadic open-angle glaucoma. IOP reduction is the only proven disease-modifying intervention regardless of genetic etiology. Where hereditary mutations (particularly *MYOC*) cause trabecular meshwork dysfunction leading to elevated IOP, ROCK inhibition targets that dysfunction directly, making the mechanistic extrapolation from general POAG to hereditary POAG both logical and biologically plausible.

Importantly, the TxGNN model independently ranked general "glaucoma" as the Rank 2 prediction for netarsudil (score 99.47%), a direction supported by an extensive evidence base: multiple completed Phase 3 RCTs (ROCKET-2 n=708, MERCURY-3 n=436, J-ROCKET n=245), a meta-analysis of RCTs, and over 20 publications, together achieving an L1 evidence level with a "Proceed with Guardrails" recommendation. This corroborates the model's confidence in the ROCK-inhibition → IOP-lowering → glaucoma treatment axis. The prediction for primary hereditary glaucoma should therefore be interpreted as a mechanistic extension to an unstudied genetic subpopulation, rather than a novel therapeutic direction with independent evidence. The key unanswered question is not whether ROCK inhibition works for IOP, but whether patients with specific hereditary mutations respond equivalently to sporadic POAG patients.

---

## Clinical Trial Evidence

No clinical trials specifically targeting **Primary Hereditary Glaucoma** were identified. The following trial was retrieved by the evidence collection system but carries only indirect relevance:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT06969586](https://clinicaltrials.gov/study/NCT06969586) | N/A (Observational) | Enrolling by Invitation | 50 | Evaluates whether topical ROCK inhibitors reduce loss of corneal endothelial cells after cataract surgery in patients with **Fuchs endothelial corneal dystrophy** co-occurring with glaucoma. Fuchs dystrophy is a distinct hereditary eye condition; this trial does not address IOP management or primary hereditary glaucoma treatment. Grade C relevance — should not be counted as supporting evidence for the hereditary glaucoma indication. |

---

## Literature Evidence

Currently no literature directly supporting Netarsudil in **Primary Hereditary Glaucoma** is available.

---

## India Market Information

Netarsudil is not registered or marketed in India. No product authorizations are on record (0 registrations).

---

## Safety Considerations

Please refer to the package insert for safety information.

**Known pharmacological targets (from drug interaction database):**
- **ROCK1** (gene: *ROCK1*, ENSG00000067900): Primary target; mediates trabecular meshwork relaxation. The S-enantiomer racemate has a Ki of 4.2 nM vs. ROCK2.
- **ROCK2** (gene: *ROCK2*, ENSG00000134318): Co-primary target; in a kinase screening panel at 0.5 μM, netarsudil inhibited 11 kinases by >90%, with ROCK1, ROCK2, PKCδ, and PKCη identified as the four relevant targets for IOP lowering.

At high concentrations (10 μM), netarsudil also inhibits the norepinephrine transporter (NET, 96%) and serotonin transporter (SERT, 94%); however, these effects are considered secondary at clinical ophthalmic doses (0.02% topical solution). No formal drug-drug interaction warnings are currently available for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the ROCK-inhibiting mechanism of netarsudil is directly applicable to IOP-driven primary hereditary glaucoma — and the drug carries strong Phase 3 evidence in the broader glaucoma population — no clinical trial or publication has specifically studied this genetically defined subgroup. The TxGNN prediction reflects mechanistic plausibility and disease proximity rather than an independent evidence base for the hereditary subtype.

**To proceed, the following is needed:**

- **Retrospective subgroup analysis**: Mine existing ROCKET/MERCURY Phase 3 trial datasets to identify efficacy and safety signals in patients with family history or genetically confirmed hereditary glaucoma
- **Prospective registry or dedicated RCT**: Enroll genetically confirmed primary hereditary glaucoma patients (*MYOC*, *OPTN*, *NTF4* mutation-positive) to directly evaluate IOP response to netarsudil
- **Mechanistic studies**: Examine whether trabecular meshwork cells derived from hereditary glaucoma donors (particularly MYOC-mutant) respond to ROCK inhibition comparably to sporadic POAG cells
- **India regulatory pathway**: As the drug is not marketed in India (0 registrations), a market authorization pathway must be established before any local clinical research or use can proceed
- **Safety data gap remediation** (DG001): Obtain and parse the official package insert from a country with current approval (U.S./EU/Japan) to complete the blocking safety evaluation
- **MOA data gap remediation** (DG002): Retrieve complete mechanism of action annotation from DrugBank (DB13931) to support a rigorous mechanistic rationale document
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

