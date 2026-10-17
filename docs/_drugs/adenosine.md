---
layout: default
title: Adenosine
parent: Model Prediction Only (L5)
nav_order: 28
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Adenosine: predicted new indication Obsolete bundle branch block (evidence level L5). Approved use: Ventricular tachycardia"
monitor_inn: "Adenosine"
predicted_indications: ["obsolete bundle branch block"]
---

# Adenosine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Adenosine: From Ventricular Tachycardia to Obsolete Bundle Branch Block

## One-Sentence Summary

Adenosine is an injectable antiarrhythmic originally used for ventricular tachycardia.
The TxGNN model predicts it may be effective for **obsolete bundle branch block** (an outdated ontology term), with **no registered clinical trials** and **no related publications** supporting this prediction.
The second-ranked prediction, **catecholaminergic polymorphic ventricular tachycardia (CPVT)**, has **no clinical trials** and **10 retrieved publications**, but only one case report directly relates to it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ventricular tachycardia (the India licence records contain no approved indication text) |
| Predicted New Indication | Obsolete bundle branch block |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 11 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. From general pharmacology, adenosine acts on A1 receptors at the AV node and slows conduction. That makes a link to conduction disorders plausible. However, the same action means adenosine may worsen bundle branch or AV conduction block rather than treat it. It is also used diagnostically to unmask conduction abnormalities.

The disease name is flagged as obsolete, which suggests an outdated ontology term that maps to a poorly defined or merged concept. Despite the very high score, the prediction is not clinically interpretable and may be a graph artifact.

**Secondary prediction: CPVT (score 99.42%, evidence level L4).** CPVT is driven by sarcoplasmic reticulum calcium leak and triggered activity during adrenergic stimulation. Adenosine opposes catecholamine effects through A1 receptor signalling, which lowers cAMP and may reduce triggered activity. This gives a biologically plausible route to terminating adrenergically driven arrhythmias. The only direct clinical evidence is one case report in which adenosine *triphosphate* (ATP, not adenosine itself) terminated bidirectional VT in a CPVT patient. Standard CPVT therapy (beta-blockers, flecainide, ICD, sympathetic denervation) remains the reference, and adenosine could at most be an acute adjunct.

## Clinical Trial Evidence

Currently no related clinical trials registered, for either the top prediction or the CPVT prediction.

## Literature Evidence

No literature was found for the top prediction (obsolete bundle branch block). The table below covers the second prediction, CPVT. Most papers address CPVT pathophysiology, diagnostics or general arrhythmia management, and none test adenosine as a CPVT treatment.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) | 2008 | Case report | Heart Rhythm | ATP terminated bidirectional VT in a CPVT patient (indirect support only) |
| [40165484](https://pubmed.ncbi.nlm.nih.gov/40165484/) | 2025 | Review (consensus statement) | Europace | Expert consensus on pharmacological provocation testing in cardiac electrophysiology |
| [18368865](https://pubmed.ncbi.nlm.nih.gov/18368865/) | 2007 | Review | J Assoc Physicians India | Recognition and management of idiopathic VT in structurally normal hearts |
| [39148245](https://pubmed.ncbi.nlm.nih.gov/39148245/) | 2024 | Review | Paediatr Anaesth | Pediatric arrhythmias for anesthesiologists |
| [15324613](https://pubmed.ncbi.nlm.nih.gov/15324613/) | 2004 | Review | Curr Treat Options Cardiovasc Med | Treatment alternatives for syncope |
| [21699856](https://pubmed.ncbi.nlm.nih.gov/21699856/) | 2011 | Case report | Heart Rhythm | Abnormal post-pacing repolarization in CPVT with an RyR2 mutation |
| [38776406](https://pubmed.ncbi.nlm.nih.gov/38776406/) | 2024 | Preclinical (animal) | Cardiovasc Res | PDE2A/PDE4B gene therapy improved heart failure and arrhythmias via cAMP compartmentation |
| [30209242](https://pubmed.ncbi.nlm.nih.gov/30209242/) | 2018 | Preclinical (animal) | Sci Transl Med | SR calcium leak contributes to arrhythmia but not to heart failure progression |
| [35577932](https://pubmed.ncbi.nlm.nih.gov/35577932/) | 2022 | Preclinical (in vitro) | Commun Biol | TECRL deficiency impairs mitochondrial function in cardiomyocytes |
| [41691612](https://pubmed.ncbi.nlm.nih.gov/41691612/) | 2026 | Preclinical (in vitro) | J Physiol | Cardiac-neural microtissues suggest CPVT also involves sympathetic neurons |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 10712 | Adnet 3mg Injection | Vial of 2 ml injection | Not stated in licence record |
| 9204 | Adenoject 30mg Injection | Vial of 10 ml injection | Not stated in licence record |
| 179740 | Psvt 6mg Injection | Vial of 2 ml injection | Not stated in licence record |
| 3304 | Adenoz 6mg Injection | Vial of 2 ml injection | Not stated in licence record |
| 2071 | Adenocor 6mg Injection | Vial of 2 ml injection | Not stated in licence record |

Eleven valid single-ingredient licences are registered in total. All are injectable products (2 ml vials, a 10 ml vial and a 2 ml ampoule).

## Safety Considerations

- **Conditions flagged as contraindications in the knowledge graph** (not label text): chronic obstructive pulmonary disease, asthma (including intrinsic and allergic), aortic stenosis and other aortic valve disease, hypotensive disorder, acute coronary syndrome, coronary artery disease, atrioventricular block, sick sinus syndrome, respiratory failure, pulmonary emphysema, pericarditis, mitral valve stenosis, pulmonary valve insufficiency, autonomic nervous system disease and Horner syndrome.
  - The AV block and sick sinus syndrome entries are directly relevant to the predicted conduction-disorder indication.
- **Drug Interactions**: 138 interactions were identified. Major interactions include:
  - Cisapride
  - Dolasetron
  - Papaverine

  Moderate interactions include:
  - Famotidine
  - Clarithromycin
  - Granisetron
  - Levofloxacin
  - Ondansetron
  - Palonosetron

  Many of these involve QT-prolonging drugs.

Please refer to the package insert for warnings and label contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (obsolete bundle branch block) has a very high model score but no trials or literature. Its disease term is outdated, and adenosine's pharmacology suggests it could worsen conduction block. The CPVT prediction is biologically plausible but rests on a single indirect ATP case report. It is better treated as a research question than a development candidate.

**To proceed, the following is needed:**
- Clarification of which current disease concept the obsolete bundle branch block term maps to
- Mechanism of action data for adenosine
- Package insert warnings and contraindications from the India licence holders
- Direct evidence for adenosine (not ATP) in CPVT, such as controlled or prospective studies
- Safety assessment of conduction-block risk and the QT-related interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

