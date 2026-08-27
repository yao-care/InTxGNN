---
layout: default
title: Daptomycin
parent: 僅模型預測 (L5)
nav_order: 209
evidence_level: L5
indication_count: 10
---

# Daptomycin
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

# Daptomycin: From Gram-Positive Bacterial Infections to Osteoarthritis

> **⚠️ Research Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.

---

## One-Sentence Summary

Daptomycin is a cyclic lipopeptide antibiotic currently approved for serious Gram-positive bacterial infections, including complicated skin and skin structure infections, *Staphylococcus aureus* bacteremia, and right-sided infective endocarditis.
The TxGNN model assigns its highest prediction score to **Osteoarthritis** (score 99.86%), yet a closer review reveals that all 10 supporting publications relate to managing bacterial infections *in* joint-replacement patients—not to treating osteoarthritis itself—suggesting a knowledge-graph context conflation rather than a genuine repurposing signal.
A second-ranked prediction, **Rheumatoid Arthritis** (score 99.84%), carries more credible early-stage mechanistic evidence and is highlighted separately in this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gram-positive bacterial infections (skin/skin structure infections, *S. aureus* bacteremia, right-sided endocarditis) |
| Predicted New Indication | Osteoarthritis (Rank #1 by TxGNN) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 — observational / indirect clinical data only |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Daptomycin is a naturally-derived cyclic lipopeptide antibiotic produced by *Streptomyces roseosporus*. Although detailed MOA data is not available in the current evidence pack, its mechanism is well-characterised in the literature: daptomycin binds to bacterial cell membranes in a calcium-dependent manner, causing rapid membrane depolarisation, loss of intracellular potassium, and eventual cell death. This bactericidal activity is highly selective for Gram-positive organisms and does not extend to mammalian cell membranes at therapeutic concentrations.

Osteoarthritis (OA) is a chronic, degenerative joint disease driven by cartilage degradation, subchondral bone remodelling, and low-grade synovial inflammation—mechanisms that are entirely distinct from bacterial cell-membrane disruption. There is no established pharmacological bridge between daptomycin's antibiotic mechanism and any known OA disease-modifying pathway (e.g., chondroprotection, metalloproteinase inhibition, or RANKL modulation).

The TxGNN high score most likely reflects a **knowledge-graph context conflation**: the graph encodes that daptomycin is used to treat bone and joint infections (prosthetic joint infections, PJIs) in patients who often have underlying OA, creating a semantic proximity between "daptomycin → bone/joint disease" that the model interprets as a repurposing signal. All 10 retrieved publications confirm this pattern—they document daptomycin for treating *infections complicating* joint-replacement surgery, not for treating OA itself.

---

## Clinical Trial Evidence

No clinical trials for Daptomycin in osteoarthritis are currently registered.

---

## Literature Evidence

All retrieved publications relate to treating prosthetic joint infections (PJIs) in orthopaedic patients—not to treating osteoarthritis as a disease entity. This finding reinforces the context-conflation interpretation.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Retrospective Comparative | *J Antimicrob Chemother* | Daptomycin vs. standard therapy for osteoarticular infections (OAIs) associated with *S. aureus* bacteremia |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Case Series | *J Antimicrob Chemother* | Daptomycin efficacy and safety for hip and knee periprosthetic joint infections (PJIs) |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In Vitro Susceptibility Study | *J Antibiotics* | Daptomycin susceptibility of *S. aureus* and *S. epidermidis* from prosthetic joint infections |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Expert Network Survey | *Int J Antimicrob Agents* | Current management practices for PJIs; daptomycin as a preferred agent for MRSA/MSSA PJI |
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Retrospective Multicenter | *Int Orthopaedics* | High-dose daptomycin + rifampicin for Gram-positive osteoarticular infections; safety and efficacy |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Registry Study (EU-CORE) | *Med Clin* | Real-world daptomycin use across European countries including orthopaedic infections |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Microbiological Profile Study | *Surg Infect* | 10-year antibiotic susceptibility trends for staphylococci causing osteoarticular infections |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Retrospective Multicenter | *Int J Antimicrob Agents* | High-dose daptomycin (>6 mg/kg) for complicated bone/joint and implant-associated infections |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Case Report | *Case Rep Orthop* | Septic arthritis masquerading as osteoarthritis; daptomycin used in management |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | Case Report | *ASM Case Reports* | Septic arthritis due to *Corynebacterium propinquum* in a patient with pre-existing joint disease |

---

## India Market Information

Daptomycin is currently not marketed in India and has no registered product licences on file. No authorisation table can be generated.

---

## Notable Secondary Prediction: Rheumatoid Arthritis (Rank #2)

Although the primary focus of this report is the top TxGNN prediction (osteoarthritis), the **rheumatoid arthritis** prediction (TxGNN score 99.84%, rank #2) warrants specific attention as it carries a more credible, though still early-stage, mechanistic rationale.

Two 2025 publications provide direct mechanistic evidence:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39571268](https://pubmed.ncbi.nlm.nih.gov/39571268/) | 2025 | Animal Study (CIA model) | *Int Immunopharmacol* | Daptomycin alleviates collagen-induced arthritis in mice by suppressing TNF-α, IL-1β, IL-6 and inhibiting the NF-κB signalling pathway—first demonstration of anti-RA activity |
| [40923559](https://pubmed.ncbi.nlm.nih.gov/40923559/) | 2025 | In Vitro + Animal Study | *J Med Chem* | Novel daptomycin-derived cyclic lipopeptides with superior anti-RA activity; structural optimisation confirms the anti-inflammatory pharmacophore of the daptomycin scaffold |

**Assessment:** The NF-κB pathway is a central driver of RA pathogenesis, and these findings provide biological plausibility. However, all evidence remains at the animal-model level (Evidence Level L4). No human trials have been initiated. This constitutes a legitimate **Research Question** rather than an actionable repurposing candidate.

---

## Safety Considerations

### Drug–Drug Interactions

12 interactions identified (DDInter database). The most clinically significant are listed below:

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Rosuvastatin | Moderate | Concurrent statin use increases risk of daptomycin-associated myopathy and rhabdomyolysis |
| Simvastatin | Moderate | Same mechanism as above; statin dose reduction or temporary discontinuation recommended |
| Cyclosporine | Moderate | Potential for increased daptomycin plasma levels and additive nephrotoxicity |
| Mycophenolic acid | Moderate | Pharmacokinetic interaction; monitoring advised in immunosuppressed patients |
| Ibuprofen | Moderate | NSAIDs may reduce renal clearance of daptomycin; risk of nephrotoxicity |
| Diclofenac | Moderate | Same mechanism as above |
| Celecoxib | Moderate | Same mechanism as above |
| Ethinylestradiol | Moderate | Potential alteration in hormonal contraceptive efficacy during antibiotic therapy |
| Picosulfuric acid | Moderate | Bowel-preparation context; monitor electrolytes |
| Iobenguane (I-131) | Moderate | Potential interference with radioiodine uptake in diagnostic/therapeutic settings |
| Warfarin | Minor | Minor effect on anticoagulation; INR monitoring advisable |
| Dicoumarol | Minor | Similar to warfarin; minor interaction |

> **Critical Note (Gout Safety Signal):** A published case report ([PMID 36693494](https://pubmed.ncbi.nlm.nih.gov/36693494/), 2023) documents daptomycin-induced rhabdomyolysis leading to acute gouty arthritis via hyperuricaemia. This is an adverse drug reaction, not a repurposing opportunity. The TxGNN rank-4 "gout" prediction (score 99.79%) should be interpreted as a **safety hazard signal**, not as therapeutic potential.

Please refer to the package insert for full warnings and contraindications, which were not available in the current evidence pack.

---

## Comprehensive Prediction Landscape

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|---------------------|------------|----------------|-----------|
| 1 | Osteoarthritis | 99.86% | L4 | ⛔ Context conflation — all evidence is PJI management, not OA treatment |
| 2 | Rheumatoid Arthritis | 99.84% | L4 | 🔬 Research Question — animal model mechanistic evidence (NF-κB pathway) |
| 3 | Osteoarthritis Susceptibility | 99.79% | L5 | ⛔ Semantic drift — literature addresses infection susceptibility, not OA genetics |
| 4 | Gout | 99.79% | L5 | ⚠️ Adverse effect signal — daptomycin *causes* gout via rhabdomyolysis |
| 5–10 | Rare skeletal dysplasias (pseudoachondroplasia, brachyolmia, brachydactyly-syndactyly, etc.) | 99.47–99.74% | L5 | ⛔ KG skeletal disease cluster effect — zero literature, no mechanistic basis |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction (osteoarthritis, score 99.86%) is a false-positive driven by knowledge-graph semantic proximity between daptomycin's antibiotic use in orthopaedic infections and the underlying OA diagnosis in those patients. There is no mechanistic pathway connecting daptomycin to OA treatment, and none of the 10 retrieved publications support osteoarthritis as a therapeutic indication. The gout prediction (rank 4) represents an active safety warning rather than a repurposing opportunity.

**The one signal worth monitoring is:**
The rheumatoid arthritis prediction, which has preliminary but biologically coherent evidence from two 2025 animal studies demonstrating NF-κB-mediated anti-inflammatory effects.

**To proceed further with the RA research question, the following steps are needed:**

- [ ] Confirm daptomycin MOA data from DrugBank to characterise the anti-inflammatory pharmacophore
- [ ] Retrieve CDSCO (India) and global package insert data for complete warning and contraindication profiles
- [ ] Commission or identify *in vitro* human synoviocyte/macrophage studies to validate NF-κB pathway inhibition in human cell lines
- [ ] Assess whether IV-only administration route is compatible with a chronic RA treatment paradigm (oral bioavailability is negligible)
- [ ] Design a Phase 0/1 translational study protocol if preclinical human-cell evidence is confirmed
- [ ] Conduct a formal statin co-medication risk assessment given the myopathy interaction profile, relevant for RA patients on concomitant lipid-lowering therapy

---

*Report generated: 2026-04-04 | Evidence Pack: TW-DB00080-multi v4 | Data cutoff: 2026-04-04*
*For research use only. All repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

