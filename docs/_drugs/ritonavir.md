---
layout: default
title: Ritonavir
parent: Model Prediction Only (L5)
nav_order: 746
evidence_level: L5
indication_count: 3
monitor_inn: "Ritonavir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-30
description: "Ritonavir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: Chronic hepatitis C virus infection, hepatitis C virus infection…"
---

# Ritonavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Ritonavir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Ritonavir is an HIV protease inhibitor, recorded in the knowledge graph for HIV/AIDS and hepatitis C virus infection.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but **no clinical trials and no publications** directly support this prediction.
The evidence is model prediction only, and the high score likely reflects the disease's network proximity to HIV/AIDS.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus infection, hepatitis C virus infection, HIV infectious disease and AIDS (relations recorded in the knowledge graph; the licence records contain no approved indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (17 of 17) – CDSCO approval status is not included in this data |
| Number of Listed Products | 17 (valid: 17) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general drug knowledge, ritonavir is an HIV-1 protease inhibitor and a strong CYP3A4 inhibitor. These details are not drawn from the compiled data, so please verify them.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV, so a protease-based rationale is conceivable. However, FIV protease differs from HIV-1 protease in substrate specificity, and HIV-1 protease inhibitors are generally reported to have limited activity against it. The very high score comes from the TxGNN model (deep learning) and most likely reflects similarities the model learned between related diseases, such as HIV/AIDS, not biological evidence.

For context, the second-ranked prediction, **simian immunodeficiency virus infection** (same score of 0.9992), has some supporting literature. This includes an in vitro study showing SIVmac239 is inhibited by ritonavir (EC50 about 13 nM, versus about 25 nM for HIV-1; PMID 12709355) and several macaque studies of combination antiretroviral regimens. These are animal models of HIV rather than human therapeutic indications, and ritonavir's individual contribution is not isolated in the combination studies. The third prediction, a rare genetic neurodevelopmental disorder, has no identifiable mechanistic link to ritonavir.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for feline acquired immunodeficiency syndrome.

---

## India Market Information

Ritonavir is marketed in India with 17 valid single-ingredient approvals. The licence records contain no approved indication text. The five listed below are examples of the 17.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 127028 | Lopimune 50 mg/200 mg Capsule (Cipla Ltd) | Strip of 30 capsules | Not stated in the records |
| 195263 | Ritomax 100mg Capsule (Alkem Laboratories Ltd) | Box of 60 capsules | Not stated in the records |
| 235925 | Viriton 100mg Tablet (Sun Pharmaceutical Industries Ltd) | Bottle of 60 tablets | Not stated in the records |
| 76377 | Empetus 100mg Tablet (Emcure Pharmaceuticals Ltd) | Strip of 30 tablets | Not stated in the records |
| 185243 | Ritomune 100mg Capsule (Cipla Ltd) | Strip of 30 capsules | Not stated in the records |

All products are oral formulations (capsules and tablets). No veterinary product is listed.

---

## Safety Considerations

**Knowledge-graph contraindication relations** (these are graph relations, not label text) include:
- **Cardiac and conduction:** long QT syndrome, familial long QT syndrome, torsades de pointes, sudden cardiac arrest, heart conduction disease, atrioventricular block, myocardial ischemia, coronary artery disease, cardiomyopathy, hypertrophic cardiomyopathy
- **Liver and biliary:** liver disease, cirrhosis of liver, gallbladder disease, hyperbilirubinemia, Gilbert syndrome, chronic hepatitis B virus infection
- **Metabolic:** diabetes mellitus, diabetic ketoacidosis, hyperglycemia, hypertriglyceridemia, familial combined hyperlipidemia, potassium deficiency disease, gout
- **Other:** pancreatitis, hemophilia

**Drug interactions:** 343 interactions are recorded. Examples include:
- **Major:** loperamide, triamcinolone, budesonide
- **Moderate:** acarbose, metformin, alogliptin, canagliflozin, chlorpropamide, bupropion, aprepitant, clarithromycin, metronidazole, dexamethasone, hydrocortisone, betamethasone

Please refer to the package insert for label warnings and contraindications, which are not available in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication directly studies ritonavir in feline acquired immunodeficiency syndrome, so the evidence level is L5 and the high score is not independent support. Ritonavir has a large number of drug interactions and many knowledge-graph contraindication relations. Any use in cats would be a veterinary question outside human drug repurposing.

**To proceed, the following is needed:**
- Mechanism of action data and package insert warnings and contraindications
- Direct evidence of ritonavir activity against FIV, for example in vitro protease inhibition and veterinary studies
- A decision on whether a veterinary indication is within the scope of this programme
- If a different target is preferred, a review of the SIV literature for ritonavir-specific findings. This is a preclinical model, not a human indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

