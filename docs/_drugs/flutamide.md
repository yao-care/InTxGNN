---
layout: default
title: Flutamide
parent: Model Prediction Only (L5)
nav_order: 373
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Flutamide: predicted new indication Prostate cancer/brain cancer susceptibility (evidence level L5). Approved use: Prostate cancer"
monitor_inn: "Flutamide"
predicted_indications: ["prostate cancer/brain cancer susceptibility", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "prostate leiomyoma", "male reproductive organ cancer", "benign prostate phyllodes tumor", "HIV infectious disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome"]
---

# Flutamide
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

# Flutamide: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Flutamide is an oral androgen receptor antagonist originally used to treat prostate cancer.
The TxGNN model's top-ranked prediction is **prostate cancer/brain cancer susceptibility**, but this label appears to be a genetic susceptibility entity rather than a treatable indication, and **no clinical trials or publications** support it.
The broader category of **male reproductive organ cancer** (rank 6) has **43 registered trials and 20 publications**, but these are almost entirely prostate cancer studies, which is the existing indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (from the knowledge graph; the India licence records list no approved indication text) |
| Predicted New Indication | Prostate cancer/brain cancer susceptibility |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (top-ranked prediction); the best-supported category, male reproductive organ cancer, is graded L1 but mainly reflects the existing indication |
| India Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, flutamide is a nonsteroidal androgen receptor antagonist. Its efficacy in prostate cancer is established, and the literature describes it as a "pure antiandrogen" that blocks androgen action in the prostate.

The top-ranked prediction is not a convincing new indication. The prostate cancer component is simply the approved use. The brain cancer susceptibility component has no supporting mechanism, and the label looks like a genetic susceptibility entity rather than a disease that can be treated. The high score most likely reflects closeness to prostate cancer in the knowledge graph.

Several other predictions are also weak. Fibroma of prostate, prostate leiomyoma and benign prostate phyllodes tumor are very rare entities with no trials or literature. Brenner tumor, an ovarian neoplasm, has no known androgen-dependent mechanism. The HIV, simian immunodeficiency virus and feline immunodeficiency predictions have no plausible link to androgen receptor blockade and appear to be graph artifacts.

