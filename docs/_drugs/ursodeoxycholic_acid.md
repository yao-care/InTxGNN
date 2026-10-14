---
layout: default
title: Ursodeoxycholic Acid
parent: Model Prediction Only (L5)
nav_order: 877
evidence_level: L5
indication_count: 1
---

# Ursodeoxycholic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Ursodeoxycholic Acid: From Gallstone and Biliary Disease to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Ursodeoxycholic acid (UDCA) is a bile acid originally used to treat gallstone disease (cholelithiasis, cholecystolithiasis, choledocholithiasis) and primary biliary cholangitis.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia (HoFH)**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cholelithiasis, cholecystolithiasis, choledocholithiasis, primary biliary cholangitis, Reynolds syndrome (from the knowledge graph; the approved indication text on Indian licences is blank) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, UDCA is a bile acid with established use in gallstone dissolution and primary biliary cholangitis, and it acts on bile acid and cholesterol metabolism, so it may be mechanistically linked to a lipid disorder.

A plausible but unverified link runs through cholesterol handling. UDCA is reported to reduce intestinal cholesterol absorption and to suppress hepatic cholesterol synthesis and secretion, and it may lower LDL cholesterol modestly. This shared lipid and bile acid pathway is the most likely reason the graph model connects the drug to hypercholesterolemia.

The mechanistic case is weak, however. HoFH is caused mainly by LDL receptor dysfunction (variants in LDLR, APOB, PCSK9 or LDLRAP1), and its LDL elevation is largely independent of the pathways UDCA affects. A meaningful effect is therefore doubtful. The high score most likely reflects network proximity in the knowledge graph (shared lipid and bile acid nodes) and not demonstrated efficacy.

## India Market Information

UDCA is marketed in India as single-ingredient oral tablets, with 20 valid registrations and none cancelled. The approved indication text is not listed for these registrations. Five representative registrations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 232290 | UD Dox 300mg Tablet | Strip of 10 tablets | Not listed |
| 230251 | Urdohep 300 Tablet | Strip of 10 tablets | Not listed |
| 231713 | Udcasafe 300mg Tablet | Strip of 10 tablets | Not listed |
| 231464 | Uvido 300mg Tablet | Strip of 10 tablets | Not listed |
| 200052 | Shinoliv 300mg Tablet | Strip of 10 tablets | Not listed |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 272 potential interactions. The first 20 entries listed include:
  - Minor: cyclosporine, aluminum hydroxide, magaldrate
  - Severity not classified: cyanocobalamin, calcitriol, folic acid, pravastatin, ramipril, lorazepam, tramadol, fluconazole, oseltamivir, erythromycin, sildenafil, pantoprazole, citalopram, moxifloxacin, nelfinavir, glimepiride, indinavir
  - Of note for a lipid indication, pravastatin (a statin) appears among the interacting drugs, and its severity is not classified. Concomitant use with lipid-lowering therapy would need review.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (evidence level L5), and the proposed mechanism is doubtful because HoFH is driven by LDL receptor defects that UDCA does not address. The drug's established safety record and wide Indian availability do not offset the lack of efficacy evidence.

**To proceed, the following is needed:**
- Mechanism of action data for UDCA, to allow a proper mechanistic analysis
- Package insert warnings and contraindications for Indian products (the safety screen cannot proceed without them)
- Preclinical or clinical data showing an LDL-lowering effect of UDCA in HoFH or related LDL receptor-deficient models
- A review of the literature on UDCA and LDL cholesterol in other lipid disorders
- Assessment of interactions with standard HoFH therapies, including statins
- Confirmation of route compatibility (the oral tablet is the only Indian dosage form listed)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

