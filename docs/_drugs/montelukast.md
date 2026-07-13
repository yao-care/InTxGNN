---
layout: default
title: Montelukast
parent: 僅模型預測 (L5)
nav_order: 434
evidence_level: L5
indication_count: 5
---

# Montelukast
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Montelukast: From Asthma & Allergic Rhinitis to Bronchitis

## One-Sentence Summary

Montelukast is a selective cysteinyl leukotriene 1 (CysLT1) receptor antagonist, globally established for the maintenance treatment of asthma and the relief of symptoms of allergic rhinitis.
The TxGNN model predicts it may be effective for **Bronchitis** — encompassing viral bronchiolitis, eosinophilic bronchitis, and post-transplant bronchiolitis obliterans syndrome (BOS) — with **23 clinical trials** and **20 publications** currently supporting this direction.
While Montelukast is not currently marketed in India, its robust global approval history and the breadth of existing clinical evidence across bronchitis subtypes make this an evidence-supported repurposing candidate warranting serious evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not documented in India regulatory data; globally approved for asthma and allergic rhinitis |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Montelukast acts as a highly selective antagonist of the CysLT1 receptor, blocking the binding of cysteinyl leukotrienes — specifically LTC4, LTD4, and LTE4. This suppresses a cascade of pro-inflammatory events central to bronchial disease: eosinophil recruitment into the airway epithelium, excessive mucus secretion, bronchospasm, and airway hyperreactivity. These mediators are released by mast cells, eosinophils, and basophils in response to both allergens and viral triggers such as respiratory syncytial virus (RSV). Mechanistic data also shows montelukast inhibits TGF-β1 expression, conferring additional anti-remodelling effects relevant to chronic or recurrent bronchitis.

The link between Montelukast's established indication (asthma/allergic rhinitis) and bronchitis is mechanistically direct: both conditions share leukotriene-driven airway inflammation as a core pathophysiological driver. In viral bronchiolitis, RSV infection upregulates cysteinyl leukotriene production, contributing to post-infection wheezing and recurrent lower airway obstruction in infants — a precisely targetable pathway for CysLT1 blockade. In non-asthmatic eosinophilic bronchitis (NAEB), the CysLT pathway is over-activated independently of bronchospasm, making eosinophilic airway inflammation the primary target. In post-transplant BOS, LTB4-mediated pathways drive fibrotic destruction of bronchiolar epithelium (PMID 28545478), and multiple prospective trials have positioned montelukast — particularly within the FAM protocol (Fluticasone + Azithromycin + Montelukast) — as a component of active management.

