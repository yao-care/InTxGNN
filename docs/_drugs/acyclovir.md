---
layout: default
title: Acyclovir
parent: Model Prediction Only (L5)
nav_order: 24
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Acyclovir: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Herpes simplex infection, herpes zoster, chickenpox, herpes labialis…"
monitor_inn: "Acyclovir"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "common wart", "post-infectious neuralgia", "hepatitis C induced liver cirrhosis", "eosinophilic pustular folliculitis", "sequela of COVID-19", "vulvovaginal candidiasis", "papular urticaria", "disease of orbital region", "epidemic keratoconjunctivitis"]
---

# Acyclovir
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

## Acyclovir: From Herpes Simplex Infection to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Acyclovir is an antiviral originally used to treat herpes simplex infections, herpes zoster, chickenpox, herpes labialis, herpes simplex encephalitis and genital herpes.
The TxGNN model ranks **punctate epithelial keratoconjunctivitis** highest at 0.9967, but **no clinical trials** and only **2 unrelated publications** support it. The better-supported secondary signal is **common warts**, with **4 clinical trials** (intralesional acyclovir) and **about 20 publications**, including recent randomized trials.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpes simplex infection, herpes zoster, chickenpox, herpes labialis, herpes simplex encephalitis, genital herpes (the licence records carry no approved-indication text) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis (top-ranked); common wart (best-supported alternative) |
| TxGNN Prediction Score | 0.9967 (punctate epithelial keratoconjunctivitis); 0.9946 (common wart) |
| Evidence Level | L5 (top-ranked indication); L2 (common wart) |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold (top-ranked indication); Proceed with Guardrails for common wart as a research question |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Acyclovir is a well-known guanosine analogue antiviral. It is activated by viral thymidine kinase and then inhibits herpesvirus DNA polymerase, which is why it works against HSV and VZV.

**Top-ranked prediction (punctate epithelial keratoconjunctivitis).** This condition can be herpetic or adenoviral. A plausible link exists only for herpetic cases. The two papers retrieved concern microsporidial keratoconjunctivitis and drug-induced corneal lipidosis in AIDS, so neither supports acyclovir use. The high score is a model prediction without clinical backing.

**Common wart.** Warts are caused by HPV, a DNA virus that lacks its own thymidine kinase, so acyclovir's selective activation is not expected to work as it does in herpesviruses. Proposed mechanisms are non-specific inhibition of viral DNA synthesis and immune modulation after intralesional injection. The mechanistic rationale is weak, but clinical activity has been reported repeatedly in small randomized comparisons, mostly from Egypt.

**Other predictions** are weakly supported:
- Herpetic eye disease (disease of the orbital region) largely overlaps with existing herpes indications.
- Epidemic keratoconjunctivitis is adenoviral, so acyclovir is not expected to work.
- Hepatitis C cirrhosis (an RNA virus) and vulvovaginal candidiasis (a fungus) have no plausible acyclovir target.
- Sequela of COVID-19 mostly reflects treatment of reactivated herpes infections, not COVID-19 itself.
- Post-infectious neuralgia, eosinophilic pustular folliculitis and papular urticaria have no retrieved evidence.

## Clinical Trial Evidence

Trials for the top-ranked indication: currently no related clinical trials registered.

