---
layout: default
title: Isoniazid
parent: Model Prediction Only (L5)
nav_order: 449
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Isoniazid: predicted new indication Conjunctivitis (evidence level L4). Approved use: Pulmonary tuberculosis"
monitor_inn: "Isoniazid"
predicted_indications: ["conjunctivitis"]
---

# Isoniazid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Isoniazid: From Pulmonary Tuberculosis to Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Isoniazid is an anti-tubercular drug, originally used to treat pulmonary tuberculosis.
The TxGNN model predicts it may be effective for **conjunctivitis**, but there are **no registered clinical trials** and the **12 publications** retrieved are mostly case reports, reviews, or off-topic papers, so evidence is weak and the prediction is essentially model-only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 0.9936 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Isoniazid is a well-established anti-tubercular agent. It is generally understood to act by inhibiting mycolic acid synthesis in *Mycobacterium tuberculosis* (via InhA), but this was not confirmed in the compiled data.

There is no direct mechanistic support for using isoniazid against common bacterial or viral conjunctivitis. The only plausible link is narrow and tuberculosis-related:
- **Conjunctival tuberculosis** is a true mycobacterial infection, where anti-tubercular therapy may be relevant.
- **Phlyctenular keratoconjunctivitis** is a hypersensitivity reaction to mycobacterial antigens, often seen in patients with TB exposure.

The high TxGNN score is a model prediction and likely reflects these TB-associated eye diseases rather than conjunctivitis in general. Several retrieved publications concern drug-induced ocular side effects, BCG-related reactive arthritis, or unrelated topics, and do not support efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The publications most relevant to TB-related eye disease are listed below. All are old or low-level evidence (case reports, case series, field studies), and none demonstrates efficacy in general conjunctivitis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Cohort/Field prophylaxis study | Am Rev Respir Dis | Isoniazid prophylaxis for phlyctenular keratoconjunctivitis among Eskimos in southwestern Alaska (no abstract available) |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case report | Medicine | Pediatric phlyctenular keratoconjunctivitis associated with primary sinonasal tuberculosis; TB is a common cause in high-endemic areas |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Not classified | Oftalmologia | 28 cases of tuberculous keratoconjunctivitis, 13 in children with primary TB; all had positive tuberculin tests |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case report | Arch Ophthalmol | Primary tuberculosis of the conjunctiva (no abstract available) |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Not classified | Ann Oculist | Local isoniazid use in ocular tuberculosis (no abstract available) |
| [10084171](https://pubmed.ncbi.nlm.nih.gov/10084171/) | 1999 | Case report | Rev Rhum (Engl Ed) | Isoniazid used for refractory arthropathy after intravesical BCG therapy; not an eye indication |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optom Clin | Ocular side effects of systemic drugs, including drug-associated conjunctivitis; not evidence of benefit |

## India Market Information

Isoniazid is marketed in India with 20 valid registrations, all as single-entry records (mostly fixed-dose combination anti-tubercular products). The data compiled for this report contain no approved indication text. Examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 224928 | Tibizim Forte Tablet | Strip of 10 tablets | Not available |
| 192406 | RF 3 150 mg/100 mg/500 mg Tablet | Strip of 10 tablets | Not available |
| 209857 | Scc JR Plus 150 mg/75 mg/400 mg Tablet | Strip of 10 tablets | Not available |
| 42286 | CAVICIN E KIT | Packet of 1 kit | Not available |
| 253567 | Zyrifa Capsule | Strip of 10 capsules | Not available |

All marketed forms are oral tablets, capsules, or kits. No ophthalmic formulation is registered, so the route needed for conjunctivitis is not currently available.

## Safety Considerations

- **Contraindications / risk conditions (from the knowledge graph, not label text):** liver failure, acute liver failure, liver disease, hepatitis, porphyria (including inherited porphyria and porphyrin metabolism disease), gallbladder disease, diabetes mellitus, diabetic ketoacidosis, gout, peripheral neuropathy and other peripheral nervous system disease, substance abuse/dependence, and slow acetylator status.
- **Drug interactions:** 242 interactions were identified. Examples include moderate interactions with antidiabetic agents (acarbose, alogliptin, metformin, pioglitazone, canagliflozin, dapagliflozin, chlorpropamide, albiglutide), metronidazole, budesonide, vitamin D analogues (cholecalciferol, calcifediol, calcitriol), and alosetron. Minor interactions include corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone).

Please refer to the package insert for full warnings, as label-based safety data were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but it is model-based only: there are no registered trials, and the literature is limited to old case reports and field studies on TB-related eye disease. Isoniazid is not supported for general conjunctivitis, and no ophthalmic formulation exists in India.

**To proceed, the following is needed:**
- Narrow the indication to TB-associated ocular disease (phlyctenular keratoconjunctivitis, conjunctival tuberculosis) and assess it as a distinct question
- Obtain mechanism of action data and the package insert warnings and contraindications
- Review controlled evidence for isoniazid in TB-related eye disease, and confirm whether systemic anti-tubercular therapy is already standard care
- Evaluate route and formulation feasibility, since no ophthalmic product is registered
- Assess the hepatotoxicity and neuropathy risk against the expected benefit in this population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