The TxGNN prediction is therefore grounded in robust biological plausibility rather than merely statistical association. Montelukast's global approval for asthma is predicated on the same CysLT1-inhibition mechanisms operative in bronchitis subtypes. Of note, "bronchitis" as a disease label in this prediction spans heterogeneous subtypes with differing evidence strengths: viral bronchiolitis and eosinophilic bronchitis carry stronger clinical trial evidence, while the post-transplant BOS application is supported by Phase 2 prospective data involving montelukast directly. Any repurposing strategy for India should differentiate the target subtype clearly, as evidence quality and regulatory pathway will vary accordingly.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00076973](https://clinicaltrials.gov/study/NCT00076973) | Phase 3 | Completed | 1,125 | Large-scale multi-dose, double-blind study comparing two doses of Montelukast (MK0476) vs placebo for respiratory symptoms associated with RSV-induced bronchiolitis in children aged 3–24 months |
| [NCT01370187](https://clinicaltrials.gov/study/NCT01370187) | N/A | Completed | 146 | Evaluated Montelukast efficacy for acute bronchiolitis and post-bronchiolitis viral-induced wheezing in infants aged 3–12 months; direct assessment of symptom resolution |
| [NCT00863317](https://clinicaltrials.gov/study/NCT00863317) | N/A | Completed | 141 | Randomized double-blind placebo-controlled trial of once-daily Montelukast for first-time viral bronchiolitis; primary endpoint was duration of acute illness |
| [NCT03369119](https://clinicaltrials.gov/study/NCT03369119) | Phase 4 | Completed | 100 | Oral Montelukast added to maximal standard treatment in hospitalized preschool children with acute asthma; assessed additive benefit over standard care |
| [NCT04613180](https://clinicaltrials.gov/study/NCT04613180) | Phase 4 | Unknown | 100 | Evaluated Montelukast sodium for treatment and prevention of recurrent obstructive bronchitis in children aged 1–7 years; 80 participants randomized to two groups |
| [NCT01211509](https://clinicaltrials.gov/study/NCT01211509) | Phase 4 | Completed | 30 | Randomized double-blind placebo-controlled trial of Montelukast for BOS after lung transplantation; tested whether Montelukast slows chronic rejection progression |
| [NCT00656058](https://clinicaltrials.gov/study/NCT00656058) | Phase 2 | Completed | 25 | Multi-institutional Phase 2 study of Montelukast for BOS following allogeneic or autologous SCT in children and adults; Montelukast used for years in this indication |
| [NCT01307462](https://clinicaltrials.gov/study/NCT01307462) | Phase 2 | Completed | 36 | Phase 2 trial of FAM regimen (Fluticasone + Azithromycin + Montelukast) for BOS after stem cell transplant; primary endpoint: treatment failure defined as ≥10% FEV1 decline |
| [NCT01121016](https://clinicaltrials.gov/study/NCT01121016) | Phase 4 | Unknown | 63 | Randomized double-blind placebo-controlled study of add-on Montelukast to inhaled budesonide for non-asthmatic eosinophilic bronchitis (NAEB); primary endpoint: cough VAS score reduction and airway eosinophilia |
| [NCT02479074](https://clinicaltrials.gov/study/NCT02479074) | Phase 4 | Completed | 49 | Evaluated Montelukast vs prednisolone for chronic cough using FeNO-guided differential diagnosis; measured 24-hour cough counts via automated counter at 2 weeks |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [25563311](https://pubmed.ncbi.nlm.nih.gov/25563311/) | 2015 | RCT | Chinese Medical Journal | Add-on Montelukast to budesonide vs budesonide monotherapy in NAEB; significant improvement in cough VAS score, faster reduction in airway eosinophilia, and enhanced quality of life in the combination group |
| [20976161](https://pubmed.ncbi.nlm.nih.gov/20976161/) | 2010 | RCT | PLoS One | Randomized controlled comparison of fish oil, Montelukast, and their combination for airway inflammation and eucapnic voluntary hyperpnea-induced bronchoconstriction in asthmatics; both agents independently reduced leukotriene-mediated airway response |
| [38485149](https://pubmed.ncbi.nlm.nih.gov/38485149/) | 2024 | Clinical Practice Guideline | European Respiratory Journal | Joint ERS/EBMT clinical practice guidelines for pulmonary chronic graft-versus-host disease; endorses Montelukast as part of the FAM protocol for BOS management |
| [38504551](https://pubmed.ncbi.nlm.nih.gov/38504551/) | 2024 | Review | Therapeutic Advances in Respiratory Disease | Comprehensive review of Montelukast's therapeutic potential in post-transplant BOS; discusses TH-1/TH-2, NF-κB, and TGF-β mechanisms relevant to both lung and HSCT-associated BOS |
| [35114411](https://pubmed.ncbi.nlm.nih.gov/35114411/) | 2022 | Phase II Trial | Transplantation and Cellular Therapy | Prospective Phase II trial of Montelukast for BOS after HCT; evaluated CysLT blockade on lung function decline and explored BOS pathogenesis including bronchiolar fibrosis mechanisms |
| [26475726](https://pubmed.ncbi.nlm.nih.gov/26475726/) | 2016 | Clinical Study | Biology of Blood and Marrow Transplantation | FAM plus brief steroid pulse for new-onset BOS post-allogeneic HCT; n=36, Phase II multicenter; evaluated treatment failure at 6 months, demonstrated lung stabilization in majority of patients |
| [27229850](https://pubmed.ncbi.nlm.nih.gov/27229850/) | 2016 | Clinical Study | Respiratory Research | Budesonide/formoterol + Montelukast + N-acetylcysteine for BOS after HSCT; compared to systemic corticosteroids; demonstrated lung function stabilization in a subgroup of BOS patients |
| [24118637](https://pubmed.ncbi.nlm.nih.gov/24118637/) | 2014 | Systematic Review | Pediatric Allergy and Immunology | Systematic review of Montelukast's efficacy for preventing post-bronchiolitis wheezing; synthesized evidence on CysLT role in RSV-triggered recurrent airway obstruction in infants |
| [28545478](https://pubmed.ncbi.nlm.nih.gov/28545478/) | 2017 | Animal Study | Journal of Cardiothoracic Surgery | Investigated role of LTB4 and Montelukast in transplantation-related bronchiolitis obliterans in rats; demonstrated LTB4 as a key mediator in chronic rejection and Montelukast's protective fibrosis-reducing effect |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Review | BMJ Clinical Evidence | Evidence-based review of interventions for bronchiolitis; contextualizes leukotriene antagonists within the treatment landscape for lower respiratory tract infection in infants |

---

## Safety Considerations

**Drug Interactions**: A total of 470 drug-drug interactions have been identified (DDInter database). Notable interactions of Moderate severity include:

| Interacting Drug | Severity | Clinical Note |
|------|------|------|
| Dexamethasone | Moderate | CYP3A4 induction by dexamethasone may reduce Montelukast plasma levels; monitor for reduced therapeutic effect in patients on concurrent corticosteroid therapy |
| Metronidazole | Moderate | Potential pharmacokinetic interaction; clinical monitoring of efficacy and tolerability advised |
| Miconazole | Moderate | CYP3A4/2C9 inhibition may increase Montelukast plasma concentrations; watch for dose-dependent adverse effects |
| Nateglinide | Moderate | Possible metabolic interaction via CYP2C9; monitor blood glucose and glycaemic response |
| Nitisinone | Moderate | Interaction mechanism not fully characterized; clinical monitoring recommended |
| Troglitazone | Moderate | CYP-mediated metabolic interaction; note that troglitazone has been withdrawn from most markets globally |

**Neuropsychiatric Safety Signal**: Multiple published studies and a 2020 US FDA Boxed Warning have identified an association between Montelukast use and neuropsychiatric adverse events, including mood changes, abnormal dreams, insomnia, and suicidal ideation. The risk appears to be age-related and is of particular concern in paediatric populations (PMID 37758273; PMID 39836401; PMID 36948487). This warning should be incorporated into any patient counselling, prescribing guidance, and pharmacovigilance plan for India market entry.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple clinical trials — including a Phase 3 study in 1,125 patients with RSV bronchiolitis, Phase 4 studies in recurrent obstructive bronchitis, and Phase 2 prospective trials in post-transplant BOS directly using Montelukast — support an L2 evidence rating. The CysLT1-blockade mechanism is directly relevant to leukotriene-driven bronchial inflammation across all bronchitis subtypes, and Montelukast has decades of global post-marketing safety data. However, efficacy evidence is heterogeneous across subtypes, and the FDA-boxed neuropsychiatric safety signal requires structured risk management.

**To proceed, the following is needed:**

- **MOA documentation**: Obtain formal mechanism of action data from DrugBank or the approved prescribing information (currently classified as Data Gap) for inclusion in the regulatory dossier
- **CDSCO regulatory filing**: Prepare and submit a New Drug Application to the Central Drugs Standard Control Organisation (CDSCO) for India market authorization, leveraging global approval dossiers
- **Package insert review**: Obtain the official product monograph to extract approved warnings, contraindications, and dosing guidance — currently unavailable in this evidence pack
- **Subtype-specific evidence stratification**: Separate evidence packages should be developed for (1) viral bronchiolitis in infants, (2) non-asthmatic eosinophilic bronchitis in adults, and (3) post-transplant BOS, as each subtype carries a different regulatory and clinical pathway
- **Neuropsychiatric risk mitigation plan**: Design a pharmacovigilance and risk minimisation strategy aligned with the FDA Boxed Warning, with particular attention to paediatric populations where most bronchitis indication studies are conducted
- **India-specific safety monitoring programme**: Given the large paediatric patient population likely to be treated for bronchiolitis in India, establish safety monitoring aligned with CDSCO requirements and PMCPA guidelines

> ⚠️ *Disclaimer: This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

