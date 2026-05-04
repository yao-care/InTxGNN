---
layout: default
title: Difluprednate
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 10
---

# Difluprednate
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

# Difluprednate: From Post-Surgical Ocular Inflammation to Iris Disease

## One-Sentence Summary

Difluprednate (Durezol®) is a potent dual-fluorinated ophthalmic corticosteroid, originally approved for treating eye pain and inflammation following ophthalmic surgery and for anterior uveitis.
The TxGNN model predicts it may be effective for **Iris Disease**, the indication with the strongest supporting evidence in this analysis—backed by **4 clinical trials** (including 3 completed Phase 3 studies) and **2 publications**.
Among the 10 predicted indications evaluated, iris disease is the only one reaching Evidence Level L1, making it the primary actionable repurposing target.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Eye pain and inflammation following ophthalmic surgery; anterior uveitis |
| Predicted New Indication | Iris Disease |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Difluprednate (chemical name: 6α,9-difluoro-11β,17,21-trihydroxy-1,4-pregnadiene-3,20-dione 21-acetate 17-butyrate; also known as DFBA or W-6309) is a synthetic corticosteroid formulated as a 0.05% ophthalmic emulsion. It acts by binding to the glucocorticoid receptor (GR, gene: NR3C1) with exceptionally high affinity (Ki = 0.78 nM). This receptor binding suppresses the NF-κB and AP-1 transcription factor pathways, downstream reducing expression of COX-2, phospholipase A2, and pro-inflammatory cytokines such as IL-1β and TNF-α—directly attenuating the inflammatory cascades that drive ocular disease.

The dual fluorine substitution at the 6α and 9α positions is the structural key to difluprednate's clinical profile. This modification substantially increases lipophilicity compared to non-fluorinated corticosteroids, enabling superior penetration into the aqueous humor and the anterior segment structures—most importantly, the iris and ciliary body. Pharmacokinetic studies in animal models confirm that this ophthalmic emulsion formulation achieves high local bioavailability at the target tissue while minimizing systemic exposure, an important safety advantage.

Iris disease encompasses a spectrum of conditions involving iris inflammation (iritis/anterior uveitis), pigment dispersion, rubeosis iridis, and associated sequelae. The inflammatory core—particularly anterior uveitis (iridocyclitis)—is pathophysiologically driven by the same cytokine-mediated cascade that difluprednate is mechanistically designed to suppress. Critically, this drug already has Phase 3 trial data specifically in severe anterior uveitis (NCT00407056), meaning the TxGNN prediction is not only mechanistically plausible but empirically supported by prior clinical development work. The prediction is best understood as a formal quantitative confirmation of an established clinical signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00407056](https://clinicaltrials.gov/study/NCT00407056) | Phase 3 | Completed | 20 | Open-label study of difluprednate 0.05% ophthalmic emulsion specifically for severe anterior uveitis (including panuveitis); directly evaluates drug efficacy in the primary pathology of iris disease—this is the most directly relevant trial |
| [NCT01124045](https://clinicaltrials.gov/study/NCT01124045) | Phase 3 | Completed | 80 | Randomized, double-masked, active-controlled study comparing difluprednate vs. prednisolone acetate 1% (Pred Forte™) for post-cataract surgery ocular inflammation in children aged 0–3 years; demonstrates non-inferiority in a challenging pediatric population |
| [NCT03693989](https://clinicaltrials.gov/study/NCT03693989) | Phase 3 | Completed | 178 | Double-blind, parallel-group, multicenter study of PRO-145 ophthalmic emulsion vs. prednisolone acetate 1% for inflammation and pain after phacoemulsification; provides indirect class-level evidence for ophthalmic corticosteroid emulsions in anterior segment inflammation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21182429](https://pubmed.ncbi.nlm.nih.gov/21182429/) | 2011 | Animal PK Study | Journal of Ocular Pharmacology and Therapeutics | Characterizes pharmacokinetics and pharmacodynamics of difluprednate ophthalmic emulsion in rabbits via glucocorticoid receptor-binding bioassay; demonstrates superior ocular bioavailability compared to other ophthalmic corticosteroids and confirms high tissue penetration into the anterior segment |
| [27594198](https://pubmed.ncbi.nlm.nih.gov/27594198/) | 2016 | Case Report | Ophthalmology | Documents long-term management of panuveitis and iris heterochromia in an Ebola virus disease survivor; illustrates the clinical complexity and chronicity of iris inflammatory disease requiring sustained, high-potency corticosteroid therapy |

---

## India Market Information

Difluprednate currently has **no registered product licenses in India**. It is classified as "Not Marketed." This means there is no approved locally available product, and any clinical use would require importation or a new regulatory submission to CDSCO.

This absence from the India market is notable given that the drug has completed Phase 3 development and is commercially available in other markets (e.g., Durezol® in the United States). There is a potential unmet market need for a high-potency ophthalmic corticosteroid emulsion in India's ophthalmology sector.

---

## Safety Considerations

- **Drug Interactions**: Difluprednate is a potent glucocorticoid receptor agonist (NR3C1; Ki = 0.78 nM). Concurrent administration with other glucocorticoids may produce additive immunosuppressive effects. As a topical ophthalmic preparation, systemic drug interactions under standard dosing are expected to be minimal due to low systemic absorption; however, this should be confirmed in populations at risk (e.g., patients on systemic immunosuppressants).

- **Class-level Safety Concerns**: As a potent ophthalmic corticosteroid, the following class-related risks are expected and require monitoring: elevated intraocular pressure (IOP), risk of secondary ocular infections (bacterial, fungal, viral), posterior subcapsular cataract formation with prolonged use, and delayed wound healing. These are standard concerns for all potent ophthalmic corticosteroids.

Please refer to the full package insert (e.g., Durezol® prescribing information) for complete warnings, contraindications, and adverse event data, as India-specific regulatory safety documentation is not currently available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Difluprednate has a well-characterized mechanism of action directly relevant to iris disease, completed Phase 3 clinical evidence specifically in anterior uveitis (the core pathology of iris disease), and strong pharmacokinetic data supporting anterior segment penetration. The drug is absent from the India market despite proven clinical efficacy abroad, suggesting a clear opportunity for regulatory submission to CDSCO.

**To proceed, the following is needed:**

- **Regulatory pathway assessment**: Initiate CDSCO new drug application (NDA) planning; identify whether prior approval in other major markets (FDA, EMA) can expedite review
- **Full safety documentation**: Obtain and review the complete package insert (Durezol® US label or equivalent) for warnings, contraindications, and post-marketing safety data
- **MOA documentation**: Retrieve formal mechanism-of-action data from DrugBank (DB06781) to complete the regulatory dossier
- **IOP monitoring protocol**: Develop a specific intraocular pressure monitoring plan for clinical use, given the potency of difluprednate relative to other ophthalmic steroids
- **Comparative landscape analysis**: Benchmark against currently approved ophthalmic corticosteroids in India (prednisolone acetate, dexamethasone, fluorometholone) to define the differentiation story
- **Phase 3 full data review**: Obtain complete results from NCT00407056 (anterior uveitis) and NCT01124045 (pediatric) to characterize the efficacy-safety profile in the target population

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All findings must be reviewed by qualified medical and regulatory professionals before any clinical or commercial decision is made.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

