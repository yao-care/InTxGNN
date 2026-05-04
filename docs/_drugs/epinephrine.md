---
layout: default
title: Epinephrine
parent: 僅模型預測 (L5)
nav_order: 236
evidence_level: L5
indication_count: 4
---

# Epinephrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Epinephrine: From Anaphylaxis & Emergency Resuscitation to Obstructive Lung Disease

## One-Sentence Summary

Epinephrine is a non-selective adrenergic agonist serving as a cornerstone emergency medicine for anaphylaxis, cardiac arrest, and severe bronchospasm globally—though it holds no registered product approvals in India.
The TxGNN model predicts it may be effective for **Obstructive Lung Disease** (encompassing acute asthma exacerbations, viral bronchiolitis, and croup),
with multiple completed clinical trials and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anaphylaxis, cardiac arrest, severe bronchospasm (global standard; no India registration on record) |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Epinephrine is a non-selective α/β-adrenergic receptor agonist that acts simultaneously across multiple receptor subtypes. Although a formal DrugBank MOA record was not retrieved in this analysis cycle, the drug's pharmacological profile is extremely well-established: **β2-receptor activation** relaxes bronchial smooth muscle and relieves airway spasm; **α1-receptor activation** produces mucosal vasoconstriction that reduces airway wall edema and secretion; and **β1-receptor activation** provides compensatory hemodynamic support. This triple mechanism makes epinephrine uniquely suited to conditions involving acute reversible airway obstruction.

Obstructive lung disease—spanning acute asthma exacerbations, viral bronchiolitis in infants, croup (laryngotracheobronchitis), and COPD exacerbations with bronchospasm—shares a core pathophysiology of airway narrowing driven by bronchospasm, mucosal edema, and mucus accumulation. Epinephrine's three-pronged pharmacological attack directly addresses all three components simultaneously, which no selective β2-agonist (such as salbutamol) can replicate alone. Notably, nebulized racemic epinephrine has been used in clinical practice for croup and bronchiolitis for decades, and inhaled epinephrine (Primatene Mist) holds FDA over-the-counter approval for asthma bronchospasm relief in the United States.

