---
layout: default
title: Omalizumab
parent: Moderate Evidence (L3-L4)
nav_order: 613
evidence_level: L4
indication_count: 10
---

# Omalizumab
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Omalizumab: From IgE-Mediated Allergic Asthma to Bronchitis

## One-Sentence Summary

Omalizumab is an anti-IgE monoclonal antibody whose established global use is for moderate-to-severe IgE-mediated persistent asthma and chronic spontaneous urticaria; it is not currently marketed in Taiwan. The TxGNN model's top-ranked prediction is **Bronchitis**, but the supporting **2 clinical trials** and **8 publications** overwhelmingly describe asthma or asthma-eosinophilic-bronchitis overlap populations rather than bronchitis as a primary diagnosis, suggesting a possible disease-ontology mapping error rather than a genuine new signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in Taiwan regulatory data (drug is unregistered locally); globally documented use is moderate-to-severe IgE-mediated persistent asthma (per pharmacology reference data in this pack) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.9992% |
| Evidence Level | L4 |
| Taiwan Market Status | Not marketed (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The `original_moa` field in this evidence pack is marked as a data gap. However, the pharmacology reference data embedded in the DDI results describes Omalizumab as a humanized monoclonal antibody that binds the Cε3 domain of immunoglobulin E (IgE), blocking IgE interaction with the high-affinity FcεRI receptor on mast cells and basophils. This anti-IgE mechanism is the pharmacological basis for its approved use in IgE-mediated persistent asthma (moderate-to-severe, inadequately controlled by inhaled corticosteroids) and chronic idiopathic/spontaneous urticaria, with more recent approvals extending to food-allergy risk reduction.

Bronchitis and asthma share overlapping airway inflammation biology, particularly in phenotypes such as eosinophilic bronchitis, so a mechanistic rationale for anti-IgE therapy is plausible in principle. **However, the evidence pack's own relevance grading flags a significant caveat**: the two retrieved trials are graded "C" (only indirectly relevant), and one of them (NCT02049294) actually enrolled asthma patients with eosinophilic bronchitis (n=11) rather than primary bronchitis, while the other (NCT02477332) was a chronic spontaneous urticaria trial. Most of the literature results likewise discuss asthma, asthma-COPD overlap, or pediatric monoclonal antibody use in general, not bronchitis specifically. This pattern strongly suggests the TxGNN knowledge graph may have mapped "asthma" onto a "bronchitis" disease node, rather than reflecting a genuinely novel indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2b | Completed | 382 | Dose-finding study of QGE031 (ligelizumab, an anti-IgE agent) as add-on therapy in Chronic Spontaneous Urticaria — not a bronchitis trial; only mechanistically adjacent. |
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Completed | 11 | Evaluated whether adding Omalizumab allows prednisone dose reduction in asthma patients with persistent eosinophilic bronchitis; very small sample, population is asthma-based. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clin Rev Allergy Immunol | Omalizumab reduces free serum IgE and FcεRI expression, improving airway inflammation in moderate-to-severe persistent asthma; approval/post-approval overview. |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui (Jpn J Anesthesiology) | Preoperative management review noting omalizumab as an option for severe allergic asthma per Japanese guidelines; bronchitis mentioned only in passing. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | Discusses chronic bronchitis/emphysema/ACO in smokers with asthma; notes these patients are typically excluded from omalizumab trials. |
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Case Series | Postepy Dermatol Alergol | Biologic therapy (including omalizumab) in older patients with severe allergic asthma–COPD overlap. |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Pooled Safety Analysis | Curr Med Res Opin | Pooled safety/tolerability analysis of omalizumab in children with allergic asthma. |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | Review | Rev Mal Respir | French expert review on adult asthma exacerbations; general asthma management, not bronchitis-specific. |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Review | Allergol Immunopathol | General review of monoclonal antibodies in pediatrics, including anti-IgE therapy for allergic disease. |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case Report | J Investig Allergol Clin Immunol | Rare case of plastic bronchitis following bronchial thermoplasty (an asthma procedure) — tangential to omalizumab use. |

## Taiwan Market Information

Omalizumab currently has **0 registered licenses** in Taiwan (market status: Not marketed / Not Marketed). No product registration records are available in this evidence pack.

## Safety Considerations

**Drug Interactions** (8 recorded, DDInter source):

| Interacting Substance | Interaction Level |
|---|---|
| Omacetaxine mepesuccinate | Moderate |
| Zinc sulfate | Minor |
| Zinc acetate | Minor |
| Zinc gluconate | Minor |
| Zinc chloride | Minor |
| Echinacea | Minor |
| Vitamin E | Minor |

Detailed key warnings and contraindications are not available in the current data pack — please refer to the package insert for this information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Bronchitis, L4 evidence) is not well supported — the underlying trials and literature largely reflect asthma or asthma-overlap populations rather than bronchitis itself, indicating a likely disease-mapping artifact. Combined with the drug's non-marketed status in Taiwan and missing MOA/warning/contraindication data (data gaps DG001, DG002), this candidate does not currently meet the bar for safety pre-screening (S1).

**To proceed, the following is needed:**
- Resolve the disease-ontology mismatch between "bronchitis" and "asthma" in the TxGNN mapping before treating this as a genuine new signal
- Obtain TFDA/package-insert data on key warnings and contraindications (currently blocking, DG001)
- Obtain confirmed mechanism-of-action documentation (DG002)
- Note: within this same evidence pack, **obstructive lung disease** (rank 3, L1 evidence, "Proceed with Guardrails") and **atopic eczema/dermatitis** (ranks 2 & 4, L2 evidence, direct Phase 4 trial NCT02300701) show materially stronger and more clinically coherent evidence, and may be more productive candidates to prioritize than the top-ranked bronchitis entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