The more interesting signals are in the benign and prevention settings:
- **Benign reproductive system neoplasm** (rank 4): androgen blockade is plausible for androgen-sensitive benign tumors such as benign prostatic hyperplasia. A 1991 study examined flutamide's effect on prostate volume, PSA and testosterone in such men.
- **Prostatic intraepithelial neoplasia chemoprevention** (within rank 6): a Phase 2 trial tested flutamide as a preventive agent.

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction. The table below shows the most relevant trials from the male reproductive organ cancer category (rank 6), which is dominated by prostate cancer. Flutamide's role in several of these trials is not confirmed.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006214](https://clinicaltrials.gov/study/NCT00006214) | Phase 2 | Completed | 63 | Randomized chemoprevention trial of flutamide in men with prostatic intraepithelial neoplasia; the most direct flutamide-specific trial and a possible new use (prevention) |
| [NCT06601205](https://clinicaltrials.gov/study/NCT06601205) | Phase 2/3 | Completed | 125 | Pre-surgical window-of-opportunity trial of finasteride vs low-dose flutamide vs placebo in prostate cancer |
| [NCT02918968](https://clinicaltrials.gov/study/NCT02918968) | Phase 4 | Completed | 206 | Enzalutamide vs flutamide in castration-resistant prostate cancer after bicalutamide failure |
| [NCT03507608](https://clinicaltrials.gov/study/NCT03507608) | Early Phase 1 | Completed | 25 | Single pulsed-dose flutamide to induce DNA double-strand breaks in prostate cancer with androgen suppression and brachytherapy; exploratory |
| [NCT00003645](https://clinicaltrials.gov/study/NCT00003645) | Phase 3 | Terminated | 64 | Adjuvant leuprolide plus flutamide after prostate surgery in high-risk patients; underpowered |
| [NCT00002597](https://clinicaltrials.gov/study/NCT00002597) | Phase 3 | Completed | 2028 | Radiation therapy with or without antiandrogen therapy (flutamide, goserelin, leuprolide) in locally confined prostate cancer |
| [NCT00104741](https://clinicaltrials.gov/study/NCT00104741) | Phase 3 | Completed | 378 | Triptorelin plus flutamide with radiotherapy in intermediate-risk localized prostate cancer |
| [NCT00003734](https://clinicaltrials.gov/study/NCT00003734) | Phase 3 | Unknown | 276 | 4 vs 8 months of triptorelin plus flutamide before radiotherapy in high-risk localized prostate cancer |
| [NCT00450463](https://clinicaltrials.gov/study/NCT00450463) | Phase 2 | Completed | 64 | PROSTVAC vaccine plus flutamide vs flutamide alone in androgen-insensitive non-metastatic prostate cancer |
| [NCT00003323](https://clinicaltrials.gov/study/NCT00003323) | Phase 2 | Completed | 101 | Flutamide plus finasteride as potency-sparing hormonal therapy for rising PSA after radiation or prostatectomy |

## Literature Evidence

No publications are available for the top-ranked prediction. The table below shows the most relevant publications retrieved for the related categories (male reproductive organ cancer and benign reproductive system neoplasm). No randomized trial publications were retrieved.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8252497](https://pubmed.ncbi.nlm.nih.gov/8252497/) | 1993 | Review (mechanism) | Cancer | Mechanism of action and pure antiandrogenic properties of flutamide; combining it with an LHRH agonist gives maximal prostate inhibition |
| [3071951](https://pubmed.ncbi.nlm.nih.gov/3071951/) | 1988 | Review | Am J Clin Oncol | Rationale for combining a nonsteroidal antiandrogen with an LHRH agonist in prostate cancer |
| [3285484](https://pubmed.ncbi.nlm.nih.gov/3285484/) | 1988 | Review/clinical | Semin Oncol | Advantages of total androgen blockade in advanced prostate cancer |
| [1722793](https://pubmed.ncbi.nlm.nih.gov/1722793/) | 1991 | Clinical study | J Androl | Flutamide (750 mg/day) in men with benign prostatic hyperplasia: effects on prostate volume, PSA and testosterone |
| [1989458](https://pubmed.ncbi.nlm.nih.gov/1989458/) | 1991 | Clinical/histological | Am J Surg Pathol | LHRH agonist plus flutamide pretreatment caused marked atrophy of benign prostate glands in 23 prostatectomies |
| [24950779](https://pubmed.ncbi.nlm.nih.gov/24950779/) | 2014 | Preclinical and Phase 2 | Cancer Prev Res | Flutamide and tissue biomarkers in women at high risk for ovarian cancer |
| [8146068](https://pubmed.ncbi.nlm.nih.gov/8146068/) | 1994 | Preclinical (rat) | Prostate | Early flutamide exposure delayed tumor appearance and reduced growth in a rat prostatic tumor model |
| [20541672](https://pubmed.ncbi.nlm.nih.gov/20541672/) | 2010 | Review | Prog Brain Res | Hormonal therapy of prostate cancer and optimal androgen blockade |
| [29958919](https://pubmed.ncbi.nlm.nih.gov/29958919/) | 2018 | Preclinical/Review | Reprod Toxicol | Effects of flutamide on cell-cell junctions in the testis, epididymis and prostate |
| [7576816](https://pubmed.ncbi.nlm.nih.gov/7576816/) | 1995 | Review (toxicology) | Hum Exp Toxicol | Drug-induced Leydig cell hyperplasia and neoplasia in rats, including flutamide |

## India Market Information

Seven valid single-ingredient registrations exist. All are 250 mg oral tablets supplied as strips of 10. No approved indication text is recorded for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 34456 | Cytomid 250 Tablet (Cipla Ltd) | Strip of 10 tablets | Not recorded |
| 225020 | Ticum 250mg Tablet (Neon Laboratories Ltd) | Strip of 10 tablets | Not recorded |
| 89698 | Flutacare 250mg Tablet (Criticare Laboratories Pvt Ltd) | Strip of 10 tablets | Not recorded |
| 87899 | Flutide 250mg Tablet (Samarth Life Sciences Pvt Ltd) | Strip of 10 tablets | Not recorded |
| 89008 | Flutatec 250mg Tablet (United Biotech Pvt Ltd) | Strip of 10 tablets | Not recorded |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (nonsteroidal antiandrogen), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function (see Safety Considerations); please also refer to the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (disease associations from the knowledge graph, not label text): liver failure, liver disease, gallbladder disease, methemoglobinemia, sulfhemoglobinemia, hyperbilirubinemia (including hereditary forms and Gilbert syndrome), G6PD deficiency, glycogen storage disease, cystinuria, galactosemia, pyruvate dehydrogenase E3 deficiency, and methemoglobinemia due to methemoglobin reductase deficiency.
- **Hepatotoxicity**: the analysis of the HIV prediction notes a boxed warning for hepatotoxicity, and hepatotoxicity also limits use in benign conditions. This should be confirmed against the package insert.
- **Drug interactions**: 285 interactions are recorded. Major interactions include **dolasetron** and **cisapride**. Moderate interactions include famotidine, loperamide, bisacodyl, clarithromycin, levofloxacin, ondansetron, palonosetron, naltrexone and obeticholic acid, as well as several laxatives and bowel-preparation agents (picosulfuric acid, polyethylene glycol, sodium sulfate, lactitol, lactulose, castor oil, glycerin). Metronidazole is a minor interaction.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, prostate cancer/brain cancer susceptibility, has no trials or literature and is not a treatable indication. The trial-rich category of male reproductive organ cancer mostly represents flutamide's existing prostate cancer use, not a new one. The nearest genuine repurposing signals are prostatic intraepithelial neoplasia chemoprevention (NCT00006214) and androgen-sensitive benign prostate conditions, both based on small, older studies. Flutamide's hepatotoxicity and the many drug interactions add further caution.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking data gap for safety screening), including hepatotoxicity monitoring requirements
- Detailed mechanism of action data
- Verification of flutamide's specific role and results in the Phase 3 hormonal therapy trials, and the published outcomes of the Phase 2 chemoprevention trial NCT00006214
- A clearly defined, treatable target indication (for example prostatic intraepithelial neoplasia or benign prostatic conditions) with a comparison against established alternatives such as 5-alpha-reductase inhibitors and alpha-blockers
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

