---
layout: default
title: Digoxin
parent: Model Prediction Only (L5)
nav_order: 268
evidence_level: L5
indication_count: 5
monitor_inn: "Digoxin"
predicted_indications: ["Prinzmetal angina", "duodenal obstruction", "duodenal ulcer (disease)", "duodenogastric reflux", "hypoalphalipoproteinemia"]
last_modified_at: 2026-10-30
description: "Digoxin: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not recorded in the local data"
---

# Digoxin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Digoxin: Cardiac glycoside (Na+/K+-ATPase inhibitor) → Prinzmetal angina
{: .text-alpha }

## One-Sentence Summary

Digoxin is a cardiac glycoside used in heart rhythm and heart failure care. The TxGNN model predicts it may be relevant to **Prinzmetal angina**, but this is a model prediction only: **0 clinical trials** and **1 publication** are linked, and that publication does not study digoxin in this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 0.9981 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (19 of 19) – CDSCO approval status is not included in this data |
| Number of Registrations | 19 (valid: 19) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Digoxin is generally known to inhibit Na+/K+-ATPase, which raises intracellular calcium and increases cardiac contractility.

No established mechanistic link to Prinzmetal angina was identified. This condition is driven by coronary vasospasm and is typically treated with vasodilators such as calcium channel blockers and nitrates. Because digoxin can increase vascular tone, it could plausibly worsen vasospasm rather than relieve it.

The high prediction score is therefore best treated as a model signal that needs scrutiny, not as evidence of benefit. The only linked paper is a 1999 review on chronopharmacology of antihypertensive treatment. It is not specific to digoxin or to Prinzmetal angina.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta physiologica et pharmacologica Bulgarica | General review of circadian rhythms and their impact on antihypertensive treatment; does not address digoxin or Prinzmetal angina |

## India Market Information

Digoxin is marketed in India. All 19 single-ingredient licences in the data compiled for this report are valid, and none are cancelled. No approved indication text is recorded for them. Main authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 38328 | Cardioxin 0.25mg Tablet | Strip of 10 tablets | Not recorded |
| 120831 | Lanoxin Tablet | Strip of 10 tablets | Not recorded |
| 59517 | Digon Tablet | Strip of 10 tablets | Not recorded |
| 62540 | Dixin 3mg Syrup | Bottle of 60 ml syrup | Not recorded |
| 59678 | Dixin 0.25mg Injection | Vial of 2 injections | Not recorded |

Available forms include tablets, syrup, elixir, oral solution and injection.

## Safety Considerations

- **Disease-related cautions (from relationship data, not label text):** digoxin is recorded as contraindicated or problematic in conditions including myocardial infarction, Wolff-Parkinson-White syndrome, sick sinus syndrome, atrioventricular block, ventricular fibrillation, hypertrophic and restrictive cardiomyopathy, constrictive pericarditis, myocarditis, cor pulmonale, kidney disease, hypercalcemia, potassium deficiency, and hypothyroidism/myxedema.
- **Drug Interactions:** 304 interactions were found. Examples at moderate level include acarbose, rabeprazole, doxycycline, epinephrine, hydrocortisone, metformin, amphotericin B, bupropion, dexamethasone, tetracycline and acetylsalicylic acid. Minor examples include atropine, hyoscyamine and glycopyrronium.

Please also refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. No trials exist, the single linked paper is unrelated to digoxin in this disease, and the pharmacology suggests possible harm in coronary vasospasm.

**To proceed, the following is needed:**
- Direct clinical or preclinical studies of digoxin in coronary vasospasm or Prinzmetal angina
- Mechanism of action data and a clear mechanistic rationale
- Package insert warnings and contraindications for a proper safety review
- Assessment of vasoconstriction risk in patients with vasospastic angina
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