The TxGNN prediction score of 99.71% strongly reflects this deeply validated mechanistic and clinical overlap. This is not a speculative repurposing hypothesis: the biological rationale is firmly established, supported by Cochrane-level systematic reviews and multiple completed Phase 3–4 trials. The central question for the India market is therefore not whether the drug works, but how to structure a regulatory pathway and clinical adoption framework given the complete absence of domestic product registration.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01143051](https://clinicaltrials.gov/study/NCT01143051) | Phase 1/2 | Completed | 24 | Directly evaluated PK and safety of Epinephrine Inhalation Aerosol USP (E004, HFA-MDI new formulation) in healthy adults under augmented dose conditions; foundational study for inhaled epinephrine in obstructive lung disease |
| [NCT04207840](https://clinicaltrials.gov/study/NCT04207840) | Phase 4 | Completed | 28 | Three-way crossover PK comparison of Primatene Mist (inhaled epinephrine 0.25 mg) vs epinephrine IM injection (0.30 mg) vs ProAir albuterol (0.18 mg) in healthy adults; characterized systemic exposure differences between routes |
| [NCT01737905](https://clinicaltrials.gov/study/NCT01737905) | Phase 3 | Completed | 28 | Double-blind, placebo-controlled crossover RCT of E004 (inhaled epinephrine) single dose in children aged 4–11 with asthma; assessed bronchodilatory efficacy and safety in the pediatric obstructive lung disease population |
| [NCT01705964](https://clinicaltrials.gov/study/NCT01705964) | Phase 4 | Completed | 49 | RCT of IM epinephrine (1:1000, weight-based) as adjunct to inhaled β2-agonists for severe pediatric asthma exacerbation; evaluated whether adding epinephrine improves outcomes beyond standard bronchodilator therapy alone |
| [NCT00817466](https://clinicaltrials.gov/study/NCT00817466) | Phase 4 | Unknown | 500 | Large multicenter RCT of optimal inhalation treatment for infants aged 0–12 months with acute bronchiolitis in SE Norway; consistent with Nordic standard of care that routinely includes nebulized epinephrine as a treatment arm |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | N/A | Unknown | 600 | Head-to-head RCT comparing epinephrine vs albuterol in bronchiolitis (N=600); addresses which bronchodilator provides superior efficacy in this common pediatric obstructive lung condition |
| [NCT02585531](https://clinicaltrials.gov/study/NCT02585531) | Phase 2 | Unknown | 100 | Three-arm trial of epinephrine, dexamethasone, and hypertonic saline in children with bronchiolitis; directly evaluates epinephrine's role in reducing disease severity score and hospitalization duration |
| [NCT02586961](https://clinicaltrials.gov/study/NCT02586961) | Phase 2/3 | Terminated | 195 | Multicenter RCT of nebulized adrenaline + high-dose oral betamethasone vs placebo for acute bronchiolitis in emergency settings; terminated early but 195 subjects enrolled, providing usable safety and trend data |
| [NCT00435994](https://clinicaltrials.gov/study/NCT00435994) | N/A | Completed | 59 | Assessed how nebulized aerosol medications (including epinephrine) improve airway function in infants with lower respiratory infections and bronchiolitis/RSV; included VEGF biomarker analysis |
| [NCT01737892](https://clinicaltrials.gov/study/NCT01737892) | Phase 1/2 | Terminated | 21 | PK study using deuterium-labeled epinephrine (epinephrine-d3) to separate administered drug from endogenous catecholamine in volunteers; critical methodology for accurate PK characterization of inhaled E004 |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34593615](https://pubmed.ncbi.nlm.nih.gov/34593615/) | 2022 | Systematic Review / Meta-analysis | Thorax | Compared epinephrine vs selective β2-agonist in acute asthma in adults and children; found epinephrine non-inferior and potentially beneficial in pre-hospital severe/life-threatening asthma, challenging guideline restrictions |
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Cochrane Review | Cochrane Database Syst Rev | Comprehensive systematic review of epinephrine for acute bronchiolitis; assessed efficacy vs placebo and other bronchodilators; provided the most definitive evidence base for epinephrine's role in this condition |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Cochrane Review | Cochrane Database Syst Rev | Earlier Cochrane review on epinephrine for bronchiolitis; demonstrated modest short-term benefit in mild-to-moderate bronchiolitis, establishing the evidence foundation that prompted subsequent larger trials |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Narrative Review | Expert Rev Respir Med | Synthesized 10 years (2009–2018) of evidence on racemic epinephrine, systemic corticosteroids, hypertonic saline, and high-flow oxygen therapy in infant bronchiolitis; clarifies epinephrine's current therapeutic position |
| [19135584](https://pubmed.ncbi.nlm.nih.gov/19135584/) | 2009 | Clinical Review | Pediatr Clin North Am | Reviewed acute bronchiolitis and croup together; documented evidence for nebulized adrenaline providing temporary symptomatic benefit in both virally-induced obstructive conditions in early childhood |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Clinical Review | BMJ Clin Evid | Comprehensive clinical evidence review on bronchiolitis epidemiology and treatment; assessed epinephrine alongside other interventions within the systematic BMJ Clinical Evidence framework |
| [4606289](https://pubmed.ncbi.nlm.nih.gov/4606289/) | 1974 | Clinical Study | Clin Pharmacol Ther | Direct comparison of bronchodilator effects of terbutaline vs epinephrine in patients with obstructive lung disease; early clinical pharmacology evidence establishing epinephrine's bronchodilatory efficacy |
| [30856157](https://pubmed.ncbi.nlm.nih.gov/30856157/) | 2019 | Drug Update | Med Lett Drugs Ther | Reviewed the return of Primatene Mist (OTC inhaled epinephrine HFA) to the US market after CFC reformulation; summarizes the regulatory and clinical context for epinephrine in asthma management |
| [6777857](https://pubmed.ncbi.nlm.nih.gov/6777857/) | 1980 | Cohort Study | Scand J Clin Lab Invest | Demonstrated elevated plasma noradrenaline in chronic obstructive lung disease patients, inversely correlated with arterial O₂ saturation; provides mechanistic evidence for sympathoadrenal axis dysregulation in COPD |
| [11339733](https://pubmed.ncbi.nlm.nih.gov/11339733/) | 2001 | Systematic Review | Prehosp Emerg Care | Reviewed prehospital subcutaneous epinephrine use for asthma and anaphylaxis in elderly patients; addressed safety concerns and evidence levels for epinephrine across obstructive lung conditions in high-risk populations |

---

## India Market Information

Epinephrine (DrugBank ID: DB00668) currently holds **no registered product approvals in India** as of the data cutoff (2026-04-04). There are zero active marketing authorizations on record with the Central Drugs Standard Control Organisation (CDSCO).

This absence from formal product registration likely reflects epinephrine's status as a long-established generic active pharmaceutical ingredient commonly stocked in hospital formularies, emergency departments, and crash carts without product-specific marketing authorization, rather than true clinical unavailability. Epinephrine ampoules (1:1000, 1:10000) and auto-injectors are recognized in Indian emergency medicine practice guidelines as essential medicines for anaphylaxis and cardiac resuscitation.

For the obstructive lung disease indication specifically, no inhaled epinephrine formulation (HFA-MDI or nebulizer solution) appears to hold domestic market authorization. A formal regulatory dossier would need to be constructed from scratch.

---

## Safety Considerations

**Drug Interactions (385 interactions identified; key interactions listed below):**

Epinephrine's broad adrenergic mechanism creates an extensive interaction landscape. The most clinically significant interactions are:

- **Major interactions:**
  - **Amitriptyline** (tricyclic antidepressant): Inhibits reuptake transporters → potentiates epinephrine's vasopressor and arrhythmogenic effects; risk of hypertensive crisis and severe dysrhythmia
  - **Amoxapine** (tricyclic-related agent): Similar mechanism to amitriptyline; marked cardiovascular potentiation

- **Notable Moderate interactions requiring clinical monitoring:**
  - **Beta-blockers** (Acebutolol, Atenolol, Betaxolol): Competitive β-blockade abolishes bronchodilatory (β2) effect while leaving α-vasoconstriction unopposed → reflex bradycardia and paradoxical hypertension
  - **Long-acting β2-agonists** (Formoterol, Arformoterol, Salbutamol): Additive adrenergic stimulation; compounding tachycardia, tremor, and hypokalemia risk
  - **Antidiabetic agents** (Acarbose, Acetohexamide, Alogliptin, Albiglutide): Epinephrine elevates blood glucose via hepatic glycogenolysis and gluconeogenesis; may blunt glycemic control
  - **Antipsychotics** (Amisulpride, Aripiprazole, Asenapine): QT-prolongation risk is compounded by epinephrine-induced tachycardia; cardiac monitoring warranted
  - **Stimulants / ADHD agents** (Methylphenidate, Amphetamine, Benzphetamine, Atomoxetine): Additive sympathomimetic cardiovascular effects; risk of arrhythmia and hypertensive episodes

Please refer to the approved package insert for complete contraindication, warning, and special population guidance, as formal product-level safety data was not available in this analysis cycle.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Epinephrine's efficacy in obstructive lung disease is supported by L1-level evidence—including two Cochrane systematic reviews, a 2022 meta-analysis published in *Thorax*, and multiple completed Phase 1–4 clinical trials that directly studied inhaled and injectable epinephrine in acute asthma, bronchiolitis, and croup. The mechanistic rationale (β2 bronchodilation + α1 mucosal decongestant + β1 cardiac support) is unambiguous, biologically well-validated, and without meaningful scientific controversy. The primary barrier to structured India market utilization is regulatory and logistical, not scientific.

**To proceed, the following is needed:**

- **Regulatory pathway assessment**: Evaluate whether existing global approvals (FDA OTC approval of Primatene Mist; established European precedents) support an expedited or bridging registration application with CDSCO for an inhaled epinephrine formulation
- **Formulation strategy decision**: Define target indication and route of administration—inhaled HFA-MDI for asthma, nebulized racemic epinephrine for bronchiolitis/croup, or IM auto-injector for anaphylaxis—as each requires a separate regulatory submission and clinical dossier
- **MOA documentation**: Retrieve complete DrugBank pharmacodynamics and pharmacokinetics data to finalize the mechanism-of-action section of any regulatory submission
- **Safety dossier completion**: Obtain CDSCO-approved or equivalent prescribing information to formally document contraindications, warnings, and special population guidance; the current analysis identified a data gap at blocking severity
- **Drug interaction risk stratification**: Given 385 identified interactions, develop a structured prescriber guidance document and pharmacovigilance monitoring protocol focused on highest-risk combinations (beta-blockers, tricyclic antidepressants, antidiabetics)
- **India-specific pharmacoeconomic assessment**: Model cost-effectiveness vs. existing alternatives (salbutamol, ipratropium) for the obstructive lung disease setting in the Indian healthcare context
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

