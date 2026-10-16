---
layout: default
title: Pancuronium
parent: Model Prediction Only (L5)
nav_order: 640
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pancuronium: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not stated in the registration data compiled for this report (pancuro…"
monitor_inn: "Pancuronium"
predicted_indications: ["cauda equina syndrome", "irritable bowel syndrome", "obsolete neurogenic bladder (disease)", "neurocirculatory asthenia", "migraine disorder", "migraine with brainstem aura", "familial mitral valve prolapse", "mitral valve prolapse (disease)", "autonomic nervous system disease", "MVP1"]
---

# Pancuronium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Pancuronium: From Neuromuscular Blockade to Cauda Equina Syndrome

## One-Sentence Summary

Pancuronium is a non-depolarizing neuromuscular blocker, used as a muscle relaxant during anesthesia and mechanical ventilation. The TxGNN model predicts it may be effective for **cauda equina syndrome**, but **no clinical trials and no directly relevant publications** currently support this prediction. It rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data compiled for this report (pancuronium is generally known as a neuromuscular blocking agent) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, pancuronium is a non-depolarizing neuromuscular blocker. It antagonizes nicotinic acetylcholine receptors at the motor endplate and also has vagolytic activity.

The link to cauda equina syndrome is weak. Cauda equina syndrome is a compressive neurological emergency that normally requires surgical decompression, and neuromuscular blockade has no plausible disease-modifying role. The high TxGNN score (99.95%) is a model output only. It is not backed by trials or literature, and it likely reflects network proximity in the knowledge graph rather than a pharmacological rationale.

Other predictions had similarly weak rationale:

- **Irritable bowel syndrome** (99.93%): a theoretical antimuscarinic or vagolytic effect on gut motility, but a systemic neuromuscular blocker that needs ventilatory support is impractical for a chronic functional disorder.
- **Neurogenic bladder (obsolete term)** (99.89%): weak M2 blocking activity, but not a recognized or practical therapeutic route.
- **Neurocirculatory asthenia** (99.81%): pancuronium's sympathomimetic-like hemodynamic effects are the opposite of what would be needed.
- **Migraine and migraine with brainstem aura** (99.70% and 99.62%): no established mechanism.
- **Mitral valve prolapse (familial, general, and MVP1)** (99.48%, 99.48%, 99.40%): a structural valve disorder, and pancuronium's tachycardic effect could be undesirable.
- **Autonomic nervous system disease** (99.45%): the only prediction with a genuine pharmacological link, because pancuronium acts on autonomic pathways. However, the literature describes drug behavior in patients who already have autonomic dysfunction, not treatment of the disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for cauda equina syndrome.

---

## Literature Evidence

Currently no related literature available for cauda equina syndrome.

For reference, the publications found for the lower-ranked prediction **autonomic nervous system disease** are indirect. They are mostly anesthesia-management reports, hemodynamic studies, and animal experiments, and none shows that pancuronium treats autonomic disease:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7793215](https://pubmed.ncbi.nlm.nih.gov/7793215/) | 1995 | Clinical hemodynamic study | Acta Anaesthesiol Scand | Compared hemodynamic effects of vecuronium and pancuronium in diabetic patients with autonomic neuropathy during vitrectomy |
| [156745](https://pubmed.ncbi.nlm.nih.gov/156745/) | 1979 | Clinical observational | Intensive Care Med | Autonomic dysfunction in tetanus: morphine controlled sympathetic overactivity; sympathetic effects of pancuronium, d-tubocurarine and alcuronium discussed |
| [24558930](https://pubmed.ncbi.nlm.nih.gov/24558930/) | 2014 | Review | Masui | Anesthetic management in arrhythmogenic right ventricular cardiomyopathy |
| [2677433](https://pubmed.ncbi.nlm.nih.gov/2677433/) | 1989 | Case report | Masui | Anesthesia in a patient with Shy-Drager syndrome |
| [9227591](https://pubmed.ncbi.nlm.nih.gov/9227591/) | 1997 | Preclinical (rat) | Am J Physiol | Esophagocardiovascular reflex in rats |

For neurocirculatory asthenia, one retrieved paper ([2633661](https://pubmed.ncbi.nlm.nih.gov/2633661/), 1989, Ann Fr Anesth Reanim) concerns hemodynamics in liver transplantation with a veno-venous shunt. It is not about the predicted disease and provides no therapeutic evidence.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 152603 | Neocuron Injection | Vial of 2 ml injection | Not stated |
| 175813 | Pancuronium Bromide 2mg Injection | Vial of 2 ml injection | Not stated |
| 180269 | Panconium Injection | Vial of 2 ml injection | Not stated |

All three registrations are valid single-ingredient injectable products.

---

## Safety Considerations

**Drug Interactions:** 71 interactions were recorded. Major-level examples include:
- Paromomycin
- Kanamycin
- Neomycin

Moderate-level examples include:
- Aminoglycoside and glycopeptide antibiotics (vancomycin)
- Tetracyclines (doxycycline, tetracycline, minocycline)
- Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone)
- Amphotericin B
- Magnesium salts (magnesium sulfate, magnesium chloride)
- Mannitol
- Metoclopramide
- Trospium

Minor-level example: ranitidine.

Concomitant use with these agents may potentiate or alter neuromuscular blockade. The literature also notes that pancuronium's autonomic and hemodynamic effects (vagolytic tachycardia) could be a safety concern in patients with autonomic instability or arrhythmic conditions.

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for cauda equina syndrome is supported only by a model score (Evidence Level L5). There are no trials or literature, and no plausible mechanism links neuromuscular blockade to this condition. Pancuronium is also a hospital-administered injectable that requires ventilatory support, which limits practical repurposing. None of the other nine predicted indications has stronger support.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A credible mechanistic hypothesis and preclinical evidence for any candidate indication
- Route and setting compatibility assessment (injectable, ventilator-supported use)
- Evidence for **autonomic nervous system disease** reviewed first, as the only prediction with a pharmacological link, though current literature is indirect and safety-oriented
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