Trials for common wart (best-supported alternative):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06261684](https://clinicaltrials.gov/study/NCT06261684) | Phase 2/3 | Unknown | 92 | Randomized trial of intralesional acyclovir vs cryotherapy in plantar warts; safety and efficacy comparison |
| [NCT05429151](https://clinicaltrials.gov/study/NCT05429151) | Phase 4 | Unknown | 40 | Intralesional acyclovir vs Candida antigen in plantar warts |
| [NCT05324904](https://clinicaltrials.gov/study/NCT05324904) | Not applicable | Unknown | 44 | Intralesional vitamin D3 vs acyclovir in plantar warts |
| [NCT07448844](https://clinicaltrials.gov/study/NCT07448844) | Phase 4 | Recruiting | 40 | Intralesional vitamin D3 vs acyclovir in cutaneous viral warts; complete clearance at week 8 |

Related ocular trials (herpetic eye disease, disease of the orbital region):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06757907](https://clinicaltrials.gov/study/NCT06757907) | Not applicable | Completed | 20 | Topical ganciclovir vs systemic acyclovir in herpetic keratitis |
| [NCT05313828](https://clinicaltrials.gov/study/NCT05313828) | Not applicable | Unknown | 40 | Treatment modalities for dendritic viral ulcer |
| [NCT03389191](https://clinicaltrials.gov/study/NCT03389191) | Not applicable | Unknown | 30 | Oral acyclovir in refractory viral uveitis |

## Literature Evidence

Common wart (best-supported alternative):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40889709](https://pubmed.ncbi.nlm.nih.gov/40889709/) | 2026 | RCT | J Am Acad Dermatol | Intralesional acyclovir vs cryotherapy in plantar warts |
| [40488756](https://pubmed.ncbi.nlm.nih.gov/40488756/) | 2025 | RCT/Comparative | Arch Dermatol Res | Intralesional acyclovir vs 5-fluorouracil in recalcitrant warts |
| [38822848](https://pubmed.ncbi.nlm.nih.gov/38822848/) | 2024 | RCT | Arch Dermatol Res | Intralesional acyclovir vs hepatitis B vaccine in resistant plantar warts (48 patients) |
| [41686619](https://pubmed.ncbi.nlm.nih.gov/41686619/) | 2026 | Systematic review / network meta-analysis | Medicine | Comparison of treatment modalities for cutaneous warts, including intralesional acyclovir |
| [40056255](https://pubmed.ncbi.nlm.nih.gov/40056255/) | 2025 | Clinical trial | Arch Dermatol Res | Intralesional acyclovir vs quadrivalent HPV vaccine in recalcitrant warts (60 patients) |
| [37303436](https://pubmed.ncbi.nlm.nih.gov/37303436/) | 2023 | Comparative study | Cureus | Intralesional acyclovir vs PPD immunotherapy in viral warts |
| [34412535](https://pubmed.ncbi.nlm.nih.gov/34412535/) | 2022 | Clinical study | J Cutan Med Surg | Intralesional acyclovir as a potential option for cutaneous warts |
| [38793636](https://pubmed.ncbi.nlm.nih.gov/38793636/) | 2024 | Case reports and review | Viruses | Remission of HPV-related disease with acyclovir or valacyclovir |
| [26885794](https://pubmed.ncbi.nlm.nih.gov/26885794/) | 2016 | Case report | J Drugs Dermatol | Persistent plantar warts resolved after oral acyclovir given for zoster |

Top-ranked indication (punctate epithelial keratoconjunctivitis):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Case series | Indian J Pathol Microbiol | Microsporidial keratoconjunctivitis cohort; no acyclovir link |
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Case report | Am J Ophthalmol | Drug-induced corneal lipidosis in AIDS; not relevant to acyclovir efficacy |

## India Market Information

Acyclovir has 20 valid single-ingredient registrations, and all of them are marketed. Oral tablets (including dispersible forms) and injectables are available. The licence records contain no approved-indication text. Five main registrations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 90 | Acivir 400 DT Tablet (Cipla Ltd) | Dispersible tablet, strip of 5 | Not specified in the records |
| 5358 | Acloveer 400 Tablet (Knoll Pharmaceuticals Ltd) | Tablet, strip of 10 | Not specified in the records |
| 103927 | Herpex 200mg Tablet (Torrent Pharmaceuticals Ltd) | Tablet, strip of 10 | Not specified in the records |
| 124530 | Lovir 800mg Tablet (Eli Lilly and Company India Pvt Ltd) | Tablet, strip of 5 | Not specified in the records |
| 193040 | Riv 500mg Injection (Medilife Health Sciences Pvt Ltd) | Injection, vial | Not specified in the records |

An injectable formulation (500 mg vial) is registered, so the intralesional approach used in wart trials relies on diluting an existing vial. This is off-label and no wart-specific product exists.

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (not drawn from label text): hypertension, kidney disease and impaired renal function, hemolytic-uremic syndrome, thrombocytopenic purpura, diabetes and hyperglycemia, diabetic ketoacidosis, adrenocortical insufficiency, stroke and cerebrovascular disorders, myocardial infarction, peripheral vascular disease, obesity, skin atrophy and telangiectasia. Several of these look like class-level or non-specific associations, so they should be checked against the package insert.
- **Drug Interactions**: 100 interactions were found. Those graded Moderate are the aminosalicylates (balsalazide, mesalazine, olsalazine, sulfasalazine) and trospium. Others, such as amphotericin B, metformin, glimepiride, rosiglitazone, morphine, doxycycline, omeprazole, pantoprazole, lansoprazole, sucralfate, calcitriol, mannitol, epinephrine, palonosetron and clotrimazole, are listed with unknown severity.

Warnings and contraindications from the package insert were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold for punctate epithelial keratoconjunctivitis; Proceed with Guardrails for common wart (research question only)**

**Rationale:**
- The top-ranked prediction rests on model score alone. The retrieved papers are unrelated, and the mechanism applies only to herpetic cases.
- Common wart has the strongest signal (4 small trials, several recent RCTs), but the mechanism is weak, the samples are small, most work comes from one region, and the Phase 2/3 trial has unknown status. This supports further study, not clinical adoption.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (blocking gap for safety screening)
- Detailed mechanism-of-action data
- For warts: a larger, multicentre, blinded RCT with a defined dose and long-term recurrence follow-up, plus a review of local-injection safety
- For the eye indication: confirmation of herpetic aetiology and clear separation from existing herpes keratitis indications
- Route compatibility assessment (intralesional use is off-label relative to the registered oral and intravenous forms)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

