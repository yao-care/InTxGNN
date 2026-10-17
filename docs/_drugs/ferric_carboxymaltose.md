---
layout: default
title: Ferric Carboxymaltose
parent: Model Prediction Only (L5)
nav_order: 347
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ferric Carboxymaltose: predicted new indication Bronchitis (evidence level L5). Approved use: Not stated in the India license data (the product is an intravenous i…"
monitor_inn: "Ferric carboxymaltose"
predicted_indications: ["bronchitis", "thrombotic disease", "rheumatoid arthritis", "bronchial neoplasm (disease)", "idiopathic granulomatous myositis", "myositis fibrosa", "exostosis", "laryngotracheitis", "tendinitis", "heparin cofactor 2 deficiency"]
---

# Ferric Carboxymaltose
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

# Ferric Carboxymaltose: From Iron Deficiency Replacement to Bronchitis

## One-Sentence Summary

Ferric carboxymaltose is an intravenous iron replacement product marketed in India. The TxGNN model predicts it may be effective for **bronchitis**, but this prediction rests on the graph model alone, with **0 clinical trials** and **0 publications** currently supporting it. Evidence is limited to model prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India license data (the product is an intravenous iron replacement) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.00% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 14 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ferric carboxymaltose is an intravenous iron preparation used to correct iron deficiency, and its efficacy in iron repletion is established.

For bronchitis, no identifiable mechanistic link exists in the data compiled for this report. Nothing connects iron repletion to airway inflammation or infection. The high score (0.990) is a graph-based prediction only, and the TxGNN rank (14,476) is not a sign of independent support.

Other top-ranked predictions were also reviewed:
- **Thrombotic disease** (score 98.04%, L4): Iron deficiency is linked to reactive thrombocytosis and a prothrombotic tendency, and iron repletion may lower platelet counts. This suggests a possible reduction of thrombotic risk factors in iron-deficient patients, but it does not show that the drug treats thrombotic disease.
- **Rheumatoid arthritis** (score 96.88%, L4): The drug appears effective and safe for iron-deficiency anaemia in inflammatory rheumatic disease. This is a supportive-care benefit, not disease modification.
- **Bronchial neoplasm, granulomatous myositis, myositis fibrosa, exostosis, laryngotracheitis, tendinitis and heparin cofactor 2 deficiency**: No supporting evidence or plausible mechanism was found.

## Clinical Trial Evidence

Currently no related clinical trials registered for bronchitis.

## Literature Evidence

Currently no related literature available for bronchitis.

For context, the literature linked to the second-ranked prediction (thrombotic disease) is listed below. It is indirect and does not support bronchitis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36282723](https://pubmed.ncbi.nlm.nih.gov/36282723/) | 2023 | Review | European Heart Journal | Iron deficiency is common in cardiovascular disease, including coronary artery disease, heart failure and pulmonary hypertension |
| [41912474](https://pubmed.ncbi.nlm.nih.gov/41912474/) | 2026 | Cohort | Renal Failure | IV ferric carboxymaltose in non-dialysis CKD patients with iron deficiency; effects on platelet counts and transferrin, with possible implications for thrombogenicity |
| [32079699](https://pubmed.ncbi.nlm.nih.gov/32079699/) | 2021 | Preclinical (animal) | Haematologica | In rats, iron deficiency-induced thrombocytosis increased thrombotic tendency; ferric carboxymaltose was used to reverse iron deficiency |
| [42785516](https://pubmed.ncbi.nlm.nih.gov/42785516/) | 2026 | Review/Observational | Journal of Pediatrics | Comparison of effectiveness and safety of IV iron formulations in children with iron deficiency |

## India Market Information

Fourteen valid single-ingredient registrations are on record. The approved indication text is not available in the license data. The five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 72698 | Encicarb 1K Injection (Emcure Pharmaceuticals) | Vial of 20 ml injection | Not available |
| 120929 | Larinject 50mg Injection (La Renon Healthcare) | Vial of 10 ml injection | Not available |
| 84463 | Ferinject 50mg/ml Solution for Injection (Lupin) | Vial of 20 ml solution for injection | Not available |
| 184334 | Revofer Solution for Injection (Lupin) | Vial of 10 ml solution for injection | Not available |
| 161707 | Orofer FCM 1K Injection (Emcure Pharmaceuticals) | Vial of 20 ml injection | Not available |

## Safety Considerations

- **Drug Interactions** (5 recorded):
  - **Major**: Dimercaprol
  - **Moderate**: Iron, ferrous fumarate, ferrous gluconate, chloramphenicol
- **Other safety note**: Ferric carboxymaltose is known to cause hypophosphatemia, which is relevant to bone health with repeated dosing.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction has no clinical trials, no literature and no identifiable mechanism, so it rests on the TxGNN score alone (evidence level L5). The drug's established role is correcting iron deficiency, and the stronger signals (thrombotic disease, rheumatoid arthritis) reflect benefits of treating iron deficiency in those populations, not direct treatment of the disease.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator or manufacturers, since safety screening cannot proceed without them
- Mechanism of action data (for example from DrugBank)
- Approved indication text for the registered products
- Any preclinical or clinical rationale connecting iron repletion to airway disease, before further investment
- If a repurposing direction is pursued, consider the better-supported iron-deficiency anaemia settings (for example inflammatory rheumatic disease or cardiovascular disease) rather than bronchitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

