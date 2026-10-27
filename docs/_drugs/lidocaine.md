---
layout: default
title: Lidocaine
parent: Model Prediction Only (L5)
nav_order: 491
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lidocaine: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Not stated in the India licence records"
monitor_inn: "Lidocaine"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "papillary conjunctivitis", "rosacea conjunctivitis", "exposure keratitis", "atopic conjunctivitis", "conjunctival disorder", "nephrotic syndrome", "non-human animal disease", "sporadic idiopathic steroid-resistant nephrotic syndrome"]
---

# Lidocaine
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

## Lidocaine: From Local Anaesthesia and Neuralgia to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Lidocaine is a sodium channel blocker, originally used as a local anaesthetic and for conditions such as neuralgia, postherpetic neuralgia, haemorrhoids, dermatitis and parasitic skin infestations.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis** (top-ranked prediction), but **no clinical trials and no publications** currently support this specific indication, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India licence records; the knowledge graph lists dermatitis, neuralgia, postherpetic neuralgia, haemorrhoid, scabies and other conditions |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Lidocaine is generally known as a sodium channel blocker, and it acts as a topical ocular anaesthetic. It could in principle relieve surface pain.

However, the link to the predicted indication is weak. Lidocaine does not treat the underlying epithelial inflammation or infection in punctate epithelial keratoconjunctivitis. Prolonged topical anaesthetic use is also known to be toxic to the corneal epithelium, which argues against therapeutic use. The very high TxGNN score is therefore not matched by any mechanistic or clinical support.

Other high-ranking predictions (papillary conjunctivitis, rosacea conjunctivitis, exposure keratitis, nephrotic syndrome, tinea corporis) show the same pattern: no plausible disease-modifying mechanism and no supportive trials. The one slightly more interesting lead is **atopic conjunctivitis** (L4), where a 2023 preclinical study suggests sensory nerve signalling, which lidocaine blocks, may influence allergen passage through the conjunctiva. This remains a research question rather than a clinical signal.

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top-ranked predicted indication, punctate epithelial keratoconjunctivitis.

For context, the closest trials found relate to the lower-ranked prediction "conjunctival disorder". They concern procedural anaesthesia, not treatment of a disease:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05978687](https://clinicaltrials.gov/study/NCT05978687) | Phase 4 | Completed | 41 | Lidocaine gel vs subconjunctival injection for pain control in pterygium excision |
| [NCT01350024](https://clinicaltrials.gov/study/NCT01350024) | N/A | Completed | 34 | Postoperative pain with two types of local anaesthesia in ptosis (drooping eyelid) surgery |

## Literature Evidence

Currently no related literature is available for punctate epithelial keratoconjunctivitis.

Selected publications linked to other predicted ocular indications are shown below for context:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18989343](https://pubmed.ncbi.nlm.nih.gov/18989343/) | 2009 | RCT | Eye (London) | Lidocaine 2% gel vs tetracaine 1% drops as sole topical anaesthetic in primary pterygium surgery |
| [29135709](https://pubmed.ncbi.nlm.nih.gov/29135709/) | 2018 | Pilot study | Cornea | Subconjunctival injection vs 2% vs 5% lidocaine gel in pterygium surgery |
| [15799734](https://pubmed.ncbi.nlm.nih.gov/15799734/) | 2005 | Clinical study | Acta Ophthalmol Scand | Efficacy of lidocaine 2% gel as topical anaesthetic in pterygium surgery |
| [37819721](https://pubmed.ncbi.nlm.nih.gov/37819721/) | 2023 | Preclinical mechanistic study | JCI Insight | Nerve-goblet cell association promotes antigen passage in allergic conjunctivitis |
| [8039024](https://pubmed.ncbi.nlm.nih.gov/8039024/) | 1994 | Experimental physiological study | Clin Exp Allergy | Nasal anaesthesia and lacrimal function after nasal allergen challenge |
| [19250287](https://pubmed.ncbi.nlm.nih.gov/19250287/) | 2009 | Review | Cephalalgia | Neuropsychiatric and cardiac side effects of lidocaine, based on headache patients and literature |

## India Market Information

Lidocaine has 20 valid single-ingredient registrations. The records do not include approved indication text. Five main authorisations are shown:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 125383 | Lidofix 2% Injection | Vial of 30 ml injection | Not stated |
| 127832 | Lignocip 2% Injection (Cipla) | Vial of 30 ml injection | Not stated |
| 121665 | Lignox 2% Gel (Indoco) | Tube of 30 gm gel | Not stated |
| 203383 | Skore Not Out Lidocaine Topical Spray | Bottle of 12 gm spray | Not stated |
| 109472 | Ilidotrans Transdermal Patch | Box of 2 transdermal patches | Not stated |

Other forms on the market include an oral topical solution and 1% ophthalmic-use injection (Oculan). No ophthalmic drop formulation appears among the registered products.

## Safety Considerations

- **Contraindication signals (knowledge graph, not label text)**: Linked conditions include hypertension, liver failure and liver disease, cirrhosis, kidney disease, epilepsy, adrenocortical insufficiency, hypothyroidism, open-angle glaucoma, herpes simplex virus keratitis, varicella zoster infection, atopic dermatitis, osteoporosis, psychotic disorders, fungal infections and gastritis. These should be verified against the product label.
- **Drug Interactions**: 100 interactions were identified. Major: **bupropion**. Moderate: aprepitant, cimetidine, liposomal morphine, obeticholic acid, polyethylene glycol (3350 with electrolytes), picosulfuric acid and sodium sulfate. Minor: dexamethasone, kanamycin, neomycin, streptomycin, omeprazole and troglitazone.
- **Literature-reported risks**: Neuropsychiatric and cardiac side effects with intravenous use (PMID 19250287); drug-induced methemoglobinaemia, including a paediatric case with topical lidocaine, benzocaine and co-trimoxazole (PMID 41995267); seizures in animals at low doses when lidocaine was used as a diluent (PMID 19858165); and corneal epithelial toxicity with prolonged topical ocular use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has a very high model score but no clinical trials or literature. Lidocaine only provides symptomatic surface anaesthesia, does not treat the underlying disease, and prolonged topical use can damage the corneal epithelium. Existing ocular evidence concerns procedural anaesthesia, not disease treatment.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India-registered products
- Detailed mechanism of action data
- A clear case for a disease-modifying or symptomatic role in punctate epithelial keratoconjunctivitis, including corneal toxicity risk assessment
- If pursuing the atopic conjunctivitis lead, preclinical or early clinical studies on sensory nerve blockade, together with confirmation of suitable ophthalmic formulations and routes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

