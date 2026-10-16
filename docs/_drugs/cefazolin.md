---
layout: default
title: Cefazolin
parent: Moderate Evidence (L3-L4)
nav_order: 152
evidence_level: L4
indication_count: 8
last_modified_at: 2026-10-14
description: "Cefazolin: predicted new indication Infectious otitis media (evidence level L4). Approved use: Bacterial pneumonia"
---

# Cefazolin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **8** 
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

# Cefazolin: From Bacterial Pneumonia to Infectious Otitis Media

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic, originally used for bacterial infections such as bacterial, streptococcal and staphylococcal pneumonia, endocarditis, bacterial arthritis and cholangitis.
The TxGNN model predicts it may be effective for **infectious otitis media**, but there are **no registered clinical trials** and only **2 loosely related publications** (a case report and an unrelated review) supporting this direction.
The evidence is therefore mostly model-driven and indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial pneumonia (the Indian licence records contain no approved indication text; this comes from the knowledge-graph indication list) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the compiled data. Based on general pharmacological knowledge, cefazolin is a beta-lactam antibiotic that inhibits bacterial cell wall synthesis. It is active against gram-positive organisms such as streptococci and methicillin-susceptible staphylococci. Its efficacy in respiratory and other bacterial infections is established, and mechanistically it may be applicable to otitis media.

Otitis media is often caused by streptococci and staphylococci, so the original indications (streptococcal and staphylococcal pneumonia) and the predicted indication share relevant pathogens. This pathogen overlap probably explains the high model score.

There are important limitations. Cefazolin has limited gram-negative and *Haemophilus* coverage, and it is available only as an injection, with limited middle-ear penetration. The only direct support is a 2025 case report of ceftazidime-cefazolin empiric therapy in pediatric Gradenigo syndrome (a complication of otitis media), where the effect cannot be attributed to cefazolin alone.

Other otitis-related predictions (suppurative otitis media, chronic otitis media, middle ear disease) show similar patterns. Suppurative otitis media has the most relevant human evidence, a 1982 comparative study of cefmetazole versus cefazolin. Non-suppurative and allergic otitis media have little antibacterial rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case report/Case series | Ann Otol Rhinol Laryngol | Ceftazidime-cefazolin empiric therapy in pediatric Gradenigo syndrome, a complication of acute otitis media; effect of cefazolin alone cannot be separated |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Review | Clin Pharm | Management of Stevens-Johnson syndrome; otitis media is mentioned only as the original illness in one patient, so it is not relevant to cefazolin efficacy |

**Related evidence for other predicted ear indications (for context):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6752467](https://pubmed.ncbi.nlm.nih.gov/6752467/) | 1982 | Comparative clinical study | Jpn J Antibiot | Cefmetazole vs cefazolin in suppurative otitis media (172 patients analysed for efficacy); the only human comparative data, old and of limited verifiability |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 169724 | Ozolin 500mg Injection | Vial of 1 powder for injection | Not specified in the data |
| 14583 | Alcizon 250mg Injection | Vial of 1 injection | Not specified in the data |
| 45152 | Cefadin 1000mg Injection | Vial of 1 injection | Not specified in the data |
| 185235 | Reflin 1gm Injection | Vial of 5 ml injection | Not specified in the data |
| 44638 | Cezolin 500mg Injection | Vial of 1 injection | Not specified in the data |

Twenty valid single-ingredient licences are registered in total, all injectable forms and none cancelled.

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** blood coagulation disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, congenital prothrombin deficiency.
- **Drug Interactions:** 112 interactions recorded. Moderate-level ones include aminoglycosides (kanamycin, neomycin, streptomycin) and picosulfuric acid. Others (e.g. amphotericin B, epinephrine, metformin, omeprazole, aspirin) are of unknown severity.

Please also refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (99.44%), but there are no registered trials and the available literature is indirect, a single confounded case report combined with another antibiotic. Cefazolin's spectrum and injection-only route are poorly matched to typical otitis media pathogens and treatment settings. The otitis media group of predictions largely overlaps with graph proximity rather than independent evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator (currently missing and blocking safety screening)
- Mechanism of action data from DrugBank
- Review of the 1982 suppurative otitis media comparison to see whether it reports usable cefazolin efficacy data
- Modern pathogen susceptibility data for otitis media and a route-of-administration assessment
- If pursued, suppurative otitis media is the more promising target to investigate first, as it has the strongest human evidence (Evidence Level L3)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

