---
layout: default
title: Amifostine
parent: Moderate Evidence (L3-L4)
nav_order: 47
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-30
description: "Amifostine: predicted new indication Hypertensive disorder (evidence level L5). Approved use: Not stated in the available licence records (the drug is known as a c…"
monitor_inn: "Amifostine"
predicted_indications: ["hypertensive disorder", "alopecia", "congenital hypotrichosis milia", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant renovascular hypertension", "malignant hypertensive renal disease", "Braddock syndrome", "hypotrichosis simplex of the scalp", "diffuse alopecia areata"]
---

# Amifostine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

## Amifostine: From Cytoprotection in Cancer Therapy to Hypertensive Disorder
{: .text-alpha }

## One-Sentence Summary

Amifostine is a cytoprotective agent used alongside chemotherapy and radiotherapy to protect normal tissues from treatment toxicity.
The TxGNN model predicts it may be effective for **hypertensive disorder**, but this is a model prediction only: **no clinical trials** are registered for this indication, and the **9 publications** retrieved are indirect (preclinical or oncology-supportive-care studies).
Amifostine can itself cause hypotension, which makes this prediction hard to justify.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence records (the drug is known as a cytoprotectant in cancer therapy) |
| Predicted New Indication | Hypertensive disorder |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L4 (preclinical and mechanistic literature only; no direct studies) |
| India Market Status | Listed in a compiled Indian medicine price dataset (8 of 8) – CDSCO approval status is not included in this data |
| Number of Registrations | 8 (valid: 8) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on published literature, amifostine is a thiophosphate prodrug. It is dephosphorylated to an active thiol that scavenges free radicals and protects normal tissue from radiation and chemotherapy damage.

The link to hypertension is weak and indirect. The retrieved papers describe protection against doxorubicin cardiotoxicity in hypertensive rats, renal protection during radionuclide therapy, and chemotherapy-induced (mitomycin, cisplatin) pulmonary vascular injury. These point to a general organ-protective role, not to blood-pressure-lowering or treatment of hypertension.

There is also a safety conflict. Amifostine commonly causes transient hypotension, so any use in hypertension would need to be carefully justified. The very high TxGNN score (0.99995) reflects a model prediction and does not replace clinical evidence.

Other predictions from the model include alopecia, several forms of pulmonary hypertension, malignant renovascular hypertension, and rare hair disorders. All are at L4 or L5 evidence, and all are on Hold.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11335791](https://pubmed.ncbi.nlm.nih.gov/11335791/) | 2001 | Clinical tolerability study | Anti-Cancer Drugs | Compared amifostine side effects in patients aged 70 and over with younger patients; transient hypotension was the most common side effect |
| [15560691](https://pubmed.ncbi.nlm.nih.gov/15560691/) | 2004 | Phase 2 | J Med Assoc Thai | Cisplatin-vinblastine with amifostine in advanced non-small cell lung cancer, testing toxicity reduction without loss of efficacy |
| [10755322](https://pubmed.ncbi.nlm.nih.gov/10755322/) | 2000 | Preclinical | Cancer Chemother Pharmacol | Compared amifostine and dexrazoxane against doxorubicin toxicity in spontaneously hypertensive rats |
| [19915842](https://pubmed.ncbi.nlm.nih.gov/19915842/) | 2010 | Review | Eur J Nucl Med Mol Imaging | Kidney protection during peptide receptor radionuclide therapy |
| [26130118](https://pubmed.ncbi.nlm.nih.gov/26130118/) | 2015 | Human disease and animal models | Circulation | Mitomycin-induced pulmonary veno-occlusive disease |
| [40479584](https://pubmed.ncbi.nlm.nih.gov/40479584/) | 2025 | Preclinical | Am J Respir Crit Care Med | FANCL deficiency and endothelial damage in alkylating-agent-associated pulmonary hypertension |
| [42850567](https://pubmed.ncbi.nlm.nih.gov/42850567/) | 2026 | Preclinical | Adv Sci (Weinh) | Alkylating-agent-induced FANCL impairment damages pulmonary vascular endothelium |
| [27855533](https://pubmed.ncbi.nlm.nih.gov/27855533/) | 2016 | Preclinical | Drug Delivery | Sustained-release amifostine microspheres for radioprotection with fewer side effects |
| [19395196](https://pubmed.ncbi.nlm.nih.gov/19395196/) | 2009 | Cohort | Int J Radiat Oncol Biol Phys | Wine as a radioprotective agent in breast cancer; amifostine is mentioned only as a costly comparator |

None of these studies tested amifostine as a treatment for hypertension.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 13570 | Amiget 500mg Injection | Vial of 5 ml injection | Not stated |
| 14477 | Amiphos 500mg Injection | Vial of 1 injection | Not stated |
| 145409 | M-Fost 500mg Injection | Vial of 1 injection | Not stated |
| 157917 | Natfost 500mg Injection | Vial of 1 injection | Not stated |
| 54035 | Chemophos 500mg Injection | Vial of 1 injection | Not stated |

There are 8 valid single-ingredient registrations in total, all injectables.

---

## Cytotoxicity

Amifostine is a cytoprotectant used with cytotoxic therapy, not a cytotoxic drug itself, so this section is omitted.

---

## Safety Considerations

- **Hypotension**: Transient hypotension is the most common side effect reported in the literature (PMID 11335791). This is a direct concern for any use in hypertensive patients.
- **Knowledge-graph contraindication signals** (from drug-disease links in the TxGNN knowledge graph, not label text): hypotensive disorder, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, stroke and cerebrovascular disorders, cerebral infarction, sudden cardiac arrest, heart conduction disease, myocardial ischaemia, coronary artery disease, transient ischaemic attack and vertebrobasilar insufficiency.
- **Drug Interactions**: 134 interactions were identified. Moderate-level interactions include:
  - Antihypertensives and vasodilators: acebutolol, nifedipine, fosinopril, aliskiren, alfuzosin, hydrochlorothiazide, amiloride, papaverine
  - Others: furosemide, mannitol, foscarnet

  Many interactions are of unknown severity, including pantoprazole, omeprazole, simvastatin, granisetron, ondansetron, aspirin, metoclopramide, dexamethasone and bupropion. Additive hypotension with antihypertensives is a particular concern.

Package insert warnings and contraindications were not available for this report, so please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. No clinical trials exist, the literature is indirect, and amifostine's known hypotensive effect and cardiovascular contraindication signals run against use in hypertension.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications for the Indian products
- Detailed mechanism of action data
- Direct preclinical evidence of a blood-pressure-lowering or vascular-protective effect
- A safety assessment of the hypotension risk and of interactions with antihypertensive drugs
- A better-supported alternative to evaluate, such as chemotherapy-induced alopecia, which has plausible but still indirect support (full-text review of toxicity outcomes in the oncology trials is needed)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

