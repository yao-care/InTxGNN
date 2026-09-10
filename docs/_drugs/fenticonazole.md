---
layout: default
title: Fenticonazole
parent: 僅模型預測 (L5)
nav_order: 343
evidence_level: L5
indication_count: 10
---

# Fenticonazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Fenticonazole: From Vulvovaginal Candidiasis to Trichomonal Vulvovaginitis

## One-Sentence Summary

Fenticonazole is a topical imidazole antifungal with established international use against candidal vulvovaginitis and dermatomycoses; no India/Taiwan regulatory license data is currently on file for this drug.
The TxGNN model predicts it may be effective for **Trichomonal Vulvovaginitis**, but the supporting evidence comes from a *fixed-dose combination* (fenticonazole + tinidazole + lidocaine), not fenticonazole monotherapy.
Currently **1 clinical trial** and **2 publications** support this specific direction, and fenticonazole itself has no known intrinsic antitrichomonal activity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in India regulatory data (drug unmarketed); established international use as a topical antifungal for vulvovaginal candidiasis / dermatomycoses (per literature evidence) |
| Predicted New Indication | Trichomonal Vulvovaginitis |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L1 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for fenticonazole is not currently available in this evidence pack. Based on the supporting literature, fenticonazole is an imidazole derivative antifungal that inhibits CYP51 (lanosterol demethylase) and damages the fungal cytoplasmic membrane — a mechanism with no known direct activity against *Trichomonas vaginalis*.

The clinical trial evidence behind this prediction (NCT06056947) is a Phase 3 study of a **combination product** — fenticonazole + tinidazole + lidocaine — evaluated across bacterial vaginosis, candidal vulvovaginitis, trichomonal vaginitis, and mixed infections. Tinidazole, not fenticonazole, is the pharmacologically active agent against *Trichomonas*. This means the trial's efficacy signal for trichomonal vulvovaginitis cannot be attributed to fenticonazole alone, and the TxGNN score likely reflects proximity in the knowledge graph (shared trial/indication co-occurrence) rather than a validated fenticonazole-specific mechanism.

For context, fenticonazole's TxGNN-predicted "vulvovaginitis" indication (a related candidate in this evidence pack) is not a novel repurposing signal at all — it reflects the drug's already-established antifungal use. The genuinely novel and mechanistically unsupported claim is specifically the antitrichomonal effect, which should be interpreted with caution.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06056947](https://clinicaltrials.gov/study/NCT06056947) | Phase 3 | Completed | 577 | Randomized, 3-arm, multicenter study comparing two new fenticonazole+tinidazole+lidocaine formulations against Gynomax® XL ovule for trichomonal vaginitis, bacterial vaginosis, candidal vulvovaginitis, and mixed vaginal infections — evidence pertains to the combination product, not fenticonazole monotherapy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15216954](https://pubmed.ncbi.nlm.nih.gov/15216954/) | 2004 | Open-label cohort | Journal of Chemotherapy | Prospective, open-label pilot study of fenticonazole nitrate 1g vaginal ovules (ultra-short 2-day regimen) in 101 women with vulvovaginitis from Candida albicans, Trichomonas vaginalis, and/or Gardnerella vaginalis (single or mixed infections) |
| [18840006](https://pubmed.ncbi.nlm.nih.gov/18840006/) | 2008 | Review | Drugs | Reviews fenticonazole's antimycotic mechanism (protease inhibition, cytoplasmic membrane damage, cytochrome oxidase/peroxidase blockade) and notes additional antibacterial activity; does not report specific antitrichomonal efficacy data |

---

## India Market Information

Currently no market authorization records — fenticonazole is not marketed in India per available regulatory data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 trial (n=577) exists, satisfying L1 evidence-level criteria on a formal count basis, but the trial evaluates a fenticonazole+tinidazole combination, not fenticonazole alone — the antitrichomonal effect is very likely driven by tinidazole. This is a plausible market-entry opportunity for a *combination product* rather than a validated mechanistic repurposing of fenticonazole itself.

**To proceed, the following is needed:**
- Fenticonazole monotherapy data (in vitro or clinical) specifically against Trichomonas vaginalis to confirm or refute independent antitrichomonal activity
- Confirmed mechanism of action (MOA) documentation from DrugBank or equivalent source
- India/Taiwan regulatory pathway assessment, since the drug currently holds zero local market authorizations
- Full local prescribing information (warnings, contraindications, drug interactions) — none of this safety data is currently on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

