---
layout: default
title: Sulbactam
parent: 僅模型預測 (L5)
nav_order: 788
evidence_level: L5
indication_count: 1
---

# Sulbactam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Sulbactam: From Bacterial Infections to Bacterial Arthritis

## One-Sentence Summary

Sulbactam is a beta-lactamase inhibitor conventionally combined with ampicillin (ampicillin/sulbactam) for treatment of susceptible bacterial infections.
The TxGNN model predicts it may be effective for **Bacterial Arthritis**,
with **no registered clinical trials** but **20 supporting publications**, several of which directly describe ampicillin/sulbactam use in septic arthritis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No India-approved indication on record — Sulbactam is not individually marketed in India; it is conventionally combined with ampicillin for susceptible bacterial infections |
| Predicted New Indication | Bacterial Arthritis |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L3 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Sulbactam is not available. Based on known pharmacology, Sulbactam is a beta-lactamase inhibitor typically administered together with ampicillin (as ampicillin/sulbactam), which extends ampicillin's spectrum to cover beta-lactamase-producing Gram-positive and Gram-negative organisms as well as anaerobes. Its efficacy in treating susceptible bacterial infections is well established through decades of clinical use.

Bacterial (septic) arthritis is itself a bacterial infection — specifically, a joint-space infection caused by organisms such as *Staphylococcus aureus*, *Streptococcus* spp., and *Haemophilus influenzae*, all of which fall within the treatment spectrum of ampicillin/sulbactam. In this sense, the "new" indication is less a mechanistic leap and more a specific anatomical manifestation of the drug's already-established antibacterial activity.

This is reinforced by the literature: publications dating from 1986 through 2024 document ampicillin/sulbactam being used specifically for septic arthritis and osteomyelitis in both pediatric and adult populations, including randomized comparative studies against cefotaxime and ceftriaxone. This long clinical track record supports the biological plausibility of the TxGNN prediction, even though no dedicated randomized trial has evaluated Sulbactam solely for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3026009](https://pubmed.ncbi.nlm.nih.gov/3026009/) | 1986 | RCT | Reviews of Infectious Diseases | Open, randomized comparative trial: sulbactam/ampicillin vs. cefotaxime for bone, joint, and soft-tissue infections; comparable clinical cure rates at 2-week follow-up |
| [2677956](https://pubmed.ncbi.nlm.nih.gov/2677956/) | 1989 | RCT | The Pediatric Infectious Disease Journal | Randomized 2:1 comparison of ampicillin/sulbactam vs. ceftriaxone in children with suppurative arthritis and osteomyelitis; *S. aureus* and *S. pyogenes* most common pathogens |
| [1745624](https://pubmed.ncbi.nlm.nih.gov/1745624/) | 1991 | Review | Pharmacotherapy | Reviews in vitro activity and clinical efficacy of ampicillin-sulbactam vs. ticarcillin-clavulanate against beta-lactamase-producing pathogens |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Review | International Journal of Antimicrobial Agents | Review of off-label/formal use of conventional and novel antibiotics (including sulbactam-based combinations) against multidrug-resistant Gram-positive and Gram-negative infections |
| [3026018](https://pubmed.ncbi.nlm.nih.gov/3026018/) | 1986 | Case series | Reviews of Infectious Diseases | Sequential parenteral sulbactam/ampicillin then oral sultamicillin in 9 children with osteomyelitis/septic arthritis; all susceptible pathogens cleared |
| [3252119](https://pubmed.ncbi.nlm.nih.gov/3252119/) | 1988 | Case series | Mikrobiyoloji Bulteni | 84 patients with various infections, including 5 with septic arthritis/osteomyelitis, treated with parenteral ampicillin/sulbactam with favorable outcomes |
| [16269877](https://pubmed.ncbi.nlm.nih.gov/16269877/) | 2005 | Observational study | Acta Orthopaedica et Traumatologica Turcica | Clinical/laboratory characterization of septic arthritis across age groups, establishing initial empiric antibiotic protocol |
| [9263167](https://pubmed.ncbi.nlm.nih.gov/9263167/) | 1997 | Case report | The Journal of Rheumatology | *Pasteurella multocida* septic arthritis after cat bite successfully treated with ampicillin/sulbactam plus joint aspiration |
| [16148860](https://pubmed.ncbi.nlm.nih.gov/16148860/) | 2005 | Case report | The Pediatric Infectious Disease Journal | *Fusobacterium necrophorum* septic arthritis in a child; recurrence despite ampicillin-sulbactam required escalation to meropenem/clindamycin |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Observational study | Clinical Laboratory | Pathogen distribution and antimicrobial resistance patterns in pediatric bone and joint infections, informing empiric beta-lactam/beta-lactamase-inhibitor selection |

---

## India Market Information

Currently no marketing authorization registered in India.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Sulbactam has no marketing authorization in India, and critical safety data (contraindications, warnings, local label text) remains an unresolved blocking gap, preventing safety evaluation. While the TxGNN score is high and decades of literature (including two randomized comparative trials) support ampicillin/sulbactam's real-world use in septic/bacterial arthritis, the lack of registered clinical trials specific to this indication and the absence of India market presence limit near-term actionability.

**To proceed, the following is needed:**
- India-specific package insert/label documentation to resolve the blocking safety data gap (DG001)
- Formal mechanism of action documentation from DrugBank (DG002)
- Assessment of regulatory pathway/feasibility for registering a currently non-marketed drug in India
- Search for any registered interventional trials (ClinicalTrials.gov/ICTRP) evaluating ampicillin/sulbactam specifically for septic/bacterial arthritis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

