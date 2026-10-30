---
layout: default
title: Bacampicillin
parent: Model Prediction Only (L5)
nav_order: 87
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Bacampicillin: predicted new indication Epiglottitis (evidence level L4). Approved use: Urinary tract infection, gonorrhea, pharyngitis…"
monitor_inn: "Bacampicillin"
predicted_indications: ["epiglottitis", "abdominal ectopic pregnancy", "abdominal cystic lymphangioma", "celiac trunk compression syndrome", "lymph node palisaded myofibroblastoma", "sacrum chordoma", "disease of retroperitoneum", "disease of uterine broad ligament", "urethral disease", "disease of peritoneum"]
---

# Bacampicillin
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

## Bacampicillin: From Urinary Tract Infection to Epiglottitis
{: .text-alpha }

## One-Sentence Summary

Bacampicillin is an oral prodrug of ampicillin, originally used to treat urinary tract infection, gonorrhea, pharyngitis and sinusitis.
The TxGNN model predicts it may be effective for **epiglottitis**, but **no clinical trials and no publications** currently support this specific prediction.
The only study found among the top-ranked predictions is a small 1989 pilot study in a different condition (urethral disease).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, gonorrhea, pharyngitis, sinusitis (the marketed product has no indication text on file) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, bacampicillin is an ampicillin prodrug (a penicillin-class beta-lactam antibacterial). Its efficacy in upper respiratory and urinary tract bacterial infections is established, and it may mechanistically be applicable to epiglottitis.

Epiglottitis is a bacterial infection of the upper airway, historically caused mainly by *Haemophilus influenzae* type b. It is related to the existing indications of pharyngitis and sinusitis, so an indirect antibacterial link is plausible.

There are important limits. The TxGNN score is only a model prediction. Epiglottitis is an acute airway emergency, and current standard care uses parenteral, beta-lactamase-stable agents such as third-generation cephalosporins. An oral ampicillin prodrug would not be suitable in this setting.

## Other Predictions Reviewed

The other top-ranked predictions have little or no support. Most (for example abdominal cystic lymphangioma, celiac trunk compression syndrome, abdominal ectopic pregnancy, lymph node palisaded myofibroblastoma and sacrum chordoma) are non-infectious conditions with no plausible antibacterial mechanism, and their high scores are likely model artifacts. Broad categories such as disease of retroperitoneum, disease of uterine broad ligament and disease of peritoneum could respond only if the cause were a bacterial infection, and no evidence was provided.

The one prediction with any literature is **urethral disease** (rank 9, score 0.9985, evidence level L3). A 1989 pilot study gave bacampicillin 800 mg twice daily for 7 days to 84 men with non-gonococcal urethritis. Among the 23 *Chlamydia*-positive patients who attended follow-up, 22 became chlamydia-negative, but only 14 also became asymptomatic with normal urethral smears. This was a small, non-randomized study. Non-gonococcal urethritis is often caused by organisms poorly covered by beta-lactams, and guidelines favor doxycycline or azithromycin, so efficacy remains doubtful.

## Literature Evidence

No literature is available for epiglottitis. The only publication among the top 10 predictions concerns urethral disease:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2921050](https://pubmed.ncbi.nlm.nih.gov/2921050/) | 1989 | Pilot study | Genitourinary medicine | Bacampicillin 800 mg twice daily for 7 days in 84 men with non-gonococcal urethritis; 22 of 23 chlamydia-positive patients who attended follow-up became negative, but only 14 became asymptomatic with normal smears |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 177972 | Penglobe 200mg Tablet (AstraZeneca) | Strip of 6 tablets (oral) | Not specified |

## Safety Considerations

- **Disease-level contraindications (from knowledge graph, not label text)**: kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, infectious mononucleosis, chronic Epstein-Barr virus infection syndrome.
- **Drug Interactions**: 34 interactions were identified. Most are Moderate. Main ones include:
  - Acid suppressants: famotidine, ranitidine, cimetidine, nizatidine, and the proton pump inhibitors omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole and rabeprazole
  - Tetracyclines: doxycycline, tetracycline and minocycline
  - Antacids: calcium carbonate, aluminum hydroxide, magnesium carbonate and magnesium hydroxide
  - Others: balsalazide and picosulfuric acid (Moderate); clarithromycin (Minor)

Please refer to the package insert for warnings and label contraindications, as these were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for epiglottitis is supported only by a plausible antibacterial link, with no trials or literature. The oral formulation also does not fit the acute, airway-threatening nature of the disease, and standard care already relies on parenteral agents. Most other top predictions have no mechanistic basis. Urethral disease is the only one with any literature, and that is a single small, early study with doubtful applicability.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed product (a blocking gap for safety screening)
- Detailed mechanism of action data
- Clinical or observational evidence of bacampicillin use in epiglottitis, or a formal assessment of whether an oral route is clinically acceptable
- Confirmation of the approved indication text for the registered product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

