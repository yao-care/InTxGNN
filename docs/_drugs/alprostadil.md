---
layout: default
title: Alprostadil
parent: Model Prediction Only (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Alprostadil: predicted new indication Aortic malformation (evidence level L4). Approved use: Erectile dysfunction, psychologic dyspareunia, premature ejaculation…"
monitor_inn: "Alprostadil"
predicted_indications: ["aortic malformation", "congenital tricuspid stenosis", "congenital valvular dysplasia", "tricuspid valve agenesis", "straddling or overriding tricuspid valve", "tricuspid valve prolapse (disease)", "anomaly of the tricuspid subvalvular apparatus", "double outlet right ventricle with atrioventricular septal defect, pulmonary stenosis, heterotaxy", "heart septal defect", "endemic goiter"]
---

# Alprostadil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Alprostadil: From Erectile Dysfunction and Congenital Heart Defects to Aortic Malformation
{: .text-alpha }

## One-Sentence Summary

Alprostadil (prostaglandin E1) was originally used for erectile dysfunction and to keep the ductus arteriosus open in newborns with certain congenital heart defects.
The TxGNN model predicts it may be effective for **aortic malformation**, but this overlaps heavily with existing uses (aortic coarctation is already among its original indications).
Support comes from **8 publications** (mostly case reports and small clinical studies) and **no registered clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Erectile dysfunction, psychologic dyspareunia, premature ejaculation, tricuspid atresia, aortic coarctation, tetralogy of Fallot, and related congenital heart lesions (the India licence records list no approved indication text) |
| Predicted New Indication | Aortic malformation |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 5 of 5) |
| Number of Registrations | 5 (valid: 5) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, alprostadil is a synthetic prostaglandin E1 that relaxes the smooth muscle of the ductus arteriosus and of blood vessels in general. In newborns with ductal-dependent heart lesions, this keeps the duct open so that blood can reach the lungs or the body.

The relationship between the original and predicted indications is close. Aortic coarctation and interrupted aortic arch rely on the ductus to supply blood to the lower body. The predicted "aortic malformation" therefore largely overlaps with a use that is already established, rather than representing a truly new therapeutic direction.

Secondary effects may also be relevant. Alprostadil has shown anti-inflammatory and organ-protective effects around cardiopulmonary bypass in children with congenital heart disease. It has also reduced skeletal muscle ischaemia-reperfusion injury in rats. These findings are plausible but indirect or preclinical.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6763200](https://pubmed.ncbi.nlm.nih.gov/6763200/) | 1982 | Review / clinical evaluation | Pharmacotherapy | Alprostadil dilates the ductus, increases pulmonary blood flow, and supports newborns with congenital heart lesions that depend on the duct |
| [19080093](https://pubmed.ncbi.nlm.nih.gov/19080093/) | 2008 | Clinical study | Zhonghua Yi Xue Za Zhi | Alprostadil and ulinastatin studied for inflammatory response and lung injury after cardiopulmonary bypass in children with congenital heart disease |
| [19068708](https://pubmed.ncbi.nlm.nih.gov/19068708/) | 2008 | Case report | Kyobu Geka | Neonate with interrupted aortic arch type B; alprostadil used to keep the duct open before single-stage repair |
| [15362549](https://pubmed.ncbi.nlm.nih.gov/15362549/) | 2004 | Review | Kyobu Geka | Alprostadil keeps the duct open to preserve left ventricular function in transposition of the great arteries before arterial switch surgery |
| [30184041](https://pubmed.ncbi.nlm.nih.gov/30184041/) | 2018 | Case report | Braz J Cardiovasc Surg | Aortopulmonary window; milrinone and alprostadil used before surgery to counter high lung pressure |
| [41167776](https://pubmed.ncbi.nlm.nih.gov/41167776/) | 2025 | Retrospective cohort | Zhonghua Fu Chan Ke Za Zhi | Delivery mode and timing in 123 fetuses with complex congenital heart disease |
| [42469655](https://pubmed.ncbi.nlm.nih.gov/42469655/) | 2026 | Retrospective cohort | BMC Pregnancy Childbirth | Perinatal management and postnatal outcomes of complex fetal congenital heart disease |
| [20029353](https://pubmed.ncbi.nlm.nih.gov/20029353/) | 2009 | Preclinical (rat) | Minerva Chir | Alprostadil attenuated skeletal muscle ischaemia-reperfusion injury in rats |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 26832 | Bioglandin 500mcg Injection | Vial of 1 injection | Not stated in the licence record |
| 889 | Alpostin 500mcg Injection | Vial of 1 ml injection | Not stated in the licence record |
| 178514 | Prostaver 500mcg Injection | Vial of 1 injection | Not stated in the licence record |
| 175756 | Prostin VR 500mcg Injection | Vial of 1 ml injection | Not stated in the licence record |
| 175429 | Prostal Injection | Vial of 1 ml injection | Not stated in the licence record |

---

## Safety Considerations

- **Contraindications (from the TxGNN model (deep learning), not label text; these may reflect similarities the model learned between related diseases, not biological evidence):** newborn and acute respiratory distress syndrome, hypotensive disorder, blood coagulation disease, sickle cell disease and other haemoglobinopathies, lung disease, plasma cell myeloma, leukaemia, polycythaemia, thrombocytosis, pyloric stenosis, priapism, Peyronie disease, urethral stricture, urethritis, balanitis and balanoposthitis.
- **Safety signals from the literature:** prolonged infusion in neonates has been linked to gastric outlet obstruction (antral foveolar hyperplasia and hypertrophic pyloric stenosis) and to pseudo-Bartter syndrome. Other recognised infusion effects in newborns include apnoea, fever and flushing.
- **Drug interactions:** 59 interactions were identified. Moderate-level interactions were found with SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), lorcaserin and sapropterin. Others, such as morphine, metformin, prednisone, simvastatin and vancomycin, have an unclassified severity level.

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication largely duplicates an existing use of alprostadil in ductal-dependent aortic lesions. The supporting evidence is limited to case reports, small clinical studies and preclinical work, with no registered trials. Little genuine repurposing value has been shown.

Several other predictions (congenital tricuspid stenosis, congenital valvular dysplasia, tricuspid valve agenesis and others) are model predictions only. Endemic goiter has no plausible mechanistic link and is likely a TxGNN model (deep learning) artefact. Heart septal defect has some case-report support but remains at the research-question stage.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indication text for the Indian products
- Detailed mechanism of action data
- Clarification of whether "aortic malformation" adds anything beyond the already established coarctation and interrupted aortic arch uses
- Controlled clinical data in specific lesion subtypes, if a distinct new use is pursued
- A neonatal safety monitoring plan for prolonged infusion (gastric outlet obstruction, apnoea, electrolyte disturbances)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

