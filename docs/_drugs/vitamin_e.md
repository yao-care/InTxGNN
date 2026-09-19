---
layout: default
title: Vitamin E
parent: Model Prediction Only (L5)
nav_order: 886
evidence_level: L5
indication_count: 10
---

# Vitamin E
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

# Vitamin E: From Vitamin Supplementation Indication to Inborn Disorder of Bilirubin Metabolism

## One-Sentence Summary

Vitamin E is a fat-soluble antioxidant nutrient for which no approved drug license or clearly defined approved indication has been identified in Taiwan. The TxGNN model predicts that it may have potential benefit for **inborn disorder of bilirubin metabolism**, but currently only **3 clinical trials** (none directly testing Vitamin E in this disease) and **2 publications** (both Tier 3 reviews/case reports) provide support, indicating weak evidence strength.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No data found (Taiwan Not marketed; no approved indication text) |
| Predicted New Indication | Inborn Disorder of Bilirubin Metabolism |
| TxGNN Prediction Score | 99.99% (rank 522) |
| Evidence Level | L4 (mechanism/preclinical level) |
| Taiwan Market Status | Not marketed |
| Number of Drug Licenses | 0 |
| Recommended Decision | **Hold (deferred)** |

---

## Why is This Prediction Reasonable?

Currently **no detailed Vitamin E mechanism of action (MOA) data is available** (DG002, High severity gap). Based on existing public information, Vitamin E is a fat-soluble antioxidant vitamin whose efficacy in "Vitamin E deficiency" has been established; mechanistically, as a free radical scavenger, it could theoretically reduce lipid peroxidation and lower oxidative stress, thus being linked by the model to hepatobiliary metabolism-related diseases.

However, in inborn disorders of bilirubin metabolism (such as Crigler-Najjar syndrome, progressive familial intrahepatic cholestasis, etc.), the core pathophysiology is **primary genetic defects of bilirubin-synthesizing enzymes or transport proteins**, not oxidative stress-driven disease. Literature and trial evidence show that such patients frequently present with malabsorption of fat-soluble vitamins (including Vitamin E), so clinical Vitamin E supplementation typically aims to "correct secondary deficiency" rather than "treat primary metabolic defects." The 3 listed clinical trials are also not designed to directly test Vitamin E intervention in this disease; the associations are indirect and the mechanistic reasoning awaits validation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|--------------|-------|--------|------------|--------------|
| [NCT06465810](https://clinicaltrials.gov/study/NCT06465810) | N/A | Recruiting | 1,850 | International ATTR amyloidosis real-world registry study, encompassing a cohort with bilirubin metabolism disease, but not specifically testing Vitamin E intervention (relevance grade B) |
| [NCT01556906](https://clinicaltrials.gov/study/NCT01556906) | Phase 2 | Completed | 6 | Dose-escalation trial of MTP inhibitor lomitapide in homozygous familial hypercholesterolemia; investigational drug is not Vitamin E, only indirectly related (relevance grade C) |
| [NCT03115086](https://clinicaltrials.gov/study/NCT03115086) | N/A | Active, not recruiting | 55 | Post-marketing patient registry for Cholbam (cholic acid), collecting disease natural history data; not a drug intervention trial (relevance grade B) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [7915305](https://pubmed.ncbi.nlm.nih.gov/7915305/) | 1994 | Case report/Review | The Journal of Pediatrics | Describes a novel disease cause (3β-hydroxy-C27-steroid dehydrogenase/isomerase deficiency) leading to progressive familial intrahepatic cholestasis; this is a disease mechanistic descriptive publication, not a Vitamin E intervention study |
| [803225](https://pubmed.ncbi.nlm.nih.gov/803225/) | 1975 | Review | The New England Journal of Medicine | Review of unconjugated hyperbilirubinemia in newborns; no abstract available; no direct association with Vitamin E treatment |

---

## Taiwan Market Information

No approved drug license data currently identified in Taiwan (market status: Not marketed; registration count: 0; no permit/indication text available for display).

---

## Safety Considerations

**Drug Interactions** (source: DDInter; 173 interaction records identified total; excerpted below):

- **Moderate grade** (warrant attention; predominantly related to anticoagulation/antiplatelet agents and mineral absorption): Acetylsalicylic acid, Iron, Iron sucrose, Sevelamer, Abciximab, Antithrombin III human, Apixaban, Dipyridamole, Betrixaban, Bivalirudin, Cangrelor, Caplacizumab — high-dose Vitamin E could theoretically potentiate the bleeding risk of anticoagulant/antiplatelet drugs and may produce absorption-level interactions with iron products/phosphate binders.
- **Minor grade**: Hydrocortisone, Triamcinolone, Dexamethasone, Betamethasone, Budesonide, Orlistat, Prednisone, Prednisolone.

⚠️ Due to **missing product information warnings and contraindication data** (DG001, Blocking severity), a comprehensive safety initial assessment cannot be completed, which is a blocking gap for proceeding to the next phase.

---

## Conclusion and Next Steps

**Decision: Hold (deferred)**

**Rationale:**
- The top-ranked predicted indication (inborn disorder of bilirubin metabolism) achieves only L4 (mechanism/preclinical) evidence level; the 3 existing trials are not designed to directly test Vitamin E in this disease, and the 2 publications are merely descriptive reviews/case reports, insufficient to support progression to the next stage of safety assessment.
- Missing product information warnings and contraindication data constitute a Blocking-level gap; per protocol, S1 safety initial assessment cannot be completed.

**To proceed further, the following must be completed:**
- TFDA product information warnings and contraindication data (download and parse official product information PDF)
- Complete Vitamin E mechanism of action (MOA) data (query the DrugBank API)
- Direct intervention human trial evidence for inborn disorder of bilirubin metabolism

**Note:** In the same Evidence Pack, the second-ranked indication "bilirubin metabolism disease (broad sense bilirubin metabolism disease, including NAFLD/NASH-related hepatic dysfunction)" achieves **L2** evidence level, supported by one completed Phase 4 head-to-head RCT (Vitamin E vs UDCA vs pentoxifylline, n=102) and multiple observational cohorts; evaluation of the feasibility of advancing this indication is recommended as a separate agenda item.

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

