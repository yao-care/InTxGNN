---
layout: default
title: Artemether
parent: Model Prediction Only (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Artemether: predicted new indication Acquired angioedema (evidence level L5). Approved use: Not stated in the licence records compiled for this report (artemethe…"
monitor_inn: "Artemether"
predicted_indications: ["acquired angioedema", "Plasmodium falciparum malaria", "angioedema", "hereditary angioedema", "nephrogenic syndrome of inappropriate antidiuresis", "acute contagious conjunctivitis", "scleroderma (disease)", "conjunctivitis", "renin-angiotensin-aldosterone system-blocker-induced angioedema"]
---

# Artemether
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

## Artemether: From Malaria Treatment to Acquired Angioedema (Top Prediction) — and the Malaria Indication Behind the Evidence
{: .text-alpha }

> **Note on the target indication.** The top-ranked TxGNN prediction (acquired angioedema) has no supporting trials or literature. The only predictions with real evidence (P. falciparum malaria and malaria) describe artemether's established use, not a new one. This report therefore covers the top-ranked prediction in the overview and uses the best-supported prediction (P. falciparum malaria) for the evidence sections.

## One-Sentence Summary

Artemether is an artemisinin-derivative antimalarial, used mainly in a fixed-dose combination with lumefantrine for uncomplicated falciparum malaria.
The TxGNN model's top-ranked prediction is **acquired angioedema** (score 99.90%), but it has **0 clinical trials and 0 publications** and no plausible mechanism. The best-supported prediction, **Plasmodium falciparum malaria**, is an established indication with **33 registered trials** and **20 publications**, so it is not a true repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records compiled for this report (artemether is used for malaria) |
| Predicted New Indication | Acquired angioedema (rank 1); P. falciparum malaria (rank 2) is an established use |
| TxGNN Prediction Score | 99.90% (acquired angioedema); 99.77% (P. falciparum malaria) |
| Evidence Level | L5 for acquired angioedema; L1 for P. falciparum malaria |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold for acquired angioedema; Proceed with Guardrails for malaria (established use) |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled records. From general knowledge, artemether is an artemisinin derivative activated by heme iron, which generates free radicals that damage parasite proteins. It is used with lumefantrine as first-line therapy for uncomplicated P. falciparum malaria.

For **acquired angioedema** and the other angioedema entries (angioedema, hereditary angioedema, RAAS-blocker-induced angioedema), no mechanistic link was found. Artemether is not known to act on the kallikrein-kinin pathway or on C1-inhibitor biology. These high scores most likely reflect shared neighbours in the knowledge graph rather than real biology, and the model's confidence should not be read as clinical promise.

The other low-evidence predictions (nephrogenic syndrome of inappropriate antidiuresis, acute contagious conjunctivitis, conjunctivitis) also lack any supporting mechanism or data. Scleroderma has only loose preclinical anti-fibrotic reports for artemisinins, which is speculative.

The **malaria** predictions reflect the drug's existing use. They confirm that the model recovers known biology but do not suggest a new indication.

## Clinical Trial Evidence

Trials below are for P. falciparum malaria, the only prediction with trial data. The top 10 most relevant are shown.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00422084](https://clinicaltrials.gov/study/NCT00422084) | Phase 3 | Completed | 1272 | Double-blind comparison of pyronaridine-artesunate versus artemether-lumefantrine in children and adults |
| [NCT01082705](https://clinicaltrials.gov/study/NCT01082705) | Phase 3 | Completed | 323 | In vivo efficacy of artemisinin combination therapies in Tanzanian children |
| [NCT00677833](https://clinicaltrials.gov/study/NCT00677833) | Phase 2/3 | Completed | 361 | Azithromycin plus chloroquine versus artemether-lumefantrine in African children |
| [NCT05951595](https://clinicaltrials.gov/study/NCT05951595) | Phase 3 | Recruiting | 1680 | Triple therapy (artemether-lumefantrine-amodiaquine) versus first-line combinations |
| [NCT02020330](https://clinicaltrials.gov/study/NCT02020330) | Phase 3 | Completed | 150 | 3-day versus 5-day artemether-lumefantrine in Myanmar |
| [NCT00529867](https://clinicaltrials.gov/study/NCT00529867) | Phase 4 | Completed | 267 | Suspension versus tablets in Kenyan children under five |
| [NCT01017770](https://clinicaltrials.gov/study/NCT01017770) | Phase 4 | Completed | 340 | Artemether-lumefantrine versus artesunate-amodiaquine in Burkina Faso |
| [NCT03453840](https://clinicaltrials.gov/study/NCT03453840) | Phase 4 | Completed | 305 | Extended-duration regimen in children, including HIV-infected children on efavirenz |
| [NCT02637128](https://clinicaltrials.gov/study/NCT02637128) | Phase 4 | Completed | 452 | In vivo efficacy in Malawi |
| [NCT01998295](https://clinicaltrials.gov/study/NCT01998295) | Phase 4 | Completed | 45 | Parasite clearance time in Tanzanian children |

For acquired angioedema and the other non-malaria predictions, currently no related clinical trials are registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33957925](https://pubmed.ncbi.nlm.nih.gov/33957925/) | 2021 | Systematic review/meta-analysis | Malaria Journal | Efficacy and safety of artemether-lumefantrine in Ethiopia |
| [22548983](https://pubmed.ncbi.nlm.nih.gov/22548983/) | 2012 | Systematic review | Malaria Journal | Safety and efficacy in pregnancy |
| [35271592](https://pubmed.ncbi.nlm.nih.gov/35271592/) | 2022 | Systematic review/meta-analysis | PLoS One | Efficacy of three ACTs in Sub-Saharan Africa |
| [34983552](https://pubmed.ncbi.nlm.nih.gov/34983552/) | 2022 | Systematic review/meta-analysis | Malaria Journal | Safety of dihydroartemisinin-piperaquine versus artemether-lumefantrine in African children |
| [31210357](https://pubmed.ncbi.nlm.nih.gov/31210357/) | 2019 | Cochrane review | Cochrane Database Syst Rev | Intramuscular artemether versus quinine and artesunate in severe malaria |
| [17402835](https://pubmed.ncbi.nlm.nih.gov/17402835/) | 2007 | Review | Expert Rev Anti Infect Ther | Artesunate, artemether or quinine in severe malaria |
| [1346408](https://pubmed.ncbi.nlm.nih.gov/1346408/) | 1992 | RCT | Lancet | Artemether versus chloroquine in Gambian children with severe malaria |
| [40845863](https://pubmed.ncbi.nlm.nih.gov/40845863/) | 2026 | Randomised phase 4 trial | Lancet Infect Dis | Efficacy of four ACTs in Ugandan children, with concern about waning ACT efficacy in east Africa |
| [40138574](https://pubmed.ncbi.nlm.nih.gov/40138574/) | 2025 | Resistance marker study | J Infect Dis | Artemether-lumefantrine treatment selects pfmdr1 copy-number increase in African infections |
| [38741101](https://pubmed.ncbi.nlm.nih.gov/38741101/) | 2024 | Therapeutic efficacy study | Malaria Journal | Efficacy and tolerability in Niger, 2020 |

For acquired angioedema and the other non-malaria predictions, currently no related literature is available.

## India Market Information

All 20 registrations are valid single-ingredient licences. The compiled records contain no approved-indication text. The first five are listed.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 188232 | Rezatrin 80 mg/480 mg Tablet | Strip of 6 tablets | Not stated |
| 231992 | Ufither L 80mg/480mg Tablet | Strip of 6 tablets | Not stated |
| 157460 | Numal Forte Oral Suspension | Bottle of 30 ml oral suspension | Not stated |
| 101327 | Gnate L Syrup | Bottle of 30 ml syrup | Not stated |
| 190805 | Rezart M 80mg Injection | Vial of 1 ml injection | Not stated |

Other formulations on the market include dispersible tablets, dry syrups, capsules and ampoule injections.

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): long QT syndrome, familial long QT syndrome, torsades de pointes, and potassium deficiency disease. These relate to QT-prolongation risk, and a Phase 1 QT study (NCT01103830) exists in the trial data.
- **Drug Interactions**: 95 interactions are recorded. Major interactions include clarithromycin, cobicistat, amprenavir, apalutamide, atazanavir and boceprevir. Moderate interactions include dexamethasone, miconazole, troglitazone, deferasirox, bosentan and bexarotene. Many involve CYP3A4 induction or inhibition. Trial and literature data also point to interactions with antiretrovirals such as dolutegravir, nevirapine and efavirenz.
- **Resistance**: Emerging artemisinin partial resistance and pfmdr1 selection are reported in Africa.

Please refer to the package insert for label warnings and contraindications, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold (acquired angioedema and other non-malaria predictions); Proceed with Guardrails (malaria, established indication only)**

**Rationale:**
The top-ranked prediction, acquired angioedema, rests on a graph-based score alone, with no trials, no literature and no plausible mechanism, so it should not advance. The malaria predictions have strong L1 evidence, but they describe the drug's existing use rather than a repurposing opportunity.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator (currently missing)
- Mechanism of action data from DrugBank
- For angioedema: any biological rationale (preclinical or mechanistic) before further consideration
- For malaria use: monitoring for artemisinin partial resistance and pfmdr1 selection, QT-risk assessment, and a DDI management plan (especially with antiretrovirals and CYP3A4 modulators)
- Separate uncomplicated from severe malaria in any plan, since IV artesunate is preferred over intramuscular artemether for severe disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

