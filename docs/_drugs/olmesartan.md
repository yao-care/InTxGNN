---
layout: default
title: Olmesartan
parent: Model Prediction Only (L5)
nav_order: 617
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Olmesartan: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not stated in the available licence data (olmesartan is an ARB…"
monitor_inn: "olmesartan"
predicted_indications: ["Prinzmetal angina", "hypotrichosis simplex of the scalp", "migraine disorder", "alopecia", "pulmonary hypertension", "congenital hypotrichosis milia", "diffuse alopecia areata", "migraine with brainstem aura", "kyphoscoliotic heart disease", "open-angle glaucoma"]
---

# Olmesartan
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

## Olmesartan: From Hypertension to Prinzmetal Angina
{: .text-alpha }

## One-Sentence Summary

Olmesartan is an angiotensin II receptor blocker (ARB) marketed in India, mainly in antihypertensive products, though the registered indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but this is a model prediction only, with **0 clinical trials** and **0 publications** behind it.
The strongest evidence among the top 10 predictions is for **migraine disorder** (3 publications, including a 2019 systematic review of ACE inhibitors and ARBs).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence data (olmesartan is an ARB, typically used for hypertension) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Olmesartan belongs to the ARB class, which blocks the angiotensin II type 1 (AT1) receptor. This lowers vasoconstriction and blood pressure.

For Prinzmetal angina (coronary vasospasm), a plausible but speculative link is that reduced angiotensin II-driven vasoconstriction could affect coronary spasm. No trials or publications support this, and the high score comes from the TxGNN model (deep learning). It may reflect similarities the model learned between related diseases, not biological evidence.

Other predictions in the top 10 vary in plausibility:
- **Migraine disorder** has the most supporting literature (see below). The evidence is mostly from hypertensive patients, so benefit in people with normal blood pressure is unclear.
- **Pulmonary hypertension** has preclinical support only (rat and mouse models, evidence level L4).
- **Hair-related conditions** (hypotrichosis simplex of the scalp, alopecia, congenital hypotrichosis milia, diffuse alopecia areata) have no plausible mechanism and no evidence. The scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.
- **Open-angle glaucoma** has only a general treatment review with no olmesartan-specific data.
- **Migraine with brainstem aura** and **kyphoscoliotic heart disease** have no subtype-specific evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for Prinzmetal angina.

For reference, the only trial in the top 10 predictions was linked to pulmonary hypertension and is not relevant to it:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04330300](https://clinicaltrials.gov/study/NCT04330300) | Phase 4 | Suspended | 2414 | Continuing vs stopping ACE inhibitor/ARB in COVID-19 patients (CORONACION); does not address pulmonary hypertension |

---

## Literature Evidence

Currently no related literature is available for Prinzmetal angina.

The best-supported alternative prediction is migraine disorder:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31515634](https://pubmed.ncbi.nlm.nih.gov/31515634/) | 2019 | Systematic review | Curr Pain Headache Rep | ACE inhibitors and ARBs for preventing episodic migraine in adults; identifies research gaps and guides future trials |
| [16618270](https://pubmed.ncbi.nlm.nih.gov/16618270/) | 2006 | Clinical study | Headache | Effect of olmesartan on migraine frequency and severity in patients with hypertension or prehypertension |
| [16942482](https://pubmed.ncbi.nlm.nih.gov/16942482/) | 2006 | Commentary | Headache | Commentary on olmesartan, migraine and blood pressure |

Preclinical evidence for pulmonary hypertension:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18209564](https://pubmed.ncbi.nlm.nih.gov/18209564/) | 2008 | Preclinical | J Cardiovasc Pharmacol | Olmesartan medoxomil tested in the rat monocrotaline pulmonary hypertension model |
| [16336959](https://pubmed.ncbi.nlm.nih.gov/16336959/) | 2005 | Preclinical | Eur J Pharmacol | Olmesartan medoxomil in chronic hypoxic rats, evaluating hypoxic pulmonary hypertension |
| [17089097](https://pubmed.ncbi.nlm.nih.gov/17089097/) | 2006 | Preclinical | Naunyn Schmiedebergs Arch Pharmacol | Olmesartan reduced hypoxia-induced ERK1/2 activation and pro-inflammatory signalling in mouse lung |

---

## India Market Information

Twenty valid registrations are listed. Approved indication text is not available for any of them. Main examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 161843 | Olmin Trio 40 Tablet (Eris Lifesciences) | Strip of 10 tablets | Not available |
| 164832 | Olmedox 20mg Tablet (Caplet India) | Strip of 10 tablets | Not available |
| 164446 | Olmy-CH 20mg/12.5mg Tablet (Zydus Cadila) | Strip of 10 tablets | Not available |
| 169144 | Olmesat AM 20mg/5mg Tablet (Biocon) | Strip of 10 tablets | Not available |
| 162087 | Olmy-D 40 Tablet SR (Zydus Cadila) | Strip of 10 tablet SR | Not available |

---

## Safety Considerations

- **Drug Interactions**: 94 interactions were identified. Notable examples:
  - **Major**: potassium chloride and potassium bicarbonate (risk of hyperkalaemia).
  - **Moderate**: hydrocortisone, eluxadoline, exenatide, polyethylene glycol with electrolytes, and numerous insulin products (insulin human, aspart, degludec, detemir, glargine, glulisine, lispro and others).
- **Pregnancy**: A 2026 case report notes that ARBs are contraindicated in pregnancy because of risks such as oligohydramnios, renal dysgenesis and pulmonary hypoplasia.

Please refer to the package insert for other warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Prinzmetal angina prediction rests on a model score alone (evidence level L5) with no trials or literature, and the mechanistic link is speculative. Migraine is the most promising alternative, with a systematic review and olmesartan-specific reports, but the evidence is mostly from hypertensive populations and warrants further research rather than a go decision.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- Registered indication text for the Indian licences
- Any clinical or mechanistic evidence for coronary vasospasm
- For migraine, a controlled trial that includes normotensive patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

