---
layout: default
title: Cimetidine
parent: Model Prediction Only (L5)
nav_order: 183
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Cimetidine: predicted new indication Smouldering systemic mastocytosis (evidence level L5). Approved use: Gastric ulcer, gastroesophageal reflux disease, duodenal ulcer…"
monitor_inn: "Cimetidine"
predicted_indications: ["peptic ulcer perforation", "lymphoadenopathic mastocytosis with eosinophilia", "duodenal obstruction", "acne (disease)", "abnormality of glucagon secretion"]
---

# Cimetidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Cimetidine: From Gastric Ulcer to Smouldering Systemic Mastocytosis
{: .text-alpha }

## One-Sentence Summary

Cimetidine is a histamine H2-receptor blocker, originally used to treat gastric and duodenal ulcers, reflux disease and gastric hypersecretory conditions.
The TxGNN model predicts it may be effective for **Smouldering Systemic Mastocytosis**,
but there are currently **0 clinical trials** and **0 publications** specific to this indication, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric ulcer, gastroesophageal reflux disease, duodenal ulcer, Zollinger-Ellison syndrome, systemic mastocytosis and related conditions (the India licence records list no approved indication text) |
| Predicted New Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cimetidine is a histamine H2-receptor antagonist. Its efficacy in acid-related conditions is well established, and mechanistically it may be applicable to smouldering systemic mastocytosis.

Cimetidine already appears among the known indications for systemic mastocytosis and mastocytosis. In these diseases, excess histamine from mast cells drives gastric acid hypersecretion and related symptoms. Blocking H2 receptors reduces that effect. Smouldering systemic mastocytosis is a subtype of the same disease family, so a high model score is plausible.

Note that this is symptom control (acid-related symptoms), not treatment of the underlying mast cell disease. No trials or publications were found for this specific subtype.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top predicted indication.

For context, the second-ranked prediction, active peptic ulcer disease (an on-label use rather than true repurposing), has only one possibly direct trial: a 1981 double-blind study of 72 patients with cimetidine, antacid/anticholinergic and placebo, in which 3-week healing was 67% with cimetidine (p<0.005 vs placebo). Its design cannot be fully verified from the title and abstract alone.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT (probable) | Scand J Gastroenterol | Cimetidine vs antacid/anticholinergic vs placebo in active duodenal and prepyloric ulcers; 67% healing at 3 weeks with cimetidine |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 231297 | Ulciban 400mg Tablet (Torrent Pharmaceuticals) | Strip of 10 tablets | Not specified in the data compiled |
| 223407 | Tagasec 200mg Tablet (Taj Pharma India) | Strip of 10 tablets | Not specified in the data compiled |
| 43394 | Cimetiget 200mg Tablet (Franco-Indian Pharmaceuticals) | Strip of 10 tablets | Not specified in the data compiled |
| 155392 | Neotid 400mg Tablet (Neon Laboratories) | Strip of 10 tablets | Not specified in the data compiled |
| 39684 | Cimetiget 400mg Tablet (Franco-Indian Pharmaceuticals) | Strip of 10 tablets | Not specified in the data compiled |

All 8 registrations are valid single-ingredient oral tablet products. Only the first five are listed here.

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** liver disease, gallbladder disease, impaired renal function, and gastric cancer or neoplasm (including diffuse gastric adenocarcinoma, linitis plastica and gastric carcinoma).
- **Drug interactions:** 551 interactions were recorded. Examples at moderate level include paclitaxel, fentanyl, acalabrutinib, lidocaine, acebutolol, dihydrocodeine, codeine, tramadol, nifedipine and alfentanil. Minor-level examples include dolutegravir, zidovudine, acetaminophen, ibuprofen, ketorolac, ethinylestradiol, albendazole and ethanol.
- **Literature signals:** the supplied literature includes reports of ulcer perforation while on cimetidine, gynaecomastia, and an increased risk of nosocomial pneumonia with H2 blockers in stress ulcer prophylaxis.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction scores very high (99.80%), but it is supported only by the model and by cimetidine's existing use in mastocytosis. No trials or publications exist for the smouldering subtype, and any benefit would likely be limited to symptom control.

Other predictions rank similarly. Active peptic ulcer disease, gastrojejunal ulcer, duodenogastric reflux and duodenal obstruction are L4, largely on-label or indirect evidence, and PPIs have largely replaced H2 blockers. Peptic ulcer perforation is likely a model artifact, as reports describe perforation occurring during cimetidine therapy. Acne (anti-androgenic mechanism) is a research question only. Abnormality of glucagon secretion is L5 and appears to be a knowledge-graph artifact.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank
- Package insert warnings and contraindications for the India-marketed products, which are currently missing and block safety screening
- Clinical or observational data on cimetidine in smouldering systemic mastocytosis, including comparison with current standard symptom control
- Review of the interaction profile (especially the moderate-level interactions) and the liver, kidney and gallbladder contraindication signals before any patient-facing use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

