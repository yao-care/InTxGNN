---
layout: default
title: Omalizumab
parent: Model Prediction Only (L5)
nav_order: 619
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-04
monitor_inn: "Omalizumab"
predicted_indications: ["bronchitis", "atopic eczema", "dermatitis", "bronchial neoplasm (disease)", "acne keloid", "acrodermatitis chronica atrophicans", "hydroa vacciniforme, familial", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease"]
description: "Omalizumab: predicted new indication Bronchitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Omalizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Omalizumab: Bronchitis
{: .text-alpha }

## One-Sentence Summary

Omalizumab is an anti-IgE monoclonal antibody that is currently marketed in India.
The TxGNN model predicts it may be effective for **bronchitis**, but no published study has tested omalizumab in bronchitis itself.
The two registered trials and the 7 publications linked to this prediction concern other conditions, so the evidence level is **L5**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (4 of 4) – CDSCO approval status is not included in this data |
| Number of Listed Products | 4 (valid: 4) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Omalizumab binds free IgE, the antibody that drives allergic reactions. It also lowers expression of the high-affinity IgE receptor (FcεRI) on mast cells and basophils. Together these effects dampen allergic airway inflammation. Detailed mechanism-of-action data were not available in the data compiled for this report. This description comes from general pharmacology of the antibody and its IgE target.

If a bronchitis case were driven by allergic, IgE-mediated or eosinophilic airway inflammation, anti-IgE therapy could in principle help. That is the only mechanistic link available, and it is indirect.

The supporting material does not address bronchitis itself. The literature covers allergic airway disease, overlap with chronic airway disease in smokers, and general antibody therapy. One of the two linked trials is a small steroid-sparing study in people with persistent airway eosinophilia. The other is a urticaria trial. The high model score therefore reflects a computational prediction, not demonstrated clinical benefit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Completed | 11 | Placebo-controlled test of whether omalizumab allows a lower prednisone dose in patients with persistent eosinophilic bronchitis and asthma. The sample is very small and the condition studied is not clearly bronchitis. |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2 | Completed | 382 | Dose-finding study of an anti-IgE antibody (QGE031) in chronic spontaneous urticaria. It does not test omalizumab in bronchitis. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clin Rev Allergy Immunol | Approval and post-approval experience with omalizumab in persistent allergic airway disease. Bronchitis is not studied. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | Management challenges in smokers whose airway disease includes chronic bronchitis. Drug treatment is uncertain because these patients are excluded from most trials. |
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Cohort | Postepy Dermatol Alergol | Omalizumab in middle-aged or older patients with severe allergic disease overlapping with chronic obstructive lung changes. |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Pooled safety analysis | Curr Med Res Opin | Safety and tolerability of omalizumab in children with allergic (IgE-mediated) airway disease. |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case report | J Investig Allergol Clin Immunol | Rare case of plastic bronchitis after bronchial thermoplasty. It is not a study of omalizumab efficacy. |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui | Preoperative management of patients with bronchial asthma or chronic bronchitis. Omalizumab is mentioned only as one treatment option. |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Review | Allergol Immunopathol | Overview of monoclonal antibodies in pediatrics. Bronchitis is not specifically addressed. |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 162721 | Omalirel Injection (Reliance Life Sciences) | Vial of 1 injection | Not listed |
| 26361 | Bolstran 150mg Injection (Cipla Ltd) | Vial of 2 ml injection | Not listed |
| 243818 | Xolair 150mg Injection (Novartis India Ltd) | Packet of 5 ml injection | Not listed |
| 72758 | Emzumab 150mg Injection (Cipla Ltd) | Vial of 1 injection | Not listed |

All four authorizations are for single-ingredient products and are currently valid.

---

## Safety Considerations

- **Drug Interactions**: 8 interaction records were found.
  - **Moderate**: omacetaxine mepesuccinate.
  - **Minor**: zinc sulfate, zinc acetate, zinc gluconate, zinc chloride, echinacea and vitamin E.
  - **Target record**: the pharmacology data confirm that the drug acts on the IgE heavy chain (IGHE).

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No published study supports omalizumab in bronchitis. The linked trial studied patients with airway eosinophilia and asthma, and the other trial concerns urticaria. The high TxGNN score alone is not enough to move forward.

**To proceed, the following is needed:**
- A clear clinical definition of the bronchitis population that might benefit, such as allergic or eosinophilic bronchitis
- Controlled studies in that population showing a benefit over standard care
- Detailed mechanism-of-action data
- Package insert warnings and contraindications, which are not yet available
- A safety plan covering the moderate interaction with omacetaxine mepesuccinate

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

