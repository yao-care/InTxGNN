---
layout: default
title: Simvastatin
parent: High Evidence (L1-L2)
nav_order: 767
evidence_level: L1
indication_count: 8
---

# Simvastatin
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **8** 
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

# Simvastatin: From Hypercholesterolemia to Familial Hypercholesterolemia

## One-Sentence Summary

> Simvastatin is an HMG-CoA reductase inhibitor (statin) originally used to lower LDL cholesterol and reduce cardiovascular risk in patients with hypercholesterolemia.
> The TxGNN model predicts it may be effective for **Familial Hypercholesterolemia**,
> with **19 clinical trials** and **18 publications** currently supporting this direction.
>
> **Important caveat**: the evidence pack's own rationale notes this is essentially an existing *labeled* use of statins (LDL-receptor pathway), not a genuine off-label repurposing discovery — it confirms known standard-of-care rather than uncovering a new therapeutic use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no India/Taiwan license records in this evidence pack (Simvastatin is generally used for hypercholesterolemia/dyslipidemia and cardiovascular risk reduction) |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available directly from DrugBank in this evidence pack. However, the evidence pack's repurposing rationale supplies the relevant mechanistic detail: Simvastatin is an HMG-CoA reductase inhibitor that directly blocks hepatic cholesterol synthesis and upregulates LDL-receptor expression on hepatocytes. This is precisely the core therapeutic mechanism for familial hypercholesterolemia (FH), a disorder caused by LDL-receptor deficiency or dysfunction.

Because FH is fundamentally a disease of impaired LDL clearance, statins — including simvastatin — are guideline-recommended, first-line therapy already in routine use for this population, both alone and combined with agents like ezetimibe or PCSK9 inhibitors. The mechanistic link is therefore direct and well-established, rather than a novel repurposing hypothesis.

For this reason, the evidence pack itself flags familial hypercholesterolemia as "not true repurposing" — it reflects confirmation of an already-known label indication rather than discovery of a new one. The clinical and mechanistic strength is real, but its value as a *repurposing* candidate is limited; its main practical relevance here is validating data quality/model calibration rather than identifying new commercial opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | Completed | 486 | Placebo-controlled RCT of alirocumab added to statin-based lipid-modifying therapy (incl. simvastatin) in heterozygous FH |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE trial: ezetimibe + high-dose simvastatin vs. simvastatin alone on carotid atherosclerosis progression in heFH |
| [NCT00145574](https://clinicaltrials.gov/study/NCT00145574) | Phase 4 | Completed | 194 | Colesevelam add-on to stable statin (incl. simvastatin) in pediatric heFH |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Completed | 248 | Ezetimibe + simvastatin in adolescents with heFH |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Alirocumab in children/adolescents with homozygous FH, on background statin therapy |
| [NCT00465088](https://clinicaltrials.gov/study/NCT00465088) | Phase 3 | Completed | 199 | SUPREME: niacin ER + simvastatin vs. atorvastatin in hyperlipidemia/mixed dyslipidemia |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Completed | 442 | Renal effects of rosuvastatin vs. simvastatin in Fredrickson IIa/IIb dyslipidemia incl. heFH |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | Long-term safety of ezetimibe + atorvastatin/simvastatin in homozygous FH |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Completed | 249 | Placebo-controlled RCT of alirocumab in heFH not adequately controlled on lipid-modifying therapy |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | Completed | 216 | Alirocumab add-on to stable statin therapy in heFH/high CV-risk hypercholesterolemia |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | N Engl J Med | ENHANCE trial: ezetimibe added to simvastatin did not slow atherosclerosis progression vs. simvastatin alone in heFH |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Cohort | J Am Coll Cardiol | Statin therapy substantially reduces CAD events and all-cause mortality in heFH |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Statins (incl. simvastatin) are effective and generally safe for lowering LDL-C in children with FH |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opin Drug Saf | Long-term benefit/risk assessment of simvastatin in FH |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Safety | Benefits and risks of simvastatin in FH patients requiring long-term therapy |
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Guideline | Circulation | ACC/AHA 2026 dyslipidemia management guideline (replaces 2018 cholesterol guideline) |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Cross-sectional | J Clin Med | Simvastatin treatment effects on cellular immunity parameters in children with FH |
| [30270066](https://pubmed.ncbi.nlm.nih.gov/30270066/) | 2018 | Retrospective | Atherosclerosis | Real-world FH treatment patterns and LDL-C goal attainment in lipid clinics |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Comparative Study | Nutr Metab Cardiovasc Dis | Atorvastatin vs. simvastatin efficacy in heterozygous FH |
| [18638604](https://pubmed.ncbi.nlm.nih.gov/18638604/) | 2008 | Commentary | Am J Cardiol | Critical re-analysis of the ENHANCE trial and its implications for lipid-lowering strategy |

---

## Safety Considerations

**Drug Interactions**: DDI screening identified 696 total interaction records for simvastatin. Among the reviewed subset, the following are flagged at **Major** severity and warrant particular caution (consistent with simvastatin's known CYP3A4-mediated myopathy/rhabdomyolysis risk):

- Amiodarone — Major
- Amlodipine — Major
- Fenofibrate — Major

Additional Moderate-level interactions of note include ethanol, nifedipine, omeprazole, apalutamide, aprepitant, and several biologic/oncology agents (e.g., paclitaxel, trastuzumab emtansine, adalimumab).

Detailed key warnings and contraindications are not yet available in this evidence pack (blocked pending TFDA-equivalent label data — see Next Steps).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence quality is strong (L1, multiple completed Phase 3 RCTs directly in the FH population, including the large ENHANCE trial), but this indication is essentially an already-established labeled use of statins rather than a genuine repurposing opportunity — it reflects confirmation of known pharmacology, not new therapeutic discovery. Combined with the drug's current absence from the India market (0 registrations) and a Blocking data gap on label warnings/contraindications, any forward action should proceed cautiously and be scoped around regulatory/safety completion rather than efficacy validation.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse official label warnings/contraindications before S1 safety evaluation
- Resolve DG002: confirm mechanism of action via DrugBank API query
- Clarify local market/registration pathway, since simvastatin currently has zero registrations in this jurisdiction
- Reassess whether "familial hypercholesterolemia" should be tracked as a repurposing candidate at all, given it reflects existing label use rather than a novel indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

