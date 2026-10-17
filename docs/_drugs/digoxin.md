---
layout: default
title: Digoxin
parent: Model Prediction Only (L5)
nav_order: 268
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Digoxin: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Atrial fibrillation"
monitor_inn: "Digoxin"
predicted_indications: ["Prinzmetal angina", "duodenal obstruction", "duodenal ulcer (disease)", "duodenogastric reflux", "obsolete susceptibility to ischemic stroke", "hypoalphalipoproteinemia"]
---

# Digoxin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Digoxin: From Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Digoxin is a cardiac glycoside originally used for atrial fibrillation and digitalis poisoning.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but there are currently **no clinical trials** and only **1 loosely related publication** supporting this direction.
This is a model-only prediction, and the available mechanistic reasoning actually points toward possible harm.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation; digitalis poisoning (from the knowledge graph, as the regulatory records contain no approved indication text) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 19 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, digoxin inhibits the Na+/K+-ATPase pump, which raises intracellular calcium. This increases cardiac contractility and slows atrioventricular conduction, which is why it is used for rate control in atrial fibrillation.

Prinzmetal angina, however, is caused by coronary vasospasm and is usually treated with vasodilators such as calcium channel blockers and nitrates. The rise in intracellular calcium and vascular tone from digoxin could plausibly worsen vasospasm rather than relieve it. There is therefore no established mechanistic link between digoxin and this condition.

The high TxGNN score is most likely an artifact of the knowledge graph, which links drugs and diseases through shared network neighbours rather than demonstrated biology. The only linked paper is a review on chronopharmacology in antihypertensive treatment, which is not specific to digoxin or Prinzmetal angina.

Other predicted indications (duodenal obstruction, duodenal ulcer, duodenogastric reflux, an obsolete ischemic stroke susceptibility term, and hypoalphalipoproteinemia) have no plausible mechanistic rationale either, and all remain at evidence level L5.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiol Pharmacol Bulg | General review of circadian rhythms and chronopharmacology in antihypertensive treatment; not specific to digoxin or Prinzmetal angina |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 38328 | Cardioxin 0.25mg Tablet | Strip of 10 tablets | Not stated in the available records |
| 120831 | Lanoxin Tablet | Strip of 10 tablets | Not stated in the available records |
| 123301 | Lanoxin Syrup | Bottle of 30 ml syrup | Not stated in the available records |
| 59678 | Dixin 0.25mg Injection | Vial of 2 injections | Not stated in the available records |
| 204387 | Sangoxin 0.25mg Tablet | Strip of 14 tablets | Not stated in the available records |

There are 19 valid single-ingredient registrations in total, covering oral tablets, syrups, elixir, oral solution and injections.

---

## Safety Considerations

- **Contraindications (from knowledge graph associations, not label text)**: kidney disease, potassium deficiency, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, myocardial infarction, coronary thrombosis, hemoglobinopathy, cor pulmonale, Wolff-Parkinson-White syndrome, sick sinus syndrome, ventricular fibrillation, hypertrophic cardiomyopathy, atrioventricular block, myxedema, hypothyroidism, myocarditis, constrictive pericarditis, restrictive cardiomyopathy.
- **Drug Interactions**: 304 interactions were recorded. Examples at moderate level include acarbose, rabeprazole, doxycycline, epinephrine, hydrocortisone, metformin, amphotericin B, bupropion, acetylsalicylic acid, dexamethasone and tetracycline. Minor-level examples include albiglutide, hyoscyamine, atropine and glycopyrronium.
- Many of the contraindicated conditions are cardiac. Given the predicted indication is also a cardiac condition (coronary vasospasm), caution is especially warranted.

Please also refer to the package insert for full warnings, as label-based warnings and contraindications were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a model score, with no clinical trials and no relevant literature. Digoxin's known pharmacology could worsen coronary vasospasm, so the high score is likely a graph artifact rather than a real therapeutic signal.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian-marketed products (currently missing, and blocking safety screening)
- Detailed mechanism of action data from DrugBank
- Any preclinical or clinical evidence specifically linking digoxin to coronary vasospasm
- A safety assessment of digoxin in patients with coronary artery disease and vasospastic angina
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

