---
layout: default
title: Conivaptan
parent: Moderate Evidence (L3-L4)
nav_order: 211
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-14
description: "Conivaptan: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Not stated in the Indian license data (conivaptan is generally used f…"
monitor_inn: "Conivaptan"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "Prinzmetal angina", "migraine with brainstem aura", "kyphoscoliotic heart disease", "peripheral arterial disease", "peripheral vascular disease"]
---

# Conivaptan
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

## Conivaptan: From Hyponatremia (Injectable Vasopressin Antagonist) to Pulmonary Hypertension
{: .text-alpha }

## One-Sentence Summary

Conivaptan is an injectable vasopressin V1A/V2 receptor antagonist, marketed in India under the brand Hyponat 20 mg Injection.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but the supporting evidence is thin: **1 clinical trial** (withdrawn, no participants enrolled) and **1 review article** on hyponatremia in heart failure.
At this stage the prediction is a research question, not an evidence-backed indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Indian license data (conivaptan is generally used for hyponatremia) |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 0.9952 |
| Evidence Level | L4 (preclinical and mechanistic support only; the one trial was withdrawn) |
| India Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Conivaptan is a dual vasopressin V1A/V2 receptor antagonist. Blocking V2 receptors promotes aquaresis (excretion of free water without major electrolyte loss), which may help control body volume. Blocking V1A receptors may reduce vasopressin-driven vasoconstriction.

In pulmonary arterial hypertension with right ventricular failure, sodium and water retention is driven partly by secondary hyperaldosteronism and non-osmotic vasopressin release. A V2 antagonist could in theory ease this volume overload. The link is plausible but indirect. It mainly supports managing hyponatremia and congestion in heart failure, not treating the pulmonary vascular disease itself.

Detailed mechanism of action data was not available in the data compiled for this report. The mechanistic description above is based on the known pharmacology of conivaptan.

Other model predictions (migraine disorder, Prinzmetal angina, migraine with brainstem aura, kyphoscoliotic heart disease, peripheral arterial disease, peripheral vascular disease) have no supporting trials, or only unrelated literature. They are not developed further here.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00811486](https://clinicaltrials.gov/study/NCT00811486) | NA | Withdrawn | 0 | Planned study of body volume regulation in pulmonary arterial hypertension with right ventricular failure, using a mineralocorticoid antagonist plus a V2 antagonist. Withdrawn with no participants, so it produced no efficacy or safety data. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30843491](https://pubmed.ncbi.nlm.nih.gov/30843491/) | 2019 | Review | Current Cardiology Reviews | Pathogenesis and management of hyponatremia in heart failure. Relevant to volume handling, not directly to pulmonary hypertension. |
| [15847853](https://pubmed.ncbi.nlm.nih.gov/15847853/) | 2005 | Review | American Journal of Cardiology | Treatments for hyponatremia in congestive heart failure. Linked to the peripheral arterial disease prediction and does not address vascular disease. |
| [10448882](https://pubmed.ncbi.nlm.nih.gov/10448882/) | 1999 | Preclinical | European Journal of Pharmacology | Cardiovascular and renal effects of conivaptan (YM087) in dogs with pacing-induced heart failure. Linked to the peripheral vascular disease prediction. Pharmacology and hemodynamics only. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 104711 | Hyponat 20mg Injection (Zydus Cadila) | Vial of 4 ml injection | Not stated in the license data |

## Safety Considerations

- **Drug Interactions**: The interaction screen identified 180 potential interacting drugs. Examples of **Major** interactions include loperamide, triamcinolone, budesonide, clarithromycin, cisapride, eliglustat, and naloxegol. **Moderate** interactions include rabeprazole, hydrocortisone, dexamethasone, betamethasone, aprepitant, granisetron, miconazole, eluxadoline, and naldemedine. Many of these (for example clarithromycin) are consistent with CYP3A4-related effects, but the data compiled for this report do not specify the mechanism.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score (0.9952) is a computational prediction. The only trial was withdrawn without enrolling anyone, and the literature consists of reviews on heart-failure hyponatremia and animal pharmacology. The mechanistic link is plausible but indirect, so there is no clinical evidence for pulmonary hypertension.

**To proceed, the following is needed:**
- Package insert warnings, contraindications, and approved indication text for Hyponat 20 mg Injection (currently missing and blocking safety screening)
- Detailed mechanism of action data
- Clinical data in pulmonary hypertension, such as a well-designed pilot or Phase 2 study, especially in right heart failure with volume overload
- Evaluation of the clinical relevance of the many Major drug interactions
- Assessment of whether the injectable-only route suits the intended use in pulmonary hypertension
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

