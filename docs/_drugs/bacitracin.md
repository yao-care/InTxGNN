---
layout: default
title: Bacitracin
parent: Model Prediction Only (L5)
nav_order: 88
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bacitracin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Keratitis, keratoconjunctivitis, blepharoconjunctivitis"
monitor_inn: "Bacitracin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "infective urethral stricture", "post-infectious syndrome", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy"]
---

# Bacitracin
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

# Bacitracin: From Keratitis to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Bacitracin is a topical antibiotic originally used for ocular surface infections such as keratitis, keratoconjunctivitis and blepharoconjunctivitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Keratitis, keratoconjunctivitis, blepharoconjunctivitis |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 11 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, bacitracin is a topical polypeptide antibiotic that acts on Gram-positive bacterial cell wall synthesis. It is used for ocular surface infections, and mechanistically it could be applicable to bacterial forms of surface eye disease.

The predicted indication is biologically close to the approved ocular uses, which likely explains the very high score. However, punctate epithelial keratoconjunctivitis is frequently viral (for example adenoviral) or non-infectious, and an antibacterial would not be expected to act on those causes. The score most likely reflects proximity to the approved ocular indications in the knowledge graph rather than independent evidence.

Other predictions in the top 10 are weaker still. Exposure keratitis may benefit only from supportive protection against secondary infection. Otitis externa has a plausible antibacterial rationale, mainly through combination ear products. Most of the remaining predictions are non-specific categories or conditions with no plausible mechanistic link (for example Chagas cardiomyopathy, infection-related hemolytic uremic syndrome).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top predicted indication.

For reference, the fourth-ranked prediction, otitis externa, has limited literature, mostly on combination products:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17503066](https://pubmed.ncbi.nlm.nih.gov/17503066/) | 2007 | Double-blind clinical study (151 patients) | Eur Arch Otorhinolaryngol | Polymyxin B + bacitracin ointment compared with the same ointment plus hydrocortisone in acute bacterial otitis externa |
| [9820118](https://pubmed.ncbi.nlm.nih.gov/9820118/) | 1998 | In vitro susceptibility study (veterinary) | Zentralbl Veterinarmed B | Increased antibiotic resistance in bacteria from chronic canine otitis externa |
| [14055264](https://pubmed.ncbi.nlm.nih.gov/14055264/) | 1963 | Review / practice article | Maryland State Med J | Practical treatment of otitis externa |
| [14048629](https://pubmed.ncbi.nlm.nih.gov/14048629/) | 1963 | Clinical report (combination product) | Z Laryngol Rhinol Otol | Local treatment of inflammatory, secretory ear conditions with a combination product |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 150914 | Neosporin Eye Drop | Eye drop, 10 ml | Not specified |
| 150820 | Neosporin Antibiotic Ointment | Ointment, 10 g tube | Not specified |
| 150452 | Neosporin Ointment | Ointment, 10 g tube | Not specified |
| 150299 | Neosporin Dusting Powder | Dusting powder, 10 g | Not specified |
| 151066 | Nebasulf Ointment | Ointment, 5 g tube | Not specified |

All 11 registrations are valid single-ingredient licences. Only one is an ophthalmic product (Neosporin Eye Drop). The others are ointments or powders.

## Safety Considerations

- **Contraindications (from knowledge-graph disease associations, not label text)**: Eye-related entries include herpes simplex virus keratitis, viral eye infection, fungal infection of the eye, conjunctivitis, eye infectious disease, open-angle glaucoma and ocular hypertension. Other listed conditions include kidney disease, liver disease, myasthenia gravis and neuromuscular junction disease, epilepsy, diabetes mellitus, adrenocortical insufficiency, and heart block. These associations likely partly reflect companion ingredients in combination products and should be verified against the label.
- **Drug Interactions** (84 recorded; selected examples):
  - **Major**: kanamycin, neomycin, streptomycin (additive nephrotoxicity and neurotoxicity risk with aminoglycosides), deferasirox, and iodinated contrast agents (diatrizoate, iodipamide, iodixanol, iohexol).
  - **Moderate**: mesalazine, balsalazide, olsalazine, sulfasalazine, vancomycin, exenatide, picosulfuric acid.
- Systemic bacitracin is nephrotoxic, so any use beyond topical application is a concern.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score, with no trials or literature. The most likely causes of punctate epithelial keratoconjunctivitis (viral or non-infectious) are not addressed by an antibacterial, so the high score probably reflects graph proximity to the approved ocular uses.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian products (currently a blocking gap for safety screening)
- Mechanism of action data
- Clarification of the cause of punctate epithelial keratoconjunctivitis, and whether a bacterial subset exists
- Clinical or preclinical evidence specific to this condition
- Confirmation of approved indications for the Indian licences, and whether an ophthalmic ointment is available
- If the project continues, otitis externa (the only prediction with some clinical literature) could be explored as a separate research question, using evidence on bacitracin as a single agent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

