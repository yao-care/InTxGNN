---
layout: default
title: Nystatin
parent: Moderate Evidence (L3-L4)
nav_order: 610
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-30
description: "Nystatin: predicted new indication Vulvovaginitis (evidence level L3). Approved use: Cutaneous candidiasis, oral candidiasis, candidiasis…"
monitor_inn: "Nystatin"
predicted_indications: ["vulvovaginitis", "disease of orbital region", "disease of orbital part of eye adnexa", "cystic teratoma", "spinal cord dermoid cyst", "postmenopausal atrophic vaginitis", "biotin metabolic disease", "vulvitis", "commissural lip fistula", "osteoradionecrosis of the mandible"]
---

# Nystatin
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

## Nystatin: From Cutaneous Candidiasis to Vulvovaginitis
{: .text-alpha }

## One-Sentence Summary

Nystatin is a polyene antifungal originally used to treat candidiasis of the skin, mouth and vulvovaginal area.
The TxGNN model predicts it may be effective for **vulvovaginitis**, with **no registered clinical trials** and **20 publications** (mostly reviews) currently supporting this direction.
This is largely an on-label use for candidal vulvovaginitis rather than true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cutaneous candidiasis, oral candidiasis, candidiasis, vulvovaginal candidiasis |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L3 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, nystatin is a polyene antifungal that binds ergosterol in the Candida cell membrane. This forms pores and causes leakage of cell contents.

Vulvovaginitis is largely caused by Candida, and vulvovaginal candidiasis is already among nystatin's original indications. The prediction is therefore mostly a re-statement of an existing use rather than a new one.

The literature supports efficacy against candidal vulvovaginitis. It does not support efficacy against non-candidal causes such as bacterial, trichomonal or atrophic vaginitis. The same applies to the related predicted indication, vulvitis, which responds only when the cause is candidal.

## Clinical Trial Evidence

Currently no related clinical trials registered for vulvovaginitis.

## Literature Evidence

The literature set includes reviews and some comparative or in vitro studies. Most items are reviews. Priority below is given to higher-tier reviews and studies directly involving nystatin.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Review | Pharmaceutics | Management of fluconazole-resistant vulvovaginal candidiasis; nystatin is among the alternative therapies discussed |
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Review | BMJ Clinical Evidence | Vulvovaginal candidiasis is the second most common cause of vaginitis; Candida albicans accounts for 85–90% of cases |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Womens Health | Boric acid for recurrent vulvovaginal candidiasis; non-albicans species are more azole-resistant |
| [18729533](https://pubmed.ncbi.nlm.nih.gov/18729533/) | 2008 | Review | Drugs | Local treatment of vulvovaginal candidosis; local and oral therapy considered equally effective for uncomplicated disease |
| [1436934](https://pubmed.ncbi.nlm.nih.gov/1436934/) | 1992 | Review | Obstet Gynecol Clin North Am | Nystatin was introduced in the 1950s for vulvovaginal candidiasis, and has since been surpassed by azoles as first choice |
| [2212172](https://pubmed.ncbi.nlm.nih.gov/2212172/) | 1990 | Review | J Am Acad Dermatol | Many effective antimycotics exist; little evidence that topical formulation affects outcome |
| [25416649](https://pubmed.ncbi.nlm.nih.gov/25416649/) | 2015 | Comparative study | Mycopathologia | Vaginal nystatin vs oral fluconazole in recurrent VVC (n=293); initial mycological cure 78.3% (nystatin) vs 73.8% (fluconazole) |
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | Clinical study | Mycoses | Fluconazole and nystatin susceptibility correlated with clinical outcome in complicated VVC (287 isolates, 283 patients) |
| [21918792](https://pubmed.ncbi.nlm.nih.gov/21918792/) | 2012 | Clinical study | Acta Derm Venereol | Compared fluconazole and nystatin efficacy against vaginal Candida in Brazilian women |
| [10796183](https://pubmed.ncbi.nlm.nih.gov/10796183/) | 2000 | Systematic review | Cochrane Database Syst Rev | Topical treatment for vaginal candidiasis in pregnancy |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 151372 | Nistin 100000IU Ointment (Jawa Pharmaceuticals Pvt Ltd) | Tube of 3 g ointment | Not stated in the registration record |

Only a topical ointment is registered. No vaginal formulation is registered in India according to the compiled data.

## Safety Considerations

- **Drug Interactions**: The interaction query returned 347 records. The severity level is unclassified for all of the first 20 listed, which include cyclosporine, fluconazole, erythromycin, azithromycin, tramadol, lorazepam, bortezomib and sildenafil. Clinical significance cannot be judged from these data.
- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not label text): adrenocortical insufficiency, Addison disease, skin atrophy, telangiectasis, capillary disease and hereditary hemorrhagic telangiectasia. These should be verified against the package insert.

Package insert warnings and contraindications were not available. Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence supports nystatin for candidal vulvovaginitis (and candidal vulvitis), which is already within its original indications. The support is mostly reviews plus a few comparative studies, with no registered trials. The other nine predictions are unsupported by evidence (L5, Hold). These include orbital disease, cystic teratoma, spinal cord dermoid cyst, atrophic vaginitis, biotin metabolic disease, commissural lip fistula and osteoradionecrosis of the mandible. The one trial linked to orbital disease concerns an unrelated product.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are required before safety screening
- Detailed mechanism of action data
- Confirmation of the intended formulation, since only a topical ointment is registered in India and a vaginal formulation would need to be considered
- Restriction of the use to confirmed candidal etiology, with no extension to bacterial, trichomonal or atrophic vaginitis
- Review of the interaction records to grade clinical severity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

