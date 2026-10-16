---
layout: default
title: Fenticonazole
parent: Model Prediction Only (L5)
nav_order: 346
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fenticonazole: predicted new indication Trichomonal vulvovaginitis (evidence level L5). Approved use: Vulvovaginal candidiasis"
monitor_inn: "Fenticonazole"
predicted_indications: ["trichomonal vulvovaginitis", "postmenopausal atrophic vaginitis", "vulvovaginitis", "vulvitis", "herpetic vulvovaginitis", "vaginitis (disease)", "ulceration of vulva", "vulvar neoplasm", "vaginal discharge", "bacterial vaginosis"]
---

# Fenticonazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Fenticonazole: From Vulvovaginal Candidiasis to Trichomonal Vulvovaginitis

## One-Sentence Summary

Fenticonazole is an imidazole antifungal, originally used to treat vulvovaginal candidiasis.
The TxGNN model predicts it may be effective for **trichomonal vulvovaginitis**, but **no registered clinical trials** and **no Trichomonas-specific publications** currently support this prediction.
The related, broader indication of **vulvovaginitis** has stronger support (**about 20 publications**, including several comparative trials), but that evidence mostly overlaps with the already-approved candidiasis use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vulvovaginal candidiasis |
| Predicted New Indication | Trichomonal vulvovaginitis |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L4 (for trichomonal vulvovaginitis) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the literature, fenticonazole is an imidazole derivative with broad antimycotic activity. It is described as acting by inhibiting Candida acid protease secretion, damaging the cytoplasmic membrane, and blocking cytochrome oxidases and peroxidases. It has also shown some antibacterial activity.

Trichomonal vulvovaginitis and candidal vulvovaginitis present similarly and affect the same anatomical site. Other imidazoles are reported to have some in vitro activity against Trichomonas, which makes the prediction plausible. However, this link is unconfirmed. The retrieved papers address vulvovaginitis in general, mainly candidal, and do not show Trichomonas-specific efficacy. One open-label pilot study (PMID 15216954) enrolled women with mixed infections including *Trichomonas vaginalis*, but the available summary does not report results for the trichomonal subgroup. The high TxGNN score is a computational prediction only.

## Clinical Trial Evidence

Currently no related clinical trials are registered for trichomonal vulvovaginitis.

## Literature Evidence

No Trichomonas-specific publication was found. The two papers below were retrieved for this prediction, and both are general vulvovaginitis papers.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15216954](https://pubmed.ncbi.nlm.nih.gov/15216954/) | 2004 | Clinical study (open-label, multicenter pilot) | Journal of Chemotherapy | 101 women with single or mixed vulvovaginitis (Candida, Trichomonas, Gardnerella); 1 g ovules on days 1 and 3 |
| [18840006](https://pubmed.ncbi.nlm.nih.gov/18840006/) | 2008 | Review | Drugs | Topical fenticonazole in dermatology and gynaecology: broad antimycotic activity, some antibacterial action |

### Supporting evidence for related indications

The broader indication **vulvovaginitis** (rank 3) has more support (evidence level L2, recommendation Proceed with Guardrails). It rests mainly on candidal infection, so it is not a true repurposing signal.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12017948](https://pubmed.ncbi.nlm.nih.gov/12017948/) | 2002 | Comparative trial | Ginecol Obstet Mex | Fenticonazole 200 mg vs miconazole 400 mg in mycotic vulvovaginitis |
| [2202548](https://pubmed.ncbi.nlm.nih.gov/2202548/) | 1990 | Randomized comparative trial | Curr Med Res Opin | 153 patients; single 600 mg ovule vs clotrimazole 500 mg tablet in vaginal candidiasis |
| [2680285](https://pubmed.ncbi.nlm.nih.gov/2680285/) | 1989 | Randomized comparative trial | Curr Med Res Opin | 50 patients; fenticonazole 600 mg ovule vs clotrimazole 500 mg tablet |
| [3542628](https://pubmed.ncbi.nlm.nih.gov/3542628/) | 1986 | Double-blind trial | J Int Med Res | 54 patients; fenticonazole cream vs clotrimazole for 7 days |
| [22481619](https://pubmed.ncbi.nlm.nih.gov/22481619/) | 2012 | Comparative study | Minerva Ginecol | Fluconazole 150 mg vs intravaginal fenticonazole 600 mg in acute vulvovaginal candidiasis |
| [2019858](https://pubmed.ncbi.nlm.nih.gov/2019858/) | 1991 | Pharmacokinetic study | J Chemother | Low systemic absorption after vaginal administration of 1 g |
| [31845594](https://pubmed.ncbi.nlm.nih.gov/31845594/) | 2019 | Review | Future Microbiol | Fenticonazole as an empiric treatment in mixed vaginitis |

Evidence for **bacterial vaginosis** (rank 10, L4) is preclinical: a mouse model ([37960949](https://pubmed.ncbi.nlm.nih.gov/37960949/)) and in vitro activity against *Gardnerella vaginalis* ([36427832](https://pubmed.ncbi.nlm.nih.gov/36427832/), [31061161](https://pubmed.ncbi.nlm.nih.gov/31061161/)). No human controlled trial was found.

Other predicted indications (postmenopausal atrophic vaginitis, herpetic vulvovaginitis, vulvar ulceration, vulvar neoplasm) have no supporting clinical or literature evidence and no plausible mechanistic rationale for an antifungal.

## India Market Information

Fenticonazole is marketed in India with 20 valid single-ingredient registrations. Approved indication text is not available in the data compiled for this report. Five representative registrations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 35154 | Cosfen Vaginal Capsule | Strip of 1 vaginal capsule | Not available |
| 84742 | Fenticad Vaginal Capsule | Strip of 1 vaginal capsule | Not available |
| 84206 | Fentin Vaginal Capsule | Strip of 1 vaginal capsule | Not available |
| 84154 | Fenza Vaginal Capsule | Strip of 2 vaginal capsules | Not available |
| 34871 | Cosfen Vaginal Cream | Tube of 30 g vaginal cream | Not available |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the data compiled for this report. The one available pharmacokinetic study suggests low systemic absorption after vaginal use (PMID 2019858).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for trichomonal vulvovaginitis is high (99.50%), but there are no registered trials and no Trichomonas-specific data, so the prediction remains unconfirmed. The best-supported nearby indication, vulvovaginitis, is largely the same as the approved candidiasis use. It does not represent a new indication.

**To proceed, the following is needed:**
- In vitro activity data of fenticonazole against *Trichomonas vaginalis*, and the Trichomonas subgroup results from PMID 15216954
- A controlled clinical trial against the standard comparator (nitroimidazoles such as metronidazole) if in vitro data are favourable
- Package insert warnings and contraindications from Indian regulatory sources
- Detailed mechanism of action data
- Human controlled trials in mixed vaginitis or bacterial vaginosis, if those indications are to be pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

