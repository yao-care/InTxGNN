---
layout: default
title: Daptomycin
parent: Moderate Evidence (L3-L4)
nav_order: 233
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Daptomycin: predicted new indication Osteoarthritis (evidence level L4). Approved use: Gram-positive bacterial infections"
monitor_inn: "Daptomycin"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "osteoarthritis susceptibility", "gout", "pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome"]
---

# Daptomycin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Daptomycin: From Gram-Positive Bacterial Infections to Osteoarthritis

## One-Sentence Summary

Daptomycin is a cyclic lipopeptide antibiotic marketed in India as an injectable for Gram-positive bacterial infections.
The TxGNN model predicts it may be effective for **Osteoarthritis**, but there are **no registered clinical trials** and the **10 publications** retrieved concern joint *infections*, not osteoarthritis itself.
This prediction is best viewed as a model artefact rather than a genuine repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gram-positive bacterial infections (the approved indication text is not recorded in the licence data compiled for this report; this is based on the known antibacterial use of the drug) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, daptomycin is a cyclic lipopeptide antibiotic with activity against Gram-positive bacteria, and its efficacy in bacterial infections is established.

For osteoarthritis, however, no mechanistic link has been established. The retrieved literature covers daptomycin as an antibacterial treatment for osteoarticular and prosthetic joint infections caused by organisms such as *Staphylococcus*. These are infectious conditions, not degenerative osteoarthritis. The high TxGNN score most likely reflects the graph proximity of joint-related terms, not a true therapeutic signal.

**Other predictions worth noting:**
- **Rheumatoid arthritis** (score 99.84%): this is the only prediction with a plausible hypothesis. A 2025 animal study (PMID 39571268) reported that daptomycin alleviated collagen-induced arthritis by suppressing inflammatory cytokines and the NF-κB pathway, and a follow-up study (PMID 40923559) tested derived lipopeptides. The evidence is preclinical only (Level L4), with no human data. It is better treated as a research question than as a candidate for development.
- **Gout** (score 99.79%): the only report describes daptomycin-induced rhabdomyolysis complicated by acute gouty arthritis. This is an adverse-event signal and potentially harmful.
- **Rare skeletal dysplasias and genetic syndromes** (ranks 5–10, such as pseudoachondroplasia and brachyolmia): prediction only, with no literature and no plausible mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Cohort | Int Orthop | Safety and efficacy of high-dose daptomycin plus rifampicin in Gram-positive osteoarticular infections (infection, not osteoarthritis) |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Cohort | J Antimicrob Chemother | Daptomycin versus standard therapy for osteoarticular infections with *S. aureus* bacteraemia |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Cohort | J Antimicrob Chemother | Clinical experience with daptomycin in knee and hip periprosthetic joint infections |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Cohort | Int J Antimicrob Agents | High-dose daptomycin (>6 mg/kg) for complicated bone, joint and implant-associated infections |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Cohort | Med Clin (Barc) | Spanish experience with daptomycin from the EU-CORE registry |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In vitro | J Antibiot | Susceptibility of *S. aureus* and *S. epidermidis* from prosthetic joint infections |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Cohort | Surg Infect | Ten-year evolution of staphylococcal profiles in osteoarticular infections |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Survey | Int J Antimicrob Agents | Survey of current practice in managing prosthetic joint infections |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Case report | Case Rep Orthop | Chronic *Corynebacterium striatum* septic arthritis in a patient with known osteoarthritis |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | Case report | ASM Case Rep | Septic arthritis due to *Corynebacterium propinquum* in a native joint |

None of these studies tests daptomycin as a treatment for osteoarthritis.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 64994 | Daptocure 350mg Injection (Emcure) | Vial of 1 injection | Not recorded |
| 60273 | Dapmicin 350mg Injection (Glenmark) | Vial of 1 injection | Not recorded |
| 64857 | Daptovan 350mg Injection (German Remedies) | Vial of 1 injection | Not recorded |
| 61793 | Dapute 350mg Injection (Concord Biotech) | Vial of 1 injection | Not recorded |
| 63125 | Daptobio 350mg Injection (Biocon) | Vial of 1 injection | Not recorded |

Eight valid single-ingredient licences exist in total (the three others are Cubicin by Novartis India, Ivdapt by Fusion Healthcare and Daptojub by Jubilant). All are injectables.

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these are graph associations, not label text): myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, diarrhoeal disease, *Clostridium difficile* colitis, perinatal necrotising enterocolitis, eosinophilic pneumonia, pulmonary eosinophilia, peripheral neuropathy and peripheral nervous system disease.
- **Muscle toxicity**: a published case describes daptomycin-induced rhabdomyolysis followed by acute gouty arthritis (PMID 36693494).
- **Drug interactions** (12 recorded):
  - Moderate: picosulfuric acid, rosuvastatin, simvastatin, iobenguane (I-131), ibuprofen, diclofenac, ethinylestradiol, celecoxib, cyclosporine, mycophenolic acid. Statins are of particular note given the myopathy and rhabdomyolysis risk.
  - Minor: dicoumarol, warfarin.
- Package insert warnings and contraindications were not available for this report; please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The osteoarthritis prediction has no clinical trials and no supporting literature. The retrieved papers describe joint infections, not degenerative joint disease. The only scientifically interesting lead is rheumatoid arthritis, which rests on animal data alone. Using an antibiotic of last resort in a chronic non-infectious condition also raises concerns about resistance and long-term muscle toxicity.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- For the rheumatoid arthritis hypothesis: confirmatory preclinical studies, dose translation for an immunomodulatory effect, and a safety and resistance-risk assessment
- Approved indication text for the Indian licences, to confirm the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

