---
layout: default
title: Polidocanol
parent: Model Prediction Only (L5)
nav_order: 683
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Polidocanol: predicted new indication Esophageal varices with bleeding (evidence level L5). Approved use: Varicose disease"
---

# Polidocanol
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

# Polidocanol: From Varicose Disease to Esophageal Varices with Bleeding

## One-Sentence Summary

Polidocanol is an injectable sclerosing agent, originally used to treat varicose disease (varicose veins).
The TxGNN model predicts it may be effective for **esophageal varices with bleeding**,
and although **no registered clinical trials** were found, **20 publications** (including several randomized trials) currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Varicose disease (from the knowledge graph; no approved indication text in the India licence records) |
| Predicted New Indication | Esophageal varices with bleeding |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 (based on the supplied scoring; supported by randomized trials in the literature, with no registered trials) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, polidocanol is a sclerosing agent that damages the vascular endothelium, causing thrombosis and fibrosis of the vessel. Its efficacy in varicose veins is established.

Esophageal varices are also dilated veins. The same endothelial sclerosing effect applies directly to endoscopic injection sclerotherapy, in which the drug is injected into or beside the varix to obliterate it. This is why the literature shows decades of use of polidocanol for variceal bleeding.

Some guardrails apply. Sclerotherapy is associated with esophageal stricture, dysphagia and ulceration. Current practice often favors endoscopic band ligation as first-line treatment, so polidocanol is best positioned as an alternative or adjunct (for example, combined with ligation or cyanoacrylate).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9255525](https://pubmed.ncbi.nlm.nih.gov/9255525/) | 1997 | RCT | Endoscopy | Prospective study of cyanoacrylate plus polidocanol versus polidocanol alone for bleeding esophageal varices in unselected cirrhosis patients |
| [10385713](https://pubmed.ncbi.nlm.nih.gov/10385713/) | 1999 | RCT | Gastrointest Endosc | Ligation versus combined ligation and sclerotherapy for bleeding esophageal varices |
| [3069543](https://pubmed.ncbi.nlm.nih.gov/3069543/) | 1988 | RCT / comparative | Gastroenterol Clin Biol | Intravariceal polidocanol versus perivariceal quinine-urea in 74 patients with bleeding varices |
| [2693076](https://pubmed.ncbi.nlm.nih.gov/2693076/) | 1989 | Randomized trial | Endoscopy | Ethanolamine versus polidocanol in 50 cirrhotic patients; eradication 81% vs 64% (not significant) |
| [10434360](https://pubmed.ncbi.nlm.nih.gov/10434360/) | 1999 | Comparative | J UOEH | Ligation (101 patients) versus polidocanol sclerotherapy (40 patients); hemostasis 100% in both, rebleeding 40.0% vs 29.6% |
| [3262931](https://pubmed.ncbi.nlm.nih.gov/3262931/) | 1988 | Prospective cohort | Surg Endosc | Immediate endoscopic sclerosis in 232 consecutive patients with variceal bleeding |
| [36509625](https://pubmed.ncbi.nlm.nih.gov/36509625/) | 2023 | Cohort | Arch Pediatr | Polidocanol sclerotherapy for cardiac varices in children and adolescents |
| [29473522](https://pubmed.ncbi.nlm.nih.gov/29473522/) | 2017 | Review | Curr Clin Pharmacol | Evidence-based review of off-label uses of polidocanol |
| [32517718](https://pubmed.ncbi.nlm.nih.gov/32517718/) | 2020 | Systematic review | BMC Gastroenterol | Rebleeding risk after initial cyanoacrylate treatment of gastroesophageal varices |
| [6609102](https://pubmed.ncbi.nlm.nih.gov/6609102/) | 1984 | Cohort / safety report | Gut | Stricture or dysphagia in 20 of 34 patients (59%) after polidocanol (3%) sclerotherapy |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 702 | Asklerol 3% Injection | Vial of 2 ml injection | Not stated in the available records |
| 218882 | Troydoca 30mg Injection | Vial of 2 ml injection | Not stated in the available records |

## Safety Considerations

- **Procedure-related risks (from the literature)**: Esophageal stricture or dysphagia occurred in 59% of patients (20 of 34) after repeated endoscopic polidocanol sclerotherapy (PMID 6609102). Sclerotherapy may also cause ulceration, and one study noted it can aggravate portal hypertension by suppressing portosystemic shunts (PMID 2344911).

Please refer to the package insert for other safety information, including warnings, contraindications and drug interactions.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several randomized trials and comparative studies describe polidocanol sclerotherapy for bleeding esophageal varices, with a plausible mechanism shared with its approved use. However, no registered trials exist, the studies are mostly older, and band ligation is generally preferred first-line, so polidocanol is better positioned as an alternative or adjunct.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed Indian products, and confirmation of their approved indications
- Detailed mechanism of action data from DrugBank
- Confirmation that the marketed injection and its labelling suit endoscopic use in the esophagus, since the Indian products are vials of 2 ml injection with no stated indication
- Contemporary comparative data against band ligation, and combination use with ligation or cyanoacrylate
- A monitoring plan for stricture, dysphagia and ulceration

**Other predictions:**
- Esophageal varices without bleeding (score 99.95%): Research Question. The evidence for prevention is indirect, and guidelines favor beta-blockers or band ligation.
- The remaining eight predictions (for example, immunoerythromyeloid hypoplasia, retinal and cone disorders, and monosomy X) have no trials, no literature and no plausible mechanistic link. They are Hold and are likely graph artifacts.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

